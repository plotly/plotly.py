from __future__ import absolute_import
from plotly import utils
import textwrap
import os
import sys
if sys.version[:3] == '2.6':
    from ordereddict import OrderedDict
    import simplejson as json
else:
    from collections import OrderedDict
    import json
import six

from pkg_resources import resource_string


# Define graph reference loader
def _load_graph_ref():
    graph_reference_dir = 'graph_reference'
    json_files = [
        'graph_objs_meta.json',
        'OBJ_MAP.json',
        'NAME_TO_KEY.json',
        'KEY_TO_NAME.json'
    ]
    out = []
    for json_file in json_files:
        relative_path = os.path.join(graph_reference_dir, json_file)
        s = resource_string('plotly', relative_path).decode('utf-8')
        tmp = json.loads(s, object_pairs_hook=OrderedDict)
        tmp = utils.decode_unicode(tmp)
        out += [tmp]
    return tuple(out)

# Load graph reference
INFO, OBJ_MAP, NAME_TO_KEY, KEY_TO_NAME = _load_graph_ref()

# Add mentions to Python-specific graph obj
# to NAME_TO_KEY, KEY_TO_NAME, INFO
NAME_TO_KEY['PlotlyList'] = 'plotlylist'
NAME_TO_KEY['PlotlyDict'] = 'plotlydict'
NAME_TO_KEY['PlotlyTrace'] = 'plotlytrace'
NAME_TO_KEY['Trace'] = 'trace'
KEY_TO_NAME['plotlylist'] = 'PlotlyList'
KEY_TO_NAME['plotlydict'] = 'PlotlyDict'
KEY_TO_NAME['plotlytrace'] = 'PlotlyTrace'
KEY_TO_NAME['trace'] = 'Trace'
INFO['plotlylist'] = dict(keymeta=dict())
INFO['plotlydict'] = dict(keymeta=dict())
INFO['plotlytrace'] = dict(keymeta=dict())
INFO['trace'] = dict(keymeta=dict())

# Define line and tab size for help text!
LINE_SIZE = 76
TAB_SIZE = 4


# Doc make function for list-like objects
def make_list_doc(name):
    # get info for this graph obj
    info = INFO[NAME_TO_KEY[name]]
    # add docstring to doc
    doc = info['docstring']
    doc = "\t" + "\n\t".join(textwrap.wrap(doc, width=LINE_SIZE)) + "\n"
    # Add examples to doc
    examples = info['examples']
    if len(examples):
        doc += "\nExample:\n\n    >>> " + "\n    >>> ".join(examples) + "\n"
    # Add links to online examples to doc
    links = info['links']
    if len(links) == 1:
        doc += "\nOnline example:\n\n    " + "\n    ".join(links) + "\n"
    elif len(links) > 1:
        doc += "\nOnline examples:\n\n    " + "\n    ".join(links) + "\n"
    # Add parents keys to doc
    parent_keys = info['parent_keys']
    if len(parent_keys) == 1:
        doc += "\nParent key:\n\n    " + "\n    ".join(parent_keys) + "\n"
    elif len(parent_keys) > 1:
        doc += "\nParent keys:\n\n    " + "\n    ".join(parent_keys) + "\n"
    # Add method list to doc
    doc += "\nQuick method reference:\n\n"
    doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
        ["update(changes)", "strip_style()", "get_data()",
         "to_graph_objs()", "validate()", "to_string()",
         "force_clean()"]) + "\n\n"
    return doc.expandtabs(TAB_SIZE)


