import _plotly_utils.basevalidators as _bv


class GeoValidator(_bv.SubplotidValidator):
    def __init__(self, plotly_name="geo", parent_name="choropleth", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            dflt=kwargs.pop("dflt", "geo"),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
