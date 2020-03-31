import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yanchor", parent_name="layout.legend", **kwargs):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="y", parent_name="layout.legend", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            max=kwargs.pop("max", 3),
            min=kwargs.pop("min", -2),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.legend", **kwargs):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "left", "center", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="x", parent_name="layout.legend", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            max=kwargs.pop("max", 3),
            min=kwargs.pop("min", -2),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValignValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="valign", parent_name="layout.legend", **kwargs):
        super(ValignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="layout.legend", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TraceorderValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="traceorder", parent_name="layout.legend", **kwargs):
        super(TraceorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            extras=kwargs.pop("extras", ["normal"]),
            flags=kwargs.pop("flags", ["reversed", "grouped"]),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TracegroupgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="tracegroupgap", parent_name="layout.legend", **kwargs
    ):
        super(TracegroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TitleValidator(_plotly_utils.basevalidators.TitleValidator):
    def __init__(self, plotly_name="title", parent_name="layout.legend", **kwargs):
        super(TitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Title"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets this legend's title font.
            side
                Determines the location of legend's title with
                respect to the legend items. Defaulted to "top"
                with `orientation` is "h". Defaulted to "left"
                with `orientation` is "v". The *top left*
                options could be used to expand legend area in
                both x and y sides.
            text
                Sets the title of the legend.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="orientation", parent_name="layout.legend", **kwargs
    ):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["v", "h"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ItemsizingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="itemsizing", parent_name="layout.legend", **kwargs):
        super(ItemsizingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["trace", "constant"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ItemdoubleclickValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="itemdoubleclick", parent_name="layout.legend", **kwargs
    ):
        super(ItemdoubleclickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["toggle", "toggleothers", False]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ItemclickValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="itemclick", parent_name="layout.legend", **kwargs):
        super(ItemclickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["toggle", "toggleothers", False]),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="font", parent_name="layout.legend", **kwargs):
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


class BorderwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="borderwidth", parent_name="layout.legend", **kwargs
    ):
        super(BorderwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BordercolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="bordercolor", parent_name="layout.legend", **kwargs
    ):
        super(BordercolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="bgcolor", parent_name="layout.legend", **kwargs):
        super(BgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
