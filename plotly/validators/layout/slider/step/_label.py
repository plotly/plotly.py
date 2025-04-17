import _plotly_utils.basevalidators as _bv


class LabelValidator(_bv.StringValidator):
    def __init__(self, plotly_name="label", parent_name="layout.slider.step", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            **kwargs,
        )
