import _plotly_utils.basevalidators


class ZsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="zsrc", parent_name="contourcarpet", **kwargs):
        super(ZsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="zmin", parent_name="contourcarpet", **kwargs):
        super(ZminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"zauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZmidValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="zmid", parent_name="contourcarpet", **kwargs):
        super(ZmidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZmaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="zmax", parent_name="contourcarpet", **kwargs):
        super(ZmaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"zauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZautoValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="zauto", parent_name="contourcarpet", **kwargs):
        super(ZautoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="z", parent_name="contourcarpet", **kwargs):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YAxisValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(self, plotly_name="yaxis", parent_name="contourcarpet", **kwargs):
        super(YAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", "y"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XAxisValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(self, plotly_name="xaxis", parent_name="contourcarpet", **kwargs):
        super(XAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", "x"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="visible", parent_name="contourcarpet", **kwargs):
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
    def __init__(self, plotly_name="uirevision", parent_name="contourcarpet", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UidValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="uid", parent_name="contourcarpet", **kwargs):
        super(UidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TransposeValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="transpose", parent_name="contourcarpet", **kwargs):
        super(TransposeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="textsrc", parent_name="contourcarpet", **kwargs):
        super(TextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="text", parent_name="contourcarpet", **kwargs):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class StreamValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="stream", parent_name="contourcarpet", **kwargs):
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
                plot with a stream. See https://chart-
                studio.plotly.com/settings for more details.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowscaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showscale", parent_name="contourcarpet", **kwargs):
        super(ShowscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlegendValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="showlegend", parent_name="contourcarpet", **kwargs):
        super(ShowlegendValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ReversescaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="reversescale", parent_name="contourcarpet", **kwargs
    ):
        super(ReversescaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="opacity", parent_name="contourcarpet", **kwargs):
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


class NcontoursValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="ncontours", parent_name="contourcarpet", **kwargs):
        super(NcontoursValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="contourcarpet", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="contourcarpet", **kwargs):
        super(MetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="meta", parent_name="contourcarpet", **kwargs):
        super(MetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="contourcarpet", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the color of the contour level. Has no
                effect if `contours.coloring` is set to
                "lines".
            dash
                Sets the dash style of lines. Set to a dash
                type string ("solid", "dot", "dash",
                "longdash", "dashdot", or "longdashdot") or a
                dash length list in px (eg "5px,10px,2px,2px").
            smoothing
                Sets the amount of smoothing for the contour
                lines, where 0 corresponds to no smoothing.
            width
                Sets the contour line width in (in px) Defaults
                to 0.5 when `contours.type` is "levels".
                Defaults to 2 when `contour.type` is
                "constraint".
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LegendgroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="legendgroup", parent_name="contourcarpet", **kwargs
    ):
        super(LegendgroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="idssrc", parent_name="contourcarpet", **kwargs):
        super(IdssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="ids", parent_name="contourcarpet", **kwargs):
        super(IdsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="hovertextsrc", parent_name="contourcarpet", **kwargs
    ):
        super(HovertextsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HovertextValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="hovertext", parent_name="contourcarpet", **kwargs):
        super(HovertextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="fillcolor", parent_name="contourcarpet", **kwargs):
        super(FillcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            colorscale_path=kwargs.pop("colorscale_path", "contourcarpet.colorscale"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DbValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="db", parent_name="contourcarpet", **kwargs):
        super(DbValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "scaled"}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DaValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="da", parent_name="contourcarpet", **kwargs):
        super(DaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"xtype": "scaled"}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdatasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="customdatasrc", parent_name="contourcarpet", **kwargs
    ):
        super(CustomdatasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="customdata", parent_name="contourcarpet", **kwargs):
        super(CustomdataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ContoursValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="contours", parent_name="contourcarpet", **kwargs):
        super(ContoursValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Contours"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            coloring
                Determines the coloring method showing the
                contour values. If "fill", coloring is done
                evenly between each contour level If "lines",
                coloring is done on the contour lines. If
                "none", no coloring is applied on this trace.
            end
                Sets the end contour level value. Must be more
                than `contours.start`
            labelfont
                Sets the font used for labeling the contour
                levels. The default color comes from the lines,
                if shown. The default family and size come from
                `layout.font`.
            labelformat
                Sets the contour label formatting rule using d3
                formatting mini-language which is very similar
                to Python, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
            operation
                Sets the constraint operation. "=" keeps
                regions equal to `value` "<" and "<=" keep
                regions less than `value` ">" and ">=" keep
                regions greater than `value` "[]", "()", "[)",
                and "(]" keep regions inside `value[0]` to
                `value[1]` "][", ")(", "](", ")[" keep regions
                outside `value[0]` to value[1]` Open vs. closed
                intervals make no difference to constraint
                display, but all versions are allowed for
                consistency with filter transforms.
            showlabels
                Determines whether to label the contour lines
                with their values.
            showlines
                Determines whether or not the contour lines are
                drawn. Has an effect only if
                `contours.coloring` is set to "fill".
            size
                Sets the step between each contour level. Must
                be positive.
            start
                Sets the starting contour level value. Must be
                less than `contours.end`
            type
                If `levels`, the data is represented as a
                contour plot with multiple levels displayed. If
                `constraint`, the data is represented as
                constraints with the invalid region shaded as
                specified by the `operation` and `value`
                parameters.
            value
                Sets the value or values of the constraint
                boundary. When `operation` is set to one of the
                comparison values (=,<,>=,>,<=) "value" is
                expected to be a number. When `operation` is
                set to one of the interval values
                ([],(),[),(],][,)(,](,)[) "value" is expected
                to be an array of two numbers where the first
                is the lower bound and the second is the upper
                bound.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorscaleValidator(_plotly_utils.basevalidators.ColorscaleValidator):
    def __init__(self, plotly_name="colorscale", parent_name="contourcarpet", **kwargs):
        super(ColorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {"autocolorscale": False}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorBarValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="colorbar", parent_name="contourcarpet", **kwargs):
        super(ColorBarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "ColorBar"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            bgcolor
                Sets the color of padded area.
            bordercolor
                Sets the axis line color.
            borderwidth
                Sets the width (in px) or the border enclosing
                this color bar.
            dtick
                Sets the step in-between ticks on this axis.
                Use with `tick0`. Must be a positive number, or
                special strings available to "log" and "date"
                axes. If the axis `type` is "log", then ticks
                are set every 10^(n*dtick) where n is the tick
                number. For example, to set a tick mark at 1,
                10, 100, 1000, ... set dtick to 1. To set tick
                marks at 1, 100, 10000, ... set dtick to 2. To
                set tick marks at 1, 5, 25, 125, 625, 3125, ...
                set dtick to log_10(5), or 0.69897000433. "log"
                has several special values; "L<f>", where `f`
                is a positive number, gives ticks linearly
                spaced in value (but not position). For example
                `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                plus small digits between, use "D1" (all
                digits) or "D2" (only 2 and 5). `tick0` is
                ignored for "D1" and "D2". If the axis `type`
                is "date", then you must convert the time to
                milliseconds. For example, to set the interval
                between ticks to one day, set `dtick` to
                86400000.0. "date" also has special values
                "M<n>" gives ticks spaced by a number of
                months. `n` must be a positive integer. To set
                ticks on the 15th of every third month, set
                `tick0` to "2000-01-15" and `dtick` to "M3". To
                set ticks every 4 years, set `dtick` to "M48"
            exponentformat
                Determines a formatting rule for the tick
                exponents. For example, consider the number
                1,000,000,000. If "none", it appears as
                1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                "power", 1x10^9 (with 9 in a super script). If
                "SI", 1G. If "B", 1B.
            len
                Sets the length of the color bar This measure
                excludes the padding of both ends. That is, the
                color bar length is this length minus the
                padding on both ends.
            lenmode
                Determines whether this color bar's length
                (i.e. the measure in the color variation
                direction) is set in units of plot "fraction"
                or in *pixels. Use `len` to set the value.
            nticks
                Specifies the maximum number of ticks for the
                particular axis. The actual number of ticks
                will be chosen automatically to be less than or
                equal to `nticks`. Has an effect only if
                `tickmode` is set to "auto".
            outlinecolor
                Sets the axis line color.
            outlinewidth
                Sets the width (in px) of the axis line.
            separatethousands
                If "true", even 4-digit integers are separated
            showexponent
                If "all", all exponents are shown besides their
                significands. If "first", only the exponent of
                the first tick is shown. If "last", only the
                exponent of the last tick is shown. If "none",
                no exponents appear.
            showticklabels
                Determines whether or not the tick labels are
                drawn.
            showtickprefix
                If "all", all tick labels are displayed with a
                prefix. If "first", only the first tick is
                displayed with a prefix. If "last", only the
                last tick is displayed with a suffix. If
                "none", tick prefixes are hidden.
            showticksuffix
                Same as `showtickprefix` but for tick suffixes.
            thickness
                Sets the thickness of the color bar This
                measure excludes the size of the padding, ticks
                and labels.
            thicknessmode
                Determines whether this color bar's thickness
                (i.e. the measure in the constant color
                direction) is set in units of plot "fraction"
                or in "pixels". Use `thickness` to set the
                value.
            tick0
                Sets the placement of the first tick on this
                axis. Use with `dtick`. If the axis `type` is
                "log", then you must take the log of your
                starting tick (e.g. to set the starting tick to
                100, set the `tick0` to 2) except when
                `dtick`=*L<f>* (see `dtick` for more info). If
                the axis `type` is "date", it should be a date
                string, like date data. If the axis `type` is
                "category", it should be a number, using the
                scale where each category is assigned a serial
                number from zero in the order it appears.
            tickangle
                Sets the angle of the tick labels with respect
                to the horizontal. For example, a `tickangle`
                of -90 draws the tick labels vertically.
            tickcolor
                Sets the tick color.
            tickfont
                Sets the color bar's tick label font
            tickformat
                Sets the tick label formatting rule using d3
                formatting mini-languages which are very
                similar to those in Python. For numbers, see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Time-Formatting.md#format
                We add one item to d3's date formatter: "%{n}f"
                for fractional seconds with n digits. For
                example, *2016-10-13 09:15:23.456* with
                tickformat "%H~%M~%S.%2f" would display
                "09~15~23.46"
            tickformatstops
                A tuple of :class:`plotly.graph_objects.contour
                carpet.colorbar.Tickformatstop` instances or
                dicts with compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.dat
                a.contourcarpet.colorbar.tickformatstopdefaults
                ), sets the default property values to use for
                elements of
                contourcarpet.colorbar.tickformatstops
            ticklen
                Sets the tick length (in px).
            tickmode
                Sets the tick mode for this axis. If "auto",
                the number of ticks is set via `nticks`. If
                "linear", the placement of the ticks is
                determined by a starting position `tick0` and a
                tick step `dtick` ("linear" is the default
                value if `tick0` and `dtick` are provided). If
                "array", the placement of the ticks is set via
                `tickvals` and the tick text is `ticktext`.
                ("array" is the default value if `tickvals` is
                provided).
            tickprefix
                Sets a tick label prefix.
            ticks
                Determines whether ticks are drawn or not. If
                "", this axis' ticks are not drawn. If
                "outside" ("inside"), this axis' are drawn
                outside (inside) the axis lines.
            ticksuffix
                Sets a tick label suffix.
            ticktext
                Sets the text displayed at the ticks position
                via `tickvals`. Only has an effect if
                `tickmode` is set to "array". Used with
                `tickvals`.
            ticktextsrc
                Sets the source reference on Chart Studio Cloud
                for  ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on Chart Studio Cloud
                for  tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                :class:`plotly.graph_objects.contourcarpet.colo
                rbar.Title` instance or dict with compatible
                properties
            titlefont
                Deprecated: Please use
                contourcarpet.colorbar.title.font instead. Sets
                this color bar's title font. Note that the
                title's font used to be set by the now
                deprecated `titlefont` attribute.
            titleside
                Deprecated: Please use
                contourcarpet.colorbar.title.side instead.
                Determines the location of color bar's title
                with respect to the color bar. Note that the
                title's location used to be set by the now
                deprecated `titleside` attribute.
            x
                Sets the x position of the color bar (in plot
                fraction).
            xanchor
                Sets this color bar's horizontal position
                anchor. This anchor binds the `x` position to
                the "left", "center" or "right" of the color
                bar.
            xpad
                Sets the amount of padding (in px) along the x
                direction.
            y
                Sets the y position of the color bar (in plot
                fraction).
            yanchor
                Sets this color bar's vertical position anchor
                This anchor binds the `y` position to the
                "top", "middle" or "bottom" of the color bar.
            ypad
                Sets the amount of padding (in px) along the y
                direction.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColoraxisValidator(_plotly_utils.basevalidators.SubplotidValidator):
    def __init__(self, plotly_name="coloraxis", parent_name="contourcarpet", **kwargs):
        super(ColoraxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop("dflt", None),
            edit_type=kwargs.pop("edit_type", "calc"),
            regex=kwargs.pop("regex", "/^coloraxis([2-9]|[1-9][0-9]+)?$/"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CarpetValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="carpet", parent_name="contourcarpet", **kwargs):
        super(CarpetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BtypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="btype", parent_name="contourcarpet", **kwargs):
        super(BtypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["array", "scaled"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class BsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="bsrc", parent_name="contourcarpet", **kwargs):
        super(BsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class B0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="b0", parent_name="contourcarpet", **kwargs):
        super(B0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "scaled"}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="b", parent_name="contourcarpet", **kwargs):
        super(BValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            implied_edits=kwargs.pop("implied_edits", {"ytype": "array"}),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutocontourValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="autocontour", parent_name="contourcarpet", **kwargs
    ):
        super(AutocontourValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutocolorscaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="autocolorscale", parent_name="contourcarpet", **kwargs
    ):
        super(AutocolorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AtypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="atype", parent_name="contourcarpet", **kwargs):
        super(AtypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["array", "scaled"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class AsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="asrc", parent_name="contourcarpet", **kwargs):
        super(AsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class A0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="a0", parent_name="contourcarpet", **kwargs):
        super(A0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            implied_edits=kwargs.pop("implied_edits", {"xtype": "scaled"}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="a", parent_name="contourcarpet", **kwargs):
        super(AValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            implied_edits=kwargs.pop("implied_edits", {"xtype": "array"}),
            role=kwargs.pop("role", "data"),
            **kwargs
        )
