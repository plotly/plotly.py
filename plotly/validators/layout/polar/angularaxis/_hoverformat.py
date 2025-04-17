import _plotly_utils.basevalidators as _bv


class HoverformatValidator(_bv.StringValidator):
    def __init__(
        self,
        plotly_name="hoverformat",
        parent_name="layout.polar.angularaxis",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
