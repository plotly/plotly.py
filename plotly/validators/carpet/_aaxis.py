import _plotly_utils.basevalidators as _bv


class AaxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="aaxis", parent_name="carpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Aaxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
