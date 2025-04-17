import _plotly_utils.basevalidators as _bv


class NewshapeValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="newshape", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Newshape"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
