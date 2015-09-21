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


# for backwards compat, we need to add a few class names
_BACKWARDS_COMPAT_CLASS_NAME_TO_OBJECT_NAME = {
    'AngularAxis': 'angularaxis',
    'ColorBar': 'colorbar',
    'Area': 'scatter',
    'Histogram2d': 'histogram2d',
    'Histogram2dContour': 'histogram2dcontour',
    'RadialAxis': 'radialaxis',
    'Scatter3d': 'scatter3d',
    'XAxis': 'xaxis',
    'XBins': 'xbins',
    'YAxis': 'yaxis',
    'YBins': 'ybins',
    'ZAxis': 'zaxis'
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


def object_name_to_class_name(object_name):
    """
    Single function to handle turning object names into class names.

    GRAPH_REFERENCE has names like `error_y`, which we'll turn into `ErrorY`.

    :param (str) object_name: Presumably an object_name from GRAPH_REFERENCE.
    :return: (str)

    """
    string = _get_hr_name(object_name)

    # capitalize first letter
    string = re.sub(r'[A-Za-z]', lambda m: m.group().title(), string, count=1)

    # replace `*_<c>` with `*<C>` E.g., `Error_x` --> `ErrorX`
    string = re.sub(r'_[A-Za-z0-9]+', lambda m: m.group()[1:].title(), string)

    return string


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


def _get_hr_name(object_name):
    """Get human readable object name from reference ('hrName')."""
    if object_name in ARRAYS:
        return object_name  # TODO: how to handle hr name on array?

    object_dict = OBJECTS[object_name]
    meta_paths = object_dict['meta_paths']
    for meta_path in meta_paths:
        meta_dict = utils.get_by_path(GRAPH_REFERENCE, meta_path)
        if meta_dict.get('_isLinkedToArray'):
            return object_name  # TODO: how to handle hr name on array?
        if 'hrName' in meta_dict:
            return meta_dict['hrName']

    return object_name  # default is to keep the original name


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

        # note that arrays are *not* stored in objects! they're arrays!
        if node.get('role') == 'object':
            object_name = path[-1]
            if node.get('_isLinkedToArray'):
                object_name = object_name[:-1]

            if object_name not in objects:
                objects[object_name] = {'meta_paths': [],
                                        'attribute_paths': [],
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
    for object_name, object_dict in OBJECTS.items():
        meta_paths = object_dict['meta_paths']
        for meta_path in meta_paths:
            meta_dict = utils.get_by_path(GRAPH_REFERENCE, meta_path)
            if meta_dict.get('_isLinkedToArray'):

                # TODO can we have multiply defined arrays?
                arrays[object_name + 's'] = {'meta_paths': [meta_path],
                                             'items': [object_name]}
    return arrays


def _patch_arrays():
    """Adds information on our eventual Data array."""
    ARRAYS['data'] = {'meta_paths': [('traces', )], 'items': list(TRACE_NAMES)}


def _get_class_names_to_object_names():
    """
    We eventually make classes out of the objects in GRAPH_REFERENCE.

    :return: (dict) A mapping of class names to object names.

    """
    class_names_to_object_names = {}
    for object_name in OBJECTS:
        class_name = object_name_to_class_name(object_name)
        class_names_to_object_names[class_name] = object_name

    for array_name in ARRAYS:
        class_name = object_name_to_class_name(array_name)
        class_names_to_object_names[class_name] = array_name

    for class_name in _BACKWARDS_COMPAT_CLASS_NAME_TO_OBJECT_NAME:
        object_name = _BACKWARDS_COMPAT_CLASS_NAME_TO_OBJECT_NAME[class_name]
        class_names_to_object_names[class_name] = object_name

    return class_names_to_object_names


# The ordering here is important.
GRAPH_REFERENCE = get_graph_reference()

# See http://blog.labix.org/2008/06/27/watch-out-for-listdictkeys-in-python-3
TRACE_NAMES = list(GRAPH_REFERENCE['traces'].keys())

OBJECTS = _get_objects()
_patch_objects()
ARRAYS = _get_arrays()
_patch_arrays()

CLASS_NAMES_TO_OBJECT_NAMES = _get_class_names_to_object_names()
