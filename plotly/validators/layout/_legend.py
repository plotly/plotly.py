import _plotly_utils.basevalidators


class LegendValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='legend', parent_name='layout', **kwargs):
        super(LegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Legend',
            data_docs="""
            bgcolor
                Sets the legend background color.
            bordercolor
                Sets the color of the border enclosing the
                legend.
            borderwidth
                Sets the width (in px) of the border enclosing
                the legend.
            font
                Sets the font used to text the legend items.
            orientation
                Sets the orientation of the legend.
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
            x
                Sets the x position (in normalized coordinates)
                of the legend.
            xanchor
                Sets the legend's horizontal position anchor.
                This anchor binds the `x` position to the
                "left", "center" or "right" of the legend.
            y
                Sets the y position (in normalized coordinates)
                of the legend.
            yanchor
                Sets the legend's vertical position anchor This
                anchor binds the `y` position to the "top",
                "middle" or "bottom" of the legend.
""",
            **kwargs
        )
