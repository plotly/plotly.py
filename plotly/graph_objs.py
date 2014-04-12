"""
graph_objs
==========

A module that understands plotly language and can manage the json
structures. This module defines two base classes: PlotlyList and PlotlyDict.
The former is a generic container inheriting from `list` and the latter
inherits from `dict` and is used to contain all information for each part of
a plotly figure. A third structure, PlotlyTrace, is also considered a base
class for all subclassing 'trace' objects like Scatter, Box, Bar, etc. It is
also not meant to instantiated by users.

Goals of this module:
---------------------

* A dict/list with the same entries as a PlotlyDict/PlotlyList should look
exactly the same once a call is made to plot.

* Only mutate object structure when users ASK for it.

* It should always be possible to get a dict/list JSON representation from a
graph_objs object and it should always be possible to make a graph_objs object
from a dict/list JSON representation.

"""
import warnings
import collections
import json
from textwrap import wrap
from . import exceptions
from . import utils

# TODO: BIG ONE, how should exceptions bubble up in this inheritance scheme?
    # TODO: related, WHAT exceptions should bubble up?

from pkg_resources import resource_string
INFO = json.loads(resource_string('plotly',
                                  'graph_reference/graph_objs_meta.json'),
                  object_pairs_hook=collections.OrderedDict)

INFO = utils.decode_unicode(INFO)

KEY_TO_CLASS_NAME = dict(
    plotlylist='PlotlyList',
    data='Data',
    annotations='Annotations',
    plotlydict='PlotlyDict',
    plotlytrace='PlotlyTrace',
    bar='Bar',
    box='Box',
    contour='Contour',
    heatmap='Heatmap',
    histogram2d='Histogram2d',
    histogramx='Histogramx',
    histogramy='Histogramy',
    scatter='Scatter',
    annotation='Annotation',
    colorbar='ColorBar',
    error_y='Error_Y',
    figure='Figure',
    font='Font',
    layout='Layout',
    legend='Legend',
    line='Line',
    margin='Margin',
    marker='Marker',
    stream='Stream',
    textfont='Font',
    tickfont='Font',
    titlefont='Font',
    xaxis='XAxis',
    xbins='XBins',
    yaxis='YAxis',
    ybins='YBins'
)


