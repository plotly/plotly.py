from io import StringIO
import os
import os.path as opath
import textwrap
import importlib
from typing import List, Dict

from codegen.utils import TraceNode, format_source, PlotlyNode


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


def build_datatypes_py(parent_node: PlotlyNode,
                       extra_nodes: Dict[str, 'PlotlyNode'] = {}):

    compound_nodes = parent_node.child_compound_datatypes
    if not compound_nodes:
        return None

    buffer = StringIO()

    # Imports
    # -------
    buffer.write('from typing import *\n')
    buffer.write('from numbers import Number\n')
    buffer.write(f'from ipyplotly.basedatatypes import {parent_node.base_datatype_class}\n')

    # ### Validators ###
    validators_csv = ', '.join([f'{n.plotly_name} as v_{n.plotly_name}' for n in compound_nodes])
    buffer.write(f'from ipyplotly.validators{parent_node.pkg_str} import ({validators_csv})\n')

    # ### Datatypes ###
    datatypes_csv = ', '.join([f'{n.plotly_name} as d_{n.plotly_name}' for n in compound_nodes if n.child_compound_datatypes])
    if datatypes_csv:
        buffer.write(f'from ipyplotly.datatypes{parent_node.pkg_str} import ({datatypes_csv})\n')

    # Compound datatypes loop
    # -----------------------
    for compound_node in compound_nodes:

        # grab literals
        literal_nodes = [n for n in compound_node.child_literals if n.plotly_name in ['type']]

        # ### Class definition ###
        buffer.write(f"""

class {compound_node.name_class}({parent_node.base_datatype_class}):\n""")

        # ### Property definitions ###
        child_datatype_nodes = compound_node.child_datatypes
        extra_subtype_nodes = [node for node_name, node in
                               extra_nodes.items() if
                               node_name.startswith(compound_node.dir_str)]

        subtype_nodes = child_datatype_nodes + extra_subtype_nodes
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
                                                           width=80 - 8))

            # #### Get validator description ####
            validator = subtype_node.validator_instance
            validator_description = reindent_validator_description(validator, 4)

            # #### Combine to form property docstring ####
            if property_description.strip():
                property_docstring = f"""{property_description}  
                
        {validator_description}"""
            else:
                property_docstring = validator_description

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
            indent=8,
            extra_nodes=extra_subtype_nodes))

        buffer.write(f"""
        \"\"\"""")

        # ### Constructor ###
        buffer.write(f"""
    def __init__(self""")

        add_constructor_params(buffer, subtype_nodes)
        add_docstring(buffer, compound_node, extra_subtype_nodes)

        buffer.write(f"""
        super().__init__('{compound_node.name_property}', **kwargs)
        
        # Initialize validators
        # ---------------------""")
        for subtype_node in subtype_nodes:

            buffer.write(f"""
        self._validators['{subtype_node.name_property}'] = v_{compound_node.plotly_name}.{subtype_node.name_validator}()""")

        buffer.write(f"""
        
        # Populate data dict with properties
        # ----------------------------------""")
        for subtype_node in subtype_nodes:
            buffer.write(f"""
        self.{subtype_node.name_property} = {subtype_node.name_property}""")

        # ### Literals ###
        literal_nodes = [n for n in compound_node.child_literals if n.plotly_name in ['type']]
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


def add_docstring(buffer, compound_node, extra_subtype_nodes=[]):
    # ### Docstring ###
    buffer.write(f"""
        \"\"\"
        Construct a new {compound_node.name_pascal_case} object
        
        Parameters
        ----------""")
    buffer.write(compound_node.get_constructor_params_docstring(
        indent=8,
        extra_nodes=extra_subtype_nodes ))

    # #### close docstring ####
    buffer.write(f"""

        Returns
        -------
        {compound_node.name_pascal_case}
        \"\"\"""")


def write_datatypes_py(outdir, node: PlotlyNode,
                       extra_nodes: Dict[str, 'PlotlyNode']={}):

    # Generate source code
    # --------------------
    datatype_source = build_datatypes_py(node, extra_nodes)
    if datatype_source:
        try:
            formatted_source = format_source(datatype_source)
        except Exception as e:
            print(datatype_source)
            raise e

        # Write file
        # ----------
        filedir = opath.join(outdir, 'datatypes', *node.dir_path)
        os.makedirs(filedir, exist_ok=True)
        filepath = opath.join(filedir, '__init__.py')

        mode = 'at' if os.path.exists(filepath) else 'wt'
        with open(filepath, mode) as f:
            if mode == 'at':
                f.write("\n\n")
            f.write(formatted_source)
            f.flush()
            os.fsync(f.fileno())


def build_figure_py(trace_node, base_package, base_classname, fig_classname):
    buffer = StringIO()
    trace_nodes = trace_node.child_compound_datatypes

    # Imports
    # -------
    buffer.write(f'from ipyplotly.{base_package} import {base_classname}\n')

    trace_types_csv = ', '.join([n.name_pascal_case for n in trace_nodes])
    buffer.write(f'from ipyplotly.datatypes.trace import ({trace_types_csv})\n')

    buffer.write(f"""

class {fig_classname}({base_classname}):\n""")

    # Reload validators and datatypes modules since we're appending
    # Classes to them as we go
    validators_module = importlib.import_module('ipyplotly.validators')
    importlib.reload(validators_module)
    datatypes_module = importlib.import_module('ipyplotly.datatypes')
    importlib.reload(datatypes_module)

    # Build constructor description strings
    data_validator = validators_module.DataValidator()
    data_description = reindent_validator_description(data_validator, 8)

    layout_validator = validators_module.LayoutValidator()
    layout_description = reindent_validator_description(layout_validator, 8)

    frames_validator = validators_module.FramesValidator()
    frames_description = reindent_validator_description(frames_validator, 8)

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
        add_docstring(buffer, trace_node)

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


def append_figure_class(outdir, trace_node):

    if trace_node.node_path:
        raise ValueError('Expected root trace node. Received node with path "%s"' % trace_node.dir_str)

    base_figures = [('basewidget', 'BaseFigureWidget', 'FigureWidget'),
                    ('basedatatypes', 'BaseFigure', 'Figure')]

    for base_package, base_classname, fig_classname in base_figures:
        figure_source = build_figure_py(trace_node, base_package, base_classname, fig_classname)
        formatted_source = format_source(figure_source)

        # Append to file
        # --------------
        filepath = opath.join(outdir, '__init__.py')

        with open(filepath, 'a') as f:
            f.write('\n\n')
            f.write(formatted_source)
            f.flush()
            os.fsync(f.fileno())
