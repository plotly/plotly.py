import _plotly_utils.basevalidators as _bv


class VertexnormalsepsilonValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="vertexnormalsepsilon", parent_name="cone.lighting", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
