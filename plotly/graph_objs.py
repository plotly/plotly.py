"""
graph_objs
==========

A module that understands plotly language and can manage the json
structures. This module defines two base classes: PlotlyList and PlotlyDict.
The former is a generic container inheriting from `list` and the latter
inherits from `dict` and is used to contain all information for each part of
a plotly figure.

Development rules:

* A dict/list with the same entries as a PlotlyDict/PlotlyList should look
exactly the same once a call is made to plot.

* Only mutate object structure when users ASK for it.

* It should always be possible to get a dict/list JSON representation from a
graph_objs object and it should always be possible to make a graph_objs object
from a dict/list JSON representation.

"""
from . graph_objs_meta import INFO
from . exceptions import InvalidListItemError, InvalidKeyError

# TODO: BIG ONE, how should exceptions bubble up in this inheritance scheme?
# TODO: related, WHAT exceptions should bubble up?
# TODO: slap users on the wrist if they instantiate PlotlyDict/List or Trace?


class DictMeta(type):
    """A meta class for PlotlyDict class creation.

    The sole purpose of this meta class is to properly create the __doc__
    attribute so that running help(*), where * is a subclass of PlotlyDict,
    will return information about key-value pairs for that object.

    """
    def __new__(mcs, name, bases, attrs):
        kind = name.lower()
        doc = "\n".join([line.lstrip()
                         for line in attrs['__doc__'].splitlines()])
        if 'valid' in INFO[kind]:
            if len(INFO[kind]['valid']):
                doc += "Valid keys:\n\n"
                for key in INFO[kind]['valid']:
                    types = INFO[kind]['types'][key]
                    descriptor = INFO[kind]['descriptors'][key]
                    doc += "\t{} ({}): \n\t\t{}\n".format(key,
                                                          types,
                                                          descriptor)
        attrs['__doc__'] = doc.expandtabs(4)
        return super(DictMeta, mcs).__new__(mcs, name, bases, attrs)


class PlotlyList(list):
    """A container for PlotlyDicts, inherits from standard list.

    Plotly uses lists and dicts as collections to hold information about a
    figure. This container is simply a list that understands some plotly
    language and apes the methods in a PlotlyDict, passing them on to its
    constituents.

    It can be initialized like any other list so long as the entries are all
    PlotlyDict objects or subclasses thereof.

    Any available methods that hold for a list object hold for a PlotlyList.

    Validation checking is preformed upon instantiation.

    """
    def __init__(self, *args):
        super(PlotlyList, self).__init__(*args)
        self.to_graph_objs()
        self.validate()  # TODO: IF this checks for missing, this is wrong here!

    def _get_class_name(self):
        return self.__class__.__name__.lower()

    def clean(self):  # TODO: is this a bit too dangerous for users?
        del_indicies = [index for index, entry in self
                        if not isinstance(entry, PlotlyDict)]
        for index in del_indicies:
            del self[index]
        for plotly_dict in self:
            plotly_dict.clean()

    def get_json(self):
        self.to_graph_objs()
        l = [plotly_dict.get_json() for plotly_dict in self]
        return l

    def to_graph_objs(self):  # TODO: PlotlyList([{}]) == PlotlyList([Trace()])?
        for index, entry in enumerate(self):
            if isinstance(entry, PlotlyDict):
                entry.to_graph_objs()
            elif isinstance(entry, dict):
                try:
                    obj_type = entry['type']
                    try:
                        _class = TYPE_TO_CLASS[obj_type]
                        self[index] = _class(**entry)
                        # TODO: explicitly call for a new to_graphs?
                    except KeyError:
                        raise InvalidListItemError("Entry had invalid 'type'")
                except KeyError:
                    raise InvalidListItemError("Entry didn't have key: 'type'")
            else:
                raise InvalidListItemError("Invalid entry, {}".format(entry))

    def strip_style(self):
        self.to_graph_objs()
        for plotly_dict in self:
            plotly_dict.strip_style()

    def validate(self):  # TODO: should this check for MISSING, required stuff?
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for plotly_dict in self:
            plotly_dict.validate()  # recursively check the rest of the obj


