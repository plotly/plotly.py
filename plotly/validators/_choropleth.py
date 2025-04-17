import _plotly_utils.basevalidators as _bv


class ChoroplethValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="choropleth", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Choropleth"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
