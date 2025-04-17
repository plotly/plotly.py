import _plotly_utils.basevalidators as _bv


class NamelengthValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="namelength", parent_name="densitymap.hoverlabel", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", -1),
            **kwargs,
        )
