import _plotly_utils.basevalidators as _bv


class TypesrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="typesrc", parent_name="scattergeo.marker.gradient", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
