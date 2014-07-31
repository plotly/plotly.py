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
import textwrap
import six
import sys
from plotly.graph_objs import graph_objs_tools
import copy
from plotly import exceptions
from plotly import utils

if sys.version[:3] == '2.6':
    from ordereddict import OrderedDict
    import simplejson as json
else:
    from collections import OrderedDict
    import json

__all__ = ["Data",
           "Annotations",
           "Area",
           "Bar",
           "Box",
           "Contour",
           "Heatmap",
           "Histogram",
           "Histogram2d",
           "Histogram2dContour",
           "Scatter",
           "Annotation",
           "AngularAxis",
           "ColorBar",
           "Contours",
           "ErrorX",
           "ErrorY",
           "Figure",
           "Font",
           "Layout",
           "Legend",
           "Line",
           "Margin",
           "Marker",
           "RadialAxis",
           "Stream",
           "Trace",
           "XAxis",
           "XBins",
           "YAxis",
           "YBins"]

# TODO: BIG ONE, how should exceptions bubble up in this inheritance scheme?
    # TODO: related, WHAT exceptions should bubble up?

from pkg_resources import resource_string
s = resource_string('plotly',
                    'graph_reference/graph_objs_meta.json').decode('utf-8')
INFO = json.loads(s, object_pairs_hook=OrderedDict)

INFO = utils.decode_unicode(INFO)

# define how to map from keys in INFO to a class
# mapping: (n->m, m < n)
KEY_TO_NAME = dict(
    plotlylist='PlotlyList',
    data='Data',
    angularaxis='AngularAxis',
    annotations='Annotations',
    area='Area',
    plotlydict='PlotlyDict',
    plotlytrace='PlotlyTrace',
    bar='Bar',
    box='Box',
    contour='Contour',
    heatmap='Heatmap',
    histogram='Histogram',
    histogram2d='Histogram2d',
    histogram2dcontour='Histogram2dContour',
    scatter='Scatter',
    annotation='Annotation',
    colorbar='ColorBar',
    contours='Contours',
    error_x='ErrorX',
    error_y='ErrorY',
    figure='Figure',
    font='Font',
    layout='Layout',
    legend='Legend',
    line='Line',
    margin='Margin',
    marker='Marker',
    radialaxis='RadialAxis',
    stream='Stream',
    trace='Trace',
    textfont='Font',
    tickfont='Font',
    titlefont='Font',
    xaxis='XAxis',
    xbins='XBins',
    yaxis='YAxis',
    ybins='YBins'
)

# define how to map from a class name to a key name in INFO
# mapping: (n->n)
NAME_TO_KEY = dict(
    PlotlyList='plotlylist',
    Data='data',
    AngularAxis='angularaxis',
    Annotations='annotations',
    PlotlyDict='plotlydict',
    PlotlyTrace='plotlytrace',
    Area='area',
    Bar='bar',
    Box='box',
    Contour='contour',
    Heatmap='heatmap',
    Histogram='histogram',
    Histogram2d='histogram2d',
    Histogram2dContour='histogram2dcontour',
    Scatter='scatter',
    Annotation='annotation',
    ColorBar='colorbar',
    Contours='contours',
    ErrorX='error_x',
    ErrorY='error_y',
    Figure='figure',
    Font='font',
    Layout='layout',
    Legend='legend',
    Line='line',
    Margin='margin',
    Marker='marker',
    RadialAxis='radialaxis',
    Stream='stream',
    Trace='trace',
    XAxis='xaxis',
    XBins='xbins',
    YAxis='yaxis',
    YBins='ybins'
)


class ListMeta(type):
    """A meta class for PlotlyList class creation.

    The sole purpose of this meta class is to properly create the __doc__
    attribute so that running help(Obj), where Obj is a subclass of PlotlyList,
    will return useful information for that object.

    """

    def __new__(mcs, name, bases, attrs):
        doc = attrs['__doc__']
        tab_size = 4
        min_indent = min([len(a) - len(b)
                          for a, b in zip(doc.splitlines(),
                                          [l.lstrip()
                                           for l in doc.splitlines()])])
        doc = "".join([line[min_indent:] + '\n' for line in doc.splitlines()])
        # Add section header for method list...
        doc += "Quick method reference:\n\n"
        doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
            ["update(changes)", "strip_style()", "get_data()",
             "to_graph_objs()", "validate()", "to_string()",
             "force_clean()"]) + "\n\n"
        attrs['__doc__'] = doc.expandtabs(tab_size)
        return super(ListMeta, mcs).__new__(mcs, name, bases, attrs)


