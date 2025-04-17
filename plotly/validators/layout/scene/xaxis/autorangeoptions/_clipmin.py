import _plotly_utils.basevalidators as _bv


class ClipminValidator(_bv.AnyValidator):
    def __init__(
        self,
        plotly_name="clipmin",
        parent_name="layout.scene.xaxis.autorangeoptions",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {}),
            **kwargs,
        )
