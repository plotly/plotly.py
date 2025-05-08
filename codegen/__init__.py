import json
import os
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
    build_from_imports_py,
)
from codegen.validators import (
    get_data_validator_params,
    get_validator_params,
    write_validator_json,
    get_data_validator_instance,
)

# Target Python version for code formatting with Black.
# Must be one of the values listed in pyproject.toml.
BLACK_TARGET_VERSIONS = "py38 py39 py310 py311 py312"


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


def perform_codegen(reformat=True):
    # Set root codegen output directory
    # ---------------------------------
    # (relative to project root)
    abs_file_path = opath.realpath(__file__)
    project_root = opath.dirname(opath.dirname(abs_file_path))
    outdir = opath.join(project_root, "plotly")

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
        project_root, "codegen", "resources", "plot-schema.json"
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

    validator_params = {}
    # Write out validators
    # --------------------
    # # ### Layout ###
    for node in all_layout_nodes:
        get_validator_params(node, validator_params)

    # ### Trace ###
    for node in all_trace_nodes:
        get_validator_params(node, validator_params)

    # ### Frames ###
    for node in all_frame_nodes:
        get_validator_params(node, validator_params)

    # ### Data (traces) validator ###
    get_data_validator_params(base_traces_node, validator_params)

    # Write out the JSON data for the validators
    os.makedirs(validators_pkgdir, exist_ok=True)
    write_validator_json(outdir, validator_params)

    # Alls
    # ----
    alls = {}

    # Write out datatypes
    # -------------------
    for node in all_compound_nodes:
        write_datatype_py(outdir, node)

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
    datatype_rel_class_imports = {}
    datatype_rel_module_imports = {}

    for node in all_compound_nodes:
        key = node.parent_path_parts

        # class import
        datatype_rel_class_imports.setdefault(key, []).append(
            f"._{node.name_undercase}.{node.name_datatype_class}"
        )

        # submodule import
        if node.child_compound_datatypes:
            datatype_rel_module_imports.setdefault(key, []).append(
                f".{node.name_undercase}"
            )

    # ### Write plotly/graph_objs/graph_objs.py ###
    # This if for backward compatibility. It just imports everything from
    # graph_objs/__init__.py
    write_graph_objs_graph_objs(outdir)

    # ### Add Figure and FigureWidget ###
    root_datatype_imports = datatype_rel_class_imports[()]
    root_datatype_imports.append("._figure.Figure")

    # ### Add deprecations ###
    for dep_clas in DEPRECATED_DATATYPES:
        root_datatype_imports.append(f"._deprecations.{dep_clas}")

    optional_figure_widget_import = f"""
__all__.append("FigureWidget")
orig_getattr = __getattr__
def __getattr__(import_name):
    if import_name == "FigureWidget":
        try:
            import ipywidgets
            from packaging.version import Version

            if Version(ipywidgets.__version__) >= Version("7.0.0"):
                from ..graph_objs._figurewidget import FigureWidget
                return FigureWidget
            else:
                raise ImportError()
        except Exception:
            from ..missing_anywidget import FigureWidget
            return FigureWidget

    return orig_getattr(import_name)
"""
    # ### __all__ ###
    for path_parts, class_names in alls.items():
        if path_parts and class_names:
            filepath = opath.join(outdir, "graph_objs", *path_parts, "__init__.py")
            with open(filepath, "at") as f:
                f.write(f"\n__all__ = {class_names}")

    # ### Output datatype __init__.py files ###
    graph_objs_pkg = opath.join(outdir, "graph_objs")
    for path_parts in datatype_rel_class_imports:
        rel_classes = sorted(datatype_rel_class_imports[path_parts])
        rel_modules = sorted(datatype_rel_module_imports.get(path_parts, []))
        if path_parts == ():
            init_extra = optional_figure_widget_import
        else:
            init_extra = ""
        write_init_py(graph_objs_pkg, path_parts, rel_modules, rel_classes, init_extra)

    # ### Output graph_objects.py alias
    graph_objects_rel_classes = [
        "..graph_objs." + rel_path.split(".")[-1]
        for rel_path in datatype_rel_class_imports[()]
    ]
    graph_objects_rel_modules = [
        "..graph_objs." + rel_module.split(".")[-1]
        for rel_module in datatype_rel_module_imports[()]
    ]

    graph_objects_init_source = build_from_imports_py(
        graph_objects_rel_modules,
        graph_objects_rel_classes,
        init_extra=optional_figure_widget_import,
    )
    graph_objects_path = opath.join(outdir, "graph_objects", "__init__.py")
    os.makedirs(opath.join(outdir, "graph_objects"), exist_ok=True)
    with open(graph_objects_path, "wt") as f:
        f.write(graph_objects_init_source)

    # ### Run black code formatter on output directories ###
    if reformat:
        target_version = [
            f"--target-version={v}" for v in BLACK_TARGET_VERSIONS.split()
        ]
        subprocess.call(["black", *target_version, validators_pkgdir])
        subprocess.call(["black", *target_version, graph_objs_pkgdir])
        subprocess.call(["black", *target_version, graph_objects_path])
    else:
        print("skipping reformatting")


if __name__ == "__main__":
    perform_codegen()
