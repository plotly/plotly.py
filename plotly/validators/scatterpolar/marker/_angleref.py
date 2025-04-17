import _plotly_utils.basevalidators as _bv


class AnglerefValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="angleref", parent_name="scatterpolar.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["previous", "up"]),
            **kwargs,
        )
