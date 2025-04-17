import _plotly_utils.basevalidators as _bv


class BarnormValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="barnorm", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["", "fraction", "percent"]),
            **kwargs,
        )
