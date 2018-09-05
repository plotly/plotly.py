import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='x', parent_name='surface.contours', **kwargs
    ):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='X',
            data_docs="""
            color
                Sets the color of the contour lines.
            highlight
                Determines whether or not contour lines about
                the x dimension are highlighted on hover.
            highlightcolor
                Sets the color of the highlighted contour
                lines.
            highlightwidth
                Sets the width of the highlighted contour
                lines.
            project
                plotly.graph_objs.surface.contours.x.Project
                instance or dict with compatible properties
            show
                Determines whether or not contour lines about
                the x dimension are drawn.
            usecolormap
                An alternate to "color". Determines whether or
                not the contour lines are colored using the
                trace "colorscale".
            width
                Sets the width of the contour lines.
""",
            **kwargs
        )