class PlotlyDict(dict):
    """A base dict class for all objects that style a figure in plotly.

    A PlotlyDict can be instantiated like any dict object. This class
    offers some useful recursive methods that can be used by higher-level
    subclasses and containers so long as all plot objects are instantiated
    as a subclass of PlotlyDict. Each PlotlyDict should be instantiated
    with a `kind` keyword argument. This defines the special _info
    dictionary for the object.

    Any available methods that hold for a dict hold for a PlotlyDict.

    """
    __metaclass__ = DictMeta

    def __init__(self, **kwargs):
        super(PlotlyDict, self).__init__(**kwargs)
        self.validate()

    def _get_class_name(self):
        return self.__class__.__name__.lower()

    def clean(self):  # TODO: make this remove invalid *values* too!
        """Recursively rid PlotlyDict of `None` entries and invalid keys.

        CAREFUL! This will remove all inconsistencies quitely. If you want
        to know about invalid entries, try using the validate() method.

        """
        class_name = self._get_class_name()
        none_keys = set([key for key in self if self[key] is None])
        invalid_keys = set([key for key in self
                            if key not in INFO[class_name]['valid']])
        del_keys = set().union(none_keys, invalid_keys)
        for key in del_keys:
            del self[key]
        for val in self.values():
            try:
                val.clean()
            except AttributeError:
                pass

    def get_json(self):
        """Get a JSON representation for the PlotlyDict.

        This function changes all of the internal PlotlyDicts and PlotlyLists
        into normal lists and dicts.

        """
        d = dict()
        for key, val in self.items():
            try:
                d[key] = val.get_json()
            except AttributeError:
                d[key] = val
        return d

    def strip_style(self):
        """Strip style from the current representation of the plotly figure.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.
        The other attributes that will not be deleted are stored in the
        graph_objs_meta.py module under INFO['*']['safe'] for each `kind` of
        plotly object.

        """
        class_name = self._get_class_name()
        keys = self.keys()
        for key in keys:
            try:
                self[key].strip_style()
            except AttributeError:
                if key not in INFO[class_name]['safe']:
                    del self[key]

    def to_graph_objs(self):
        """Walk obj, convert dicts and lists to plotly graph objs.

        For each key in the object, if it corresponds to a special key that
        should be associated with a graph object, the ordinary dict or list
        will be reinitialized as a special PlotlyDict or PlotlyList of the
        appropriate `kind`.

        """
        keys = self.keys()
        for key in keys:
            if key in INFO:
                _class = TYPE_TO_CLASS[key]  # gets class constructor
                obj = _class(**self.pop(key))
                obj.to_graph_objs()
                self[key] = obj

    def validate(self):  # TODO: validate values too?
        """Recursively check the validity of the keys in a PlotlyDict.

        The valid keys are stored in plotly_word.py under INFO['*']['valid']
        for each `kind` of plotly object.

        """
        self.to_graph_objs()  # change everything to 'checkable' objs
        class_name = self._get_class_name()
        for key, val in self.items():
            try:
                val.validate()
            except AttributeError:
                try:
                    if key not in INFO[class_name]['valid']:
                        raise InvalidKeyError("Invalid key, '{}', for class, "
                                       "'{}'".format(key, self.__class__))
                except KeyError:
                    pass    # TODO: this *ignores* empty listings in INFO!!
                            # TODO: mostly for inital development...


# TODO: complete Data, Annotations,

class Data(PlotlyList):
    """Data doc.

    """
    def validate(self):  # TODO: should this check for MISSING, required stuff?
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for trace in self:
            if not issubclass(trace.__class__, Trace):
                raise InvalidListItemError("Trace Only!")
            trace.validate()  # recursively check the rest of the obj


class Annotations(PlotlyList):
    """Annotations doc.

    """
    def validate(self):  # TODO: should this check for MISSING, required stuff?
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for annotation in self:
            if not issubclass(annotation.__class__, Annotation):
                raise InvalidListItemError("Annotation Only!")
            annotation.validate()  # recursively check the rest of the obj


class Trace(PlotlyDict):
    """A general data class for plotly.

    """
    pass


class Bar(Trace):
    """A bar chart dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'bar'  # TODO: should this happen now or later?
        super(Bar, self).__init__(**kwargs)


class Box(Trace):
    """A box plot dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'box'  # TODO: should this happen now or later?
        super(Box, self).__init__(**kwargs)


class Contour(Trace):
    """A contour plot dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'contour'  # TODO: should this happen now or later?
        super(Contour, self).__init__(**kwargs)


class Heatmap(Trace):
    """A heatmap dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'heatmap'  # TODO: should this happen now or later?
        super(Heatmap, self).__init__(**kwargs)


class Histogramx(Trace):
    """A histogramx dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'histogramx'  # TODO: should this happen now or later?
        super(Histogramx, self).__init__(**kwargs)


class Histogramy(Trace):
    """A histgramy dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'histogramy'  # TODO: should this happen now or later?
        super(Histogramy, self).__init__(**kwargs)


class Histogram2d(Trace):
    """A histogram2d dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'histogram2d'  # TODO: should this happen now or later?
        super(Histogram2d, self).__init__(**kwargs)


class Scatter(Trace):
    """A scatter plot dictionary.

    """
    def __init__(self, **kwargs):
        kwargs['type'] = 'scatter'  # TODO: should this happen now or later?
        super(Scatter, self).__init__(**kwargs)


class Annotation(PlotlyDict):
    """Annotation doc.

    """
    pass


class ErrorX(PlotlyDict):
    """ErrorX doc.

    """
    pass


class ErrorY(PlotlyDict):
    """ErrorY doc.

    """
    pass


class Figure(PlotlyDict):
    """Documentation for Figure.

    """
    pass


class Font(PlotlyDict):
    """Font doc.

    """
    pass


class Layout(PlotlyDict):
    """Documentation for Layout.

    """
    pass


class Legend(PlotlyDict):
    """Legend doc.

    """
    pass


class Line(PlotlyDict):
    """Line doc.

    """
    pass


class Marker(PlotlyDict):
    """Marker doc.

    """
    pass


class Margin(PlotlyDict):
    """Margin doc.

    """
    pass


class TitleFont(PlotlyDict):
    """TitleFont doc.

    """
    pass


class XAxis(PlotlyDict):
    """XAxis doc.

    """
    pass


class YAxis(PlotlyDict):
    """YAxis doc.

    """
    pass


TYPE_TO_CLASS = dict(plotlylist=PlotlyList,
                     data=Data,
                     annotations=Annotations,
                     plotlydict=PlotlyDict,
                     trace=Trace,
                     bar=Bar,
                     box=Box,
                     contour=Contour,
                     heatmap=Heatmap,
                     hisogram2d=Histogram2d,
                     hisogramx=Histogramx,
                     hisogramy=Histogramy,
                     scatter=Scatter,
                     annotation=Annotation,
                     figure=Figure,
                     font=Font,
                     layout=Layout,
                     legend=Legend,
                     line=Line,
                     margin=Margin,
                     marker=Marker,
                     titlefont=TitleFont,
                     xaxis=XAxis,
                     yaxis=YAxis
                     )