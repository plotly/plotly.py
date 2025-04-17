import _plotly_utils.basevalidators as _bv


class IncludesrcValidator(_bv.SrcValidator):
    def __init__(
        self,
        plotly_name="includesrc",
        parent_name="layout.scene.xaxis.autorangeoptions",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
