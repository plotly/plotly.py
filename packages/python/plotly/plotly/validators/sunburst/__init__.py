import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="visible", parent_name="sunburst", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [True, False, "legendonly"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValuessrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="valuessrc", parent_name="sunburst", **kwargs):
        super(ValuessrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValuesValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="values", parent_name="sunburst", **kwargs):
        super(ValuesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="sunburst", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UidValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="uid", parent_name="sunburst", **kwargs):
        super(UidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TexttemplatesrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="texttemplatesrc", parent_name="sunburst", **kwargs):
        super(TexttemplatesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TexttemplateValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="texttemplate", parent_name="sunburst", **kwargs):
        super(TexttemplateValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="textsrc", parent_name="sunburst", **kwargs):
        super(TextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="textinfo", parent_name="sunburst", **kwargs):
        super(TextinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop(
                "flags",
                [
                    "label",
                    "text",
                    "value",
                    "current path",
                    "percent root",
                    "percent entry",
                    "percent parent",
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="textfont", parent_name="sunburst", **kwargs):
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
            familysrc
                Sets the source reference on plot.ly for
                family .
            size

            sizesrc
                Sets the source reference on plot.ly for  size
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="text", parent_name="sunburst", **kwargs):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StreamValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="stream", parent_name="sunburst", **kwargs):
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


class ParentssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="parentssrc", parent_name="sunburst", **kwargs):
        super(ParentssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ParentsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="parents", parent_name="sunburst", **kwargs):
        super(ParentsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OutsidetextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="outsidetextfont", parent_name="sunburst", **kwargs):
        super(OutsidetextfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Outsidetextfont"),
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
            familysrc
                Sets the source reference on plot.ly for
                family .
            size

            sizesrc
                Sets the source reference on plot.ly for  size
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="opacity", parent_name="sunburst", **kwargs):
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
    def __init__(self, plotly_name="name", parent_name="sunburst", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="sunburst", **kwargs):
        super(MetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="meta", parent_name="sunburst", **kwargs):
        super(MetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MaxdepthValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="maxdepth", parent_name="sunburst", **kwargs):
        super(MaxdepthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="marker", parent_name="sunburst", **kwargs):
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
                effect only if colorsis set to a numerical
                array. In case `colorscale` is unspecified or
                `autocolorscale` is true, the default  palette
                will be chosen according to whether numbers in
                the `color` array are all positive, all
                negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                colors) or the bounds set in `marker.cmin` and
                `marker.cmax`  Has an effect only if colorsis
                set to a numerical array. Defaults to `false`
                when `marker.cmin` and `marker.cmax` are set by
                the user.
            cmax
                Sets the upper bound of the color domain. Has
                an effect only if colorsis set to a numerical
                array. Value should have the same units as
                colors and if set, `marker.cmin` must be set as
                well.
            cmid
                Sets the mid-point of the color domain by
                scaling `marker.cmin` and/or `marker.cmax` to
                be equidistant to this point. Has an effect
                only if colorsis set to a numerical array.
                Value should have the same units as colors. Has
                no effect when `marker.cauto` is `false`.
            cmin
                Sets the lower bound of the color domain. Has
                an effect only if colorsis set to a numerical
                array. Value should have the same units as
                colors and if set, `marker.cmax` must be set as
                well.
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
                plotly.graph_objects.sunburst.marker.ColorBar
                instance or dict with compatible properties
            colors
                Sets the color of each sector of this trace. If
                not specified, the default trace color set is
                used to pick the sector colors.
            colorscale
                Sets the colorscale. Has an effect only if
                colorsis set to a numerical array. The
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
            colorssrc
                Sets the source reference on plot.ly for
                colors .
            line
                plotly.graph_objects.sunburst.marker.Line
                instance or dict with compatible properties
            reversescale
                Reverses the color mapping if true. Has an
                effect only if colorsis set to a numerical
                array. If true, `marker.cmin` will correspond
                to the last color in the array and
                `marker.cmax` will correspond to the first
                color.
            showscale
                Determines whether or not a colorbar is
                displayed for this trace. Has an effect only if
                colorsis set to a numerical array.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LevelValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="level", parent_name="sunburst", **kwargs):
        super(LevelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LeafValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="leaf", parent_name="sunburst", **kwargs):
        super(LeafValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Leaf"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            opacity
                Sets the opacity of the leaves. With colorscale
                it is defaulted to 1; otherwise it is defaulted
                to 0.7
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LabelssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="labelssrc", parent_name="sunburst", **kwargs):
        super(LabelssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LabelsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="labels", parent_name="sunburst", **kwargs):
        super(LabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class InsidetextorientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="insidetextorientation", parent_name="sunburst", **kwargs
    ):
        super(InsidetextorientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["horizontal", "radial", "tangential", "auto"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class InsidetextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="insidetextfont", parent_name="sunburst", **kwargs):
        super(InsidetextfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Insidetextfont"),
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
            familysrc
                Sets the source reference on plot.ly for
                family .
            size

            sizesrc
                Sets the source reference on plot.ly for  size
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="idssrc", parent_name="sunburst", **kwargs):
        super(IdssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="ids", parent_name="sunburst", **kwargs):
        super(IdsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="hovertextsrc", parent_name="sunburst", **kwargs):
        super(HovertextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="hovertext", parent_name="sunburst", **kwargs):
        super(HovertextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertemplatesrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="hovertemplatesrc", parent_name="sunburst", **kwargs
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
    def __init__(self, plotly_name="hovertemplate", parent_name="sunburst", **kwargs):
        super(HovertemplateValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="hoverlabel", parent_name="sunburst", **kwargs):
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
    def __init__(self, plotly_name="hoverinfosrc", parent_name="sunburst", **kwargs):
        super(HoverinfosrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="hoverinfo", parent_name="sunburst", **kwargs):
        super(HoverinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            extras=kwargs.pop("extras", ["all", "none", "skip"]),
            flags=kwargs.pop(
                "flags",
                [
                    "label",
                    "text",
                    "value",
                    "name",
                    "current path",
                    "percent root",
                    "percent entry",
                    "percent parent",
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="sunburst", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            column
                If there is a layout grid, use the domain for
                this column in the grid for this sunburst trace
                .
            row
                If there is a layout grid, use the domain for
                this row in the grid for this sunburst trace .
            x
                Sets the horizontal domain of this sunburst
                trace (in plot fraction).
            y
                Sets the vertical domain of this sunburst trace
                (in plot fraction).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdatasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="customdatasrc", parent_name="sunburst", **kwargs):
        super(CustomdatasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="customdata", parent_name="sunburst", **kwargs):
        super(CustomdataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CountValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="count", parent_name="sunburst", **kwargs):
        super(CountValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            flags=kwargs.pop("flags", ["branches", "leaves"]),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BranchvaluesValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="branchvalues", parent_name="sunburst", **kwargs):
        super(BranchvaluesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["remainder", "total"]),
            **kwargs
        )
