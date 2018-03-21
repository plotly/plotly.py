import json
import os.path as opath
import shutil

from codegen.datatypes import (build_datatypes_py, write_datatypes_py,
                               write_figure_class, write_deprecated_datatypes,
                               write_graph_objs_graph_objs,
                               DEPRECATED_DATATYPES)
from codegen.datatypes import write_datatypes_init_py
from codegen.utils import TraceNode, PlotlyNode, LayoutNode, FrameNode
from codegen.validators import (write_validator_py,
                                write_data_validator_py,
                                get_data_validator_instance)
from codegen.validators import write_validators_init_py


# Import notes
# ------------
# Nothing from the plotly/ package should be imported during code
# generation. This introduces a lot of complexity regarding when imports
# happen relative to when various stages of code generation occur.  Instead,
# helpers that are only needed during code generation should reside in the
# codegen/ package, and helpers used both during code generation and at
# runtime should reside in the _plotly_utils/ package.

def perform_codegen():
    outdir = 'plotly'

    # Delete prior codegen output
    # ---------------------------
    validators_pkgdir = opath.join(outdir, 'validators')
    if opath.exists(validators_pkgdir):
        shutil.rmtree(validators_pkgdir)

    graph_objs_pkgdir = opath.join(outdir, 'graph_objs')
    if opath.exists(graph_objs_pkgdir):
        shutil.rmtree(graph_objs_pkgdir)

    # plotly/datatypes is not used anymore, but was at one point so we'll
    # still delete it if we find it in case a developer is upgrading from an
    # older version
    datatypes_pkgdir = opath.join(outdir, 'datatypes')
    if opath.exists(datatypes_pkgdir):
        shutil.rmtree(datatypes_pkgdir)

    # Load plotly schema
    # ------------------
    with open('plotly/package_data/default-schema.json', 'r') as f:
        plotly_schema = json.load(f)

    # Compute property paths
    # ----------------------
    base_traces_node = TraceNode(plotly_schema)
    compound_trace_nodes = PlotlyNode.get_all_compound_datatype_nodes(plotly_schema, TraceNode)
    all_trace_nodes = PlotlyNode.get_all_datatype_nodes(plotly_schema,
                                                        TraceNode)

    compound_layout_nodes = PlotlyNode.get_all_compound_datatype_nodes(plotly_schema, LayoutNode)
    layout_node = compound_layout_nodes[0]
    all_layout_nodes = PlotlyNode.get_all_datatype_nodes(
        plotly_schema, LayoutNode)

    compound_frame_nodes = PlotlyNode.get_all_compound_datatype_nodes(plotly_schema, FrameNode)
    frame_node = compound_frame_nodes[0]
    all_frame_nodes = PlotlyNode.get_all_datatype_nodes(plotly_schema, FrameNode)

    all_datatype_nodes = (all_trace_nodes + all_layout_nodes + all_frame_nodes)

    # Write out validators
    # --------------------
    # # ### Layout ###
    for node in all_layout_nodes:
        write_validator_py(outdir, node)

    # ### Trace ###
    for node in all_trace_nodes:
        write_validator_py(outdir, node)

    # ### Frames ###
    for node in all_frame_nodes:
        write_validator_py(outdir, node)

    # ### Write data (traces) validator ###
    write_data_validator_py(outdir, base_traces_node)

    # Write out datatypes
    # -------------------
    # ### Layout ###
    for node in compound_layout_nodes:
        write_datatypes_py(outdir, node)

    # ### Trace ###
    for node in compound_trace_nodes:
        write_datatypes_py(outdir, node)

    # ### Frames ###
    for node in compound_frame_nodes:
        write_datatypes_py(outdir, node)

    # ### Deprecated ###
    write_deprecated_datatypes(outdir)

    # Write figure class to graph_objs
    # --------------------------------
    data_validator = get_data_validator_instance(base_traces_node)
    layout_validator = layout_node.get_validator_instance()
    frame_validator = frame_node.get_validator_instance()

    write_figure_class(outdir,
                       base_traces_node,
                       data_validator,
                       layout_validator,
                       frame_validator)

    # Write __init__.py files
    # -----------------------
    # ### Write __init__.py files for each validator package ###
    path_to_validator_import_info = {}
    for node in all_datatype_nodes:
        key = node.parent_dir_path
        path_to_validator_import_info.setdefault(key, []).append(
            (f"._{node.name_property}", node.name_validator)
        )

    # Add Data validator
    root_validator_pairs = path_to_validator_import_info[()]
    root_validator_pairs.append(('._data', 'DataValidator'))

    for dir_path, import_pairs in path_to_validator_import_info.items():
        write_validators_init_py(outdir, dir_path, import_pairs)

    # ### Write __init__.py files for each graph_objs package ###
    all_compound_nodes = [node for node in all_datatype_nodes
                          if node.is_compound]

    path_to_datatype_import_info = {}
    for node in all_compound_nodes:
        key = node.parent_dir_path

        # class import
        path_to_datatype_import_info.setdefault(key, []).append(
            (f"._{node.name_undercase}", node.name_class)
        )

        # submodule import
        if node.child_compound_datatypes:
            path_to_datatype_import_info.setdefault(key, []).append(
                (f"plotly.graph_objs{node.parent_pkg_str}", node.name_undercase)
            )

    # ### Write plotly/graph_objs/graph_objs.py for backward compatibility
    write_graph_objs_graph_objs(outdir)

    # Add Figure and FigureWidget
    root_datatype_pairs = path_to_datatype_import_info[()]
    root_datatype_pairs.append(('._figure', 'Figure'))
    root_datatype_pairs.append(('._figurewidget', 'FigureWidget'))

    # Add deprecations
    root_datatype_pairs.append(('._deprecations', DEPRECATED_DATATYPES.keys()))
    for dir_path, import_pairs in path_to_datatype_import_info.items():
        write_datatypes_init_py(outdir, dir_path, import_pairs)


if __name__ == '__main__':
    perform_codegen()
