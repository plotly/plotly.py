"""
This module handles accessing, storing, and managing the graph reference.

"""
from __future__ import absolute_import

import hashlib
import json
import os
import re
from pkg_resources import resource_string

import requests
import six

from plotly import files, utils

GRAPH_REFERENCE_PATH = '/v2/plot-schema'
GRAPH_REFERENCE_DOWNLOAD_TIMEOUT = 5  # seconds


# For backwards compat, we keep this list of previously known objects.
# Moving forward, we only add new trace names.
# {<ClassName>: {'object_name': <object_name>, 'base_type': <base-type>}
_BACKWARDS_COMPAT_CLASS_NAMES = {
    'AngularAxis': {'object_name': 'angularaxis', 'base_type': dict},
    'Annotation': {'object_name': 'annotation', 'base_type': dict},
    'Annotations': {'object_name': 'annotations', 'base_type': list},
    'Area': {'object_name': 'area', 'base_type': dict},
    'Bar': {'object_name': 'bar', 'base_type': dict},
    'Box': {'object_name': 'box', 'base_type': dict},
    'ColorBar': {'object_name': 'colorbar', 'base_type': dict},
    'Contour': {'object_name': 'contour', 'base_type': dict},
    'Contours': {'object_name': 'contours', 'base_type': dict},
    'Data': {'object_name': 'data', 'base_type': list},
    'ErrorX': {'object_name': 'error_x', 'base_type': dict},
    'ErrorY': {'object_name': 'error_y', 'base_type': dict},
    'ErrorZ': {'object_name': 'error_z', 'base_type': dict},
    'Figure': {'object_name': 'figure', 'base_type': dict},
    'Font': {'object_name': 'font', 'base_type': dict},
    'Heatmap': {'object_name': 'heatmap', 'base_type': dict},
    'Histogram': {'object_name': 'histogram', 'base_type': dict},
    'Histogram2d': {'object_name': 'histogram2d', 'base_type': dict},
    'Histogram2dContour': {'object_name': 'histogram2dcontour',
                           'base_type': dict},
    'Layout': {'object_name': 'layout', 'base_type': dict},
    'Legend': {'object_name': 'legend', 'base_type': dict},
    'Line': {'object_name': 'line', 'base_type': dict},
    'Margin': {'object_name': 'margin', 'base_type': dict},
    'Marker': {'object_name': 'marker', 'base_type': dict},
    'RadialAxis': {'object_name': 'radialaxis', 'base_type': dict},
    'Scatter': {'object_name': 'scatter', 'base_type': dict},
    'Scatter3d': {'object_name': 'scatter3d', 'base_type': dict},
    'Scene': {'object_name': 'scene', 'base_type': dict},
    'Stream': {'object_name': 'stream', 'base_type': dict},
    'Surface': {'object_name': 'surface', 'base_type': dict},
    'Trace': {'object_name': None, 'base_type': dict},
    'XAxis': {'object_name': 'xaxis', 'base_type': dict},
    'XBins': {'object_name': 'xbins', 'base_type': dict},
    'YAxis': {'object_name': 'yaxis', 'base_type': dict},
    'YBins': {'object_name': 'ybins', 'base_type': dict},
    'ZAxis': {'object_name': 'zaxis', 'base_type': dict}
}


