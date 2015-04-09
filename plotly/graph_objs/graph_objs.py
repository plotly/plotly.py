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

* Only mutate object structure when users ASK for it.

* It should always be possible to get a dict/list JSON representation from a
graph_objs object and it should always be possible to make a graph_objs object
from a dict/list JSON representation.

"""
from __future__ import absolute_import

import warnings
import six
from plotly.graph_objs import graph_objs_tools
from plotly.graph_objs.graph_objs_tools import (
    INFO, OBJ_MAP, NAME_TO_KEY, KEY_TO_NAME
)

from plotly import exceptions
from plotly import utils

import copy
import sys
if sys.version[:3] == '2.6':
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

__all__ = None


# (1) Make primitive graph objects
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
        if args and isinstance(args[0], dict):
            raise exceptions.PlotlyListEntryError(
                obj=self,
                index=0,
                notes="Just like a `list`, `{name}` must be instantiated with "
                      "a *single* collection.\n"
                      "In other words these are OK:\n"
                      ">>> {name}()\n"
                      ">>> {name}([])\n"
                      ">>> {name}([dict()])\n"
                      ">>> {name}([dict(), dict()])\n"
                      "However, these don't make sense:\n"
                      ">>> {name}(dict())\n"
                      ">>> {name}(dict(), dict())"
                      "".format(name=self.__class__.__name__)
            )
        self.validate()
        if self.__class__.__name__ == 'PlotlyList':
            warnings.warn("\nThe PlotlyList class is a base class of "
                          "list-like graph_objs.\nIt is not meant to be a "
                          "user interface.")

    def to_graph_objs(self, caller=True):
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyDict.
            2. Call `to_graph_objects` on each of these entries.

        """
        for index, entry in enumerate(self):
            if isinstance(entry, PlotlyDict):
                try:
                    entry.to_graph_objs(caller=False)
                except exceptions.PlotlyGraphObjectError as err:
                    err.add_to_error_path(index)
                    err.prepare()
                    raise  # re-raise current exception
            else:
                raise exceptions.PlotlyListEntryError(obj=self,
                                                      index=index,
                                                      entry=entry)

    def update(self, changes, make_copies=False):
        """Update current list with changed_list, which must be iterable.
        The 'changes' should be a list of dictionaries, however,
        it is permitted to be a single dict object.

        Because mutable objects contain references to their values, updating
        multiple items in a list will cause the items to all reference the same
        original set of objects. To change this behavior add
        `make_copies=True` which makes deep copies of the update items and
        therefore break references.

        """
        if isinstance(changes, dict):
            changes = [changes]
        self.to_graph_objs()
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
        """Strip style from the current representation.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.

        Keys that will be stripped in this process are tagged with
        `'type': 'style'` in graph_objs_meta.json.

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

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        Flattening may increase the utility of the result.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        self.to_graph_objs()
        l = list()
        for _plotlydict in self:
            l += [_plotlydict.get_data(flatten=flatten)]
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

    def validate(self, caller=True):
        """Recursively check the validity of the entries in a PlotlyList.

        PlotlyList may only contain suclasses of PlotlyDict, or dictionary-like
        objects that can be re-instantiated as subclasses of PlotlyDict.

        The validation process first requires that all nested collections be
        converted to the appropriate subclass of PlotlyDict/PlotlyList. Then,
        each of these objects call `validate` and so on, recursively,
        until the entire list has been validated.

        """
        if caller:  # change everything to PlotlyList/Dict objects
            try:
                self.to_graph_objs()
            except exceptions.PlotlyGraphObjectError as err:
                err.prepare()
                raise
        for index, entry in enumerate(self):
            if isinstance(entry, PlotlyDict):
                try:
                    entry.validate(caller=False)
                except exceptions.PlotlyGraphObjectError as err:
                    err.add_to_error_path(index)
                    err.prepare()
                    raise
            else:
                raise exceptions.PlotlyGraphObjectError(  # TODO!!!
                    message=(
                        "uh-oh, this error shouldn't have happenend."
                    ),
                    plain_message=(
                        "uh-oh, this error shouldn't have happenend."
                    ),
                    path=[index],
                )

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print(obj.to_string())

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\\n') -- set end of line character(s)
        pretty (default = True) -- curtail long list output with a '...'
        max_chars (default = 80) -- set max characters per line

        """
        self.to_graph_objs()
        if not len(self):
            return "{name}()".format(name=self.__class__.__name__)
        string = "{name}([{eol}{indent}".format(
            name=self.__class__.__name__,
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

    def get_ordered(self, caller=True):
        if caller:
            try:
                self.to_graph_objs(caller=False)
            except exceptions.PlotlyGraphObjectError as err:
                err.add_note("Could not order list because it could not be "
                             "converted to a valid graph object.")
                err.prepare()
                raise
        ordered_list = []
        for index, entry in enumerate(self):
            ordered_list += [entry.get_ordered()]
        return ordered_list

    def force_clean(self, caller=True):
        """Attempts to convert to graph_objs and calls force_clean() on entries.

        Calling force_clean() on a PlotlyList will ensure that the object is
        valid and may be sent to plotly. This process will remove any entries
        that end up with a length == 0. It will also remove itself from
        enclosing trivial structures if it is enclosed by a collection with
        length 1, meaning the data is the ONLY object in the collection.

        Careful! This will delete any invalid entries *silently*.

        """
        if caller:
            self.to_graph_objs()  # TODO add error handling here!
        for entry in self:
            entry.force_clean(caller=False)
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

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__

        for key in kwargs:
            if utils.is_source_key(key):
                kwargs[key] = self._assign_id_to_src(key, kwargs[key])

        super(PlotlyDict, self).__init__(*args, **kwargs)
        if issubclass(NAME_TO_CLASS[class_name], PlotlyTrace):
            if (class_name != 'PlotlyTrace') and (class_name != 'Trace'):
                self['type'] = NAME_TO_KEY[class_name]
        self.validate()
        if self.__class__.__name__ == 'PlotlyDict':
            warnings.warn("\nThe PlotlyDict class is a base class of "
                          "dictionary-like graph_objs.\nIt is not meant to be "
                          "a user interface.")

    def __setitem__(self, key, value):

        if key in ('xsrc', 'ysrc'):
            value = self._assign_id_to_src(key, value)

        return super(PlotlyDict, self).__setitem__(key, value)

    def _assign_id_to_src(self, src_name, src_value):
        if isinstance(src_value, six.string_types):
            src_id = src_value
        else:
            try:
                src_id = src_value.id
            except:
                err = ("{0} does not have an `id` property. "
                       "{1} needs to be assigned to either an "
                       "object with an `id` (like a "
                       "plotly.grid_objs.Column) or a string. "
                       "The `id` is a unique identifier "
                       "assigned by the Plotly webserver "
                       "to this grid column.")
                src_value_str = str(src_value)
                err = err.format(src_name, src_value_str)
                raise exceptions.InputError(err)

        if src_id == '':
            err = exceptions.COLUMN_NOT_YET_UPLOADED_MESSAGE
            err.format(column_name=src_value.name, reference=src_name)
            raise exceptions.InputError(err)
        return src_id

    def update(self, dict1=None, **dict2):
        """Update current dict with dict1 and then dict2.

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
        self.to_graph_objs()

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
        self.to_graph_objs()

    def strip_style(self):
        """Strip style from the current representation.

        All PlotlyDicts and PlotlyLists are guaranteed to survive the
        stripping process, though they made be left empty. This is allowable.

        Keys that will be stripped in this process are tagged with
        `'type': 'style'` in graph_objs_meta.json.

        This process first attempts to convert nested collections from dicts
        or lists to subclasses of PlotlyList/PlotlyDict. This process forces
        a validation, which may throw exceptions.

        Then, each of these objects call `strip_style` on themselves and so
        on, recursively until the entire structure has been validated and
        stripped.

        """
        self.to_graph_objs()
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        keys = list(self.keys())
        for key in keys:
            if isinstance(self[key], (PlotlyDict, PlotlyList)):
                self[key].strip_style()
            else:
                try:
                    if INFO[obj_key]['keymeta'][key]['key_type'] == 'style':

                        # TODO: use graph_objs_tools.value_is_data
                        if isinstance(self[key], six.string_types):
                            del self[key]
                        elif not hasattr(self[key], '__iter__'):
                            del self[key]
                except KeyError:  # TODO: Update the JSON
                    # print("'type' not in {0} for {1}".format(obj_key, key))
                    pass

    def get_data(self, flatten=False):
        """Returns the JSON for the plot with non-data elements stripped."""
        self.to_graph_objs()
        class_name = self.__class__.__name__
        obj_key = NAME_TO_KEY[class_name]
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
                try:
                    # TODO: Update the JSON
                    if graph_objs_tools.value_is_data(obj_key, key, val):
                        d[key] = val
                except KeyError:
                    pass
        keys = list(d.keys())
        for key in keys:
            if isinstance(d[key], (dict, list)):
                if len(d[key]) == 0:
                    del d[key]
        return d

    def to_graph_objs(self, caller=True):
        """Walk obj, convert dicts and lists to plotly graph objs.

        For each key in the object, if it corresponds to a special key that
        should be associated with a graph object, the ordinary dict or list
        will be reinitialized as a special PlotlyDict or PlotlyList of the
        appropriate `kind`.

        """
        info_key = NAME_TO_KEY[self.__class__.__name__]
        keys = self.keys()
        updated_keys = graph_objs_tools.update_keys(keys)
        for k_old, k_new in zip(keys, updated_keys):
            if k_old != k_new:
                self[k_new] = self.pop(k_old)
                warnings.warn(
                    "\n"
                    "The key, '{old}', has been depreciated, it's been "
                    "converted to '{new}'. You should change your code to use "
                    "'{new}' in the future."
                    "".format(old=k_old, new=k_new)
                )
        for key in updated_keys:
            if isinstance(self[key], (PlotlyDict, PlotlyList)):
                try:
                    self[key].to_graph_objs(caller=False)
                except exceptions.PlotlyGraphObjectError as err:
                    err.add_to_error_path(key)
                    err.prepare()
                    raise
            elif (key in INFO[info_key]['keymeta'].keys() and
                  'key_type' in INFO[info_key]['keymeta'][key].keys()):
                if INFO[info_key]['keymeta'][key]['key_type'] == 'object':
                    class_name = KEY_TO_NAME[key]
                    obj = get_class_instance_by_name(class_name)
                    if isinstance(obj, PlotlyDict):
                        if not isinstance(self[key], dict):
                            try:
                                val_types = (
                                    INFO[info_key]['keymeta'][key]['val_types']
                                )
                            except KeyError:
                                val_types = 'undocumented'
                            raise exceptions.PlotlyDictValueError(
                                obj=self,
                                key=key,
                                value=self[key],
                                val_types=val_types,
                                notes="value needs to be dictionary-like"
                            )
                        for k, v in list(self.pop(key).items()):
                            obj[k] = v  # finish up momentarily...
                    else:  # if not PlotlyDict, it MUST be a PlotlyList
                        if not isinstance(self[key], list):
                            try:
                                val_types = (
                                    INFO[info_key]['keymeta'][key]['val_types']
                                )
                            except KeyError:
                                val_types = 'undocumented'
                            raise exceptions.PlotlyDictValueError(  # TODO!!!
                                obj=self,
                                key=key,
                                value=self[key],
                                val_types=val_types,
                                notes="value needs to be list-like"
                            )
                        obj += self.pop(key)
                    try:
                        obj.to_graph_objs(caller=False)
                    except exceptions.PlotlyGraphObjectError as err:
                        err.add_to_error_path(key)
                        err.prepare()
                        raise
                    self[key] = obj  # whew! made it!

    def validate(self, caller=True):  # TODO: validate values too?
        """Recursively check the validity of the keys in a PlotlyDict.

        The valid keys constitute the entries in each object
        dictionary in graph_objs_meta.json

        The validation process first requires that all nested collections be
        converted to the appropriate subclass of PlotlyDict/PlotlyList. Then,
        each of these objects call `validate` and so on, recursively,
        until the entire object has been validated.

        """
        if caller:  # change everything to 'checkable' objs
            try:
                self.to_graph_objs(caller=False)
            except exceptions.PlotlyGraphObjectError as err:
                err.prepare()
                raise
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        for key, val in list(self.items()):
            if isinstance(val, (PlotlyDict, PlotlyList)):
                try:
                    val.validate(caller=False)
                except exceptions.PlotlyGraphObjectError as err:
                    err.add_to_error_path(key)
                    err.prepare()
                    raise
            else:
                if key in INFO[obj_key]['keymeta'].keys():
                    if 'key_type' not in INFO[obj_key]['keymeta'][key].keys():
                        continue  # TODO: 'type' may not be documented yet!
                    if INFO[obj_key]['keymeta'][key]['key_type'] == 'object':
                        try:
                            val_types = (
                                INFO[obj_key]['keymeta'][key]['val_types'])
                        except KeyError:
                            val_types = 'undocumented'
                        raise exceptions.PlotlyDictValueError(
                            obj=self,
                            key=key,
                            value=val,
                            val_types=val_types
                        )
                else:
                    matching_objects = [obj for obj in
                                        INFO if key in INFO[obj]['keymeta']]
                    notes = ''
                    if len(matching_objects):
                        notes += "That key is valid only in these objects:\n\n"
                        for obj in matching_objects:
                            notes += "\t{0}".format(KEY_TO_NAME[obj])
                            try:
                                notes += '({0}="{1}")\n'.format(
                                    repr(key),
                                    INFO[obj]['keymeta'][key]['val_types'])
                            except KeyError:
                                notes += '({0}="..")\n'.format(repr(key))
                        notes.expandtabs()
                    else:
                        notes += ("Couldn't find uses for key: {0}\n\n"
                                  "".format(repr(key)))
                    raise exceptions.PlotlyDictKeyError(obj=self,
                                                        key=key,
                                                        notes=notes)

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print(obj.to_string())

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\\n') -- set end of line character(s)
        pretty (default = True) -- curtail long list output with a '...'
        max_chars (default = 80) -- set max characters per line

        """
        self.to_graph_objs()  # todo, consider catching and re-raising?
        if not len(self):
            return "{name}()".format(name=self.__class__.__name__)
        string = "{name}(".format(name=self.__class__.__name__)
        index = 0
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        # This sets the order of the keys! nice.
        for key in INFO[obj_key]['keymeta']:
            if key in self:
                index += 1
                string += "{eol}{indent}{key}=".format(
                    eol=eol,
                    indent=' ' * indent * (level+1),
                    key=key)
                try:
                    string += self[key].to_string(level=level+1,
                                                  indent=indent,
                                                  eol=eol,
                                                  pretty=pretty,
                                                  max_chars=max_chars)
                except AttributeError:
                    if pretty:  # curtail representation if too many chars
                        max_len = (max_chars -
                                   indent*(level + 1) -
                                   len(key + "=") -
                                   len(eol))
                        if index < len(self):
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
                if index < len(self):
                    string += ","
                if index == len(self):  # TODO: extraneous...
                    break
        string += "{eol}{indent})".format(eol=eol, indent=' ' * indent * level)
        return string

    def get_ordered(self, caller=True):
        if caller:  # change everything to 'order-able' objs
            try:
                self.to_graph_objs(caller=False)
            except exceptions.PlotlyGraphObjectError as err:
                err.add_note("dictionary could not be ordered because it "
                             "could not be converted to a valid plotly graph "
                             "object.")
                err.prepare()
                raise
        obj_type = NAME_TO_KEY[self.__class__.__name__]
        ordered_dict = OrderedDict()
        # grab keys like xaxis1, xaxis2, etc...
        unordered_keys = [key for key in self
                          if key not in INFO[obj_type]['keymeta']]
        for key in INFO[obj_type]['keymeta']:
            if key in self:
                if isinstance(self[key], (PlotlyDict, PlotlyList)):
                    ordered_dict[key] = self[key].get_ordered(caller=False)
                else:
                    ordered_dict[key] = self[key]
        for key in unordered_keys:
            if isinstance(self[key], (PlotlyDict, PlotlyList)):
                ordered_dict[key] = self[key].get_ordered(caller=False)
            else:
                ordered_dict[key] = self[key]
        return ordered_dict

    def force_clean(self, caller=True):
        """Attempts to convert to graph_objs and call force_clean() on values.

        Calling force_clean() on a PlotlyDict will ensure that the object is
        valid and may be sent to plotly. This process will also remove any
        entries that end up with a length == 0.

        Careful! This will delete any invalid entries *silently*.

        """
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        if caller:
            self.to_graph_objs(caller=False)
        del_keys = [key for key in self
                    if str(key) not in INFO[obj_key]['keymeta']]
        for key in del_keys:
            del self[key]
        keys = list(self.keys())
        for key in keys:
            try:
                self[key].force_clean(caller=False)  # TODO: add error handling
            except AttributeError:
                pass
            if isinstance(self[key], (dict, list)):
                if len(self[key]) == 0:
                    del self[key]  # clears empty collections!
            elif self[key] is None:
                del self[key]


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
        if self.__class__.__name__ == 'PlotlyTrace':
            warnings.warn("\nThe PlotlyTrace class is a base class of "
                          "dictionary-like plot types.\nIt is not meant to be "
                          "a user interface.")

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print(obj.to_string())

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\\n') -- set end of line character(s)
        pretty (default = True) -- curtail long list output with a '...'
        max_chars (default = 80) -- set max characters per line

        """
        self.to_graph_objs()
        if self.__class__.__name__ != "Trace":
            trace_type = self.pop('type')
            string = super(PlotlyTrace, self).to_string(level=level,
                                                        indent=indent,
                                                        eol=eol,
                                                        pretty=pretty,
                                                        max_chars=max_chars)
            self['type'] = trace_type
        else:
            string = super(PlotlyTrace, self).to_string(level=level,
                                                        indent=indent,
                                                        eol=eol,
                                                        pretty=pretty,
                                                        max_chars=max_chars)
        return string


class Trace(PlotlyTrace):
    """A general data class for plotly. Never validated...

    This class should be used only for the right reason. This class does not
    do much validation because plotly usually accepts more trace specifiers
    and more value type varieties, e.g., 'x', 'y', 'r', 't', marker = [
    array], etc.

    If you are getting errors locally, you might try using this case if
    you're sure that what you're attempting to plot is valid.

    Also, when getting figures from plotly, you may get back `Trace` types if
    the figure was constructed with data objects that don't fall into any of
    the class categorizations that are defined in this api.

    """
    pass


# (2) Generate graph objects using OBJ_MAP
# With type(name, bases, dict) :
# - name will be the new class name
# - bases are the base classes that the new class inherits from
# - dict holds attributes for the new class, e.g., __doc__
for obj in OBJ_MAP:
    base_name = graph_objs_tools.OBJ_MAP[obj]['base_name']
    if base_name == 'PlotlyList':
        doc = graph_objs_tools.make_list_doc(obj)
    else:
        doc = graph_objs_tools.make_dict_doc(obj)
    base = globals()[base_name]
    globals()[obj] = type(obj, (base,), {'__doc__': doc, '__name__': obj})


# (3) Patch 'custom' methods into some graph objects
def get_patched_data_class(Data):
    def to_graph_objs(self, caller=True):  # TODO TODO TODO! check logic!
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyTrace.
            2. Call `to_graph_objects` on each of these entries.

        """
        for index, entry in enumerate(self):
            if isinstance(entry, PlotlyDict):
                self[index] = get_class_instance_by_name(
                    entry.__class__.__name__, entry)
            elif isinstance(entry, dict):
                if 'type' not in entry:  # assume 'scatter' if not given
                    entry['type'] = 'scatter'
                try:
                    obj_name = KEY_TO_NAME[entry['type']]
                except KeyError:
                    raise exceptions.PlotlyDataTypeError(
                        obj=self,
                        index=index
                    )
                obj = get_class_instance_by_name(obj_name)
                for k, v in list(entry.items()):
                    obj[k] = v
                self[index] = obj
            if not isinstance(self[index], PlotlyTrace):  # Trace ONLY!!!
                raise exceptions.PlotlyListEntryError(
                    obj=self,
                    index=index,
                    notes=(
                        "The entry could not be converted into a PlotlyTrace "
                        "object (e.g., Scatter, Heatmap, Bar, etc)."
                    ),
                )
        super(Data, self).to_graph_objs(caller=caller)
    Data.to_graph_objs = to_graph_objs  # override method!

    def get_data(self, flatten=False):
        """

        :param flatten:
        :return:

        """
        if flatten:
            self.to_graph_objs()
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
                        new_trace_name = "{0}_{1}".format(trace_name, j)
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
    Data.get_data = get_data

    return Data

Data = get_patched_data_class(Data)


def get_patched_annotations_class(Annotations):
    def to_graph_objs(self, caller=True):
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyDict.
            2. Call `to_graph_objects` on each of these entries.

        """
        for index, entry in enumerate(self):
            if isinstance(entry, (PlotlyDict, PlotlyList)):
                if not isinstance(entry, NAME_TO_CLASS['Annotation']):
                    raise exceptions.PlotlyListEntryError(
                        obj=self,
                        index=index,
                        notes="The entry could not be converted into an "
                              "Annotation object because it was already a "
                              "different kind of graph object.",
                    )
            elif isinstance(entry, dict):
                obj = get_class_instance_by_name('Annotation')
                for k, v in list(entry.items()):
                    obj[k] = v
                self[index] = obj
            else:
                raise exceptions.PlotlyListEntryError(
                    obj=self,
                    index=index,
                    notes=(
                        "The entry could not be converted into an Annotation "
                        "object because it was not a dictionary."
                    ),
                )
        super(Annotations, self).to_graph_objs(caller=caller)
    Annotations.to_graph_objs = to_graph_objs  # override method!
    return Annotations

Annotations = get_patched_annotations_class(Annotations)


def get_patched_figure_class(Figure):
    def __init__(self, *args, **kwargs):
        if len(args):
            if ('data' not in kwargs) and ('data' not in args[0]):
                kwargs['data'] = Data()
            if ('layout' not in kwargs) and ('layout' not in args[0]):
                kwargs['layout'] = Layout()
        else:
            if 'data' not in kwargs:
                kwargs['data'] = Data()
            if 'layout' not in kwargs:
                kwargs['layout'] = Layout()
        super(Figure, self).__init__(*args, **kwargs)
    Figure.__init__ = __init__  # override method!

    def print_grid(self):
        """Print a visual layout of the figure's axes arrangement.

        This is only valid for figures that are created
        with plotly.tools.make_subplots.
        """
        try:
            grid_str = self._grid_str
        except KeyError:
            raise Exception("Use plotly.tools.make_subplots "
                            "to create a subplot grid.")
        print(grid_str)
    Figure.print_grid = print_grid

    def get_data(self, flatten=False):
        """
        Returns the JSON for the plot with non-data elements stripped.

        Flattening may increase the utility of the result.

        :param (bool) flatten: {'a': {'b': ''}} --> {'a.b': ''}
        :returns: (dict|list) Depending on (flat|unflat)

        """
        self.to_graph_objs()
        return self['data'].get_data(flatten=flatten)
    Figure.get_data = get_data

    def to_dataframe(self):
        data = self.get_data(flatten=True)
        from pandas import DataFrame, Series
        return DataFrame(dict([(k, Series(v)) for k, v in data.items()]))
    Figure.to_dataframe = to_dataframe

    def append_trace(self, trace, row, col):
        """ Helper function to add a data traces to your figure
        that is bound to axes at the row, col index.

        The row, col index is generated from figures created with
        plotly.tools.make_subplots and can be viewed with Figure.print_grid.

        Example:
        # stack two subplots vertically
        fig = tools.make_subplots(rows=2)

        This is the format of your plot grid:
        [ (1,1) x1,y1 ]
        [ (2,1) x2,y2 ]

        fig.append_trace(Scatter(x=[1,2,3], y=[2,1,2]), 1, 1)
        fig.append_trace(Scatter(x=[1,2,3], y=[2,1,2]), 2, 1)

        Arguments:

        trace (plotly trace object):
            The data trace to be bound.

        row (int):
            Subplot row index on the subplot grid (see Figure.print_grid)

        col (int):
            Subplot column index on the subplot grid (see Figure.print_grid)

        """
        try:
            grid_ref = self._grid_ref
        except KeyError:
            raise Exception("In order to use Figure.append_trace, "
                            "you must first use plotly.tools.make_subplots "
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
            raise Exception("The (row, col) pair sent is out of range. "
                            "Use Figure.print_grid to view the subplot grid. ")
        if 'scene' in ref[0]:
            trace['scene'] = ref[0]
            if ref[0] not in self['layout']:
                raise Exception("Something went wrong. "
                                "The scene object for ({r},{c}) subplot cell "
                                "got deleted.".format(r=row, c=col))
        else:
            xaxis_key = "xaxis{ref}".format(ref=ref[0][1:])
            yaxis_key = "yaxis{ref}".format(ref=ref[1][1:])
            if (xaxis_key not in self['layout']
                    or yaxis_key not in self['layout']):
                raise Exception("Something went wrong. "
                                "An axis object for ({r},{c}) subplot cell "
                                "got deleted.".format(r=row, c=col))
            trace['xaxis'] = ref[0]
            trace['yaxis'] = ref[1]
        self['data'] += [trace]
    Figure.append_trace = append_trace

    return Figure

Figure = get_patched_figure_class(Figure)


def get_patched_layout_class(Layout):
    def __init__(self, *args, **kwargs):
        super(Layout, self).__init__(*args, **kwargs)

    def to_graph_objs(self, caller=True):
        """Walk obj, convert dicts and lists to plotly graph objs.

        For each key in the object, if it corresponds to a special key that
        should be associated with a graph object, the ordinary dict or list
        will be reinitialized as a special PlotlyDict or PlotlyList of the
        appropriate `kind`.

        """
        keys = list(self.keys())
        for key in keys:
            if key[:5] in ['xaxis', 'yaxis']:  # allows appended integers!
                try:
                    axis_int = int(key[5:])  # may raise ValueError
                    if axis_int == 0:
                        continue  # xaxis0 and yaxis0 are not valid keys...
                except ValueError:
                    continue  # not an XAxis or YAxis object after all
                if isinstance(self[key], dict):
                    if key[:5] == 'xaxis':
                        obj = get_class_instance_by_name('XAxis')
                    else:
                        obj = get_class_instance_by_name('YAxis')
                    for k, v in list(self.pop(key).items()):
                        obj[k] = v
                    self[key] = obj  # call to super will call 'to_graph_objs'
        super(Layout, self).to_graph_objs(caller=caller)

    def to_string(self, level=0, indent=4, eol='\n',
                  pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print(obj.to_string())

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\\n') -- set end of line character(s)
        pretty (default = True) -- curtail long list output with a '...'
        max_chars (default = 80) -- set max characters per line

        """
        # TODO: can't call super
        self.to_graph_objs()
        if not len(self):
            return "{name}()".format(name=self.__class__.__name__)
        string = "{name}(".format(name=self.__class__.__name__)
        index = 0
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        for key in INFO[obj_key]['keymeta']:
            if key in self:
                string += "{eol}{indent}{key}=".format(
                    eol=eol,
                    indent=' ' * indent * (level+1),
                    key=key)
                try:
                    string += self[key].to_string(level=level+1,
                                                  indent=indent,
                                                  eol=eol,
                                                  pretty=pretty,
                                                  max_chars=max_chars)
                except AttributeError:
                    if pretty:  # curtail representation if too many chars
                        max_len = (max_chars -
                                   indent*(level + 1) -
                                   len(key + "=") -
                                   len(eol))
                        if index < len(self):
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
                if index < len(self) - 1:
                    string += ","
                index += 1
                if index == len(self):  # TODO: extraneous...
                    break
        left_over_keys = [key for key in self
                          if key not in INFO[obj_key]['keymeta']]
        left_over_keys.sort()
        for key in left_over_keys:
            string += "{eol}{indent}{key}=".format(
                eol=eol,
                indent=' ' * indent * (level+1),
                key=key)
            try:
                string += self[key].to_string(level=level + 1,
                                              indent=indent,
                                              eol=eol,
                                              pretty=pretty,
                                              max_chars=max_chars)
            except AttributeError:
                string += str(repr(self[key]))
            if index < len(self) - 1:
                string += ","
            index += 1
        string += "{eol}{indent})".format(eol=eol, indent=' ' * indent * level)
        return string

    def force_clean(self, caller=True):  # TODO: can't make call to super...
        """Attempts to convert to graph_objs and call force_clean() on values.

        Calling force_clean() on a Layout will ensure that the object is
        valid and may be sent to plotly. This process will also remove any
        entries that end up with a length == 0.

        Careful! This will delete any invalid entries *silently*.

        This method differs from the parent (PlotlyDict) method in that it
        must check for an infinite number of possible axis keys, i.e. 'xaxis',
        'xaxis1', 'xaxis2', 'xaxis3', etc. Therefore, it cannot make a call
        to super...

        """
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        if caller:
            self.to_graph_objs(caller=False)
        del_keys = [key for key in self
                    if str(key) not in INFO[obj_key]['keymeta']]
        for key in del_keys:
            if (key[:5] == 'xaxis') or (key[:5] == 'yaxis'):
                try:
                    test_if_int = int(key[5:])
                except ValueError:
                    del self[key]
            else:
                del self[key]
        keys = list(self.keys())
        for key in keys:
            try:
                self[key].force_clean(caller=False)  # TODO error handling??
            except AttributeError:
                pass
            if isinstance(self[key], (dict, list)):
                if len(self[key]) == 0:
                    del self[key]  # clears empty collections!
            elif self[key] is None:
                del self[key]
    Layout.__init__ = __init__
    Layout.to_graph_objs = to_graph_objs
    Layout.to_string = to_string
    Layout.force_clean = force_clean  # override methods!
    return Layout

Layout = get_patched_layout_class(Layout)


# (4) NAME_TO_CLASS dict and class-generating function
# NOTE: used to be a dict comprehension, but we try and support 2.6.x now
NAME_TO_CLASS = {}
for name in NAME_TO_KEY.keys():
    NAME_TO_CLASS[name] = getattr(sys.modules[__name__], name)


def get_class_instance_by_name(name, *args, **kwargs):
    """All class creation goes through here.

    Because call signatures for the different classes are different, we have
    anticipate that args, kwargs, or both may be specified. Note, this still
    allows instantiation errors to occur naturally.

    """
    if args and kwargs:
        return NAME_TO_CLASS[name](*args, **kwargs)
    elif args:
        return NAME_TO_CLASS[name](*args)
    elif kwargs:
        return NAME_TO_CLASS[name](**kwargs)
    else:
        return NAME_TO_CLASS[name]()
