import _plotly_utils.basevalidators as _bv


class CumulativeValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="cumulative", parent_name="histogram", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Cumulative"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
