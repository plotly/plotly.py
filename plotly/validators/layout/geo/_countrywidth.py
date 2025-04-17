import _plotly_utils.basevalidators as _bv


class CountrywidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="countrywidth", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
