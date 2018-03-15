import json
import os.path as opath
import os
import shutil

import time

from codegen.datatypes import build_datatypes_py, write_datatypes_py, append_figure_class
from codegen.utils import TraceNode, PlotlyNode, LayoutNode, FrameNode
from codegen.validators import write_validator_py, append_traces_validator_py


def perform_codegen():
    outdir = 'ipyplotly/'
    # outdir = 'codegen/output'
    # Load plotly schema
    # ------------------
    with open('codegen/resources/plot-schema.json', 'r') as f:
        plotly_schema = json.load(f)

    # Compute property paths
    # ----------------------
    base_traces_node = TraceNode(plotly_schema)
    compound_trace_nodes = PlotlyNode.get_all_compound_datatype_nodes(plotly_schema, TraceNode)
    compound_layout_nodes = PlotlyNode.get_all_compound_datatype_nodes(plotly_schema, LayoutNode)
    compound_frame_nodes = PlotlyNode.get_all_compound_datatype_nodes(plotly_schema, FrameNode)

    extra_layout_nodes = PlotlyNode.get_all_trace_layout_nodes(plotly_schema)

    # Write out validators
    # --------------------
    validators_pkgdir = opath.join(outdir, 'validators')
    if opath.exists(validators_pkgdir):
        shutil.rmtree(validators_pkgdir)

    # ### Layout ###
    for node in compound_layout_nodes:
        write_validator_py(outdir, node, extra_layout_nodes)

    # ### Trace ###
    for node in compound_trace_nodes:
        write_validator_py(outdir, node)

    # Write out datatypes
    # -------------------
    datatypes_pkgdir = opath.join(outdir, 'datatypes')
    if opath.exists(datatypes_pkgdir):
        shutil.rmtree(datatypes_pkgdir)

    # ### Layout ###
    for node in compound_layout_nodes:
        write_datatypes_py(outdir, node, extra_layout_nodes)

    # ### Trace ###
    for node in compound_trace_nodes:
        write_datatypes_py(outdir, node)

    # Append traces validator class
    # -----------------------------
    append_traces_validator_py(validators_pkgdir, base_traces_node)

    # Add Frames
    # ----------
    # ### Validator ###
    for node in compound_frame_nodes:
        write_validator_py(outdir, node)

    # ### Datatypes ###
    for node in compound_frame_nodes:
        write_datatypes_py(outdir, node)

    # Append figure class to datatypes
    # --------------------------------
    append_figure_class(datatypes_pkgdir, base_traces_node)


if __name__ == '__main__':
    perform_codegen()
