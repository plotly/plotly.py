import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="z", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YshiftValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="yshift", parent_name="layout.scene.annotation", **kwargs
    ):
        super(YshiftValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="yanchor", parent_name="layout.scene.annotation", **kwargs
    ):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="y", parent_name="layout.scene.annotation", **kwargs
    ):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XshiftValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="xshift", parent_name="layout.scene.annotation", **kwargs
    ):
        super(XshiftValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="xanchor", parent_name="layout.scene.annotation", **kwargs
    ):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "left", "center", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="x", parent_name="layout.scene.annotation", **kwargs
    ):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="width", parent_name="layout.scene.annotation", **kwargs
    ):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="layout.scene.annotation", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValignValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="valign", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ValignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextangleValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(
        self, plotly_name="textangle", parent_name="layout.scene.annotation", **kwargs
    ):
        super(TextangleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="text", parent_name="layout.scene.annotation", **kwargs
    ):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self,
        plotly_name="templateitemname",
        parent_name="layout.scene.annotation",
        **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StartstandoffValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self,
        plotly_name="startstandoff",
        parent_name="layout.scene.annotation",
        **kwargs
    ):
        super(StartstandoffValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StartarrowsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self,
        plotly_name="startarrowsize",
        parent_name="layout.scene.annotation",
        **kwargs
    ):
        super(StartarrowsizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0.3),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StartarrowheadValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self,
        plotly_name="startarrowhead",
        parent_name="layout.scene.annotation",
        **kwargs
    ):
        super(StartarrowheadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 8),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StandoffValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="standoff", parent_name="layout.scene.annotation", **kwargs
    ):
        super(StandoffValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowarrowValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showarrow", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ShowarrowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="opacity", parent_name="layout.scene.annotation", **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="name", parent_name="layout.scene.annotation", **kwargs
    ):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="hovertext", parent_name="layout.scene.annotation", **kwargs
    ):
        super(HovertextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="hoverlabel", parent_name="layout.scene.annotation", **kwargs
    ):
        super(HoverlabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Hoverlabel"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            bgcolor
                Sets the background color of the hover label.
                By default uses the annotation's `bgcolor` made
                opaque, or white if it was transparent.
            bordercolor
                Sets the border color of the hover label. By
                default uses either dark grey or white, for
                maximum contrast with `hoverlabel.bgcolor`.
            font
                Sets the hover label text font. By default uses
                the global hover font and size, with color from
                `hoverlabel.bordercolor`.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HeightValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="height", parent_name="layout.scene.annotation", **kwargs
    ):
        super(HeightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="font", parent_name="layout.scene.annotation", **kwargs
    ):
        super(FontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Font"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The Chart Studio Cloud (at
                https://chart-studio.plotly.com or on-premise)
                generates images on a server, where only a
                select number of fonts are installed and
                supported. These include "Arial", "Balto",
                "Courier New", "Droid Sans",, "Droid Serif",
                "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CaptureeventsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="captureevents",
        parent_name="layout.scene.annotation",
        **kwargs
    ):
        super(CaptureeventsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BorderwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="borderwidth", parent_name="layout.scene.annotation", **kwargs
    ):
        super(BorderwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BorderpadValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="borderpad", parent_name="layout.scene.annotation", **kwargs
    ):
        super(BorderpadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="bordercolor", parent_name="layout.scene.annotation", **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="bgcolor", parent_name="layout.scene.annotation", **kwargs
    ):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AyValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="ay", parent_name="layout.scene.annotation", **kwargs
    ):
        super(AyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="ax", parent_name="layout.scene.annotation", **kwargs
    ):
        super(AxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrowwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="arrowwidth", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ArrowwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0.1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrowsizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="arrowsize", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ArrowsizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0.3),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrowsideValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(
        self, plotly_name="arrowside", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ArrowsideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["end", "start"]),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrowheadValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self, plotly_name="arrowhead", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ArrowheadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 8),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrowcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="arrowcolor", parent_name="layout.scene.annotation", **kwargs
    ):
        super(ArrowcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AlignValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="align", parent_name="layout.scene.annotation", **kwargs
    ):
        super(AlignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["left", "center", "right"]),
            **kwargs
        )
