from __future__ import print_function

from plotly.graph_objs import graph_objs_tools
from plotly.graph_reference import ARRAYS, CLASSES, TRACE_NAMES

FLAG = '# AUTO-GENERATED BELOW. DO NOT EDIT! See makefile.'


def get_non_generated_file_lines():
    """
    Copy each line up to our special FLAG line and return.

    :raises: (ValueError) If the FLAG isn't found.
    :return: (list) The lines we're copying.
    """

    lines_to_copy = []
    flag_found = False
    with open('./plotly/graph_objs/graph_objs.py', 'r') as f:
        for line_to_copy in f:
            if line_to_copy.startswith(FLAG):
                flag_found = True
                break
            lines_to_copy.append(line_to_copy)
    if not flag_found:
        raise ValueError(
            'Failed to find flag:\n"{}"\nin graph_objs_tools.py.'.format(FLAG)
        )
    return lines_to_copy


def print_class(name, f):
    if name == 'Figure':
        print('from plotly.datatypes import Figure', file=f, end='\n\n\n')
    elif name == 'Layout':
        print('from plotly.datatypes import Layout', file=f, end='\n\n\n')
    else:
        class_dict = CLASSES[name]
        object_name = class_dict['object_name']

        if object_name in TRACE_NAMES:
            print('from plotly.datatypes.trace import {}'.format(name), file=f, end='\n\n\n')
        elif object_name in ARRAYS:
            print('class {}(list):'.format(name), file=f, end='\n')
            print('    pass', file=f, end='\n\n\n')
        else:
            print('class {}(dict):'.format(name), file=f, end='\n')
            print('    pass', file=f, end='\n\n\n')


copied_lines = get_non_generated_file_lines()
with open('./plotly/graph_objs/graph_objs.py', 'w') as graph_objs_file:

    # Keep things *exactly* as they were above our special FLAG.
    for line in copied_lines:
        print(line, file=graph_objs_file, end='')
    print(FLAG, file=graph_objs_file)

    # For each object in the plot schema, generate a class in the file.
    class_names = list(CLASSES.keys())
    class_names.sort()
    for class_name in class_names:
        print_class(class_name, graph_objs_file)

    # Finish off the file by only exporting plot-schema names.
    print('__all__ = [cls for cls in graph_reference.CLASSES.keys() '
          'if cls in globals()] + ["FigureWidget"]', file=graph_objs_file)
