import os
import os.path as opath
import shutil
from io import StringIO
from typing import Dict

from codegen.utils import format_source, PlotlyNode, TraceNode

def build_validators_py(parent_node: PlotlyNode,
                        extra_nodes: Dict[str, 'PlotlyNode'] = {}):

    extra_subtype_nodes = [node for node_name, node in
                           extra_nodes.items() if
                           parent_node.dir_str and node_name.startswith(parent_node.dir_str)]

    datatype_nodes = parent_node.child_datatypes + extra_subtype_nodes

    if not datatype_nodes:
        return None

    buffer = StringIO()

    # Imports
    # -------
    # Compute needed imports
    import_strs = set()
    for datatype_node in datatype_nodes:
        module_str = '.'.join(datatype_node.name_base_validator.split('.')[:-1])
        import_strs.add(module_str)

    for import_str in import_strs:
        buffer.write(f'import {import_str}\n')

    # Check for colorscale node
    # -------------------------
    colorscale_node_list = [node for node in datatype_nodes if node.datatype == 'colorscale']
    if colorscale_node_list:
        colorscale_path = colorscale_node_list[0].dir_str
    else:
        colorscale_path = None

        # Compound datatypes loop
    # -----------------------
    for datatype_node in datatype_nodes:

        parent_dir_str = datatype_node.parent_dir_str if datatype_node.parent_dir_str else 'figure'
        buffer.write(f"""
        
class {datatype_node.name_validator}({datatype_node.name_base_validator}):
    def __init__(self, plotly_name='{datatype_node.name_property}', parent_name='{parent_dir_str}'):""")

        # Add import
        if datatype_node.is_compound:
            buffer.write(f"""
        from ipyplotly.datatypes{parent_node.pkg_str} import {datatype_node.name_pascal_case}""")

        buffer.write(f"""
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name""")

        if datatype_node.is_array_element:
            buffer.write(f""",
                         element_class={datatype_node.name_class},
                         element_docs=\"\"\"{datatype_node.get_constructor_params_docstring()}\"\"\"""")
        elif datatype_node.is_compound:
            buffer.write(f""",
                         data_class={datatype_node.name_class},
                         data_docs=\"\"\"{datatype_node.get_constructor_params_docstring()}\"\"\"""")
        else:
            assert datatype_node.is_simple

            # Exclude general properties
            excluded_props = ['valType', 'description', 'role', 'dflt']
            if datatype_node.datatype == 'subplotid':
                # Default is required for subplotid validator
                excluded_props.remove('dflt')

            attr_nodes = [n for n in datatype_node.simple_attrs
                          if n.plotly_name not in excluded_props]

            attr_dict = {node.name_undercase: repr(node.node_data) for node in attr_nodes}

            # Add special properties
            if datatype_node.datatype == 'color' and colorscale_path:
                attr_dict['colorscale_path'] = repr(colorscale_path)

            for attr_name, attr_val in attr_dict.items():
                buffer.write(f""",
                         {attr_name}={attr_val}""")

        buffer.write(')')

    return buffer.getvalue()


def write_validator_py(outdir,
                       node: PlotlyNode,
                       extra_nodes: Dict[str, 'PlotlyNode'] = {}):

    # Generate source code
    # --------------------
    validator_source = build_validators_py(node, extra_nodes)
    if validator_source:
        try:
            formatted_source = format_source(validator_source)
        except Exception as e:
            print(validator_source)
            raise e

        # Write file
        # ----------
        filedir = opath.join(outdir, 'validators', *node.dir_path)
        os.makedirs(filedir, exist_ok=True)
        filepath = opath.join(filedir, '__init__.py')

        mode = 'at' if os.path.exists(filepath) else 'wt'
        with open(filepath, mode) as f:
            if mode == 'at':
                f.write("\n\n")
            f.write(formatted_source)
            f.flush()
            os.fsync(f.fileno())


def build_traces_validator_py(base_node: TraceNode):
    tracetype_nodes = base_node.child_compound_datatypes
    buffer = StringIO()

    import_csv = ', '.join([tracetype_node.name_class for tracetype_node in tracetype_nodes])

    buffer.write(f"""
class DataValidator(ipyplotly.basevalidators.BaseDataValidator):

    def __init__(self, plotly_name='data', parent_name='figure'):
        from ipyplotly.datatypes.trace import ({import_csv})
        super().__init__(class_map={{
    """)

    for i, tracetype_node in enumerate(tracetype_nodes):
        sfx = ',' if i < len(tracetype_nodes) else ''

        buffer.write(f"""
            '{tracetype_node.name_property}': {tracetype_node.name_class}{sfx}""")

    buffer.write("""
        },
        plotly_name=plotly_name,
        parent_name=parent_name)""")

    return buffer.getvalue()


def append_traces_validator_py(outdir, base_node: TraceNode):

    if base_node.node_path:
        raise ValueError('Expected root trace node. Received node with path "%s"' % base_node.dir_str)

    source = build_traces_validator_py(base_node)
    formatted_source = format_source(source)

    # Append to file
    # --------------
    filepath = opath.join(outdir, '__init__.py')

    with open(filepath, 'a') as f:
        f.write('\n\n')
        f.write(formatted_source)
        f.flush()
        os.fsync(f.fileno())
