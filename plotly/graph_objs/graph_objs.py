"""
graph_objs
==========

A module that understands plotly language and can manage the json
structures. This module defines two base classes: PlotlyList and PlotlyDict.
The former inherits from `list` and the latter inherits from `dict`. and is
A third structure, PlotlyTrace, is also considered a base class for all
subclassing 'trace' objects like Scatter, Box, Bar, etc. It is also not meant
to instantiated by users.

Goals of this module:
---------------------

* A dict/list with the same entries as a PlotlyDict/PlotlyList should look
exactly the same once a call is made to plot.

* Only mutate object structure when users ASK for it. (some magic now...)

* It should always be possible to get a dict/list JSON representation from a
graph_objs object and it should always be possible to make a graph_objs object
from a dict/list JSON representation.

"""
from __future__ import absolute_import

import copy
import re
import warnings
from collections import OrderedDict

import six

from plotly import exceptions, graph_reference
from plotly.graph_objs import graph_objs_tools

_subplot_regex = re.compile(r'(?P<digits>\d+$)')


class PlotlyBase(object):
    """
    Base object for PlotlyList and PlotlyDict.

    """
    _name = None
    _parent = None
    _parent_key = None

    def _get_path(self):
        """
        Get a tuple of the str keys and int indices for this object's path.

        :return: (tuple)

        """
        path = []
        parents = self._get_parents()
        parents.reverse()
        children = [self] + parents[:-1]
        for parent, child in zip(parents, children):
            path.append(child._parent_key)
        path.reverse()
        return tuple(path)

    def _get_parents(self):
        """
        Get a list of all the parent objects above this one.

        :return: (list[PlotlyBase])

        """
        parents = []
        parent = self._parent
        while parent is not None:
            parents.append(parent)
            parent = parent._parent
        parents.reverse()
        return parents

    def _get_parent_object_names(self):
        """
        Get a list of the names of the parent objects above this one.

        :return: (list[str])

        """
        parents = self._get_parents()
        return [parent._name for parent in parents]

    def _get_class_name(self):
        """For convenience. See `graph_reference.object_name_to_class_name`."""
        return graph_reference.object_name_to_class_name(self._name)

    def help(self, return_help=False):
        """
        Print a help string for this object.

        :param (bool) return_help: Return help string instead of prining?
        :return: (None|str) Optionally can return help string.

        """
        object_name = self._name
        path = self._get_path()
        parent_object_names = self._get_parent_object_names()
        help_string = graph_objs_tools.get_help(object_name, path,
                                                parent_object_names)
        if return_help:
            return help_string
        print(help_string)

    def to_graph_objs(self, **kwargs):
        """Everything is cast into graph_objs. Here for backwards compat."""
        pass

    def validate(self):
        """Everything is *always* validated now. Keep for backwards compat."""
        pass


class PlotlyList(list, PlotlyBase):
    """
    Base class for list-like Plotly objects.

    """
    _name = None

    def __init__(self, *args, **kwargs):
        _raise = kwargs.get('_raise', True)
        if self._name is None:
            self.__dict__['_name'] = kwargs.pop('_name', None)
        self.__dict__['_parent'] = kwargs.get('_parent')
        self.__dict__['_parent_key'] = kwargs.get('_parent_key')

        if self._name is None:
            raise exceptions.PlotlyError(
                "PlotlyList is a base class. It's shouldn't be instantiated."
            )

        if args and isinstance(args[0], dict):
            note = (
                "Just like a `list`, `{name}` must be instantiated "
                "with a *single* collection.\n"
                "In other words these are OK:\n"
                ">>> {name}()\n"
                ">>> {name}([])\n"
                ">>> {name}([dict()])\n"
                ">>> {name}([dict(), dict()])\n"
                "However, these don't make sense:\n"
                ">>> {name}(dict())\n"
                ">>> {name}(dict(), dict())"
                .format(name=self._get_class_name())
            )
            raise exceptions.PlotlyListEntryError(self, [0], notes=[note])

        super(PlotlyList, self).__init__()

        for index, value in enumerate(list(*args)):
            value = self._value_to_graph_object(index, value, _raise=_raise)

            if isinstance(value, PlotlyBase):
                self.append(value)

    def __setitem__(self, index, value, _raise=True):
        """Override to enforce validation."""
        if not isinstance(index, int):
            if _raise:
                index_type = type(index)
                raise TypeError('Index must be int, not {}'.format(index_type))
            return

        if index >= len(self):
            raise IndexError(index)

        value = self._value_to_graph_object(index, value, _raise=_raise)
        if isinstance(value, (PlotlyDict, PlotlyList)):
            super(PlotlyList, self).__setitem__(index, value)

    def __setattr__(self, key, value):
        raise exceptions.PlotlyError('Setting attributes on a PlotlyList is '
                                     'not allowed')

    def __iadd__(self, other):
        """Defines the `+=` operator, which we map to extend."""
        self.extend(other)
        return self

    def __copy__(self):

        # TODO: https://github.com/plotly/python-api/issues/291
        return GraphObjectFactory.create(self._name, _parent=self._parent,
                                         _parent_key=self._parent_key, *self)

    def __deepcopy__(self, memodict={}):

        # TODO: https://github.com/plotly/python-api/issues/291
        return self.__copy__()

    def _value_to_graph_object(self, index, value, _raise=True):
        """
        Attempt to change the given value into a graph object.

        If _raise is False, this won't raise. If the entry can't be converted,
        `None` is returned, meaning the caller should ignore the value or
        discard it as a failed conversion.

        :param (dict) value: A dict to be converted into a graph object.
        :param (bool) _raise: If False, ignore bad values instead of raising.
        :return: (PlotlyBase|None) The graph object or possibly `None`.

        """
        if not isinstance(value, dict):
            if _raise:
                path = self._get_path() + (index, )
                raise exceptions.PlotlyListEntryError(self, path)
            else:
                return

        items = graph_reference.ARRAYS[self._name]['items']
        for i, item in enumerate(items, 1):
            try:
                return GraphObjectFactory.create(item, _raise=_raise,
                                                 _parent=self,
                                                 _parent_key=index, **value)
            except exceptions.PlotlyGraphObjectError:
                if i == len(items) and _raise:
                    raise

    def append(self, value):
        """Override to enforce validation."""
        index = len(self)  # used for error messages
        value = self._value_to_graph_object(index, value)
        super(PlotlyList, self).append(value)

    def extend(self, iterable):
        """Override to enforce validation."""
        for value in iterable:
            index = len(self)
            value = self._value_to_graph_object(index, value)
            super(PlotlyList, self).append(value)

    def insert(self, index, value):
        """Override to enforce validation."""
        value = self._value_to_graph_object(index, value)
        super(PlotlyList, self).insert(index, value)

    def update(self, changes, make_copies=False):
        """
        Update current list with changed_list, which must be iterable.

        :param (dict|list[dict]) changes:
        :param (bool) make_copies:

        Because mutable objects contain references to their values, updating
        multiple items in a list will cause the items to all reference the same
        original set of objects. To change this behavior add
        `make_copies=True` which makes deep copies of the update items and
        therefore break references.

        """
        if isinstance(changes, dict):
            changes = [changes]
        for index in range(len(self)):
            try:
                update = changes[index % len(changes)]
            except ZeroDivisionError:
                pass
            else:
                if make_copies:
                    self[index].update(copy.deepcopy(update))
                else:
                    self[index].update(update)

    def strip_style(self):
        """Strip style by calling `stip_style` on children items."""
        for plotly_dict in self:
            plotly_dict.strip_style()

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        l = list()
        for plotly_dict in self:
            l += [plotly_dict.get_data(flatten=flatten)]
        del_indicies = [index for index, item in enumerate(self)
                        if len(item) == 0]
        del_ct = 0
        for index in del_indicies:
            del self[index - del_ct]
            del_ct += 1

        if flatten:
            d = {}
            for i, e in enumerate(l):
                for k, v in e.items():
                    key = "{0}.{1}".format(i, k)
                    d[key] = v
            return d
        else:
            return l

    def get_ordered(self, **kwargs):
        """All children are already validated. Just use get_ordered on them."""
        return [child.get_ordered() for child in self]

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """Get formatted string by calling `to_string` on children items."""
        if not len(self):
            return "{name}()".format(name=self._get_class_name())
        string = "{name}([{eol}{indent}".format(
            name=self._get_class_name(),
            eol=eol,
            indent=' ' * indent * (level + 1))
        for index, entry in enumerate(self):
            string += entry.to_string(level=level+1,
                                      indent=indent,
                                      eol=eol,
                                      pretty=pretty,
                                      max_chars=max_chars)
            if index < len(self) - 1:
                string += ",{eol}{indent}".format(
                    eol=eol,
                    indent=' ' * indent * (level + 1))
        string += (
            "{eol}{indent}])").format(eol=eol, indent=' ' * indent * level)
        return string

    def force_clean(self, **kwargs):
        """Remove empty/None values by calling `force_clean()` on children."""
        for entry in self:
            entry.force_clean()
        del_indicies = [index for index, item in enumerate(self)
                        if len(item) == 0]
        del_ct = 0
        for index in del_indicies:
            del self[index - del_ct]
            del_ct += 1


