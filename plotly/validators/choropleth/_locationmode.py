#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

import _plotly_utils.basevalidators as _bv


class LocationmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="locationmode", parent_name="choropleth", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values", ["ISO-3", "USA-states", "country names", "geojson-id"]
            ),
            **kwargs,
        )
