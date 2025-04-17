import _plotly_utils.basevalidators as _bv


class MarkerValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="marker", parent_name="scattermapbox", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Marker"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
