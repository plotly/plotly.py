from io import StringIO
from os import path as opath

from _plotly_utils.basevalidators import (
    BaseDataValidator,
    CompoundValidator,
    CompoundArrayValidator,
)
from codegen.datatypes import (
    reindent_validator_description,
    add_constructor_params,
    add_docstring,
)
from codegen.utils import PlotlyNode, write_source_py

import inflect


def build_figure_py(
    trace_node,
    base_package,
    base_classname,
    fig_classname,
    data_validator,
    layout_validator,
    frame_validator,
    subplot_nodes,
    layout_array_nodes,
):
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
    subplot_nodes: list of str
        List of names of all of the layout subplot properties
    layout_array_nodes: list of PlotlyNode
        List of array nodes under layout that can be positioned using xref/yref
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
    buffer.write(f"from plotly.{base_package} import {base_classname}\n")

    # Write class definition
    # ----------------------
    buffer.write(
        f"""

class {fig_classname}({base_classname}):\n"""
    )

    # ### Constructor ###
    # Build constructor description strings
    data_description = reindent_validator_description(data_validator, 8)
    layout_description = reindent_validator_description(layout_validator, 8)
    frames_description = reindent_validator_description(frame_validator, 8)

    buffer.write(
        f"""
    def __init__(self, data=None, layout=None,
                 frames=None, skip_invalid=False, **kwargs):
        \"\"\"
        Create a new :class:{fig_classname} instance

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
                                              frames, skip_invalid,
                                              **kwargs)
    """
    )

    # ### add_trace methods for each trace type ###
    for trace_node in trace_nodes:

        include_secondary_y = bool(
            [d for d in trace_node.child_datatypes if d.name_property == "yaxis"]
        )

        # #### Function signature ####
        buffer.write(
            f"""
    def add_{trace_node.plotly_name}(self"""
        )

        # #### Function params####
        param_extras = ["row", "col"]
        if include_secondary_y:
            param_extras.append("secondary_y")
        add_constructor_params(
            buffer, trace_node.child_datatypes, append_extras=param_extras
        )

        # #### Docstring ####
        header = f"Add a new {trace_node.name_datatype_class} trace"

        doc_extras = [
            (
                "row : 'all', int or None (default)",
                "Subplot row index (starting from 1) for the trace to be "
                "added. Only valid if figure was created using "
                "`plotly.tools.make_subplots`."
                "If 'all', addresses all rows in the specified column(s).",
            ),
            (
                "col : 'all', int or None (default)",
                "Subplot col index (starting from 1) for the trace to be "
                "added. Only valid if figure was created using "
                "`plotly.tools.make_subplots`."
                "If 'all', addresses all columns in the specified row(s).",
            ),
        ]

        if include_secondary_y:
            doc_extras.append(
                (
                    "secondary_y: boolean or None (default None)",
                    """\
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.\
""",
                )
            )

        add_docstring(
            buffer,
            trace_node,
            header,
            append_extras=doc_extras,
            return_type=fig_classname,
        )

        # #### Function body ####
        buffer.write(
            f"""
        from plotly.graph_objs import {trace_node.name_datatype_class}
        new_trace = {trace_node.name_datatype_class}(
        """
        )

        for i, subtype_node in enumerate(trace_node.child_datatypes):
            subtype_prop_name = subtype_node.name_property
            buffer.write(
                f"""
                {subtype_prop_name}={subtype_prop_name},"""
            )

        buffer.write(
            f"""
            **kwargs)"""
        )

        if include_secondary_y:
            secondary_y_kwarg = ", secondary_y=secondary_y"
        else:
            secondary_y_kwarg = ""

        buffer.write(
            f"""
        return self.add_trace(
            new_trace, row=row, col=col{secondary_y_kwarg})"""
        )

    # update layout subplots
    # ----------------------
    inflect_eng = inflect.engine()
    for subplot_node in subplot_nodes:
        singular_name = subplot_node.name_property
        plural_name = inflect_eng.plural_noun(singular_name)

        if singular_name == "yaxis":
            secondary_y_1 = ", secondary_y=None"
            secondary_y_2 = ", secondary_y=secondary_y"
            secondary_y_docstring = f"""
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition.

            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes."""
        else:
            secondary_y_1 = ""
            secondary_y_2 = ""
            secondary_y_docstring = ""

        buffer.write(
            f"""

    def select_{plural_name}(
            self, selector=None, row=None, col=None{secondary_y_1}):
        \"\"\"
        Select {singular_name} subplot objects from a particular subplot cell
        and/or {singular_name} subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            {singular_name} objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all {singular_name} objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            {singular_name} and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of {singular_name} objects to select.
            To select {singular_name} objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all {singular_name} objects are selected.\
{secondary_y_docstring}
        Returns
        -------
        generator
            Generator that iterates through all of the {singular_name}
            objects that satisfy all of the specified selection criteria
        \"\"\"

        return self._select_layout_subplots_by_prefix(
            '{singular_name}', selector, row, col{secondary_y_2})

    def for_each_{singular_name}(
            self, fn, selector=None, row=None, col=None{secondary_y_1}):
        \"\"\"
        Apply a function to all {singular_name} objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single {singular_name} object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            {singular_name} objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all {singular_name} objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            {singular_name} and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of {singular_name} objects to select.
            To select {singular_name} objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all {singular_name} objects are selected.\
{secondary_y_docstring}
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        \"\"\"
        for obj in self.select_{plural_name}(
                selector=selector, row=row, col=col{secondary_y_2}):
            fn(obj)

        return self

    def update_{plural_name}(
            self,
            patch=None,
            selector=None,
            overwrite=False,
            row=None, col=None{secondary_y_1},
            **kwargs):
        \"\"\"
        Perform a property update operation on all {singular_name} objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            {singular_name} objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            {singular_name} objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all {singular_name} objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            {singular_name} and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of {singular_name} objects to select.
            To select {singular_name} objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all {singular_name} objects are selected.\
{secondary_y_docstring}
        **kwargs
            Additional property updates to apply to each selected
            {singular_name} object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        \"\"\"
        for obj in self.select_{plural_name}(
                selector=selector, row=row, col=col{secondary_y_2}):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self"""
        )

    # update annotations/shapes/images
    # --------------------------------
    for node in layout_array_nodes:
        singular_name = node.plotly_name
        plural_name = node.name_property

        if singular_name == "image":
            # Rename image to layout_image to avoid conflict with an image trace
            method_prefix = "layout_"
        else:
            method_prefix = ""

        buffer.write(
            f"""
    def select_{method_prefix}{plural_name}(
        self, selector=None, row=None, col=None, secondary_y=None
    ):
        \"\"\"
        Select {plural_name} from a particular subplot cell and/or {plural_name}
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict, function, int, str, or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all {plural_name} are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each {singular_name} and those for which the function returned True
            will be in the selection. If an int N, the Nth {singular_name} matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of {plural_name} to select.
            To select {plural_name} by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            {singular_name} that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all {plural_name} are selected.
        secondary_y: boolean or None (default None)
            * If True, only select {plural_name} associated with the secondary
              y-axis of the subplot.
            * If False, only select {plural_name} associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter {plural_name} based on secondary
              y-axis.

            To select {plural_name} by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the {plural_name} that satisfy
            all of the specified selection criteria
        \"\"\"
        return self._select_annotations_like(
            "{plural_name}", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_{method_prefix}{singular_name}(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        \"\"\"
        Apply a function to all {plural_name} that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single {singular_name} object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all {plural_name} are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each {singular_name} and those for which the function returned True
            will be in the selection. If an int N, the Nth {singular_name} matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of {plural_name} to select.
            To select {plural_name} by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            {plural_name} that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all {plural_name} are selected.
        secondary_y: boolean or None (default None)
            * If True, only select {plural_name} associated with the secondary
              y-axis of the subplot.
            * If False, only select {plural_name} associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter {plural_name} based on secondary
              y-axis.

            To select {plural_name} by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        \"\"\"
        for obj in self._select_annotations_like(
            prop='{plural_name}',
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_{method_prefix}{plural_name}(
        self,
        patch=None,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        \"\"\"
        Perform a property update operation on all {plural_name} that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all {plural_name} that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all {plural_name} are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each {singular_name} and those for which the function returned True
            will be in the selection. If an int N, the Nth {singular_name} matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of {plural_name} to select.
            To select {plural_name} by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            {singular_name} that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all {plural_name} are selected.
        secondary_y: boolean or None (default None)
            * If True, only select {plural_name} associated with the secondary
              y-axis of the subplot.
            * If False, only select {plural_name} associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter {plural_name} based on secondary
              y-axis.

            To select {plural_name} by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected {singular_name}. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the Figure object that the method was called on
        \"\"\"
        for obj in self._select_annotations_like(
            prop='{plural_name}',
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self
"""
        )
        # Add layout array items
        buffer.write(
            f"""
    def add_{method_prefix}{singular_name}(self"""
        )
        add_constructor_params(
            buffer,
            node.child_datatypes,
            prepend_extras=["arg"],
            append_extras=["row", "col", "secondary_y", "exclude_empty_subplots"],
        )

        prepend_extras = [
            (
                "arg",
                f"instance of {node.name_datatype_class} or dict with "
                "compatible properties",
            )
        ]
        append_extras = [
            (
                "row",
                f"Subplot row for {singular_name}. If 'all', addresses all rows in the specified column(s).",
            ),
            (
                "col",
                f"Subplot column for {singular_name}. If 'all', addresses all columns in the specified row(s).",
            ),
            ("secondary_y", f"Whether to add {singular_name} to secondary y-axis"),
            (
                "exclude_empty_subplots",
                f"If True, {singular_name} will not be added to subplots without traces.",
            ),
        ]
        add_docstring(
            buffer,
            node,
            header=f"Create and add a new {singular_name} to the figure's layout",
            prepend_extras=prepend_extras,
            append_extras=append_extras,
            return_type=fig_classname,
        )

        # #### Function body ####
        buffer.write(
            f"""
        from plotly.graph_objs import layout as _layout
        new_obj = _layout.{node.name_datatype_class}(arg,
            """
        )

        for i, subtype_node in enumerate(node.child_datatypes):
            subtype_prop_name = subtype_node.name_property
            buffer.write(
                f"""
                {subtype_prop_name}={subtype_prop_name},"""
            )

        buffer.write("""**kwargs)""")

        buffer.write(
            f"""
        return self._add_annotation_like(
            '{singular_name}',
            '{plural_name}',
            new_obj,
            row=row,
            col=col,
            secondary_y=secondary_y,
            exclude_empty_subplots=exclude_empty_subplots,
        )"""
        )

    # Return source string
    # --------------------
    buffer.write("\n")
    return buffer.getvalue()


