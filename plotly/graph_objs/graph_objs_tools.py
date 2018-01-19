from __future__ import absolute_import
import re
import textwrap
import six

from plotly import exceptions, graph_reference

# Define line and tab size for help text!
LINE_SIZE = 76
TAB_SIZE = 4


def get_help(object_name, path=(), parent_object_names=(), attribute=None):
    """
    Returns a help string for a graph object.

    :param (str) object_name: An object name from GRAPH_REFERENCE
    :param (tuple[str]) path: The path within a `figure` object.
    :param parent_object_names: An iterable of names of this object's parents.
    :param (str|None) attribute: An attribute of <object_name> given <path>.
    :return: (str) A printable string to show to users.

    """
    if object_name in graph_reference.ARRAYS:
        help_string = _list_help(object_name, path, parent_object_names)
    else:
        if attribute:
            help_string = _dict_attribute_help(object_name, path,
                                               parent_object_names, attribute)
        else:
            help_string = _dict_object_help(object_name, path,
                                            parent_object_names)
    return help_string.expandtabs(TAB_SIZE)


def _list_help(object_name, path=(), parent_object_names=()):
    """See get_help()."""
    items = graph_reference.ARRAYS[object_name]['items']
    items_classes = set()
    for item in items:
        if item in graph_reference.OBJECT_NAME_TO_CLASS_NAME:
            items_classes.add(graph_reference.string_to_class_name(item))
        else:
            # There are no lists objects which can contain list entries.
            items_classes.add('dict')
    items_classes = list(items_classes)
    items_classes.sort()
    lines = textwrap.wrap(repr(items_classes), width=LINE_SIZE-TAB_SIZE-1)

    help_dict = {
        'object_name': object_name,
        'path_string': '[' + ']['.join(repr(k) for k in path) + ']',
        'parent_object_names': parent_object_names,
        'items_string': '\t' + '\n\t'.join(lines)
    }

    return (
        "Valid items for '{object_name}' at path {path_string} under parents "
        "{parent_object_names}:\n{items_string}\n".format(**help_dict)
    )


def _dict_object_help(object_name, path, parent_object_names):
    """See get_help()."""
    attributes = list(
        graph_reference.get_valid_attributes(object_name, parent_object_names))
    attributes.sort()
    lines = textwrap.wrap(repr(list(attributes)), width=LINE_SIZE-TAB_SIZE-1)

    help_dict = {
        'object_name': object_name,
        'path_string': '[' + ']['.join(repr(k) for k in path) + ']',
        'parent_object_names': parent_object_names,
        'attributes_string': '\t' + '\n\t'.join(lines)
    }

    return (
        "Valid attributes for '{object_name}' at path {path_string} under "
        "parents {parent_object_names}:\n\n{attributes_string}\n\n"
        "Run `<{object_name}-object>.help('attribute')` on any of the above.\n"
        "'<{object_name}-object>' is the object at {path_string}"
        .format(**help_dict)
    )


def _dict_attribute_help(object_name, path, parent_object_names, attribute):
    """
    Get general help information or information on a specific attribute.

    See get_help().

    :param (str|unicode) attribute: The attribute we'll get info for.

    """
    help_dict = {
        'object_name': object_name,
        'path_string': '[' + ']['.join(repr(k) for k in path) + ']',
        'parent_object_names': parent_object_names,
        'attribute': attribute
    }

    valid_attributes = graph_reference.get_valid_attributes(
        object_name, parent_object_names
    )

    help_string = (
        "Current path: {path_string}\n"
        "Current parent object_names: {parent_object_names}\n\n")

    if attribute not in valid_attributes:
        help_string += "'{attribute}' is not allowed here.\n"
        return help_string.format(**help_dict)

    attributes_dicts = graph_reference.get_attributes_dicts(
        object_name, parent_object_names
    )

    attribute_definitions = []
    additional_definition = None
    meta_keys = graph_reference.GRAPH_REFERENCE['defs']['metaKeys']
    trace_names = graph_reference.TRACE_NAMES
    for key, attribute_dict in attributes_dicts.items():
        if attribute in attribute_dict:
            if object_name in trace_names and attribute == 'type':
                d = {'role': 'info'}
            else:
                d = {k: v for k, v in attribute_dict[attribute].items()
                     if k in meta_keys and not k.startswith('_')}
        elif attribute in attribute_dict.get('_deprecated', {}):
            deprecate_attribute_dict = attribute_dict['_deprecated'][attribute]
            d = {k: v for k, v in deprecate_attribute_dict.items()
                 if k in meta_keys and not k.startswith('_')}
            d['deprecated'] = True
        else:
            continue

        if key == 'additional_attributes':
            additional_definition = d
            continue

        new_definition = True
        for item in attribute_definitions:
            if item['definition'] == d:
                item['paths'].append(key)
                new_definition = False
        if new_definition:
            attribute_definitions.append({'paths': [key], 'definition': d})

    if attribute_definitions:
        help_string += ("With the current parents, '{attribute}' can be "
                        "used as follows:\n\n")

    help_string = help_string.format(**help_dict)

    for item in attribute_definitions:
        valid_parents_objects_names = [
            graph_reference.attribute_path_to_object_names(definition_path)
            for definition_path in item['paths']
        ]

        if len(valid_parents_objects_names) == 1:
            valid_parent_objects_names = valid_parents_objects_names[0]
            help_string += 'Under {}:\n\n'.format(
                str(valid_parent_objects_names)
            )
        else:
            help_string += 'Under any of:\n\t\t* {}\n\n'.format(
                '\n\t\t* '.join(str(tup) for tup in valid_parents_objects_names)
            )

        for meta_key, val in sorted(item['definition'].items()):
            help_string += '\t{}: '.format(meta_key)
            if meta_key == 'description':

                # TODO: https://github.com/plotly/streambed/issues/3950
                if isinstance(val, list) and attribute == 'showline':
                    val = val[0]

                lines = textwrap.wrap(val, width=LINE_SIZE-1)
                help_string += '\n\t\t'.join(lines)
            else:
                help_string += '{}'.format(val)
            help_string += '\n'
        help_string += '\n\n'

    if additional_definition:
        help_string += 'Additionally:\n\n'
        for item in sorted(additional_definition.items()):
            help_string += '\t{}: {}\n'.format(*item)
        help_string += '\n'

    return help_string


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


