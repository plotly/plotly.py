import _plotly_utils.basevalidators as _bv


class SpikesnapValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="spikesnap", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            values=kwargs.pop("values", ["data", "cursor", "hovered data"]),
            **kwargs,
        )
