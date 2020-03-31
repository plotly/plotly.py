import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="uirevision", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="type", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["-", "linear", "log", "date", "category"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TitleValidator(_plotly_utils.basevalidators.TitleValidator):
    def __init__(
        self, plotly_name="title", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Title"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            font
                Sets this axis' title font. Note that the
                title's font used to be customized by the now
                deprecated `titlefont` attribute.
            text
                Sets the title of this axis. Note that before
                the existence of `title.text`, the title's
                contents used to be defined as the `title`
                attribute itself. This behavior has been
                deprecated.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="tickwidth", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickvalssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="tickvalssrc", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickvalssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickvalsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(
        self, plotly_name="tickvals", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickvalsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicktextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="ticktextsrc", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TicktextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicktextValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(
        self, plotly_name="ticktext", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TicktextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicksuffixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="ticksuffix", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TicksuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicksValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="ticks", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TicksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["outside", "inside", ""]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickprefixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="tickprefix", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickprefixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="tickmode", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["auto", "linear", "array"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicklenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="ticklen", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TicklenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickformatstopValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self,
        plotly_name="tickformatstopdefaults",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(TickformatstopValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickformatstop"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickformatstopsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(
        self,
        plotly_name="tickformatstops",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(TickformatstopsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickformatstop"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            dtickrange
                range [*min*, *max*], where "min", "max" -
                dtick values which describe some zoom level, it
                is possible to omit "min" or "max" value by
                passing "null"
            enabled
                Determines whether or not this stop is used. If
                `false`, this stop is ignored even within its
                `dtickrange`.
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
            value
                string - dtickformat for described zoom level,
                the same as "tickformat"
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="tickformat", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="tickfont", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tickfont"),
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


class TickcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="tickcolor", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickangleValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(
        self, plotly_name="tickangle", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(TickangleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class Tick0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="tick0", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(Tick0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"tickmode": "linear"}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="side", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(SideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["clockwise", "counterclockwise"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowticksuffixValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="showticksuffix",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(ShowticksuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowtickprefixValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="showtickprefix",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(ShowtickprefixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowticklabelsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="showticklabels",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(ShowticklabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlineValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showline", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(ShowlineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowgridValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showgrid", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(ShowgridValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowexponentValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="showexponent",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(ShowexponentValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class SeparatethousandsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self,
        plotly_name="separatethousands",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(SeparatethousandsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RangemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="rangemode", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(RangemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["tozero", "nonnegative", "normal"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(
        self, plotly_name="range", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop("anim", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"autorange": False}),
            items=kwargs.pop(
                "items",
                [
                    {
                        "valType": "any",
                        "editType": "plot",
                        "impliedEdits": {"^autorange": False},
                    },
                    {
                        "valType": "any",
                        "editType": "plot",
                        "impliedEdits": {"^autorange": False},
                    },
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NticksValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self, plotly_name="nticks", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(NticksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LinewidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="linewidth", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(LinewidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LinecolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="linecolor", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(LinecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LayerValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="layer", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(LayerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["above traces", "below traces"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="hoverformat", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(HoverformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class GridwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="gridwidth", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(GridwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class GridcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="gridcolor", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(GridcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ExponentformatValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="exponentformat",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(ExponentformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["none", "e", "E", "power", "SI", "B"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class DtickValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="dtick", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(DtickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"tickmode": "linear"}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CategoryorderValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="categoryorder",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(CategoryorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values",
                [
                    "trace",
                    "category ascending",
                    "category descending",
                    "array",
                    "total ascending",
                    "total descending",
                    "min ascending",
                    "min descending",
                    "max ascending",
                    "max descending",
                    "sum ascending",
                    "sum descending",
                    "mean ascending",
                    "mean descending",
                    "median ascending",
                    "median descending",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CategoryarraysrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self,
        plotly_name="categoryarraysrc",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(CategoryarraysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CategoryarrayValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(
        self,
        plotly_name="categoryarray",
        parent_name="layout.polar.radialaxis",
        **kwargs
    ):
        super(CategoryarrayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CalendarValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="calendar", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(CalendarValidator, self).__init__(
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


class AutorangeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="autorange", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(AutorangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [True, False, "reversed"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class AngleValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(
        self, plotly_name="angle", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super(AngleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
