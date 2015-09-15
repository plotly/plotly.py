from __future__ import absolute_import

import json
import os
import textwrap
from collections import OrderedDict
from pkg_resources import resource_string

import six

from plotly import utils


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
from plotly import exceptions, graph_reference

# Define line and tab size for help text!
LINE_SIZE = 76
TAB_SIZE = 4


def get_class_create_args(object_name, list_class=list, dict_class=dict):

    object_paths = graph_reference.OBJECTS[object_name]

    class_name = graph_reference.string_to_class_name(object_name)

    if object_paths:
        object_infos = [graph_reference.get_object_info(path, object_name)
                        for path in object_paths]
    else:
        object_info = graph_reference.get_object_info(None, object_name)
        object_infos = [object_info]

    if object_infos[0]['is_array']:

        _items = set()
        for object_info in object_infos:
            _items.update(object_info['items'])
        _items = list(_items)
        class_bases = (list_class, )
        class_dict = {'__name__': class_name, '_name': object_name,
                      '_items': _items}

    else:

        _attributes = set()
        for object_info in object_infos:
            _attributes.update(object_info['attributes'])
        _attributes = list(_attributes)
        class_bases = (dict_class, )
        class_dict = {'__name__': class_name, '_name': object_name,
                      '_attributes': _attributes}

    return class_name, class_bases, class_dict


def make_doc(object_name):

    _, class_bases, _ = get_class_create_args(object_name)

    if class_bases[0] == list:
        return _make_list_doc(object_name)
    else:
        return _make_dict_doc(object_name)


def _make_list_doc(name):

    # TODO: https://github.com/plotly/python-api/issues/289
    items = get_class_create_args(name)[2]['_items']
    items_classes = [graph_reference.string_to_class_name(item)
                     for item in items]
    doc = 'Documentation for {}.\n'.format(name)
    doc = '\t' + '\n\t'.join(textwrap.wrap(doc, width=LINE_SIZE)) + '\n\n'

    items_string = '\n\t* {}\n'.format('\n\t* '.join(items_classes))
    doc += 'Valid Item Classes:\n{}\n'.format(items_string)
    return doc.expandtabs(TAB_SIZE)


def _make_dict_doc(name):

    # TODO: https://github.com/plotly/python-api/issues/289
    attributes = get_class_create_args(name)[2]['_attributes']
    doc = 'Documentation for {}'.format(name)
    doc = '\t' + '\n\t'.join(textwrap.wrap(doc, width=LINE_SIZE)) + '\n\n'

    attributes_string = '\n\t* {}\n'.format('\n\t* '.join(attributes))
    doc += 'Valid Attributes:\n{}\n'.format(attributes_string)
    return doc.expandtabs(TAB_SIZE)


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


def value_is_data(obj_name, key, value):
    """
    Values have types associated with them based on graph_reference.

    'data' type values are always kept
    'style' values are kept if they're sequences (but not strings)

    :param (str) obj_name: E.g., 'scatter', 'figure'
    :param (str) key: E.g., 'x', 'y', 'text'
    :param (*) value:
    :returns: (bool)

    """
    try:
        key_type = INFO[obj_name]['keymeta'][key]['key_type']
    except KeyError:
        return False

    if key_type not in ['data', 'style']:
        return False

    if key_type == 'data':
        return True

    if key_type == 'style':
        iterable = hasattr(value, '__iter__')
        stringy = isinstance(value, six.string_types)
        dicty = isinstance(value, dict)
        return iterable and not stringy and not dicty

    return False

def assign_id_to_src(src_name, src_value):
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

