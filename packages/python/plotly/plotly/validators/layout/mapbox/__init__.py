import _plotly_utils.basevalidators


class ZoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="zoom", parent_name="layout.mapbox", **kwargs):
        super(ZoomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="layout.mapbox", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StyleValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="style", parent_name="layout.mapbox", **kwargs):
        super(StyleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop(
                "values",
                [
                    "basic",
                    "streets",
                    "outdoors",
                    "light",
                    "dark",
                    "satellite",
                    "satellite-streets",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class PitchValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="pitch", parent_name="layout.mapbox", **kwargs):
        super(PitchValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LayerValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="layerdefaults", parent_name="layout.mapbox", **kwargs
    ):
        super(LayerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Layer"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LayersValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="layers", parent_name="layout.mapbox", **kwargs):
        super(LayersValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Layer"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            below
                Determines if the layer will be inserted before
                the layer with the specified ID. If omitted or
                set to '', the layer will be inserted above
                every existing layer.
            circle
                plotly.graph_objects.layout.mapbox.layer.Circle
                instance or dict with compatible properties
            color
                Sets the primary layer color. If `type` is
                "circle", color corresponds to the circle color
                (mapbox.layer.paint.circle-color) If `type` is
                "line", color corresponds to the line color
                (mapbox.layer.paint.line-color) If `type` is
                "fill", color corresponds to the fill color
                (mapbox.layer.paint.fill-color) If `type` is
                "symbol", color corresponds to the icon color
                (mapbox.layer.paint.icon-color)
            fill
                plotly.graph_objects.layout.mapbox.layer.Fill
                instance or dict with compatible properties
            line
                plotly.graph_objects.layout.mapbox.layer.Line
                instance or dict with compatible properties
            maxzoom
                Sets the maximum zoom level
                (mapbox.layer.maxzoom). At zoom levels equal to
                or greater than the maxzoom, the layer will be
                hidden.
            minzoom
                Sets the minimum zoom level
                (mapbox.layer.minzoom). At zoom levels less
                than the minzoom, the layer will be hidden.
            name
                When used in a template, named items are
                created in the output figure in addition to any
                items the figure already has in this array. You
                can modify these items in the output figure by
                making your own item with `templateitemname`
                matching this `name` alongside your
                modifications (including `visible: false` or
                `enabled: false` to hide it). Has no effect
                outside of a template.
            opacity
                Sets the opacity of the layer. If `type` is
                "circle", opacity corresponds to the circle
                opacity (mapbox.layer.paint.circle-opacity) If
                `type` is "line", opacity corresponds to the
                line opacity (mapbox.layer.paint.line-opacity)
                If `type` is "fill", opacity corresponds to the
                fill opacity (mapbox.layer.paint.fill-opacity)
                If `type` is "symbol", opacity corresponds to
                the icon/text opacity (mapbox.layer.paint.text-
                opacity)
            source
                Sets the source data for this layer
                (mapbox.layer.source). Source can be either a
                URL, a geojson object (with `sourcetype` set to
                "geojson") or an array of tile URLS (with
                `sourcetype` set to "vector").
            sourcelayer
                Specifies the layer to use from a vector tile
                source (mapbox.layer.source-layer). Required
                for "vector" source type that supports multiple
                layers.
            sourcetype
                Sets the source type for this layer. Support
                for "raster", "image" and "video" source types
                is coming soon.
            symbol
                plotly.graph_objects.layout.mapbox.layer.Symbol
                instance or dict with compatible properties
            templateitemname
                Used to refer to a named item in this array in
                the template. Named items from the template
                will be created even without a matching item in
                the input figure, but you can modify one by
                making an item with `templateitemname` matching
                its `name`, alongside your modifications
                (including `visible: false` or `enabled: false`
                to hide it). If there is no template or no
                matching item, this item will be hidden unless
                you explicitly show it with `visible: true`.
            type
                Sets the layer type (mapbox.layer.type).
                Support for "raster", "background" types is
                coming soon. Note that "line" and "fill" are
                not compatible with Point GeoJSON geometries.
            visible
                Determines whether this layer is displayed
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.mapbox", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            column
                If there is a layout grid, use the domain for
                this column in the grid for this mapbox subplot
                .
            row
                If there is a layout grid, use the domain for
                this row in the grid for this mapbox subplot .
            x
                Sets the horizontal domain of this mapbox
                subplot (in plot fraction).
            y
                Sets the vertical domain of this mapbox subplot
                (in plot fraction).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CenterValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="center", parent_name="layout.mapbox", **kwargs):
        super(CenterValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Center"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            lat
                Sets the latitude of the center of the map (in
                degrees North).
            lon
                Sets the longitude of the center of the map (in
                degrees East).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BearingValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="bearing", parent_name="layout.mapbox", **kwargs):
        super(BearingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AccesstokenValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="accesstoken", parent_name="layout.mapbox", **kwargs
    ):
        super(AccesstokenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            no_blank=kwargs.pop("no_blank", True),
            role=kwargs.pop("role", "info"),
            strict=kwargs.pop("strict", True),
            **kwargs
        )
