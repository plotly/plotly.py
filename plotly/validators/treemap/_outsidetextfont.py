import _plotly_utils.basevalidators as _bv


class OutsidetextfontValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="outsidetextfont", parent_name="treemap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Outsidetextfont"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
