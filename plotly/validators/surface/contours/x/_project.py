import _plotly_utils.basevalidators as _bv


class ProjectValidator(_bv.CompoundValidator):
    def __init__(
        self, plotly_name="project", parent_name="surface.contours.x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Project"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
