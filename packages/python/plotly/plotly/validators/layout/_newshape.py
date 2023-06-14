import _plotly_utils.basevalidators


class NewshapeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="newshape", parent_name="layout", **kwargs):
        super(NewshapeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Newshape"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            drawdirection
                When `dragmode` is set to "drawrect",
                "drawline" or "drawcircle" this limits the drag
                to be horizontal, vertical or diagonal. Using
                "diagonal" there is no limit e.g. in drawing
                lines in any direction. "ortho" limits the draw
                to be either horizontal or vertical.
                "horizontal" allows horizontal extend.
                "vertical" allows vertical extend.
            fillcolor
                Sets the color filling new shapes' interior.
                Please note that if using a fillcolor with
                alpha greater than half, drag inside the active
                shape starts moving the shape underneath,
                otherwise a new shape could be started over.
            fillrule
                Determines the path's interior. For more info
                please visit https://developer.mozilla.org/en-
                US/docs/Web/SVG/Attribute/fill-rule
            label
                :class:`plotly.graph_objects.layout.newshape.La
                bel` instance or dict with compatible
                properties
            layer
                Specifies whether new shapes are drawn below or
                above traces.
            line
                :class:`plotly.graph_objects.layout.newshape.Li
                ne` instance or dict with compatible properties
            opacity
                Sets the opacity of new shapes.
""",
            ),
            **kwargs,
        )
