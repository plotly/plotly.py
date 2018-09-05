import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='y', parent_name='surface.contours', **kwargs
    ):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Y',
            data_docs="""
            color
                Sets the color of the contour lines.
            highlight
                Determines whether or not contour lines about
                the y dimension are highlighted on hover.
            highlightcolor
                Sets the color of the highlighted contour
                lines.
            highlightwidth
                Sets the width of the highlighted contour
                lines.
            project
                plotly.graph_objs.surface.contours.y.Project
                instance or dict with compatible properties
            show
                Determines whether or not contour lines about
                the y dimension are drawn.
            usecolormap
                An alternate to "color". Determines whether or
                not the contour lines are colored using the
                trace "colorscale".
            width
                Sets the width of the contour lines.
""",
            **kwargs
        )