class PlotlyDict(dict, PlotlyBase):
    """
    Base class for dict-like Plotly objects.

    """
    _name = None
    _parent_key = None
    _valid_attributes = None
    _deprecated_attributes = None
    _subplot_attributes = None

    def __init__(self, *args, **kwargs):

        _raise = kwargs.pop('_raise', True)
        if self._name is None:
            self.__dict__['_name'] = kwargs.pop('_name', None)
        self.__dict__['_parent'] = kwargs.pop('_parent', None)
        self.__dict__['_parent_key'] = kwargs.pop('_parent_key', None)

        if self._name is None:
            raise exceptions.PlotlyError(
                "PlotlyDict is a base class. It's shouldn't be instantiated."
            )

        super(PlotlyDict, self).__init__()

        if self._name in graph_reference.TRACE_NAMES:
            self['type'] = self._name

        # force key-value pairs to go through validation
        d = {key: val for key, val in dict(*args, **kwargs).items()}
        for key, val in d.items():
            self.__setitem__(key, val, _raise=_raise)

    def __dir__(self):
        """Dynamically return the existing and possible attributes."""
        return sorted(list(self._get_valid_attributes()))

    def __getitem__(self, key):
        """Calls __missing__ when key is not found. May mutate object."""
        if key not in self:
            self.__missing__(key)
        return super(PlotlyDict, self).__getitem__(key)

    def __setattr__(self, key, value):
        """Maps __setattr__ onto __setitem__"""
        self.__setitem__(key, value)

    def __setitem__(self, key, value, _raise=True):
        """Validates/Converts values which should be Graph Objects."""
        if not isinstance(key, six.string_types):
            if _raise:
                raise TypeError('Key must be string, not {}'.format(type(key)))
            return

        if key.endswith('src'):
            if key in self._get_valid_attributes():
                value = graph_objs_tools.assign_id_to_src(key, value)
                return super(PlotlyDict, self).__setitem__(key, value)

        subplot_key = self._get_subplot_key(key)
        if subplot_key is not None:
            value = self._value_to_graph_object(subplot_key, value,
                                                _raise=_raise)
            if isinstance(value, (PlotlyDict, PlotlyList)):
                return super(PlotlyDict, self).__setitem__(key, value)

        if key not in self._get_valid_attributes():

            if key in self._get_deprecated_attributes():
                warnings.warn(
                    "Oops! '{attribute}' has been deprecated in "
                    "'{object_name}'\nThis may still work, but you should "
                    "update your code when possible.\n\n"
                    "Run `.help('{attribute}')` for more information."
                    .format(attribute=key, object_name=self._name)
                )

                # this means deprecated attrs get set *as-is*!
                return super(PlotlyDict, self).__setitem__(key, value)
            else:
                if _raise:
                    path = self._get_path() + (key, )
                    raise exceptions.PlotlyDictKeyError(self, path)
                return

        if self._get_attribute_role(key) == 'object':
            value = self._value_to_graph_object(key, value, _raise=_raise)
            if not isinstance(value, (PlotlyDict, PlotlyList)):
                return

        super(PlotlyDict, self).__setitem__(key, value)

    def __getattr__(self, key):
        """Python only calls this when key is missing!"""
        try:
            return self.__getitem__(key)
        except KeyError:
            raise AttributeError(key)

    def __copy__(self):

        # TODO: https://github.com/plotly/python-api/issues/291
        return GraphObjectFactory.create(self._name, _parent=self.parent,
                                         _parent_key=self._parent_key, **self)

    def __deepcopy__(self, memodict={}):

        # TODO: https://github.com/plotly/python-api/issues/291
        return self.__copy__()

    def __missing__(self, key):
        """Mimics defaultdict. This is called from __getitem__ when key DNE."""
        if key in self._get_valid_attributes():
            if self._get_attribute_role(key) == 'object':
                value = GraphObjectFactory.create(key, _parent=self,
                                                  _parent_key=key)
                return super(PlotlyDict, self).__setitem__(key, value)

        subplot_key = self._get_subplot_key(key)
        if subplot_key is not None:
            value = GraphObjectFactory.create(subplot_key, _parent=self,
                                              _parent_key=key)
            super(PlotlyDict, self).__setitem__(key, value)

    def _get_attribute_role(self, key, value=None):
        """See `graph_reference.get_role`."""
        object_name = self._name
        parent_object_names = self._get_parent_object_names()
        return graph_reference.get_role(
            object_name, key, value=value,
            parent_object_names=parent_object_names
        )

    def _get_valid_attributes(self):
        """See `graph_reference.get_valid_attributes`."""
        if self._valid_attributes is None:
            parent_object_names = self._get_parent_object_names()
            valid_attributes = graph_reference.get_valid_attributes(
                self._name, parent_object_names
            )
            self.__dict__['_valid_attributes'] = valid_attributes
        return self._valid_attributes

    def _get_deprecated_attributes(self):
        """See `graph_reference.get_deprecated_attributes`."""
        if self._deprecated_attributes is None:
            parent_object_names = self._get_parent_object_names()
            deprecated_attributes = graph_reference.get_deprecated_attributes(
                self._name, parent_object_names
            )
            self.__dict__['_deprecated_attributes'] = deprecated_attributes
        return self._deprecated_attributes

    def _get_subplot_attributes(self):
        """See `graph_reference.get_subplot_attributes`."""
        if self._subplot_attributes is None:
            parent_object_names = self._get_parent_object_names()
            subplot_attributes = graph_reference.get_subplot_attributes(
                self._name, parent_object_names
            )
            self.__dict__['_subplot_attributes'] = subplot_attributes
        return self._subplot_attributes

    def _get_subplot_key(self, key):
        """Some keys can have appended integers, this handles that."""
        match = _subplot_regex.search(key)
        if match:
            root_key = key[:match.start()]
            if (root_key in self._get_subplot_attributes() and
                    not match.group('digits').startswith('0')):
                return root_key

    def _value_to_graph_object(self, key, value, _raise=True):
        """
        Attempt to convert value to graph object.

        :param (str|unicode) key: Should be an object_name from GRAPH_REFERENCE
        :param (dict) value: This will fail if it's not a dict.
        :param (bool) _raise: Flag to prevent inappropriate erring.

        :return: (PlotlyList|PlotlyDict|None) `None` if `_raise` and failure.

        """
        if key in graph_reference.ARRAYS:
            val_types = (list, )
        else:
            val_types = (dict, )

        if not isinstance(value, val_types):
            if _raise:
                path = self._get_path() + (key, )
                raise exceptions.PlotlyDictValueError(self, path)
            else:
                return

        # this can be `None` when `_raise == False`
        return GraphObjectFactory.create(key, value, _raise=_raise,
                                         _parent=self, _parent_key=key)

    def help(self, attribute=None, return_help=False):
        """
        Print help string for this object or an attribute of this object.

        :param (str) attribute: A valid attribute string for this object.
        :param (bool) return_help: Return help_string instead of printing it?
        :return: (None|str)

        """
        if not attribute:
            return super(PlotlyDict, self).help(return_help=return_help)

        object_name = self._name
        path = self._get_path()
        parent_object_names = self._get_parent_object_names()
        help_string = graph_objs_tools.get_help(object_name, path,
                                                parent_object_names, attribute)

        if return_help:
            return help_string
        print(help_string)

    def update(self, dict1=None, **dict2):
        """
        Update current dict with dict1 and then dict2.

        This recursively updates the structure of the original dictionary-like
        object with the new entries in the second and third objects. This
        allows users to update with large, nested structures.

        Note, because the dict2 packs up all the keyword arguments, you can
        specify the changes as a list of keyword arguments.

        Examples:
        # update with dict
        obj = Layout(title='my title', xaxis=XAxis(range=[0,1], domain=[0,1]))
        update_dict = dict(title='new title', xaxis=dict(domain=[0,.8]))
        obj.update(update_dict)
        obj
        {'title': 'new title', 'xaxis': {'range': [0,1], 'domain': [0,.8]}}

        # update with list of keyword arguments
        obj = Layout(title='my title', xaxis=XAxis(range=[0,1], domain=[0,1]))
        obj.update(title='new title', xaxis=dict(domain=[0,.8]))
        obj
        {'title': 'new title', 'xaxis': {'range': [0,1], 'domain': [0,.8]}}

        This 'fully' supports duck-typing in that the call signature is
        identical, however this differs slightly from the normal update
        method provided by Python's dictionaries.

        """
        if dict1 is not None:
            for key, val in list(dict1.items()):
                if key in self:
                    if isinstance(self[key], (PlotlyDict, PlotlyList)):
                        self[key].update(val)
                    else:
                        self[key] = val
                else:
                    self[key] = val

        if len(dict2):
            for key, val in list(dict2.items()):
                if key in self:
                    if isinstance(self[key], (PlotlyDict, PlotlyList)):
                        self[key].update(val)
                    else:
                        self[key] = val
                else:
                    self[key] = val

    def strip_style(self):
        """
        Recursively strip style from the current representation.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.

        Keys that will be stripped in this process are tagged with
        `'type': 'style'` in graph_objs_meta.json. Note that a key tagged as
        style, but with an array as a value may still be considered data.

        """
        keys = list(self.keys())
        for key in keys:
            if isinstance(self[key], (PlotlyDict, PlotlyList)):
                self[key].strip_style()
            else:
                if self._get_attribute_role(key, value=self[key]) == 'style':
                    del self[key]

                # this is for backwards compat when we updated graph reference.
                elif self._name == 'layout' and key == 'autosize':
                    del self[key]

    def get_data(self, flatten=False):
        """Returns the JSON for the plot with non-data elements stripped."""
        d = dict()
        for key, val in list(self.items()):
            if isinstance(val, (PlotlyDict, PlotlyList)):
                sub_data = val.get_data(flatten=flatten)
                if flatten:
                    for sub_key, sub_val in sub_data.items():
                        key_string = "{0}.{1}".format(key, sub_key)
                        d[key_string] = sub_val
                else:
                    d[key] = sub_data
            else:
                if self._get_attribute_role(key, value=val) == 'data':
                    d[key] = val

                # we use the name to help make data frames
                if self._name in graph_reference.TRACE_NAMES and key == 'name':
                    d[key] = val
        keys = list(d.keys())
        for key in keys:
            if isinstance(d[key], (dict, list)):
                if len(d[key]) == 0:
                    del d[key]
        return d

    def get_ordered(self, **kwargs):
        """Return a predictable, OrderedDict version of self."""
        keys = sorted(self.keys(), key=graph_objs_tools.sort_keys)
        ordered = OrderedDict()
        for key in keys:
            if isinstance(self[key], PlotlyBase):
                ordered[key] = self[key].get_ordered()
            else:
                ordered[key] = self[key]
        return ordered

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """
        Returns a formatted string showing graph_obj constructors.

        :param (int) level: The number of indentations to start with.
        :param (int) indent: The indentation amount.
        :param (str) eol: The end of line character(s).
        :param (bool) pretty: Curtail long list output with a '..' ?
        :param (int) max_chars: The max characters per line.

        Example:

            print(obj.to_string())

        """
        if not len(self):
            return "{name}()".format(name=self._get_class_name())
        string = "{name}(".format(name=self._get_class_name())
        if self._name in graph_reference.TRACE_NAMES:
            keys = [key for key in self.keys() if key != 'type']
        else:
            keys = self.keys()

        keys = sorted(keys, key=graph_objs_tools.sort_keys)
        num_keys = len(keys)

        for index, key in enumerate(keys, 1):
            string += "{eol}{indent}{key}=".format(
                eol=eol,
                indent=' ' * indent * (level+1),
                key=key)
            if isinstance(self[key], PlotlyBase):
                string += self[key].to_string(level=level+1,
                                              indent=indent,
                                              eol=eol,
                                              pretty=pretty,
                                              max_chars=max_chars)
            else:
                if pretty:  # curtail representation if too many chars
                    max_len = (max_chars -
                               indent*(level + 1) -
                               len(key + "=") -
                               len(eol))
                    if index < num_keys:
                        max_len -= len(',')  # remember the comma!
                    if isinstance(self[key], list):
                        s = "[]"
                        for iii, entry in enumerate(self[key], 1):
                            if iii < len(self[key]):
                                s_sub = graph_objs_tools.curtail_val_repr(
                                    entry,
                                    max_chars=max_len - len(s),
                                    add_delim=True
                                )
                            else:
                                s_sub = graph_objs_tools.curtail_val_repr(
                                    entry,
                                    max_chars=max_len - len(s),
                                    add_delim=False
                                )
                            s = s[:-1] + s_sub + s[-1]
                            if len(s) == max_len:
                                break
                        string += s
                    else:
                        string += graph_objs_tools.curtail_val_repr(
                            self[key], max_len)
                else:  # they want it all!
                    string += repr(self[key])
            if index < num_keys:
                string += ","
        string += "{eol}{indent})".format(eol=eol, indent=' ' * indent * level)
        return string

    def force_clean(self, **kwargs):
        """Recursively remove empty/None values."""
        keys = list(self.keys())
        for key in keys:
            try:
                self[key].force_clean()
            except AttributeError:
                pass
            if isinstance(self[key], (dict, list)):
                if len(self[key]) == 0:
                    del self[key]  # clears empty collections!
            elif self[key] is None:
                del self[key]


