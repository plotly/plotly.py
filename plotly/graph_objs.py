"""
graph_objs
==========

A module that understands plotly language and can manage the json
structures. This module defines two base classes: PlotlyList and PlotlyDict.
The former is a generic container inheriting from `list` and the latter
inherits from `dict` and is used to contain all information for each part of
a plotly figure.

"""

from . graph_objs_meta import INFO


class DictMeta(type):
    """A meta class for PlotlyDict class creation.

    The sole purpose of this meta class is to properly create the __doc__
    attribute so that running help(*), where * is a subclass of PlotlyDict,
    will return information about key-value pairs for that object.

    """
    def __new__(cls, name, bases, attrs):
        kind = name.lower()
        doc = "\n".join([line.lstrip()
                         for line in attrs['__doc__'].splitlines()])
        if 'valid' in INFO[kind]:
            if len(INFO[kind]['valid']):
                doc += "Valid keys:\n\n"
                for key in INFO[kind]['valid']:
                    types = INFO[kind]['types'][key]
                    descriptor = INFO[kind]['descriptors'][key]
                    doc += "\t{} ({}): \n\t\t{}\n".format(key,types,descriptor)
        attrs['__doc__'] = doc.expandtabs(4)
        return super(DictMeta, cls).__new__(cls, name, bases, attrs)


class PlotlyList(list):
    """A container for PlotlyDicts, inherits from standard list.
    
    Plotly uses lists and dicts as collections to hold information about a
    figure. This container is simply a list that understands some plotly
    language and apes the methods in a PlotlyDict, passing them on to its
    constituents.
    
    It can be initialized like any other list so long as the entries are all
    PlotlyDict objects or subclasses thereof.
    
    Any available methods that hold for a list object hold for a PlotlyList.

    """

    def __init__(self, *args):
        super(PlotlyList, self).__init__(self)
        for arg in args:
            self.append(arg)

    def __setitem__(self, key, value):
        if not isinstance(value, PlotlyDict):
            raise ValueError("Only PlotlyDict or subclasses thereof can "
                             "populate a PlotlyList.")
        super(PlotlyList, self).__setitem__(key, value)

    def append(self, arg):
        if not isinstance(arg, PlotlyDict):
            raise ValueError("Only PlotlyDict or subclasses thereof can "
                             "populate a PlotlyList.")
        super(PlotlyList, self).append(arg)

    def to_json(self):
        """Return a json structure representation for the PlotlyList."""
        l = list()
        for pd in self:
            l.append(pd.to_json())
        return l

    def to_pandas(self):
        return "not yet implemented!!!"

    def to_numpy(self):
        return "not yet implemented!!!"

    def to_datetime(self):
        return "not yet implemented!!!"

    def get_data(self):
        return "not yet implemented!!!"

    def strip_style(self):
        """Strip style information from each of the PlotlyList's entries."""
        for pd in self:
            pd.strip_style()

    def clean(self):  # TODO: make this remove invalid entries too!
        """Remove any entries that are NoneType from PlotlyLists's entries."""
        for item in self:
            item.clean()

    def check(self):
        """Check each entry in the PlotlyList for invalid keys."""
        for item in self:
            item.check()

    def repair_vals(self):
        """Some unfortunately placed functionality for use with mplexporter."""
        for item in self:
            item.repair_vals()

    def repair_keys(self):
        """Some unfortunately placed functionality for use with mplexporter."""
        for item in self:
            item.repair_keys()

# TODO: complete Data, Annotations,

class Data(PlotlyList):
    """A plotly list that may contain only objects subclassed from Trace."""
    def __init__(self, *args):
        super(Data, self).__init__(*args)

    def check(self):
        """Check for invalid dict entries, then pass to super.check()."""
        for item in self:
            if not isinstance(item, Trace):
                raise ValueError('Non-Trace type objects cannot populate Data.')
            super(Data, self).check()