class DictMeta(type):
    """A meta class for PlotlyDict class creation.

    The sole purpose of this meta class is to properly create the __doc__
    attribute so that running help(Obj), where Obj is a subclass of PlotlyDict,
    will return information about key-value pairs for that object.

    """
    def __new__(mcs, name, bases, attrs):
        obj_key = NAME_TO_KEY[name]
        # remove min indentation...
        doc = attrs['__doc__']
        obj_info = INFO[obj_key]
        line_size = 76
        tab_size = 4
        min_indent = min([len(a) - len(b)
                          for a, b in zip(doc.splitlines(),
                                          [l.lstrip()
                                           for l in doc.splitlines()])])
        doc = "".join([line[min_indent:] + '\n' for line in doc.splitlines()])
        # Add section header for method list...
        doc += "Quick method reference:\n\n"
        doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
            ["update(changes)", "strip_style()", "get_data()",
             "to_graph_objs()", "validate()", "to_string()",
             "force_clean()"]) + "\n\n"
        # Add section header
        if len(obj_info):
            doc += "Valid keys:\n\n"
            # Add each key one-by-one and format
            width1 = line_size-tab_size
            width2 = line_size-2*tab_size
            width3 = line_size-3*tab_size
            undocumented = "Aw, snap! Undocumented!"
            for key in obj_info:
                # main portion of documentation
                try:
                    required = str(obj_info[key]['required'])
                except KeyError:
                    required = undocumented

                try:
                    typ = str(obj_info[key]['type'])
                except KeyError:
                    typ = undocumented

                try:
                    val_types = str(obj_info[key]['val_types'])
                    if typ == 'object':
                        val_types = "{0} object | ".format(KEY_TO_NAME[key])+\
                                    val_types
                except KeyError:
                    val_types = undocumented
                try:
                    descr = str(obj_info[key]['description'])
                except KeyError:
                    descr = undocumented
                str_1 = "{0} [required={1}] (value={2})".format(
                    key, required, val_types)
                if "streamable" in obj_info[key] and obj_info[key]["streamable"]:
                    str_1 += " (streamable)"
                str_1 += ":\n"
                str_1 = "\t" + "\n\t".join(textwrap.wrap(str_1,
                                                         width=width1)) + "\n"
                str_2 = "\t\t" + "\n\t\t".join(textwrap.wrap(descr,
                                               width=width2)) + "\n"
                doc += str_1 + str_2
                # if a user can run help on this value, tell them!
                if typ == "object":
                    doc += "\n\t\tFor more, run `help(plotly.graph_objs.{0" \
                           "})`\n".format(KEY_TO_NAME[key])
                # if example usage exists, tell them!
                if 'examples' in obj_info[key]:
                    ex = "\n\t\tExamples:\n" + "\t\t\t"
                    ex += "\n\t\t\t".join(
                        textwrap.wrap(str(obj_info[key]['examples']),
                                      width=width3)) + "\n"
                    doc += ex
                if 'code' in obj_info[key]:
                    code = "\n\t\tCode snippet:"
                    code += "\n\t\t\t>>>".join(
                        str(obj_info[key]['code']).split('>>>')) + "\n"
                    doc += code
                doc += '\n'
        attrs['__doc__'] = doc.expandtabs(tab_size)
        return super(DictMeta, mcs).__new__(mcs, name, bases, attrs)