class GraphObjectFactory(object):
    """GraphObject creation in this module should run through this factory."""

    @staticmethod
    def create(object_name, *args, **kwargs):
        """
        Create a graph object from the OBJECTS dict by name, args, and kwargs.

        :param (str) object_name: A valid object name from OBJECTS.
        :param args: Arguments to pass to class constructor.
        :param kwargs: Keyword arguments to pass to class constructor.

        :return: (PlotlyList|PlotlyDict) The instantiated graph object.

        """
        is_array = object_name in graph_reference.ARRAYS
        is_object = object_name in graph_reference.OBJECTS
        if not (is_array or is_object):
            raise exceptions.PlotlyError(
                "'{}' is not a valid object name.".format(object_name)
            )

        # We patch Figure and Data, so they actually require the subclass.
        class_name = graph_reference.OBJECT_NAME_TO_CLASS_NAME.get(object_name)
        if class_name in ['Figure', 'Data', 'Frames']:
            return globals()[class_name](*args, **kwargs)
        else:
            kwargs['_name'] = object_name
            if is_array:
                return PlotlyList(*args, **kwargs)
            else:
                return PlotlyDict(*args, **kwargs)


# AUTO-GENERATED BELOW. DO NOT EDIT! See makefile.


class AngularAxis(PlotlyDict):
    """
    Valid attributes for 'angularaxis' at path [] under parents ():
    
        ['categoryarray', 'categoryarraysrc', 'categoryorder', 'color',
        'direction', 'domain', 'dtick', 'endpadding', 'exponentformat',
        'gridcolor', 'gridwidth', 'hoverformat', 'layer', 'linecolor',
        'linewidth', 'nticks', 'period', 'range', 'rotation',
        'separatethousands', 'showexponent', 'showgrid', 'showline',
        'showticklabels', 'showtickprefix', 'showticksuffix', 'thetaunit',
        'tick0', 'tickangle', 'tickcolor', 'tickfont', 'tickformat',
        'tickformatstops', 'ticklen', 'tickmode', 'tickorientation',
        'tickprefix', 'ticks', 'ticksuffix', 'ticktext', 'ticktextsrc',
        'tickvals', 'tickvalssrc', 'tickwidth', 'type', 'visible']
    
    Run `<angularaxis-object>.help('attribute')` on any of the above.
    '<angularaxis-object>' is the object at []

    """
    _name = 'angularaxis'


class Annotation(PlotlyDict):
    """
    Valid attributes for 'annotation' at path [] under parents ():
    
        ['align', 'arrowcolor', 'arrowhead', 'arrowside', 'arrowsize',
        'arrowwidth', 'ax', 'axref', 'ay', 'ayref', 'bgcolor', 'bordercolor',
        'borderpad', 'borderwidth', 'captureevents', 'clicktoshow', 'font',
        'height', 'hoverlabel', 'hovertext', 'opacity', 'ref', 'showarrow',
        'standoff', 'startarrowhead', 'startarrowsize', 'startstandoff',
        'text', 'textangle', 'valign', 'visible', 'width', 'x', 'xanchor',
        'xclick', 'xref', 'xshift', 'y', 'yanchor', 'yclick', 'yref', 'yshift',
        'z']
    
    Run `<annotation-object>.help('attribute')` on any of the above.
    '<annotation-object>' is the object at []

    """
    _name = 'annotation'


class Annotations(PlotlyList):
    """
    Valid items for 'annotations' at path [] under parents ():
        ['Annotation']

    """
    _name = 'annotations'


class Area(PlotlyDict):
    """
    Valid attributes for 'area' at path [] under parents ():
    
        ['customdata', 'customdatasrc', 'hoverinfo', 'hoverinfosrc',
        'hoverlabel', 'ids', 'idssrc', 'legendgroup', 'marker', 'name',
        'opacity', 'r', 'rsrc', 'selectedpoints', 'showlegend', 'stream', 't',
        'tsrc', 'type', 'uid', 'visible']
    
    Run `<area-object>.help('attribute')` on any of the above.
    '<area-object>' is the object at []

    """
    _name = 'area'


class Bar(PlotlyDict):
    """
    Valid attributes for 'bar' at path [] under parents ():
    
        ['bardir', 'base', 'basesrc', 'cliponaxis', 'constraintext',
        'customdata', 'customdatasrc', 'dx', 'dy', 'error_x', 'error_y',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hovertext', 'hovertextsrc',
        'ids', 'idssrc', 'insidetextfont', 'legendgroup', 'marker', 'name',
        'offset', 'offsetsrc', 'opacity', 'orientation', 'outsidetextfont',
        'r', 'rsrc', 'selected', 'selectedpoints', 'showlegend', 'stream', 't',
        'text', 'textfont', 'textposition', 'textpositionsrc', 'textsrc',
        'tsrc', 'type', 'uid', 'unselected', 'visible', 'width', 'widthsrc',
        'x', 'x0', 'xaxis', 'xcalendar', 'xsrc', 'y', 'y0', 'yaxis',
        'ycalendar', 'ysrc']
    
    Run `<bar-object>.help('attribute')` on any of the above.
    '<bar-object>' is the object at []

    """
    _name = 'bar'


