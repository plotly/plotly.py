import _plotly_utils.basevalidators as _bv


class InsidetextfontValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="insidetextfont", parent_name="histogram", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Insidetextfont"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
