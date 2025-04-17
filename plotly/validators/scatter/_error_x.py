import _plotly_utils.basevalidators as _bv


class Error_XValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="error_x", parent_name="scatter", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorX"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