class Annotations(PlotlyList):
    """A PlotlyList that may contain only Annotation objects."""
    def __init__(self, *args):
        super(Annotations, self).__init__(*args)

    def check(self):
        """Check for invalid dict entries, then pass to super.check()."""
        for item in self:
            if not isinstance(item, Annotation):
                raise ValueError('Non-Annotation type objects cannot populate '
                                 'Annotations.')
            super(Annotations, self).check()


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

    def __init__(self, kind=None, **kwargs):
        if kind is not None:
            kwargs['_info'] = INFO[kind]
        else:
            kwargs['_info'] = INFO['base_dict']
        super(PlotlyDict, self).__init__(**kwargs)

    def __str__(self):
        return str(self.to_json())

    def _pop_info(self):
        """Private. Remove `_info` dictionary from PlotlyDict."""
        return self.pop('_info')

    def _push_info(self, _info):
        """Private. Add `_info` back dictionary to PlotlyDict."""
        self['_info'] = _info

    def to_graph_objs(self):
        """Walk obj, convert dicts and lists to plotly graph objs.

        For each key in the object, if it corresponds to a special key that
        should be associated with a graph object, the ordinary dict or list
        will be reinitialized as a special PlotlyDict or PlotlyList of the
        appropriate `kind`.

        """
        _info = self._pop_info()
        p_keys = ['marker', 'line', 'legend', 'font']
        keys = self.keys()
        for key in keys:
            if key in p_keys:
                try:
                    self[key]._pop_info()
                except AttributeError:
                    pass
                d = PlotlyDict(kind=key, **self.pop(key))
                d.to_graph_objs()
                self[key] = d
        self._push_info(_info)

    def get_help(self, key):
        """Return a 'key (types):\n description' string"""
        try:
            kind = self['_info']['kind']
            types = self['_info']['types'][key]
            description = self['_info']['descriptors'][key]
            string = "Query on key from object kind, {}:\n\n"\
                     "key: {}\n"\
                     "allowable value types: {}\n"\
                     "key description: {}\n\n".format(kind, key,
                                                      types, description)
            return string
        except KeyError:
            return "{} is not a valid key for obj kind, {}".format(key, kind)

    def to_json(self):
        """Get a JSON representation for the PlotlyDict.

        This function changes all of the internal PlotlyDicts and PlotlyLists
        into normal lists and dicts.

        """
        d = dict()
        _info = self._pop_info()
        for key, val in self.items():
            try:
                d[key] = val.to_json()
            except AttributeError:
                d[key] = val
        self._push_info(_info)
        return d

    def to_pandas(self):
        return "not yet implemented!!!"

    def to_numpy(self):
        return "not yet implemented!!!"

    def to_datetime(self):
        return "not yet implemented!!!"

    def get_data(self):
        return "not yet implemented!!!"

    def strip_style(self):
        """Strip style from the current representation of the plotly figure.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.
        The other attributes that will not be deleted are stored in the
        graph_objs_meta.py module under INFO['*']['safe'] for each `kind` of
        plotly object.

        """
        _info = self._pop_info()
        keys = self.keys()
        for key in keys:
            try:
                self[key].strip_style()
            except AttributeError:
                if key not in _info['safe']:
                    del self[key]
        self._push_info(_info)

    def clean(self):  # TODO: make this remove invalid entries too!
        """Recursively rid PlotlyDict of `None` entries."""
        del_keys = [key for key in self if self[key] is None]
        for key in del_keys:
            del self[key]
        for val in self.values():
            try:
                val.clean()
            except AttributeError:
                pass

    def check(self):
        """Recursively check the validity of the keys in a PlotlyDict.

        The valid keys are stored in plotly_word.py under INFO['*']['valid']
        for each `kind` of plotly object.

        """
        _info = self._pop_info()
        for key, val in self.items():
            try:
                val.check()
            except AttributeError:
                if key not in _info['valid']:
                    raise KeyError("Invalid key, '{}', for PlotlyDict kind, "
                                   "'{}'".format(key, _info['kind']))
        self._push_info(_info)

    def repair_vals(self):
        """Repair known common value problems.

        Plotly objects that require this functionality define a
        non-trivial INFO['*']['repair_vals'] `dict` in graph_objs_meta.py. The
        structure of these dictionaries are as follows:

        INFO['*']['repair_vals'] =
            dict(key_1=[suspect_val_1, correct_val_1], ...)

        """
        _info = self._pop_info()
        for key in self:
            try:
                self[key].repair_vals()
            except AttributeError:
                try:
                    if self[key] == _info['repair_vals'][key][0]:
                        self[key] = _info['repair_vals'][key][1]
                except KeyError:
                    pass
        self._push_info(_info)
        self.clean()

    def repair_keys(self):
        """Repair known common key problems.

        Plotly objects that require this functionality define a private
        non-trivial INFO['*']['repair_keys'] `dict` in graph_objs_meta.py. The
        structure of these dictionaries are as follows:

        INFO['*']['repair_keys'] = dict(suspect_key_1=correct_key_1, ...)

        """
        _info = self._pop_info()
        for key in self:
            if key in _info['repair_keys']:
                self[_info['repair_keys'][key]] = self.pop(key)
        for key in self:
            try:
                self[key].repair_keys()
            except AttributeError:
                pass
        self._push_info(_info)
        self.clean()


class Trace(PlotlyDict):
    """A general data class for plotly."""
    def __init__(self, **kwargs):
        super(Trace, self).__init__(**kwargs)


class Scatter(Trace):
    """A scatter plot dictionary.

    """
    def __init__(self, **kwargs):
        super(Scatter, self).__init__(kind='scatter', **kwargs)


class Heatmap(Trace):
    """A heatmap dictionary.

    """
    def __init__(self, **kwargs):
        super(Heatmap, self).__init__(kind='heatmap', **kwargs)


class Layout(PlotlyDict):
    """Documentation for Layout.

    """
    def __init__(self, **kwargs):
        super(Layout, self).__init__(kind='layout', **kwargs)


class Font(PlotlyDict):
    """Font doc.

    """
    def __init__(self, **kwargs):
        super(Font, self).__init__(kind='font', **kwargs)


class Line(PlotlyDict):
    """Line doc.

    """
    def __init__(self, **kwargs):
        super(Line, self).__init__(kind='line', **kwargs)


class Marker(PlotlyDict):
    """Marker doc.

    """
    def __init__(self, **kwargs):
        super(Marker, self).__init__(kind='marker', **kwargs)


class Annotation(PlotlyDict):
    """Annotation doc.

    """
    def __init__(self, **kwargs):
        super(Annotation, self).__init__(kind='annotation', **kwargs)

# TODO: Add ErrorY, ErrorX