def get_graph_reference():
    """
    Attempts to load local copy of graph reference or makes GET request if DNE.

    :return: (dict) The graph reference.
    :raises: (PlotlyError) When graph reference DNE and GET request fails.

    """
    default_config = files.FILE_CONTENT[files.CONFIG_FILE]
    if files.check_file_permissions():
        graph_reference = utils.load_json_dict(files.GRAPH_REFERENCE_FILE)
        config = utils.load_json_dict(files.CONFIG_FILE)

        # TODO: https://github.com/plotly/python-api/issues/293
        plotly_api_domain = config.get('plotly_api_domain',
                                       default_config['plotly_api_domain'])
    else:
        graph_reference = {}
        plotly_api_domain = default_config['plotly_api_domain']

    sha1 = hashlib.sha1(six.b(str(graph_reference))).hexdigest()

    graph_reference_url = '{}{}?sha1={}'.format(plotly_api_domain,
                                                GRAPH_REFERENCE_PATH, sha1)

    try:
        response = requests.get(graph_reference_url,
                                timeout=GRAPH_REFERENCE_DOWNLOAD_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        if not graph_reference:
            path = os.path.join('graph_reference', 'default-schema.json')
            s = resource_string('plotly', path).decode('utf-8')
            graph_reference = json.loads(s)
    else:
        if six.PY3:
            content = str(response.content, encoding='utf-8')
        else:
            content = response.content
        data = json.loads(content)
        if data['modified']:
            graph_reference = data['schema']

    return utils.decode_unicode(graph_reference)


def string_to_class_name(string):
    """
    Single function to handle turning object names into class names.

    GRAPH_REFERENCE has names like `error_y`, which we'll turn into `ErrorY`.

    :param (str) string: A string that we'll turn into a class name string.
    :return: (str)

    """

    # capitalize first letter
    string = re.sub(r'[A-Za-z]', lambda m: m.group().title(), string, count=1)

    # replace `*_<c>` with `*<C>` E.g., `Error_x` --> `ErrorX`
    string = re.sub(r'_[A-Za-z0-9]+', lambda m: m.group()[1:].title(), string)

    return str(string)


def object_name_to_class_name(object_name):
    """Not all objects have classes auto-generated."""
    if object_name in TRACE_NAMES:
        return string_to_class_name(object_name)

    if object_name in OBJECT_NAME_TO_CLASS_NAME:
        return OBJECT_NAME_TO_CLASS_NAME[object_name]

    if object_name in ARRAYS:
        return 'list'
    else:
        return 'dict'


def get_attributes_dicts(object_name, parent_object_names=()):
    """
    Returns *all* attribute information given the context of parents.

    The response has the form:
    {
      ('some', 'path'): {},
      ('some', 'other', 'path'): {},
      ...
      'additional_attributes': {}
    }

    There may be any number of paths mapping to attribute dicts. There will be
    one attribute dict under 'additional_attributes' which will usually be
    empty.

    :param (str|unicode) object_name: The object name whose attributes we want.
    :param (list[str|unicode]) parent_object_names: Names of parent objects.
    :return: (dict)

    """
    object_dict = OBJECTS[object_name]

    # If we patched this object, we may have added hard-coded attrs.
    additional_attributes = object_dict['additional_attributes']

    # We should also one or more paths where attributes are defined.
    attribute_paths = list(object_dict['attribute_paths'])  # shallow copy

    # If we have parent_names, some of these attribute paths may be invalid.
    for parent_object_name in reversed(parent_object_names):
        if parent_object_name in ARRAYS:
            continue
        parent_object_dict = OBJECTS[parent_object_name]
        parent_attribute_paths = parent_object_dict['attribute_paths']
        for path in list(attribute_paths):
            if not _is_valid_sub_path(path, parent_attribute_paths):
                attribute_paths.remove(path)

    # We return a dict mapping paths to attributes. We also add in additional
    # attributes if defined.
    attributes_dicts = {path: utils.get_by_path(GRAPH_REFERENCE, path)
                  for path in attribute_paths}
    attributes_dicts['additional_attributes'] = additional_attributes

    return attributes_dicts


def get_valid_attributes(object_name, parent_object_names=()):
    attributes = get_attributes_dicts(object_name, parent_object_names)
    # These are for documentation and quick lookups. They're just strings.
    valid_attributes = set()
    for attributes_dict in attributes.values():

        for key, val in attributes_dict.items():
            if key not in GRAPH_REFERENCE['defs']['metaKeys']:
                valid_attributes.add(key)

        deprecated_attributes = attributes_dict.get('_deprecated', {})
        for key, val in deprecated_attributes.items():
            if key not in GRAPH_REFERENCE['defs']['metaKeys']:
                valid_attributes.add(key)

    return valid_attributes


def get_deprecated_attributes(object_name, parent_object_names=()):
    attributes = get_attributes_dicts(object_name, parent_object_names)
    # These are for documentation and quick lookups. They're just strings.
    deprecated_attributes = set()
    for attributes_dict in attributes.values():

        deprecated_attributes_dict = attributes_dict.get('_deprecated', {})
        for key, val in deprecated_attributes_dict.items():
            if key not in GRAPH_REFERENCE['defs']['metaKeys']:
                deprecated_attributes.add(key)

    return deprecated_attributes


def get_subplot_attributes(object_name, parent_object_names=()):
    attributes = get_attributes_dicts(object_name, parent_object_names)
    # These are for documentation and quick lookups. They're just strings.
    subplot_attributes = set()
    for attributes_dict in attributes.values():

        for key, val in attributes_dict.items():
            if key not in GRAPH_REFERENCE['defs']['metaKeys']:
                if isinstance(val, dict) and val.get('_isSubplotObj'):
                    subplot_attributes.add(key)

        deprecated_attributes = attributes_dict.get('_deprecated', {})
        for key, val in deprecated_attributes.items():
            if key not in GRAPH_REFERENCE['defs']['metaKeys']:
                if isinstance(val, dict) and val.get('_isSubplotObj'):
                    subplot_attributes.add(key)

    return subplot_attributes


def attribute_path_to_object_names(attribute_container_path):
    """
    Return a location within a figure from a path existing in GRAPH_REFERENCE.

    Users don't need to know about GRAPH_REFERENCE, so yielding information
    about paths there would only be confusing. Also, the implementation and
    structure there may change, but figure structure won't.

    :param (tuple[str]) attribute_container_path: An object should exist here.

    :return: (tuple[str]) A tuple of object names:

    Example:

        In: ('traces', 'pie', 'attributes', 'marker')
        Out: ('figure', 'data', 'pie', 'marker')

    """
    object_names = ['figure']  # this is always the case

    if 'layout' in attribute_container_path:

        for path_part in attribute_container_path:

            if path_part in OBJECTS:
                object_names.append(path_part)

            if path_part in ARRAYS:
                object_names.append(path_part)
                object_names.append(path_part[:-1])

    elif 'layoutAttributes' in attribute_container_path:

        object_names.append('layout')

        start_index = attribute_container_path.index('layoutAttributes')
        for path_part in attribute_container_path[start_index:]:

            if path_part in OBJECTS:
                object_names.append(path_part)

            if path_part in ARRAYS:
                object_names.append(path_part)
                object_names.append(path_part[:-1])

    else:

        # assume it's in 'traces'
        object_names.append('data')
        for path_part in attribute_container_path:

            if path_part in OBJECTS:
                object_names.append(path_part)

            if path_part in ARRAYS:
                object_names.append(path_part)
                object_names.append(path_part[:-1])

    return tuple(object_names)


def get_role(object_name, attribute, value=None, parent_object_names=()):
    """
    Values have types associated with them based on graph_reference.

    'data' type values are always kept
    'style' values are kept if they're sequences (but not strings)

    :param (str) object_name: The name of the object containing 'attribute'.
    :param (str) attribute: The attribute we want the `role` of.
    :param (*) value: If the value is an array, the return can be different.
    :param parent_object_names: An iterable of obj names from graph reference.
    :returns: (str) This will be 'data', 'style', or 'info'.

    """
    if object_name in TRACE_NAMES and attribute == 'type':
        return 'info'
    attributes_dicts = get_attributes_dicts(object_name, parent_object_names)
    matches = []
    for attributes_dict in attributes_dicts.values():

        for key, val in attributes_dict.items():
            if key == attribute:
                matches.append(val)

        for key, val in attributes_dict.get('_deprecated', {}).items():
            if key == attribute:
                matches.append(val)

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


def _is_valid_sub_path(path, parent_paths):
    """
    Check if a sub path is valid given an iterable of parent paths.

    :param (tuple[str]) path: The path that may be a sub path.
    :param (list[tuple]) parent_paths: The known parent paths.
    :return: (bool)

    Examples:

        * ('a', 'b', 'c') is a valid subpath of ('a', )
        * ('a', 'd') is not a valid subpath of ('b', )
        * ('a', ) is not a valid subpath of ('a', 'b')
        * ('anything',) is a valid subpath of ()

    """
    if not parent_paths:
        return True
    for parent_path in parent_paths:
        if path[:len(parent_path)] == parent_path:
            return True
    return False


def _get_objects():
    """
    Create a reorganization of graph reference which organizes by object name.

    Each object can have *many* different definitions in the graph reference.
    These possibilities get narrowed down when we have contextual information
    about parent objects. For instance, Marker in Scatter has a different
    definition than Marker in Pie. However, we need Marker, Scatter, and Pie
    to exist on their own as well.

    Each value has the form:
    {
        'meta_paths': [],
        'attribute_paths': [],
        'additional_attributes': {}
    }

    * meta_paths describes the top-most path where this object is defined
    * attribute_paths describes all the locations where attributes exist
    * additional_attributes can be used to hard-code (patch) the plot schema

    :return: (dict)

    """
    objects = {}
    for node, path in utils.node_generator(GRAPH_REFERENCE):

        if any([key in path for key in GRAPH_REFERENCE['defs']['metaKeys']]):
            continue  # objects don't exist under nested meta keys
        if node.get('role') != 'object':
            continue
        if 'items' in node:
            continue

        object_name = path[-1]
        if object_name not in objects:
            objects[object_name] = {'meta_paths': [], 'attribute_paths': [],
                                    'additional_attributes': {}}

        if node.get('attributes'):
            objects[object_name]['attribute_paths'].append(
                path + ('attributes', )
            )
        else:
            objects[object_name]['attribute_paths'].append(path)

        objects[object_name]['meta_paths'].append(path)

    return objects


def _patch_objects():
    """Things like Layout, Figure, and Data need to be included."""
    layout_attribute_paths = []
    for node, path in utils.node_generator(GRAPH_REFERENCE):
        if any([key in path for key in GRAPH_REFERENCE['defs']['metaKeys']]):
            continue  # objects don't exist under nested meta keys

        if path and path[-1] == 'layoutAttributes':
            layout_attribute_paths.append(path)

    for trace_name in TRACE_NAMES:
        OBJECTS[trace_name] = {
            'meta_paths': [('traces', trace_name)],
            'attribute_paths': [('traces', trace_name, 'attributes')],
            'additional_attributes': {}
        }

    OBJECTS['layout'] = {'meta_paths': [('layout', )],
                         'attribute_paths': layout_attribute_paths,
                         'additional_attributes': {}}

    figure_attributes = {'layout': {'role': 'object'},
                         'data': {'role': 'object', '_isLinkedToArray': True}}
    OBJECTS['figure'] = {'meta_paths': [],
                         'attribute_paths': [],
                         'additional_attributes': figure_attributes}


def _get_arrays():
    """Very few arrays, but this dict is the complement of OBJECTS."""
    arrays = {}
    for node, path in utils.node_generator(GRAPH_REFERENCE):

        if any([key in path for key in GRAPH_REFERENCE['defs']['metaKeys']]):
            continue  # objects don't exist under nested meta keys
        if node.get('role') != 'object':
            continue
        if 'items' not in node:
            continue

        object_name = path[-1]
        if object_name not in arrays:
            items = node['items']

            # If items is a dict, it's anyOf them.
            if isinstance(items, dict):
                item_names = list(items.keys())
            else:
                item_names = [object_name[:-1]]
            arrays[object_name] = {'meta_paths': [path], 'items': item_names}

    return arrays


def _patch_arrays():
    """Adds information on our eventual Data array."""
    ARRAYS['data'] = {'meta_paths': [('traces', )], 'items': list(TRACE_NAMES)}


def _get_classes():
    """
    We eventually make classes out of the objects in GRAPH_REFERENCE.

    :return: (dict) A mapping of class names to object names.

    """
    classes = {}

    # add all the objects we had before, but mark them if they no longer
    # exist in the graph reference
    for class_name, class_dict in _BACKWARDS_COMPAT_CLASS_NAMES.items():
        object_name = class_dict['object_name']
        base_type = class_dict['base_type']
        if object_name in OBJECTS or object_name in ARRAYS:
            classes[class_name] = {'object_name': object_name,
                                   'base_type': base_type}
        else:
            classes[class_name] = {'object_name': None, 'base_type': base_type}

    # always keep the trace dicts up to date
    for object_name in TRACE_NAMES:
        class_name = string_to_class_name(object_name)
        classes[class_name] = {'object_name': object_name, 'base_type': dict}

    return classes


# The ordering here is important.
GRAPH_REFERENCE = get_graph_reference()

# See http://blog.labix.org/2008/06/27/watch-out-for-listdictkeys-in-python-3
TRACE_NAMES = list(GRAPH_REFERENCE['traces'].keys())

OBJECTS = _get_objects()
_patch_objects()
ARRAYS = _get_arrays()
_patch_arrays()

CLASSES = _get_classes()

OBJECT_NAME_TO_CLASS_NAME = {class_dict['object_name']: class_name
                             for class_name, class_dict in CLASSES.items()
                             if class_dict['object_name'] is not None}
