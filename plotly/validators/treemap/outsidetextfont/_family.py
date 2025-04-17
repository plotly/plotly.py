import _plotly_utils.basevalidators as _bv


class FamilyValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="family", parent_name="treemap.outsidetextfont", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            no_blank=kwargs.pop("no_blank", True),
            strict=kwargs.pop("strict", True),
            **kwargs,
        )
