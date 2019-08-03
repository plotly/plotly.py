import _plotly_utils.basevalidators


class YsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="ysrc", parent_name="waterfall", **kwargs):
        super(YsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YAxisValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(self, plotly_name="yaxis", parent_name="waterfall", **kwargs):
        super(YAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", "y"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class Y0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="y0", parent_name="waterfall", **kwargs):
        super(Y0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="y", parent_name="waterfall", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="xsrc", parent_name="waterfall", **kwargs):
        super(XsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XAxisValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(self, plotly_name="xaxis", parent_name="waterfall", **kwargs):
        super(XAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", "x"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class X0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="x0", parent_name="waterfall", **kwargs):
        super(X0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="x", parent_name="waterfall", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class WidthsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="widthsrc", parent_name="waterfall", **kwargs):
        super(WidthsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="waterfall", **kwargs):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="visible", parent_name="waterfall", **kwargs):
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
    def __init__(self, plotly_name="uirevision", parent_name="waterfall", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UidValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="uid", parent_name="waterfall", **kwargs):
        super(UidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TotalsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="totals", parent_name="waterfall", **kwargs):
        super(TotalsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Totals"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            marker
                plotly.graph_objects.waterfall.totals.Marker
                instance or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="textsrc", parent_name="waterfall", **kwargs):
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
        self, plotly_name="textpositionsrc", parent_name="waterfall", **kwargs
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
    def __init__(self, plotly_name="textposition", parent_name="waterfall", **kwargs):
        super(TextpositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["inside", "outside", "auto", "none"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="textinfo", parent_name="waterfall", **kwargs):
        super(TextinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["label", "text", "initial", "delta", "final"]),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="textfont", parent_name="waterfall", **kwargs):
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


class TextangleValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(self, plotly_name="textangle", parent_name="waterfall", **kwargs):
        super(TextangleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="text", parent_name="waterfall", **kwargs):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StreamValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="stream", parent_name="waterfall", **kwargs):
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
    def __init__(self, plotly_name="showlegend", parent_name="waterfall", **kwargs):
        super(ShowlegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SelectedpointsValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="selectedpoints", parent_name="waterfall", **kwargs):
        super(SelectedpointsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OutsidetextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="outsidetextfont", parent_name="waterfall", **kwargs
    ):
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


class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="orientation", parent_name="waterfall", **kwargs):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["v", "h"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="opacity", parent_name="waterfall", **kwargs):
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


class OffsetsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="offsetsrc", parent_name="waterfall", **kwargs):
        super(OffsetsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OffsetgroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="offsetgroup", parent_name="waterfall", **kwargs):
        super(OffsetgroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OffsetValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="offset", parent_name="waterfall", **kwargs):
        super(OffsetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="waterfall", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="waterfall", **kwargs):
        super(MetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="meta", parent_name="waterfall", **kwargs):
        super(MetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MeasuresrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="measuresrc", parent_name="waterfall", **kwargs):
        super(MeasuresrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MeasureValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="measure", parent_name="waterfall", **kwargs):
        super(MeasureValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LegendgroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="legendgroup", parent_name="waterfall", **kwargs):
        super(LegendgroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class InsidetextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="insidetextfont", parent_name="waterfall", **kwargs):
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


class InsidetextanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="insidetextanchor", parent_name="waterfall", **kwargs
    ):
        super(InsidetextanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["end", "middle", "start"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class IncreasingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="increasing", parent_name="waterfall", **kwargs):
        super(IncreasingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Increasing"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            marker
                plotly.graph_objects.waterfall.increasing.Marke
                r instance or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="idssrc", parent_name="waterfall", **kwargs):
        super(IdssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="ids", parent_name="waterfall", **kwargs):
        super(IdsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="hovertextsrc", parent_name="waterfall", **kwargs):
        super(HovertextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="hovertext", parent_name="waterfall", **kwargs):
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
        self, plotly_name="hovertemplatesrc", parent_name="waterfall", **kwargs
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
    def __init__(self, plotly_name="hovertemplate", parent_name="waterfall", **kwargs):
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
    def __init__(self, plotly_name="hoverlabel", parent_name="waterfall", **kwargs):
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
    def __init__(self, plotly_name="hoverinfosrc", parent_name="waterfall", **kwargs):
        super(HoverinfosrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="hoverinfo", parent_name="waterfall", **kwargs):
        super(HoverinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            extras=kwargs.pop("extras", ["all", "none", "skip"]),
            flags=kwargs.pop(
                "flags", ["name", "x", "y", "text", "initial", "delta", "final"]
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DyValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="dy", parent_name="waterfall", **kwargs):
        super(DyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="dx", parent_name="waterfall", **kwargs):
        super(DxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DecreasingValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="decreasing", parent_name="waterfall", **kwargs):
        super(DecreasingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Decreasing"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            marker
                plotly.graph_objects.waterfall.decreasing.Marke
                r instance or dict with compatible properties
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdatasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="customdatasrc", parent_name="waterfall", **kwargs):
        super(CustomdatasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="customdata", parent_name="waterfall", **kwargs):
        super(CustomdataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ConstraintextValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="constraintext", parent_name="waterfall", **kwargs):
        super(ConstraintextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["inside", "outside", "both", "none"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ConnectorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="connector", parent_name="waterfall", **kwargs):
        super(ConnectorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Connector"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            line
                plotly.graph_objects.waterfall.connector.Line
                instance or dict with compatible properties
            mode
                Sets the shape of connector lines.
            visible
                Determines if connector lines are drawn.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CliponaxisValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="cliponaxis", parent_name="waterfall", **kwargs):
        super(CliponaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BaseValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="base", parent_name="waterfall", **kwargs):
        super(BaseValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AlignmentgroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="alignmentgroup", parent_name="waterfall", **kwargs):
        super(AlignmentgroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
