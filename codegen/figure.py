from io import StringIO
from os import path as opath

from _plotly_utils.basevalidators import (BaseDataValidator,
                                          CompoundValidator,
                                          CompoundArrayValidator)
from codegen.datatypes import (reindent_validator_description,
                               add_constructor_params, add_docstring)
from codegen.utils import PlotlyNode, format_and_write_source_py


def build_figure_py(trace_node, base_package, base_classname, fig_classname,
                    data_validator, layout_validator, frame_validator):
    """

    Parameters
    ----------
    trace_node : PlotlyNode
        Root trace node (the node that is the parent of all of the
        individual trace nodes like bar, scatter, etc.)
    base_package : str
        Package that the figure's superclass resides in
    base_classname : str
        Name of the figure's superclass
    fig_classname : str
        Name of the Figure class to be generated
    data_validator : BaseDataValidator
        DataValidator instance
    layout_validator : CompoundValidator
        LayoutValidator instance
    frame_validator : CompoundArrayValidator
        FrameValidator instance

    Returns
    -------
    str
        Source code for figure class definition
    """

    # Initialize source code buffer
    # -----------------------------
    buffer = StringIO()

    # Get list of trace type nodes
    # ----------------------------
    trace_nodes = trace_node.child_compound_datatypes

    # Write imports
    # -------------
    # ### Import base class ###
    buffer.write(f'from plotly.{base_package} import {base_classname}\n')

    # ### Import trace graph_obj classes ###
    trace_types_csv = ', '.join([n.name_datatype_class for n in trace_nodes])
    buffer.write(f'from plotly.graph_objs import ({trace_types_csv})\n')

    # Write class definition
    # ----------------------
    buffer.write(f"""

class {fig_classname}({base_classname}):\n""")

    # ### Constructor ###
    # Build constructor description strings
    data_description = reindent_validator_description(data_validator, 8)
    layout_description = reindent_validator_description(layout_validator, 8)
    frames_description = reindent_validator_description(frame_validator, 8)

    buffer.write(f"""
    def __init__(self, data=None, layout=None,
                 frames=None, skip_invalid=False):
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
            
        skip_invalid: bool
            If True, invalid properties in the figure specification will be
            skipped silently. If False (default) invalid properties in the
            figure specification will result in a ValueError

        Raises
        ------
        ValueError
            if a property in the specification of data, layout, or frames
            is invalid AND skip_invalid is False
        \"\"\"
        super({fig_classname} ,self).__init__(data, layout,
                                              frames, skip_invalid)
    """)

    # ### add_trace methods for each trace type ###
    for trace_node in trace_nodes:

        # #### Function signature ####
        buffer.write(f"""
    def add_{trace_node.plotly_name}(self""")

        # #### Function params####
        add_constructor_params(buffer,
                               trace_node.child_datatypes,
                               append_extras=['row', 'col'])

        # #### Docstring ####
        header = f"Add a new {trace_node.name_datatype_class} trace"

        extras = (('row : int or None (default)',
                   'Subplot row index (starting from 1) for the trace to be '
                   'added. Only valid if figure was created using '
                   '`plotly.tools.make_subplots`'),
                  ('col : int or None (default)',
                   'Subplot col index (starting from 1) for the trace to be '
                   'added. Only valid if figure was created using '
                   '`plotly.tools.make_subplots`'))

        add_docstring(buffer, trace_node, header, append_extras=extras)

        # #### Function body ####
        buffer.write(f"""
        new_trace = {trace_node.name_datatype_class}(
        """)

        for i, subtype_node in enumerate(trace_node.child_datatypes):
            subtype_prop_name = subtype_node.name_property
            buffer.write(f"""
                {subtype_prop_name}={subtype_prop_name},""")

        buffer.write(f"""
            **kwargs)""")

        buffer.write(f"""
        return self.add_trace(new_trace, row=row, col=col)""")

    # Return source string
    # --------------------
    buffer.write('\n')
    return buffer.getvalue()


def write_figure_classes(outdir, trace_node,
                         data_validator,
                         layout_validator,
                         frame_validator):
    """
    Construct source code for the Figure and FigureWidget classes and
    write to graph_objs/_figure.py and graph_objs/_figurewidget.py
    respectively

    Parameters
    ----------
    outdir : str
        Root outdir in which the graph_objs package should reside
    trace_node : PlotlyNode
        Root trace node (the node that is the parent of all of the
        individual trace nodes like bar, scatter, etc.)
    data_validator : BaseDataValidator
        DataValidator instance
    layout_validator : CompoundValidator
        LayoutValidator instance
    frame_validator : CompoundArrayValidator
        FrameValidator instance

    Returns
    -------
    None
    """

    # Validate inputs
    # ---------------
    if trace_node.node_path:
        raise ValueError(f'Expected root trace node.\n'
                         f'Received node with path "{trace_node.path_str}"')

    # Loop over figure types
    # ----------------------
    base_figures = [('basewidget', 'BaseFigureWidget', 'FigureWidget'),
                    ('basedatatypes', 'BaseFigure', 'Figure')]

    for base_package, base_classname, fig_classname in base_figures:

        # ### Build figure source code string ###
        figure_source = build_figure_py(trace_node,
                                        base_package,
                                        base_classname,
                                        fig_classname,
                                        data_validator,
                                        layout_validator,
                                        frame_validator)

        # ### Format and write to file###
        filepath = opath.join(outdir, 'graph_objs',
                              f'_{fig_classname.lower()}.py')
        format_and_write_source_py(figure_source, filepath)
