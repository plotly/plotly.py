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
import warnings
import collections
import json
import textwrap
from .. import exceptions
from .. import utils

__all__ = ["Data", "Annotations", "Bar", "Box", "Contour", "Heatmap",
           "Histogram", "Histogram2d", "Histogram2dContour", "Scatter",
           "Annotation", "ColorBar", "Contours", "ErrorY", "Figure", "Font",
           "Layout", "Legend", "Line", "Margin", "Marker", "Stream", "Trace",
           "XAxis", "XBins", "YAxis", "YBins"]

# TODO: BIG ONE, how should exceptions bubble up in this inheritance scheme?
    # TODO: related, WHAT exceptions should bubble up?

from pkg_resources import resource_string
s = resource_string('plotly',
                    'graph_reference/graph_objs_meta.json').decode('utf-8')
INFO = json.loads(s, object_pairs_hook=collections.OrderedDict)

INFO = utils.decode_unicode(INFO)

# define how to map from keys in INFO to a class
# mapping: (n->m, m < n)
KEY_TO_NAME = dict(
    plotlylist='PlotlyList',
    data='Data',
    angularAxis='AngularAxis',
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
    error_y='ErrorY',
    figure='Figure',
    font='Font',
    layout='Layout',
    legend='Legend',
    line='Line',
    margin='Margin',
    marker='Marker',
    radialAxis='RadialAxis',
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
    AngularAxis='angularAxis',
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
    ErrorY='error_y',
    Figure='figure',
    Font='font',
    Layout='layout',
    Legend='legend',
    Line='line',
    Margin='margin',
    Marker='marker',
    RadialAxis='radialAxis',
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
        doc += "\t{}.".format(name) + "\n\t{}.".format(name).join(
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
        doc += "\t{}.".format(name) + "\n\t{}.".format(name).join(
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
                        val_types = "{} object | ".format(KEY_TO_NAME[key]) + \
                                    val_types
                except KeyError:
                    val_types = undocumented
                try:
                    descr = str(obj_info[key]['description'])
                except KeyError:
                    descr = undocumented
                str_1 = "{} [required={}] (value={}):\n".format(key, required,
                                                                val_types)
                str_1 = "\t" + "\n\t".join(textwrap.wrap(str_1,
                                                         width=width1)) + "\n"
                str_2 = "\t\t" + "\n\t\t".join(textwrap.wrap(descr,
                                               width=width2)) + "\n"
                doc += str_1 + str_2
                # if a user can run help on this value, tell them!
                if typ == "object":
                    doc += "\n\t\tFor more, run `help(plotly.graph_objs.{" \
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
    __metaclass__ = ListMeta

    def __init__(self, *args):
        super(PlotlyList, self).__init__(*args)
        self.validate()
        if self.__class__.__name__ == 'PlotlyList':
            warnings.warn("\nThe PlotlyList class is a base class of "
                          "list-like graph_objs.\nIt is not meant to be a "
                          "user interface.")

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
                    obj_name = KEY_TO_NAME[entry['type']]
                    try:
                        _class = NAME_TO_CLASS[obj_name]
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

    def update(self, changes):
        """Update current list with changed_list, which must be iterable.
        The 'changes' should be a list of dictionaries, however,
        it is permitted to be a single dict object.

        """
        if isinstance(changes, dict):
            changes = [changes]
        self.to_graph_objs()
        for index in range(len(self)):
            try:
                self[index].update(changes[index % len(changes)])
            except ZeroDivisionError:
                pass

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
        string += "{eol}{indent}])".format(eol=eol,
                                           indent=' ' * indent * level)
        return string

    def force_clean(self):
        """Attempts to convert to graph_objs and calls force_clean() on entries.

        Calling force_clean() on a PlotlyList will ensure that the object is
        valid and may be sent to plotly. This process will remove any entries
        that end up with a length == 0. It will also remove itself from
        enclosing trivial structures if it is enclosed by a collection with
        length 1, meaning the data is the ONLY object in the collection.

        Careful! This will delete any invalid entries *silently*.

        """
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
            for key, val in dict1.items():
                if key in self:
                    if isinstance(self[key], (PlotlyDict, PlotlyList)):
                        self[key].update(val)
                    else:
                        self[key] = val
                else:
                    self[key] = val

        if len(dict2):
            for key, val in dict2.items():
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
        keys = self.keys()
        for key in keys:
            try:
                self[key].strip_style()
            except AttributeError:
                try:
                    if INFO[obj_key][key]['type'] != 'style':
                        pass
                    else:
                        del self[key]
                except KeyError:  # TODO: Update the JSON
                    # print "'type' not in {} for {}".format(obj_key, key)
                    pass

    def get_data(self):
        """Returns the JSON for the plot with non-data elements stripped."""
        self.to_graph_objs()
        class_name = self.__class__.__name__
        obj_key = NAME_TO_KEY[class_name]
        d = dict()
        for key, val in self.items():
            try:
                d[key] = val.get_data()
            except AttributeError:
                try:
                    if INFO[obj_key][key]['type'] == 'data':
                        d[key] = val
                except KeyError:
                    pass
        keys = d.keys()
        for key in keys:
            if isinstance(d[key], (dict, list)):
                if len(d[key]) == 0:
                    del d[key]
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
                class_name = KEY_TO_NAME[key]
                if isinstance(self[key], dict):
                    obj = NAME_TO_CLASS[class_name]()  # gets constructor
                    for k, v in self.pop(key).items():
                        obj[k] = v
                    obj.to_graph_objs()
                    self[key] = obj
                elif isinstance(self[key], list):
                    obj = NAME_TO_CLASS[class_name]()  # gets constructor
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
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        for key, val in self.items():
            try:
                val.validate()
            except AttributeError:
                if key in INFO[obj_key]:
                    try:  # TODO: eventually this should be removed...
                        if INFO[obj_key][key]['type'] == 'object':
                            msg = ("Class '{cls}' for key '{key}' in '{obj}' "
                                   "graph object is invalid. Valid types for this "
                                   "key are '{types}'.\n\nRun 'help(plotly"
                                   ".graph_objs.{obj})' for more information."
                                   "".format(cls=val.__class__.__name__,
                                             key=key,
                                             obj=self.__class__.__name__,
                                             types=INFO[obj_key][key]['val_types']))
                            raise exceptions.PlotlyError(msg)
                    except KeyError:
                        pass
                else:
                    matching_objects = [obj for obj in INFO if key in INFO[obj]]
                    msg = ("Invalid key, '{key}', for class, '{obj}'\n\nRun "
                           "'help(plotly.graph_objs.{obj})' for more "
                           "information.\n\n".format(
                           key=key,
                           obj=self.__class__.__name__))
                    if len(matching_objects):
                        msg += "That key is valid only in these objects:\n\n"
                        for obj in matching_objects:
                            msg += "\t{}".format(KEY_TO_NAME[obj])
                            try:
                                msg += "({}='{}')\n".format(
                                    key, INFO[obj][key]['val_types'])
                            except KeyError:
                                msg += "({}='..')\n".format(key)
                        msg.expandtabs()
                    else:
                        msg += "Couldn't find uses for key: {}\n\n".format(key)
                    raise exceptions.PlotlyInvalidKeyError(msg)

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
                    val = repr(self[key])
                    val_chars = max_chars - (indent*(level+1)) - (len(key)+1)
                    if pretty and (len(val) > val_chars):
                        string += val[:val_chars - 5] + '...' + val[-1]
                    else:
                        string += val
                if index < len(self) - 1:
                    string += ","
                index += 1
                if index == len(self):
                    break
        string += "{eol}{indent})".format(eol=eol, indent=' ' * indent * level)
        return string

    def force_clean(self):
        """Attempts to convert to graph_objs and call force_clean() on values.

        Calling force_clean() on a PlotlyDict will ensure that the object is
        valid and may be sent to plotly. This process will also remove any
        entries that end up with a length == 0.

        Careful! This will delete any invalid entries *silently*.

        """
        obj_key = NAME_TO_KEY[self.__class__.__name__]
        self.to_graph_objs()
        del_keys = [key for key in self if str(key) not in INFO[obj_key]]
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
            elif self[key] is None:
                del self[key]


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
        for _plotlytrace in self:
            if not issubclass(_plotlytrace.__class__, PlotlyTrace):
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
        for no, entry in enumerate(self):
            if isinstance(entry, Trace):
                pass
            elif isinstance(entry, dict):
                if 'type' not in entry:
                    entry['type'] = 'scatter'
                try:
                    obj_type = entry['type']
                    type_info = INFO[obj_type]
                    use_trace = False
                    for key in entry:
                        if (key not in type_info) and (key in INFO['trace']):
                            pass
                            # use_trace = True
                    if use_trace:
                        self[no] = Trace(entry)
                        warnings.warn(
                            "converting object '{}' with type '{}' to object "
                            "'Trace'. Everything will work upon upload to "
                            "plotly, howevever some of the keys specified "
                            "won't be functional.".format(
                                KEY_TO_NAME['obj_type'], obj_type))
                except KeyError:
                    pass  # TODO: no error will happen here, get's caught later.
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
        """Recursively check the validity of the entries in a Annotations.

        Annotations may only contain Annotation objects or dictionary-like
        objects that can be re-instantiated as an Annotation.

        The validation process first requires that all nested collections be
        converted to the appropriate subclass of PlotlyDict/PlotlyList. Then,
        each of these objects call `validate` and so on, recursively,
        until the entire data list has been validated.

        """
        self.to_graph_objs()  # change everything to PlotlyList/Dict objects...
        for annotation in self:
            if not issubclass(annotation.__class__, Annotation):
                raise exceptions.PlotlyInvalidListItemError(
                    "Annotation objects only in Annotations.")
        super(Annotations, self).validate()

    def to_graph_objs(self):
        """Change any nested collections to subclasses of PlotlyDict/List.

        Procedure:
            1. Attempt to convert all entries to a subclass of PlotlyDict.
            2. Call `to_graph_objects` on each of these entries.

        """
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
                        axis_int = int(key[5:])
                        if axis_int == 0:
                            continue
                        obj = XAxis()
                        for k, v in self.pop(key).items():
                            obj[k] = v
                        obj.to_graph_objs()
                        self[key] = obj
                    except ValueError:
                        pass
                elif key[:5] == 'yaxis':  # allows appended integers!
                    try:
                        axis_int = int(key[5:])
                        if axis_int == 0:
                            continue
                        obj = YAxis()
                        for k, v in self.pop(key).items():
                            obj[k] = v
                        obj.to_graph_objs()
                        self[key] = obj
                    except ValueError:
                        pass
        super(Layout, self).to_graph_objs()

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
                    val = repr(self[key])
                    val_chars = max_chars - (indent*(level+1)) - (len(key)+1)
                    if pretty and (len(val) > val_chars):
                        string += val[:val_chars - 5] + '...' + val[-1]
                    else:
                        string += val
                if index < len(self) - 1:
                    string += ","
                index += 1
                if index == len(self):
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

    def force_clean(self):  # TODO: can't make call to super...
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
        self.to_graph_objs()
        del_keys = [key for key in self if str(key) not in INFO[obj_key]]
        for key in del_keys:
            if (key[:5] == 'xaxis') or (key[:5] == 'yaxis'):
                try:
                    test_if_int = int(key[5:])
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