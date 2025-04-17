import _plotly_utils.basevalidators as _bv


class DthetaValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="dtheta", parent_name="scatterpolar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
