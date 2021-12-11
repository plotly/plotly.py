import _plotly_utils.basevalidators


class LegendValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="legend", parent_name="layout", **kwargs):
        super(LegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Legend"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            bgcolor
                Sets the legend background color. Defaults to
                `layout.paper_bgcolor`.
            bordercolor
                Sets the color of the border enclosing the
                legend.
            borderwidth
                Sets the width (in px) of the border enclosing
                the legend.
            font
                Sets the font used to text the legend items.
            groupclick
                Determines the behavior on legend group item
                click. "toggleitem" toggles the visibility of
                the individual item clicked on the graph.
                "togglegroup" toggles the visibility of all
                items in the same legendgroup as the item
                clicked on the graph.
            grouptitlefont
                Sets the font for group titles in legend.
                Defaults to `legend.font` with its size
                increased about 10%.
            itemclick
                Determines the behavior on legend item click.
                "toggle" toggles the visibility of the item
                clicked on the graph. "toggleothers" makes the
                clicked item the sole visible item on the
                graph. False disables legend item click
                interactions.
            itemdoubleclick
                Determines the behavior on legend item double-
                click. "toggle" toggles the visibility of the
                item clicked on the graph. "toggleothers" makes
                the clicked item the sole visible item on the
                graph. False disables legend item double-click
                interactions.
            itemsizing
                Determines if the legend items symbols scale
                with their corresponding "trace" attributes or
                remain "constant" independent of the symbol
                size on the graph.
            itemwidth
                Sets the width (in px) of the legend item
                symbols (the part other than the title.text).
            orientation
                Sets the orientation of the legend.
            title
                :class:`plotly.graph_objects.layout.legend.Titl
                e` instance or dict with compatible properties
            tracegroupgap
                Sets the amount of vertical space (in px)
                between legend groups.
            traceorder
                Determines the order at which the legend items
                are displayed. If "normal", the items are
                displayed top-to-bottom in the same order as
                the input data. If "reversed", the items are
                displayed in the opposite order as "normal". If
                "grouped", the items are displayed in groups
                (when a trace `legendgroup` is provided). if
                "grouped+reversed", the items are displayed in
                the opposite order as "grouped".
            uirevision
                Controls persistence of legend-driven changes
                in trace and pie label visibility. Defaults to
                `layout.uirevision`.
            valign
                Sets the vertical alignment of the symbols with
                respect to their associated text.
            x
                Sets the x position (in normalized coordinates)
                of the legend. Defaults to 1.02 for vertical
                legends and defaults to 0 for horizontal
                legends.
            xanchor
                Sets the legend's horizontal position anchor.
                This anchor binds the `x` position to the
                "left", "center" or "right" of the legend.
                Value "auto" anchors legends to the right for
                `x` values greater than or equal to 2/3,
                anchors legends to the left for `x` values less
                than or equal to 1/3 and anchors legends with
                respect to their center otherwise.
            y
                Sets the y position (in normalized coordinates)
                of the legend. Defaults to 1 for vertical
                legends, defaults to "-0.1" for horizontal
                legends on graphs w/o range sliders and
                defaults to 1.1 for horizontal legends on graph
                with one or multiple range sliders.
            yanchor
                Sets the legend's vertical position anchor This
                anchor binds the `y` position to the "top",
                "middle" or "bottom" of the legend. Value
                "auto" anchors legends at their bottom for `y`
                values less than or equal to 1/3, anchors
                legends to at their top for `y` values greater
                than or equal to 2/3 and anchors legends with
                respect to their middle otherwise.
""",
            ),
            **kwargs
        )
