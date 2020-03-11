import _plotly_utils.basevalidators


class SymbolsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="symbolsrc", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SymbolsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SymbolValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="symbol", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SymbolValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop(
                "values",
                [
                    0,
                    "circle",
                    100,
                    "circle-open",
                    200,
                    "circle-dot",
                    300,
                    "circle-open-dot",
                    1,
                    "square",
                    101,
                    "square-open",
                    201,
                    "square-dot",
                    301,
                    "square-open-dot",
                    2,
                    "diamond",
                    102,
                    "diamond-open",
                    202,
                    "diamond-dot",
                    302,
                    "diamond-open-dot",
                    3,
                    "cross",
                    103,
                    "cross-open",
                    203,
                    "cross-dot",
                    303,
                    "cross-open-dot",
                    4,
                    "x",
                    104,
                    "x-open",
                    204,
                    "x-dot",
                    304,
                    "x-open-dot",
                    5,
                    "triangle-up",
                    105,
                    "triangle-up-open",
                    205,
                    "triangle-up-dot",
                    305,
                    "triangle-up-open-dot",
                    6,
                    "triangle-down",
                    106,
                    "triangle-down-open",
                    206,
                    "triangle-down-dot",
                    306,
                    "triangle-down-open-dot",
                    7,
                    "triangle-left",
                    107,
                    "triangle-left-open",
                    207,
                    "triangle-left-dot",
                    307,
                    "triangle-left-open-dot",
                    8,
                    "triangle-right",
                    108,
                    "triangle-right-open",
                    208,
                    "triangle-right-dot",
                    308,
                    "triangle-right-open-dot",
                    9,
                    "triangle-ne",
                    109,
                    "triangle-ne-open",
                    209,
                    "triangle-ne-dot",
                    309,
                    "triangle-ne-open-dot",
                    10,
                    "triangle-se",
                    110,
                    "triangle-se-open",
                    210,
                    "triangle-se-dot",
                    310,
                    "triangle-se-open-dot",
                    11,
                    "triangle-sw",
                    111,
                    "triangle-sw-open",
                    211,
                    "triangle-sw-dot",
                    311,
                    "triangle-sw-open-dot",
                    12,
                    "triangle-nw",
                    112,
                    "triangle-nw-open",
                    212,
                    "triangle-nw-dot",
                    312,
                    "triangle-nw-open-dot",
                    13,
                    "pentagon",
                    113,
                    "pentagon-open",
                    213,
                    "pentagon-dot",
                    313,
                    "pentagon-open-dot",
                    14,
                    "hexagon",
                    114,
                    "hexagon-open",
                    214,
                    "hexagon-dot",
                    314,
                    "hexagon-open-dot",
                    15,
                    "hexagon2",
                    115,
                    "hexagon2-open",
                    215,
                    "hexagon2-dot",
                    315,
                    "hexagon2-open-dot",
                    16,
                    "octagon",
                    116,
                    "octagon-open",
                    216,
                    "octagon-dot",
                    316,
                    "octagon-open-dot",
                    17,
                    "star",
                    117,
                    "star-open",
                    217,
                    "star-dot",
                    317,
                    "star-open-dot",
                    18,
                    "hexagram",
                    118,
                    "hexagram-open",
                    218,
                    "hexagram-dot",
                    318,
                    "hexagram-open-dot",
                    19,
                    "star-triangle-up",
                    119,
                    "star-triangle-up-open",
                    219,
                    "star-triangle-up-dot",
                    319,
                    "star-triangle-up-open-dot",
                    20,
                    "star-triangle-down",
                    120,
                    "star-triangle-down-open",
                    220,
                    "star-triangle-down-dot",
                    320,
                    "star-triangle-down-open-dot",
                    21,
                    "star-square",
                    121,
                    "star-square-open",
                    221,
                    "star-square-dot",
                    321,
                    "star-square-open-dot",
                    22,
                    "star-diamond",
                    122,
                    "star-diamond-open",
                    222,
                    "star-diamond-dot",
                    322,
                    "star-diamond-open-dot",
                    23,
                    "diamond-tall",
                    123,
                    "diamond-tall-open",
                    223,
                    "diamond-tall-dot",
                    323,
                    "diamond-tall-open-dot",
                    24,
                    "diamond-wide",
                    124,
                    "diamond-wide-open",
                    224,
                    "diamond-wide-dot",
                    324,
                    "diamond-wide-open-dot",
                    25,
                    "hourglass",
                    125,
                    "hourglass-open",
                    26,
                    "bowtie",
                    126,
                    "bowtie-open",
                    27,
                    "circle-cross",
                    127,
                    "circle-cross-open",
                    28,
                    "circle-x",
                    128,
                    "circle-x-open",
                    29,
                    "square-cross",
                    129,
                    "square-cross-open",
                    30,
                    "square-x",
                    130,
                    "square-x-open",
                    31,
                    "diamond-cross",
                    131,
                    "diamond-cross-open",
                    32,
                    "diamond-x",
                    132,
                    "diamond-x-open",
                    33,
                    "cross-thin",
                    133,
                    "cross-thin-open",
                    34,
                    "x-thin",
                    134,
                    "x-thin-open",
                    35,
                    "asterisk",
                    135,
                    "asterisk-open",
                    36,
                    "hash",
                    136,
                    "hash-open",
                    236,
                    "hash-dot",
                    336,
                    "hash-open-dot",
                    37,
                    "y-up",
                    137,
                    "y-up-open",
                    38,
                    "y-down",
                    138,
                    "y-down-open",
                    39,
                    "y-left",
                    139,
                    "y-left-open",
                    40,
                    "y-right",
                    140,
                    "y-right-open",
                    41,
                    "line-ew",
                    141,
                    "line-ew-open",
                    42,
                    "line-ns",
                    142,
                    "line-ns-open",
                    43,
                    "line-ne",
                    143,
                    "line-ne-open",
                    44,
                    "line-nw",
                    144,
                    "line-nw-open",
                ],
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizesrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="sizesrc", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SizesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizerefValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="sizeref", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SizerefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="sizemode", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SizemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["diameter", "area"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizeminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="sizemin", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SizeminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="size", parent_name="scattercarpet.marker", **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowscaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showscale", parent_name="scattercarpet.marker", **kwargs
    ):
        super(ShowscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ReversescaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="reversescale", parent_name="scattercarpet.marker", **kwargs
    ):
        super(ReversescaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacitysrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="opacitysrc", parent_name="scattercarpet.marker", **kwargs
    ):
        super(OpacitysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="opacity", parent_name="scattercarpet.marker", **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MaxdisplayedValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="maxdisplayed", parent_name="scattercarpet.marker", **kwargs
    ):
        super(MaxdisplayedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="line", parent_name="scattercarpet.marker", **kwargs
    ):
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
                determined by `marker.line.colorscale`. Has an
                effect only if in `marker.line.color`is set to
                a numerical array. In case `colorscale` is
                unspecified or `autocolorscale` is true, the
                default  palette will be chosen according to
                whether numbers in the `color` array are all
                positive, all negative or mixed.
            cauto
                Determines whether or not the color domain is
                computed with respect to the input data (here
                in `marker.line.color`) or the bounds set in
                `marker.line.cmin` and `marker.line.cmax`  Has
                an effect only if in `marker.line.color`is set
                to a numerical array. Defaults to `false` when
                `marker.line.cmin` and `marker.line.cmax` are
                set by the user.
            cmax
                Sets the upper bound of the color domain. Has
                an effect only if in `marker.line.color`is set
                to a numerical array. Value should have the
                same units as in `marker.line.color` and if
                set, `marker.line.cmin` must be set as well.
            cmid
                Sets the mid-point of the color domain by
                scaling `marker.line.cmin` and/or
                `marker.line.cmax` to be equidistant to this
                point. Has an effect only if in
                `marker.line.color`is set to a numerical array.
                Value should have the same units as in
                `marker.line.color`. Has no effect when
                `marker.line.cauto` is `false`.
            cmin
                Sets the lower bound of the color domain. Has
                an effect only if in `marker.line.color`is set
                to a numerical array. Value should have the
                same units as in `marker.line.color` and if
                set, `marker.line.cmax` must be set as well.
            color
                Sets themarker.linecolor. It accepts either a
                specific color or an array of numbers that are
                mapped to the colorscale relative to the max
                and min values of the array or relative to
                `marker.line.cmin` and `marker.line.cmax` if
                set.
            coloraxis
                Sets a reference to a shared color axis.
                References to these shared color axes are
                "coloraxis", "coloraxis2", "coloraxis3", etc.
                Settings for these shared color axes are set in
                the layout, under `layout.coloraxis`,
                `layout.coloraxis2`, etc. Note that multiple
                color scales can be linked to the same color
                axis.
            colorscale
                Sets the colorscale. Has an effect only if in
                `marker.line.color`is set to a numerical array.
                The colorscale must be an array containing
                arrays mapping a normalized value to an rgb,
                rgba, hex, hsl, hsv, or named color string. At
                minimum, a mapping for the lowest (0) and
                highest (1) values are required. For example,
                `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                To control the bounds of the colorscale in
                color space, use`marker.line.cmin` and
                `marker.line.cmax`. Alternatively, `colorscale`
                may be a palette name string of the following
                list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,R
                eds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Black
                body,Earth,Electric,Viridis,Cividis.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            reversescale
                Reverses the color mapping if true. Has an
                effect only if in `marker.line.color`is set to
                a numerical array. If true, `marker.line.cmin`
                will correspond to the last color in the array
                and `marker.line.cmax` will correspond to the
                first color.
            width
                Sets the width (in px) of the lines bounding
                the marker points.
            widthsrc
                Sets the source reference on plot.ly for  width
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class GradientValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="gradient", parent_name="scattercarpet.marker", **kwargs
    ):
        super(GradientValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Gradient"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the final color of the gradient fill: the
                center color for radial, the right for
                horizontal, or the bottom for vertical.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            type
                Sets the type of gradient used to fill the
                markers
            typesrc
                Sets the source reference on plot.ly for  type
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="colorsrc", parent_name="scattercarpet.marker", **kwargs
    ):
        super(ColorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorscaleValidator(_plotly_utils.basevalidators.ColorscaleValidator):
    def __init__(
        self, plotly_name="colorscale", parent_name="scattercarpet.marker", **kwargs
    ):
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
    def __init__(
        self, plotly_name="colorbar", parent_name="scattercarpet.marker", **kwargs
    ):
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
                A tuple of :class:`plotly.graph_objects.scatter
                carpet.marker.colorbar.Tickformatstop`
                instances or dicts with compatible properties
            tickformatstopdefaults
                When used in a template (as layout.template.dat
                a.scattercarpet.marker.colorbar.tickformatstopd
                efaults), sets the default property values to
                use for elements of
                scattercarpet.marker.colorbar.tickformatstops
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
                Sets the source reference on plot.ly for
                ticktext .
            tickvals
                Sets the values at which ticks on this axis
                appear. Only has an effect if `tickmode` is set
                to "array". Used with `ticktext`.
            tickvalssrc
                Sets the source reference on plot.ly for
                tickvals .
            tickwidth
                Sets the tick width (in px).
            title
                :class:`plotly.graph_objects.scattercarpet.mark
                er.colorbar.Title` instance or dict with
                compatible properties
            titlefont
                Deprecated: Please use
                scattercarpet.marker.colorbar.title.font
                instead. Sets this color bar's title font. Note
                that the title's font used to be set by the now
                deprecated `titlefont` attribute.
            titleside
                Deprecated: Please use
                scattercarpet.marker.colorbar.title.side
                instead. Determines the location of color bar's
                title with respect to the color bar. Note that
                the title's location used to be set by the now
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
    def __init__(
        self, plotly_name="coloraxis", parent_name="scattercarpet.marker", **kwargs
    ):
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


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="scattercarpet.marker", **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "style"),
            colorscale_path=kwargs.pop(
                "colorscale_path", "scattercarpet.marker.colorscale"
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmin", parent_name="scattercarpet.marker", **kwargs
    ):
        super(CminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CmidValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmid", parent_name="scattercarpet.marker", **kwargs
    ):
        super(CmidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CmaxValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="cmax", parent_name="scattercarpet.marker", **kwargs
    ):
        super(CmaxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"cauto": False}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CautoValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="cauto", parent_name="scattercarpet.marker", **kwargs
    ):
        super(CautoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AutocolorscaleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="autocolorscale", parent_name="scattercarpet.marker", **kwargs
    ):
        super(AutocolorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
