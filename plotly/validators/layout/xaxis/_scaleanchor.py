import _plotly_utils.basevalidators as _bv


class ScaleanchorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="scaleanchor", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop(
                "values",
                [
                    "/^x([2-9]|[1-9][0-9]+)?( domain)?$/",
                    "/^y([2-9]|[1-9][0-9]+)?( domain)?$/",
                    False,
                ],
            ),
            **kwargs,
        )