def write_figure_classes(
    outdir,
    trace_node,
    data_validator,
    layout_validator,
    frame_validator,
    subplot_nodes,
    layout_array_nodes,
):
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
    subplot_nodes: list of PlotlyNode
        List of names of all of the layout subplot properties
    layout_array_nodes: list of PlotlyNode
        List of array nodes under layout that can be positioned using xref/yref
    Returns
    -------
    None
    """

    # Validate inputs
    # ---------------
    if trace_node.node_path:
        raise ValueError(
            f"Expected root trace node.\n"
            f'Received node with path "{trace_node.path_str}"'
        )

    # Loop over figure types
    # ----------------------
    base_figures = [
        ("basewidget", "BaseFigureWidget", "FigureWidget"),
        ("basedatatypes", "BaseFigure", "Figure"),
    ]

    for base_package, base_classname, fig_classname in base_figures:

        # ### Build figure source code string ###
        figure_source = build_figure_py(
            trace_node,
            base_package,
            base_classname,
            fig_classname,
            data_validator,
            layout_validator,
            frame_validator,
            subplot_nodes,
            layout_array_nodes,
        )

        # ### Format and write to file###
        filepath = opath.join(outdir, "graph_objs", f"_{fig_classname.lower()}.py")
        write_source_py(figure_source, filepath)
