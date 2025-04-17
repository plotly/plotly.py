import _plotly_utils.basevalidators as _bv


class ProjectionValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="projection", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Projection"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
