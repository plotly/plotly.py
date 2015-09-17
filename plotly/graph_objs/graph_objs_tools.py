from __future__ import absolute_import
import textwrap
import six

from plotly import exceptions, graph_reference

# Define line and tab size for help text!
LINE_SIZE = 76
TAB_SIZE = 4


def get_class_create_args(object_name, list_class=list, dict_class=dict):
    """
    Graph objects are created dynamically, this assists that process.

    We default to `list` and `dict` because importing `PlotlyDict` and
    `PlotlyList` would be circular and doesn't make sense hierarchically.

    :param (str|unicode) object_name: The object name from GRAPH_REFERENCE.
    :param list_class: Either `list` or `PlotlyList`.
    :param dict_class: Either `dict` or `PlotlyDict`.
    :return: (str, type, dict) class_name, class_bases, and class_dict values.

    """
    object_paths = graph_reference.OBJECTS[object_name]

    class_name = graph_reference.object_name_to_class_name(object_name)

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
        _deprecated_attributes = set()
        _subplot_attributes = set()
        for object_info in object_infos:
            _attributes.update(object_info['attributes'])
            _deprecated_attributes.update(object_info['deprecated_attributes'])
            _subplot_attributes.update(object_info['subplot_attributes'])
        _attributes = list(_attributes)
        _deprecated_attributes = list(_deprecated_attributes)
        _subplot_attributes = list(_subplot_attributes)
        class_bases = (dict_class, )
        class_dict = {'__name__': class_name, '_name': object_name,
                      '_attributes': _attributes,
                      '_deprecated_attributes': _deprecated_attributes,
                      '_subplot_attributes': _subplot_attributes}

    return class_name, class_bases, class_dict


def make_doc(object_name):
    """
    Single path to create general documentation based on the object name.

    Graph objects are created dynamically based on external information. The
    docs are also based on this information and must be created at runtime.

    :param (str|unicode) object_name: The object name from GRAPH_REFERENCE.
    :return: (str) The formatted doc string.

    """
    _, class_bases, _ = get_class_create_args(object_name)

    if class_bases[0] == list:
        return _make_list_doc(object_name)
    else:
        return _make_dict_doc(object_name)


def _make_list_doc(name):

    # TODO: https://github.com/plotly/python-api/issues/289
    items = get_class_create_args(name)[2]['_items']
    items_classes = [graph_reference.object_name_to_class_name(item)
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
    """
    Used mostly by the `to_string` function on Graph Objects to pretty print.

    Limit the number of characters of output, but keep the representation
    pretty.

    :param (*) val: The `repr(val)` result is what gets curtailed.
    :param (int) max_chars: Max number of chars which may be returned.
    :param (bool) add_delim: Used if a value is *not* the last in an iterable.
    :return: (str)

    """
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


def get_role(parent, key, value=None):
    """
    Values have types associated with them based on graph_reference.

    'data' type values are always kept
    'style' values are kept if they're sequences (but not strings)

    :returns: (bool)

    """
    parents = parent.get_parents() + [parent]
    parent_names = [p._name for p in parents]

    object_name = parent_names[-1]
    try:
        parent_object_name = parent_names[-2]
    except IndexError:
        parent_object_name = None

    object_paths = graph_reference.OBJECTS[object_name]
    if object_paths:
        object_infos = [graph_reference.get_object_info(path, object_name)
                        for path in object_paths]
    else:
        object_info = graph_reference.get_object_info(None, object_name)
        object_infos = [object_info]

    if parent_object_name is not None:
        object_infos = [object_info for object_info in object_infos
                        if object_info['parent'] == parent_object_name]

    # TODO: I'd be curious to know if object_infos can have length > 1 ?
    role = None
    for object_info in object_infos:

        # we assume the first match holds for all
        if key in object_info['attributes']:
            role = object_info['attributes'][key]['role']
            array_ok = object_info['attributes'][key].get('arrayOk', False)

            if value is not None and array_ok:
                iterable = hasattr(value, '__iter__')
                stringy = isinstance(value, six.string_types)
                dicty = isinstance(value, dict)
                if iterable and not stringy and not dicty:
                    role = 'data'

        if role == 'data':
            break  # we do this to play it as conservatively as possible.

    return role


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


def sort_keys(key):
    """
    Temporary function. See https://github.com/plotly/python-api/issues/290.

    :param (str|unicode) key: The attribute we're sorting on.
    :return: (bool, str|unicode) The naturally-sortable tuple.

    """
    is_special = key in 'rtxyz'
    return not is_special, key
