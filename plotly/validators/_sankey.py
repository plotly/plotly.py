import _plotly_utils.basevalidators as _bv


class SankeyValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="sankey", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Sankey"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
