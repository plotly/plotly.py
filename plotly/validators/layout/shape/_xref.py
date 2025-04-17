import _plotly_utils.basevalidators as _bv


class XrefValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="xref", parent_name="layout.shape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values", ["paper", "/^x([2-9]|[1-9][0-9]+)?( domain)?$/"]
            ),
            **kwargs,
        )
