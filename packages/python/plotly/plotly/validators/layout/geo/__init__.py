import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="visible", parent_name="layout.geo", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="layout.geo", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SubunitwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="subunitwidth", parent_name="layout.geo", **kwargs):
        super(SubunitwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SubunitcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="subunitcolor", parent_name="layout.geo", **kwargs):
        super(SubunitcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowsubunitsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showsubunits", parent_name="layout.geo", **kwargs):
        super(ShowsubunitsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowriversValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showrivers", parent_name="layout.geo", **kwargs):
        super(ShowriversValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowoceanValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showocean", parent_name="layout.geo", **kwargs):
        super(ShowoceanValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlandValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showland", parent_name="layout.geo", **kwargs):
        super(ShowlandValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlakesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showlakes", parent_name="layout.geo", **kwargs):
        super(ShowlakesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowframeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showframe", parent_name="layout.geo", **kwargs):
        super(ShowframeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowcountriesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showcountries", parent_name="layout.geo", **kwargs):
        super(ShowcountriesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowcoastlinesValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showcoastlines", parent_name="layout.geo", **kwargs
    ):
        super(ShowcoastlinesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ScopeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="scope", parent_name="layout.geo", **kwargs):
        super(ScopeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "world",
                    "usa",
                    "europe",
                    "asia",
                    "africa",
                    "north america",
                    "south america",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class RiverwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="riverwidth", parent_name="layout.geo", **kwargs):
        super(RiverwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RivercolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="rivercolor", parent_name="layout.geo", **kwargs):
        super(RivercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ResolutionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="resolution", parent_name="layout.geo", **kwargs):
        super(ResolutionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            coerce_number=kwargs.pop("coerce_number", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [110, 50]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ProjectionValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="projection", parent_name="layout.geo", **kwargs):
        super(ProjectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Projection"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            parallels
                For conic projection types only. Sets the
                parallels (tangent, secant) where the cone
                intersects the sphere.
            rotation
                :class:`plotly.graph_objects.layout.geo.project
                ion.Rotation` instance or dict with compatible
                properties
            scale
                Zooms in or out on the map view. A scale of 1
                corresponds to the largest zoom level that fits
                the map's lon and lat ranges.
            type
                Sets the projection type.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class OceancolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="oceancolor", parent_name="layout.geo", **kwargs):
        super(OceancolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LonaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="lonaxis", parent_name="layout.geo", **kwargs):
        super(LonaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lonaxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            dtick
                Sets the graticule's longitude/latitude tick
                step.
            gridcolor
                Sets the graticule's stroke color.
            gridwidth
                Sets the graticule's stroke width (in px).
            range
                Sets the range of this axis (in degrees), sets
                the map's clipped coordinates.
            showgrid
                Sets whether or not graticule are shown on the
                map.
            tick0
                Sets the graticule's starting tick
                longitude/latitude.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LataxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="lataxis", parent_name="layout.geo", **kwargs):
        super(LataxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lataxis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            dtick
                Sets the graticule's longitude/latitude tick
                step.
            gridcolor
                Sets the graticule's stroke color.
            gridwidth
                Sets the graticule's stroke width (in px).
            range
                Sets the range of this axis (in degrees), sets
                the map's clipped coordinates.
            showgrid
                Sets whether or not graticule are shown on the
                map.
            tick0
                Sets the graticule's starting tick
                longitude/latitude.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LandcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="landcolor", parent_name="layout.geo", **kwargs):
        super(LandcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LakecolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="lakecolor", parent_name="layout.geo", **kwargs):
        super(LakecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FramewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="framewidth", parent_name="layout.geo", **kwargs):
        super(FramewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FramecolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="framecolor", parent_name="layout.geo", **kwargs):
        super(FramecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FitboundsValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="fitbounds", parent_name="layout.geo", **kwargs):
        super(FitboundsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [False, "locations", "geojson"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.geo", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            column
                If there is a layout grid, use the domain for
                this column in the grid for this geo subplot .
                Note that geo subplots are constrained by
                domain. In general, when `projection.scale` is
                set to 1. a map will fit either its x or y
                domain, but not both.
            row
                If there is a layout grid, use the domain for
                this row in the grid for this geo subplot .
                Note that geo subplots are constrained by
                domain. In general, when `projection.scale` is
                set to 1. a map will fit either its x or y
                domain, but not both.
            x
                Sets the horizontal domain of this geo subplot
                (in plot fraction). Note that geo subplots are
                constrained by domain. In general, when
                `projection.scale` is set to 1. a map will fit
                either its x or y domain, but not both.
            y
                Sets the vertical domain of this geo subplot
                (in plot fraction). Note that geo subplots are
                constrained by domain. In general, when
                `projection.scale` is set to 1. a map will fit
                either its x or y domain, but not both.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CountrywidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="countrywidth", parent_name="layout.geo", **kwargs):
        super(CountrywidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CountrycolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="countrycolor", parent_name="layout.geo", **kwargs):
        super(CountrycolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CoastlinewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="coastlinewidth", parent_name="layout.geo", **kwargs
    ):
        super(CoastlinewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CoastlinecolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="coastlinecolor", parent_name="layout.geo", **kwargs
    ):
        super(CoastlinecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CenterValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="center", parent_name="layout.geo", **kwargs):
        super(CenterValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Center"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            lat
                Sets the latitude of the map's center. For all
                projection types, the map's latitude center
                lies at the middle of the latitude range by
                default.
            lon
                Sets the longitude of the map's center. By
                default, the map's longitude center lies at the
                middle of the longitude range for scoped
                projection and above `projection.rotation.lon`
                otherwise.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="bgcolor", parent_name="layout.geo", **kwargs):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