_underscore_attr_regex = re.compile(
    "(" + "|".join(graph_reference.UNDERSCORE_ATTRS) + ")"
)


def _key_parts(key):
    if "_" in key:
        match = _underscore_attr_regex.search(key)
        if match is not None:
            if key in graph_reference.UNDERSCORE_ATTRS:
                # we have _exactly_ one of the underscore
                # attrs
                return [key]
            else:
                # have one underscore in the UNDERSCORE_ATTR
                # and then at least one underscore not part
                # of the attr. Need to break out the attr
                # and then split the other parts
                parts = []
                if match.start() == 0:
                    # UNDERSCORE_ATTR is at start of key
                    parts.append(match.group(1))
                else:
                    # something comes first
                    before = key[0:match.start()-1]
                    parts.extend(before.split("_"))
                    parts.append(match.group(1))

                # now take care of anything that might come
                # after the underscore attr
                if match.end() < len(key):
                    parts.extend(key[match.end()+1:].split("_"))

                return parts
        else:  # no underscore attributes. just split on `_`
            return key.split("_")

    else:
        return [key]


def _underscore_magic(parts, val, obj=None, skip_dict_check=False):
    if obj is None:
        obj = {}

    if isinstance(parts, str):
        return _underscore_magic(_key_parts(parts), val, obj)

    if isinstance(val, dict) and not skip_dict_check:
        return _underscore_magic_dict(parts, val, obj)

    if len(parts) == 1:
        obj[parts[0]] = val

    if len(parts) == 2:
        k1, k2 = parts
        d1 = obj.get(k1, dict())
        d1[k2] = val
        obj[k1] = d1

    if len(parts) == 3:
        k1, k2, k3 = parts
        d1 = obj.get(k1, dict())
        d2 = d1.get(k2, dict())
        d2[k3] = val
        d1[k2] = d2
        obj[k1] = d1

    if len(parts) == 4:
        k1, k2, k3, k4 = parts
        d1 = obj.get(k1, dict())
        d2 = d1.get(k2, dict())
        d3 = d2.get(k3, dict())
        d3[k4] = val
        d2[k3] = d3
        d1[k2] = d2
        obj[k1] = d1

    if len(parts) > 4:
        msg = (
            "The plotly schema shouldn't have any attributes nested"
            " beyond level 4. Check that you are setting a valid attribute"
        )
        raise ValueError(msg)

    return obj


def _underscore_magic_dict(parts, val, obj=None):
    if obj is None:
        obj = {}
    if not isinstance(val, dict):
        msg = "This function is only meant to be called when val is a dict"
        raise ValueError(msg)

    # make sure obj has the key all the way up to parts
    _underscore_magic(parts, {}, obj, True)

    for key, val2 in val.items():
        _underscore_magic(parts + [key], val2, obj)

    return obj


def attr(obj=None, **kwargs):
    if obj is None:
        obj = dict()

    for k, v in kwargs.items():
        _underscore_magic(k, v, obj)

    return obj
