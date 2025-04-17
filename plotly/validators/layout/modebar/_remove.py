import _plotly_utils.basevalidators as _bv


class RemoveValidator(_bv.StringValidator):
    def __init__(self, plotly_name="remove", parent_name="layout.modebar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "modebar"),
            **kwargs,
        )
