import os
import os.path as opath
import textwrap
from io import StringIO
from typing import List, Tuple

from codegen.utils import format_source, PlotlyNode, \
    write_source_py, build_from_imports_py

DEPRECATED_DATATYPES = {
    # List types
    'Data':
        {'base_type': list,
         'new': ['Scatter', 'Bar', 'Area', 'Histogram', 'etc.']},
    'Annotations':
        {'base_type': list,
         'new': ['layout', 'layout.scene']},
    'Frames':
        {'base_type': list,
         'new': ['Frame']},

    # Dict types
    'AngularAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.polar']},
    'Annotation':
        {'base_type': dict,
         'new': ['layout', 'layout.scene']},
    'ColorBar':
        {'base_type': dict,
         'new': ['scatter.marker', 'surface', 'etc.']},
    'Contours':
        {'base_type': dict,
         'new': ['contour', 'surface', 'etc.']},
    'ErrorX':
        {'base_type': dict,
         'new': ['scatter', 'histogram', 'etc.']},
    'ErrorY':
        {'base_type': dict,
         'new': ['scatter', 'histogram', 'etc.']},
    'ErrorZ':
        {'base_type': dict,
         'new': ['scatter3d']},
    'Font':
        {'base_type': dict,
         'new': ['layout', 'layout.hoverlabel', 'etc.']},
    'Legend':
        {'base_type': dict,
         'new': ['layout']},
    'Line':
        {'base_type': dict,
         'new': ['scatter', 'layout.shape', 'etc.']},
    'Margin':
        {'base_type': dict,
         'new': ['layout']},
    'Marker':
        {'base_type': dict,
         'new': ['scatter', 'histogram.selected', 'etc.']},
    'RadialAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.polar']},
    'Scene':
        {'base_type': dict,
         'new': ['Scene']},
    'Stream':
        {'base_type': dict,
         'new': ['scatter', 'area']},
    'XAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.scene']},
    'YAxis':
        {'base_type': dict,
         'new': ['layout', 'layout.scene']},
    'ZAxis':
        {'base_type': dict,
         'new': ['layout.scene']},
    'XBins':
        {'base_type': dict,
         'new': ['histogram', 'histogram2d']},
    'YBins':
        {'base_type': dict,
         'new': ['histogram', 'histogram2d']},
    'Trace':
        {'base_type': dict,
         'new': ['Scatter', 'Bar', 'Area', 'Histogram', 'etc.']},
    'Histogram2dcontour':
        {'base_type': dict,
         'new': ['Histogram2dContour']},
}


def get_typing_type(plotly_type, array_ok=False):
    if plotly_type in ('data_array', 'info_array', 'colorlist'):
        pytype = 'List'
    elif plotly_type in ('string', 'color', 'colorscale', 'subplotid'):
        pytype = 'str'
    elif plotly_type in ('enumerated', 'flaglist', 'any'):
        pytype = 'Any'
    elif plotly_type in ('number', 'angle'):
        pytype = 'Number'
    elif plotly_type == 'integer':
        pytype = 'int'
    elif plotly_type == 'boolean':
        pytype = 'bool'
    else:
        raise ValueError('Unknown plotly type: %s' % plotly_type)

    if array_ok:
        return f'Union[{pytype}, List[{pytype}]]'
    else:
        return pytype