class Box(PlotlyDict):
    """
    Valid attributes for 'box' at path [] under parents ():
    
        ['boxmean', 'boxpoints', 'customdata', 'customdatasrc', 'fillcolor',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hoveron', 'ids', 'idssrc',
        'jitter', 'legendgroup', 'line', 'marker', 'name', 'notched',
        'notchwidth', 'opacity', 'orientation', 'pointpos', 'selected',
        'selectedpoints', 'showlegend', 'stream', 'text', 'textsrc', 'type',
        'uid', 'unselected', 'visible', 'whiskerwidth', 'x', 'x0', 'xaxis',
        'xcalendar', 'xsrc', 'y', 'y0', 'yaxis', 'ycalendar', 'ysrc']
    
    Run `<box-object>.help('attribute')` on any of the above.
    '<box-object>' is the object at []

    """
    _name = 'box'


class Candlestick(PlotlyDict):
    """
    Valid attributes for 'candlestick' at path [] under parents ():
    
        ['close', 'closesrc', 'customdata', 'customdatasrc', 'decreasing',
        'high', 'highsrc', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids',
        'idssrc', 'increasing', 'legendgroup', 'line', 'low', 'lowsrc', 'name',
        'opacity', 'open', 'opensrc', 'selectedpoints', 'showlegend', 'stream',
        'text', 'textsrc', 'type', 'uid', 'visible', 'whiskerwidth', 'x',
        'xaxis', 'xcalendar', 'xsrc', 'yaxis']
    
    Run `<candlestick-object>.help('attribute')` on any of the above.
    '<candlestick-object>' is the object at []

    """
    _name = 'candlestick'


class Carpet(PlotlyDict):
    """
    Valid attributes for 'carpet' at path [] under parents ():
    
        ['a', 'a0', 'aaxis', 'asrc', 'b', 'b0', 'baxis', 'bsrc', 'carpet',
        'cheaterslope', 'color', 'customdata', 'customdatasrc', 'da', 'db',
        'font', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc',
        'legendgroup', 'name', 'opacity', 'selectedpoints', 'showlegend',
        'stream', 'type', 'uid', 'visible', 'x', 'xaxis', 'xsrc', 'y', 'yaxis',
        'ysrc']
    
    Run `<carpet-object>.help('attribute')` on any of the above.
    '<carpet-object>' is the object at []

    """
    _name = 'carpet'


class Choropleth(PlotlyDict):
    """
    Valid attributes for 'choropleth' at path [] under parents ():
    
        ['autocolorscale', 'colorbar', 'colorscale', 'customdata',
        'customdatasrc', 'geo', 'hoverinfo', 'hoverinfosrc', 'hoverlabel',
        'ids', 'idssrc', 'legendgroup', 'locationmode', 'locations',
        'locationssrc', 'marker', 'name', 'opacity', 'reversescale',
        'selected', 'selectedpoints', 'showlegend', 'showscale', 'stream',
        'text', 'textsrc', 'type', 'uid', 'unselected', 'visible', 'z',
        'zauto', 'zmax', 'zmin', 'zsrc']
    
    Run `<choropleth-object>.help('attribute')` on any of the above.
    '<choropleth-object>' is the object at []

    """
    _name = 'choropleth'


class ColorBar(PlotlyDict):
    """
    Valid attributes for 'colorbar' at path [] under parents ():
    
        ['bgcolor', 'bordercolor', 'borderwidth', 'dtick', 'exponentformat',
        'len', 'lenmode', 'nticks', 'outlinecolor', 'outlinewidth',
        'separatethousands', 'showexponent', 'showticklabels',
        'showtickprefix', 'showticksuffix', 'thickness', 'thicknessmode',
        'tick0', 'tickangle', 'tickcolor', 'tickfont', 'tickformat',
        'tickformatstops', 'ticklen', 'tickmode', 'tickprefix', 'ticks',
        'ticksuffix', 'ticktext', 'ticktextsrc', 'tickvals', 'tickvalssrc',
        'tickwidth', 'title', 'titlefont', 'titleside', 'x', 'xanchor', 'xpad',
        'y', 'yanchor', 'ypad']
    
    Run `<colorbar-object>.help('attribute')` on any of the above.
    '<colorbar-object>' is the object at []

    """
    _name = 'colorbar'


class Contour(PlotlyDict):
    """
    Valid attributes for 'contour' at path [] under parents ():
    
        ['autocolorscale', 'autocontour', 'colorbar', 'colorscale',
        'connectgaps', 'contours', 'customdata', 'customdatasrc', 'dx', 'dy',
        'fillcolor', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids',
        'idssrc', 'legendgroup', 'line', 'name', 'ncontours', 'opacity',
        'reversescale', 'selectedpoints', 'showlegend', 'showscale', 'stream',
        'text', 'textsrc', 'transpose', 'type', 'uid', 'visible', 'x', 'x0',
        'xaxis', 'xcalendar', 'xsrc', 'xtype', 'y', 'y0', 'yaxis', 'ycalendar',
        'ysrc', 'ytype', 'z', 'zauto', 'zhoverformat', 'zmax', 'zmin', 'zsrc']
    
    Run `<contour-object>.help('attribute')` on any of the above.
    '<contour-object>' is the object at []

    """
    _name = 'contour'


class Contourcarpet(PlotlyDict):
    """
    Valid attributes for 'contourcarpet' at path [] under parents ():
    
        ['a', 'a0', 'asrc', 'atype', 'autocolorscale', 'autocontour', 'b',
        'b0', 'bsrc', 'btype', 'carpet', 'colorbar', 'colorscale', 'contours',
        'customdata', 'customdatasrc', 'da', 'db', 'fillcolor', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc', 'legendgroup', 'line',
        'name', 'ncontours', 'opacity', 'reversescale', 'selectedpoints',
        'showlegend', 'showscale', 'stream', 'text', 'textsrc', 'transpose',
        'type', 'uid', 'visible', 'xaxis', 'yaxis', 'z', 'zauto', 'zmax',
        'zmin', 'zsrc']
    
    Run `<contourcarpet-object>.help('attribute')` on any of the above.
    '<contourcarpet-object>' is the object at []

    """
    _name = 'contourcarpet'


class Contours(PlotlyDict):
    """
    Valid attributes for 'contours' at path [] under parents ():
    
        ['coloring', 'end', 'labelfont', 'labelformat', 'operation',
        'showlabels', 'showlines', 'size', 'start', 'type', 'value', 'x', 'y',
        'z']
    
    Run `<contours-object>.help('attribute')` on any of the above.
    '<contours-object>' is the object at []

    """
    _name = 'contours'


class Data(PlotlyList):
    """
    Valid items for 'data' at path [] under parents ():
        ['Area', 'Bar', 'Box', 'Candlestick', 'Carpet', 'Choropleth',
        'Contour', 'Contourcarpet', 'Heatmap', 'Heatmapgl', 'Histogram',
        'Histogram2d', 'Histogram2dcontour', 'Mesh3d', 'Ohlc', 'Parcoords',
        'Pie', 'Pointcloud', 'Sankey', 'Scatter', 'Scatter3d', 'Scattercarpet',
        'Scattergeo', 'Scattergl', 'Scattermapbox', 'Scatterpolar',
        'Scatterpolargl', 'Scatterternary', 'Splom', 'Surface', 'Table',
        'Violin']

    """
    _name = 'data'

    def _value_to_graph_object(self, index, value, _raise=True):

        if not isinstance(value, dict):
            if _raise:
                notes = ['Entry should subclass dict.']
                path = self._get_path() + (index, )
                raise exceptions.PlotlyListEntryError(self, path,
                                                      notes=notes)
            else:
                return

        item = value.get('type', 'scatter')
        if item not in graph_reference.ARRAYS['data']['items']:
            if _raise:
                path = self._get_path() + (0, )
                raise exceptions.PlotlyDataTypeError(self, path)

        return GraphObjectFactory.create(item, _raise=_raise,
                                         _parent=self,
                                         _parent_key=index, **value)

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        if flatten:
            data = [v.get_data(flatten=flatten) for v in self]
            d = {}
            taken_names = []
            for i, trace in enumerate(data):

                # we want to give the traces helpful names
                # however, we need to be sure they're unique too...
                trace_name = trace.pop('name', 'trace_{0}'.format(i))
                if trace_name in taken_names:
                    j = 1
                    new_trace_name = "{0}_{1}".format(trace_name, j)
                    while new_trace_name in taken_names:
                        new_trace_name = (
                            "{0}_{1}".format(trace_name, j)
                        )
                        j += 1
                    trace_name = new_trace_name
                taken_names.append(trace_name)

                # finish up the dot-concatenation
                for k, v in trace.items():
                    key = "{0}.{1}".format(trace_name, k)
                    d[key] = v
            return d
        else:
            return super(Data, self).get_data(flatten=flatten)


class ErrorX(PlotlyDict):
    """
    Valid attributes for 'error_x' at path [] under parents ():
    
        ['array', 'arrayminus', 'arrayminussrc', 'arraysrc', 'color',
        'copy_ystyle', 'copy_zstyle', 'opacity', 'symmetric', 'thickness',
        'traceref', 'tracerefminus', 'type', 'value', 'valueminus', 'visible',
        'width']
    
    Run `<error_x-object>.help('attribute')` on any of the above.
    '<error_x-object>' is the object at []

    """
    _name = 'error_x'


class ErrorY(PlotlyDict):
    """
    Valid attributes for 'error_y' at path [] under parents ():
    
        ['array', 'arrayminus', 'arrayminussrc', 'arraysrc', 'color',
        'copy_zstyle', 'opacity', 'symmetric', 'thickness', 'traceref',
        'tracerefminus', 'type', 'value', 'valueminus', 'visible', 'width']
    
    Run `<error_y-object>.help('attribute')` on any of the above.
    '<error_y-object>' is the object at []

    """
    _name = 'error_y'


