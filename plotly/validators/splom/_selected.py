import _plotly_utils.basevalidators as _bv


class SelectedValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="selected", parent_name="splom", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Selected"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