def build_datatypes_py(compound_node: PlotlyNode):

    buffer = StringIO()

    # Imports
    # -------
    buffer.write('from typing import *\n')
    buffer.write('from numbers import Number\n')
    buffer.write(
        f'from plotly.basedatatypes import {compound_node.base_datatype_class}\n')

    # ### Import type's validator package with rename ###
    buffer.write(
        f'from plotly.validators{compound_node.parent_pkg_str} import '
        f'{compound_node.name_undercase} as v_{compound_node.name_undercase}\n')

    # ### Import type's graph_objs package with rename ###
    # If type has any compound children, then import that package that holds
    #  them
    if compound_node.child_compound_datatypes:
        buffer.write(
            f'from plotly.graph_objs{compound_node.parent_pkg_str} import '
            f'{compound_node.name_undercase} as d_{compound_node.name_undercase}\n')

    # Save literal nodes
    # ------------------
    literal_nodes = [n for n in compound_node.child_literals if
                     n.plotly_name in ['type']]

    # Write class definition
    # ----------------------
    buffer.write(f"""

class {compound_node.name_class}({compound_node.base_datatype_class}):\n""")

    # ### Property definitions ###
    child_datatype_nodes = compound_node.child_datatypes

    subtype_nodes = child_datatype_nodes
    for subtype_node in subtype_nodes:
        if subtype_node.is_array_element:
            prop_type = f'Tuple[d_{compound_node.plotly_name}.{subtype_node.name_class}]'
        elif subtype_node.is_compound:
            prop_type = f'd_{compound_node.plotly_name}.{subtype_node.name_class}'
        else:
            prop_type = get_typing_type(subtype_node.datatype)

        # #### Get property description ####
        raw_description = subtype_node.description
        property_description = '\n'.join(textwrap.wrap(raw_description,
                                                       subsequent_indent=' ' * 8,
                                                       width=79 - 8))

        # # #### Get validator description ####
        validator = subtype_node.get_validator_instance()
        if validator:
            validator_description = reindent_validator_description(validator, 4)

            # #### Combine to form property docstring ####
            if property_description.strip():
                property_docstring = f"""{property_description}
    
        {validator_description}"""
            else:
                property_docstring = validator_description
        else:
            property_docstring = property_description

        # #### Write property ###
        buffer.write(f"""\

    # {subtype_node.name_property}
    # {'-' * len(subtype_node.name_property)}
    @property
    def {subtype_node.name_property}(self) -> {prop_type}:
        \"\"\"
        {property_docstring}
        \"\"\"
        return self['{subtype_node.name_property}']""")

        # #### Set property ###
        buffer.write(f"""

    @{subtype_node.name_property}.setter
    def {subtype_node.name_property}(self, val):
        self['{subtype_node.name_property}'] = val\n""")

        # ### Literals ###
    for literal_node in literal_nodes:
        buffer.write(f"""\

    # {literal_node.name_property}
    # {'-' * len(literal_node.name_property)}
    @property
    def {literal_node.name_property}(self) -> {prop_type}:
        return self._props['{literal_node.name_property}']\n""")

    # ### Self properties description ###
    buffer.write(f"""

    # property parent name
    # --------------------
    @property
    def _parent_path(self) -> str:
        return '{compound_node.parent_dir_str}'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self) -> str:
        return \"\"\"\\""")

    buffer.write(compound_node.get_constructor_params_docstring(
        indent=8))

    buffer.write(f"""
        \"\"\"""")

    # ### Constructor ###
    buffer.write(f"""
    def __init__(self""")

    add_constructor_params(buffer, subtype_nodes)
    header = f"Construct a new {compound_node.name_pascal_case} object"
    add_docstring(buffer, compound_node, header=header)

    buffer.write(f"""
        super().__init__('{compound_node.name_property}', **kwargs)

        # Initialize validators
        # ---------------------""")
    for subtype_node in subtype_nodes:
        buffer.write(f"""
        self._validators['{subtype_node.name_property}'] = v_{compound_node.name_undercase}.{subtype_node.name_validator}()""")

    buffer.write(f"""

        # Populate data dict with properties
        # ----------------------------------""")
    for subtype_node in subtype_nodes:
        buffer.write(f"""
        self.{subtype_node.name_property} = {subtype_node.name_property}""")

    # ### Literals ###
    literal_nodes = [n for n in compound_node.child_literals if
                     n.plotly_name in ['type']]
    if literal_nodes:
        buffer.write(f"""

        # Read-only literals
        # ------------------""")
        for literal_node in literal_nodes:
            buffer.write(f"""
        self._props['{literal_node.name_property}'] = '{literal_node.node_data}'""")

    return buffer.getvalue()