class DictMeta(type):
    """A meta class for PlotlyDict class creation.

    The sole purpose of this meta class is to properly create the __doc__
    attribute so that running help(Obj), where Obj is a subclass of PlotlyDict,
    will return information about key-value pairs for that object.

    """
    def __new__(mcs, name, bases, attrs):
        class_name = name.lower()
        # remove min indentation...
        doc = attrs['__doc__']
        obj_info = INFO[class_name]
        line_size = 76
        tab_size = 4
        min_indent = min([len(a) - len(b)
                          for a, b in zip(doc.splitlines(),
                                          [l.lstrip()
                                           for l in doc.splitlines()])])
        doc = "".join([line[min_indent:] + '\n' for line in doc.splitlines()])
        # Add section header
        if len(obj_info):
            doc += "Valid keys:\n\n"
            # Add each key one-by-one and format
            width1 = line_size-tab_size
            width2 = line_size-2*tab_size
            width3 = line_size-3*tab_size
            undocumented = "Aw, sorry. Undocumented for now!"
            for key in obj_info:
                # main portion of documentation
                try:
                    required = str(obj_info[key]['required'])
                except KeyError:
                    required = undocumented
                try:
                    val_types = str(obj_info[key]['val_types'])
                except KeyError:
                    val_types = undocumented
                try:
                    descr = str(obj_info[key]['description'])
                except KeyError:
                    descr = undocumented
                try:
                    typ = str(obj_info[key]['type'])
                except KeyError:
                    typ = undocumented
                str_1 = "{} [required={}] (value={}):\n".format(key, required,
                                                                val_types)
                str_1 = "\t" + "\n\t".join(wrap(str_1, width=width1)) + "\n"
                str_2 = "\t\t" + "\n\t\t".join(wrap(descr, width=width2)) + "\n"
                doc += str_1 + str_2
                # if a user can run help on this value, tell them!
                if typ == "object":
                    doc += "\n\t\tFor more, run `help(plotly.graph_objs.{" \
                           "})`\n".format(KEY_TO_CLASS_NAME[key])
                # if example usage exists, tell them!
                if 'examples' in obj_info[key]:
                    ex = "\n\t\tExamples:\n" + "\t\t\t"
                    ex += "\n\t\t\t".join(wrap(str(obj_info[key]['examples']),
                                               width=width3)) + "\n"
                    doc += ex
                doc += '\n'
        attrs['__doc__'] = doc.expandtabs(tab_size)
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

    Valid entry types: empty PlotlyDict or dict only.


    """
    def __init__(self, *args):
        super(PlotlyList, self).__init__(*args)
        self.validate()
        if self._get_class_name() == 'plotlylist':
            warnings.warn("\nThe PlotlyList class is a base class of "
                          "list-like graph_objs.\nIt is not meant to be a "
                          "user interface.")

    def _get_class_name(self):
        """A hidden method allowing a class to know it's key in INFO."""
        return self.__class__.__name__.lower()

    def to_graph_objs(self):
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyDict.
            2. Call `to_graph_objects` on each of these entries.

        """
        for index, entry in enumerate(self):
            if isinstance(entry, PlotlyDict):
                entry.to_graph_objs()
            elif isinstance(entry, dict):
                try:
                    obj_type = entry['type']
                    try:
                        _class = STRING_TO_CLASS[obj_type]
                        self[index] = _class()
                        for key, val in entry.items():
                            self[index][key] = val
                        self[index].to_graph_objs()
                    except KeyError:
                        # TODO: should this default to Scatter?
                        raise exceptions.PlotlyInvalidListItemError(
                            "Entry had invalid 'type'")
                except KeyError:
                    raise exceptions.PlotlyInvalidListItemError(
                        "Entry didn't have key: 'type'")
            else:
                raise exceptions.PlotlyInvalidListItemError(
                    "Invalid entry, {}. PlotlyList entries must be dict-like."
                    "".format(entry))

    def update(self, changed_list, rollover=True):
        """Update current list with changed_list, which must be iterable.

        If rollover=True, the shorter list rolls over
        """
        # Since we allow lists of dicts of uneven lengths to update each other,
        # take it one step further and allow a list to be updated by a dict
        # by tossing it in a list of length 1
        if isinstance(changed_list, dict) and rollover:
            changed_list = [changed_list]
        self.to_graph_objs()
        if rollover:
            for i in range(max(len(self), len(changed_list))):
                self[i % len(self)].update(changed_list[i % len(changed_list)])
        else:
            for old_item, changed_item in zip(self, changed_list):
                old_item.update(changed_item)

    def strip_style(self):
        """Strip style from the current representation.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.

        Keys that will be stripped in this process are tagged with
        `'type': 'style'` in the INFO dictionary listed in graph_objs_meta.py.

        This process first attempts to convert nested collections from dicts
        or lists to subclasses of PlotlyList/PlotlyDict. This process forces
        a validation, which may throw exceptions.

        Then, each of these objects call `strip_style` on themselves and so
        on, recursively until the entire structure has been validated and
        stripped.

        """
        self.to_graph_objs()
        for plotly_dict in self:
            plotly_dict.strip_style()

    def get_data(self):
        """Returns the JSON for the plot with non-data elements stripped."""
        self.to_graph_objs()
        l = list()
        for plotlydict in self:
            l.append(plotlydict.get_data())
        for index, entry in enumerate(l):
            if len(entry) == 0:
                del l[index]
        return l

    def validate(self):
        """Recursively check the validity of the entries in a PlotlyList.

        PlotlyList may only contain suclasses of PlotlyDict, or dictionary-like
        objects that can be re-instantiated as subclasses of PlotlyDict.

        The validation process first requires that all nested collections be
        converted to the appropriate subclass of PlotlyDict/PlotlyList. Then,
        each of these objects call `validate` and so on, recursively,
        until the entire list has been validated.

        """
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for plotly_dict in self:
            try:
                plotly_dict.validate()  # recursively check the rest of the obj
            except AttributeError:
                raise exceptions.PlotlyInvalidListItemError(
                    "Plotly list-type objects can only contain plotly "
                    "dict-like objects.")

    def force_clean(self):
        self.to_graph_objs()
        for entry in self:
            entry.force_clean()
        del_indicies = [index for index, item in enumerate(self)
                        if len(item) == 0]
        del_ct = 0
        for index in del_indicies:
            del self[index - del_ct]
            del_ct += 1


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

    def __init__(self, *args, **kwargs):
        class_name = self._get_class_name()
        super(PlotlyDict, self).__init__(*args, **kwargs)
        if issubclass(STRING_TO_CLASS[class_name], PlotlyTrace):
            if class_name != 'plotlytrace':
                self['type'] = class_name
        self.validate()
        if self._get_class_name() == 'plotlydict':
            warnings.warn("\nThe PlotlyDict class is a base class of "
                          "dictionary-like graph_objs.\nIt is not meant to be "
                          "a user interface.")

    def _get_class_name(self):
        """A hidden method allowing a class to know it's key in INFO."""
        return self.__class__.__name__.lower()

    def update(self, dict1=None, **dict2):
        """Update current dict with changed_dict.

        This recursively updates the structure of the original dictionary-like
        object with the new entries in the second object. This allows users
        to update with large, nested structures.

        Example:
        obj = Layout(title='my title', xaxis=XAxis(range=[0,1], domain=[0,1]))
        obj.update(dict(title='new title', xaxis=dict(domain=[0,.8])))
        obj
        {'title': 'new title', 'xaxis': {'range': [0,1], 'domain': [0,.8]}}

        This `somewhat` supports duck-typing. It will accept the standard
        call to `update` like any dict object, however, it only supports
        updating from ONE new dictionary, a second dictionary will simply be
        ignored and the user will be warned.

        """
        try:
            dict1 = STRING_TO_CLASS[self._get_class_name()](dict1)
            dict2 = STRING_TO_CLASS[self._get_class_name()](dict2)
        except exceptions.PlotlyError:
            raise exceptions.PlotlyInstantiationError(
                "A dictionary to be used as an update cannot be instantiated "
                "as a graph_obj. Make sure it is of the same form as the "
                "graph_obj you are trying to update it with.")
        self.to_graph_objs()
        if len(dict2):
            dict2.update(dict1)
        if dict1 is not None:
            for key, val in dict1.items():
                if key in self:
                    if isinstance(self[key], (PlotlyDict, PlotlyList)):
                        self[key].update(val)
                    else:
                        self[key] = val
                else:
                    self[key] = val

    def strip_style(self):
        """Strip style from the current representation.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.

        Keys that will be stripped in this process are tagged with
        `'type': 'style'` in the INFO dictionary listed in graph_objs_meta.py.

        This process first attempts to convert nested collections from dicts
        or lists to subclasses of PlotlyList/PlotlyDict. This process forces
        a validation, which may throw exceptions.

        Then, each of these objects call `strip_style` on themselves and so
        on, recursively until the entire structure has been validated and
        stripped.

        """
        self.to_graph_objs()
        class_name = self._get_class_name()
        keys = self.keys()
        for key in keys:
            try:
                self[key].strip_style()
            except AttributeError:
                try:
                    if INFO[class_name][key]['type'] != 'style':
                        pass
                    else:
                        del self[key]
                except KeyError:  # TODO: Update the JSON
                    # print "'type' not in {} for {}".format(class_name, key)
                    del self[key]

    def get_data(self):
        """Returns the JSON for the plot with non-data elements stripped."""
        self.to_graph_objs()
        class_name = self._get_class_name()
        d = STRING_TO_CLASS[class_name]()
        try:
            del d['type']  # if this is any Trace, it will have 'type'
        except KeyError:
            pass
        for key, val in self.items():
            try:
                d[key] = val.get_data()
            except AttributeError:
                try:
                    if INFO[class_name][key]['type'] == 'data':
                        d[key] = val
                except KeyError:
                    pass
        d.force_clean()
        if len(d) == 1:
            d = d.values()[0]
        return d

    def to_graph_objs(self):
        """Walk obj, convert dicts and lists to plotly graph objs.

        For each key in the object, if it corresponds to a special key that
        should be associated with a graph object, the ordinary dict or list
        will be reinitialized as a special PlotlyDict or PlotlyList of the
        appropriate `kind`.

        """
        keys = self.keys()
        for key in keys:
            try:
                class_name = KEY_TO_CLASS_NAME[key].lower()
                if isinstance(self[key], dict):
                    obj = STRING_TO_CLASS[class_name]()  # gets constructor
                    for k, v in self.pop(key).items():
                        obj[k] = v
                    obj.to_graph_objs()
                    self[key] = obj
                elif isinstance(self[key], list):
                    obj = STRING_TO_CLASS[class_name]()  # gets constructor
                    obj += self.pop(key)
                    obj.to_graph_objs()
                    self[key] = obj
            except KeyError:
                try:
                    self[key].to_graph_objs()
                except AttributeError:
                    pass  # TODO: this means you don't get errors here...

    def validate(self):  # TODO: validate values too?
        """Recursively check the validity of the keys in a PlotlyDict.

        The valid keys constitute the entries in each object
        dictionary in INFO stored in graph_objs_meta.py.

        The validation process first requires that all nested collections be
        converted to the appropriate subclass of PlotlyDict/PlotlyList. Then,
        each of these objects call `validate` and so on, recursively,
        until the entire object has been validated.

        """
        self.to_graph_objs()  # change everything to 'checkable' objs
        class_name = self._get_class_name()
        for key, val in self.items():
            try:
                val.validate()
            except AttributeError:
                if key not in INFO[class_name]:
                    matching_objects = [obj for obj in INFO if key in INFO[obj]]
                    msg = "Invalid key, '{}', " \
                          "for class, '{}'\n\n".format(key, self.__class__)
                    if len(matching_objects):
                        msg += "That key is valid only in these objects:\n\n"
                        for obj in matching_objects:
                            msg += "\t{}".format(KEY_TO_CLASS_NAME[obj])
                            try:
                                msg += "({}='{}')\n".format(
                                    key, INFO[obj][key]['val_types'])
                            except KeyError:
                                msg += "({}='..')\n".format(key)
                        msg.expandtabs()
                    else:
                        msg += "Couldn't find uses for key: {}\n\n".format(key)
                    raise exceptions.PlotlyInvalidKeyError(msg)

    def force_clean(self):
        class_name = self._get_class_name()
        self.to_graph_objs()
        del_keys = [key for key in self if str(key) not in INFO[class_name]]
        for key in del_keys:
            del self[key]
        keys = self.keys()
        for key in keys:
            try:
                self[key].force_clean()
            except AttributeError:
                pass
            if isinstance(self[key], (dict, list)):
                if len(self[key]) == 0:
                    del self[key]  # clears empty collections!


