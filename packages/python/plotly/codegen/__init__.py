import json
import os.path as opath
import shutil
import subprocess

from codegen.datatypes import build_datatype_py, write_datatype_py
from codegen.compatibility import (
    write_deprecated_datatypes,
    write_graph_objs_graph_objs,
    DEPRECATED_DATATYPES,
)
from codegen.figure import write_figure_classes
from codegen.utils import (
    TraceNode,
    PlotlyNode,
    LayoutNode,
    FrameNode,
    write_init_py,
    ElementDefaultsNode,
)
from codegen.validators import (
    write_validator_py,
    write_data_validator_py,
    get_data_validator_instance,
)


# Import notes
# ------------
# Nothing from the plotly/ package should be imported during code
# generation. This introduces a lot of complexity regarding when imports
# happen relative to when various stages of code generation occur.  Instead,
# helpers that are only needed during code generation should reside in the
# codegen/ package, and helpers used both during code generation and at
# runtime should reside in the _plotly_utils/ package.
# ----------------------------------------------------------------------------
def preprocess_schema(plotly_schema):
    """
    Central location to make changes to schema before it's seen by the
    PlotlyNode classes
    """

    # Update template
    # ---------------
    layout = plotly_schema["layout"]["layoutAttributes"]

    # Create codegen-friendly template scheme
    template = {
        "data": {
            trace + "s": {"items": {trace: {}}, "role": "object"}
            for trace in plotly_schema["traces"]
        },
        "layout": {},
        "description": """\
Default attributes to be applied to the plot.
This should be a dict with format: `{'layout': layoutTemplate, 'data':
{trace_type: [traceTemplate, ...], ...}}` where `layoutTemplate` is a dict
matching the structure of `figure.layout` and `traceTemplate` is a dict
matching the structure of the trace with type `trace_type` (e.g. 'scatter').
Alternatively, this may be specified as an instance of
plotly.graph_objs.layout.Template.

Trace templates are applied cyclically to
traces of each type. Container arrays (eg `annotations`) have special
handling: An object ending in `defaults` (eg `annotationdefaults`) is
applied to each array item. But if an item has a `templateitemname`
key we look in the template array for an item with matching `name` and
apply that instead. If no matching `name` is found we mark the item
invisible. Any named template item not referenced is appended to the
end of the array, so this can be used to add a watermark annotation or a
logo image, for example. To omit one of these items on the plot, make
an item with matching `templateitemname` and `visible: false`.""",
    }

    layout["template"] = template

    # Rename concentrationscales to colorscale to match conventions
    items = plotly_schema["traces"]["sankey"]["attributes"]["link"]["colorscales"][
        "items"
    ]

    if "concentrationscales" in items:
        items["colorscale"] = items.pop("concentrationscales")


