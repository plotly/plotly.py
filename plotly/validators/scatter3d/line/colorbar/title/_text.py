import _plotly_utils.basevalidators as _bv


class TextValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="text", parent_name="scatter3d.line.colorbar.title", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