def reindent_validator_description(validator, extra_indent):
    # Remove leading indent and add extra spaces to subsequent indent
    return ('\n' + ' ' * extra_indent).join(validator.description().strip().split('\n'))


def add_constructor_params(buffer, subtype_nodes, colon=True):
    for i, subtype_node in enumerate(subtype_nodes):
        dflt = None
        buffer.write(f""",
            {subtype_node.name_property}={repr(dflt)}""")

    buffer.write(""",
            **kwargs""")
    buffer.write(f"""
        ){':' if colon else ''}""")


def add_docstring(buffer, compound_node, header):

    node_description = compound_node.description
    if node_description:
        description_lines = textwrap.wrap(
            node_description,
            width=79-8,
            subsequent_indent=' ' * 8)

        node_description = '\n'.join(description_lines) + '\n\n'

    # ### Docstring ###
    buffer.write(f"""
        \"\"\"
        {header}
        
        {node_description}        Parameters
        ----------""")
    buffer.write(compound_node.get_constructor_params_docstring(
        indent=8))

    # #### close docstring ####
    buffer.write(f"""

        Returns
        -------
        {compound_node.name_pascal_case}
        \"\"\"""")


def write_datatypes_py(outdir, node: PlotlyNode):

    # Generate source code
    # --------------------
    datatype_source = build_datatypes_py(node)
    if datatype_source:
        try:
            formatted_source = format_source(datatype_source)
        except Exception as e:
            print(datatype_source)
            raise e

        # Write file
        # ----------
        filedir = opath.join(outdir, 'graph_objs', *node.parent_dir_path)
        os.makedirs(filedir, exist_ok=True)
        filepath = opath.join(filedir, '_' + node.name_undercase + '.py')

        with open(filepath, 'wt') as f:
            f.write(formatted_source)


def build_datatypes_init_py(root_dir: str, dir_path: Tuple[str], nodes: List['PlotlyNode']):
    buffer = StringIO()
    for node in nodes:
        buffer.write(f"""\
from ._{node.name_undercase} import {node.name_class}\n""")

    return buffer.getvalue()


def write_datatypes_init_py(outdir, dir_path, import_pairs):
    # Generate source code
    # --------------------
    init_source = build_from_imports_py(import_pairs)

    # Write file
    # ----------
    filepath = opath.join(outdir, 'graph_objs', *dir_path, '__init__.py')
    write_source_py(init_source, filepath)


def build_figure_py(trace_node, base_package, base_classname, fig_classname,
                    data_validator, layout_validator, frame_validator):
    buffer = StringIO()
    trace_nodes = trace_node.child_compound_datatypes

    # Imports
    # -------
    buffer.write(f'from plotly.{base_package} import {base_classname}\n')

    trace_types_csv = ', '.join([n.name_pascal_case for n in trace_nodes])
    buffer.write(f'from plotly.graph_objs import ({trace_types_csv})\n')

    buffer.write(f"""

class {fig_classname}({base_classname}):\n""")

    # Build constructor description strings
    data_description = reindent_validator_description(data_validator, 8)
    layout_description = reindent_validator_description(layout_validator, 8)
    frames_description = reindent_validator_description(frame_validator, 8)

    buffer.write(f"""
    def __init__(self, data=None, layout=None, frames=None):
        \"\"\"
        Create a new {fig_classname} instance
        
        Parameters
        ----------
        data
            {data_description}
        layout
            {layout_description}
        frames
            {frames_description}
        \"\"\"
        super().__init__(data, layout, frames)
    """)

    # add_trace methods
    for trace_node in trace_nodes:

        # Function signature
        # ------------------
        buffer.write(f"""
    def add_{trace_node.plotly_name}(self""")

        add_constructor_params(buffer, trace_node.child_datatypes)
        header = f"Add a new {trace_node.name_pascal_case} trace"
        add_docstring(buffer, trace_node, header)

        # Function body
        # -------------
        buffer.write(f"""
        new_trace = {trace_node.name_pascal_case}(
        """)

        for i, subtype_node in enumerate(trace_node.child_datatypes):
            is_last = i == len(trace_node.child_datatypes) - 1
            buffer.write(f"""
                {subtype_node.name_property}={subtype_node.name_property}{'' if is_last else ','}""")

        buffer.write(f""",
            **kwargs)""")

        buffer.write(f"""
        return self.add_traces(new_trace)[0]""")

    buffer.write('\n')
    return buffer.getvalue()


