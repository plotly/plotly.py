import _plotly_utils.basevalidators as _bv


class ItemdoubleclickValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="itemdoubleclick", parent_name="layout.legend", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            values=kwargs.pop("values", ["toggle", "toggleothers", False]),
            **kwargs,
        )
