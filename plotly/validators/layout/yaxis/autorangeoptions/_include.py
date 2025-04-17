import _plotly_utils.basevalidators as _bv


class IncludeValidator(_bv.AnyValidator):
    def __init__(
        self,
        plotly_name="include",
        parent_name="layout.yaxis.autorangeoptions",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {}),
            **kwargs,
        )
