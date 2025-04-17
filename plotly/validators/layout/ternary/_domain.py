import _plotly_utils.basevalidators as _bv


class DomainValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.ternary", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
