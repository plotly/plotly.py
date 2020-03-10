from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class RadialAxis(_BaseLayoutHierarchyType):

    # angle
    # -----
    @property
    def angle(self):
        """
        Sets the angle (in degrees) from which the radial axis is
        drawn. Note that by default, radial axis line on the theta=0
        line corresponds to a line pointing right (like what
        mathematicians prefer). Defaults to the first `polar.sector`
        angle.
    
        The 'angle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["angle"]

    @angle.setter
    def angle(self, val):
        self["angle"] = val

    # autorange
    # ---------
    @property
    def autorange(self):
        """
        Determines whether or not the range of this axis is computed in
        relation to the input data. See `rangemode` for more info. If
        `range` is provided, then `autorange` is set to False.
    
        The 'autorange' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'reversed']

        Returns
        -------
        Any
        """
        return self["autorange"]

    @autorange.setter
    def autorange(self, val):
        self["autorange"] = val

    # calendar
    # --------
    @property
    def calendar(self):
        """
        Sets the calendar system to use for `range` and `tick0` if this
        is a date axis. This does not set the calendar for interpreting
        data on this axis, that's specified in the trace or via the
        global `layout.calendar`
    
        The 'calendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self["calendar"]

    @calendar.setter
    def calendar(self, val):
        self["calendar"] = val

    # categoryarray
    # -------------
    @property
    def categoryarray(self):
        """
        Sets the order in which categories on this axis appear. Only
        has an effect if `categoryorder` is set to "array". Used with
        `categoryorder`.
    
        The 'categoryarray' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["categoryarray"]

    @categoryarray.setter
    def categoryarray(self, val):
        self["categoryarray"] = val

    # categoryarraysrc
    # ----------------
    @property
    def categoryarraysrc(self):
        """
        Sets the source reference on plot.ly for  categoryarray .
    
        The 'categoryarraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["categoryarraysrc"]

    @categoryarraysrc.setter
    def categoryarraysrc(self, val):
        self["categoryarraysrc"] = val

    # categoryorder
    # -------------
    @property
    def categoryorder(self):
        """
        Specifies the ordering logic for the case of categorical
        variables. By default, plotly uses "trace", which specifies the
        order that is present in the data supplied. Set `categoryorder`
        to *category ascending* or *category descending* if order
        should be determined by the alphanumerical order of the
        category names. Set `categoryorder` to "array" to derive the
        ordering from the attribute `categoryarray`. If a category is
        not found in the `categoryarray` array, the sorting behavior
        for that attribute will be identical to the "trace" mode. The
        unspecified categories will follow the categories in
        `categoryarray`. Set `categoryorder` to *total ascending* or
        *total descending* if order should be determined by the
        numerical order of the values. Similarly, the order can be
        determined by the min, max, sum, mean or median of all the
        values.
    
        The 'categoryorder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'category ascending', 'category descending',
                'array', 'total ascending', 'total descending', 'min
                ascending', 'min descending', 'max ascending', 'max
                descending', 'sum ascending', 'sum descending', 'mean
                ascending', 'mean descending', 'median ascending', 'median
                descending']

        Returns
        -------
        Any
        """
        return self["categoryorder"]

    @categoryorder.setter
    def categoryorder(self, val):
        self["categoryorder"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets default for all colors associated with this axis all at
        once: line, font, tick, and grid colors. Grid color is
        lightened by blending this with the plot background Individual
        pieces can override this.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to
        "log" and "date" axes. If the axis `type` is "log", then ticks
        are set every 10^(n*dtick) where n is the tick number. For
        example, to set a tick mark at 1, 10, 100, 1000, ... set dtick
        to 1. To set tick marks at 1, 100, 10000, ... set dtick to 2.
        To set tick marks at 1, 5, 25, 125, 625, 3125, ... set dtick to
        log_10(5), or 0.69897000433. "log" has several special values;
        "L<f>", where `f` is a positive number, gives ticks linearly
        spaced in value (but not position). For example `tick0` = 0.1,
        `dtick` = "L0.5" will put ticks at 0.1, 0.6, 1.1, 1.6 etc. To
        show powers of 10 plus small digits between, use "D1" (all
        digits) or "D2" (only 2 and 5). `tick0` is ignored for "D1" and
        "D2". If the axis `type` is "date", then you must convert the
        time to milliseconds. For example, to set the interval between
        ticks to one day, set `dtick` to 86400000.0. "date" also has
        special values "M<n>" gives ticks spaced by a number of months.
        `n` must be a positive integer. To set ticks on the 15th of
        every third month, set `tick0` to "2000-01-15" and `dtick` to
        "M3". To set ticks every 4 years, set `dtick` to "M48"
    
        The 'dtick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["dtick"]

    @dtick.setter
    def dtick(self, val):
        self["dtick"] = val

    # exponentformat
    # --------------
    @property
    def exponentformat(self):
        """
        Determines a formatting rule for the tick exponents. For
        example, consider the number 1,000,000,000. If "none", it
        appears as 1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
        "power", 1x10^9 (with 9 in a super script). If "SI", 1G. If
        "B", 1B.
    
        The 'exponentformat' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'e', 'E', 'power', 'SI', 'B']

        Returns
        -------
        Any
        """
        return self["exponentformat"]

    @exponentformat.setter
    def exponentformat(self, val):
        self["exponentformat"] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the color of the grid lines.
    
        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["gridcolor"]

    @gridcolor.setter
    def gridcolor(self, val):
        self["gridcolor"] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the width (in px) of the grid lines.
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["gridwidth"]

    @gridwidth.setter
    def gridwidth(self, val):
        self["gridwidth"] = val

    # hoverformat
    # -----------
    @property
    def hoverformat(self):
        """
        Sets the hover text formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format And for dates
        see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Time-Formatting.md#format We add one item
        to d3's date formatter: "%{n}f" for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display "09~15~23.46"
    
        The 'hoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["hoverformat"]

    @hoverformat.setter
    def hoverformat(self, val):
        self["hoverformat"] = val

    # layer
    # -----
    @property
    def layer(self):
        """
        Sets the layer on which this axis is displayed. If *above
        traces*, this axis is displayed above all the subplot's traces
        If *below traces*, this axis is displayed below all the
        subplot's traces, but above the grid lines. Useful when used
        together with scatter-like traces with `cliponaxis` set to
        False to show markers and/or text nodes above this axis.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['above traces', 'below traces']

        Returns
        -------
        Any
        """
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    # linecolor
    # ---------
    @property
    def linecolor(self):
        """
        Sets the axis line color.
    
        The 'linecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["linecolor"]

    @linecolor.setter
    def linecolor(self, val):
        self["linecolor"] = val

    # linewidth
    # ---------
    @property
    def linewidth(self):
        """
        Sets the width (in px) of the axis line.
    
        The 'linewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["linewidth"]

    @linewidth.setter
    def linewidth(self, val):
        self["linewidth"] = val

    # nticks
    # ------
    @property
    def nticks(self):
        """
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to "auto".
    
        The 'nticks' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["nticks"]

    @nticks.setter
    def nticks(self, val):
        self["nticks"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis. If the axis `type` is "log", then
        you must take the log of your desired range (e.g. to set the
        range from 1 to 100, set the range from 0 to 2). If the axis
        `type` is "date", it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is "category", it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property accepts values of any type
    (1) The 'range[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    # rangemode
    # ---------
    @property
    def rangemode(self):
        """
        If *tozero*`, the range extends to 0, regardless of the input
        data If "nonnegative", the range is non-negative, regardless of
        the input data. If "normal", the range is computed in relation
        to the extrema of the input data (same behavior as for
        cartesian axes).
    
        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['tozero', 'nonnegative', 'normal']

        Returns
        -------
        Any
        """
        return self["rangemode"]

    @rangemode.setter
    def rangemode(self, val):
        self["rangemode"] = val

    # separatethousands
    # -----------------
    @property
    def separatethousands(self):
        """
        If "true", even 4-digit integers are separated
    
        The 'separatethousands' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["separatethousands"]

    @separatethousands.setter
    def separatethousands(self, val):
        self["separatethousands"] = val

    # showexponent
    # ------------
    @property
    def showexponent(self):
        """
        If "all", all exponents are shown besides their significands.
        If "first", only the exponent of the first tick is shown. If
        "last", only the exponent of the last tick is shown. If "none",
        no exponents appear.
    
        The 'showexponent' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self["showexponent"]

    @showexponent.setter
    def showexponent(self, val):
        self["showexponent"] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Determines whether or not grid lines are drawn. If True, the
        grid lines are drawn at every tick mark.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showgrid"]

    @showgrid.setter
    def showgrid(self, val):
        self["showgrid"] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Determines whether or not a line bounding this axis is drawn.
    
        The 'showline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showline"]

    @showline.setter
    def showline(self, val):
        self["showline"] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether or not the tick labels are drawn.
    
        The 'showticklabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showticklabels"]

    @showticklabels.setter
    def showticklabels(self, val):
        self["showticklabels"] = val

    # showtickprefix
    # --------------
    @property
    def showtickprefix(self):
        """
        If "all", all tick labels are displayed with a prefix. If
        "first", only the first tick is displayed with a prefix. If
        "last", only the last tick is displayed with a suffix. If
        "none", tick prefixes are hidden.
    
        The 'showtickprefix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self["showtickprefix"]

    @showtickprefix.setter
    def showtickprefix(self, val):
        self["showtickprefix"] = val

    # showticksuffix
    # --------------
    @property
    def showticksuffix(self):
        """
        Same as `showtickprefix` but for tick suffixes.
    
        The 'showticksuffix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self["showticksuffix"]

    @showticksuffix.setter
    def showticksuffix(self, val):
        self["showticksuffix"] = val

    # side
    # ----
    @property
    def side(self):
        """
        Determines on which side of radial axis line the tick and tick
        labels appear.
    
        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['clockwise', 'counterclockwise']

        Returns
        -------
        Any
        """
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the placement of the first tick on this axis. Use with
        `dtick`. If the axis `type` is "log", then you must take the
        log of your starting tick (e.g. to set the starting tick to
        100, set the `tick0` to 2) except when `dtick`=*L<f>* (see
        `dtick` for more info). If the axis `type` is "date", it should
        be a date string, like date data. If the axis `type` is
        "category", it should be a number, using the scale where each
        category is assigned a serial number from zero in the order it
        appears.
    
        The 'tick0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["tick0"]

    @tick0.setter
    def tick0(self, val):
        self["tick0"] = val

    # tickangle
    # ---------
    @property
    def tickangle(self):
        """
        Sets the angle of the tick labels with respect to the
        horizontal. For example, a `tickangle` of -90 draws the tick
        labels vertically.
    
        The 'tickangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["tickangle"]

    @tickangle.setter
    def tickangle(self, val):
        self["tickangle"] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the tick color.
    
        The 'tickcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["tickcolor"]

    @tickcolor.setter
    def tickcolor(self, val):
        self["tickcolor"] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the tick font.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.radialaxis.Tickfont`
          - A dict of string/value properties that will be passed
            to the Tickfont constructor
    
            Supported dict properties:
                
                color
    
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

        Returns
        -------
        plotly.graph_objs.layout.polar.radialaxis.Tickfont
        """
        return self["tickfont"]

    @tickfont.setter
    def tickfont(self, val):
        self["tickfont"] = val

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format And for dates
        see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Time-Formatting.md#format We add one item
        to d3's date formatter: "%{n}f" for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display "09~15~23.46"
    
        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["tickformat"]

    @tickformat.setter
    def tickformat(self, val):
        self["tickformat"] = val

    # tickformatstops
    # ---------------
    @property
    def tickformatstops(self):
        """
        The 'tickformatstops' property is a tuple of instances of
        Tickformatstop that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.polar.radialaxis.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor
    
            Supported dict properties:
                
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

        Returns
        -------
        tuple[plotly.graph_objs.layout.polar.radialaxis.Tickformatstop]
        """
        return self["tickformatstops"]

    @tickformatstops.setter
    def tickformatstops(self, val):
        self["tickformatstops"] = val

    # tickformatstopdefaults
    # ----------------------
    @property
    def tickformatstopdefaults(self):
        """
        When used in a template (as layout.template.layout.polar.radial
        axis.tickformatstopdefaults), sets the default property values
        to use for elements of layout.polar.radialaxis.tickformatstops
    
        The 'tickformatstopdefaults' property is an instance of Tickformatstop
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.radialaxis.Tickformatstop`
          - A dict of string/value properties that will be passed
            to the Tickformatstop constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.polar.radialaxis.Tickformatstop
        """
        return self["tickformatstopdefaults"]

    @tickformatstopdefaults.setter
    def tickformatstopdefaults(self, val):
        self["tickformatstopdefaults"] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the tick length (in px).
    
        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["ticklen"]

    @ticklen.setter
    def ticklen(self, val):
        self["ticklen"] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        Sets the tick mode for this axis. If "auto", the number of
        ticks is set via `nticks`. If "linear", the placement of the
        ticks is determined by a starting position `tick0` and a tick
        step `dtick` ("linear" is the default value if `tick0` and
        `dtick` are provided). If "array", the placement of the ticks
        is set via `tickvals` and the tick text is `ticktext`. ("array"
        is the default value if `tickvals` is provided).
    
        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'linear', 'array']

        Returns
        -------
        Any
        """
        return self["tickmode"]

    @tickmode.setter
    def tickmode(self, val):
        self["tickmode"] = val

    # tickprefix
    # ----------
    @property
    def tickprefix(self):
        """
        Sets a tick label prefix.
    
        The 'tickprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["tickprefix"]

    @tickprefix.setter
    def tickprefix(self, val):
        self["tickprefix"] = val

    # ticks
    # -----
    @property
    def ticks(self):
        """
        Determines whether ticks are drawn or not. If "", this axis'
        ticks are not drawn. If "outside" ("inside"), this axis' are
        drawn outside (inside) the axis lines.
    
        The 'ticks' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['outside', 'inside', '']

        Returns
        -------
        Any
        """
        return self["ticks"]

    @ticks.setter
    def ticks(self, val):
        self["ticks"] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Sets a tick label suffix.
    
        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["ticksuffix"]

    @ticksuffix.setter
    def ticksuffix(self, val):
        self["ticksuffix"] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to "array". Used with
        `tickvals`.
    
        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["ticktext"]

    @ticktext.setter
    def ticktext(self, val):
        self["ticktext"] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on plot.ly for  ticktext .
    
        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ticktextsrc"]

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self["ticktextsrc"] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to "array". Used with `ticktext`.
    
        The 'tickvals' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["tickvals"]

    @tickvals.setter
    def tickvals(self, val):
        self["tickvals"] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on plot.ly for  tickvals .
    
        The 'tickvalssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["tickvalssrc"]

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self["tickvalssrc"] = val

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the tick width (in px).
    
        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["tickwidth"]

    @tickwidth.setter
    def tickwidth(self, val):
        self["tickwidth"] = val

    # title
    # -----
    @property
    def title(self):
        """
        The 'title' property is an instance of Title
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.radialaxis.Title`
          - A dict of string/value properties that will be passed
            to the Title constructor
    
            Supported dict properties:
                
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

        Returns
        -------
        plotly.graph_objs.layout.polar.radialaxis.Title
        """
        return self["title"]

    @title.setter
    def title(self, val):
        self["title"] = val

    # titlefont
    # ---------
    @property
    def titlefont(self):
        """
        Deprecated: Please use layout.polar.radialaxis.title.font
        instead. Sets this axis' title font. Note that the title's font
        used to be customized by the now deprecated `titlefont`
        attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.radialaxis.title.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
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

        Returns
        -------
        
        """
        return self["titlefont"]

    @titlefont.setter
    def titlefont(self, val):
        self["titlefont"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the axis type. By default, plotly attempts to determined
        the axis type by looking into the data of the traces that
        referenced the axis in question.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['-', 'linear', 'log', 'date', 'category']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in axis `range`,
        `autorange`, `angle`, and `title` if in `editable: true`
        configuration. Defaults to `polar<N>.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        A single toggle to hide the axis while preserving interaction
        like dragging. Default is true when a cheater plot is present
        on the axis, otherwise false
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.polar"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        angle
            Sets the angle (in degrees) from which the radial axis
            is drawn. Note that by default, radial axis line on the
            theta=0 line corresponds to a line pointing right (like
            what mathematicians prefer). Defaults to the first
            `polar.sector` angle.
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to False.
        calendar
            Sets the calendar system to use for `range` and `tick0`
            if this is a date axis. This does not set the calendar
            for interpreting data on this axis, that's specified in
            the trace or via the global `layout.calendar`
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses "trace",
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to "array" to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            "trace" mode. The unspecified categories will follow
            the categories in `categoryarray`. Set `categoryorder`
            to *total ascending* or *total descending* if order
            should be determined by the numerical order of the
            values. Similarly, the order can be determined by the
            min, max, sum, mean or median of all the values.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to "log" and "date" axes. If the axis `type`
            is "log", then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. "log" has several special
            values; "L<f>", where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = "L0.5" will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use "D1" (all digits) or "D2"
            (only 2 and 5). `tick0` is ignored for "D1" and "D2".
            If the axis `type` is "date", then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            "date" also has special values "M<n>" gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to "2000-01-15" and `dtick` to "M3". To set
            ticks every 4 years, set `dtick` to "M48"
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            "none", it appears as 1,000,000,000. If "e", 1e+9. If
            "E", 1E+9. If "power", 1x10^9 (with 9 in a super
            script). If "SI", 1G. If "B", 1B.
        gridcolor
            Sets the color of the grid lines.
        gridwidth
            Sets the width (in px) of the grid lines.
        hoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        layer
            Sets the layer on which this axis is displayed. If
            *above traces*, this axis is displayed above all the
            subplot's traces If *below traces*, this axis is
            displayed below all the subplot's traces, but above the
            grid lines. Useful when used together with scatter-like
            traces with `cliponaxis` set to False to show markers
            and/or text nodes above this axis.
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        range
            Sets the range of this axis. If the axis `type` is
            "log", then you must take the log of your desired range
            (e.g. to set the range from 1 to 100, set the range
            from 0 to 2). If the axis `type` is "date", it should
            be date strings, like date data, though Date objects
            and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is "category", it should be
            numbers, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        rangemode
            If *tozero*`, the range extends to 0, regardless of the
            input data If "nonnegative", the range is non-negative,
            regardless of the input data. If "normal", the range is
            computed in relation to the extrema of the input data
            (same behavior as for cartesian axes).
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If "all", all exponents are shown besides their
            significands. If "first", only the exponent of the
            first tick is shown. If "last", only the exponent of
            the last tick is shown. If "none", no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            True, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        side
            Determines on which side of radial axis line the tick
            and tick labels appear.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is "log", then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is "date", it should be a date string, like
            date data. If the axis `type` is "category", it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.layout.polar.ra
            dialaxis.Tickformatstop` instances or dicts with
            compatible properties
        tickformatstopdefaults
            When used in a template (as layout.template.layout.pola
            r.radialaxis.tickformatstopdefaults), sets the default
            property values to use for elements of
            layout.polar.radialaxis.tickformatstops
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If "auto", the number
            of ticks is set via `nticks`. If "linear", the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` ("linear" is
            the default value if `tick0` and `dtick` are provided).
            If "array", the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. ("array" is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If "", this
            axis' ticks are not drawn. If "outside" ("inside"),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        title
            :class:`plotly.graph_objects.layout.polar.radialaxis.Ti
            tle` instance or dict with compatible properties
        titlefont
            Deprecated: Please use
            layout.polar.radialaxis.title.font instead. Sets this
            axis' title font. Note that the title's font used to be
            customized by the now deprecated `titlefont` attribute.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        uirevision
            Controls persistence of user-driven changes in axis
            `range`, `autorange`, `angle`, and `title` if in
            `editable: true` configuration. Defaults to
            `polar<N>.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        """

    _mapped_properties = {"titlefont": ("title", "font")}

    def __init__(
        self,
        arg=None,
        angle=None,
        autorange=None,
        calendar=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        dtick=None,
        exponentformat=None,
        gridcolor=None,
        gridwidth=None,
        hoverformat=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        nticks=None,
        range=None,
        rangemode=None,
        separatethousands=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        side=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickformatstopdefaults=None,
        ticklen=None,
        tickmode=None,
        tickprefix=None,
        ticks=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,
        title=None,
        titlefont=None,
        type=None,
        uirevision=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new RadialAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.polar.RadialAxis`
        angle
            Sets the angle (in degrees) from which the radial axis
            is drawn. Note that by default, radial axis line on the
            theta=0 line corresponds to a line pointing right (like
            what mathematicians prefer). Defaults to the first
            `polar.sector` angle.
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to False.
        calendar
            Sets the calendar system to use for `range` and `tick0`
            if this is a date axis. This does not set the calendar
            for interpreting data on this axis, that's specified in
            the trace or via the global `layout.calendar`
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses "trace",
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to "array" to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            "trace" mode. The unspecified categories will follow
            the categories in `categoryarray`. Set `categoryorder`
            to *total ascending* or *total descending* if order
            should be determined by the numerical order of the
            values. Similarly, the order can be determined by the
            min, max, sum, mean or median of all the values.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to "log" and "date" axes. If the axis `type`
            is "log", then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. "log" has several special
            values; "L<f>", where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = "L0.5" will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use "D1" (all digits) or "D2"
            (only 2 and 5). `tick0` is ignored for "D1" and "D2".
            If the axis `type` is "date", then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            "date" also has special values "M<n>" gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to "2000-01-15" and `dtick` to "M3". To set
            ticks every 4 years, set `dtick` to "M48"
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            "none", it appears as 1,000,000,000. If "e", 1e+9. If
            "E", 1E+9. If "power", 1x10^9 (with 9 in a super
            script). If "SI", 1G. If "B", 1B.
        gridcolor
            Sets the color of the grid lines.
        gridwidth
            Sets the width (in px) of the grid lines.
        hoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        layer
            Sets the layer on which this axis is displayed. If
            *above traces*, this axis is displayed above all the
            subplot's traces If *below traces*, this axis is
            displayed below all the subplot's traces, but above the
            grid lines. Useful when used together with scatter-like
            traces with `cliponaxis` set to False to show markers
            and/or text nodes above this axis.
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        range
            Sets the range of this axis. If the axis `type` is
            "log", then you must take the log of your desired range
            (e.g. to set the range from 1 to 100, set the range
            from 0 to 2). If the axis `type` is "date", it should
            be date strings, like date data, though Date objects
            and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is "category", it should be
            numbers, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        rangemode
            If *tozero*`, the range extends to 0, regardless of the
            input data If "nonnegative", the range is non-negative,
            regardless of the input data. If "normal", the range is
            computed in relation to the extrema of the input data
            (same behavior as for cartesian axes).
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If "all", all exponents are shown besides their
            significands. If "first", only the exponent of the
            first tick is shown. If "last", only the exponent of
            the last tick is shown. If "none", no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            True, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        side
            Determines on which side of radial axis line the tick
            and tick labels appear.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is "log", then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is "date", it should be a date string, like
            date data. If the axis `type` is "category", it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.layout.polar.ra
            dialaxis.Tickformatstop` instances or dicts with
            compatible properties
        tickformatstopdefaults
            When used in a template (as layout.template.layout.pola
            r.radialaxis.tickformatstopdefaults), sets the default
            property values to use for elements of
            layout.polar.radialaxis.tickformatstops
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If "auto", the number
            of ticks is set via `nticks`. If "linear", the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` ("linear" is
            the default value if `tick0` and `dtick` are provided).
            If "array", the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. ("array" is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If "", this
            axis' ticks are not drawn. If "outside" ("inside"),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        title
            :class:`plotly.graph_objects.layout.polar.radialaxis.Ti
            tle` instance or dict with compatible properties
        titlefont
            Deprecated: Please use
            layout.polar.radialaxis.title.font instead. Sets this
            axis' title font. Note that the title's font used to be
            customized by the now deprecated `titlefont` attribute.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        uirevision
            Controls persistence of user-driven changes in axis
            `range`, `autorange`, `angle`, and `title` if in
            `editable: true` configuration. Defaults to
            `polar<N>.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false

        Returns
        -------
        RadialAxis
        """
        super(RadialAxis, self).__init__("radialaxis")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.polar.RadialAxis 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.polar.RadialAxis`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.polar import radialaxis as v_radialaxis

        # Initialize validators
        # ---------------------
        self._validators["angle"] = v_radialaxis.AngleValidator()
        self._validators["autorange"] = v_radialaxis.AutorangeValidator()
        self._validators["calendar"] = v_radialaxis.CalendarValidator()
        self._validators["categoryarray"] = v_radialaxis.CategoryarrayValidator()
        self._validators["categoryarraysrc"] = v_radialaxis.CategoryarraysrcValidator()
        self._validators["categoryorder"] = v_radialaxis.CategoryorderValidator()
        self._validators["color"] = v_radialaxis.ColorValidator()
        self._validators["dtick"] = v_radialaxis.DtickValidator()
        self._validators["exponentformat"] = v_radialaxis.ExponentformatValidator()
        self._validators["gridcolor"] = v_radialaxis.GridcolorValidator()
        self._validators["gridwidth"] = v_radialaxis.GridwidthValidator()
        self._validators["hoverformat"] = v_radialaxis.HoverformatValidator()
        self._validators["layer"] = v_radialaxis.LayerValidator()
        self._validators["linecolor"] = v_radialaxis.LinecolorValidator()
        self._validators["linewidth"] = v_radialaxis.LinewidthValidator()
        self._validators["nticks"] = v_radialaxis.NticksValidator()
        self._validators["range"] = v_radialaxis.RangeValidator()
        self._validators["rangemode"] = v_radialaxis.RangemodeValidator()
        self._validators[
            "separatethousands"
        ] = v_radialaxis.SeparatethousandsValidator()
        self._validators["showexponent"] = v_radialaxis.ShowexponentValidator()
        self._validators["showgrid"] = v_radialaxis.ShowgridValidator()
        self._validators["showline"] = v_radialaxis.ShowlineValidator()
        self._validators["showticklabels"] = v_radialaxis.ShowticklabelsValidator()
        self._validators["showtickprefix"] = v_radialaxis.ShowtickprefixValidator()
        self._validators["showticksuffix"] = v_radialaxis.ShowticksuffixValidator()
        self._validators["side"] = v_radialaxis.SideValidator()
        self._validators["tick0"] = v_radialaxis.Tick0Validator()
        self._validators["tickangle"] = v_radialaxis.TickangleValidator()
        self._validators["tickcolor"] = v_radialaxis.TickcolorValidator()
        self._validators["tickfont"] = v_radialaxis.TickfontValidator()
        self._validators["tickformat"] = v_radialaxis.TickformatValidator()
        self._validators["tickformatstops"] = v_radialaxis.TickformatstopsValidator()
        self._validators[
            "tickformatstopdefaults"
        ] = v_radialaxis.TickformatstopValidator()
        self._validators["ticklen"] = v_radialaxis.TicklenValidator()
        self._validators["tickmode"] = v_radialaxis.TickmodeValidator()
        self._validators["tickprefix"] = v_radialaxis.TickprefixValidator()
        self._validators["ticks"] = v_radialaxis.TicksValidator()
        self._validators["ticksuffix"] = v_radialaxis.TicksuffixValidator()
        self._validators["ticktext"] = v_radialaxis.TicktextValidator()
        self._validators["ticktextsrc"] = v_radialaxis.TicktextsrcValidator()
        self._validators["tickvals"] = v_radialaxis.TickvalsValidator()
        self._validators["tickvalssrc"] = v_radialaxis.TickvalssrcValidator()
        self._validators["tickwidth"] = v_radialaxis.TickwidthValidator()
        self._validators["title"] = v_radialaxis.TitleValidator()
        self._validators["type"] = v_radialaxis.TypeValidator()
        self._validators["uirevision"] = v_radialaxis.UirevisionValidator()
        self._validators["visible"] = v_radialaxis.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("angle", None)
        self["angle"] = angle if angle is not None else _v
        _v = arg.pop("autorange", None)
        self["autorange"] = autorange if autorange is not None else _v
        _v = arg.pop("calendar", None)
        self["calendar"] = calendar if calendar is not None else _v
        _v = arg.pop("categoryarray", None)
        self["categoryarray"] = categoryarray if categoryarray is not None else _v
        _v = arg.pop("categoryarraysrc", None)
        self["categoryarraysrc"] = (
            categoryarraysrc if categoryarraysrc is not None else _v
        )
        _v = arg.pop("categoryorder", None)
        self["categoryorder"] = categoryorder if categoryorder is not None else _v
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("dtick", None)
        self["dtick"] = dtick if dtick is not None else _v
        _v = arg.pop("exponentformat", None)
        self["exponentformat"] = exponentformat if exponentformat is not None else _v
        _v = arg.pop("gridcolor", None)
        self["gridcolor"] = gridcolor if gridcolor is not None else _v
        _v = arg.pop("gridwidth", None)
        self["gridwidth"] = gridwidth if gridwidth is not None else _v
        _v = arg.pop("hoverformat", None)
        self["hoverformat"] = hoverformat if hoverformat is not None else _v
        _v = arg.pop("layer", None)
        self["layer"] = layer if layer is not None else _v
        _v = arg.pop("linecolor", None)
        self["linecolor"] = linecolor if linecolor is not None else _v
        _v = arg.pop("linewidth", None)
        self["linewidth"] = linewidth if linewidth is not None else _v
        _v = arg.pop("nticks", None)
        self["nticks"] = nticks if nticks is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("rangemode", None)
        self["rangemode"] = rangemode if rangemode is not None else _v
        _v = arg.pop("separatethousands", None)
        self["separatethousands"] = (
            separatethousands if separatethousands is not None else _v
        )
        _v = arg.pop("showexponent", None)
        self["showexponent"] = showexponent if showexponent is not None else _v
        _v = arg.pop("showgrid", None)
        self["showgrid"] = showgrid if showgrid is not None else _v
        _v = arg.pop("showline", None)
        self["showline"] = showline if showline is not None else _v
        _v = arg.pop("showticklabels", None)
        self["showticklabels"] = showticklabels if showticklabels is not None else _v
        _v = arg.pop("showtickprefix", None)
        self["showtickprefix"] = showtickprefix if showtickprefix is not None else _v
        _v = arg.pop("showticksuffix", None)
        self["showticksuffix"] = showticksuffix if showticksuffix is not None else _v
        _v = arg.pop("side", None)
        self["side"] = side if side is not None else _v
        _v = arg.pop("tick0", None)
        self["tick0"] = tick0 if tick0 is not None else _v
        _v = arg.pop("tickangle", None)
        self["tickangle"] = tickangle if tickangle is not None else _v
        _v = arg.pop("tickcolor", None)
        self["tickcolor"] = tickcolor if tickcolor is not None else _v
        _v = arg.pop("tickfont", None)
        self["tickfont"] = tickfont if tickfont is not None else _v
        _v = arg.pop("tickformat", None)
        self["tickformat"] = tickformat if tickformat is not None else _v
        _v = arg.pop("tickformatstops", None)
        self["tickformatstops"] = tickformatstops if tickformatstops is not None else _v
        _v = arg.pop("tickformatstopdefaults", None)
        self["tickformatstopdefaults"] = (
            tickformatstopdefaults if tickformatstopdefaults is not None else _v
        )
        _v = arg.pop("ticklen", None)
        self["ticklen"] = ticklen if ticklen is not None else _v
        _v = arg.pop("tickmode", None)
        self["tickmode"] = tickmode if tickmode is not None else _v
        _v = arg.pop("tickprefix", None)
        self["tickprefix"] = tickprefix if tickprefix is not None else _v
        _v = arg.pop("ticks", None)
        self["ticks"] = ticks if ticks is not None else _v
        _v = arg.pop("ticksuffix", None)
        self["ticksuffix"] = ticksuffix if ticksuffix is not None else _v
        _v = arg.pop("ticktext", None)
        self["ticktext"] = ticktext if ticktext is not None else _v
        _v = arg.pop("ticktextsrc", None)
        self["ticktextsrc"] = ticktextsrc if ticktextsrc is not None else _v
        _v = arg.pop("tickvals", None)
        self["tickvals"] = tickvals if tickvals is not None else _v
        _v = arg.pop("tickvalssrc", None)
        self["tickvalssrc"] = tickvalssrc if tickvalssrc is not None else _v
        _v = arg.pop("tickwidth", None)
        self["tickwidth"] = tickwidth if tickwidth is not None else _v
        _v = arg.pop("title", None)
        self["title"] = title if title is not None else _v
        _v = arg.pop("titlefont", None)
        _v = titlefont if titlefont is not None else _v
        if _v is not None:
            self["titlefont"] = _v
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Domain(_BaseLayoutHierarchyType):

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this polar subplot .
    
        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["column"]

    @column.setter
    def column(self, val):
        self["column"] = val

    # row
    # ---
    @property
    def row(self):
        """
        If there is a layout grid, use the domain for this row in the
        grid for this polar subplot .
    
        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["row"]

    @row.setter
    def row(self, val):
        self["row"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this polar subplot (in plot
        fraction).
    
        The 'x' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this polar subplot (in plot
        fraction).
    
        The 'y' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.polar"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this polar subplot .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this polar subplot .
        x
            Sets the horizontal domain of this polar subplot (in
            plot fraction).
        y
            Sets the vertical domain of this polar subplot (in plot
            fraction).
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.polar.Domain`
        column
            If there is a layout grid, use the domain for this
            column in the grid for this polar subplot .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this polar subplot .
        x
            Sets the horizontal domain of this polar subplot (in
            plot fraction).
        y
            Sets the vertical domain of this polar subplot (in plot
            fraction).

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__("domain")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.polar.Domain 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.polar.Domain`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.polar import domain as v_domain

        # Initialize validators
        # ---------------------
        self._validators["column"] = v_domain.ColumnValidator()
        self._validators["row"] = v_domain.RowValidator()
        self._validators["x"] = v_domain.XValidator()
        self._validators["y"] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("column", None)
        self["column"] = column if column is not None else _v
        _v = arg.pop("row", None)
        self["row"] = row if row is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class AngularAxis(_BaseLayoutHierarchyType):

    # categoryarray
    # -------------
    @property
    def categoryarray(self):
        """
        Sets the order in which categories on this axis appear. Only
        has an effect if `categoryorder` is set to "array". Used with
        `categoryorder`.
    
        The 'categoryarray' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["categoryarray"]

    @categoryarray.setter
    def categoryarray(self, val):
        self["categoryarray"] = val

    # categoryarraysrc
    # ----------------
    @property
    def categoryarraysrc(self):
        """
        Sets the source reference on plot.ly for  categoryarray .
    
        The 'categoryarraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["categoryarraysrc"]

    @categoryarraysrc.setter
    def categoryarraysrc(self, val):
        self["categoryarraysrc"] = val

    # categoryorder
    # -------------
    @property
    def categoryorder(self):
        """
        Specifies the ordering logic for the case of categorical
        variables. By default, plotly uses "trace", which specifies the
        order that is present in the data supplied. Set `categoryorder`
        to *category ascending* or *category descending* if order
        should be determined by the alphanumerical order of the
        category names. Set `categoryorder` to "array" to derive the
        ordering from the attribute `categoryarray`. If a category is
        not found in the `categoryarray` array, the sorting behavior
        for that attribute will be identical to the "trace" mode. The
        unspecified categories will follow the categories in
        `categoryarray`. Set `categoryorder` to *total ascending* or
        *total descending* if order should be determined by the
        numerical order of the values. Similarly, the order can be
        determined by the min, max, sum, mean or median of all the
        values.
    
        The 'categoryorder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'category ascending', 'category descending',
                'array', 'total ascending', 'total descending', 'min
                ascending', 'min descending', 'max ascending', 'max
                descending', 'sum ascending', 'sum descending', 'mean
                ascending', 'mean descending', 'median ascending', 'median
                descending']

        Returns
        -------
        Any
        """
        return self["categoryorder"]

    @categoryorder.setter
    def categoryorder(self, val):
        self["categoryorder"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets default for all colors associated with this axis all at
        once: line, font, tick, and grid colors. Grid color is
        lightened by blending this with the plot background Individual
        pieces can override this.
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # direction
    # ---------
    @property
    def direction(self):
        """
        Sets the direction corresponding to positive angles.
    
        The 'direction' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['counterclockwise', 'clockwise']

        Returns
        -------
        Any
        """
        return self["direction"]

    @direction.setter
    def direction(self, val):
        self["direction"] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to
        "log" and "date" axes. If the axis `type` is "log", then ticks
        are set every 10^(n*dtick) where n is the tick number. For
        example, to set a tick mark at 1, 10, 100, 1000, ... set dtick
        to 1. To set tick marks at 1, 100, 10000, ... set dtick to 2.
        To set tick marks at 1, 5, 25, 125, 625, 3125, ... set dtick to
        log_10(5), or 0.69897000433. "log" has several special values;
        "L<f>", where `f` is a positive number, gives ticks linearly
        spaced in value (but not position). For example `tick0` = 0.1,
        `dtick` = "L0.5" will put ticks at 0.1, 0.6, 1.1, 1.6 etc. To
        show powers of 10 plus small digits between, use "D1" (all
        digits) or "D2" (only 2 and 5). `tick0` is ignored for "D1" and
        "D2". If the axis `type` is "date", then you must convert the
        time to milliseconds. For example, to set the interval between
        ticks to one day, set `dtick` to 86400000.0. "date" also has
        special values "M<n>" gives ticks spaced by a number of months.
        `n` must be a positive integer. To set ticks on the 15th of
        every third month, set `tick0` to "2000-01-15" and `dtick` to
        "M3". To set ticks every 4 years, set `dtick` to "M48"
    
        The 'dtick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["dtick"]

    @dtick.setter
    def dtick(self, val):
        self["dtick"] = val

    # exponentformat
    # --------------
    @property
    def exponentformat(self):
        """
        Determines a formatting rule for the tick exponents. For
        example, consider the number 1,000,000,000. If "none", it
        appears as 1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
        "power", 1x10^9 (with 9 in a super script). If "SI", 1G. If
        "B", 1B.
    
        The 'exponentformat' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'e', 'E', 'power', 'SI', 'B']

        Returns
        -------
        Any
        """
        return self["exponentformat"]

    @exponentformat.setter
    def exponentformat(self, val):
        self["exponentformat"] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the color of the grid lines.
    
        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["gridcolor"]

    @gridcolor.setter
    def gridcolor(self, val):
        self["gridcolor"] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the width (in px) of the grid lines.
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["gridwidth"]

    @gridwidth.setter
    def gridwidth(self, val):
        self["gridwidth"] = val

    # hoverformat
    # -----------
    @property
    def hoverformat(self):
        """
        Sets the hover text formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format And for dates
        see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Time-Formatting.md#format We add one item
        to d3's date formatter: "%{n}f" for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display "09~15~23.46"
    
        The 'hoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["hoverformat"]

    @hoverformat.setter
    def hoverformat(self, val):
        self["hoverformat"] = val

    # layer
    # -----
    @property
    def layer(self):
        """
        Sets the layer on which this axis is displayed. If *above
        traces*, this axis is displayed above all the subplot's traces
        If *below traces*, this axis is displayed below all the
        subplot's traces, but above the grid lines. Useful when used
        together with scatter-like traces with `cliponaxis` set to
        False to show markers and/or text nodes above this axis.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['above traces', 'below traces']

        Returns
        -------
        Any
        """
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    # linecolor
    # ---------
    @property
    def linecolor(self):
        """
        Sets the axis line color.
    
        The 'linecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["linecolor"]

    @linecolor.setter
    def linecolor(self, val):
        self["linecolor"] = val

    # linewidth
    # ---------
    @property
    def linewidth(self):
        """
        Sets the width (in px) of the axis line.
    
        The 'linewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["linewidth"]

    @linewidth.setter
    def linewidth(self, val):
        self["linewidth"] = val

    # nticks
    # ------
    @property
    def nticks(self):
        """
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to "auto".
    
        The 'nticks' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["nticks"]

    @nticks.setter
    def nticks(self, val):
        self["nticks"] = val

    # period
    # ------
    @property
    def period(self):
        """
        Set the angular period. Has an effect only when
        `angularaxis.type` is "category".
    
        The 'period' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["period"]

    @period.setter
    def period(self, val):
        self["period"] = val

    # rotation
    # --------
    @property
    def rotation(self):
        """
        Sets that start position (in degrees) of the angular axis By
        default, polar subplots with `direction` set to
        "counterclockwise" get a `rotation` of 0 which corresponds to
        due East (like what mathematicians prefer). In turn, polar with
        `direction` set to "clockwise" get a rotation of 90 which
        corresponds to due North (like on a compass),
    
        The 'rotation' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["rotation"]

    @rotation.setter
    def rotation(self, val):
        self["rotation"] = val

    # separatethousands
    # -----------------
    @property
    def separatethousands(self):
        """
        If "true", even 4-digit integers are separated
    
        The 'separatethousands' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["separatethousands"]

    @separatethousands.setter
    def separatethousands(self, val):
        self["separatethousands"] = val

    # showexponent
    # ------------
    @property
    def showexponent(self):
        """
        If "all", all exponents are shown besides their significands.
        If "first", only the exponent of the first tick is shown. If
        "last", only the exponent of the last tick is shown. If "none",
        no exponents appear.
    
        The 'showexponent' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self["showexponent"]

    @showexponent.setter
    def showexponent(self, val):
        self["showexponent"] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Determines whether or not grid lines are drawn. If True, the
        grid lines are drawn at every tick mark.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showgrid"]

    @showgrid.setter
    def showgrid(self, val):
        self["showgrid"] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Determines whether or not a line bounding this axis is drawn.
    
        The 'showline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showline"]

    @showline.setter
    def showline(self, val):
        self["showline"] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether or not the tick labels are drawn.
    
        The 'showticklabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showticklabels"]

    @showticklabels.setter
    def showticklabels(self, val):
        self["showticklabels"] = val

    # showtickprefix
    # --------------
    @property
    def showtickprefix(self):
        """
        If "all", all tick labels are displayed with a prefix. If
        "first", only the first tick is displayed with a prefix. If
        "last", only the last tick is displayed with a suffix. If
        "none", tick prefixes are hidden.
    
        The 'showtickprefix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self["showtickprefix"]

    @showtickprefix.setter
    def showtickprefix(self, val):
        self["showtickprefix"] = val

    # showticksuffix
    # --------------
    @property
    def showticksuffix(self):
        """
        Same as `showtickprefix` but for tick suffixes.
    
        The 'showticksuffix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self["showticksuffix"]

    @showticksuffix.setter
    def showticksuffix(self, val):
        self["showticksuffix"] = val

    # thetaunit
    # ---------
    @property
    def thetaunit(self):
        """
        Sets the format unit of the formatted "theta" values. Has an
        effect only when `angularaxis.type` is "linear".
    
        The 'thetaunit' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['radians', 'degrees']

        Returns
        -------
        Any
        """
        return self["thetaunit"]

    @thetaunit.setter
    def thetaunit(self, val):
        self["thetaunit"] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the placement of the first tick on this axis. Use with
        `dtick`. If the axis `type` is "log", then you must take the
        log of your starting tick (e.g. to set the starting tick to
        100, set the `tick0` to 2) except when `dtick`=*L<f>* (see
        `dtick` for more info). If the axis `type` is "date", it should
        be a date string, like date data. If the axis `type` is
        "category", it should be a number, using the scale where each
        category is assigned a serial number from zero in the order it
        appears.
    
        The 'tick0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["tick0"]

    @tick0.setter
    def tick0(self, val):
        self["tick0"] = val

    # tickangle
    # ---------
    @property
    def tickangle(self):
        """
        Sets the angle of the tick labels with respect to the
        horizontal. For example, a `tickangle` of -90 draws the tick
        labels vertically.
    
        The 'tickangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["tickangle"]

    @tickangle.setter
    def tickangle(self, val):
        self["tickangle"] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the tick color.
    
        The 'tickcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["tickcolor"]

    @tickcolor.setter
    def tickcolor(self, val):
        self["tickcolor"] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the tick font.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.angularaxis.Tickfont`
          - A dict of string/value properties that will be passed
            to the Tickfont constructor
    
            Supported dict properties:
                
                color
    
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

        Returns
        -------
        plotly.graph_objs.layout.polar.angularaxis.Tickfont
        """
        return self["tickfont"]

    @tickfont.setter
    def tickfont(self, val):
        self["tickfont"] = val

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format And for dates
        see: https://github.com/d3/d3-3.x-api-
        reference/blob/master/Time-Formatting.md#format We add one item
        to d3's date formatter: "%{n}f" for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display "09~15~23.46"
    
        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["tickformat"]

    @tickformat.setter
    def tickformat(self, val):
        self["tickformat"] = val

    # tickformatstops
    # ---------------
    @property
    def tickformatstops(self):
        """
        The 'tickformatstops' property is a tuple of instances of
        Tickformatstop that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.polar.angularaxis.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor
    
            Supported dict properties:
                
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

        Returns
        -------
        tuple[plotly.graph_objs.layout.polar.angularaxis.Tickformatstop]
        """
        return self["tickformatstops"]

    @tickformatstops.setter
    def tickformatstops(self, val):
        self["tickformatstops"] = val

    # tickformatstopdefaults
    # ----------------------
    @property
    def tickformatstopdefaults(self):
        """
        When used in a template (as layout.template.layout.polar.angula
        raxis.tickformatstopdefaults), sets the default property values
        to use for elements of layout.polar.angularaxis.tickformatstops
    
        The 'tickformatstopdefaults' property is an instance of Tickformatstop
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.polar.angularaxis.Tickformatstop`
          - A dict of string/value properties that will be passed
            to the Tickformatstop constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.polar.angularaxis.Tickformatstop
        """
        return self["tickformatstopdefaults"]

    @tickformatstopdefaults.setter
    def tickformatstopdefaults(self, val):
        self["tickformatstopdefaults"] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the tick length (in px).
    
        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["ticklen"]

    @ticklen.setter
    def ticklen(self, val):
        self["ticklen"] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        Sets the tick mode for this axis. If "auto", the number of
        ticks is set via `nticks`. If "linear", the placement of the
        ticks is determined by a starting position `tick0` and a tick
        step `dtick` ("linear" is the default value if `tick0` and
        `dtick` are provided). If "array", the placement of the ticks
        is set via `tickvals` and the tick text is `ticktext`. ("array"
        is the default value if `tickvals` is provided).
    
        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'linear', 'array']

        Returns
        -------
        Any
        """
        return self["tickmode"]

    @tickmode.setter
    def tickmode(self, val):
        self["tickmode"] = val

    # tickprefix
    # ----------
    @property
    def tickprefix(self):
        """
        Sets a tick label prefix.
    
        The 'tickprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["tickprefix"]

    @tickprefix.setter
    def tickprefix(self, val):
        self["tickprefix"] = val

    # ticks
    # -----
    @property
    def ticks(self):
        """
        Determines whether ticks are drawn or not. If "", this axis'
        ticks are not drawn. If "outside" ("inside"), this axis' are
        drawn outside (inside) the axis lines.
    
        The 'ticks' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['outside', 'inside', '']

        Returns
        -------
        Any
        """
        return self["ticks"]

    @ticks.setter
    def ticks(self, val):
        self["ticks"] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Sets a tick label suffix.
    
        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["ticksuffix"]

    @ticksuffix.setter
    def ticksuffix(self, val):
        self["ticksuffix"] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to "array". Used with
        `tickvals`.
    
        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["ticktext"]

    @ticktext.setter
    def ticktext(self, val):
        self["ticktext"] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on plot.ly for  ticktext .
    
        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ticktextsrc"]

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self["ticktextsrc"] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to "array". Used with `ticktext`.
    
        The 'tickvals' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["tickvals"]

    @tickvals.setter
    def tickvals(self, val):
        self["tickvals"] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on plot.ly for  tickvals .
    
        The 'tickvalssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["tickvalssrc"]

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self["tickvalssrc"] = val

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the tick width (in px).
    
        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["tickwidth"]

    @tickwidth.setter
    def tickwidth(self, val):
        self["tickwidth"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the angular axis type. If "linear", set `thetaunit` to
        determine the unit in which axis value are shown. If *category,
        use `period` to set the number of integer coordinates around
        polar axis.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['-', 'linear', 'category']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in axis `rotation`.
        Defaults to `polar<N>.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        A single toggle to hide the axis while preserving interaction
        like dragging. Default is true when a cheater plot is present
        on the axis, otherwise false
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.polar"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses "trace",
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to "array" to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            "trace" mode. The unspecified categories will follow
            the categories in `categoryarray`. Set `categoryorder`
            to *total ascending* or *total descending* if order
            should be determined by the numerical order of the
            values. Similarly, the order can be determined by the
            min, max, sum, mean or median of all the values.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        direction
            Sets the direction corresponding to positive angles.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to "log" and "date" axes. If the axis `type`
            is "log", then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. "log" has several special
            values; "L<f>", where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = "L0.5" will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use "D1" (all digits) or "D2"
            (only 2 and 5). `tick0` is ignored for "D1" and "D2".
            If the axis `type` is "date", then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            "date" also has special values "M<n>" gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to "2000-01-15" and `dtick` to "M3". To set
            ticks every 4 years, set `dtick` to "M48"
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            "none", it appears as 1,000,000,000. If "e", 1e+9. If
            "E", 1E+9. If "power", 1x10^9 (with 9 in a super
            script). If "SI", 1G. If "B", 1B.
        gridcolor
            Sets the color of the grid lines.
        gridwidth
            Sets the width (in px) of the grid lines.
        hoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        layer
            Sets the layer on which this axis is displayed. If
            *above traces*, this axis is displayed above all the
            subplot's traces If *below traces*, this axis is
            displayed below all the subplot's traces, but above the
            grid lines. Useful when used together with scatter-like
            traces with `cliponaxis` set to False to show markers
            and/or text nodes above this axis.
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        period
            Set the angular period. Has an effect only when
            `angularaxis.type` is "category".
        rotation
            Sets that start position (in degrees) of the angular
            axis By default, polar subplots with `direction` set to
            "counterclockwise" get a `rotation` of 0 which
            corresponds to due East (like what mathematicians
            prefer). In turn, polar with `direction` set to
            "clockwise" get a rotation of 90 which corresponds to
            due North (like on a compass),
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If "all", all exponents are shown besides their
            significands. If "first", only the exponent of the
            first tick is shown. If "last", only the exponent of
            the last tick is shown. If "none", no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            True, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        thetaunit
            Sets the format unit of the formatted "theta" values.
            Has an effect only when `angularaxis.type` is "linear".
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is "log", then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is "date", it should be a date string, like
            date data. If the axis `type` is "category", it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.layout.polar.an
            gularaxis.Tickformatstop` instances or dicts with
            compatible properties
        tickformatstopdefaults
            When used in a template (as layout.template.layout.pola
            r.angularaxis.tickformatstopdefaults), sets the default
            property values to use for elements of
            layout.polar.angularaxis.tickformatstops
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If "auto", the number
            of ticks is set via `nticks`. If "linear", the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` ("linear" is
            the default value if `tick0` and `dtick` are provided).
            If "array", the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. ("array" is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If "", this
            axis' ticks are not drawn. If "outside" ("inside"),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        type
            Sets the angular axis type. If "linear", set
            `thetaunit` to determine the unit in which axis value
            are shown. If *category, use `period` to set the number
            of integer coordinates around polar axis.
        uirevision
            Controls persistence of user-driven changes in axis
            `rotation`. Defaults to `polar<N>.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        """

    def __init__(
        self,
        arg=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        direction=None,
        dtick=None,
        exponentformat=None,
        gridcolor=None,
        gridwidth=None,
        hoverformat=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        nticks=None,
        period=None,
        rotation=None,
        separatethousands=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        thetaunit=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        tickformatstopdefaults=None,
        ticklen=None,
        tickmode=None,
        tickprefix=None,
        ticks=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,
        type=None,
        uirevision=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new AngularAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.polar.AngularAxis`
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses "trace",
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to "array" to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            "trace" mode. The unspecified categories will follow
            the categories in `categoryarray`. Set `categoryorder`
            to *total ascending* or *total descending* if order
            should be determined by the numerical order of the
            values. Similarly, the order can be determined by the
            min, max, sum, mean or median of all the values.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        direction
            Sets the direction corresponding to positive angles.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to "log" and "date" axes. If the axis `type`
            is "log", then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. "log" has several special
            values; "L<f>", where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = "L0.5" will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use "D1" (all digits) or "D2"
            (only 2 and 5). `tick0` is ignored for "D1" and "D2".
            If the axis `type` is "date", then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            "date" also has special values "M<n>" gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to "2000-01-15" and `dtick` to "M3". To set
            ticks every 4 years, set `dtick` to "M48"
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            "none", it appears as 1,000,000,000. If "e", 1e+9. If
            "E", 1E+9. If "power", 1x10^9 (with 9 in a super
            script). If "SI", 1G. If "B", 1B.
        gridcolor
            Sets the color of the grid lines.
        gridwidth
            Sets the width (in px) of the grid lines.
        hoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        layer
            Sets the layer on which this axis is displayed. If
            *above traces*, this axis is displayed above all the
            subplot's traces If *below traces*, this axis is
            displayed below all the subplot's traces, but above the
            grid lines. Useful when used together with scatter-like
            traces with `cliponaxis` set to False to show markers
            and/or text nodes above this axis.
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        period
            Set the angular period. Has an effect only when
            `angularaxis.type` is "category".
        rotation
            Sets that start position (in degrees) of the angular
            axis By default, polar subplots with `direction` set to
            "counterclockwise" get a `rotation` of 0 which
            corresponds to due East (like what mathematicians
            prefer). In turn, polar with `direction` set to
            "clockwise" get a rotation of 90 which corresponds to
            due North (like on a compass),
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If "all", all exponents are shown besides their
            significands. If "first", only the exponent of the
            first tick is shown. If "last", only the exponent of
            the last tick is shown. If "none", no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            True, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        thetaunit
            Sets the format unit of the formatted "theta" values.
            Has an effect only when `angularaxis.type` is "linear".
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is "log", then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is "date", it should be a date string, like
            date data. If the axis `type` is "category", it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format And for
            dates see: https://github.com/d3/d3-3.x-api-
            reference/blob/master/Time-Formatting.md#format We add
            one item to d3's date formatter: "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.layout.polar.an
            gularaxis.Tickformatstop` instances or dicts with
            compatible properties
        tickformatstopdefaults
            When used in a template (as layout.template.layout.pola
            r.angularaxis.tickformatstopdefaults), sets the default
            property values to use for elements of
            layout.polar.angularaxis.tickformatstops
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If "auto", the number
            of ticks is set via `nticks`. If "linear", the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` ("linear" is
            the default value if `tick0` and `dtick` are provided).
            If "array", the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. ("array" is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If "", this
            axis' ticks are not drawn. If "outside" ("inside"),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        type
            Sets the angular axis type. If "linear", set
            `thetaunit` to determine the unit in which axis value
            are shown. If *category, use `period` to set the number
            of integer coordinates around polar axis.
        uirevision
            Controls persistence of user-driven changes in axis
            `rotation`. Defaults to `polar<N>.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false

        Returns
        -------
        AngularAxis
        """
        super(AngularAxis, self).__init__("angularaxis")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.polar.AngularAxis 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.polar.AngularAxis`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.polar import angularaxis as v_angularaxis

        # Initialize validators
        # ---------------------
        self._validators["categoryarray"] = v_angularaxis.CategoryarrayValidator()
        self._validators["categoryarraysrc"] = v_angularaxis.CategoryarraysrcValidator()
        self._validators["categoryorder"] = v_angularaxis.CategoryorderValidator()
        self._validators["color"] = v_angularaxis.ColorValidator()
        self._validators["direction"] = v_angularaxis.DirectionValidator()
        self._validators["dtick"] = v_angularaxis.DtickValidator()
        self._validators["exponentformat"] = v_angularaxis.ExponentformatValidator()
        self._validators["gridcolor"] = v_angularaxis.GridcolorValidator()
        self._validators["gridwidth"] = v_angularaxis.GridwidthValidator()
        self._validators["hoverformat"] = v_angularaxis.HoverformatValidator()
        self._validators["layer"] = v_angularaxis.LayerValidator()
        self._validators["linecolor"] = v_angularaxis.LinecolorValidator()
        self._validators["linewidth"] = v_angularaxis.LinewidthValidator()
        self._validators["nticks"] = v_angularaxis.NticksValidator()
        self._validators["period"] = v_angularaxis.PeriodValidator()
        self._validators["rotation"] = v_angularaxis.RotationValidator()
        self._validators[
            "separatethousands"
        ] = v_angularaxis.SeparatethousandsValidator()
        self._validators["showexponent"] = v_angularaxis.ShowexponentValidator()
        self._validators["showgrid"] = v_angularaxis.ShowgridValidator()
        self._validators["showline"] = v_angularaxis.ShowlineValidator()
        self._validators["showticklabels"] = v_angularaxis.ShowticklabelsValidator()
        self._validators["showtickprefix"] = v_angularaxis.ShowtickprefixValidator()
        self._validators["showticksuffix"] = v_angularaxis.ShowticksuffixValidator()
        self._validators["thetaunit"] = v_angularaxis.ThetaunitValidator()
        self._validators["tick0"] = v_angularaxis.Tick0Validator()
        self._validators["tickangle"] = v_angularaxis.TickangleValidator()
        self._validators["tickcolor"] = v_angularaxis.TickcolorValidator()
        self._validators["tickfont"] = v_angularaxis.TickfontValidator()
        self._validators["tickformat"] = v_angularaxis.TickformatValidator()
        self._validators["tickformatstops"] = v_angularaxis.TickformatstopsValidator()
        self._validators[
            "tickformatstopdefaults"
        ] = v_angularaxis.TickformatstopValidator()
        self._validators["ticklen"] = v_angularaxis.TicklenValidator()
        self._validators["tickmode"] = v_angularaxis.TickmodeValidator()
        self._validators["tickprefix"] = v_angularaxis.TickprefixValidator()
        self._validators["ticks"] = v_angularaxis.TicksValidator()
        self._validators["ticksuffix"] = v_angularaxis.TicksuffixValidator()
        self._validators["ticktext"] = v_angularaxis.TicktextValidator()
        self._validators["ticktextsrc"] = v_angularaxis.TicktextsrcValidator()
        self._validators["tickvals"] = v_angularaxis.TickvalsValidator()
        self._validators["tickvalssrc"] = v_angularaxis.TickvalssrcValidator()
        self._validators["tickwidth"] = v_angularaxis.TickwidthValidator()
        self._validators["type"] = v_angularaxis.TypeValidator()
        self._validators["uirevision"] = v_angularaxis.UirevisionValidator()
        self._validators["visible"] = v_angularaxis.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("categoryarray", None)
        self["categoryarray"] = categoryarray if categoryarray is not None else _v
        _v = arg.pop("categoryarraysrc", None)
        self["categoryarraysrc"] = (
            categoryarraysrc if categoryarraysrc is not None else _v
        )
        _v = arg.pop("categoryorder", None)
        self["categoryorder"] = categoryorder if categoryorder is not None else _v
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("direction", None)
        self["direction"] = direction if direction is not None else _v
        _v = arg.pop("dtick", None)
        self["dtick"] = dtick if dtick is not None else _v
        _v = arg.pop("exponentformat", None)
        self["exponentformat"] = exponentformat if exponentformat is not None else _v
        _v = arg.pop("gridcolor", None)
        self["gridcolor"] = gridcolor if gridcolor is not None else _v
        _v = arg.pop("gridwidth", None)
        self["gridwidth"] = gridwidth if gridwidth is not None else _v
        _v = arg.pop("hoverformat", None)
        self["hoverformat"] = hoverformat if hoverformat is not None else _v
        _v = arg.pop("layer", None)
        self["layer"] = layer if layer is not None else _v
        _v = arg.pop("linecolor", None)
        self["linecolor"] = linecolor if linecolor is not None else _v
        _v = arg.pop("linewidth", None)
        self["linewidth"] = linewidth if linewidth is not None else _v
        _v = arg.pop("nticks", None)
        self["nticks"] = nticks if nticks is not None else _v
        _v = arg.pop("period", None)
        self["period"] = period if period is not None else _v
        _v = arg.pop("rotation", None)
        self["rotation"] = rotation if rotation is not None else _v
        _v = arg.pop("separatethousands", None)
        self["separatethousands"] = (
            separatethousands if separatethousands is not None else _v
        )
        _v = arg.pop("showexponent", None)
        self["showexponent"] = showexponent if showexponent is not None else _v
        _v = arg.pop("showgrid", None)
        self["showgrid"] = showgrid if showgrid is not None else _v
        _v = arg.pop("showline", None)
        self["showline"] = showline if showline is not None else _v
        _v = arg.pop("showticklabels", None)
        self["showticklabels"] = showticklabels if showticklabels is not None else _v
        _v = arg.pop("showtickprefix", None)
        self["showtickprefix"] = showtickprefix if showtickprefix is not None else _v
        _v = arg.pop("showticksuffix", None)
        self["showticksuffix"] = showticksuffix if showticksuffix is not None else _v
        _v = arg.pop("thetaunit", None)
        self["thetaunit"] = thetaunit if thetaunit is not None else _v
        _v = arg.pop("tick0", None)
        self["tick0"] = tick0 if tick0 is not None else _v
        _v = arg.pop("tickangle", None)
        self["tickangle"] = tickangle if tickangle is not None else _v
        _v = arg.pop("tickcolor", None)
        self["tickcolor"] = tickcolor if tickcolor is not None else _v
        _v = arg.pop("tickfont", None)
        self["tickfont"] = tickfont if tickfont is not None else _v
        _v = arg.pop("tickformat", None)
        self["tickformat"] = tickformat if tickformat is not None else _v
        _v = arg.pop("tickformatstops", None)
        self["tickformatstops"] = tickformatstops if tickformatstops is not None else _v
        _v = arg.pop("tickformatstopdefaults", None)
        self["tickformatstopdefaults"] = (
            tickformatstopdefaults if tickformatstopdefaults is not None else _v
        )
        _v = arg.pop("ticklen", None)
        self["ticklen"] = ticklen if ticklen is not None else _v
        _v = arg.pop("tickmode", None)
        self["tickmode"] = tickmode if tickmode is not None else _v
        _v = arg.pop("tickprefix", None)
        self["tickprefix"] = tickprefix if tickprefix is not None else _v
        _v = arg.pop("ticks", None)
        self["ticks"] = ticks if ticks is not None else _v
        _v = arg.pop("ticksuffix", None)
        self["ticksuffix"] = ticksuffix if ticksuffix is not None else _v
        _v = arg.pop("ticktext", None)
        self["ticktext"] = ticktext if ticktext is not None else _v
        _v = arg.pop("ticktextsrc", None)
        self["ticktextsrc"] = ticktextsrc if ticktextsrc is not None else _v
        _v = arg.pop("tickvals", None)
        self["tickvals"] = tickvals if tickvals is not None else _v
        _v = arg.pop("tickvalssrc", None)
        self["tickvalssrc"] = tickvalssrc if tickvalssrc is not None else _v
        _v = arg.pop("tickwidth", None)
        self["tickwidth"] = tickwidth if tickwidth is not None else _v
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = ["AngularAxis", "Domain", "RadialAxis", "angularaxis", "radialaxis"]

from plotly.graph_objs.layout.polar import radialaxis
from plotly.graph_objs.layout.polar import angularaxis
