import _plotly_utils.basevalidators as _bv


class Copy_ZstyleValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="copy_zstyle", parent_name="scatter3d.error_x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