class ErrorZ(PlotlyDict):
    """
    Valid attributes for 'error_z' at path [] under parents ():
    
        ['array', 'arrayminus', 'arrayminussrc', 'arraysrc', 'color',
        'opacity', 'symmetric', 'thickness', 'traceref', 'tracerefminus',
        'type', 'value', 'valueminus', 'visible', 'width']
    
    Run `<error_z-object>.help('attribute')` on any of the above.
    '<error_z-object>' is the object at []

    """
    _name = 'error_z'


class Figure(PlotlyDict):
    """
    Valid attributes for 'figure' at path [] under parents ():
    
        ['data', 'frames', 'layout']
    
    Run `<figure-object>.help('attribute')` on any of the above.
    '<figure-object>' is the object at []

    """
    _name = 'figure'

    def __init__(self, *args, **kwargs):
        super(Figure, self).__init__(*args, **kwargs)
        if 'data' not in self:
            self.data = Data(_parent=self, _parent_key='data')

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        Flattening may increase the utility of the result.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        return self.data.get_data(flatten=flatten)

    def to_dataframe(self):
        """
        Create a dataframe with trace names and keys as column names.

        :return: (DataFrame)

        """
        data = self.get_data(flatten=True)
        from pandas import DataFrame, Series
        return DataFrame(
            dict([(k, Series(v)) for k, v in data.items()]))

    def print_grid(self):
        """
        Print a visual layout of the figure's axes arrangement.

        This is only valid for figures that are created
        with plotly.tools.make_subplots.

        """
        try:
            grid_str = self.__dict__['_grid_str']
        except AttributeError:
            raise Exception("Use plotly.tools.make_subplots "
                            "to create a subplot grid.")
        print(grid_str)

    def append_trace(self, trace, row, col):
        """
        Add a trace to your figure bound to axes at the row, col index.

        The row, col index is generated from figures created with
        plotly.tools.make_subplots and can be viewed with
        Figure.print_grid.

        :param (dict) trace: The data trace to be bound.
        :param (int) row: Subplot row index (see Figure.print_grid).
        :param (int) col: Subplot column index (see Figure.print_grid).

        Example:
        # stack two subplots vertically
        fig = tools.make_subplots(rows=2)

        This is the format of your plot grid:
        [ (1,1) x1,y1 ]
        [ (2,1) x2,y2 ]

        fig.append_trace(Scatter(x=[1,2,3], y=[2,1,2]), 1, 1)
        fig.append_trace(Scatter(x=[1,2,3], y=[2,1,2]), 2, 1)

        """
        try:
            grid_ref = self._grid_ref
        except AttributeError:
            raise Exception("In order to use Figure.append_trace, "
                            "you must first use "
                            "plotly.tools.make_subplots "
                            "to create a subplot grid.")
        if row <= 0:
            raise Exception("Row value is out of range. "
                            "Note: the starting cell is (1, 1)")
        if col <= 0:
            raise Exception("Col value is out of range. "
                            "Note: the starting cell is (1, 1)")
        try:
            ref = grid_ref[row-1][col-1]
        except IndexError:
            raise Exception("The (row, col) pair sent is out of "
                            "range. Use Figure.print_grid to view the "
                            "subplot grid. ")
        if 'scene' in ref[0]:
            trace['scene'] = ref[0]
            if ref[0] not in self['layout']:
                raise Exception("Something went wrong. "
                                "The scene object for ({r},{c}) "
                                "subplot cell "
                                "got deleted.".format(r=row, c=col))
        else:
            xaxis_key = "xaxis{ref}".format(ref=ref[0][1:])
            yaxis_key = "yaxis{ref}".format(ref=ref[1][1:])
            if (xaxis_key not in self['layout']
                    or yaxis_key not in self['layout']):
                raise Exception("Something went wrong. "
                                "An axis object for ({r},{c}) subplot "
                                "cell got deleted."
                                .format(r=row, c=col))
            trace['xaxis'] = ref[0]
            trace['yaxis'] = ref[1]
        self['data'] += [trace]


class Font(PlotlyDict):
    """
    Valid attributes for 'font' at path [] under parents ():
    
        ['color', 'colorsrc', 'family', 'familysrc', 'size', 'sizesrc']
    
    Run `<font-object>.help('attribute')` on any of the above.
    '<font-object>' is the object at []

    """
    _name = 'font'


class Frames(PlotlyList):
    """
    Valid items for 'frames' at path [] under parents ():
        ['dict']

    """
    _name = 'frames'

    def _value_to_graph_object(self, index, value, _raise=True):
        if isinstance(value, six.string_types):
            return value
        return super(Frames, self)._value_to_graph_object(index, value,
                                                          _raise=_raise)

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """Get formatted string by calling `to_string` on children items."""
        if not len(self):
            return "{name}()".format(name=self._get_class_name())
        string = "{name}([{eol}{indent}".format(
            name=self._get_class_name(),
            eol=eol,
            indent=' ' * indent * (level + 1))
        for index, entry in enumerate(self):
            if isinstance(entry, six.string_types):
                string += repr(entry)
            else:
                string += entry.to_string(level=level+1,
                                          indent=indent,
                                          eol=eol,
                                          pretty=pretty,
                                          max_chars=max_chars)
            if index < len(self) - 1:
                string += ",{eol}{indent}".format(
                    eol=eol,
                    indent=' ' * indent * (level + 1))
        string += (
            "{eol}{indent}])").format(eol=eol, indent=' ' * indent * level)
        return string


class Heatmap(PlotlyDict):
    """
    Valid attributes for 'heatmap' at path [] under parents ():
    
        ['autocolorscale', 'colorbar', 'colorscale', 'connectgaps',
        'customdata', 'customdatasrc', 'dx', 'dy', 'hoverinfo', 'hoverinfosrc',
        'hoverlabel', 'ids', 'idssrc', 'legendgroup', 'name', 'opacity',
        'reversescale', 'selectedpoints', 'showlegend', 'showscale', 'stream',
        'text', 'textsrc', 'transpose', 'type', 'uid', 'visible', 'x', 'x0',
        'xaxis', 'xcalendar', 'xgap', 'xsrc', 'xtype', 'y', 'y0', 'yaxis',
        'ycalendar', 'ygap', 'ysrc', 'ytype', 'z', 'zauto', 'zhoverformat',
        'zmax', 'zmin', 'zsmooth', 'zsrc']
    
    Run `<heatmap-object>.help('attribute')` on any of the above.
    '<heatmap-object>' is the object at []

    """
    _name = 'heatmap'


class Heatmapgl(PlotlyDict):
    """
    Valid attributes for 'heatmapgl' at path [] under parents ():
    
        ['autocolorscale', 'colorbar', 'colorscale', 'customdata',
        'customdatasrc', 'dx', 'dy', 'hoverinfo', 'hoverinfosrc', 'hoverlabel',
        'ids', 'idssrc', 'legendgroup', 'name', 'opacity', 'reversescale',
        'selectedpoints', 'showlegend', 'showscale', 'stream', 'text',
        'textsrc', 'transpose', 'type', 'uid', 'visible', 'x', 'x0', 'xaxis',
        'xsrc', 'xtype', 'y', 'y0', 'yaxis', 'ysrc', 'ytype', 'z', 'zauto',
        'zmax', 'zmin', 'zsrc']
    
    Run `<heatmapgl-object>.help('attribute')` on any of the above.
    '<heatmapgl-object>' is the object at []

    """
    _name = 'heatmapgl'


class Histogram(PlotlyDict):
    """
    Valid attributes for 'histogram' at path [] under parents ():
    
        ['autobinx', 'autobiny', 'bardir', 'cumulative', 'customdata',
        'customdatasrc', 'error_x', 'error_y', 'histfunc', 'histnorm',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc',
        'legendgroup', 'marker', 'name', 'nbinsx', 'nbinsy', 'opacity',
        'orientation', 'selected', 'selectedpoints', 'showlegend', 'stream',
        'text', 'textsrc', 'type', 'uid', 'unselected', 'visible', 'x',
        'xaxis', 'xbins', 'xcalendar', 'xsrc', 'y', 'yaxis', 'ybins',
        'ycalendar', 'ysrc']
    
    Run `<histogram-object>.help('attribute')` on any of the above.
    '<histogram-object>' is the object at []

    """
    _name = 'histogram'


class Histogram2d(PlotlyDict):
    """
    Valid attributes for 'histogram2d' at path [] under parents ():
    
        ['autobinx', 'autobiny', 'autocolorscale', 'colorbar', 'colorscale',
        'customdata', 'customdatasrc', 'histfunc', 'histnorm', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc', 'legendgroup', 'marker',
        'name', 'nbinsx', 'nbinsy', 'opacity', 'reversescale',
        'selectedpoints', 'showlegend', 'showscale', 'stream', 'type', 'uid',
        'visible', 'x', 'xaxis', 'xbins', 'xcalendar', 'xgap', 'xsrc', 'y',
        'yaxis', 'ybins', 'ycalendar', 'ygap', 'ysrc', 'z', 'zauto',
        'zhoverformat', 'zmax', 'zmin', 'zsmooth', 'zsrc']
    
    Run `<histogram2d-object>.help('attribute')` on any of the above.
    '<histogram2d-object>' is the object at []

    """
    _name = 'histogram2d'


