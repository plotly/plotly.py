import _plotly_utils.basevalidators


class TValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="t", parent_name="layout.slider.pad", **kwargs):
        super(TValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="r", parent_name="layout.slider.pad", **kwargs):
        super(RValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="l", parent_name="layout.slider.pad", **kwargs):
        super(LValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="b", parent_name="layout.slider.pad", **kwargs):
        super(BValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
