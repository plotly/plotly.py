import _plotly_utils.basevalidators as _bv


class TexttemplateValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="texttemplate", parent_name="scattercarpet", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
