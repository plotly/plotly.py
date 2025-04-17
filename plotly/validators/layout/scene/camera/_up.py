import _plotly_utils.basevalidators as _bv


class UpValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="up", parent_name="layout.scene.camera", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Up"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
