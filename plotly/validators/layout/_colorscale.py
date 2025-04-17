import _plotly_utils.basevalidators as _bv


class ColorscaleValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="colorscale", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Colorscale"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