class Histogram2dContour(PlotlyDict):
    """
    Valid attributes for 'histogram2dcontour' at path [] under parents ():
    
        ['autobinx', 'autobiny', 'autocolorscale', 'autocontour', 'colorbar',
        'colorscale', 'contours', 'customdata', 'customdatasrc', 'histfunc',
        'histnorm', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc',
        'legendgroup', 'line', 'marker', 'name', 'nbinsx', 'nbinsy',
        'ncontours', 'opacity', 'reversescale', 'selectedpoints', 'showlegend',
        'showscale', 'stream', 'type', 'uid', 'visible', 'x', 'xaxis', 'xbins',
        'xcalendar', 'xsrc', 'y', 'yaxis', 'ybins', 'ycalendar', 'ysrc', 'z',
        'zauto', 'zhoverformat', 'zmax', 'zmin', 'zsrc']
    
    Run `<histogram2dcontour-object>.help('attribute')` on any of the above.
    '<histogram2dcontour-object>' is the object at []

    """
    _name = 'histogram2dcontour'


class Histogram2dcontour(PlotlyDict):
    """
    Valid attributes for 'histogram2dcontour' at path [] under parents ():
    
        ['autobinx', 'autobiny', 'autocolorscale', 'autocontour', 'colorbar',
        'colorscale', 'contours', 'customdata', 'customdatasrc', 'histfunc',
        'histnorm', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc',
        'legendgroup', 'line', 'marker', 'name', 'nbinsx', 'nbinsy',
        'ncontours', 'opacity', 'reversescale', 'selectedpoints', 'showlegend',
        'showscale', 'stream', 'type', 'uid', 'visible', 'x', 'xaxis', 'xbins',
        'xcalendar', 'xsrc', 'y', 'yaxis', 'ybins', 'ycalendar', 'ysrc', 'z',
        'zauto', 'zhoverformat', 'zmax', 'zmin', 'zsrc']
    
    Run `<histogram2dcontour-object>.help('attribute')` on any of the above.
    '<histogram2dcontour-object>' is the object at []

    """
    _name = 'histogram2dcontour'


class Layout(PlotlyDict):
    """
    Valid attributes for 'layout' at path [] under parents ():
    
        ['angularaxis', 'annotations', 'autosize', 'bargap', 'bargroupgap',
        'barmode', 'barnorm', 'boxgap', 'boxgroupgap', 'boxmode', 'calendar',
        'colorway', 'datarevision', 'direction', 'dragmode', 'font', 'geo',
        'grid', 'height', 'hiddenlabels', 'hiddenlabelssrc', 'hidesources',
        'hoverdistance', 'hoverlabel', 'hovermode', 'images', 'legend',
        'mapbox', 'margin', 'orientation', 'paper_bgcolor', 'plot_bgcolor',
        'polar', 'radialaxis', 'scene', 'selectdirection', 'separators',
        'shapes', 'showlegend', 'sliders', 'spikedistance', 'ternary', 'title',
        'titlefont', 'updatemenus', 'violingap', 'violingroupgap',
        'violinmode', 'width', 'xaxis', 'yaxis']
    
    Run `<layout-object>.help('attribute')` on any of the above.
    '<layout-object>' is the object at []

    """
    _name = 'layout'


class Legend(PlotlyDict):
    """
    Valid attributes for 'legend' at path [] under parents ():
    
        ['bgcolor', 'bordercolor', 'borderwidth', 'font', 'orientation',
        'tracegroupgap', 'traceorder', 'x', 'xanchor', 'y', 'yanchor']
    
    Run `<legend-object>.help('attribute')` on any of the above.
    '<legend-object>' is the object at []

    """
    _name = 'legend'


class Line(PlotlyDict):
    """
    Valid attributes for 'line' at path [] under parents ():
    
        ['autocolorscale', 'cauto', 'cmax', 'cmin', 'color', 'colorbar',
        'colorscale', 'colorsrc', 'dash', 'outliercolor', 'outlierwidth',
        'reversescale', 'shape', 'showscale', 'simplify', 'smoothing', 'width',
        'widthsrc']
    
    Run `<line-object>.help('attribute')` on any of the above.
    '<line-object>' is the object at []

    """
    _name = 'line'


class Margin(PlotlyDict):
    """
    Valid attributes for 'margin' at path [] under parents ():
    
        ['autoexpand', 'b', 'l', 'pad', 'r', 't']
    
    Run `<margin-object>.help('attribute')` on any of the above.
    '<margin-object>' is the object at []

    """
    _name = 'margin'


class Marker(PlotlyDict):
    """
    Valid attributes for 'marker' at path [] under parents ():
    
        ['autocolorscale', 'blend', 'border', 'cauto', 'cmax', 'cmin', 'color',
        'colorbar', 'colors', 'colorscale', 'colorsrc', 'colorssrc',
        'gradient', 'line', 'maxdisplayed', 'opacity', 'opacitysrc',
        'outliercolor', 'reversescale', 'showscale', 'size', 'sizemax',
        'sizemin', 'sizemode', 'sizeref', 'sizesrc', 'symbol', 'symbolsrc']
    
    Run `<marker-object>.help('attribute')` on any of the above.
    '<marker-object>' is the object at []

    """
    _name = 'marker'


class Mesh3d(PlotlyDict):
    """
    Valid attributes for 'mesh3d' at path [] under parents ():
    
        ['alphahull', 'autocolorscale', 'cauto', 'cmax', 'cmin', 'color',
        'colorbar', 'colorscale', 'contour', 'customdata', 'customdatasrc',
        'delaunayaxis', 'facecolor', 'facecolorsrc', 'flatshading',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'i', 'ids', 'idssrc',
        'intensity', 'intensitysrc', 'isrc', 'j', 'jsrc', 'k', 'ksrc',
        'legendgroup', 'lighting', 'lightposition', 'name', 'opacity',
        'reversescale', 'scene', 'selectedpoints', 'showlegend', 'showscale',
        'stream', 'text', 'textsrc', 'type', 'uid', 'vertexcolor',
        'vertexcolorsrc', 'visible', 'x', 'xcalendar', 'xsrc', 'y',
        'ycalendar', 'ysrc', 'z', 'zcalendar', 'zsrc']
    
    Run `<mesh3d-object>.help('attribute')` on any of the above.
    '<mesh3d-object>' is the object at []

    """
    _name = 'mesh3d'


class Ohlc(PlotlyDict):
    """
    Valid attributes for 'ohlc' at path [] under parents ():
    
        ['close', 'closesrc', 'customdata', 'customdatasrc', 'decreasing',
        'high', 'highsrc', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids',
        'idssrc', 'increasing', 'legendgroup', 'line', 'low', 'lowsrc', 'name',
        'opacity', 'open', 'opensrc', 'selectedpoints', 'showlegend', 'stream',
        'text', 'textsrc', 'tickwidth', 'type', 'uid', 'visible', 'x', 'xaxis',
        'xcalendar', 'xsrc', 'yaxis']
    
    Run `<ohlc-object>.help('attribute')` on any of the above.
    '<ohlc-object>' is the object at []

    """
    _name = 'ohlc'


class Parcoords(PlotlyDict):
    """
    Valid attributes for 'parcoords' at path [] under parents ():
    
        ['customdata', 'customdatasrc', 'dimensions', 'domain', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc', 'labelfont',
        'legendgroup', 'line', 'name', 'opacity', 'rangefont',
        'selectedpoints', 'showlegend', 'stream', 'tickfont', 'type', 'uid',
        'visible']
    
    Run `<parcoords-object>.help('attribute')` on any of the above.
    '<parcoords-object>' is the object at []

    """
    _name = 'parcoords'


class Pie(PlotlyDict):
    """
    Valid attributes for 'pie' at path [] under parents ():
    
        ['customdata', 'customdatasrc', 'direction', 'dlabel', 'domain',
        'hole', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hovertext',
        'hovertextsrc', 'ids', 'idssrc', 'insidetextfont', 'label0', 'labels',
        'labelssrc', 'legendgroup', 'marker', 'name', 'opacity',
        'outsidetextfont', 'pull', 'pullsrc', 'rotation', 'scalegroup',
        'selectedpoints', 'showlegend', 'sort', 'stream', 'text', 'textfont',
        'textinfo', 'textposition', 'textpositionsrc', 'textsrc', 'type',
        'uid', 'values', 'valuessrc', 'visible']
    
    Run `<pie-object>.help('attribute')` on any of the above.
    '<pie-object>' is the object at []

    """
    _name = 'pie'


class Pointcloud(PlotlyDict):
    """
    Valid attributes for 'pointcloud' at path [] under parents ():
    
        ['customdata', 'customdatasrc', 'hoverinfo', 'hoverinfosrc',
        'hoverlabel', 'ids', 'idssrc', 'indices', 'indicessrc', 'legendgroup',
        'marker', 'name', 'opacity', 'selectedpoints', 'showlegend', 'stream',
        'text', 'textsrc', 'type', 'uid', 'visible', 'x', 'xaxis', 'xbounds',
        'xboundssrc', 'xsrc', 'xy', 'xysrc', 'y', 'yaxis', 'ybounds',
        'yboundssrc', 'ysrc']
    
    Run `<pointcloud-object>.help('attribute')` on any of the above.
    '<pointcloud-object>' is the object at []

    """
    _name = 'pointcloud'


