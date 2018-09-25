import os.path as opath
from io import StringIO

import _plotly_utils.basevalidators
from codegen.utils import (PlotlyNode, TraceNode,
                           format_and_write_source_py)


def build_validator_py(node: PlotlyNode):
    """
    Build validator class source code string for a datatype PlotlyNode

    Parameters
    ----------
    node : PlotlyNode
        The datatype node (node.is_datatype must evaluate to true) for which
        to build the validator class
    Returns
    -------
    str
        String containing source code for the validator class definition
    """

    # Validate inputs
    # ---------------
    assert node.is_datatype

    # Initialize source code buffer
    # -----------------------------
    buffer = StringIO()

    # Imports
    # -------
    # ### Import package of the validator's superclass ###
    import_str = '.'.join(
        node.name_base_validator.split('.')[:-1])
    buffer.write(f'import {import_str }\n')

    # Build Validator
    # ---------------
    # ### Get dict of validator's constructor params ###
    params = node.get_validator_params()

    # ### Write class definition ###
    class_name = node.name_validator_class
    superclass_name = node.name_base_validator
    buffer.write(f"""

class {class_name}({superclass_name}):
    def __init__(self, plotly_name={params['plotly_name']},
                       parent_name={params['parent_name']},
                       **kwargs):""")

    # ### Write constructor ###
    buffer.write(f"""
        super({class_name}, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name""")

    # Write out remaining constructor parameters
    for attr_name, attr_val in params.items():
        if attr_name in ['plotly_name', 'parent_name']:
            # plotly_name and parent_name are already handled
            continue

        buffer.write(f""",
                 {attr_name}=kwargs.pop('{attr_name}', {attr_val})""")

    buffer.write(f""",
        **kwargs""")


    buffer.write(')')

    # ### Return buffer's string ###
    return buffer.getvalue()


def write_validator_py(outdir,
                       node: PlotlyNode):
    """
    Build validator source code and write to a file

    Parameters
    ----------
    outdir : str
        Root outdir in which the validators package should reside
    node : PlotlyNode
        The datatype node (node.is_datatype must evaluate to true) for which
        to build a validator class
    Returns
    -------
    None
    """
    # Generate source code
    # --------------------
    validator_source = build_validator_py(node)

    # Write file
    # ----------
    filepath = opath.join(outdir, 'validators',
                          *node.parent_path_parts,
                          '_' + node.name_property + '.py')

    format_and_write_source_py(validator_source, filepath)


def build_data_validator_params(base_trace_node: TraceNode):
    """
    Build a dict of constructor params for the DataValidator.
    (This is the validator that inputs a list of traces)
    Parameters
    ----------
    base_trace_node : PlotlyNode
        PlotlyNode that is the parent of all of the individual trace nodes
    Returns
    -------
    dict
        Mapping from property name to repr-string of property value.
    """
    # Get list of trace nodes
    # -----------------------
    tracetype_nodes = base_trace_node.child_compound_datatypes

    # Build class_map_repr string
    # ---------------------------
    # This is the repr-form of a dict from trace propert name string
    # to the name of the trace datatype class in the graph_objs package.
    buffer = StringIO()
    buffer.write('{\n')
    for i, tracetype_node in enumerate(tracetype_nodes):
        sfx = ',' if i < len(tracetype_nodes) else ''
        trace_name = tracetype_node.name_property
        trace_datatype_class = tracetype_node.name_datatype_class
        buffer.write(f"""
            '{trace_name}': '{trace_datatype_class}'{sfx}""")

    buffer.write("""
        }""")

    class_map_repr = buffer.getvalue()

    # Build params dict
    # -----------------
    params = {'class_strs_map': class_map_repr,
              'plotly_name': repr('data'),
              'parent_name': repr('')}

    return params


def build_data_validator_py(base_trace_node: TraceNode):
    """
    Build source code for the DataValidator
    (this is the validator that inputs a list of traces)

    Parameters
    ----------
    base_trace_node : PlotlyNode
        PlotlyNode that is the parent of all of the individual trace nodes
    Returns
    -------
    str
        Source code string for DataValidator class
    """

    # Get constructor params
    # ----------------------
    params = build_data_validator_params(base_trace_node)

    # Build source code
    # -----------------
    buffer = StringIO()

    buffer.write(f"""
import _plotly_utils.basevalidators

class DataValidator(_plotly_utils.basevalidators.BaseDataValidator):

    def __init__(self, plotly_name={params['plotly_name']},
                       parent_name={params['parent_name']},
                       **kwargs):

        super(DataValidator, self).__init__(class_strs_map={params['class_strs_map']},
                         plotly_name=plotly_name,
                         parent_name=parent_name,
                         **kwargs)""")

    return buffer.getvalue()


def get_data_validator_instance(base_trace_node: TraceNode):
    """
    Construct an instance of the DataValidator
    (this is the validator that inputs a list of traces)

    Parameters
    ----------
    base_trace_node :
        PlotlyNode that is the parent of all of the individual trace nodes
    Returns
    -------
    BaseDataValidator
    """

    # Build constructor params
    # ------------------------
    # We need to eval the values to convert out of the repr-form of the
    # params. e.g. '3' -> 3
    params = build_data_validator_params(base_trace_node)
    eval_params = {k: eval(repr_val) for k, repr_val in params.items()}

    # Build and return BaseDataValidator instance
    # -------------------------------------------
    return _plotly_utils.basevalidators.BaseDataValidator(**eval_params)


def write_data_validator_py(outdir, base_trace_node: TraceNode):
    """
    Construct and write out the DataValidator
    (this is the validator that inputs a list of traces)

    Parameters
    ----------
    outdir : str
        Root outdir in which the top-level validators package should reside
    base_trace_node : PlotlyNode
        PlotlyNode that is the parent of all of the individual trace nodes
    Returns
    -------
    None
    """
    # Validate inputs
    # ---------------
    if base_trace_node.node_path:
        raise ValueError('Expected root trace node.\n'
                         'Received node with path "%s"'
                         % base_trace_node.path_str)

    # Build Source
    # ------------
    source = build_data_validator_py(base_trace_node)

    # Write file
    # ----------
    filepath = opath.join(outdir, 'validators', '_data.py')
    format_and_write_source_py(source, filepath)