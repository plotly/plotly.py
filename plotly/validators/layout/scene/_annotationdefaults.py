import _plotly_utils.basevalidators as _bv


class AnnotationdefaultsValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="annotationdefaults", parent_name="layout.scene", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Annotation"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
