import json

import _plotly_utils.basevalidators
from codegen.utils import PlotlyNode, TraceNode


def get_validator_params(node: PlotlyNode, store: dict):
    """
    Get params for the validator instance for the supplied node
    and add them to the store.

    Parameters
    ----------
    node : PlotlyNode
        The datatype node (node.is_datatype must evaluate to true) for which
        to build a validator class
    store : dict
        Dictionary to store the JSON data for the validator
    Returns
    -------
    None
    """
    assert isinstance(store, dict)
    assert node.is_datatype

    raw_params = node.get_validator_params()
    params = dict([(k, eval(v)) for k, v in raw_params.items()])
    superclass_name = node.name_base_validator.split(".")[-1]

    key = ".".join(node.parent_path_parts + (node.name_property,))
    store[key] = {"params": params, "superclass": superclass_name}


def get_data_validator_params(base_trace_node: TraceNode, store: dict):
    """
    Add a dict of constructor params for the DataValidator to the store.

    Parameters
    ----------
    base_trace_node : TraceNode
        PlotlyNode that is the parent of all of the individual trace nodes
    store : dict
        Dictionary to store the JSON data for the validator
    Returns
    -------
    None"""
    assert isinstance(store, dict)

    params = build_data_validator_params(base_trace_node)
    store["data"] = {
        "params": params,
        "superclass": "BaseDataValidator",
    }


def write_validator_json(codedir, params: dict):
    """
    Write out a JSON serialization of the validator arguments
    for all validators (keyed by f"{parent_name}.{plotly_name})

    Each validator has a "params": {kwargs} entry and
    a "superclass": str to indicate the class to be instantiated

    Parameters
    ----------
    codedir : str
        Root directory in which the validators package should reside
    params : dict
        Dictionary to store the JSON data for the validator
    Returns
    -------
    None
    """

    # Validate inputs
    if not isinstance(params, dict):
        raise ValueError("Expected params to be a dictionary")

    # Write file
    filepath = codedir / "validators" / "_validators.json"
    with open(filepath, "w") as f:
        f.write(json.dumps(params, indent=4))


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
    tracetype_nodes = base_trace_node.child_compound_datatypes
    class_strs_map = dict(
        [(node.name_property, node.name_datatype_class) for node in tracetype_nodes]
    )

    return {
        "class_strs_map": class_strs_map,
        "plotly_name": "data",
        "parent_name": "",
    }


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
    # We need to eval the values to convert out of the repr-form of the
    # params. e.g. '3' -> 3
    params = build_data_validator_params(base_trace_node)

    # Build and return BaseDataValidator instance
    return _plotly_utils.basevalidators.BaseDataValidator(**params)
