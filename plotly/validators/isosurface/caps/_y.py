import _plotly_utils.basevalidators as _bv


class YValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="y", parent_name="isosurface.caps", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Y"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