def write_figure_class(outdir, trace_node,
                       data_validator,
                       layout_validator,
                       frame_validator):

    if trace_node.node_path:
        raise ValueError('Expected root trace node. Received node with path "%s"' % trace_node.dir_str)

    base_figures = [('basewidget', 'BaseFigureWidget', 'FigureWidget'),
                    ('basedatatypes', 'BaseFigure', 'Figure')]

    for base_package, base_classname, fig_classname in base_figures:
        figure_source = build_figure_py(trace_node,
                                        base_package,
                                        base_classname,
                                        fig_classname,
                                        data_validator,
                                        layout_validator,
                                        frame_validator)
        formatted_source = format_source(figure_source)

        # Write to file
        # -------------
        filepath = opath.join(outdir, 'graph_objs', f'_{fig_classname.lower()}.py')

        with open(filepath, 'wt') as f:
            f.write(formatted_source)


def build_dict_deprecation_message(class_name, opts):
    replacements = []
    for repl in opts['new']:

        if repl == 'etc.':
            replacements.append(repl)
        else:
            repl_parts = repl.split('.')

            # Add class_name if class not provided
            repl_is_class = repl_parts[-1][0].isupper()
            if not repl_is_class:
                repl_parts.append(class_name)

            # Add plotly.graph_objs prefix
            full_class_str = '.'.join(['plotly', 'graph_objs'] + repl_parts)
            replacements.append(full_class_str)

    replacemens_str = '\n  - '.join(replacements)

    if opts['base_type'] == list:
        return f"""\
plotly.graph_objs.{class_name} is deprecated.
Please replace it with a list or tuple of instances of the following types
  - {replacemens_str}
"""
    else:
        return f"""\
plotly.graph_objs.{class_name} is deprecated.
Please replace it with one of the following more specific types
  - {replacemens_str}
"""


def build_deprecated_datatypes_py():
    buffer = StringIO()
    buffer.write('import warnings\n')
    buffer.write(r"""
warnings.filterwarnings('default',
                        r'plotly\.graph_objs\.\w+ is deprecated',
                        DeprecationWarning)


""")

    for class_name, opts in DEPRECATED_DATATYPES.items():
        base_class_name = opts['base_type'].__name__
        depr_msg = build_dict_deprecation_message(class_name, opts)

        buffer.write(f"""\
class {class_name}({base_class_name}):
    \"\"\"
    {depr_msg}
    \"\"\"
    def __init__(self, *args, **kwargs):
        \"\"\"
        {depr_msg}
        \"\"\"
        warnings.warn(\"\"\"{depr_msg}\"\"\", DeprecationWarning)
        super().__init__(*args, **kwargs)\n\n\n""")

    return buffer.getvalue()


def write_deprecated_datatypes(outdir):
    formatted_source = format_source(build_deprecated_datatypes_py())

    # Write to file
    # -------------
    filepath = opath.join(outdir, 'graph_objs', '_deprecations.py')

    with open(filepath, 'wt') as f:
        f.write(formatted_source)


def write_graph_objs_graph_objs(outdir):
    filepath = opath.join(outdir, 'graph_objs', 'graph_objs.py')
    with open(filepath, 'wt') as f:
        f.write("""\
from plotly.graph_objs import *
""")

