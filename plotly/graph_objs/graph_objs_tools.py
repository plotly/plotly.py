from __future__ import absolute_import
import textwrap
import six

from plotly import exceptions, graph_reference

# Define line and tab size for help text!
LINE_SIZE = 76
TAB_SIZE = 4


def make_doc(object_name):
    """
    Single path to create general documentation based on the object name.

    Graph objects are created dynamically based on external information. The
    docs are also based on this information and must be created at runtime.

    :param (str|unicode) object_name: The object name from GRAPH_REFERENCE.
    :return: (str) The formatted doc string.

    """
    if object_name in graph_reference.ARRAYS:
        return _make_list_doc(object_name)
    else:
        return _make_dict_doc(object_name)


def _make_list_doc(name):

    # TODO: https://github.com/plotly/python-api/issues/289
    items = graph_reference.ARRAYS[name]['items']
    items_classes = [graph_reference.object_name_to_class_name(item)
                     for item in items]
    doc = 'Documentation for {}.\n'.format(name)
    doc = '\t' + '\n\t'.join(textwrap.wrap(doc, width=LINE_SIZE)) + '\n\n'

    items_string = '\n\t* {}\n'.format('\n\t* '.join(items_classes))
    doc += 'Valid Item Classes:\n{}\n'.format(items_string)
    return doc.expandtabs(TAB_SIZE)


def _make_dict_doc(name):

    # TODO: https://github.com/plotly/python-api/issues/289
    attributes = graph_reference.get_valid_attributes(name)
    attributes = sorted(attributes, key=sort_keys)
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
    if parent._name in graph_reference.TRACE_NAMES and key == 'type':
        return 'info'
    matches = []
    parent_object_names = [p._name for p in parent.get_parents()]
    attributes_dicts = graph_reference.get_attributes_dicts(
        parent._name, parent_object_names=parent_object_names
    )
    for val in attributes_dicts.values():

        for k, v in val.items():
            if k == key:
                matches.append(v)

        for k, v in val.get('_deprecated', {}).items():
            if k == key:
                matches.append(v)

    roles = []
    for match in matches:
        role = match['role']
        array_ok = match.get('arrayOk')
        if value is not None and array_ok:
            iterable = hasattr(value, '__iter__')
            stringy = isinstance(value, six.string_types)
            dicty = isinstance(value, dict)
            if iterable and not stringy and not dicty:
                role = 'data'
        roles.append(role)

    # TODO: this is ambiguous until the figure is in place...
    if 'data' in roles:
        role = 'data'
    else:
        role = roles[0]
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