def perform_codegen():
    # Set root codegen output directory
    # ---------------------------------
    # (relative to project root)
    abs_file_path = opath.realpath(__file__)
    packages_py = opath.dirname(opath.dirname(opath.dirname(abs_file_path)))
    outdir = opath.join(packages_py, "plotly", "plotly")

    # Delete prior codegen output
    # ---------------------------
    validators_pkgdir = opath.join(outdir, "validators")
    if opath.exists(validators_pkgdir):
        shutil.rmtree(validators_pkgdir)

    graph_objs_pkgdir = opath.join(outdir, "graph_objs")
    if opath.exists(graph_objs_pkgdir):
        shutil.rmtree(graph_objs_pkgdir)

    # plotly/datatypes is not used anymore, but was at one point so we'll
    # still delete it if we find it in case a developer is upgrading from an
    # older version
    datatypes_pkgdir = opath.join(outdir, "datatypes")
    if opath.exists(datatypes_pkgdir):
        shutil.rmtree(datatypes_pkgdir)

    # Load plotly schema
    # ------------------
    plot_schema_path = opath.join(
        packages_py, "plotly", "codegen", "resources", "plot-schema.json"
    )

    with open(plot_schema_path, "r") as f:
        plotly_schema = json.load(f)

    # Preprocess Schema
    # -----------------
    preprocess_schema(plotly_schema)

    # Build node lists
    # ----------------
    # ### TraceNode ###
    base_traces_node = TraceNode(plotly_schema)
    compound_trace_nodes = PlotlyNode.get_all_compound_datatype_nodes(
        plotly_schema, TraceNode
    )
    all_trace_nodes = PlotlyNode.get_all_datatype_nodes(plotly_schema, TraceNode)

    # ### LayoutNode ###
    compound_layout_nodes = PlotlyNode.get_all_compound_datatype_nodes(
        plotly_schema, LayoutNode
    )
    layout_node = compound_layout_nodes[0]
    all_layout_nodes = PlotlyNode.get_all_datatype_nodes(plotly_schema, LayoutNode)

    subplot_nodes = [
        node
        for node in layout_node.child_compound_datatypes
        if node.node_data.get("_isSubplotObj", False)
    ]

    layout_array_nodes = [
        node
        for node in layout_node.child_compound_datatypes
        if node.is_array_element and node.has_child("xref") and node.has_child("yref")
    ]

    # ### FrameNode ###
    compound_frame_nodes = PlotlyNode.get_all_compound_datatype_nodes(
        plotly_schema, FrameNode
    )
    frame_node = compound_frame_nodes[0]
    all_frame_nodes = PlotlyNode.get_all_datatype_nodes(plotly_schema, FrameNode)

    # ### All nodes ###
    all_datatype_nodes = all_trace_nodes + all_layout_nodes + all_frame_nodes

    all_compound_nodes = [
        node
        for node in all_datatype_nodes
        if node.is_compound and not isinstance(node, ElementDefaultsNode)
    ]

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

    # ### Data (traces) validator ###
    write_data_validator_py(outdir, base_traces_node)

    # Alls
    # ----
    alls = {}

    # Write out datatypes
    # -------------------
    for node in all_compound_nodes:
        write_datatype_py(outdir, node)
        alls.setdefault(node.path_parts, [])
        alls[node.path_parts].extend(
            c.name_datatype_class for c in node.child_compound_datatypes
        )
        if node.parent_path_parts == ():
            # Add top-level classes to alls
            alls.setdefault((), [])
            alls[node.parent_path_parts].append(node.name_datatype_class)

    # ### Deprecated ###
    # These are deprecated legacy datatypes like graph_objs.Marker
    write_deprecated_datatypes(outdir)

    # Write figure class to graph_objs
    # --------------------------------
    data_validator = get_data_validator_instance(base_traces_node)
    layout_validator = layout_node.get_validator_instance()
    frame_validator = frame_node.get_validator_instance()

    write_figure_classes(
        outdir,
        base_traces_node,
        data_validator,
        layout_validator,
        frame_validator,
        subplot_nodes,
        layout_array_nodes,
    )

    # Write datatype __init__.py files
    # --------------------------------
    # ### Build mapping from parent package to datatype class ###
    path_to_datatype_import_info = {}
    for node in all_compound_nodes:
        key = node.parent_path_parts

        # submodule import
        if node.child_compound_datatypes:

            path_to_datatype_import_info.setdefault(key, []).append(
                (f"plotly.graph_objs{node.parent_dotpath_str}", node.name_undercase)
            )
            alls[node.parent_path_parts].append(node.name_undercase)

    # ### Write plotly/graph_objs/graph_objs.py ###
    # This if for backward compatibility. It just imports everything from
    # graph_objs/__init__.py
    write_graph_objs_graph_objs(outdir)

    # ### Add Figure and FigureWidget ###
    root_datatype_imports = path_to_datatype_import_info[()]
    root_datatype_imports.append(("._figure", "Figure"))
    alls[()].append("Figure")

    # ### Add deprecations ###
    root_datatype_imports.append(("._deprecations", DEPRECATED_DATATYPES.keys()))
    alls[()].extend(DEPRECATED_DATATYPES.keys())

    # Sort alls
    for k, v in alls.items():
        alls[k] = list(sorted(v))

    optional_figure_widget_import = f"""
__all__ = {alls[()]}
try:
    import ipywidgets
    from distutils.version import LooseVersion
    if LooseVersion(ipywidgets.__version__) >= LooseVersion('7.0.0'):
        from ._figurewidget import FigureWidget
    del LooseVersion
    del ipywidgets
    __all__.append("FigureWidget")
except ImportError:
    pass
"""
    root_datatype_imports.append(optional_figure_widget_import)

    # ### __all__ ###
    for path_parts, class_names in alls.items():
        if path_parts and class_names:
            filepath = opath.join(outdir, "graph_objs", *path_parts, "__init__.py")
            with open(filepath, "at") as f:
                f.write(f"\n__all__ = {class_names}")

    # ### Output datatype __init__.py files ###
    graph_objs_pkg = opath.join(outdir, "graph_objs")
    for path_parts, import_pairs in path_to_datatype_import_info.items():
        write_init_py(graph_objs_pkg, path_parts, import_pairs)

    # ### Output graph_objects.py alias
    graph_objects_path = opath.join(outdir, "graph_objects.py")
    with open(graph_objects_path, "wt") as f:
        f.write(
            f"""\
from __future__ import absolute_import
from plotly.graph_objs import *
__all__ = {alls[()]}"""
        )

    # ### Run black code formatter on output directories ###
    subprocess.call(["black", "--target-version=py27", validators_pkgdir])
    subprocess.call(["black", "--target-version=py27", graph_objs_pkgdir])
    subprocess.call(["black", "--target-version=py27", graph_objects_path])


if __name__ == "__main__":
    perform_codegen()