class RadialAxis(PlotlyDict):
    """
    Valid attributes for 'radialaxis' at path [] under parents ():
    
        ['angle', 'autorange', 'calendar', 'categoryarray', 'categoryarraysrc',
        'categoryorder', 'color', 'domain', 'dtick', 'endpadding',
        'exponentformat', 'gridcolor', 'gridwidth', 'hoverformat', 'layer',
        'linecolor', 'linewidth', 'nticks', 'orientation', 'range',
        'rangemode', 'separatethousands', 'showexponent', 'showgrid',
        'showline', 'showticklabels', 'showtickprefix', 'showticksuffix',
        'side', 'tick0', 'tickangle', 'tickcolor', 'tickfont', 'tickformat',
        'tickformatstops', 'ticklen', 'tickmode', 'tickorientation',
        'tickprefix', 'ticks', 'ticksuffix', 'ticktext', 'ticktextsrc',
        'tickvals', 'tickvalssrc', 'tickwidth', 'title', 'titlefont', 'type',
        'visible']
    
    Run `<radialaxis-object>.help('attribute')` on any of the above.
    '<radialaxis-object>' is the object at []

    """
    _name = 'radialaxis'


class Sankey(PlotlyDict):
    """
    Valid attributes for 'sankey' at path [] under parents ():
    
        ['arrangement', 'customdata', 'customdatasrc', 'domain', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc', 'legendgroup', 'link',
        'name', 'node', 'opacity', 'orientation', 'selectedpoints',
        'showlegend', 'stream', 'textfont', 'type', 'uid', 'valueformat',
        'valuesuffix', 'visible']
    
    Run `<sankey-object>.help('attribute')` on any of the above.
    '<sankey-object>' is the object at []

    """
    _name = 'sankey'


class Scatter(PlotlyDict):
    """
    Valid attributes for 'scatter' at path [] under parents ():
    
        ['cliponaxis', 'connectgaps', 'customdata', 'customdatasrc', 'dx',
        'dy', 'error_x', 'error_y', 'fill', 'fillcolor', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'hoveron', 'hovertext', 'hovertextsrc',
        'ids', 'idssrc', 'legendgroup', 'line', 'marker', 'mode', 'name',
        'opacity', 'r', 'rsrc', 'selected', 'selectedpoints', 'showlegend',
        'stream', 't', 'text', 'textfont', 'textposition', 'textpositionsrc',
        'textsrc', 'tsrc', 'type', 'uid', 'unselected', 'visible', 'x', 'x0',
        'xaxis', 'xcalendar', 'xsrc', 'y', 'y0', 'yaxis', 'ycalendar', 'ysrc']
    
    Run `<scatter-object>.help('attribute')` on any of the above.
    '<scatter-object>' is the object at []

    """
    _name = 'scatter'


class Scatter3d(PlotlyDict):
    """
    Valid attributes for 'scatter3d' at path [] under parents ():
    
        ['connectgaps', 'customdata', 'customdatasrc', 'error_x', 'error_y',
        'error_z', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hovertext',
        'hovertextsrc', 'ids', 'idssrc', 'legendgroup', 'line', 'marker',
        'mode', 'name', 'opacity', 'projection', 'scene', 'selectedpoints',
        'showlegend', 'stream', 'surfaceaxis', 'surfacecolor', 'text',
        'textfont', 'textposition', 'textpositionsrc', 'textsrc', 'type',
        'uid', 'visible', 'x', 'xcalendar', 'xsrc', 'y', 'ycalendar', 'ysrc',
        'z', 'zcalendar', 'zsrc']
    
    Run `<scatter3d-object>.help('attribute')` on any of the above.
    '<scatter3d-object>' is the object at []

    """
    _name = 'scatter3d'


class Scattercarpet(PlotlyDict):
    """
    Valid attributes for 'scattercarpet' at path [] under parents ():
    
        ['a', 'asrc', 'b', 'bsrc', 'carpet', 'connectgaps', 'customdata',
        'customdatasrc', 'fill', 'fillcolor', 'hoverinfo', 'hoverinfosrc',
        'hoverlabel', 'hoveron', 'ids', 'idssrc', 'legendgroup', 'line',
        'marker', 'mode', 'name', 'opacity', 'selected', 'selectedpoints',
        'showlegend', 'stream', 'text', 'textfont', 'textposition',
        'textpositionsrc', 'textsrc', 'type', 'uid', 'unselected', 'visible',
        'xaxis', 'yaxis']
    
    Run `<scattercarpet-object>.help('attribute')` on any of the above.
    '<scattercarpet-object>' is the object at []

    """
    _name = 'scattercarpet'


class Scattergeo(PlotlyDict):
    """
    Valid attributes for 'scattergeo' at path [] under parents ():
    
        ['connectgaps', 'customdata', 'customdatasrc', 'fill', 'fillcolor',
        'geo', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hovertext',
        'hovertextsrc', 'ids', 'idssrc', 'lat', 'latsrc', 'legendgroup',
        'line', 'locationmode', 'locations', 'locationssrc', 'lon', 'lonsrc',
        'marker', 'mode', 'name', 'opacity', 'selected', 'selectedpoints',
        'showlegend', 'stream', 'text', 'textfont', 'textposition',
        'textpositionsrc', 'textsrc', 'type', 'uid', 'unselected', 'visible']
    
    Run `<scattergeo-object>.help('attribute')` on any of the above.
    '<scattergeo-object>' is the object at []

    """
    _name = 'scattergeo'


class Scattergl(PlotlyDict):
    """
    Valid attributes for 'scattergl' at path [] under parents ():
    
        ['connectgaps', 'customdata', 'customdatasrc', 'dx', 'dy', 'error_x',
        'error_y', 'fill', 'fillcolor', 'hoverinfo', 'hoverinfosrc',
        'hoverlabel', 'hoveron', 'ids', 'idssrc', 'legendgroup', 'line',
        'marker', 'mode', 'name', 'opacity', 'selected', 'selectedpoints',
        'showlegend', 'stream', 'text', 'textsrc', 'type', 'uid', 'unselected',
        'visible', 'x', 'x0', 'xaxis', 'xcalendar', 'xsrc', 'y', 'y0', 'yaxis',
        'ycalendar', 'ysrc']
    
    Run `<scattergl-object>.help('attribute')` on any of the above.
    '<scattergl-object>' is the object at []

    """
    _name = 'scattergl'


class Scattermapbox(PlotlyDict):
    """
    Valid attributes for 'scattermapbox' at path [] under parents ():
    
        ['connectgaps', 'customdata', 'customdatasrc', 'fill', 'fillcolor',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hovertext', 'hovertextsrc',
        'ids', 'idssrc', 'lat', 'latsrc', 'legendgroup', 'line', 'lon',
        'lonsrc', 'marker', 'mode', 'name', 'opacity', 'selected',
        'selectedpoints', 'showlegend', 'stream', 'subplot', 'text',
        'textfont', 'textposition', 'textsrc', 'type', 'uid', 'unselected',
        'visible']
    
    Run `<scattermapbox-object>.help('attribute')` on any of the above.
    '<scattermapbox-object>' is the object at []

    """
    _name = 'scattermapbox'


class Scatterpolar(PlotlyDict):
    """
    Valid attributes for 'scatterpolar' at path [] under parents ():
    
        ['cliponaxis', 'connectgaps', 'customdata', 'customdatasrc', 'fill',
        'fillcolor', 'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hoveron',
        'hovertext', 'hovertextsrc', 'ids', 'idssrc', 'legendgroup', 'line',
        'marker', 'mode', 'name', 'opacity', 'r', 'rsrc', 'selected',
        'selectedpoints', 'showlegend', 'stream', 'subplot', 'text',
        'textfont', 'textposition', 'textpositionsrc', 'textsrc', 'theta',
        'thetasrc', 'thetaunit', 'type', 'uid', 'unselected', 'visible']
    
    Run `<scatterpolar-object>.help('attribute')` on any of the above.
    '<scatterpolar-object>' is the object at []

    """
    _name = 'scatterpolar'


class Scatterpolargl(PlotlyDict):
    """
    Valid attributes for 'scatterpolargl' at path [] under parents ():
    
        ['connectgaps', 'customdata', 'customdatasrc', 'fill', 'fillcolor',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hoveron', 'ids', 'idssrc',
        'legendgroup', 'line', 'marker', 'mode', 'name', 'opacity', 'r',
        'rsrc', 'selected', 'selectedpoints', 'showlegend', 'stream',
        'subplot', 'text', 'textsrc', 'theta', 'thetasrc', 'thetaunit', 'type',
        'uid', 'unselected', 'visible']
    
    Run `<scatterpolargl-object>.help('attribute')` on any of the above.
    '<scatterpolargl-object>' is the object at []

    """
    _name = 'scatterpolargl'