# Doc make function for dict-like objects
def make_dict_doc(name):
    # get info for this graph obj
    info = INFO[NAME_TO_KEY[name]]
    # add docstring to doc
    doc = info['docstring']
    doc = "\t" + "\n\t".join(textwrap.wrap(doc, width=LINE_SIZE)) + "\n"
    # Add examples to doc
    examples = info['examples']
    if len(examples):
        doc += "\nExample:\n\n    >>> " + "\n    >>> ".join(examples) + "\n"
    # Add links to online examples to doc
    links = info['links']
    if len(links) == 1:
        doc += "\nOnline example:\n\n    " + "\n    ".join(links) + "\n"
    elif len(links) > 1:
        doc += "\nOnline examples:\n\n    " + "\n    ".join(links) + "\n"
    # Add parents keys to doc
    parent_keys = info['parent_keys']
    if len(parent_keys) == 1:
        doc += "\nParent key:\n\n    " + "\n    ".join(parent_keys) + "\n"
    elif len(parent_keys) > 1:
        doc += "\nParent keys:\n\n    " + "\n    ".join(parent_keys) + "\n"
    # Add method list to doc
    doc += "\nQuick method reference:\n\n"
    doc += "\t{0}.".format(name) + "\n\t{0}.".format(name).join(
        ["update(changes)", "strip_style()", "get_data()",
         "to_graph_objs()", "validate()", "to_string()",
         "force_clean()"]) + "\n\n"
    # Add key meta to doc
    keymeta = info['keymeta']
    if len(keymeta):
        doc += "Valid keys:\n\n"
        # Add each key one-by-one and format
        width1 = LINE_SIZE-TAB_SIZE
        width2 = LINE_SIZE-2*TAB_SIZE
        width3 = LINE_SIZE-3*TAB_SIZE
        undocumented = "Aw, snap! Undocumented!"
        for key in keymeta:
            # main portion of documentation
            try:
                required = str(keymeta[key]['required'])
            except KeyError:
                required = undocumented
            try:
                typ = str(keymeta[key]['key_type'])
            except KeyError:
                typ = undocumented
            try:
                val_types = str(keymeta[key]['val_types'])
                if typ == 'object':
                    val_types = ("{0} object | ".format(KEY_TO_NAME[key]) +
                                 val_types)
            except KeyError:
                val_types = undocumented
            try:
                descr = str(keymeta[key]['description'])
            except KeyError:
                descr = undocumented
            str_1 = "{0} [required={1}] (value={2})".format(
                key, required, val_types)
            if "streamable" in keymeta[key] and keymeta[key]["streamable"]:
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
            try:
                if len(keymeta[key]['examples']):
                    ex = "\n\t\tExamples:\n" + "\t\t\t"
                    ex += "\n\t\t\t".join(
                        textwrap.wrap(' | '.join(keymeta[key]['examples']),
                                      width=width3)) + "\n"
                    doc += ex
            except:
                pass
            doc += '\n'
    return doc.expandtabs(TAB_SIZE)


def update_keys(keys):
    """Change keys we used to support to their new equivalent."""
    updated_keys = list()
    for key in keys:
        if key in translations:
            updated_keys += [translations[key]]
        else:
            updated_keys += [key]
    return updated_keys

translations = dict(
    scl="colorscale",
    reversescl="reversescale"
)


def curtail_val_repr(val, max_chars, add_delim=False):
    delim = ", "
    end = ".."
    if isinstance(val, six.string_types):
        if max_chars <= len("'" + end + "'"):
            return ' ' * max_chars
        elif add_delim and max_chars <= len("'" + end + "'") + len(delim):
            return "'" + end + "'" + ' ' * (max_chars - len("'" + end + "'"))
    else:
        if max_chars <= len(end):
            return ' ' * max_chars
        elif add_delim and max_chars <= len(end) + len(delim):
            return end + ' ' * (max_chars - len(end))
    if add_delim:
        max_chars -= len(delim)
    r = repr(val)
    if len(r) > max_chars:
        if isinstance(val, six.string_types):
            # TODO: can we assume this ends in "'"
            r = r[:max_chars - len(end + "'")] + end + "'"
        elif (isinstance(val, list) and
              max_chars >= len("[{end}]".format(end=end))):
            r = r[:max_chars - len(end + ']')] + end + ']'
        else:
            r = r[:max_chars - len(end)] + end
    if add_delim:
        r += delim
    return r
