"""
graph_objs
===========

A module that understands plotly language and can manage the json
structures. This module defines two classes: PlotlyList and PlotlyDict. The
former is a generic container inheriting from `list` and the latter inherits
from `dict` and is used to contain all information for each part of a plotly
figure.

"""

from . graph_objs_meta import INFO


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
        """Initialize PlotlyList.

        Differs from list initialization only in that it forces all new items
        to be added through the `append`.

        Positional arguments:
        args -- a list of positional arguments of any length

        """
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

    def get_json(self):
        """Return a json structure representation for the PlotlyList."""
        l = list()
        for pd in self:
            l.append(pd.get_json())
        return l

    def strip_style(self):
        """Strip style information from each of the PlotlyList's entries."""
        for pd in self:
            pd.strip_style()

    def clean(self):
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


class PlotlyDict(dict):
    """${add_doc('base')}
    """

    def __init__(self, kind=None, **kwargs):
        if kind is not None:
            kwargs['_info'] = INFO[kind]
        else:
            kwargs['_info'] = INFO['base']
        super(PlotlyDict, self).__init__(**kwargs)

    def __str__(self):
        return str(self.get_json())

    def _pop_info(self):
        """Remove `private` info from PlotlyDict.

        This is only temporary and should be used only by the PlotlyDict class.

        """
        return self.pop('_info')

    def _push_info(self, _info):
        """Add `private` info back to PlotlyDict.

        This is only temporary and should be used only by the PlotlyDict class.

        """
        self['_info'] = _info

    def get_json(self):
        """Get a JSON representation for the PlotlyDict.

        This function changes all of the internal PlotlyDicts and PlotlyLists
        into normal lists and dicts. Though duck-typing should allow
        PlotlyLists and PlotlyDicts to be sent to plotly directly, this is a
        safer approach for compatibility.

        """
        d = dict()
        _info = self._pop_info()
        for key, val in self.items():
            try:
                d[key] = val.get_json()
            except AttributeError:
                d[key] = val
        self._push_info(_info)
        return d

    def strip_style(self):
        """Strip style from the current representation of the plotly figure.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.
        The other attributes that will not be deleted are stored in the
        graph_objs_meta module under INFO['*']['safe'] for each `kind` of plotly
        object.

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

    def clean(self):
        """Recursively rid PlotlyDict of `None` entries.

        This only rids a PlotlyDict of `None` entries, not empty dictionaries or
        lists.

        """
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


class Data(PlotlyDict):
    """${add_doc('data')}
    """
    def __init__(self, **kwargs):
        super(Data, self).__init__(kind='data', **kwargs)

class Layout(PlotlyDict):
    """${add_doc('layout')}
    """
    def __init__(self, **kwargs):
        super(Layout, self).__init__(kind='layout', **kwargs)

class Font(PlotlyDict):
    """${add_doc('font')}
    """
    def __init__(self, **kwargs):
        super(Font, self).__init__(kind='font', **kwargs)

class Line(PlotlyDict):
    """${add_doc('line')}
    """
    def __init__(self, **kwargs):
        super(Line, self).__init__(kind='line', **kwargs)

class Marker(PlotlyDict):
    """${add_doc('marker')}
    """
    def __init__(self, **kwargs):
        super(Marker, self).__init__(kind='marker', **kwargs)

"""
Classes inheriting from PlotlyDict:


ErrorY
ErrorX


Classes inheriting from PlotlyList:
AnnotationList
DataList
"""
