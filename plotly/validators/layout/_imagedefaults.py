import _plotly_utils.basevalidators as _bv


class ImagedefaultsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="imagedefaults", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Image"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