@six.add_metaclass(ListMeta)
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
                except (exceptions.PlotlyGraphObjectError) as err:
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
        for _plotlydict in self:
            l += [_plotlydict.get_data()]
        del_indicies = [index for index, item in enumerate(self)
                        if len(item) == 0]
        del_ct = 0
        for index in del_indicies:
            del self[index - del_ct]
            del_ct += 1
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
                    message="uh-oh, this error shouldn't have happenend.",
                    plain_message="uh-oh, this error shouldn't have happenend.",
                    path=[index],
                )

    def to_string(self, level=0, indent=4, eol='\n', pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print obj.to_string()

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\n') -- set end of line character(s)
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
        string += "{eol}{indent}])".format(eol=eol, indent=' ' * indent * level)
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

@six.add_metaclass(DictMeta)
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
        super(PlotlyDict, self).__init__(*args, **kwargs)
        if issubclass(NAME_TO_CLASS[class_name], PlotlyTrace):
            if (class_name != 'PlotlyTrace') and (class_name != 'Trace'):
                self['type'] = NAME_TO_KEY[class_name]
        self.validate()
        if self.__class__.__name__ == 'PlotlyDict':
            warnings.warn("\nThe PlotlyDict class is a base class of "
                          "dictionary-like graph_objs.\nIt is not meant to be "
                          "a user interface.")

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
        `'type': 'style'` in the INFO dictionary listed in graph_objs_meta.py.

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
                    if INFO[obj_key][key]['type'] == 'style':
                        if isinstance(self[key], six.string_types):
                            del self[key]
                        elif not hasattr(self[key], '__iter__'):
                            del self[key]
                except KeyError:  # TODO: Update the JSON
                    # print "'type' not in {0} for {1}".format(obj_key, key)
                    pass

    def get_data(self):
        """Returns the JSON for the plot with non-data elements stripped."""
        self.to_graph_objs()
        class_name = self.__class__.__name__
        obj_key = NAME_TO_KEY[class_name]
        d = dict()
        for key, val in list(self.items()):
            if isinstance(val, (PlotlyDict, PlotlyList)):
                d[key] = val.get_data()
            else:
                try:
                    if INFO[obj_key][key]['type'] == 'data':  # TODO: Update the JSON
                        d[key] = val
                except KeyError:
                    pass
        keys = list(d.keys())
        for key in keys:
            if isinstance(d[key], (dict, list)):
                if len(d[key]) == 0:
                    del d[key]
        if len(d) == 1:
            d = list(d.values())[0]
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
            elif key in INFO[info_key] and 'type' in INFO[info_key][key]:
                if INFO[info_key][key]['type'] == 'object':
                    class_name = KEY_TO_NAME[key]
                    obj = NAME_TO_CLASS[class_name]()  # gets constructor
                    if isinstance(obj, PlotlyDict):
                        if not isinstance(self[key], dict):
                            try:
                                val_types = INFO[info_key][key]['val_types']
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
                                val_types = INFO[info_key][key]['val_types']
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
        dictionary in INFO stored in graph_objs_meta.py.

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
                if key in INFO[obj_key]:
                    if 'type' not in INFO[obj_key][key]:
                        continue  # TODO: 'type' may not be documented yet!
                    if INFO[obj_key][key]['type'] == 'object':
                        try:
                            val_types = INFO[obj_key][key]['val_types']
                        except KeyError:
                            val_types = 'undocumented'
                        raise exceptions.PlotlyDictValueError(
                            obj=self,
                            key=key,
                            value=val,
                            val_types=val_types
                        )
                else:
                    matching_objects = [obj for obj in INFO if key in INFO[obj]]
                    notes = ''
                    if len(matching_objects):
                        notes += "That key is valid only in these objects:\n\n"
                        for obj in matching_objects:
                            notes += "\t{0}".format(KEY_TO_NAME[obj])
                            try:
                                notes += '({0}="{1}")\n'.format(
                                    repr(key), INFO[obj][key]['val_types'])
                            except KeyError:
                                notes += '({0}="..")\n'.format(repr(key))
                        notes.expandtabs()
                    else:
                        notes += ("Couldn't find uses for key: {0}\n\n"
                                  "".format(repr(key)))
                    raise exceptions.PlotlyDictKeyError(obj=self,
                                                        key=key,
                                                        notes=notes)

    def to_string(self, level=0, indent=4, eol='\n', pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print obj.to_string()

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\n') -- set end of line character(s)
        pretty (default = True) -- curtail long list output with a '...'
        max_chars (default = 80) -- set max characters per line

        """
        self.to_graph_objs()  # todo, consider catching and re-raising?
        if not len(self):
            return "{name}()".format(name=self.__class__.__name__)
        string = "{name}(".format(name=self.__class__.__name__)
        index = 0
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        for key in INFO[obj_key]:  # this sets the order of the keys! nice.
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
        unordered_keys = [key for key in self if key not in INFO[obj_type]]
        for key in INFO[obj_type]:
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
        del_keys = [key for key in self if str(key) not in INFO[obj_key]]
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


class Data(PlotlyList):
    """A list of traces to be shown on a plot/graph.

    Any operation that can be done with a standard list may be used with Data.
    Instantiation requires an iterable (just like list does), for example:

    Data([Scatter(), Heatmap(), Box()])

    Valid entry types: (dict or any subclass of Trace, i.e., Scatter, Box, etc.)

    """
    def to_graph_objs(self, caller=True):  # TODO TODO TODO! check logic!
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyTrace.
            2. Call `to_graph_objects` on each of these entries.

        """
        for index, entry in enumerate(self):
            if isinstance(entry, PlotlyDict):
                self[index] = NAME_TO_CLASS[entry.__class__.__name__](entry)
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
                obj = NAME_TO_CLASS[obj_name]()  # don't hide if KeyError!
                for k, v in list(entry.items()):
                    obj[k] = v
                self[index] = obj
            if not isinstance(self[index], PlotlyTrace):  # Trace ONLY!!!
                raise exceptions.PlotlyListEntryError(
                    obj=self,
                    index=index,
                    notes="The entry could not be converted into a PlotlyTrace "
                          "object (e.g., Scatter, Heatmap, Bar, etc).",
                )
        super(Data, self).to_graph_objs(caller=caller)


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
    def to_graph_objs(self, caller=True):
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyDict.
            2. Call `to_graph_objects` on each of these entries.

        """
        for index, entry in enumerate(self):
            if isinstance(entry, (PlotlyDict, PlotlyList)):
                if not isinstance(entry, Annotation):
                    raise exceptions.PlotlyListEntryError(
                        obj=self,
                        index=index,
                        notes="The entry could not be converted into an "
                              "Annotation object because it was already a "
                              "different kind of graph object.",
                    )
            elif isinstance(entry, dict):
                obj = Annotation()
                for k, v in list(entry.items()):
                    obj[k] = v
                self[index] = obj
            else:
                raise exceptions.PlotlyListEntryError(
                    obj=self,
                    index=index,
                    notes="The entry could not be converted into an Annotation "
                          "object because it was not a dictionary.",
                )
        super(Annotations, self).to_graph_objs(caller=caller)


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

    def to_string(self, level=0, indent=4, eol='\n', pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print obj.to_string()

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\n') -- set end of line character(s)
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


class Area(PlotlyTrace):
    """A dictionary-like object for representing an area chart in plotly.

    """
    pass


class Bar(PlotlyTrace):
    """A dictionary-like object for representing a bar chart in plotly.

    Example:

    py.plot([Bar(x=['yesterday', 'today', 'tomorrow'], y=[5, 4, 10])])

    """
    pass


class Box(PlotlyTrace):
    """A dictionary-like object for representing a box plot in plotly.

    Example:

        py.plot([Box(name='boxy', y=[1,3,9,2,4,2,3,5,2])])

    """
    pass


class Contour(PlotlyTrace):
    """A dictionary-like object for representing a contour plot in plotly.

    Example:

        z = [[0, 1, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0],]
        y = ['a', 'b', 'c']
        x = [1, 2, 3, 4, 5]
        py.plot([Contour(z=z, x=x, y=y)])

    """
    pass


class Heatmap(PlotlyTrace):
    """A dictionary-like object for representing a heatmap in plotly.

    Example:

        z = [[0, 1, 0, 1, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0],]
        y = ['a', 'b', 'c']
        x = [1, 2, 3, 4, 5]
        py.plot([Heatmap(z=z, x=x, y=y)])

    """
    pass


class Histogram(PlotlyTrace):
    """A dictionary-like object for representing a histogram plot in plotly.

    Example:
        # make a histogram along xaxis...
        py.plot([Histogram(x=[1,1,2,3,2,3,3])])

        # make a histogram along yaxis...
        py.plot([Histogram(y=[1,1,2,3,2,3,3], orientation='h')])

    """


class Histogram2d(PlotlyTrace):
    """A dictionary-like object for representing a histogram2d plot in plotly.

    Example:

        import numpy as np
        x = np.random.randn(500)
        y = np.random.randn(500)+1
        py.iplot([Histogram2d(x=x, y=y)])

    """
    pass


class Histogram2dContour(PlotlyTrace):
    """A dict-like object for representing a histogram2d-contour plot in plotly.

    Example:

        import numpy as np
        x = np.random.randn(500)
        y = np.random.randn(500)+1
        py.iplot([Histogram2dcountour(x=x, y=y)])

    """
    pass


class Scatter(PlotlyTrace):
    """A dictionary-like object for representing a scatter plot in plotly.

    Example:

        py.plot([Scatter(name='tacters', x=[1,4,2,3], y=[1,6,2,1])])

    """
    pass


class AngularAxis(PlotlyDict):
    """A  dictionary-like object for representing an angular axis in plotly.

    """
    pass


class RadialAxis(PlotlyDict):
    """A  dictionary-like object for representing an angular axis in plotly.

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

    Example:

        note = Annotation(text='what i want this to say is:<br>THIS!',
                          x=0,
                          y=0,
                          xref='paper',
                          yref='paper,
                          yanchor='bottom',
                          xanchor='left')

    """
    pass


class ColorBar(PlotlyDict):  # TODO: ?
    """A dictionary-like object for representing a color bar in plotly.

    """
    pass


class Contours(PlotlyDict):  # TODO: ?
    """A dictionary-like object for representing a contours object in plotly.

    This object exists inside definitions for a contour plot.

    """

class ErrorX(PlotlyDict):
    """A dictionary-like object for representing a set of errorx bars in plotly.

    """
    pass


class ErrorY(PlotlyDict):
    """A dictionary-like object for representing a set of errory bars in plotly.

    """
    pass


class Figure(PlotlyDict):
    """A dictionary-like object representing a figure to be rendered in plotly.

    This is the container for all things to be rendered in a figure.

    For help with setting up subplots, run:
    `help(plotly.tools.get_subplots)`

    """
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


class Font(PlotlyDict):
    """A dictionary-like object representing details about font style.

    """
    pass


class Layout(PlotlyDict):
    """A dictionary-like object holding plot settings for plotly figures.

    """
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
                        obj = XAxis()
                    else:
                        obj = YAxis()
                    for k, v in list(self.pop(key).items()):
                        obj[k] = v
                    self[key] = obj  # call to super will call 'to_graph_objs'
        super(Layout, self).to_graph_objs(caller=caller)

    def to_string(self, level=0, indent=4, eol='\n', pretty=True, max_chars=80):
        """Returns a formatted string showing graph_obj constructors.

        Example:

            print obj.to_string()

        Keyword arguments:
        level (default = 0) -- set number of indentations to start with
        indent (default = 4) -- set indentation amount
        eol (default = '\n') -- set end of line character(s)
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
        for key in INFO[obj_key]:
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
        left_over_keys = [key for key in self if key not in INFO[obj_key]]
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
        del_keys = [key for key in self if str(key) not in INFO[obj_key]]
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


class Legend(PlotlyDict):
    """A dictionary-like object representing the legend options for a figure.

    """
    pass


class Line(PlotlyDict):
    """A dictionary-like object representing the style of a line in plotly.

    """
    pass


class Marker(PlotlyDict):
    """A dictionary-like object representing marker(s) style in plotly.

    """
    pass


class Margin(PlotlyDict):
    """A dictionary-like object holding plot margin information.

    """
    pass


class Stream(PlotlyDict):
    """A dictionary-like object representing a data stream.

    """
    pass


class XAxis(PlotlyDict):
    """A dictionary-like object representing an xaxis in plotly.

    """
    pass


class XBins(PlotlyDict):
    """A dictionary-like object representing bin information for a histogram.

    """
    pass


class YAxis(PlotlyDict):
    """A dictionary-like object representing a yaxis in plotly.

    """
    pass


class YBins(PlotlyDict):
    """A dictionary-like object representing bin information for a histogram.

    """
    pass

# finally... define how to map from a class name to an actual class
# mapping: (n->n)
NAME_TO_CLASS = dict(
    PlotlyList=PlotlyList,
    Data=Data,
    Annotations=Annotations,
    PlotlyDict=PlotlyDict,
    PlotlyTrace=PlotlyTrace,
    Area=Area,
    Bar=Bar,
    Box=Box,
    Contour=Contour,
    Heatmap=Heatmap,
    Histogram=Histogram,
    Histogram2d=Histogram2d,
    Histogram2dContour=Histogram2dContour,
    Scatter=Scatter,
    AngularAxis=AngularAxis,
    Annotation=Annotation,
    ColorBar=ColorBar,
    Contours=Contours,
    ErrorX=ErrorX,
    ErrorY=ErrorY,
    Figure=Figure,
    Font=Font,
    Layout=Layout,
    Legend=Legend,
    Line=Line,
    Margin=Margin,
    Marker=Marker,
    RadialAxis=RadialAxis,
    Stream=Stream,
    Trace=Trace,
    XAxis=XAxis,
    XBins=XBins,
    YAxis=YAxis,
    YBins=YBins
)
