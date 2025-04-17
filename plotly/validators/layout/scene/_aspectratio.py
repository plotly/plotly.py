import _plotly_utils.basevalidators as _bv


class AspectratioValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="aspectratio", parent_name="layout.scene", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Aspectratio"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
