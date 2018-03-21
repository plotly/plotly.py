import os
import os.path as opath
import shutil
from io import StringIO
from typing import Dict, Tuple, List

import _plotly_utils.basevalidators
from codegen.utils import format_source, PlotlyNode, TraceNode, \
    write_source_py, build_from_imports_py


def build_validators_py(datatype_node: PlotlyNode):

    buffer = StringIO()

    # Imports
    # -------
    # Compute base validator import
    import_str = '.'.join(
        datatype_node.name_base_validator.split('.')[:-1])

    buffer.write(f'import {import_str }\n')

    # Build Validator
    # ---------------
    params = datatype_node.get_validator_params()

    buffer.write(f"""

class {datatype_node.name_validator}({datatype_node.name_base_validator}):
    def __init__(self, plotly_name={params['plotly_name']},
                       parent_name={params['parent_name']}):""")

    buffer.write(f"""
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name""")

    # Write out remaining constructor parameters
    for attr_name, attr_val in params.items():
        if attr_name in ['plotly_name', 'parent_name']:
            # plotly_name and parent_name are already handled
            continue

        buffer.write(f""",
                 {attr_name}={attr_val}""")

    buffer.write(')')

    return buffer.getvalue()


def write_validator_py(outdir,
                       node: PlotlyNode):

    # Generate source code
    # --------------------
    validator_source = build_validators_py(node)
    if validator_source:
        try:
            formatted_source = format_source(validator_source)
        except Exception as e:
            print(validator_source)
            raise e

        # Write file
        # ----------
        filedir = opath.join(outdir, 'validators', *node.parent_dir_path)
        os.makedirs(filedir, exist_ok=True)
        filepath = opath.join(filedir, '_' + node.name_property + '.py')

        with open(filepath, 'wt') as f:
            f.write(formatted_source)


def write_validators_init_py(outdir, dir_path, import_pairs):
    # Generate source code
    # --------------------
    init_source = build_from_imports_py(import_pairs)

    # Write file
    # ----------
    filepath = opath.join(outdir, 'validators', *dir_path, '__init__.py')
    write_source_py(init_source, filepath)


def build_data_validator_params(base_node: TraceNode):
    tracetype_nodes = base_node.child_compound_datatypes

    # Build class_map repr string
    buffer = StringIO()
    buffer.write('{\n')
    for i, tracetype_node in enumerate(tracetype_nodes):
        sfx = ',' if i < len(tracetype_nodes) else ''

        buffer.write(f"""
            '{tracetype_node.name_property}': '{tracetype_node.name_class}'{sfx}""")

    buffer.write("""
        }""")

    class_map_repr = buffer.getvalue()

    # Build params
    params = {'class_map': class_map_repr,
              'plotly_name': repr('data'),
              'parent_name': repr('')}

    return params


def build_data_validator_py(base_node: TraceNode):
    params = build_data_validator_params(base_node)

    buffer = StringIO()

    buffer.write(f"""
import _plotly_utils.basevalidators
    
    
class DataValidator(_plotly_utils.basevalidators.BaseDataValidator):

    def __init__(self, plotly_name={params['plotly_name']},
                       parent_name={params['parent_name']}):

        super().__init__(class_map={params['class_map']},
                         plotly_name=plotly_name,
                         parent_name=parent_name)""")

    return buffer.getvalue()


def get_data_validator_instance(base_node: TraceNode):
    params = build_data_validator_params(base_node)
    eval_params = {k: eval(repr_val) for k, repr_val in params.items()}

    return _plotly_utils.basevalidators.BaseDataValidator(**eval_params)


def write_data_validator_py(outdir, base_node: TraceNode):

    if base_node.node_path:
        raise ValueError('Expected root trace node. Received node with path "%s"' % base_node.dir_str)

    source = build_data_validator_py(base_node)
    formatted_source = format_source(source)

    # Append to file
    # --------------
    filepath = opath.join(outdir, 'validators', '_data.py')

    with open(filepath, 'wt') as f:
        f.write(formatted_source)
