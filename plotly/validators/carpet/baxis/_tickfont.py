import _plotly_utils.basevalidators as _bv


class TickfontValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="tickfont", parent_name="carpet.baxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickfont"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