class Scatterternary(PlotlyDict):
    """
    Valid attributes for 'scatterternary' at path [] under parents ():
    
        ['a', 'asrc', 'b', 'bsrc', 'c', 'cliponaxis', 'connectgaps', 'csrc',
        'customdata', 'customdatasrc', 'fill', 'fillcolor', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'hoveron', 'hovertext', 'hovertextsrc',
        'ids', 'idssrc', 'legendgroup', 'line', 'marker', 'mode', 'name',
        'opacity', 'selected', 'selectedpoints', 'showlegend', 'stream',
        'subplot', 'sum', 'text', 'textfont', 'textposition',
        'textpositionsrc', 'textsrc', 'type', 'uid', 'unselected', 'visible']
    
    Run `<scatterternary-object>.help('attribute')` on any of the above.
    '<scatterternary-object>' is the object at []

    """
    _name = 'scatterternary'


class Scene(PlotlyDict):
    """
    Valid attributes for 'scene' at path [] under parents ():
    
        ['annotations', 'aspectmode', 'aspectratio', 'bgcolor', 'camera',
        'cameraposition', 'domain', 'dragmode', 'hovermode', 'xaxis', 'yaxis',
        'zaxis']
    
    Run `<scene-object>.help('attribute')` on any of the above.
    '<scene-object>' is the object at []

    """
    _name = 'scene'


class Splom(PlotlyDict):
    """
    Valid attributes for 'splom' at path [] under parents ():
    
        ['customdata', 'customdatasrc', 'diagonal', 'dimensions', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc', 'legendgroup', 'marker',
        'name', 'opacity', 'selected', 'selectedpoints', 'showlegend',
        'showlowerhalf', 'showupperhalf', 'stream', 'text', 'textsrc', 'type',
        'uid', 'unselected', 'visible', 'xaxes', 'yaxes']
    
    Run `<splom-object>.help('attribute')` on any of the above.
    '<splom-object>' is the object at []

    """
    _name = 'splom'


class Stream(PlotlyDict):
    """
    Valid attributes for 'stream' at path [] under parents ():
    
        ['maxpoints', 'token']
    
    Run `<stream-object>.help('attribute')` on any of the above.
    '<stream-object>' is the object at []

    """
    _name = 'stream'


class Surface(PlotlyDict):
    """
    Valid attributes for 'surface' at path [] under parents ():
    
        ['autocolorscale', 'cauto', 'cmax', 'cmin', 'colorbar', 'colorscale',
        'contours', 'customdata', 'customdatasrc', 'hidesurface', 'hoverinfo',
        'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc', 'legendgroup',
        'lighting', 'lightposition', 'name', 'opacity', 'reversescale',
        'scene', 'selectedpoints', 'showlegend', 'showscale', 'stream',
        'surfacecolor', 'surfacecolorsrc', 'text', 'textsrc', 'type', 'uid',
        'visible', 'x', 'xcalendar', 'xsrc', 'y', 'ycalendar', 'ysrc', 'z',
        'zauto', 'zcalendar', 'zmax', 'zmin', 'zsrc']
    
    Run `<surface-object>.help('attribute')` on any of the above.
    '<surface-object>' is the object at []

    """
    _name = 'surface'


class Table(PlotlyDict):
    """
    Valid attributes for 'table' at path [] under parents ():
    
        ['cells', 'columnorder', 'columnordersrc', 'columnwidth',
        'columnwidthsrc', 'customdata', 'customdatasrc', 'domain', 'header',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'ids', 'idssrc',
        'legendgroup', 'name', 'opacity', 'selectedpoints', 'showlegend',
        'stream', 'type', 'uid', 'visible']
    
    Run `<table-object>.help('attribute')` on any of the above.
    '<table-object>' is the object at []

    """
    _name = 'table'


class Trace(dict):
    pass


class Violin(PlotlyDict):
    """
    Valid attributes for 'violin' at path [] under parents ():
    
        ['bandwidth', 'box', 'customdata', 'customdatasrc', 'fillcolor',
        'hoverinfo', 'hoverinfosrc', 'hoverlabel', 'hoveron', 'ids', 'idssrc',
        'jitter', 'legendgroup', 'line', 'marker', 'meanline', 'name',
        'opacity', 'orientation', 'pointpos', 'points', 'scalegroup',
        'scalemode', 'selected', 'selectedpoints', 'showlegend', 'side',
        'span', 'spanmode', 'stream', 'text', 'textsrc', 'type', 'uid',
        'unselected', 'visible', 'x', 'x0', 'xaxis', 'xsrc', 'y', 'y0',
        'yaxis', 'ysrc']
    
    Run `<violin-object>.help('attribute')` on any of the above.
    '<violin-object>' is the object at []

    """
    _name = 'violin'


class XAxis(PlotlyDict):
    """
    Valid attributes for 'xaxis' at path [] under parents ():
    
        ['anchor', 'automargin', 'autorange', 'autotick', 'backgroundcolor',
        'calendar', 'categoryarray', 'categoryarraysrc', 'categoryorder',
        'color', 'constrain', 'constraintoward', 'domain', 'dtick',
        'exponentformat', 'fixedrange', 'gridcolor', 'gridwidth',
        'hoverformat', 'layer', 'linecolor', 'linewidth', 'mirror', 'nticks',
        'overlaying', 'position', 'range', 'rangemode', 'rangeselector',
        'rangeslider', 'scaleanchor', 'scaleratio', 'separatethousands',
        'showaxeslabels', 'showbackground', 'showexponent', 'showgrid',
        'showline', 'showspikes', 'showticklabels', 'showtickprefix',
        'showticksuffix', 'side', 'spikecolor', 'spikedash', 'spikemode',
        'spikesides', 'spikesnap', 'spikethickness', 'tick0', 'tickangle',
        'tickcolor', 'tickfont', 'tickformat', 'tickformatstops', 'ticklen',
        'tickmode', 'tickprefix', 'ticks', 'ticksuffix', 'ticktext',
        'ticktextsrc', 'tickvals', 'tickvalssrc', 'tickwidth', 'title',
        'titlefont', 'type', 'visible', 'zeroline', 'zerolinecolor',
        'zerolinewidth']
    
    Run `<xaxis-object>.help('attribute')` on any of the above.
    '<xaxis-object>' is the object at []

    """
    _name = 'xaxis'


class XBins(PlotlyDict):
    """
    Valid attributes for 'xbins' at path [] under parents ():
    
        ['end', 'size', 'start']
    
    Run `<xbins-object>.help('attribute')` on any of the above.
    '<xbins-object>' is the object at []

    """
    _name = 'xbins'


class YAxis(PlotlyDict):
    """
    Valid attributes for 'yaxis' at path [] under parents ():
    
        ['anchor', 'automargin', 'autorange', 'autotick', 'backgroundcolor',
        'calendar', 'categoryarray', 'categoryarraysrc', 'categoryorder',
        'color', 'constrain', 'constraintoward', 'domain', 'dtick',
        'exponentformat', 'fixedrange', 'gridcolor', 'gridwidth',
        'hoverformat', 'layer', 'linecolor', 'linewidth', 'mirror', 'nticks',
        'overlaying', 'position', 'range', 'rangemode', 'scaleanchor',
        'scaleratio', 'separatethousands', 'showaxeslabels', 'showbackground',
        'showexponent', 'showgrid', 'showline', 'showspikes', 'showticklabels',
        'showtickprefix', 'showticksuffix', 'side', 'spikecolor', 'spikedash',
        'spikemode', 'spikesides', 'spikesnap', 'spikethickness', 'tick0',
        'tickangle', 'tickcolor', 'tickfont', 'tickformat', 'tickformatstops',
        'ticklen', 'tickmode', 'tickprefix', 'ticks', 'ticksuffix', 'ticktext',
        'ticktextsrc', 'tickvals', 'tickvalssrc', 'tickwidth', 'title',
        'titlefont', 'type', 'visible', 'zeroline', 'zerolinecolor',
        'zerolinewidth']
    
    Run `<yaxis-object>.help('attribute')` on any of the above.
    '<yaxis-object>' is the object at []

    """
    _name = 'yaxis'


class YBins(PlotlyDict):
    """
    Valid attributes for 'ybins' at path [] under parents ():
    
        ['end', 'size', 'start']
    
    Run `<ybins-object>.help('attribute')` on any of the above.
    '<ybins-object>' is the object at []

    """
    _name = 'ybins'


class ZAxis(PlotlyDict):
    """
    Valid attributes for 'zaxis' at path [] under parents ():
    
        ['autorange', 'backgroundcolor', 'calendar', 'categoryarray',
        'categoryarraysrc', 'categoryorder', 'color', 'dtick',
        'exponentformat', 'gridcolor', 'gridwidth', 'hoverformat', 'linecolor',
        'linewidth', 'mirror', 'nticks', 'range', 'rangemode',
        'separatethousands', 'showaxeslabels', 'showbackground',
        'showexponent', 'showgrid', 'showline', 'showspikes', 'showticklabels',
        'showtickprefix', 'showticksuffix', 'spikecolor', 'spikesides',
        'spikethickness', 'tick0', 'tickangle', 'tickcolor', 'tickfont',
        'tickformat', 'tickformatstops', 'ticklen', 'tickmode', 'tickprefix',
        'ticks', 'ticksuffix', 'ticktext', 'ticktextsrc', 'tickvals',
        'tickvalssrc', 'tickwidth', 'title', 'titlefont', 'type', 'visible',
        'zeroline', 'zerolinecolor', 'zerolinewidth']
    
    Run `<zaxis-object>.help('attribute')` on any of the above.
    '<zaxis-object>' is the object at []

    """
    _name = 'zaxis'

__all__ = [cls for cls in graph_reference.CLASSES.keys() if cls in globals()]
