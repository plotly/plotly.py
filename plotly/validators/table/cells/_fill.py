import _plotly_utils.basevalidators as _bv


class FillValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="fill", parent_name="table.cells", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Fill"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
