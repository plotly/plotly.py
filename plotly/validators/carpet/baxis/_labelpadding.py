import _plotly_utils.basevalidators as _bv


class LabelpaddingValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="labelpadding", parent_name="carpet.baxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
