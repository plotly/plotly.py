import _plotly_utils.basevalidators as _bv


class SlicesValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="slices", parent_name="isosurface", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Slices"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