class Data(PlotlyList):
    """A list of traces to be shown on a plot/graph.

    Any operation that can be done with a standard list may be used with Data.
    Instantiation requires an iterable (just like list does), for example:

    Data([Scatter(), Heatmap(), Box()])

    Valid entry types: (dict or any subclass of Trace, i.e., Scatter, Box, etc.)

    """
    def validate(self):
        """Recursively check the validity of the entries in a Data.

        Data may only contain suclasses of PlotlyTrace, or dictionary-like
        objects that can be re-instantiated as subclasses of PlotlyTrace.

        The validation process first requires that all nested collections be
        converted to the appropriate subclass of PlotlyDict/PlotlyList. Then,
        each of these objects call `validate` and so on, recursively,
        until the entire data list has been validated.

        """
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for plotlytrace in self:
            if not issubclass(plotlytrace.__class__, PlotlyTrace):
                raise exceptions.PlotlyInvalidListItemError(
                    "Subclasses of PlotlyTrace only in Data, e.g. Scatter, "
                    "Box, Heatmap, etc.")
        super(Data, self).validate()

    def to_graph_objs(self):  # TODO: figure out where errors from here go.
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyTrace.
            2. Call `to_graph_objects` on each of these entries.

        """
        for item in self:
            if ('type' not in item) and isinstance(item, dict):
                item['type'] = 'scatter'
        super(Data, self).to_graph_objs()


class Annotations(PlotlyList):
    """A list-like object to contain all figure notes.

    Any operation that can be done with a standard list may be used with
    Annotations. Instantiation requires an iterable (just like list does),
    for example:

    Annotations([Annotation(), Annotation(), Annotation()])

    This Annotations list is validated upon instantiation, meaning exceptions
    will be thrown if any invalid entries are found.

    Valid entry types: (dict or Annotation)

    For help on Annotation, run `help(plotly.graph_objs.Annotation)`

    """
    def validate(self):
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for annotation in self:
            if not issubclass(annotation.__class__, Annotation):
                raise exceptions.PlotlyInvalidListItemError(
                    "Annotation objects only in Annotations.")
        super(Annotations, self).validate()

    def to_graph_objs(self):
        for index, entry in enumerate(self):
            obj = Annotation()
            for k, v in entry.items():
                obj[k] = v
            self[index] = obj
        super(Annotations, self).to_graph_objs()


class PlotlyTrace(PlotlyDict):
    """A general data class for plotly.

    The PlotlyTrace object is not meant for user interaction. It's sole
    purpose is to improve the structure of the object hierarchy established
    in this module.

    Users should work with the subclasses of PlotlyTrace: Scatter, Box, Bar,
    Heatmap, etc.

    For help with these subclasses, run:
    `help(plotly.graph_objs.Obj)` where Obj == Scatter, Box, Bar, Heatmap, etc.

    """
    def __init__(self, *args, **kwargs):
        super(PlotlyTrace, self).__init__(*args, **kwargs)
        if self._get_class_name() == 'plotlytrace':
            warnings.warn("\nThe PlotlyTrace class is a base class of "
                          "dictionary-like plot types.\nIt is not meant to be "
                          "a user interface.")


class Bar(PlotlyTrace):
    """A dictionary-like object for representing a bar chart in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Box(PlotlyTrace):
    """A dictionary-like object for representing a box plot in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Contour(PlotlyTrace):
    """A dictionary-like object for representing a contour plot in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Heatmap(PlotlyTrace):
    """A dictionary-like object for representing a heatmap in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Histogramx(PlotlyTrace):
    """A dictionary-like object for representing a histogramx plot in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Histogramy(PlotlyTrace):
    """A dictionary-like object for representing a histogramy plot in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Histogram2d(PlotlyTrace):
    """A dictionary-like object for representing a histogram2d plot in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Scatter(PlotlyTrace):
    """A dictionary-like object for representing a scatter plot in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Annotation(PlotlyDict):
    """A dictionary-like object for representing an annotation in plotly.

    Annotations appear as notes on the final figure. You can set all the
    features of the annotation text, background color, and location.
    Additionally, these notes can be anchored to actual data or the page for
    help with location after pan-and-zoom actions.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class ColorBar(PlotlyDict):  # TODO: ?
    """ColorBar doc.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Error_Y(PlotlyDict):
    """Error_Y doc.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Figure(PlotlyDict):
    """A dictionary-like object representing a figure to be rendered in plotly.

    For help with setting up subplots, run:
    `help(plotly.tools.get_subplots)`

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Font(PlotlyDict):
    """A dictionary-like object representing details about font style.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Layout(PlotlyDict):
    """A dictionary-like object holding plot settings for plotly figures.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    def __init__(self, *args, **kwargs):
        super(Layout, self).__init__(*args, **kwargs)

    def to_graph_objs(self):
        """Walk obj, convert dicts and lists to plotly graph objs.

        For each key in the object, if it corresponds to a special key that
        should be associated with a graph object, the ordinary dict or list
        will be reinitialized as a special PlotlyDict or PlotlyList of the
        appropriate `kind`.

        """
        keys = self.keys()
        for key in keys:
            if isinstance(self[key], dict):
                if key[:5] == 'xaxis':  # allows appended integers!
                    try:
                        test_if_int = int(key[5:])
                        obj = XAxis()
                        for k, v in self.pop(key):
                            obj[k] = v
                        obj.to_graph_objs()
                        self[key] = obj
                    except ValueError:
                        pass
                elif key[:5] == 'yaxis':  # allows appended integers!
                    try:
                        test_if_int = int(key[5:])
                        obj = YAxis()
                        for k, v in self.pop(key):
                            obj[k] = v
                        obj.to_graph_objs()
                        self[key] = obj
                    except ValueError:
                        pass
        super(Layout, self).to_graph_objs()

    def force_clean(self):  # TODO: can't make call to super...
        class_name = self._get_class_name()
        self.to_graph_objs()
        del_keys = [key for key in self if str(key) not in INFO[class_name]]
        for key in del_keys:
            if (key[1:5] == 'xaxis') or (key[1:5] == 'yaxis'):
                try:
                    test = int(key[5:])
                    pass
                except ValueError:
                    del self[key]
            else:
                del self[key]
        keys = self.keys()
        for key in keys:
            try:
                self[key].force_clean()
            except AttributeError:
                pass
            if isinstance(self[key], (dict, list)):
                if len(self[key]) == 0:
                    del self[key]  # clears empty collections!


class Legend(PlotlyDict):
    """A dictionary-like object representing the legend options for a figure.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Line(PlotlyDict):
    """A dictionary-like object representing the style of a line in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Marker(PlotlyDict):
    """A dictionary-like object representing marker(s) style in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Margin(PlotlyDict):
    """A dictionary-like object holding plot margin information.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class Stream(PlotlyDict):
    """Stream doc.

    """
    pass


class XAxis(PlotlyDict):
    """A dictionary-like object representing an xaxis in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class XBins(PlotlyDict):
    """A dictionary-like object representing bin information for a histogram.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class YAxis(PlotlyDict):
    """A dictionary-like object representing a yaxis in plotly.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass


class YBins(PlotlyDict):
    """A dictionary-like object representing bin information for a histogram.

    This object is validated upon instantiation, therefore, you may see
    exceptions getting thrown. These are intended to help users find the
    origin of errors faster. The errors will usually contain information that
    can be used to remedy the problem.

    """
    pass

STRING_TO_CLASS = dict(
    plotlylist=PlotlyList,
    data=Data,
    annotations=Annotations,
    plotlydict=PlotlyDict,
    plotlytrace=PlotlyTrace,
    bar=Bar,
    box=Box,
    contour=Contour,
    heatmap=Heatmap,
    hisogram2d=Histogram2d,
    hisogramx=Histogramx,
    hisogramy=Histogramy,
    scatter=Scatter,
    annotation=Annotation,
    colorbar=ColorBar,
    error_y=Error_Y,
    figure=Figure,
    font=Font,
    layout=Layout,
    legend=Legend,
    line=Line,
    margin=Margin,
    marker=Marker,
    stream=Stream,
    textfont=Font,
    tickfont=Font,
    titlefont=Font,
    xaxis=XAxis,
    xbins=XBins,
    yaxis=YAxis,
    ybins=YBins
)