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
        specify the changes as a list of keyword agruments.

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


from plotly.datatypes import FigureWidget


# AUTO-GENERATED BELOW. DO NOT EDIT! See makefile.
class AngularAxis(dict):
    pass


class Annotation(dict):
    pass


class Annotations(list):
    pass


from plotly.datatypes.trace import Area


from plotly.datatypes.trace import Bar


from plotly.datatypes.trace import Box


from plotly.datatypes.trace import Candlestick


from plotly.datatypes.trace import Carpet


from plotly.datatypes.trace import Choropleth


class ColorBar(dict):
    pass


from plotly.datatypes.trace import Contour


from plotly.datatypes.trace import Contourcarpet


class Contours(dict):
    pass


class Data(list):
    pass


class ErrorX(dict):
    pass


class ErrorY(dict):
    pass


class ErrorZ(dict):
    pass


from plotly.datatypes import Figure


class Font(dict):
    pass


class Frames(list):
    pass


from plotly.datatypes.trace import Heatmap


from plotly.datatypes.trace import Heatmapgl


from plotly.datatypes.trace import Histogram


from plotly.datatypes.trace import Histogram2d


from plotly.datatypes.trace import Histogram2dContour


from plotly.datatypes import Layout


class Legend(dict):
    pass


class Line(dict):
    pass


class Margin(dict):
    pass


class Marker(dict):
    pass


from plotly.datatypes.trace import Mesh3d


from plotly.datatypes.trace import Ohlc


from plotly.datatypes.trace import Parcoords


from plotly.datatypes.trace import Pie


from plotly.datatypes.trace import Pointcloud


class RadialAxis(dict):
    pass


from plotly.datatypes.trace import Sankey


from plotly.datatypes.trace import Scatter


from plotly.datatypes.trace import Scatter3d


from plotly.datatypes.trace import Scattercarpet


from plotly.datatypes.trace import Scattergeo


from plotly.datatypes.trace import Scattergl


from plotly.datatypes.trace import Scattermapbox


from plotly.datatypes.trace import Scatterpolar


from plotly.datatypes.trace import Scatterpolargl


from plotly.datatypes.trace import Scatterternary


class Scene(dict):
    pass


class Stream(dict):
    pass


from plotly.datatypes.trace import Surface


from plotly.datatypes.trace import Table


class Trace(dict):
    pass


from plotly.datatypes.trace import Violin


class XAxis(dict):
    pass


class XBins(dict):
    pass


class YAxis(dict):
    pass


class YBins(dict):
    pass


class ZAxis(dict):
    pass


__all__ = [cls for cls in graph_reference.CLASSES.keys() if cls in globals()] + ["FigureWidget"]
