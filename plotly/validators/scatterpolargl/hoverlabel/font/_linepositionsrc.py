import _plotly_utils.basevalidators as _bv


class LinepositionsrcValidator(_bv.SrcValidator):
    def __init__(
        self,
        plotly_name="linepositionsrc",
        parent_name="scatterpolargl.hoverlabel.font",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
