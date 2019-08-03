import _plotly_utils.basevalidators


class ZsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="zsrc", parent_name="scatter3d", **kwargs):
        super(ZsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZcalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="zcalendar", parent_name="scatter3d", **kwargs):
        super(ZcalendarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "gregorian",
                    "chinese",
                    "coptic",
                    "discworld",
                    "ethiopian",
                    "hebrew",
                    "islamic",
                    "julian",
                    "mayan",
                    "nanakshahi",
                    "nepali",
                    "persian",
                    "jalali",
                    "taiwan",
                    "thai",
                    "ummalqura",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="z", parent_name="scatter3d", **kwargs):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="ysrc", parent_name="scatter3d", **kwargs):
        super(YsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YcalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="ycalendar", parent_name="scatter3d", **kwargs):
        super(YcalendarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "gregorian",
                    "chinese",
                    "coptic",
                    "discworld",
                    "ethiopian",
                    "hebrew",
                    "islamic",
                    "julian",
                    "mayan",
                    "nanakshahi",
                    "nepali",
                    "persian",
                    "jalali",
                    "taiwan",
                    "thai",
                    "ummalqura",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="y", parent_name="scatter3d", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="xsrc", parent_name="scatter3d", **kwargs):
        super(XsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XcalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xcalendar", parent_name="scatter3d", **kwargs):
        super(XcalendarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "gregorian",
                    "chinese",
                    "coptic",
                    "discworld",
                    "ethiopian",
                    "hebrew",
                    "islamic",
                    "julian",
                    "mayan",
                    "nanakshahi",
                    "nepali",
                    "persian",
                    "jalali",
                    "taiwan",
                    "thai",
                    "ummalqura",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="x", parent_name="scatter3d", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="visible", parent_name="scatter3d", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [True, False, "legendonly"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="scatter3d", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UidValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="uid", parent_name="scatter3d", **kwargs):
        super(UidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="textsrc", parent_name="scatter3d", **kwargs):
        super(TextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextpositionsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="textpositionsrc", parent_name="scatter3d", **kwargs
    ):
        super(TextpositionsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextpositionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="textposition", parent_name="scatter3d", **kwargs):
        super(TextpositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop(
                "values",
                [
                    "top left",
                    "top center",
                    "top right",
                    "middle left",
                    "middle center",
                    "middle right",
                    "bottom left",
                    "bottom center",
                    "bottom right",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="textfont", parent_name="scatter3d", **kwargs):
        super(TextfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Textfont"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            colorsrc
                Sets the source reference on plot.ly for  color
                .
            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The plotly service (at https://plot.ly
                or on-premise) generates images on a server,
                where only a select number of fonts are
                installed and supported. These include "Arial",
                "Balto", "Courier New", "Droid Sans",, "Droid
                Serif", "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

            sizesrc
                Sets the source reference on plot.ly for  size
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="text", parent_name="scatter3d", **kwargs):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SurfacecolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="surfacecolor", parent_name="scatter3d", **kwargs):
        super(SurfacecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SurfaceaxisValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="surfaceaxis", parent_name="scatter3d", **kwargs):
        super(SurfaceaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [-1, 0, 1, 2]),
            **kwargs
        )


import _plotly_utils.basevalidators


class StreamValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="stream", parent_name="scatter3d", **kwargs):
        super(StreamValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Stream"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            maxpoints
                Sets the maximum number of points to keep on
                the plots from an incoming stream. If
                `maxpoints` is set to 50, only the newest 50
                points will be displayed on the plot.
            token
                The stream id number links a data trace on a
                plot with a stream. See
                https://plot.ly/settings for more details.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlegendValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showlegend", parent_name="scatter3d", **kwargs):
        super(ShowlegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SceneValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(self, plotly_name="scene", parent_name="scatter3d", **kwargs):
        super(SceneValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", "scene"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ProjectionValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="projection", parent_name="scatter3d", **kwargs):
        super(ProjectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Projection"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            x
                plotly.graph_objects.scatter3d.projection.X
                instance or dict with compatible properties
            y
                plotly.graph_objects.scatter3d.projection.Y
                instance or dict with compatible properties
            z
                plotly.graph_objects.scatter3d.projection.Z
                instance or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="opacity", parent_name="scatter3d", **kwargs):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="scatter3d", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ModeValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="mode", parent_name="scatter3d", **kwargs):
        super(ModeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["lines", "markers", "text"]),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="scatter3d", **kwargs):
        super(MetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="meta", parent_name="scatter3d", **kwargs):
        super(MetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="marker", parent_name="scatter3d", **kwargs):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Marker"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `marker.colorscale`. Has an
                effect only if in `marker.color`is set to a
                numerical array. In case `colorscale` is
                unspecified or `autocolorscale` is true, the
                default  palette will be chosen according to
                whether numbers in the `color` array are all
                positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `marker.color`) or the bounds set in
                `marker.cmin` and `marker.cmax`  Has an effect
                only if in `marker.color`is set to a numerical
                array. Defaults to `false` when `marker.cmin`
                and `marker.cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Has
                an effect only if in `marker.color`is set to a
                numerical array. Value should have the same
                units as in `marker.color` and if set,
                `marker.cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `marker.cmin` and/or `marker.cmax` to
                be equidistant to this point. Has an effect
                only if in `marker.color`is set to a numerical
                array. Value should have the same units as in
                `marker.color`. Has no effect when
                `marker.cauto` is `false`.
            cmin
                Sets the lower bound of the color domain. Has
                an effect only if in `marker.color`is set to a
                numerical array. Value should have the same
                units as in `marker.color` and if set,
                `marker.cmax` must be set as well.
            color
                Sets themarkercolor. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `marker.cmin` and `marker.cmax` if set.
            coloraxis
                Sets a reference to a shared color axis.
                References to these shared color axes are
                "coloraxis", "coloraxis2", "coloraxis3", etc.
                Settings for these shared color axes are set in
                the layout, under `layout.coloraxis`,
                `layout.coloraxis2`, etc. Note that multiple
                color scales can be linked to the same color
                axis.
            colorbar
                plotly.graph_objects.scatter3d.marker.ColorBar
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. Has an effect only if in
                `marker.color`is set to a numerical array. The
                colorscale must be an array containing arrays
                mapping a normalized value to an rgb, rgba,
                hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                To control the bounds of the colorscale in
                color space, use`marker.cmin` and
                `marker.cmax`. Alternatively, `colorscale` may
                be a palette name string of the following list:
                Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Bl
                ues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,E
                arth,Electric,Viridis,Cividis.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            line
                plotly.graph_objects.scatter3d.marker.Line
                instance or dict with compatible properties
            opacity
                Sets the marker opacity. Note that the marker
                opacity for scatter3d traces must be a scalar
                value for performance reasons. To set a
                blending opacity value (i.e. which is not
                transparent), set "marker.color" to an rgba
                color and use its alpha channel.
            reversescale
                Reverses the color mapping if true. Has an
                effect only if in `marker.color`is set to a
                numerical array. If true, `marker.cmin` will
                correspond to the last color in the array and
                `marker.cmax` will correspond to the first
                color.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace. Has an effect only if
                in `marker.color`is set to a numerical array.
            size
                Sets the marker size (in px).
            sizemin
                Has an effect only if `marker.size` is set to a
                numerical array. Sets the minimum size (in px)
                of the rendered marker points.
            sizemode
                Has an effect only if `marker.size` is set to a
                numerical array. Sets the rule for which the
                data in `size` is converted to pixels.
            sizeref
                Has an effect only if `marker.size` is set to a
                numerical array. Sets the scale factor used to
                determine the rendered size of marker points.
                Use with `sizemin` and `sizemode`.
            sizesrc
                Sets the source reference on plot.ly for  size
                .
            symbol
                Sets the marker symbol type.
            symbolsrc
                Sets the source reference on plot.ly for
                symbol .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="scatter3d", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            autocolorscale
                Determines whether the colorscale is a default
                palette (`autocolorscale: true`) or the palette
                determined by `line.colorscale`. Has an effect
                only if in `line.color`is set to a numerical
                array. In case `colorscale` is unspecified or
                `autocolorscale` is true, the default  palette
                will be chosen according to whether numbers in
                the `color` array are all positive, all
                negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `line.color`) or the bounds set in
                `line.cmin` and `line.cmax`  Has an effect only
                if in `line.color`is set to a numerical array.
                Defaults to `false` when `line.cmin` and
                `line.cmax` are set by the user.
            cmax
                Sets the upper bound of the color domain. Has
                an effect only if in `line.color`is set to a
                numerical array. Value should have the same
                units as in `line.color` and if set,
                `line.cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `line.cmin` and/or `line.cmax` to be
                equidistant to this point. Has an effect only
                if in `line.color`is set to a numerical array.
                Value should have the same units as in
                `line.color`. Has no effect when `line.cauto`
                is `false`.
            cmin
                Sets the lower bound of the color domain. Has
                an effect only if in `line.color`is set to a
                numerical array. Value should have the same
                units as in `line.color` and if set,
                `line.cmax` must be set as well.
            color
                Sets thelinecolor. It accepts either a specific
                color or an array of numbers that are mapped to
                the colorscale relative to the max and min
                values of the array or relative to `line.cmin`
                and `line.cmax` if set.
            coloraxis
                Sets a reference to a shared color axis.
                References to these shared color axes are
                "coloraxis", "coloraxis2", "coloraxis3", etc.
                Settings for these shared color axes are set in
                the layout, under `layout.coloraxis`,
                `layout.coloraxis2`, etc. Note that multiple
                color scales can be linked to the same color
                axis.
            colorbar
                plotly.graph_objects.scatter3d.line.ColorBar
                instance or dict with compatible properties
            colorscale
                Sets the colorscale. Has an effect only if in
                `line.color`is set to a numerical array. The
                colorscale must be an array containing arrays
                mapping a normalized value to an rgb, rgba,
                hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                To control the bounds of the colorscale in
                color space, use`line.cmin` and `line.cmax`.
                Alternatively, `colorscale` may be a palette
                name string of the following list: Greys,YlGnBu
                ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,R
                ainbow,Portland,Jet,Hot,Blackbody,Earth,Electri
                c,Viridis,Cividis.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            dash
                Sets the dash style of the lines.
            reversescale
                Reverses the color mapping if true. Has an
                effect only if in `line.color`is set to a
                numerical array. If true, `line.cmin` will
                correspond to the last color in the array and
                `line.cmax` will correspond to the first color.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace. Has an effect only if
                in `line.color`is set to a numerical array.
            width
                Sets the line width (in px).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LegendgroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="legendgroup", parent_name="scatter3d", **kwargs):
        super(LegendgroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="idssrc", parent_name="scatter3d", **kwargs):
        super(IdssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="ids", parent_name="scatter3d", **kwargs):
        super(IdsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="hovertextsrc", parent_name="scatter3d", **kwargs):
        super(HovertextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="hovertext", parent_name="scatter3d", **kwargs):
        super(HovertextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertemplatesrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="hovertemplatesrc", parent_name="scatter3d", **kwargs
    ):
        super(HovertemplatesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertemplateValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="hovertemplate", parent_name="scatter3d", **kwargs):
        super(HovertemplateValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="hoverlabel", parent_name="scatter3d", **kwargs):
        super(HoverlabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Hoverlabel"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            align
                Sets the horizontal alignment of the text
                content within hover label box. Has an effect
                only if the hover label text spans more two or
                more lines
            alignsrc
                Sets the source reference on plot.ly for  align
                .
            bgcolor
                Sets the background color of the hover labels
                for this trace
            bgcolorsrc
                Sets the source reference on plot.ly for
                bgcolor .
            bordercolor
                Sets the border color of the hover labels for
                this trace.
            bordercolorsrc
                Sets the source reference on plot.ly for
                bordercolor .
            font
                Sets the font used in hover labels.
            namelength
                Sets the default length (in number of
                characters) of the trace name in the hover
                labels for all traces. -1 shows the whole name
                regardless of length. 0-3 shows the first 0-3
                characters, and an integer >3 will show the
                whole name if it is less than that many
                characters, but if it is longer, will truncate
                to `namelength - 3` characters and add an
                ellipsis.
            namelengthsrc
                Sets the source reference on plot.ly for
                namelength .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverinfosrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="hoverinfosrc", parent_name="scatter3d", **kwargs):
        super(HoverinfosrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="hoverinfo", parent_name="scatter3d", **kwargs):
        super(HoverinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["all", "none", "skip"]),
            flags=kwargs.pop("flags", ["x", "y", "z", "text", "name"]),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ErrorZValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="error_z", parent_name="scatter3d", **kwargs):
        super(ErrorZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorZ"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            array
                Sets the data corresponding the length of each
                error bar. Values are plotted relative to the
                underlying data.
            arrayminus
                Sets the data corresponding the length of each
                error bar in the bottom (left) direction for
                vertical (horizontal) bars Values are plotted
                relative to the underlying data.
            arrayminussrc
                Sets the source reference on plot.ly for
                arrayminus .
            arraysrc
                Sets the source reference on plot.ly for  array
                .
            color
                Sets the stoke color of the error bars.
            symmetric
                Determines whether or not the error bars have
                the same length in both direction (top/bottom
                for vertical bars, left/right for horizontal
                bars.
            thickness
                Sets the thickness (in px) of the error bars.
            traceref

            tracerefminus

            type
                Determines the rule used to generate the error
                bars. If *constant`, the bar lengths are of a
                constant value. Set this constant in `value`.
                If "percent", the bar lengths correspond to a
                percentage of underlying data. Set this
                percentage in `value`. If "sqrt", the bar
                lengths correspond to the sqaure of the
                underlying data. If "data", the bar lengths are
                set with data set `array`.
            value
                Sets the value of either the percentage (if
                `type` is set to "percent") or the constant (if
                `type` is set to "constant") corresponding to
                the lengths of the error bars.
            valueminus
                Sets the value of either the percentage (if
                `type` is set to "percent") or the constant (if
                `type` is set to "constant") corresponding to
                the lengths of the error bars in the bottom
                (left) direction for vertical (horizontal) bars
            visible
                Determines whether or not this set of error
                bars is visible.
            width
                Sets the width (in px) of the cross-bar at both
                ends of the error bars.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ErrorYValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="error_y", parent_name="scatter3d", **kwargs):
        super(ErrorYValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorY"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            array
                Sets the data corresponding the length of each
                error bar. Values are plotted relative to the
                underlying data.
            arrayminus
                Sets the data corresponding the length of each
                error bar in the bottom (left) direction for
                vertical (horizontal) bars Values are plotted
                relative to the underlying data.
            arrayminussrc
                Sets the source reference on plot.ly for
                arrayminus .
            arraysrc
                Sets the source reference on plot.ly for  array
                .
            color
                Sets the stoke color of the error bars.
            copy_zstyle

            symmetric
                Determines whether or not the error bars have
                the same length in both direction (top/bottom
                for vertical bars, left/right for horizontal
                bars.
            thickness
                Sets the thickness (in px) of the error bars.
            traceref

            tracerefminus

            type
                Determines the rule used to generate the error
                bars. If *constant`, the bar lengths are of a
                constant value. Set this constant in `value`.
                If "percent", the bar lengths correspond to a
                percentage of underlying data. Set this
                percentage in `value`. If "sqrt", the bar
                lengths correspond to the sqaure of the
                underlying data. If "data", the bar lengths are
                set with data set `array`.
            value
                Sets the value of either the percentage (if
                `type` is set to "percent") or the constant (if
                `type` is set to "constant") corresponding to
                the lengths of the error bars.
            valueminus
                Sets the value of either the percentage (if
                `type` is set to "percent") or the constant (if
                `type` is set to "constant") corresponding to
                the lengths of the error bars in the bottom
                (left) direction for vertical (horizontal) bars
            visible
                Determines whether or not this set of error
                bars is visible.
            width
                Sets the width (in px) of the cross-bar at both
                ends of the error bars.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ErrorXValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="error_x", parent_name="scatter3d", **kwargs):
        super(ErrorXValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ErrorX"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            array
                Sets the data corresponding the length of each
                error bar. Values are plotted relative to the
                underlying data.
            arrayminus
                Sets the data corresponding the length of each
                error bar in the bottom (left) direction for
                vertical (horizontal) bars Values are plotted
                relative to the underlying data.
            arrayminussrc
                Sets the source reference on plot.ly for
                arrayminus .
            arraysrc
                Sets the source reference on plot.ly for  array
                .
            color
                Sets the stoke color of the error bars.
            copy_zstyle

            symmetric
                Determines whether or not the error bars have
                the same length in both direction (top/bottom
                for vertical bars, left/right for horizontal
                bars.
            thickness
                Sets the thickness (in px) of the error bars.
            traceref

            tracerefminus

            type
                Determines the rule used to generate the error
                bars. If *constant`, the bar lengths are of a
                constant value. Set this constant in `value`.
                If "percent", the bar lengths correspond to a
                percentage of underlying data. Set this
                percentage in `value`. If "sqrt", the bar
                lengths correspond to the sqaure of the
                underlying data. If "data", the bar lengths are
                set with data set `array`.
            value
                Sets the value of either the percentage (if
                `type` is set to "percent") or the constant (if
                `type` is set to "constant") corresponding to
                the lengths of the error bars.
            valueminus
                Sets the value of either the percentage (if
                `type` is set to "percent") or the constant (if
                `type` is set to "constant") corresponding to
                the lengths of the error bars in the bottom
                (left) direction for vertical (horizontal) bars
            visible
                Determines whether or not this set of error
                bars is visible.
            width
                Sets the width (in px) of the cross-bar at both
                ends of the error bars.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdatasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="customdatasrc", parent_name="scatter3d", **kwargs):
        super(CustomdatasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="customdata", parent_name="scatter3d", **kwargs):
        super(CustomdataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ConnectgapsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="connectgaps", parent_name="scatter3d", **kwargs):
        super(ConnectgapsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
