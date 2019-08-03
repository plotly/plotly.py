from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class YAxis(_BaseLayoutHierarchyType):

    # anchor
    # ------
    @property
    def anchor(self):
        """
        If set to an opposite-letter axis id (e.g. `x2`, `y`), this
        axis is bound to the corresponding opposite-letter axis. If set
        to "free", this axis' position is determined by `position`.
    
        The 'anchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['free']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["anchor"]

    @anchor.setter
    def anchor(self, val):
        self["anchor"] = val

    # automargin
    # ----------
    @property
    def automargin(self):
        """
        Determines whether long tick labels automatically grow the
        figure margins.
    
        The 'automargin' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["automargin"]

    @automargin.setter
    def automargin(self, val):
        self["automargin"] = val

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

    # constrain
    # ---------
    @property
    def constrain(self):
        """
        If this axis needs to be compressed (either due to its own
        `scaleanchor` and `scaleratio` or those of the other axis),
        determines how that happens: by increasing the "range"
        (default), or by decreasing the "domain".
    
        The 'constrain' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['range', 'domain']

        Returns
        -------
        Any
        """
        return self["constrain"]

    @constrain.setter
    def constrain(self, val):
        self["constrain"] = val

    # constraintoward
    # ---------------
    @property
    def constraintoward(self):
        """
        If this axis needs to be compressed (either due to its own
        `scaleanchor` and `scaleratio` or those of the other axis),
        determines which direction we push the originally specified
        plot area. Options are "left", "center" (default), and "right"
        for x axes, and "top", "middle" (default), and "bottom" for y
        axes.
    
        The 'constraintoward' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["constraintoward"]

    @constraintoward.setter
    def constraintoward(self, val):
        self["constraintoward"] = val

    # dividercolor
    # ------------
    @property
    def dividercolor(self):
        """
        Sets the color of the dividers Only has an effect on
        "multicategory" axes.
    
        The 'dividercolor' property is a color and may be specified as:
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
        return self["dividercolor"]

    @dividercolor.setter
    def dividercolor(self, val):
        self["dividercolor"] = val

    # dividerwidth
    # ------------
    @property
    def dividerwidth(self):
        """
        Sets the width (in px) of the dividers Only has an effect on
        "multicategory" axes.
    
        The 'dividerwidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dividerwidth"]

    @dividerwidth.setter
    def dividerwidth(self, val):
        self["dividerwidth"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        Sets the domain of this axis (in plot fraction).
    
        The 'domain' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'domain[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'domain[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

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

    # fixedrange
    # ----------
    @property
    def fixedrange(self):
        """
        Determines whether or not this axis is zoom-able. If true, then
        zoom is disabled.
    
        The 'fixedrange' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["fixedrange"]

    @fixedrange.setter
    def fixedrange(self, val):
        self["fixedrange"] = val

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

    # matches
    # -------
    @property
    def matches(self):
        """
        If set to another axis id (e.g. `x2`, `y`), the range of this
        axis will match the range of the corresponding axis in data-
        coordinates space. Moreover, matching axes share auto-range
        values, category lists and histogram auto-bins. Note that
        setting axes simultaneously in both a `scaleanchor` and a
        `matches` constraint is currently forbidden. Moreover, note
        that matching axes must have the same `type`.
    
        The 'matches' property is an enumeration that may be specified as:
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["matches"]

    @matches.setter
    def matches(self, val):
        self["matches"] = val

    # mirror
    # ------
    @property
    def mirror(self):
        """
        Determines if the axis lines or/and ticks are mirrored to the
        opposite side of the plotting area. If True, the axis lines are
        mirrored. If "ticks", the axis lines and ticks are mirrored. If
        False, mirroring is disable. If "all", axis lines are mirrored
        on all shared-axes subplots. If "allticks", axis lines and
        ticks are mirrored on all shared-axes subplots.
    
        The 'mirror' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, 'ticks', False, 'all', 'allticks']

        Returns
        -------
        Any
        """
        return self["mirror"]

    @mirror.setter
    def mirror(self, val):
        self["mirror"] = val

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

    # overlaying
    # ----------
    @property
    def overlaying(self):
        """
        If set a same-letter axis id, this axis is overlaid on top of
        the corresponding same-letter axis, with traces and axes
        visible for both axes. If False, this axis does not overlay any
        same-letter axes. In this case, for axes with overlapping
        domains only the highest-numbered axis will be visible.
    
        The 'overlaying' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['free']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["overlaying"]

    @overlaying.setter
    def overlaying(self, val):
        self["overlaying"] = val

    # position
    # --------
    @property
    def position(self):
        """
        Sets the position of this axis in the plotting space (in
        normalized coordinates). Only has an effect if `anchor` is set
        to "free".
    
        The 'position' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

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
        If "normal", the range is computed in relation to the extrema
        of the input data. If *tozero*`, the range extends to 0,
        regardless of the input data If "nonnegative", the range is
        non-negative, regardless of the input data. Applies only to
        linear axes.
    
        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'tozero', 'nonnegative']

        Returns
        -------
        Any
        """
        return self["rangemode"]

    @rangemode.setter
    def rangemode(self, val):
        self["rangemode"] = val

    # scaleanchor
    # -----------
    @property
    def scaleanchor(self):
        """
        If set to another axis id (e.g. `x2`, `y`), the range of this
        axis changes together with the range of the corresponding axis
        such that the scale of pixels per unit is in a constant ratio.
        Both axes are still zoomable, but when you zoom one, the other
        will zoom the same amount, keeping a fixed midpoint.
        `constrain` and `constraintoward` determine how we enforce the
        constraint. You can chain these, ie `yaxis: {scaleanchor: *x*},
        xaxis2: {scaleanchor: *y*}` but you can only link axes of the
        same `type`. The linked axis can have the opposite letter (to
        constrain the aspect ratio) or the same letter (to match scales
        across subplots). Loops (`yaxis: {scaleanchor: *x*}, xaxis:
        {scaleanchor: *y*}` or longer) are redundant and the last
        constraint encountered will be ignored to avoid possible
        inconsistent constraints via `scaleratio`. Note that setting
        axes simultaneously in both a `scaleanchor` and a `matches`
        constraint is currently forbidden.
    
        The 'scaleanchor' property is an enumeration that may be specified as:
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["scaleanchor"]

    @scaleanchor.setter
    def scaleanchor(self, val):
        self["scaleanchor"] = val

    # scaleratio
    # ----------
    @property
    def scaleratio(self):
        """
        If this axis is linked to another by `scaleanchor`, this
        determines the pixel to unit scale ratio. For example, if this
        value is 10, then every unit on this axis spans 10 times the
        number of pixels as a unit on the linked axis. Use this for
        example to create an elevation profile where the vertical scale
        is exaggerated a fixed amount with respect to the horizontal.
    
        The 'scaleratio' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["scaleratio"]

    @scaleratio.setter
    def scaleratio(self, val):
        self["scaleratio"] = val

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

    # showdividers
    # ------------
    @property
    def showdividers(self):
        """
        Determines whether or not a dividers are drawn between the
        category levels of this axis. Only has an effect on
        "multicategory" axes.
    
        The 'showdividers' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showdividers"]

    @showdividers.setter
    def showdividers(self, val):
        self["showdividers"] = val

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

    # showspikes
    # ----------
    @property
    def showspikes(self):
        """
        Determines whether or not spikes (aka droplines) are drawn for
        this axis. Note: This only takes affect when hovermode =
        closest
    
        The 'showspikes' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showspikes"]

    @showspikes.setter
    def showspikes(self, val):
        self["showspikes"] = val

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
        Determines whether a x (y) axis is positioned at the "bottom"
        ("left") or "top" ("right") of the plotting area.
    
        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'bottom', 'left', 'right']

        Returns
        -------
        Any
        """
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    # spikecolor
    # ----------
    @property
    def spikecolor(self):
        """
        Sets the spike color. If undefined, will use the series color
    
        The 'spikecolor' property is a color and may be specified as:
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
        return self["spikecolor"]

    @spikecolor.setter
    def spikecolor(self, val):
        self["spikecolor"] = val

    # spikedash
    # ---------
    @property
    def spikedash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").
    
        The 'spikedash' property is a string and must be specified as:
          - One of the following strings:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot',
                'longdashdot']
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["spikedash"]

    @spikedash.setter
    def spikedash(self, val):
        self["spikedash"] = val

    # spikemode
    # ---------
    @property
    def spikemode(self):
        """
        Determines the drawing mode for the spike line If "toaxis", the
        line is drawn from the data point to the axis the  series is
        plotted on. If "across", the line is drawn across the entire
        plot area, and supercedes "toaxis". If "marker", then a marker
        dot is drawn on the axis the series is plotted on
    
        The 'spikemode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['toaxis', 'across', 'marker'] joined with '+' characters
            (e.g. 'toaxis+across')

        Returns
        -------
        Any
        """
        return self["spikemode"]

    @spikemode.setter
    def spikemode(self, val):
        self["spikemode"] = val

    # spikesnap
    # ---------
    @property
    def spikesnap(self):
        """
        Determines whether spikelines are stuck to the cursor or to the
        closest datapoints.
    
        The 'spikesnap' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['data', 'cursor']

        Returns
        -------
        Any
        """
        return self["spikesnap"]

    @spikesnap.setter
    def spikesnap(self, val):
        self["spikesnap"] = val

    # spikethickness
    # --------------
    @property
    def spikethickness(self):
        """
        Sets the width (in px) of the zero line.
    
        The 'spikethickness' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["spikethickness"]

    @spikethickness.setter
    def spikethickness(self, val):
        self["spikethickness"] = val

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
          - An instance of plotly.graph_objs.layout.yaxis.Tickfont
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
        plotly.graph_objs.layout.yaxis.Tickfont
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
          - A list or tuple of instances of plotly.graph_objs.layout.yaxis.Tickformatstop
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
        tuple[plotly.graph_objs.layout.yaxis.Tickformatstop]
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
        When used in a template (as
        layout.template.layout.yaxis.tickformatstopdefaults), sets the
        default property values to use for elements of
        layout.yaxis.tickformatstops
    
        The 'tickformatstopdefaults' property is an instance of Tickformatstop
        that may be specified as:
          - An instance of plotly.graph_objs.layout.yaxis.Tickformatstop
          - A dict of string/value properties that will be passed
            to the Tickformatstop constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.yaxis.Tickformatstop
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

    # tickson
    # -------
    @property
    def tickson(self):
        """
        Determines where ticks and grid lines are drawn with respect to
        their corresponding tick labels. Only has an effect for axes of
        `type` "category" or "multicategory". When set to "boundaries",
        ticks and grid lines are drawn half a category to the
        left/bottom of labels.
    
        The 'tickson' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['labels', 'boundaries']

        Returns
        -------
        Any
        """
        return self["tickson"]

    @tickson.setter
    def tickson(self, val):
        self["tickson"] = val

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
          - An instance of plotly.graph_objs.layout.yaxis.Title
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
        plotly.graph_objs.layout.yaxis.Title
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
        Deprecated: Please use layout.yaxis.title.font instead. Sets
        this axis' title font. Note that the title's font used to be
        customized by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.yaxis.title.Font
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
                ['-', 'linear', 'log', 'date', 'category',
                'multicategory']

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
        `autorange`, and `title` if in `editable: true` configuration.
        Defaults to `layout.uirevision`.
    
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

    # zeroline
    # --------
    @property
    def zeroline(self):
        """
        Determines whether or not a line is drawn at along the 0 value
        of this axis. If True, the zero line is drawn on top of the
        grid lines.
    
        The 'zeroline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["zeroline"]

    @zeroline.setter
    def zeroline(self, val):
        self["zeroline"] = val

    # zerolinecolor
    # -------------
    @property
    def zerolinecolor(self):
        """
        Sets the line color of the zero line.
    
        The 'zerolinecolor' property is a color and may be specified as:
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
        return self["zerolinecolor"]

    @zerolinecolor.setter
    def zerolinecolor(self, val):
        self["zerolinecolor"] = val

    # zerolinewidth
    # -------------
    @property
    def zerolinewidth(self):
        """
        Sets the width (in px) of the zero line.
    
        The 'zerolinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["zerolinewidth"]

    @zerolinewidth.setter
    def zerolinewidth(self, val):
        self["zerolinewidth"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        anchor
            If set to an opposite-letter axis id (e.g. `x2`, `y`),
            this axis is bound to the corresponding opposite-letter
            axis. If set to "free", this axis' position is
            determined by `position`.
        automargin
            Determines whether long tick labels automatically grow
            the figure margins.
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
        constrain
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines how that happens: by increasing
            the "range" (default), or by decreasing the "domain".
        constraintoward
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines which direction we push the
            originally specified plot area. Options are "left",
            "center" (default), and "right" for x axes, and "top",
            "middle" (default), and "bottom" for y axes.
        dividercolor
            Sets the color of the dividers Only has an effect on
            "multicategory" axes.
        dividerwidth
            Sets the width (in px) of the dividers Only has an
            effect on "multicategory" axes.
        domain
            Sets the domain of this axis (in plot fraction).
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
        fixedrange
            Determines whether or not this axis is zoom-able. If
            true, then zoom is disabled.
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
        matches
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis will match the range of the corresponding
            axis in data-coordinates space. Moreover, matching axes
            share auto-range values, category lists and histogram
            auto-bins. Note that setting axes simultaneously in
            both a `scaleanchor` and a `matches` constraint is
            currently forbidden. Moreover, note that matching axes
            must have the same `type`.
        mirror
            Determines if the axis lines or/and ticks are mirrored
            to the opposite side of the plotting area. If True, the
            axis lines are mirrored. If "ticks", the axis lines and
            ticks are mirrored. If False, mirroring is disable. If
            "all", axis lines are mirrored on all shared-axes
            subplots. If "allticks", axis lines and ticks are
            mirrored on all shared-axes subplots.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        overlaying
            If set a same-letter axis id, this axis is overlaid on
            top of the corresponding same-letter axis, with traces
            and axes visible for both axes. If False, this axis
            does not overlay any same-letter axes. In this case,
            for axes with overlapping domains only the highest-
            numbered axis will be visible.
        position
            Sets the position of this axis in the plotting space
            (in normalized coordinates). Only has an effect if
            `anchor` is set to "free".
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
            If "normal", the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            "nonnegative", the range is non-negative, regardless of
            the input data. Applies only to linear axes.
        scaleanchor
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis changes together with the range of the
            corresponding axis such that the scale of pixels per
            unit is in a constant ratio. Both axes are still
            zoomable, but when you zoom one, the other will zoom
            the same amount, keeping a fixed midpoint. `constrain`
            and `constraintoward` determine how we enforce the
            constraint. You can chain these, ie `yaxis:
            {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}` but you
            can only link axes of the same `type`. The linked axis
            can have the opposite letter (to constrain the aspect
            ratio) or the same letter (to match scales across
            subplots). Loops (`yaxis: {scaleanchor: *x*}, xaxis:
            {scaleanchor: *y*}` or longer) are redundant and the
            last constraint encountered will be ignored to avoid
            possible inconsistent constraints via `scaleratio`.
            Note that setting axes simultaneously in both a
            `scaleanchor` and a `matches` constraint is currently
            forbidden.
        scaleratio
            If this axis is linked to another by `scaleanchor`,
            this determines the pixel to unit scale ratio. For
            example, if this value is 10, then every unit on this
            axis spans 10 times the number of pixels as a unit on
            the linked axis. Use this for example to create an
            elevation profile where the vertical scale is
            exaggerated a fixed amount with respect to the
            horizontal.
        separatethousands
            If "true", even 4-digit integers are separated
        showdividers
            Determines whether or not a dividers are drawn between
            the category levels of this axis. Only has an effect on
            "multicategory" axes.
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
        showspikes
            Determines whether or not spikes (aka droplines) are
            drawn for this axis. Note: This only takes affect when
            hovermode = closest
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
            Determines whether a x (y) axis is positioned at the
            "bottom" ("left") or "top" ("right") of the plotting
            area.
        spikecolor
            Sets the spike color. If undefined, will use the series
            color
        spikedash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        spikemode
            Determines the drawing mode for the spike line If
            "toaxis", the line is drawn from the data point to the
            axis the  series is plotted on. If "across", the line
            is drawn across the entire plot area, and supercedes
            "toaxis". If "marker", then a marker dot is drawn on
            the axis the series is plotted on
        spikesnap
            Determines whether spikelines are stuck to the cursor
            or to the closest datapoints.
        spikethickness
            Sets the width (in px) of the zero line.
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
            A tuple of
            plotly.graph_objects.layout.yaxis.Tickformatstop
            instances or dicts with compatible properties
        tickformatstopdefaults
            When used in a template (as
            layout.template.layout.yaxis.tickformatstopdefaults),
            sets the default property values to use for elements of
            layout.yaxis.tickformatstops
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
        tickson
            Determines where ticks and grid lines are drawn with
            respect to their corresponding tick labels. Only has an
            effect for axes of `type` "category" or
            "multicategory". When set to "boundaries", ticks and
            grid lines are drawn half a category to the left/bottom
            of labels.
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
            plotly.graph_objects.layout.yaxis.Title instance or
            dict with compatible properties
        titlefont
            Deprecated: Please use layout.yaxis.title.font instead.
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        uirevision
            Controls persistence of user-driven changes in axis
            `range`, `autorange`, and `title` if in `editable:
            true` configuration. Defaults to `layout.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        zeroline
            Determines whether or not a line is drawn at along the
            0 value of this axis. If True, the zero line is drawn
            on top of the grid lines.
        zerolinecolor
            Sets the line color of the zero line.
        zerolinewidth
            Sets the width (in px) of the zero line.
        """

    _mapped_properties = {"titlefont": ("title", "font")}

    def __init__(
        self,
        arg=None,
        anchor=None,
        automargin=None,
        autorange=None,
        calendar=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        constrain=None,
        constraintoward=None,
        dividercolor=None,
        dividerwidth=None,
        domain=None,
        dtick=None,
        exponentformat=None,
        fixedrange=None,
        gridcolor=None,
        gridwidth=None,
        hoverformat=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        matches=None,
        mirror=None,
        nticks=None,
        overlaying=None,
        position=None,
        range=None,
        rangemode=None,
        scaleanchor=None,
        scaleratio=None,
        separatethousands=None,
        showdividers=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showspikes=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        side=None,
        spikecolor=None,
        spikedash=None,
        spikemode=None,
        spikesnap=None,
        spikethickness=None,
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
        tickson=None,
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
        zeroline=None,
        zerolinecolor=None,
        zerolinewidth=None,
        **kwargs
    ):
        """
        Construct a new YAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.YAxis
        anchor
            If set to an opposite-letter axis id (e.g. `x2`, `y`),
            this axis is bound to the corresponding opposite-letter
            axis. If set to "free", this axis' position is
            determined by `position`.
        automargin
            Determines whether long tick labels automatically grow
            the figure margins.
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
        constrain
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines how that happens: by increasing
            the "range" (default), or by decreasing the "domain".
        constraintoward
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines which direction we push the
            originally specified plot area. Options are "left",
            "center" (default), and "right" for x axes, and "top",
            "middle" (default), and "bottom" for y axes.
        dividercolor
            Sets the color of the dividers Only has an effect on
            "multicategory" axes.
        dividerwidth
            Sets the width (in px) of the dividers Only has an
            effect on "multicategory" axes.
        domain
            Sets the domain of this axis (in plot fraction).
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
        fixedrange
            Determines whether or not this axis is zoom-able. If
            true, then zoom is disabled.
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
        matches
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis will match the range of the corresponding
            axis in data-coordinates space. Moreover, matching axes
            share auto-range values, category lists and histogram
            auto-bins. Note that setting axes simultaneously in
            both a `scaleanchor` and a `matches` constraint is
            currently forbidden. Moreover, note that matching axes
            must have the same `type`.
        mirror
            Determines if the axis lines or/and ticks are mirrored
            to the opposite side of the plotting area. If True, the
            axis lines are mirrored. If "ticks", the axis lines and
            ticks are mirrored. If False, mirroring is disable. If
            "all", axis lines are mirrored on all shared-axes
            subplots. If "allticks", axis lines and ticks are
            mirrored on all shared-axes subplots.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        overlaying
            If set a same-letter axis id, this axis is overlaid on
            top of the corresponding same-letter axis, with traces
            and axes visible for both axes. If False, this axis
            does not overlay any same-letter axes. In this case,
            for axes with overlapping domains only the highest-
            numbered axis will be visible.
        position
            Sets the position of this axis in the plotting space
            (in normalized coordinates). Only has an effect if
            `anchor` is set to "free".
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
            If "normal", the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            "nonnegative", the range is non-negative, regardless of
            the input data. Applies only to linear axes.
        scaleanchor
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis changes together with the range of the
            corresponding axis such that the scale of pixels per
            unit is in a constant ratio. Both axes are still
            zoomable, but when you zoom one, the other will zoom
            the same amount, keeping a fixed midpoint. `constrain`
            and `constraintoward` determine how we enforce the
            constraint. You can chain these, ie `yaxis:
            {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}` but you
            can only link axes of the same `type`. The linked axis
            can have the opposite letter (to constrain the aspect
            ratio) or the same letter (to match scales across
            subplots). Loops (`yaxis: {scaleanchor: *x*}, xaxis:
            {scaleanchor: *y*}` or longer) are redundant and the
            last constraint encountered will be ignored to avoid
            possible inconsistent constraints via `scaleratio`.
            Note that setting axes simultaneously in both a
            `scaleanchor` and a `matches` constraint is currently
            forbidden.
        scaleratio
            If this axis is linked to another by `scaleanchor`,
            this determines the pixel to unit scale ratio. For
            example, if this value is 10, then every unit on this
            axis spans 10 times the number of pixels as a unit on
            the linked axis. Use this for example to create an
            elevation profile where the vertical scale is
            exaggerated a fixed amount with respect to the
            horizontal.
        separatethousands
            If "true", even 4-digit integers are separated
        showdividers
            Determines whether or not a dividers are drawn between
            the category levels of this axis. Only has an effect on
            "multicategory" axes.
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
        showspikes
            Determines whether or not spikes (aka droplines) are
            drawn for this axis. Note: This only takes affect when
            hovermode = closest
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
            Determines whether a x (y) axis is positioned at the
            "bottom" ("left") or "top" ("right") of the plotting
            area.
        spikecolor
            Sets the spike color. If undefined, will use the series
            color
        spikedash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        spikemode
            Determines the drawing mode for the spike line If
            "toaxis", the line is drawn from the data point to the
            axis the  series is plotted on. If "across", the line
            is drawn across the entire plot area, and supercedes
            "toaxis". If "marker", then a marker dot is drawn on
            the axis the series is plotted on
        spikesnap
            Determines whether spikelines are stuck to the cursor
            or to the closest datapoints.
        spikethickness
            Sets the width (in px) of the zero line.
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
            A tuple of
            plotly.graph_objects.layout.yaxis.Tickformatstop
            instances or dicts with compatible properties
        tickformatstopdefaults
            When used in a template (as
            layout.template.layout.yaxis.tickformatstopdefaults),
            sets the default property values to use for elements of
            layout.yaxis.tickformatstops
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
        tickson
            Determines where ticks and grid lines are drawn with
            respect to their corresponding tick labels. Only has an
            effect for axes of `type` "category" or
            "multicategory". When set to "boundaries", ticks and
            grid lines are drawn half a category to the left/bottom
            of labels.
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
            plotly.graph_objects.layout.yaxis.Title instance or
            dict with compatible properties
        titlefont
            Deprecated: Please use layout.yaxis.title.font instead.
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        uirevision
            Controls persistence of user-driven changes in axis
            `range`, `autorange`, and `title` if in `editable:
            true` configuration. Defaults to `layout.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        zeroline
            Determines whether or not a line is drawn at along the
            0 value of this axis. If True, the zero line is drawn
            on top of the grid lines.
        zerolinecolor
            Sets the line color of the zero line.
        zerolinewidth
            Sets the width (in px) of the zero line.

        Returns
        -------
        YAxis
        """
        super(YAxis, self).__init__("yaxis")

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
The first argument to the plotly.graph_objs.layout.YAxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.YAxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import yaxis as v_yaxis

        # Initialize validators
        # ---------------------
        self._validators["anchor"] = v_yaxis.AnchorValidator()
        self._validators["automargin"] = v_yaxis.AutomarginValidator()
        self._validators["autorange"] = v_yaxis.AutorangeValidator()
        self._validators["calendar"] = v_yaxis.CalendarValidator()
        self._validators["categoryarray"] = v_yaxis.CategoryarrayValidator()
        self._validators["categoryarraysrc"] = v_yaxis.CategoryarraysrcValidator()
        self._validators["categoryorder"] = v_yaxis.CategoryorderValidator()
        self._validators["color"] = v_yaxis.ColorValidator()
        self._validators["constrain"] = v_yaxis.ConstrainValidator()
        self._validators["constraintoward"] = v_yaxis.ConstraintowardValidator()
        self._validators["dividercolor"] = v_yaxis.DividercolorValidator()
        self._validators["dividerwidth"] = v_yaxis.DividerwidthValidator()
        self._validators["domain"] = v_yaxis.DomainValidator()
        self._validators["dtick"] = v_yaxis.DtickValidator()
        self._validators["exponentformat"] = v_yaxis.ExponentformatValidator()
        self._validators["fixedrange"] = v_yaxis.FixedrangeValidator()
        self._validators["gridcolor"] = v_yaxis.GridcolorValidator()
        self._validators["gridwidth"] = v_yaxis.GridwidthValidator()
        self._validators["hoverformat"] = v_yaxis.HoverformatValidator()
        self._validators["layer"] = v_yaxis.LayerValidator()
        self._validators["linecolor"] = v_yaxis.LinecolorValidator()
        self._validators["linewidth"] = v_yaxis.LinewidthValidator()
        self._validators["matches"] = v_yaxis.MatchesValidator()
        self._validators["mirror"] = v_yaxis.MirrorValidator()
        self._validators["nticks"] = v_yaxis.NticksValidator()
        self._validators["overlaying"] = v_yaxis.OverlayingValidator()
        self._validators["position"] = v_yaxis.PositionValidator()
        self._validators["range"] = v_yaxis.RangeValidator()
        self._validators["rangemode"] = v_yaxis.RangemodeValidator()
        self._validators["scaleanchor"] = v_yaxis.ScaleanchorValidator()
        self._validators["scaleratio"] = v_yaxis.ScaleratioValidator()
        self._validators["separatethousands"] = v_yaxis.SeparatethousandsValidator()
        self._validators["showdividers"] = v_yaxis.ShowdividersValidator()
        self._validators["showexponent"] = v_yaxis.ShowexponentValidator()
        self._validators["showgrid"] = v_yaxis.ShowgridValidator()
        self._validators["showline"] = v_yaxis.ShowlineValidator()
        self._validators["showspikes"] = v_yaxis.ShowspikesValidator()
        self._validators["showticklabels"] = v_yaxis.ShowticklabelsValidator()
        self._validators["showtickprefix"] = v_yaxis.ShowtickprefixValidator()
        self._validators["showticksuffix"] = v_yaxis.ShowticksuffixValidator()
        self._validators["side"] = v_yaxis.SideValidator()
        self._validators["spikecolor"] = v_yaxis.SpikecolorValidator()
        self._validators["spikedash"] = v_yaxis.SpikedashValidator()
        self._validators["spikemode"] = v_yaxis.SpikemodeValidator()
        self._validators["spikesnap"] = v_yaxis.SpikesnapValidator()
        self._validators["spikethickness"] = v_yaxis.SpikethicknessValidator()
        self._validators["tick0"] = v_yaxis.Tick0Validator()
        self._validators["tickangle"] = v_yaxis.TickangleValidator()
        self._validators["tickcolor"] = v_yaxis.TickcolorValidator()
        self._validators["tickfont"] = v_yaxis.TickfontValidator()
        self._validators["tickformat"] = v_yaxis.TickformatValidator()
        self._validators["tickformatstops"] = v_yaxis.TickformatstopsValidator()
        self._validators["tickformatstopdefaults"] = v_yaxis.TickformatstopValidator()
        self._validators["ticklen"] = v_yaxis.TicklenValidator()
        self._validators["tickmode"] = v_yaxis.TickmodeValidator()
        self._validators["tickprefix"] = v_yaxis.TickprefixValidator()
        self._validators["ticks"] = v_yaxis.TicksValidator()
        self._validators["tickson"] = v_yaxis.TicksonValidator()
        self._validators["ticksuffix"] = v_yaxis.TicksuffixValidator()
        self._validators["ticktext"] = v_yaxis.TicktextValidator()
        self._validators["ticktextsrc"] = v_yaxis.TicktextsrcValidator()
        self._validators["tickvals"] = v_yaxis.TickvalsValidator()
        self._validators["tickvalssrc"] = v_yaxis.TickvalssrcValidator()
        self._validators["tickwidth"] = v_yaxis.TickwidthValidator()
        self._validators["title"] = v_yaxis.TitleValidator()
        self._validators["type"] = v_yaxis.TypeValidator()
        self._validators["uirevision"] = v_yaxis.UirevisionValidator()
        self._validators["visible"] = v_yaxis.VisibleValidator()
        self._validators["zeroline"] = v_yaxis.ZerolineValidator()
        self._validators["zerolinecolor"] = v_yaxis.ZerolinecolorValidator()
        self._validators["zerolinewidth"] = v_yaxis.ZerolinewidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("anchor", None)
        self["anchor"] = anchor if anchor is not None else _v
        _v = arg.pop("automargin", None)
        self["automargin"] = automargin if automargin is not None else _v
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
        _v = arg.pop("constrain", None)
        self["constrain"] = constrain if constrain is not None else _v
        _v = arg.pop("constraintoward", None)
        self["constraintoward"] = constraintoward if constraintoward is not None else _v
        _v = arg.pop("dividercolor", None)
        self["dividercolor"] = dividercolor if dividercolor is not None else _v
        _v = arg.pop("dividerwidth", None)
        self["dividerwidth"] = dividerwidth if dividerwidth is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("dtick", None)
        self["dtick"] = dtick if dtick is not None else _v
        _v = arg.pop("exponentformat", None)
        self["exponentformat"] = exponentformat if exponentformat is not None else _v
        _v = arg.pop("fixedrange", None)
        self["fixedrange"] = fixedrange if fixedrange is not None else _v
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
        _v = arg.pop("matches", None)
        self["matches"] = matches if matches is not None else _v
        _v = arg.pop("mirror", None)
        self["mirror"] = mirror if mirror is not None else _v
        _v = arg.pop("nticks", None)
        self["nticks"] = nticks if nticks is not None else _v
        _v = arg.pop("overlaying", None)
        self["overlaying"] = overlaying if overlaying is not None else _v
        _v = arg.pop("position", None)
        self["position"] = position if position is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("rangemode", None)
        self["rangemode"] = rangemode if rangemode is not None else _v
        _v = arg.pop("scaleanchor", None)
        self["scaleanchor"] = scaleanchor if scaleanchor is not None else _v
        _v = arg.pop("scaleratio", None)
        self["scaleratio"] = scaleratio if scaleratio is not None else _v
        _v = arg.pop("separatethousands", None)
        self["separatethousands"] = (
            separatethousands if separatethousands is not None else _v
        )
        _v = arg.pop("showdividers", None)
        self["showdividers"] = showdividers if showdividers is not None else _v
        _v = arg.pop("showexponent", None)
        self["showexponent"] = showexponent if showexponent is not None else _v
        _v = arg.pop("showgrid", None)
        self["showgrid"] = showgrid if showgrid is not None else _v
        _v = arg.pop("showline", None)
        self["showline"] = showline if showline is not None else _v
        _v = arg.pop("showspikes", None)
        self["showspikes"] = showspikes if showspikes is not None else _v
        _v = arg.pop("showticklabels", None)
        self["showticklabels"] = showticklabels if showticklabels is not None else _v
        _v = arg.pop("showtickprefix", None)
        self["showtickprefix"] = showtickprefix if showtickprefix is not None else _v
        _v = arg.pop("showticksuffix", None)
        self["showticksuffix"] = showticksuffix if showticksuffix is not None else _v
        _v = arg.pop("side", None)
        self["side"] = side if side is not None else _v
        _v = arg.pop("spikecolor", None)
        self["spikecolor"] = spikecolor if spikecolor is not None else _v
        _v = arg.pop("spikedash", None)
        self["spikedash"] = spikedash if spikedash is not None else _v
        _v = arg.pop("spikemode", None)
        self["spikemode"] = spikemode if spikemode is not None else _v
        _v = arg.pop("spikesnap", None)
        self["spikesnap"] = spikesnap if spikesnap is not None else _v
        _v = arg.pop("spikethickness", None)
        self["spikethickness"] = spikethickness if spikethickness is not None else _v
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
        _v = arg.pop("tickson", None)
        self["tickson"] = tickson if tickson is not None else _v
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
        _v = arg.pop("zeroline", None)
        self["zeroline"] = zeroline if zeroline is not None else _v
        _v = arg.pop("zerolinecolor", None)
        self["zerolinecolor"] = zerolinecolor if zerolinecolor is not None else _v
        _v = arg.pop("zerolinewidth", None)
        self["zerolinewidth"] = zerolinewidth if zerolinewidth is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class XAxis(_BaseLayoutHierarchyType):

    # anchor
    # ------
    @property
    def anchor(self):
        """
        If set to an opposite-letter axis id (e.g. `x2`, `y`), this
        axis is bound to the corresponding opposite-letter axis. If set
        to "free", this axis' position is determined by `position`.
    
        The 'anchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['free']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["anchor"]

    @anchor.setter
    def anchor(self, val):
        self["anchor"] = val

    # automargin
    # ----------
    @property
    def automargin(self):
        """
        Determines whether long tick labels automatically grow the
        figure margins.
    
        The 'automargin' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["automargin"]

    @automargin.setter
    def automargin(self, val):
        self["automargin"] = val

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

    # constrain
    # ---------
    @property
    def constrain(self):
        """
        If this axis needs to be compressed (either due to its own
        `scaleanchor` and `scaleratio` or those of the other axis),
        determines how that happens: by increasing the "range"
        (default), or by decreasing the "domain".
    
        The 'constrain' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['range', 'domain']

        Returns
        -------
        Any
        """
        return self["constrain"]

    @constrain.setter
    def constrain(self, val):
        self["constrain"] = val

    # constraintoward
    # ---------------
    @property
    def constraintoward(self):
        """
        If this axis needs to be compressed (either due to its own
        `scaleanchor` and `scaleratio` or those of the other axis),
        determines which direction we push the originally specified
        plot area. Options are "left", "center" (default), and "right"
        for x axes, and "top", "middle" (default), and "bottom" for y
        axes.
    
        The 'constraintoward' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["constraintoward"]

    @constraintoward.setter
    def constraintoward(self, val):
        self["constraintoward"] = val

    # dividercolor
    # ------------
    @property
    def dividercolor(self):
        """
        Sets the color of the dividers Only has an effect on
        "multicategory" axes.
    
        The 'dividercolor' property is a color and may be specified as:
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
        return self["dividercolor"]

    @dividercolor.setter
    def dividercolor(self, val):
        self["dividercolor"] = val

    # dividerwidth
    # ------------
    @property
    def dividerwidth(self):
        """
        Sets the width (in px) of the dividers Only has an effect on
        "multicategory" axes.
    
        The 'dividerwidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dividerwidth"]

    @dividerwidth.setter
    def dividerwidth(self, val):
        self["dividerwidth"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        Sets the domain of this axis (in plot fraction).
    
        The 'domain' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'domain[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'domain[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

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

    # fixedrange
    # ----------
    @property
    def fixedrange(self):
        """
        Determines whether or not this axis is zoom-able. If true, then
        zoom is disabled.
    
        The 'fixedrange' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["fixedrange"]

    @fixedrange.setter
    def fixedrange(self, val):
        self["fixedrange"] = val

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

    # matches
    # -------
    @property
    def matches(self):
        """
        If set to another axis id (e.g. `x2`, `y`), the range of this
        axis will match the range of the corresponding axis in data-
        coordinates space. Moreover, matching axes share auto-range
        values, category lists and histogram auto-bins. Note that
        setting axes simultaneously in both a `scaleanchor` and a
        `matches` constraint is currently forbidden. Moreover, note
        that matching axes must have the same `type`.
    
        The 'matches' property is an enumeration that may be specified as:
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["matches"]

    @matches.setter
    def matches(self, val):
        self["matches"] = val

    # mirror
    # ------
    @property
    def mirror(self):
        """
        Determines if the axis lines or/and ticks are mirrored to the
        opposite side of the plotting area. If True, the axis lines are
        mirrored. If "ticks", the axis lines and ticks are mirrored. If
        False, mirroring is disable. If "all", axis lines are mirrored
        on all shared-axes subplots. If "allticks", axis lines and
        ticks are mirrored on all shared-axes subplots.
    
        The 'mirror' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, 'ticks', False, 'all', 'allticks']

        Returns
        -------
        Any
        """
        return self["mirror"]

    @mirror.setter
    def mirror(self, val):
        self["mirror"] = val

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

    # overlaying
    # ----------
    @property
    def overlaying(self):
        """
        If set a same-letter axis id, this axis is overlaid on top of
        the corresponding same-letter axis, with traces and axes
        visible for both axes. If False, this axis does not overlay any
        same-letter axes. In this case, for axes with overlapping
        domains only the highest-numbered axis will be visible.
    
        The 'overlaying' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['free']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["overlaying"]

    @overlaying.setter
    def overlaying(self, val):
        self["overlaying"] = val

    # position
    # --------
    @property
    def position(self):
        """
        Sets the position of this axis in the plotting space (in
        normalized coordinates). Only has an effect if `anchor` is set
        to "free".
    
        The 'position' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

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
        If "normal", the range is computed in relation to the extrema
        of the input data. If *tozero*`, the range extends to 0,
        regardless of the input data If "nonnegative", the range is
        non-negative, regardless of the input data. Applies only to
        linear axes.
    
        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'tozero', 'nonnegative']

        Returns
        -------
        Any
        """
        return self["rangemode"]

    @rangemode.setter
    def rangemode(self, val):
        self["rangemode"] = val

    # rangeselector
    # -------------
    @property
    def rangeselector(self):
        """
        The 'rangeselector' property is an instance of Rangeselector
        that may be specified as:
          - An instance of plotly.graph_objs.layout.xaxis.Rangeselector
          - A dict of string/value properties that will be passed
            to the Rangeselector constructor
    
            Supported dict properties:
                
                activecolor
                    Sets the background color of the active range
                    selector button.
                bgcolor
                    Sets the background color of the range selector
                    buttons.
                bordercolor
                    Sets the color of the border enclosing the
                    range selector.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the range selector.
                buttons
                    Sets the specifications for each buttons. By
                    default, a range selector comes with no
                    buttons.
                buttondefaults
                    When used in a template (as layout.template.lay
                    out.xaxis.rangeselector.buttondefaults), sets
                    the default property values to use for elements
                    of layout.xaxis.rangeselector.buttons
                font
                    Sets the font of the range selector button
                    text.
                visible
                    Determines whether or not this range selector
                    is visible. Note that range selectors are only
                    available for x axes of `type` set to or auto-
                    typed to "date".
                x
                    Sets the x position (in normalized coordinates)
                    of the range selector.
                xanchor
                    Sets the range selector's horizontal position
                    anchor. This anchor binds the `x` position to
                    the "left", "center" or "right" of the range
                    selector.
                y
                    Sets the y position (in normalized coordinates)
                    of the range selector.
                yanchor
                    Sets the range selector's vertical position
                    anchor This anchor binds the `y` position to
                    the "top", "middle" or "bottom" of the range
                    selector.

        Returns
        -------
        plotly.graph_objs.layout.xaxis.Rangeselector
        """
        return self["rangeselector"]

    @rangeselector.setter
    def rangeselector(self, val):
        self["rangeselector"] = val

    # rangeslider
    # -----------
    @property
    def rangeslider(self):
        """
        The 'rangeslider' property is an instance of Rangeslider
        that may be specified as:
          - An instance of plotly.graph_objs.layout.xaxis.Rangeslider
          - A dict of string/value properties that will be passed
            to the Rangeslider constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range slider
                    range is computed in relation to the input
                    data. If `range` is provided, then `autorange`
                    is set to False.
                bgcolor
                    Sets the background color of the range slider.
                bordercolor
                    Sets the border color of the range slider.
                borderwidth
                    Sets the border width of the range slider.
                range
                    Sets the range of the range slider. If not set,
                    defaults to the full xaxis range. If the axis
                    `type` is "log", then you must take the log of
                    your desired range. If the axis `type` is
                    "date", it should be date strings, like date
                    data, though Date objects and unix milliseconds
                    will be accepted and converted to strings. If
                    the axis `type` is "category", it should be
                    numbers, using the scale where each category is
                    assigned a serial number from zero in the order
                    it appears.
                thickness
                    The height of the range slider as a fraction of
                    the total plot area height.
                visible
                    Determines whether or not the range slider will
                    be visible. If visible, perpendicular axes will
                    be set to `fixedrange`
                yaxis
                    plotly.graph_objects.layout.xaxis.rangeslider.Y
                    Axis instance or dict with compatible
                    properties

        Returns
        -------
        plotly.graph_objs.layout.xaxis.Rangeslider
        """
        return self["rangeslider"]

    @rangeslider.setter
    def rangeslider(self, val):
        self["rangeslider"] = val

    # scaleanchor
    # -----------
    @property
    def scaleanchor(self):
        """
        If set to another axis id (e.g. `x2`, `y`), the range of this
        axis changes together with the range of the corresponding axis
        such that the scale of pixels per unit is in a constant ratio.
        Both axes are still zoomable, but when you zoom one, the other
        will zoom the same amount, keeping a fixed midpoint.
        `constrain` and `constraintoward` determine how we enforce the
        constraint. You can chain these, ie `yaxis: {scaleanchor: *x*},
        xaxis2: {scaleanchor: *y*}` but you can only link axes of the
        same `type`. The linked axis can have the opposite letter (to
        constrain the aspect ratio) or the same letter (to match scales
        across subplots). Loops (`yaxis: {scaleanchor: *x*}, xaxis:
        {scaleanchor: *y*}` or longer) are redundant and the last
        constraint encountered will be ignored to avoid possible
        inconsistent constraints via `scaleratio`. Note that setting
        axes simultaneously in both a `scaleanchor` and a `matches`
        constraint is currently forbidden.
    
        The 'scaleanchor' property is an enumeration that may be specified as:
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$', '^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["scaleanchor"]

    @scaleanchor.setter
    def scaleanchor(self, val):
        self["scaleanchor"] = val

    # scaleratio
    # ----------
    @property
    def scaleratio(self):
        """
        If this axis is linked to another by `scaleanchor`, this
        determines the pixel to unit scale ratio. For example, if this
        value is 10, then every unit on this axis spans 10 times the
        number of pixels as a unit on the linked axis. Use this for
        example to create an elevation profile where the vertical scale
        is exaggerated a fixed amount with respect to the horizontal.
    
        The 'scaleratio' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["scaleratio"]

    @scaleratio.setter
    def scaleratio(self, val):
        self["scaleratio"] = val

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

    # showdividers
    # ------------
    @property
    def showdividers(self):
        """
        Determines whether or not a dividers are drawn between the
        category levels of this axis. Only has an effect on
        "multicategory" axes.
    
        The 'showdividers' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showdividers"]

    @showdividers.setter
    def showdividers(self, val):
        self["showdividers"] = val

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

    # showspikes
    # ----------
    @property
    def showspikes(self):
        """
        Determines whether or not spikes (aka droplines) are drawn for
        this axis. Note: This only takes affect when hovermode =
        closest
    
        The 'showspikes' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showspikes"]

    @showspikes.setter
    def showspikes(self, val):
        self["showspikes"] = val

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
        Determines whether a x (y) axis is positioned at the "bottom"
        ("left") or "top" ("right") of the plotting area.
    
        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'bottom', 'left', 'right']

        Returns
        -------
        Any
        """
        return self["side"]

    @side.setter
    def side(self, val):
        self["side"] = val

    # spikecolor
    # ----------
    @property
    def spikecolor(self):
        """
        Sets the spike color. If undefined, will use the series color
    
        The 'spikecolor' property is a color and may be specified as:
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
        return self["spikecolor"]

    @spikecolor.setter
    def spikecolor(self, val):
        self["spikecolor"] = val

    # spikedash
    # ---------
    @property
    def spikedash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").
    
        The 'spikedash' property is a string and must be specified as:
          - One of the following strings:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot',
                'longdashdot']
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["spikedash"]

    @spikedash.setter
    def spikedash(self, val):
        self["spikedash"] = val

    # spikemode
    # ---------
    @property
    def spikemode(self):
        """
        Determines the drawing mode for the spike line If "toaxis", the
        line is drawn from the data point to the axis the  series is
        plotted on. If "across", the line is drawn across the entire
        plot area, and supercedes "toaxis". If "marker", then a marker
        dot is drawn on the axis the series is plotted on
    
        The 'spikemode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['toaxis', 'across', 'marker'] joined with '+' characters
            (e.g. 'toaxis+across')

        Returns
        -------
        Any
        """
        return self["spikemode"]

    @spikemode.setter
    def spikemode(self, val):
        self["spikemode"] = val

    # spikesnap
    # ---------
    @property
    def spikesnap(self):
        """
        Determines whether spikelines are stuck to the cursor or to the
        closest datapoints.
    
        The 'spikesnap' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['data', 'cursor']

        Returns
        -------
        Any
        """
        return self["spikesnap"]

    @spikesnap.setter
    def spikesnap(self, val):
        self["spikesnap"] = val

    # spikethickness
    # --------------
    @property
    def spikethickness(self):
        """
        Sets the width (in px) of the zero line.
    
        The 'spikethickness' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["spikethickness"]

    @spikethickness.setter
    def spikethickness(self, val):
        self["spikethickness"] = val

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
          - An instance of plotly.graph_objs.layout.xaxis.Tickfont
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
        plotly.graph_objs.layout.xaxis.Tickfont
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
          - A list or tuple of instances of plotly.graph_objs.layout.xaxis.Tickformatstop
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
        tuple[plotly.graph_objs.layout.xaxis.Tickformatstop]
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
        When used in a template (as
        layout.template.layout.xaxis.tickformatstopdefaults), sets the
        default property values to use for elements of
        layout.xaxis.tickformatstops
    
        The 'tickformatstopdefaults' property is an instance of Tickformatstop
        that may be specified as:
          - An instance of plotly.graph_objs.layout.xaxis.Tickformatstop
          - A dict of string/value properties that will be passed
            to the Tickformatstop constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.xaxis.Tickformatstop
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

    # tickson
    # -------
    @property
    def tickson(self):
        """
        Determines where ticks and grid lines are drawn with respect to
        their corresponding tick labels. Only has an effect for axes of
        `type` "category" or "multicategory". When set to "boundaries",
        ticks and grid lines are drawn half a category to the
        left/bottom of labels.
    
        The 'tickson' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['labels', 'boundaries']

        Returns
        -------
        Any
        """
        return self["tickson"]

    @tickson.setter
    def tickson(self, val):
        self["tickson"] = val

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
          - An instance of plotly.graph_objs.layout.xaxis.Title
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
        plotly.graph_objs.layout.xaxis.Title
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
        Deprecated: Please use layout.xaxis.title.font instead. Sets
        this axis' title font. Note that the title's font used to be
        customized by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.xaxis.title.Font
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
                ['-', 'linear', 'log', 'date', 'category',
                'multicategory']

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
        `autorange`, and `title` if in `editable: true` configuration.
        Defaults to `layout.uirevision`.
    
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

    # zeroline
    # --------
    @property
    def zeroline(self):
        """
        Determines whether or not a line is drawn at along the 0 value
        of this axis. If True, the zero line is drawn on top of the
        grid lines.
    
        The 'zeroline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["zeroline"]

    @zeroline.setter
    def zeroline(self, val):
        self["zeroline"] = val

    # zerolinecolor
    # -------------
    @property
    def zerolinecolor(self):
        """
        Sets the line color of the zero line.
    
        The 'zerolinecolor' property is a color and may be specified as:
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
        return self["zerolinecolor"]

    @zerolinecolor.setter
    def zerolinecolor(self, val):
        self["zerolinecolor"] = val

    # zerolinewidth
    # -------------
    @property
    def zerolinewidth(self):
        """
        Sets the width (in px) of the zero line.
    
        The 'zerolinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["zerolinewidth"]

    @zerolinewidth.setter
    def zerolinewidth(self, val):
        self["zerolinewidth"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        anchor
            If set to an opposite-letter axis id (e.g. `x2`, `y`),
            this axis is bound to the corresponding opposite-letter
            axis. If set to "free", this axis' position is
            determined by `position`.
        automargin
            Determines whether long tick labels automatically grow
            the figure margins.
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
        constrain
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines how that happens: by increasing
            the "range" (default), or by decreasing the "domain".
        constraintoward
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines which direction we push the
            originally specified plot area. Options are "left",
            "center" (default), and "right" for x axes, and "top",
            "middle" (default), and "bottom" for y axes.
        dividercolor
            Sets the color of the dividers Only has an effect on
            "multicategory" axes.
        dividerwidth
            Sets the width (in px) of the dividers Only has an
            effect on "multicategory" axes.
        domain
            Sets the domain of this axis (in plot fraction).
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
        fixedrange
            Determines whether or not this axis is zoom-able. If
            true, then zoom is disabled.
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
        matches
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis will match the range of the corresponding
            axis in data-coordinates space. Moreover, matching axes
            share auto-range values, category lists and histogram
            auto-bins. Note that setting axes simultaneously in
            both a `scaleanchor` and a `matches` constraint is
            currently forbidden. Moreover, note that matching axes
            must have the same `type`.
        mirror
            Determines if the axis lines or/and ticks are mirrored
            to the opposite side of the plotting area. If True, the
            axis lines are mirrored. If "ticks", the axis lines and
            ticks are mirrored. If False, mirroring is disable. If
            "all", axis lines are mirrored on all shared-axes
            subplots. If "allticks", axis lines and ticks are
            mirrored on all shared-axes subplots.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        overlaying
            If set a same-letter axis id, this axis is overlaid on
            top of the corresponding same-letter axis, with traces
            and axes visible for both axes. If False, this axis
            does not overlay any same-letter axes. In this case,
            for axes with overlapping domains only the highest-
            numbered axis will be visible.
        position
            Sets the position of this axis in the plotting space
            (in normalized coordinates). Only has an effect if
            `anchor` is set to "free".
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
            If "normal", the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            "nonnegative", the range is non-negative, regardless of
            the input data. Applies only to linear axes.
        rangeselector
            plotly.graph_objects.layout.xaxis.Rangeselector
            instance or dict with compatible properties
        rangeslider
            plotly.graph_objects.layout.xaxis.Rangeslider instance
            or dict with compatible properties
        scaleanchor
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis changes together with the range of the
            corresponding axis such that the scale of pixels per
            unit is in a constant ratio. Both axes are still
            zoomable, but when you zoom one, the other will zoom
            the same amount, keeping a fixed midpoint. `constrain`
            and `constraintoward` determine how we enforce the
            constraint. You can chain these, ie `yaxis:
            {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}` but you
            can only link axes of the same `type`. The linked axis
            can have the opposite letter (to constrain the aspect
            ratio) or the same letter (to match scales across
            subplots). Loops (`yaxis: {scaleanchor: *x*}, xaxis:
            {scaleanchor: *y*}` or longer) are redundant and the
            last constraint encountered will be ignored to avoid
            possible inconsistent constraints via `scaleratio`.
            Note that setting axes simultaneously in both a
            `scaleanchor` and a `matches` constraint is currently
            forbidden.
        scaleratio
            If this axis is linked to another by `scaleanchor`,
            this determines the pixel to unit scale ratio. For
            example, if this value is 10, then every unit on this
            axis spans 10 times the number of pixels as a unit on
            the linked axis. Use this for example to create an
            elevation profile where the vertical scale is
            exaggerated a fixed amount with respect to the
            horizontal.
        separatethousands
            If "true", even 4-digit integers are separated
        showdividers
            Determines whether or not a dividers are drawn between
            the category levels of this axis. Only has an effect on
            "multicategory" axes.
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
        showspikes
            Determines whether or not spikes (aka droplines) are
            drawn for this axis. Note: This only takes affect when
            hovermode = closest
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
            Determines whether a x (y) axis is positioned at the
            "bottom" ("left") or "top" ("right") of the plotting
            area.
        spikecolor
            Sets the spike color. If undefined, will use the series
            color
        spikedash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        spikemode
            Determines the drawing mode for the spike line If
            "toaxis", the line is drawn from the data point to the
            axis the  series is plotted on. If "across", the line
            is drawn across the entire plot area, and supercedes
            "toaxis". If "marker", then a marker dot is drawn on
            the axis the series is plotted on
        spikesnap
            Determines whether spikelines are stuck to the cursor
            or to the closest datapoints.
        spikethickness
            Sets the width (in px) of the zero line.
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
            A tuple of
            plotly.graph_objects.layout.xaxis.Tickformatstop
            instances or dicts with compatible properties
        tickformatstopdefaults
            When used in a template (as
            layout.template.layout.xaxis.tickformatstopdefaults),
            sets the default property values to use for elements of
            layout.xaxis.tickformatstops
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
        tickson
            Determines where ticks and grid lines are drawn with
            respect to their corresponding tick labels. Only has an
            effect for axes of `type` "category" or
            "multicategory". When set to "boundaries", ticks and
            grid lines are drawn half a category to the left/bottom
            of labels.
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
            plotly.graph_objects.layout.xaxis.Title instance or
            dict with compatible properties
        titlefont
            Deprecated: Please use layout.xaxis.title.font instead.
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        uirevision
            Controls persistence of user-driven changes in axis
            `range`, `autorange`, and `title` if in `editable:
            true` configuration. Defaults to `layout.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        zeroline
            Determines whether or not a line is drawn at along the
            0 value of this axis. If True, the zero line is drawn
            on top of the grid lines.
        zerolinecolor
            Sets the line color of the zero line.
        zerolinewidth
            Sets the width (in px) of the zero line.
        """

    _mapped_properties = {"titlefont": ("title", "font")}

    def __init__(
        self,
        arg=None,
        anchor=None,
        automargin=None,
        autorange=None,
        calendar=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        constrain=None,
        constraintoward=None,
        dividercolor=None,
        dividerwidth=None,
        domain=None,
        dtick=None,
        exponentformat=None,
        fixedrange=None,
        gridcolor=None,
        gridwidth=None,
        hoverformat=None,
        layer=None,
        linecolor=None,
        linewidth=None,
        matches=None,
        mirror=None,
        nticks=None,
        overlaying=None,
        position=None,
        range=None,
        rangemode=None,
        rangeselector=None,
        rangeslider=None,
        scaleanchor=None,
        scaleratio=None,
        separatethousands=None,
        showdividers=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showspikes=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        side=None,
        spikecolor=None,
        spikedash=None,
        spikemode=None,
        spikesnap=None,
        spikethickness=None,
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
        tickson=None,
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
        zeroline=None,
        zerolinecolor=None,
        zerolinewidth=None,
        **kwargs
    ):
        """
        Construct a new XAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.XAxis
        anchor
            If set to an opposite-letter axis id (e.g. `x2`, `y`),
            this axis is bound to the corresponding opposite-letter
            axis. If set to "free", this axis' position is
            determined by `position`.
        automargin
            Determines whether long tick labels automatically grow
            the figure margins.
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
        constrain
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines how that happens: by increasing
            the "range" (default), or by decreasing the "domain".
        constraintoward
            If this axis needs to be compressed (either due to its
            own `scaleanchor` and `scaleratio` or those of the
            other axis), determines which direction we push the
            originally specified plot area. Options are "left",
            "center" (default), and "right" for x axes, and "top",
            "middle" (default), and "bottom" for y axes.
        dividercolor
            Sets the color of the dividers Only has an effect on
            "multicategory" axes.
        dividerwidth
            Sets the width (in px) of the dividers Only has an
            effect on "multicategory" axes.
        domain
            Sets the domain of this axis (in plot fraction).
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
        fixedrange
            Determines whether or not this axis is zoom-able. If
            true, then zoom is disabled.
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
        matches
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis will match the range of the corresponding
            axis in data-coordinates space. Moreover, matching axes
            share auto-range values, category lists and histogram
            auto-bins. Note that setting axes simultaneously in
            both a `scaleanchor` and a `matches` constraint is
            currently forbidden. Moreover, note that matching axes
            must have the same `type`.
        mirror
            Determines if the axis lines or/and ticks are mirrored
            to the opposite side of the plotting area. If True, the
            axis lines are mirrored. If "ticks", the axis lines and
            ticks are mirrored. If False, mirroring is disable. If
            "all", axis lines are mirrored on all shared-axes
            subplots. If "allticks", axis lines and ticks are
            mirrored on all shared-axes subplots.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            "auto".
        overlaying
            If set a same-letter axis id, this axis is overlaid on
            top of the corresponding same-letter axis, with traces
            and axes visible for both axes. If False, this axis
            does not overlay any same-letter axes. In this case,
            for axes with overlapping domains only the highest-
            numbered axis will be visible.
        position
            Sets the position of this axis in the plotting space
            (in normalized coordinates). Only has an effect if
            `anchor` is set to "free".
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
            If "normal", the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            "nonnegative", the range is non-negative, regardless of
            the input data. Applies only to linear axes.
        rangeselector
            plotly.graph_objects.layout.xaxis.Rangeselector
            instance or dict with compatible properties
        rangeslider
            plotly.graph_objects.layout.xaxis.Rangeslider instance
            or dict with compatible properties
        scaleanchor
            If set to another axis id (e.g. `x2`, `y`), the range
            of this axis changes together with the range of the
            corresponding axis such that the scale of pixels per
            unit is in a constant ratio. Both axes are still
            zoomable, but when you zoom one, the other will zoom
            the same amount, keeping a fixed midpoint. `constrain`
            and `constraintoward` determine how we enforce the
            constraint. You can chain these, ie `yaxis:
            {scaleanchor: *x*}, xaxis2: {scaleanchor: *y*}` but you
            can only link axes of the same `type`. The linked axis
            can have the opposite letter (to constrain the aspect
            ratio) or the same letter (to match scales across
            subplots). Loops (`yaxis: {scaleanchor: *x*}, xaxis:
            {scaleanchor: *y*}` or longer) are redundant and the
            last constraint encountered will be ignored to avoid
            possible inconsistent constraints via `scaleratio`.
            Note that setting axes simultaneously in both a
            `scaleanchor` and a `matches` constraint is currently
            forbidden.
        scaleratio
            If this axis is linked to another by `scaleanchor`,
            this determines the pixel to unit scale ratio. For
            example, if this value is 10, then every unit on this
            axis spans 10 times the number of pixels as a unit on
            the linked axis. Use this for example to create an
            elevation profile where the vertical scale is
            exaggerated a fixed amount with respect to the
            horizontal.
        separatethousands
            If "true", even 4-digit integers are separated
        showdividers
            Determines whether or not a dividers are drawn between
            the category levels of this axis. Only has an effect on
            "multicategory" axes.
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
        showspikes
            Determines whether or not spikes (aka droplines) are
            drawn for this axis. Note: This only takes affect when
            hovermode = closest
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
            Determines whether a x (y) axis is positioned at the
            "bottom" ("left") or "top" ("right") of the plotting
            area.
        spikecolor
            Sets the spike color. If undefined, will use the series
            color
        spikedash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        spikemode
            Determines the drawing mode for the spike line If
            "toaxis", the line is drawn from the data point to the
            axis the  series is plotted on. If "across", the line
            is drawn across the entire plot area, and supercedes
            "toaxis". If "marker", then a marker dot is drawn on
            the axis the series is plotted on
        spikesnap
            Determines whether spikelines are stuck to the cursor
            or to the closest datapoints.
        spikethickness
            Sets the width (in px) of the zero line.
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
            A tuple of
            plotly.graph_objects.layout.xaxis.Tickformatstop
            instances or dicts with compatible properties
        tickformatstopdefaults
            When used in a template (as
            layout.template.layout.xaxis.tickformatstopdefaults),
            sets the default property values to use for elements of
            layout.xaxis.tickformatstops
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
        tickson
            Determines where ticks and grid lines are drawn with
            respect to their corresponding tick labels. Only has an
            effect for axes of `type` "category" or
            "multicategory". When set to "boundaries", ticks and
            grid lines are drawn half a category to the left/bottom
            of labels.
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
            plotly.graph_objects.layout.xaxis.Title instance or
            dict with compatible properties
        titlefont
            Deprecated: Please use layout.xaxis.title.font instead.
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        uirevision
            Controls persistence of user-driven changes in axis
            `range`, `autorange`, and `title` if in `editable:
            true` configuration. Defaults to `layout.uirevision`.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        zeroline
            Determines whether or not a line is drawn at along the
            0 value of this axis. If True, the zero line is drawn
            on top of the grid lines.
        zerolinecolor
            Sets the line color of the zero line.
        zerolinewidth
            Sets the width (in px) of the zero line.

        Returns
        -------
        XAxis
        """
        super(XAxis, self).__init__("xaxis")

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
The first argument to the plotly.graph_objs.layout.XAxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.XAxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import xaxis as v_xaxis

        # Initialize validators
        # ---------------------
        self._validators["anchor"] = v_xaxis.AnchorValidator()
        self._validators["automargin"] = v_xaxis.AutomarginValidator()
        self._validators["autorange"] = v_xaxis.AutorangeValidator()
        self._validators["calendar"] = v_xaxis.CalendarValidator()
        self._validators["categoryarray"] = v_xaxis.CategoryarrayValidator()
        self._validators["categoryarraysrc"] = v_xaxis.CategoryarraysrcValidator()
        self._validators["categoryorder"] = v_xaxis.CategoryorderValidator()
        self._validators["color"] = v_xaxis.ColorValidator()
        self._validators["constrain"] = v_xaxis.ConstrainValidator()
        self._validators["constraintoward"] = v_xaxis.ConstraintowardValidator()
        self._validators["dividercolor"] = v_xaxis.DividercolorValidator()
        self._validators["dividerwidth"] = v_xaxis.DividerwidthValidator()
        self._validators["domain"] = v_xaxis.DomainValidator()
        self._validators["dtick"] = v_xaxis.DtickValidator()
        self._validators["exponentformat"] = v_xaxis.ExponentformatValidator()
        self._validators["fixedrange"] = v_xaxis.FixedrangeValidator()
        self._validators["gridcolor"] = v_xaxis.GridcolorValidator()
        self._validators["gridwidth"] = v_xaxis.GridwidthValidator()
        self._validators["hoverformat"] = v_xaxis.HoverformatValidator()
        self._validators["layer"] = v_xaxis.LayerValidator()
        self._validators["linecolor"] = v_xaxis.LinecolorValidator()
        self._validators["linewidth"] = v_xaxis.LinewidthValidator()
        self._validators["matches"] = v_xaxis.MatchesValidator()
        self._validators["mirror"] = v_xaxis.MirrorValidator()
        self._validators["nticks"] = v_xaxis.NticksValidator()
        self._validators["overlaying"] = v_xaxis.OverlayingValidator()
        self._validators["position"] = v_xaxis.PositionValidator()
        self._validators["range"] = v_xaxis.RangeValidator()
        self._validators["rangemode"] = v_xaxis.RangemodeValidator()
        self._validators["rangeselector"] = v_xaxis.RangeselectorValidator()
        self._validators["rangeslider"] = v_xaxis.RangesliderValidator()
        self._validators["scaleanchor"] = v_xaxis.ScaleanchorValidator()
        self._validators["scaleratio"] = v_xaxis.ScaleratioValidator()
        self._validators["separatethousands"] = v_xaxis.SeparatethousandsValidator()
        self._validators["showdividers"] = v_xaxis.ShowdividersValidator()
        self._validators["showexponent"] = v_xaxis.ShowexponentValidator()
        self._validators["showgrid"] = v_xaxis.ShowgridValidator()
        self._validators["showline"] = v_xaxis.ShowlineValidator()
        self._validators["showspikes"] = v_xaxis.ShowspikesValidator()
        self._validators["showticklabels"] = v_xaxis.ShowticklabelsValidator()
        self._validators["showtickprefix"] = v_xaxis.ShowtickprefixValidator()
        self._validators["showticksuffix"] = v_xaxis.ShowticksuffixValidator()
        self._validators["side"] = v_xaxis.SideValidator()
        self._validators["spikecolor"] = v_xaxis.SpikecolorValidator()
        self._validators["spikedash"] = v_xaxis.SpikedashValidator()
        self._validators["spikemode"] = v_xaxis.SpikemodeValidator()
        self._validators["spikesnap"] = v_xaxis.SpikesnapValidator()
        self._validators["spikethickness"] = v_xaxis.SpikethicknessValidator()
        self._validators["tick0"] = v_xaxis.Tick0Validator()
        self._validators["tickangle"] = v_xaxis.TickangleValidator()
        self._validators["tickcolor"] = v_xaxis.TickcolorValidator()
        self._validators["tickfont"] = v_xaxis.TickfontValidator()
        self._validators["tickformat"] = v_xaxis.TickformatValidator()
        self._validators["tickformatstops"] = v_xaxis.TickformatstopsValidator()
        self._validators["tickformatstopdefaults"] = v_xaxis.TickformatstopValidator()
        self._validators["ticklen"] = v_xaxis.TicklenValidator()
        self._validators["tickmode"] = v_xaxis.TickmodeValidator()
        self._validators["tickprefix"] = v_xaxis.TickprefixValidator()
        self._validators["ticks"] = v_xaxis.TicksValidator()
        self._validators["tickson"] = v_xaxis.TicksonValidator()
        self._validators["ticksuffix"] = v_xaxis.TicksuffixValidator()
        self._validators["ticktext"] = v_xaxis.TicktextValidator()
        self._validators["ticktextsrc"] = v_xaxis.TicktextsrcValidator()
        self._validators["tickvals"] = v_xaxis.TickvalsValidator()
        self._validators["tickvalssrc"] = v_xaxis.TickvalssrcValidator()
        self._validators["tickwidth"] = v_xaxis.TickwidthValidator()
        self._validators["title"] = v_xaxis.TitleValidator()
        self._validators["type"] = v_xaxis.TypeValidator()
        self._validators["uirevision"] = v_xaxis.UirevisionValidator()
        self._validators["visible"] = v_xaxis.VisibleValidator()
        self._validators["zeroline"] = v_xaxis.ZerolineValidator()
        self._validators["zerolinecolor"] = v_xaxis.ZerolinecolorValidator()
        self._validators["zerolinewidth"] = v_xaxis.ZerolinewidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("anchor", None)
        self["anchor"] = anchor if anchor is not None else _v
        _v = arg.pop("automargin", None)
        self["automargin"] = automargin if automargin is not None else _v
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
        _v = arg.pop("constrain", None)
        self["constrain"] = constrain if constrain is not None else _v
        _v = arg.pop("constraintoward", None)
        self["constraintoward"] = constraintoward if constraintoward is not None else _v
        _v = arg.pop("dividercolor", None)
        self["dividercolor"] = dividercolor if dividercolor is not None else _v
        _v = arg.pop("dividerwidth", None)
        self["dividerwidth"] = dividerwidth if dividerwidth is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("dtick", None)
        self["dtick"] = dtick if dtick is not None else _v
        _v = arg.pop("exponentformat", None)
        self["exponentformat"] = exponentformat if exponentformat is not None else _v
        _v = arg.pop("fixedrange", None)
        self["fixedrange"] = fixedrange if fixedrange is not None else _v
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
        _v = arg.pop("matches", None)
        self["matches"] = matches if matches is not None else _v
        _v = arg.pop("mirror", None)
        self["mirror"] = mirror if mirror is not None else _v
        _v = arg.pop("nticks", None)
        self["nticks"] = nticks if nticks is not None else _v
        _v = arg.pop("overlaying", None)
        self["overlaying"] = overlaying if overlaying is not None else _v
        _v = arg.pop("position", None)
        self["position"] = position if position is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("rangemode", None)
        self["rangemode"] = rangemode if rangemode is not None else _v
        _v = arg.pop("rangeselector", None)
        self["rangeselector"] = rangeselector if rangeselector is not None else _v
        _v = arg.pop("rangeslider", None)
        self["rangeslider"] = rangeslider if rangeslider is not None else _v
        _v = arg.pop("scaleanchor", None)
        self["scaleanchor"] = scaleanchor if scaleanchor is not None else _v
        _v = arg.pop("scaleratio", None)
        self["scaleratio"] = scaleratio if scaleratio is not None else _v
        _v = arg.pop("separatethousands", None)
        self["separatethousands"] = (
            separatethousands if separatethousands is not None else _v
        )
        _v = arg.pop("showdividers", None)
        self["showdividers"] = showdividers if showdividers is not None else _v
        _v = arg.pop("showexponent", None)
        self["showexponent"] = showexponent if showexponent is not None else _v
        _v = arg.pop("showgrid", None)
        self["showgrid"] = showgrid if showgrid is not None else _v
        _v = arg.pop("showline", None)
        self["showline"] = showline if showline is not None else _v
        _v = arg.pop("showspikes", None)
        self["showspikes"] = showspikes if showspikes is not None else _v
        _v = arg.pop("showticklabels", None)
        self["showticklabels"] = showticklabels if showticklabels is not None else _v
        _v = arg.pop("showtickprefix", None)
        self["showtickprefix"] = showtickprefix if showtickprefix is not None else _v
        _v = arg.pop("showticksuffix", None)
        self["showticksuffix"] = showticksuffix if showticksuffix is not None else _v
        _v = arg.pop("side", None)
        self["side"] = side if side is not None else _v
        _v = arg.pop("spikecolor", None)
        self["spikecolor"] = spikecolor if spikecolor is not None else _v
        _v = arg.pop("spikedash", None)
        self["spikedash"] = spikedash if spikedash is not None else _v
        _v = arg.pop("spikemode", None)
        self["spikemode"] = spikemode if spikemode is not None else _v
        _v = arg.pop("spikesnap", None)
        self["spikesnap"] = spikesnap if spikesnap is not None else _v
        _v = arg.pop("spikethickness", None)
        self["spikethickness"] = spikethickness if spikethickness is not None else _v
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
        _v = arg.pop("tickson", None)
        self["tickson"] = tickson if tickson is not None else _v
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
        _v = arg.pop("zeroline", None)
        self["zeroline"] = zeroline if zeroline is not None else _v
        _v = arg.pop("zerolinecolor", None)
        self["zerolinecolor"] = zerolinecolor if zerolinecolor is not None else _v
        _v = arg.pop("zerolinewidth", None)
        self["zerolinewidth"] = zerolinewidth if zerolinewidth is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Updatemenu(_BaseLayoutHierarchyType):

    # active
    # ------
    @property
    def active(self):
        """
        Determines which button (by index starting from 0) is
        considered active.
    
        The 'active' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["active"]

    @active.setter
    def active(self, val):
        self["active"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the update menu buttons.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the update menu.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the update menu.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    # buttons
    # -------
    @property
    def buttons(self):
        """
        The 'buttons' property is a tuple of instances of
        Button that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.updatemenu.Button
          - A list or tuple of dicts of string/value properties that
            will be passed to the Button constructor
    
            Supported dict properties:
                
                args
                    Sets the arguments values to be passed to the
                    Plotly method set in `method` on click.
                execute
                    When true, the API method is executed. When
                    false, all other behaviors are the same and
                    command execution is skipped. This may be
                    useful when hooking into, for example, the
                    `plotly_buttonclicked` method and executing the
                    API command manually without losing the benefit
                    of the updatemenu automatically binding to the
                    state of the plot through the specification of
                    `method` and `args`.
                label
                    Sets the text label to appear on the button.
                method
                    Sets the Plotly method to be called on click.
                    If the `skip` method is used, the API
                    updatemenu will function as normal but will
                    perform no API calls and will not bind
                    automatically to state updates. This may be
                    used to create a component interface and attach
                    to updatemenu events manually via JavaScript.
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
                visible
                    Determines whether or not this button is
                    visible.

        Returns
        -------
        tuple[plotly.graph_objs.layout.updatemenu.Button]
        """
        return self["buttons"]

    @buttons.setter
    def buttons(self, val):
        self["buttons"] = val

    # buttondefaults
    # --------------
    @property
    def buttondefaults(self):
        """
        When used in a template (as
        layout.template.layout.updatemenu.buttondefaults), sets the
        default property values to use for elements of
        layout.updatemenu.buttons
    
        The 'buttondefaults' property is an instance of Button
        that may be specified as:
          - An instance of plotly.graph_objs.layout.updatemenu.Button
          - A dict of string/value properties that will be passed
            to the Button constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.updatemenu.Button
        """
        return self["buttondefaults"]

    @buttondefaults.setter
    def buttondefaults(self, val):
        self["buttondefaults"] = val

    # direction
    # ---------
    @property
    def direction(self):
        """
        Determines the direction in which the buttons are laid out,
        whether in a dropdown menu or a row/column of buttons. For
        `left` and `up`, the buttons will still appear in left-to-right
        or top-to-bottom order respectively.
    
        The 'direction' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'up', 'down']

        Returns
        -------
        Any
        """
        return self["direction"]

    @direction.setter
    def direction(self, val):
        self["direction"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the update menu button text.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.updatemenu.Font
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
        plotly.graph_objs.layout.updatemenu.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Sets the padding around the buttons or dropdown menu.
    
        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of plotly.graph_objs.layout.updatemenu.Pad
          - A dict of string/value properties that will be passed
            to the Pad constructor
    
            Supported dict properties:
                
                b
                    The amount of padding (in px) along the bottom
                    of the component.
                l
                    The amount of padding (in px) on the left side
                    of the component.
                r
                    The amount of padding (in px) on the right side
                    of the component.
                t
                    The amount of padding (in px) along the top of
                    the component.

        Returns
        -------
        plotly.graph_objs.layout.updatemenu.Pad
        """
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    # showactive
    # ----------
    @property
    def showactive(self):
        """
        Highlights active dropdown item or active button if true.
    
        The 'showactive' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showactive"]

    @showactive.setter
    def showactive(self, val):
        self["showactive"] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Determines whether the buttons are accessible via a dropdown
        menu or whether the buttons are stacked horizontally or
        vertically
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['dropdown', 'buttons']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not the update menu is visible.
    
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

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the update
        menu.
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the update menu's horizontal position anchor. This anchor
        binds the `x` position to the "left", "center" or "right" of
        the range selector.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the update
        menu.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the update menu's vertical position anchor This anchor
        binds the `y` position to the "top", "middle" or "bottom" of
        the range selector.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        active
            Determines which button (by index starting from 0) is
            considered active.
        bgcolor
            Sets the background color of the update menu buttons.
        bordercolor
            Sets the color of the border enclosing the update menu.
        borderwidth
            Sets the width (in px) of the border enclosing the
            update menu.
        buttons
            A tuple of
            plotly.graph_objects.layout.updatemenu.Button instances
            or dicts with compatible properties
        buttondefaults
            When used in a template (as
            layout.template.layout.updatemenu.buttondefaults), sets
            the default property values to use for elements of
            layout.updatemenu.buttons
        direction
            Determines the direction in which the buttons are laid
            out, whether in a dropdown menu or a row/column of
            buttons. For `left` and `up`, the buttons will still
            appear in left-to-right or top-to-bottom order
            respectively.
        font
            Sets the font of the update menu button text.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Sets the padding around the buttons or dropdown menu.
        showactive
            Highlights active dropdown item or active button if
            true.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Determines whether the buttons are accessible via a
            dropdown menu or whether the buttons are stacked
            horizontally or vertically
        visible
            Determines whether or not the update menu is visible.
        x
            Sets the x position (in normalized coordinates) of the
            update menu.
        xanchor
            Sets the update menu's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            update menu.
        yanchor
            Sets the update menu's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.
        """

    def __init__(
        self,
        arg=None,
        active=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        buttons=None,
        buttondefaults=None,
        direction=None,
        font=None,
        name=None,
        pad=None,
        showactive=None,
        templateitemname=None,
        type=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs
    ):
        """
        Construct a new Updatemenu object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Updatemenu
        active
            Determines which button (by index starting from 0) is
            considered active.
        bgcolor
            Sets the background color of the update menu buttons.
        bordercolor
            Sets the color of the border enclosing the update menu.
        borderwidth
            Sets the width (in px) of the border enclosing the
            update menu.
        buttons
            A tuple of
            plotly.graph_objects.layout.updatemenu.Button instances
            or dicts with compatible properties
        buttondefaults
            When used in a template (as
            layout.template.layout.updatemenu.buttondefaults), sets
            the default property values to use for elements of
            layout.updatemenu.buttons
        direction
            Determines the direction in which the buttons are laid
            out, whether in a dropdown menu or a row/column of
            buttons. For `left` and `up`, the buttons will still
            appear in left-to-right or top-to-bottom order
            respectively.
        font
            Sets the font of the update menu button text.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Sets the padding around the buttons or dropdown menu.
        showactive
            Highlights active dropdown item or active button if
            true.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Determines whether the buttons are accessible via a
            dropdown menu or whether the buttons are stacked
            horizontally or vertically
        visible
            Determines whether or not the update menu is visible.
        x
            Sets the x position (in normalized coordinates) of the
            update menu.
        xanchor
            Sets the update menu's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            update menu.
        yanchor
            Sets the update menu's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.

        Returns
        -------
        Updatemenu
        """
        super(Updatemenu, self).__init__("updatemenus")

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
The first argument to the plotly.graph_objs.layout.Updatemenu 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Updatemenu"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import updatemenu as v_updatemenu

        # Initialize validators
        # ---------------------
        self._validators["active"] = v_updatemenu.ActiveValidator()
        self._validators["bgcolor"] = v_updatemenu.BgcolorValidator()
        self._validators["bordercolor"] = v_updatemenu.BordercolorValidator()
        self._validators["borderwidth"] = v_updatemenu.BorderwidthValidator()
        self._validators["buttons"] = v_updatemenu.ButtonsValidator()
        self._validators["buttondefaults"] = v_updatemenu.ButtonValidator()
        self._validators["direction"] = v_updatemenu.DirectionValidator()
        self._validators["font"] = v_updatemenu.FontValidator()
        self._validators["name"] = v_updatemenu.NameValidator()
        self._validators["pad"] = v_updatemenu.PadValidator()
        self._validators["showactive"] = v_updatemenu.ShowactiveValidator()
        self._validators["templateitemname"] = v_updatemenu.TemplateitemnameValidator()
        self._validators["type"] = v_updatemenu.TypeValidator()
        self._validators["visible"] = v_updatemenu.VisibleValidator()
        self._validators["x"] = v_updatemenu.XValidator()
        self._validators["xanchor"] = v_updatemenu.XanchorValidator()
        self._validators["y"] = v_updatemenu.YValidator()
        self._validators["yanchor"] = v_updatemenu.YanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("active", None)
        self["active"] = active if active is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("buttons", None)
        self["buttons"] = buttons if buttons is not None else _v
        _v = arg.pop("buttondefaults", None)
        self["buttondefaults"] = buttondefaults if buttondefaults is not None else _v
        _v = arg.pop("direction", None)
        self["direction"] = direction if direction is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("pad", None)
        self["pad"] = pad if pad is not None else _v
        _v = arg.pop("showactive", None)
        self["showactive"] = showactive if showactive is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Transition(_BaseLayoutHierarchyType):

    # duration
    # --------
    @property
    def duration(self):
        """
        The duration of the transition, in milliseconds. If equal to
        zero, updates are synchronous.
    
        The 'duration' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["duration"]

    @duration.setter
    def duration(self, val):
        self["duration"] = val

    # easing
    # ------
    @property
    def easing(self):
        """
        The easing function used for the transition
    
        The 'easing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'quad', 'cubic', 'sin', 'exp', 'circle',
                'elastic', 'back', 'bounce', 'linear-in', 'quad-in',
                'cubic-in', 'sin-in', 'exp-in', 'circle-in', 'elastic-in',
                'back-in', 'bounce-in', 'linear-out', 'quad-out',
                'cubic-out', 'sin-out', 'exp-out', 'circle-out',
                'elastic-out', 'back-out', 'bounce-out', 'linear-in-out',
                'quad-in-out', 'cubic-in-out', 'sin-in-out', 'exp-in-out',
                'circle-in-out', 'elastic-in-out', 'back-in-out',
                'bounce-in-out']

        Returns
        -------
        Any
        """
        return self["easing"]

    @easing.setter
    def easing(self, val):
        self["easing"] = val

    # ordering
    # --------
    @property
    def ordering(self):
        """
        Determines whether the figure's layout or traces smoothly
        transitions during updates that make both traces and layout
        change.
    
        The 'ordering' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['layout first', 'traces first']

        Returns
        -------
        Any
        """
        return self["ordering"]

    @ordering.setter
    def ordering(self, val):
        self["ordering"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        duration
            The duration of the transition, in milliseconds. If
            equal to zero, updates are synchronous.
        easing
            The easing function used for the transition
        ordering
            Determines whether the figure's layout or traces
            smoothly transitions during updates that make both
            traces and layout change.
        """

    def __init__(self, arg=None, duration=None, easing=None, ordering=None, **kwargs):
        """
        Construct a new Transition object
        
        Sets transition options used during Plotly.react updates.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Transition
        duration
            The duration of the transition, in milliseconds. If
            equal to zero, updates are synchronous.
        easing
            The easing function used for the transition
        ordering
            Determines whether the figure's layout or traces
            smoothly transitions during updates that make both
            traces and layout change.

        Returns
        -------
        Transition
        """
        super(Transition, self).__init__("transition")

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
The first argument to the plotly.graph_objs.layout.Transition 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Transition"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import transition as v_transition

        # Initialize validators
        # ---------------------
        self._validators["duration"] = v_transition.DurationValidator()
        self._validators["easing"] = v_transition.EasingValidator()
        self._validators["ordering"] = v_transition.OrderingValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("duration", None)
        self["duration"] = duration if duration is not None else _v
        _v = arg.pop("easing", None)
        self["easing"] = easing if easing is not None else _v
        _v = arg.pop("ordering", None)
        self["ordering"] = ordering if ordering is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Title(_BaseLayoutHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets the title font. Note that the title's font used to be
        customized by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.title.Font
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
        plotly.graph_objs.layout.title.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Sets the padding of the title. Each padding value only applies
        when the corresponding `xanchor`/`yanchor` value is set
        accordingly. E.g. for left padding to take effect, `xanchor`
        must be set to "left". The same rule applies if
        `xanchor`/`yanchor` is determined automatically. Padding is
        muted if the respective anchor value is "middle*/*center".
    
        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of plotly.graph_objs.layout.title.Pad
          - A dict of string/value properties that will be passed
            to the Pad constructor
    
            Supported dict properties:
                
                b
                    The amount of padding (in px) along the bottom
                    of the component.
                l
                    The amount of padding (in px) on the left side
                    of the component.
                r
                    The amount of padding (in px) on the right side
                    of the component.
                t
                    The amount of padding (in px) along the top of
                    the component.

        Returns
        -------
        plotly.graph_objs.layout.title.Pad
        """
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the plot's title. Note that before the existence of
        `title.text`, the title's contents used to be defined as the
        `title` attribute itself. This behavior has been deprecated.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position with respect to `xref` in normalized
        coordinates from 0 (left) to 1 (right).
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the title's horizontal alignment with respect to its x
        position. "left" means that the title starts at x, "right"
        means that the title ends at x and "center" means that the
        title's center is at x. "auto" divides `xref` by three and
        calculates the `xanchor` value automatically based on the value
        of `x`.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the container `x` refers to. "container" spans the entire
        `width` of the plot. "paper" refers to the width of the
        plotting area only.
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['container', 'paper']

        Returns
        -------
        Any
        """
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position with respect to `yref` in normalized
        coordinates from 0 (bottom) to 1 (top). "auto" places the
        baseline of the title onto the vertical center of the top
        margin.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the title's vertical alignment with respect to its y
        position. "top" means that the title's cap line is at y,
        "bottom" means that the title's baseline is at y and "middle"
        means that the title's midline is at y. "auto" divides `yref`
        by three and calculates the `yanchor` value automatically based
        on the value of `y`.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the container `y` refers to. "container" spans the entire
        `height` of the plot. "paper" refers to the height of the
        plotting area only.
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['container', 'paper']

        Returns
        -------
        Any
        """
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets the title font. Note that the title's font used to
            be customized by the now deprecated `titlefont`
            attribute.
        pad
            Sets the padding of the title. Each padding value only
            applies when the corresponding `xanchor`/`yanchor`
            value is set accordingly. E.g. for left padding to take
            effect, `xanchor` must be set to "left". The same rule
            applies if `xanchor`/`yanchor` is determined
            automatically. Padding is muted if the respective
            anchor value is "middle*/*center".
        text
            Sets the plot's title. Note that before the existence
            of `title.text`, the title's contents used to be
            defined as the `title` attribute itself. This behavior
            has been deprecated.
        x
            Sets the x position with respect to `xref` in
            normalized coordinates from 0 (left) to 1 (right).
        xanchor
            Sets the title's horizontal alignment with respect to
            its x position. "left" means that the title starts at
            x, "right" means that the title ends at x and "center"
            means that the title's center is at x. "auto" divides
            `xref` by three and calculates the `xanchor` value
            automatically based on the value of `x`.
        xref
            Sets the container `x` refers to. "container" spans the
            entire `width` of the plot. "paper" refers to the width
            of the plotting area only.
        y
            Sets the y position with respect to `yref` in
            normalized coordinates from 0 (bottom) to 1 (top).
            "auto" places the baseline of the title onto the
            vertical center of the top margin.
        yanchor
            Sets the title's vertical alignment with respect to its
            y position. "top" means that the title's cap line is at
            y, "bottom" means that the title's baseline is at y and
            "middle" means that the title's midline is at y. "auto"
            divides `yref` by three and calculates the `yanchor`
            value automatically based on the value of `y`.
        yref
            Sets the container `y` refers to. "container" spans the
            entire `height` of the plot. "paper" refers to the
            height of the plotting area only.
        """

    def __init__(
        self,
        arg=None,
        font=None,
        pad=None,
        text=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        **kwargs
    ):
        """
        Construct a new Title object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Title
        font
            Sets the title font. Note that the title's font used to
            be customized by the now deprecated `titlefont`
            attribute.
        pad
            Sets the padding of the title. Each padding value only
            applies when the corresponding `xanchor`/`yanchor`
            value is set accordingly. E.g. for left padding to take
            effect, `xanchor` must be set to "left". The same rule
            applies if `xanchor`/`yanchor` is determined
            automatically. Padding is muted if the respective
            anchor value is "middle*/*center".
        text
            Sets the plot's title. Note that before the existence
            of `title.text`, the title's contents used to be
            defined as the `title` attribute itself. This behavior
            has been deprecated.
        x
            Sets the x position with respect to `xref` in
            normalized coordinates from 0 (left) to 1 (right).
        xanchor
            Sets the title's horizontal alignment with respect to
            its x position. "left" means that the title starts at
            x, "right" means that the title ends at x and "center"
            means that the title's center is at x. "auto" divides
            `xref` by three and calculates the `xanchor` value
            automatically based on the value of `x`.
        xref
            Sets the container `x` refers to. "container" spans the
            entire `width` of the plot. "paper" refers to the width
            of the plotting area only.
        y
            Sets the y position with respect to `yref` in
            normalized coordinates from 0 (bottom) to 1 (top).
            "auto" places the baseline of the title onto the
            vertical center of the top margin.
        yanchor
            Sets the title's vertical alignment with respect to its
            y position. "top" means that the title's cap line is at
            y, "bottom" means that the title's baseline is at y and
            "middle" means that the title's midline is at y. "auto"
            divides `yref` by three and calculates the `yanchor`
            value automatically based on the value of `y`.
        yref
            Sets the container `y` refers to. "container" spans the
            entire `height` of the plot. "paper" refers to the
            height of the plotting area only.

        Returns
        -------
        Title
        """
        super(Title, self).__init__("title")

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
The first argument to the plotly.graph_objs.layout.Title 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Title"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import title as v_title

        # Initialize validators
        # ---------------------
        self._validators["font"] = v_title.FontValidator()
        self._validators["pad"] = v_title.PadValidator()
        self._validators["text"] = v_title.TextValidator()
        self._validators["x"] = v_title.XValidator()
        self._validators["xanchor"] = v_title.XanchorValidator()
        self._validators["xref"] = v_title.XrefValidator()
        self._validators["y"] = v_title.YValidator()
        self._validators["yanchor"] = v_title.YanchorValidator()
        self._validators["yref"] = v_title.YrefValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("pad", None)
        self["pad"] = pad if pad is not None else _v
        _v = arg.pop("text", None)
        self["text"] = text if text is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("xref", None)
        self["xref"] = xref if xref is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v
        _v = arg.pop("yref", None)
        self["yref"] = yref if yref is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Ternary(_BaseLayoutHierarchyType):

    # aaxis
    # -----
    @property
    def aaxis(self):
        """
        The 'aaxis' property is an instance of Aaxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.ternary.Aaxis
          - A dict of string/value properties that will be passed
            to the Aaxis constructor
    
            Supported dict properties:
                
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                min
                    The minimum value visible on this axis. The
                    maximum is determined by the sum minus the
                    minimum values of the other two axes. The full
                    view corresponds to all the minima set to zero.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.ternary.
                    aaxis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.ternary.aaxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of layout.ternary.aaxis.tickformatstops
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
                    plotly.graph_objects.layout.ternary.aaxis.Title
                    instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.ternary.aaxis.title.font instead. Sets
                    this axis' title font. Note that the title's
                    font used to be customized by the now
                    deprecated `titlefont` attribute.
                uirevision
                    Controls persistence of user-driven changes in
                    axis `min`, and `title` if in `editable: true`
                    configuration. Defaults to
                    `ternary<N>.uirevision`.

        Returns
        -------
        plotly.graph_objs.layout.ternary.Aaxis
        """
        return self["aaxis"]

    @aaxis.setter
    def aaxis(self, val):
        self["aaxis"] = val

    # baxis
    # -----
    @property
    def baxis(self):
        """
        The 'baxis' property is an instance of Baxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.ternary.Baxis
          - A dict of string/value properties that will be passed
            to the Baxis constructor
    
            Supported dict properties:
                
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                min
                    The minimum value visible on this axis. The
                    maximum is determined by the sum minus the
                    minimum values of the other two axes. The full
                    view corresponds to all the minima set to zero.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.ternary.
                    baxis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.ternary.baxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of layout.ternary.baxis.tickformatstops
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
                    plotly.graph_objects.layout.ternary.baxis.Title
                    instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.ternary.baxis.title.font instead. Sets
                    this axis' title font. Note that the title's
                    font used to be customized by the now
                    deprecated `titlefont` attribute.
                uirevision
                    Controls persistence of user-driven changes in
                    axis `min`, and `title` if in `editable: true`
                    configuration. Defaults to
                    `ternary<N>.uirevision`.

        Returns
        -------
        plotly.graph_objs.layout.ternary.Baxis
        """
        return self["baxis"]

    @baxis.setter
    def baxis(self, val):
        self["baxis"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Set the background color of the subplot
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # caxis
    # -----
    @property
    def caxis(self):
        """
        The 'caxis' property is an instance of Caxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.ternary.Caxis
          - A dict of string/value properties that will be passed
            to the Caxis constructor
    
            Supported dict properties:
                
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                min
                    The minimum value visible on this axis. The
                    maximum is determined by the sum minus the
                    minimum values of the other two axes. The full
                    view corresponds to all the minima set to zero.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.ternary.
                    caxis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.ternary.caxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of layout.ternary.caxis.tickformatstops
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
                    plotly.graph_objects.layout.ternary.caxis.Title
                    instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.ternary.caxis.title.font instead. Sets
                    this axis' title font. Note that the title's
                    font used to be customized by the now
                    deprecated `titlefont` attribute.
                uirevision
                    Controls persistence of user-driven changes in
                    axis `min`, and `title` if in `editable: true`
                    configuration. Defaults to
                    `ternary<N>.uirevision`.

        Returns
        -------
        plotly.graph_objs.layout.ternary.Caxis
        """
        return self["caxis"]

    @caxis.setter
    def caxis(self, val):
        self["caxis"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.ternary.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this ternary
                    subplot .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this ternary subplot .
                x
                    Sets the horizontal domain of this ternary
                    subplot (in plot fraction).
                y
                    Sets the vertical domain of this ternary
                    subplot (in plot fraction).

        Returns
        -------
        plotly.graph_objs.layout.ternary.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # sum
    # ---
    @property
    def sum(self):
        """
        The number each triplet should sum to, and the maximum range of
        each axis
    
        The 'sum' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["sum"]

    @sum.setter
    def sum(self, val):
        self["sum"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in axis `min` and
        `title`, if not overridden in the individual axes. Defaults to
        `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        aaxis
            plotly.graph_objects.layout.ternary.Aaxis instance or
            dict with compatible properties
        baxis
            plotly.graph_objects.layout.ternary.Baxis instance or
            dict with compatible properties
        bgcolor
            Set the background color of the subplot
        caxis
            plotly.graph_objects.layout.ternary.Caxis instance or
            dict with compatible properties
        domain
            plotly.graph_objects.layout.ternary.Domain instance or
            dict with compatible properties
        sum
            The number each triplet should sum to, and the maximum
            range of each axis
        uirevision
            Controls persistence of user-driven changes in axis
            `min` and `title`, if not overridden in the individual
            axes. Defaults to `layout.uirevision`.
        """

    def __init__(
        self,
        arg=None,
        aaxis=None,
        baxis=None,
        bgcolor=None,
        caxis=None,
        domain=None,
        sum=None,
        uirevision=None,
        **kwargs
    ):
        """
        Construct a new Ternary object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Ternary
        aaxis
            plotly.graph_objects.layout.ternary.Aaxis instance or
            dict with compatible properties
        baxis
            plotly.graph_objects.layout.ternary.Baxis instance or
            dict with compatible properties
        bgcolor
            Set the background color of the subplot
        caxis
            plotly.graph_objects.layout.ternary.Caxis instance or
            dict with compatible properties
        domain
            plotly.graph_objects.layout.ternary.Domain instance or
            dict with compatible properties
        sum
            The number each triplet should sum to, and the maximum
            range of each axis
        uirevision
            Controls persistence of user-driven changes in axis
            `min` and `title`, if not overridden in the individual
            axes. Defaults to `layout.uirevision`.

        Returns
        -------
        Ternary
        """
        super(Ternary, self).__init__("ternary")

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
The first argument to the plotly.graph_objs.layout.Ternary 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Ternary"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import ternary as v_ternary

        # Initialize validators
        # ---------------------
        self._validators["aaxis"] = v_ternary.AaxisValidator()
        self._validators["baxis"] = v_ternary.BaxisValidator()
        self._validators["bgcolor"] = v_ternary.BgcolorValidator()
        self._validators["caxis"] = v_ternary.CaxisValidator()
        self._validators["domain"] = v_ternary.DomainValidator()
        self._validators["sum"] = v_ternary.SumValidator()
        self._validators["uirevision"] = v_ternary.UirevisionValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("aaxis", None)
        self["aaxis"] = aaxis if aaxis is not None else _v
        _v = arg.pop("baxis", None)
        self["baxis"] = baxis if baxis is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("caxis", None)
        self["caxis"] = caxis if caxis is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("sum", None)
        self["sum"] = sum if sum is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Template(_BaseLayoutHierarchyType):

    # data
    # ----
    @property
    def data(self):
        """
        The 'data' property is an instance of Data
        that may be specified as:
          - An instance of plotly.graph_objs.layout.template.Data
          - A dict of string/value properties that will be passed
            to the Data constructor
    
            Supported dict properties:
                
                area
                    A tuple of plotly.graph_objects.Area instances
                    or dicts with compatible properties
                barpolar
                    A tuple of plotly.graph_objects.Barpolar
                    instances or dicts with compatible properties
                bar
                    A tuple of plotly.graph_objects.Bar instances
                    or dicts with compatible properties
                box
                    A tuple of plotly.graph_objects.Box instances
                    or dicts with compatible properties
                candlestick
                    A tuple of plotly.graph_objects.Candlestick
                    instances or dicts with compatible properties
                carpet
                    A tuple of plotly.graph_objects.Carpet
                    instances or dicts with compatible properties
                choroplethmapbox
                    A tuple of
                    plotly.graph_objects.Choroplethmapbox instances
                    or dicts with compatible properties
                choropleth
                    A tuple of plotly.graph_objects.Choropleth
                    instances or dicts with compatible properties
                cone
                    A tuple of plotly.graph_objects.Cone instances
                    or dicts with compatible properties
                contourcarpet
                    A tuple of plotly.graph_objects.Contourcarpet
                    instances or dicts with compatible properties
                contour
                    A tuple of plotly.graph_objects.Contour
                    instances or dicts with compatible properties
                densitymapbox
                    A tuple of plotly.graph_objects.Densitymapbox
                    instances or dicts with compatible properties
                funnelarea
                    A tuple of plotly.graph_objects.Funnelarea
                    instances or dicts with compatible properties
                funnel
                    A tuple of plotly.graph_objects.Funnel
                    instances or dicts with compatible properties
                heatmapgl
                    A tuple of plotly.graph_objects.Heatmapgl
                    instances or dicts with compatible properties
                heatmap
                    A tuple of plotly.graph_objects.Heatmap
                    instances or dicts with compatible properties
                histogram2dcontour
                    A tuple of
                    plotly.graph_objects.Histogram2dContour
                    instances or dicts with compatible properties
                histogram2d
                    A tuple of plotly.graph_objects.Histogram2d
                    instances or dicts with compatible properties
                histogram
                    A tuple of plotly.graph_objects.Histogram
                    instances or dicts with compatible properties
                indicator
                    A tuple of plotly.graph_objects.Indicator
                    instances or dicts with compatible properties
                isosurface
                    A tuple of plotly.graph_objects.Isosurface
                    instances or dicts with compatible properties
                mesh3d
                    A tuple of plotly.graph_objects.Mesh3d
                    instances or dicts with compatible properties
                ohlc
                    A tuple of plotly.graph_objects.Ohlc instances
                    or dicts with compatible properties
                parcats
                    A tuple of plotly.graph_objects.Parcats
                    instances or dicts with compatible properties
                parcoords
                    A tuple of plotly.graph_objects.Parcoords
                    instances or dicts with compatible properties
                pie
                    A tuple of plotly.graph_objects.Pie instances
                    or dicts with compatible properties
                pointcloud
                    A tuple of plotly.graph_objects.Pointcloud
                    instances or dicts with compatible properties
                sankey
                    A tuple of plotly.graph_objects.Sankey
                    instances or dicts with compatible properties
                scatter3d
                    A tuple of plotly.graph_objects.Scatter3d
                    instances or dicts with compatible properties
                scattercarpet
                    A tuple of plotly.graph_objects.Scattercarpet
                    instances or dicts with compatible properties
                scattergeo
                    A tuple of plotly.graph_objects.Scattergeo
                    instances or dicts with compatible properties
                scattergl
                    A tuple of plotly.graph_objects.Scattergl
                    instances or dicts with compatible properties
                scattermapbox
                    A tuple of plotly.graph_objects.Scattermapbox
                    instances or dicts with compatible properties
                scatterpolargl
                    A tuple of plotly.graph_objects.Scatterpolargl
                    instances or dicts with compatible properties
                scatterpolar
                    A tuple of plotly.graph_objects.Scatterpolar
                    instances or dicts with compatible properties
                scatter
                    A tuple of plotly.graph_objects.Scatter
                    instances or dicts with compatible properties
                scatterternary
                    A tuple of plotly.graph_objects.Scatterternary
                    instances or dicts with compatible properties
                splom
                    A tuple of plotly.graph_objects.Splom instances
                    or dicts with compatible properties
                streamtube
                    A tuple of plotly.graph_objects.Streamtube
                    instances or dicts with compatible properties
                sunburst
                    A tuple of plotly.graph_objects.Sunburst
                    instances or dicts with compatible properties
                surface
                    A tuple of plotly.graph_objects.Surface
                    instances or dicts with compatible properties
                table
                    A tuple of plotly.graph_objects.Table instances
                    or dicts with compatible properties
                violin
                    A tuple of plotly.graph_objects.Violin
                    instances or dicts with compatible properties
                volume
                    A tuple of plotly.graph_objects.Volume
                    instances or dicts with compatible properties
                waterfall
                    A tuple of plotly.graph_objects.Waterfall
                    instances or dicts with compatible properties

        Returns
        -------
        plotly.graph_objs.layout.template.Data
        """
        return self["data"]

    @data.setter
    def data(self, val):
        self["data"] = val

    # layout
    # ------
    @property
    def layout(self):
        """
        The 'layout' property is an instance of Layout
        that may be specified as:
          - An instance of plotly.graph_objs.Layout
          - A dict of string/value properties that will be passed
            to the Layout constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.template.Layout
        """
        return self["layout"]

    @layout.setter
    def layout(self, val):
        self["layout"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        data
            plotly.graph_objects.layout.template.Data instance or
            dict with compatible properties
        layout
            plotly.graph_objects.Layout instance or dict with
            compatible properties
        """

    def __init__(self, arg=None, data=None, layout=None, **kwargs):
        """
        Construct a new Template object
        
        Default attributes to be applied to the plot. This should be a
        dict with format: `{'layout': layoutTemplate, 'data':
        {trace_type: [traceTemplate, ...], ...}}` where
        `layoutTemplate` is a dict matching the structure of
        `figure.layout` and `traceTemplate` is a dict matching the
        structure of the trace with type `trace_type` (e.g. 'scatter').
        Alternatively, this may be specified as an instance of
        plotly.graph_objs.layout.Template.  Trace templates are applied
        cyclically to traces of each type. Container arrays (eg
        `annotations`) have special handling: An object ending in
        `defaults` (eg `annotationdefaults`) is applied to each array
        item. But if an item has a `templateitemname` key we look in
        the template array for an item with matching `name` and apply
        that instead. If no matching `name` is found we mark the item
        invisible. Any named template item not referenced is appended
        to the end of the array, so this can be used to add a watermark
        annotation or a logo image, for example. To omit one of these
        items on the plot, make an item with matching
        `templateitemname` and `visible: false`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Template
        data
            plotly.graph_objects.layout.template.Data instance or
            dict with compatible properties
        layout
            plotly.graph_objects.Layout instance or dict with
            compatible properties

        Returns
        -------
        Template
        """
        super(Template, self).__init__("template")

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
The first argument to the plotly.graph_objs.layout.Template 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Template"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import template as v_template

        # Initialize validators
        # ---------------------
        self._validators["data"] = v_template.DataValidator()
        self._validators["layout"] = v_template.LayoutValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("data", None)
        self["data"] = data if data is not None else _v
        _v = arg.pop("layout", None)
        self["layout"] = layout if layout is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Slider(_BaseLayoutHierarchyType):

    # active
    # ------
    @property
    def active(self):
        """
        Determines which button (by index starting from 0) is
        considered active.
    
        The 'active' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["active"]

    @active.setter
    def active(self, val):
        self["active"] = val

    # activebgcolor
    # -------------
    @property
    def activebgcolor(self):
        """
        Sets the background color of the slider grip while dragging.
    
        The 'activebgcolor' property is a color and may be specified as:
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
        return self["activebgcolor"]

    @activebgcolor.setter
    def activebgcolor(self, val):
        self["activebgcolor"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the slider.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the slider.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the slider.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    # currentvalue
    # ------------
    @property
    def currentvalue(self):
        """
        The 'currentvalue' property is an instance of Currentvalue
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.Currentvalue
          - A dict of string/value properties that will be passed
            to the Currentvalue constructor
    
            Supported dict properties:
                
                font
                    Sets the font of the current value label text.
                offset
                    The amount of space, in pixels, between the
                    current value label and the slider.
                prefix
                    When currentvalue.visible is true, this sets
                    the prefix of the label.
                suffix
                    When currentvalue.visible is true, this sets
                    the suffix of the label.
                visible
                    Shows the currently-selected value above the
                    slider.
                xanchor
                    The alignment of the value readout relative to
                    the length of the slider.

        Returns
        -------
        plotly.graph_objs.layout.slider.Currentvalue
        """
        return self["currentvalue"]

    @currentvalue.setter
    def currentvalue(self, val):
        self["currentvalue"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the slider step labels.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.Font
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
        plotly.graph_objs.layout.slider.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # len
    # ---
    @property
    def len(self):
        """
        Sets the length of the slider This measure excludes the padding
        of both ends. That is, the slider's length is this length minus
        the padding on both ends.
    
        The 'len' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["len"]

    @len.setter
    def len(self, val):
        self["len"] = val

    # lenmode
    # -------
    @property
    def lenmode(self):
        """
        Determines whether this slider length is set in units of plot
        "fraction" or in *pixels. Use `len` to set the value.
    
        The 'lenmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        return self["lenmode"]

    @lenmode.setter
    def lenmode(self, val):
        self["lenmode"] = val

    # minorticklen
    # ------------
    @property
    def minorticklen(self):
        """
        Sets the length in pixels of minor step tick marks
    
        The 'minorticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["minorticklen"]

    @minorticklen.setter
    def minorticklen(self, val):
        self["minorticklen"] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Set the padding of the slider component along each side.
    
        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.Pad
          - A dict of string/value properties that will be passed
            to the Pad constructor
    
            Supported dict properties:
                
                b
                    The amount of padding (in px) along the bottom
                    of the component.
                l
                    The amount of padding (in px) on the left side
                    of the component.
                r
                    The amount of padding (in px) on the right side
                    of the component.
                t
                    The amount of padding (in px) along the top of
                    the component.

        Returns
        -------
        plotly.graph_objs.layout.slider.Pad
        """
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    # steps
    # -----
    @property
    def steps(self):
        """
        The 'steps' property is a tuple of instances of
        Step that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.slider.Step
          - A list or tuple of dicts of string/value properties that
            will be passed to the Step constructor
    
            Supported dict properties:
                
                args
                    Sets the arguments values to be passed to the
                    Plotly method set in `method` on slide.
                execute
                    When true, the API method is executed. When
                    false, all other behaviors are the same and
                    command execution is skipped. This may be
                    useful when hooking into, for example, the
                    `plotly_sliderchange` method and executing the
                    API command manually without losing the benefit
                    of the slider automatically binding to the
                    state of the plot through the specification of
                    `method` and `args`.
                label
                    Sets the text label to appear on the slider
                method
                    Sets the Plotly method to be called when the
                    slider value is changed. If the `skip` method
                    is used, the API slider will function as normal
                    but will perform no API calls and will not bind
                    automatically to state updates. This may be
                    used to create a component interface and attach
                    to slider events manually via JavaScript.
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
                    Sets the value of the slider step, used to
                    refer to the step programatically. Defaults to
                    the slider label if not provided.
                visible
                    Determines whether or not this step is included
                    in the slider.

        Returns
        -------
        tuple[plotly.graph_objs.layout.slider.Step]
        """
        return self["steps"]

    @steps.setter
    def steps(self, val):
        self["steps"] = val

    # stepdefaults
    # ------------
    @property
    def stepdefaults(self):
        """
        When used in a template (as
        layout.template.layout.slider.stepdefaults), sets the default
        property values to use for elements of layout.slider.steps
    
        The 'stepdefaults' property is an instance of Step
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.Step
          - A dict of string/value properties that will be passed
            to the Step constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.slider.Step
        """
        return self["stepdefaults"]

    @stepdefaults.setter
    def stepdefaults(self, val):
        self["stepdefaults"] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the color of the border enclosing the slider.
    
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

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the length in pixels of step tick marks
    
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

    # transition
    # ----------
    @property
    def transition(self):
        """
        The 'transition' property is an instance of Transition
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.Transition
          - A dict of string/value properties that will be passed
            to the Transition constructor
    
            Supported dict properties:
                
                duration
                    Sets the duration of the slider transition
                easing
                    Sets the easing function of the slider
                    transition

        Returns
        -------
        plotly.graph_objs.layout.slider.Transition
        """
        return self["transition"]

    @transition.setter
    def transition(self, val):
        self["transition"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not the slider is visible.
    
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

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the slider.
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the slider's horizontal position anchor. This anchor binds
        the `x` position to the "left", "center" or "right" of the
        range selector.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the slider.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the slider's vertical position anchor This anchor binds
        the `y` position to the "top", "middle" or "bottom" of the
        range selector.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        active
            Determines which button (by index starting from 0) is
            considered active.
        activebgcolor
            Sets the background color of the slider grip while
            dragging.
        bgcolor
            Sets the background color of the slider.
        bordercolor
            Sets the color of the border enclosing the slider.
        borderwidth
            Sets the width (in px) of the border enclosing the
            slider.
        currentvalue
            plotly.graph_objects.layout.slider.Currentvalue
            instance or dict with compatible properties
        font
            Sets the font of the slider step labels.
        len
            Sets the length of the slider This measure excludes the
            padding of both ends. That is, the slider's length is
            this length minus the padding on both ends.
        lenmode
            Determines whether this slider length is set in units
            of plot "fraction" or in *pixels. Use `len` to set the
            value.
        minorticklen
            Sets the length in pixels of minor step tick marks
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Set the padding of the slider component along each
            side.
        steps
            A tuple of plotly.graph_objects.layout.slider.Step
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.layout.slider.stepdefaults), sets the
            default property values to use for elements of
            layout.slider.steps
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        tickcolor
            Sets the color of the border enclosing the slider.
        ticklen
            Sets the length in pixels of step tick marks
        tickwidth
            Sets the tick width (in px).
        transition
            plotly.graph_objects.layout.slider.Transition instance
            or dict with compatible properties
        visible
            Determines whether or not the slider is visible.
        x
            Sets the x position (in normalized coordinates) of the
            slider.
        xanchor
            Sets the slider's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            slider.
        yanchor
            Sets the slider's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.
        """

    def __init__(
        self,
        arg=None,
        active=None,
        activebgcolor=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        currentvalue=None,
        font=None,
        len=None,
        lenmode=None,
        minorticklen=None,
        name=None,
        pad=None,
        steps=None,
        stepdefaults=None,
        templateitemname=None,
        tickcolor=None,
        ticklen=None,
        tickwidth=None,
        transition=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs
    ):
        """
        Construct a new Slider object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Slider
        active
            Determines which button (by index starting from 0) is
            considered active.
        activebgcolor
            Sets the background color of the slider grip while
            dragging.
        bgcolor
            Sets the background color of the slider.
        bordercolor
            Sets the color of the border enclosing the slider.
        borderwidth
            Sets the width (in px) of the border enclosing the
            slider.
        currentvalue
            plotly.graph_objects.layout.slider.Currentvalue
            instance or dict with compatible properties
        font
            Sets the font of the slider step labels.
        len
            Sets the length of the slider This measure excludes the
            padding of both ends. That is, the slider's length is
            this length minus the padding on both ends.
        lenmode
            Determines whether this slider length is set in units
            of plot "fraction" or in *pixels. Use `len` to set the
            value.
        minorticklen
            Sets the length in pixels of minor step tick marks
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Set the padding of the slider component along each
            side.
        steps
            A tuple of plotly.graph_objects.layout.slider.Step
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.layout.slider.stepdefaults), sets the
            default property values to use for elements of
            layout.slider.steps
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        tickcolor
            Sets the color of the border enclosing the slider.
        ticklen
            Sets the length in pixels of step tick marks
        tickwidth
            Sets the tick width (in px).
        transition
            plotly.graph_objects.layout.slider.Transition instance
            or dict with compatible properties
        visible
            Determines whether or not the slider is visible.
        x
            Sets the x position (in normalized coordinates) of the
            slider.
        xanchor
            Sets the slider's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            slider.
        yanchor
            Sets the slider's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.

        Returns
        -------
        Slider
        """
        super(Slider, self).__init__("sliders")

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
The first argument to the plotly.graph_objs.layout.Slider 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Slider"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import slider as v_slider

        # Initialize validators
        # ---------------------
        self._validators["active"] = v_slider.ActiveValidator()
        self._validators["activebgcolor"] = v_slider.ActivebgcolorValidator()
        self._validators["bgcolor"] = v_slider.BgcolorValidator()
        self._validators["bordercolor"] = v_slider.BordercolorValidator()
        self._validators["borderwidth"] = v_slider.BorderwidthValidator()
        self._validators["currentvalue"] = v_slider.CurrentvalueValidator()
        self._validators["font"] = v_slider.FontValidator()
        self._validators["len"] = v_slider.LenValidator()
        self._validators["lenmode"] = v_slider.LenmodeValidator()
        self._validators["minorticklen"] = v_slider.MinorticklenValidator()
        self._validators["name"] = v_slider.NameValidator()
        self._validators["pad"] = v_slider.PadValidator()
        self._validators["steps"] = v_slider.StepsValidator()
        self._validators["stepdefaults"] = v_slider.StepValidator()
        self._validators["templateitemname"] = v_slider.TemplateitemnameValidator()
        self._validators["tickcolor"] = v_slider.TickcolorValidator()
        self._validators["ticklen"] = v_slider.TicklenValidator()
        self._validators["tickwidth"] = v_slider.TickwidthValidator()
        self._validators["transition"] = v_slider.TransitionValidator()
        self._validators["visible"] = v_slider.VisibleValidator()
        self._validators["x"] = v_slider.XValidator()
        self._validators["xanchor"] = v_slider.XanchorValidator()
        self._validators["y"] = v_slider.YValidator()
        self._validators["yanchor"] = v_slider.YanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("active", None)
        self["active"] = active if active is not None else _v
        _v = arg.pop("activebgcolor", None)
        self["activebgcolor"] = activebgcolor if activebgcolor is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("currentvalue", None)
        self["currentvalue"] = currentvalue if currentvalue is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("len", None)
        self["len"] = len if len is not None else _v
        _v = arg.pop("lenmode", None)
        self["lenmode"] = lenmode if lenmode is not None else _v
        _v = arg.pop("minorticklen", None)
        self["minorticklen"] = minorticklen if minorticklen is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("pad", None)
        self["pad"] = pad if pad is not None else _v
        _v = arg.pop("steps", None)
        self["steps"] = steps if steps is not None else _v
        _v = arg.pop("stepdefaults", None)
        self["stepdefaults"] = stepdefaults if stepdefaults is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("tickcolor", None)
        self["tickcolor"] = tickcolor if tickcolor is not None else _v
        _v = arg.pop("ticklen", None)
        self["ticklen"] = ticklen if ticklen is not None else _v
        _v = arg.pop("tickwidth", None)
        self["tickwidth"] = tickwidth if tickwidth is not None else _v
        _v = arg.pop("transition", None)
        self["transition"] = transition if transition is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Shape(_BaseLayoutHierarchyType):

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the color filling the shape's interior.
    
        The 'fillcolor' property is a color and may be specified as:
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
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    # layer
    # -----
    @property
    def layer(self):
        """
        Specifies whether shapes are drawn below or above traces.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['below', 'above']

        Returns
        -------
        Any
        """
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.layout.shape.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the line color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.layout.shape.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the shape.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # path
    # ----
    @property
    def path(self):
        """
        For `type` "path" - a valid SVG path with the pixel values
        replaced by data values in `xsizemode`/`ysizemode` being
        "scaled" and taken unmodified as pixels relative to `xanchor`
        and `yanchor` in case of "pixel" size mode. There are a few
        restrictions / quirks only absolute instructions, not relative.
        So the allowed segments are: M, L, H, V, Q, C, T, S, and Z arcs
        (A) are not allowed because radius rx and ry are relative. In
        the future we could consider supporting relative commands, but
        we would have to decide on how to handle date and log axes.
        Note that even as is, Q and C Bezier paths that are smooth on
        linear axes may not be smooth on log, and vice versa. no
        chained "polybezier" commands - specify the segment type for
        each one. On category axes, values are numbers scaled to the
        serial numbers of categories because using the categories
        themselves there would be no way to describe fractional
        positions On data axes: because space and T are both normal
        components of path strings, we can't use either to separate
        date from time parts. Therefore we'll use underscore for this
        purpose: 2015-02-21_13:45:56.789
    
        The 'path' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["path"]

    @path.setter
    def path(self, val):
        self["path"] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Specifies the shape type to be drawn. If "line", a line is
        drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect to the axes'
        sizing mode. If "circle", a circle is drawn from
        ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius (|(`x0`+`x1`)/2 -
        `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with respect to the axes' sizing
        mode. If "rect", a rectangle is drawn linking (`x0`,`y0`),
        (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect
        to the axes' sizing mode. If "path", draw a custom SVG path
        using `path`. with respect to the axes' sizing mode.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circle', 'rect', 'path', 'line']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this shape is visible.
    
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

    # x0
    # --
    @property
    def x0(self):
        """
        Sets the shape's starting x position. See `type` and
        `xsizemode` for more info.
    
        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x0"]

    @x0.setter
    def x0(self, val):
        self["x0"] = val

    # x1
    # --
    @property
    def x1(self):
        """
        Sets the shape's end x position. See `type` and `xsizemode` for
        more info.
    
        The 'x1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x1"]

    @x1.setter
    def x1(self, val):
        self["x1"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Only relevant in conjunction with `xsizemode` set to "pixel".
        Specifies the anchor point on the x axis to which `x0`, `x1`
        and x coordinates within `path` are relative to. E.g. useful to
        attach a pixel sized shape to a certain data value. No effect
        when `xsizemode` not set to "pixel".
    
        The 'xanchor' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the shape's x coordinate axis. If set to an x axis id
        (e.g. "x" or "x2"), the `x` position refers to an x coordinate.
        If set to "paper", the `x` position refers to the distance from
        the left side of the plotting area in normalized coordinates
        where 0 (1) corresponds to the left (right) side. If the axis
        `type` is "log", then you must take the log of your desired
        range. If the axis `type` is "date", then you must convert the
        date to unix time in milliseconds.
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    # xsizemode
    # ---------
    @property
    def xsizemode(self):
        """
        Sets the shapes's sizing mode along the x axis. If set to
        "scaled", `x0`, `x1` and x coordinates within `path` refer to
        data values on the x axis or a fraction of the plot area's
        width (`xref` set to "paper"). If set to "pixel", `xanchor`
        specifies the x position in terms of data or plot fraction but
        `x0`, `x1` and x coordinates within `path` are pixels relative
        to `xanchor`. This way, the shape can have a fixed width while
        maintaining a position relative to data or plot fraction.
    
        The 'xsizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['scaled', 'pixel']

        Returns
        -------
        Any
        """
        return self["xsizemode"]

    @xsizemode.setter
    def xsizemode(self, val):
        self["xsizemode"] = val

    # y0
    # --
    @property
    def y0(self):
        """
        Sets the shape's starting y position. See `type` and
        `ysizemode` for more info.
    
        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y0"]

    @y0.setter
    def y0(self, val):
        self["y0"] = val

    # y1
    # --
    @property
    def y1(self):
        """
        Sets the shape's end y position. See `type` and `ysizemode` for
        more info.
    
        The 'y1' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y1"]

    @y1.setter
    def y1(self, val):
        self["y1"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Only relevant in conjunction with `ysizemode` set to "pixel".
        Specifies the anchor point on the y axis to which `y0`, `y1`
        and y coordinates within `path` are relative to. E.g. useful to
        attach a pixel sized shape to a certain data value. No effect
        when `ysizemode` not set to "pixel".
    
        The 'yanchor' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the annotation's y coordinate axis. If set to an y axis id
        (e.g. "y" or "y2"), the `y` position refers to an y coordinate
        If set to "paper", the `y` position refers to the distance from
        the bottom of the plotting area in normalized coordinates where
        0 (1) corresponds to the bottom (top).
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    # ysizemode
    # ---------
    @property
    def ysizemode(self):
        """
        Sets the shapes's sizing mode along the y axis. If set to
        "scaled", `y0`, `y1` and y coordinates within `path` refer to
        data values on the y axis or a fraction of the plot area's
        height (`yref` set to "paper"). If set to "pixel", `yanchor`
        specifies the y position in terms of data or plot fraction but
        `y0`, `y1` and y coordinates within `path` are pixels relative
        to `yanchor`. This way, the shape can have a fixed height while
        maintaining a position relative to data or plot fraction.
    
        The 'ysizemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['scaled', 'pixel']

        Returns
        -------
        Any
        """
        return self["ysizemode"]

    @ysizemode.setter
    def ysizemode(self, val):
        self["ysizemode"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fillcolor
            Sets the color filling the shape's interior.
        layer
            Specifies whether shapes are drawn below or above
            traces.
        line
            plotly.graph_objects.layout.shape.Line instance or dict
            with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where 0 (1) corresponds to
            the left (right) side. If the axis `type` is "log",
            then you must take the log of your desired range. If
            the axis `type` is "date", then you must convert the
            date to unix time in milliseconds.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.
        """

    def __init__(
        self,
        arg=None,
        fillcolor=None,
        layer=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        templateitemname=None,
        type=None,
        visible=None,
        x0=None,
        x1=None,
        xanchor=None,
        xref=None,
        xsizemode=None,
        y0=None,
        y1=None,
        yanchor=None,
        yref=None,
        ysizemode=None,
        **kwargs
    ):
        """
        Construct a new Shape object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Shape
        fillcolor
            Sets the color filling the shape's interior.
        layer
            Specifies whether shapes are drawn below or above
            traces.
        line
            plotly.graph_objects.layout.shape.Line instance or dict
            with compatible properties
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the shape.
        path
            For `type` "path" - a valid SVG path with the pixel
            values replaced by data values in
            `xsizemode`/`ysizemode` being "scaled" and taken
            unmodified as pixels relative to `xanchor` and
            `yanchor` in case of "pixel" size mode. There are a few
            restrictions / quirks only absolute instructions, not
            relative. So the allowed segments are: M, L, H, V, Q,
            C, T, S, and Z arcs (A) are not allowed because radius
            rx and ry are relative. In the future we could consider
            supporting relative commands, but we would have to
            decide on how to handle date and log axes. Note that
            even as is, Q and C Bezier paths that are smooth on
            linear axes may not be smooth on log, and vice versa.
            no chained "polybezier" commands - specify the segment
            type for each one. On category axes, values are numbers
            scaled to the serial numbers of categories because
            using the categories themselves there would be no way
            to describe fractional positions On data axes: because
            space and T are both normal components of path strings,
            we can't use either to separate date from time parts.
            Therefore we'll use underscore for this purpose:
            2015-02-21_13:45:56.789
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        type
            Specifies the shape type to be drawn. If "line", a line
            is drawn from (`x0`,`y0`) to (`x1`,`y1`) with respect
            to the axes' sizing mode. If "circle", a circle is
            drawn from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius
            (|(`x0`+`x1`)/2 - `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with
            respect to the axes' sizing mode. If "rect", a
            rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`),
            (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to
            the axes' sizing mode. If "path", draw a custom SVG
            path using `path`. with respect to the axes' sizing
            mode.
        visible
            Determines whether or not this shape is visible.
        x0
            Sets the shape's starting x position. See `type` and
            `xsizemode` for more info.
        x1
            Sets the shape's end x position. See `type` and
            `xsizemode` for more info.
        xanchor
            Only relevant in conjunction with `xsizemode` set to
            "pixel". Specifies the anchor point on the x axis to
            which `x0`, `x1` and x coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `xsizemode` not
            set to "pixel".
        xref
            Sets the shape's x coordinate axis. If set to an x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            coordinate. If set to "paper", the `x` position refers
            to the distance from the left side of the plotting area
            in normalized coordinates where 0 (1) corresponds to
            the left (right) side. If the axis `type` is "log",
            then you must take the log of your desired range. If
            the axis `type` is "date", then you must convert the
            date to unix time in milliseconds.
        xsizemode
            Sets the shapes's sizing mode along the x axis. If set
            to "scaled", `x0`, `x1` and x coordinates within `path`
            refer to data values on the x axis or a fraction of the
            plot area's width (`xref` set to "paper"). If set to
            "pixel", `xanchor` specifies the x position in terms of
            data or plot fraction but `x0`, `x1` and x coordinates
            within `path` are pixels relative to `xanchor`. This
            way, the shape can have a fixed width while maintaining
            a position relative to data or plot fraction.
        y0
            Sets the shape's starting y position. See `type` and
            `ysizemode` for more info.
        y1
            Sets the shape's end y position. See `type` and
            `ysizemode` for more info.
        yanchor
            Only relevant in conjunction with `ysizemode` set to
            "pixel". Specifies the anchor point on the y axis to
            which `y0`, `y1` and y coordinates within `path` are
            relative to. E.g. useful to attach a pixel sized shape
            to a certain data value. No effect when `ysizemode` not
            set to "pixel".
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        ysizemode
            Sets the shapes's sizing mode along the y axis. If set
            to "scaled", `y0`, `y1` and y coordinates within `path`
            refer to data values on the y axis or a fraction of the
            plot area's height (`yref` set to "paper"). If set to
            "pixel", `yanchor` specifies the y position in terms of
            data or plot fraction but `y0`, `y1` and y coordinates
            within `path` are pixels relative to `yanchor`. This
            way, the shape can have a fixed height while
            maintaining a position relative to data or plot
            fraction.

        Returns
        -------
        Shape
        """
        super(Shape, self).__init__("shapes")

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
The first argument to the plotly.graph_objs.layout.Shape 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Shape"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import shape as v_shape

        # Initialize validators
        # ---------------------
        self._validators["fillcolor"] = v_shape.FillcolorValidator()
        self._validators["layer"] = v_shape.LayerValidator()
        self._validators["line"] = v_shape.LineValidator()
        self._validators["name"] = v_shape.NameValidator()
        self._validators["opacity"] = v_shape.OpacityValidator()
        self._validators["path"] = v_shape.PathValidator()
        self._validators["templateitemname"] = v_shape.TemplateitemnameValidator()
        self._validators["type"] = v_shape.TypeValidator()
        self._validators["visible"] = v_shape.VisibleValidator()
        self._validators["x0"] = v_shape.X0Validator()
        self._validators["x1"] = v_shape.X1Validator()
        self._validators["xanchor"] = v_shape.XanchorValidator()
        self._validators["xref"] = v_shape.XrefValidator()
        self._validators["xsizemode"] = v_shape.XsizemodeValidator()
        self._validators["y0"] = v_shape.Y0Validator()
        self._validators["y1"] = v_shape.Y1Validator()
        self._validators["yanchor"] = v_shape.YanchorValidator()
        self._validators["yref"] = v_shape.YrefValidator()
        self._validators["ysizemode"] = v_shape.YsizemodeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("fillcolor", None)
        self["fillcolor"] = fillcolor if fillcolor is not None else _v
        _v = arg.pop("layer", None)
        self["layer"] = layer if layer is not None else _v
        _v = arg.pop("line", None)
        self["line"] = line if line is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("opacity", None)
        self["opacity"] = opacity if opacity is not None else _v
        _v = arg.pop("path", None)
        self["path"] = path if path is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("x0", None)
        self["x0"] = x0 if x0 is not None else _v
        _v = arg.pop("x1", None)
        self["x1"] = x1 if x1 is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("xref", None)
        self["xref"] = xref if xref is not None else _v
        _v = arg.pop("xsizemode", None)
        self["xsizemode"] = xsizemode if xsizemode is not None else _v
        _v = arg.pop("y0", None)
        self["y0"] = y0 if y0 is not None else _v
        _v = arg.pop("y1", None)
        self["y1"] = y1 if y1 is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v
        _v = arg.pop("yref", None)
        self["yref"] = yref if yref is not None else _v
        _v = arg.pop("ysizemode", None)
        self["ysizemode"] = ysizemode if ysizemode is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Scene(_BaseLayoutHierarchyType):

    # annotations
    # -----------
    @property
    def annotations(self):
        """
        The 'annotations' property is a tuple of instances of
        Annotation that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.scene.Annotation
          - A list or tuple of dicts of string/value properties that
            will be passed to the Annotation constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the `text`
                    within the box. Has an effect only if `text`
                    spans more two or more lines (i.e. `text`
                    contains one or more <br> HTML tags) or if an
                    explicit width is set to override the text
                    width.
                arrowcolor
                    Sets the color of the annotation arrow.
                arrowhead
                    Sets the end annotation arrow head style.
                arrowside
                    Sets the annotation arrow head position.
                arrowsize
                    Sets the size of the end annotation arrow head,
                    relative to `arrowwidth`. A value of 1
                    (default) gives a head about 3x as wide as the
                    line.
                arrowwidth
                    Sets the width (in px) of annotation arrow
                    line.
                ax
                    Sets the x component of the arrow tail about
                    the arrow head (in pixels).
                ay
                    Sets the y component of the arrow tail about
                    the arrow head (in pixels).
                bgcolor
                    Sets the background color of the annotation.
                bordercolor
                    Sets the color of the border enclosing the
                    annotation `text`.
                borderpad
                    Sets the padding (in px) between the `text` and
                    the enclosing border.
                borderwidth
                    Sets the width (in px) of the border enclosing
                    the annotation `text`.
                captureevents
                    Determines whether the annotation text box
                    captures mouse move and click events, or allows
                    those events to pass through to data points in
                    the plot that may be behind the annotation. By
                    default `captureevents` is False unless
                    `hovertext` is provided. If you use the event
                    `plotly_clickannotation` without `hovertext`
                    you must explicitly enable `captureevents`.
                font
                    Sets the annotation text font.
                height
                    Sets an explicit height for the text box. null
                    (default) lets the text set the box height.
                    Taller text will be clipped.
                hoverlabel
                    plotly.graph_objects.layout.scene.annotation.Ho
                    verlabel instance or dict with compatible
                    properties
                hovertext
                    Sets text to appear when hovering over this
                    annotation. If omitted or blank, no hover label
                    will appear.
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
                    Sets the opacity of the annotation (text +
                    arrow).
                showarrow
                    Determines whether or not the annotation is
                    drawn with an arrow. If True, `text` is placed
                    near the arrow's tail. If False, `text` lines
                    up with the `x` and `y` provided.
                standoff
                    Sets a distance, in pixels, to move the end
                    arrowhead away from the position it is pointing
                    at, for example to point at the edge of a
                    marker independent of zoom. Note that this
                    shortens the arrow from the `ax` / `ay` vector,
                    in contrast to `xshift` / `yshift` which moves
                    everything by this amount.
                startarrowhead
                    Sets the start annotation arrow head style.
                startarrowsize
                    Sets the size of the start annotation arrow
                    head, relative to `arrowwidth`. A value of 1
                    (default) gives a head about 3x as wide as the
                    line.
                startstandoff
                    Sets a distance, in pixels, to move the start
                    arrowhead away from the position it is pointing
                    at, for example to point at the edge of a
                    marker independent of zoom. Note that this
                    shortens the arrow from the `ax` / `ay` vector,
                    in contrast to `xshift` / `yshift` which moves
                    everything by this amount.
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
                text
                    Sets the text associated with this annotation.
                    Plotly uses a subset of HTML tags to do things
                    like newline (<br>), bold (<b></b>), italics
                    (<i></i>), hyperlinks (<a href='...'></a>).
                    Tags <em>, <sup>, <sub> <span> are also
                    supported.
                textangle
                    Sets the angle at which the `text` is drawn
                    with respect to the horizontal.
                valign
                    Sets the vertical alignment of the `text`
                    within the box. Has an effect only if an
                    explicit height is set to override the text
                    height.
                visible
                    Determines whether or not this annotation is
                    visible.
                width
                    Sets an explicit width for the text box. null
                    (default) lets the text set the box width.
                    Wider text will be clipped. There is no
                    automatic wrapping; use <br> to start a new
                    line.
                x
                    Sets the annotation's x position.
                xanchor
                    Sets the text box's horizontal position anchor
                    This anchor binds the `x` position to the
                    "left", "center" or "right" of the annotation.
                    For example, if `x` is set to 1, `xref` to
                    "paper" and `xanchor` to "right" then the
                    right-most portion of the annotation lines up
                    with the right-most edge of the plotting area.
                    If "auto", the anchor is equivalent to "center"
                    for data-referenced annotations or if there is
                    an arrow, whereas for paper-referenced with no
                    arrow, the anchor picked corresponds to the
                    closest side.
                xshift
                    Shifts the position of the whole annotation and
                    arrow to the right (positive) or left
                    (negative) by this many pixels.
                y
                    Sets the annotation's y position.
                yanchor
                    Sets the text box's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the annotation.
                    For example, if `y` is set to 1, `yref` to
                    "paper" and `yanchor` to "top" then the top-
                    most portion of the annotation lines up with
                    the top-most edge of the plotting area. If
                    "auto", the anchor is equivalent to "middle"
                    for data-referenced annotations or if there is
                    an arrow, whereas for paper-referenced with no
                    arrow, the anchor picked corresponds to the
                    closest side.
                yshift
                    Shifts the position of the whole annotation and
                    arrow up (positive) or down (negative) by this
                    many pixels.
                z
                    Sets the annotation's z position.

        Returns
        -------
        tuple[plotly.graph_objs.layout.scene.Annotation]
        """
        return self["annotations"]

    @annotations.setter
    def annotations(self, val):
        self["annotations"] = val

    # annotationdefaults
    # ------------------
    @property
    def annotationdefaults(self):
        """
        When used in a template (as
        layout.template.layout.scene.annotationdefaults), sets the
        default property values to use for elements of
        layout.scene.annotations
    
        The 'annotationdefaults' property is an instance of Annotation
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Annotation
          - A dict of string/value properties that will be passed
            to the Annotation constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.scene.Annotation
        """
        return self["annotationdefaults"]

    @annotationdefaults.setter
    def annotationdefaults(self, val):
        self["annotationdefaults"] = val

    # aspectmode
    # ----------
    @property
    def aspectmode(self):
        """
        If "cube", this scene's axes are drawn as a cube, regardless of
        the axes' ranges. If "data", this scene's axes are drawn in
        proportion with the axes' ranges. If "manual", this scene's
        axes are drawn in proportion with the input of "aspectratio"
        (the default behavior if "aspectratio" is provided). If "auto",
        this scene's axes are drawn using the results of "data" except
        when one axis is more than four times the size of the two
        others, where in that case the results of "cube" are used.
    
        The 'aspectmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'cube', 'data', 'manual']

        Returns
        -------
        Any
        """
        return self["aspectmode"]

    @aspectmode.setter
    def aspectmode(self, val):
        self["aspectmode"] = val

    # aspectratio
    # -----------
    @property
    def aspectratio(self):
        """
        Sets this scene's axis aspectratio.
    
        The 'aspectratio' property is an instance of Aspectratio
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Aspectratio
          - A dict of string/value properties that will be passed
            to the Aspectratio constructor
    
            Supported dict properties:
                
                x
    
                y
    
                z

        Returns
        -------
        plotly.graph_objs.layout.scene.Aspectratio
        """
        return self["aspectratio"]

    @aspectratio.setter
    def aspectratio(self, val):
        self["aspectratio"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # camera
    # ------
    @property
    def camera(self):
        """
        The 'camera' property is an instance of Camera
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Camera
          - A dict of string/value properties that will be passed
            to the Camera constructor
    
            Supported dict properties:
                
                center
                    Sets the (x,y,z) components of the 'center'
                    camera vector This vector determines the
                    translation (x,y,z) space about the center of
                    this scene. By default, there is no such
                    translation.
                eye
                    Sets the (x,y,z) components of the 'eye' camera
                    vector. This vector determines the view point
                    about the origin of this scene.
                projection
                    plotly.graph_objects.layout.scene.camera.Projec
                    tion instance or dict with compatible
                    properties
                up
                    Sets the (x,y,z) components of the 'up' camera
                    vector. This vector determines the up direction
                    of this scene with respect to the page. The
                    default is *{x: 0, y: 0, z: 1}* which means
                    that the z axis points up.

        Returns
        -------
        plotly.graph_objs.layout.scene.Camera
        """
        return self["camera"]

    @camera.setter
    def camera(self, val):
        self["camera"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this scene subplot
                    .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this scene subplot .
                x
                    Sets the horizontal domain of this scene
                    subplot (in plot fraction).
                y
                    Sets the vertical domain of this scene subplot
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.layout.scene.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # dragmode
    # --------
    @property
    def dragmode(self):
        """
        Determines the mode of drag interactions for this scene.
    
        The 'dragmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['orbit', 'turntable', 'zoom', 'pan', False]

        Returns
        -------
        Any
        """
        return self["dragmode"]

    @dragmode.setter
    def dragmode(self, val):
        self["dragmode"] = val

    # hovermode
    # ---------
    @property
    def hovermode(self):
        """
        Determines the mode of hover interactions for this scene.
    
        The 'hovermode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['closest', False]

        Returns
        -------
        Any
        """
        return self["hovermode"]

    @hovermode.setter
    def hovermode(self, val):
        self["hovermode"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in camera
        attributes. Defaults to `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        The 'xaxis' property is an instance of XAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.XAxis
          - A dict of string/value properties that will be passed
            to the XAxis constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
                backgroundcolor
                    Sets the background color of this axis' wall.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`. Set
                    `categoryorder` to *total ascending* or *total
                    descending* if order should be determined by
                    the numerical order of the values. Similarly,
                    the order can be determined by the min, max,
                    sum, mean or median of all the values.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If True, the axis lines are mirrored. If
                    "ticks", the axis lines and ticks are mirrored.
                    If False, mirroring is disable. If "all", axis
                    lines are mirrored on all shared-axes subplots.
                    If "allticks", axis lines and ticks are
                    mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                range
                    Sets the range of this axis. If the axis `type`
                    is "log", then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is "date", it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is "category", it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If "normal", the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If "nonnegative", the range is non-
                    negative, regardless of the input data. Applies
                    only to linear axes.
                separatethousands
                    If "true", even 4-digit integers are separated
                showaxeslabels
                    Sets whether or not this axis is labeled
                showbackground
                    Sets whether or not this axis' wall has a
                    background color.
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Sets whether or not spikes starting from data
                    points to this axis' wall are shown on hover.
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
                spikecolor
                    Sets the color of the spikes.
                spikesides
                    Sets whether or not spikes extending from the
                    projection data points to this axis' wall
                    boundaries are shown on hover.
                spikethickness
                    Sets the thickness (in px) of the spikes.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.scene.xa
                    xis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.scene.xaxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of layout.scene.xaxis.tickformatstops
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
                    plotly.graph_objects.layout.scene.xaxis.Title
                    instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.scene.xaxis.title.font instead. Sets
                    this axis' title font. Note that the title's
                    font used to be customized by the now
                    deprecated `titlefont` attribute.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If True, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.scene.XAxis
        """
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        The 'yaxis' property is an instance of YAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.YAxis
          - A dict of string/value properties that will be passed
            to the YAxis constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
                backgroundcolor
                    Sets the background color of this axis' wall.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`. Set
                    `categoryorder` to *total ascending* or *total
                    descending* if order should be determined by
                    the numerical order of the values. Similarly,
                    the order can be determined by the min, max,
                    sum, mean or median of all the values.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If True, the axis lines are mirrored. If
                    "ticks", the axis lines and ticks are mirrored.
                    If False, mirroring is disable. If "all", axis
                    lines are mirrored on all shared-axes subplots.
                    If "allticks", axis lines and ticks are
                    mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                range
                    Sets the range of this axis. If the axis `type`
                    is "log", then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is "date", it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is "category", it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If "normal", the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If "nonnegative", the range is non-
                    negative, regardless of the input data. Applies
                    only to linear axes.
                separatethousands
                    If "true", even 4-digit integers are separated
                showaxeslabels
                    Sets whether or not this axis is labeled
                showbackground
                    Sets whether or not this axis' wall has a
                    background color.
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Sets whether or not spikes starting from data
                    points to this axis' wall are shown on hover.
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
                spikecolor
                    Sets the color of the spikes.
                spikesides
                    Sets whether or not spikes extending from the
                    projection data points to this axis' wall
                    boundaries are shown on hover.
                spikethickness
                    Sets the thickness (in px) of the spikes.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.scene.ya
                    xis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.scene.yaxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of layout.scene.yaxis.tickformatstops
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
                    plotly.graph_objects.layout.scene.yaxis.Title
                    instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.scene.yaxis.title.font instead. Sets
                    this axis' title font. Note that the title's
                    font used to be customized by the now
                    deprecated `titlefont` attribute.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If True, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.scene.YAxis
        """
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    # zaxis
    # -----
    @property
    def zaxis(self):
        """
        The 'zaxis' property is an instance of ZAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.ZAxis
          - A dict of string/value properties that will be passed
            to the ZAxis constructor
    
            Supported dict properties:
                
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
                backgroundcolor
                    Sets the background color of this axis' wall.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`. Set
                    `categoryorder` to *total ascending* or *total
                    descending* if order should be determined by
                    the numerical order of the values. Similarly,
                    the order can be determined by the min, max,
                    sum, mean or median of all the values.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                mirror
                    Determines if the axis lines or/and ticks are
                    mirrored to the opposite side of the plotting
                    area. If True, the axis lines are mirrored. If
                    "ticks", the axis lines and ticks are mirrored.
                    If False, mirroring is disable. If "all", axis
                    lines are mirrored on all shared-axes subplots.
                    If "allticks", axis lines and ticks are
                    mirrored on all shared-axes subplots.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                range
                    Sets the range of this axis. If the axis `type`
                    is "log", then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is "date", it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is "category", it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If "normal", the range is computed in relation
                    to the extrema of the input data. If *tozero*`,
                    the range extends to 0, regardless of the input
                    data If "nonnegative", the range is non-
                    negative, regardless of the input data. Applies
                    only to linear axes.
                separatethousands
                    If "true", even 4-digit integers are separated
                showaxeslabels
                    Sets whether or not this axis is labeled
                showbackground
                    Sets whether or not this axis' wall has a
                    background color.
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
                showspikes
                    Sets whether or not spikes starting from data
                    points to this axis' wall are shown on hover.
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
                spikecolor
                    Sets the color of the spikes.
                spikesides
                    Sets whether or not spikes extending from the
                    projection data points to this axis' wall
                    boundaries are shown on hover.
                spikethickness
                    Sets the thickness (in px) of the spikes.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.scene.za
                    xis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.scene.zaxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of layout.scene.zaxis.tickformatstops
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
                    plotly.graph_objects.layout.scene.zaxis.Title
                    instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.scene.zaxis.title.font instead. Sets
                    this axis' title font. Note that the title's
                    font used to be customized by the now
                    deprecated `titlefont` attribute.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false
                zeroline
                    Determines whether or not a line is drawn at
                    along the 0 value of this axis. If True, the
                    zero line is drawn on top of the grid lines.
                zerolinecolor
                    Sets the line color of the zero line.
                zerolinewidth
                    Sets the width (in px) of the zero line.

        Returns
        -------
        plotly.graph_objs.layout.scene.ZAxis
        """
        return self["zaxis"]

    @zaxis.setter
    def zaxis(self, val):
        self["zaxis"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        annotations
            A tuple of plotly.graph_objects.layout.scene.Annotation
            instances or dicts with compatible properties
        annotationdefaults
            When used in a template (as
            layout.template.layout.scene.annotationdefaults), sets
            the default property values to use for elements of
            layout.scene.annotations
        aspectmode
            If "cube", this scene's axes are drawn as a cube,
            regardless of the axes' ranges. If "data", this scene's
            axes are drawn in proportion with the axes' ranges. If
            "manual", this scene's axes are drawn in proportion
            with the input of "aspectratio" (the default behavior
            if "aspectratio" is provided). If "auto", this scene's
            axes are drawn using the results of "data" except when
            one axis is more than four times the size of the two
            others, where in that case the results of "cube" are
            used.
        aspectratio
            Sets this scene's axis aspectratio.
        bgcolor

        camera
            plotly.graph_objects.layout.scene.Camera instance or
            dict with compatible properties
        domain
            plotly.graph_objects.layout.scene.Domain instance or
            dict with compatible properties
        dragmode
            Determines the mode of drag interactions for this
            scene.
        hovermode
            Determines the mode of hover interactions for this
            scene.
        uirevision
            Controls persistence of user-driven changes in camera
            attributes. Defaults to `layout.uirevision`.
        xaxis
            plotly.graph_objects.layout.scene.XAxis instance or
            dict with compatible properties
        yaxis
            plotly.graph_objects.layout.scene.YAxis instance or
            dict with compatible properties
        zaxis
            plotly.graph_objects.layout.scene.ZAxis instance or
            dict with compatible properties
        """

    def __init__(
        self,
        arg=None,
        annotations=None,
        annotationdefaults=None,
        aspectmode=None,
        aspectratio=None,
        bgcolor=None,
        camera=None,
        domain=None,
        dragmode=None,
        hovermode=None,
        uirevision=None,
        xaxis=None,
        yaxis=None,
        zaxis=None,
        **kwargs
    ):
        """
        Construct a new Scene object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Scene
        annotations
            A tuple of plotly.graph_objects.layout.scene.Annotation
            instances or dicts with compatible properties
        annotationdefaults
            When used in a template (as
            layout.template.layout.scene.annotationdefaults), sets
            the default property values to use for elements of
            layout.scene.annotations
        aspectmode
            If "cube", this scene's axes are drawn as a cube,
            regardless of the axes' ranges. If "data", this scene's
            axes are drawn in proportion with the axes' ranges. If
            "manual", this scene's axes are drawn in proportion
            with the input of "aspectratio" (the default behavior
            if "aspectratio" is provided). If "auto", this scene's
            axes are drawn using the results of "data" except when
            one axis is more than four times the size of the two
            others, where in that case the results of "cube" are
            used.
        aspectratio
            Sets this scene's axis aspectratio.
        bgcolor

        camera
            plotly.graph_objects.layout.scene.Camera instance or
            dict with compatible properties
        domain
            plotly.graph_objects.layout.scene.Domain instance or
            dict with compatible properties
        dragmode
            Determines the mode of drag interactions for this
            scene.
        hovermode
            Determines the mode of hover interactions for this
            scene.
        uirevision
            Controls persistence of user-driven changes in camera
            attributes. Defaults to `layout.uirevision`.
        xaxis
            plotly.graph_objects.layout.scene.XAxis instance or
            dict with compatible properties
        yaxis
            plotly.graph_objects.layout.scene.YAxis instance or
            dict with compatible properties
        zaxis
            plotly.graph_objects.layout.scene.ZAxis instance or
            dict with compatible properties

        Returns
        -------
        Scene
        """
        super(Scene, self).__init__("scene")

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
The first argument to the plotly.graph_objs.layout.Scene 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Scene"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import scene as v_scene

        # Initialize validators
        # ---------------------
        self._validators["annotations"] = v_scene.AnnotationsValidator()
        self._validators["annotationdefaults"] = v_scene.AnnotationValidator()
        self._validators["aspectmode"] = v_scene.AspectmodeValidator()
        self._validators["aspectratio"] = v_scene.AspectratioValidator()
        self._validators["bgcolor"] = v_scene.BgcolorValidator()
        self._validators["camera"] = v_scene.CameraValidator()
        self._validators["domain"] = v_scene.DomainValidator()
        self._validators["dragmode"] = v_scene.DragmodeValidator()
        self._validators["hovermode"] = v_scene.HovermodeValidator()
        self._validators["uirevision"] = v_scene.UirevisionValidator()
        self._validators["xaxis"] = v_scene.XAxisValidator()
        self._validators["yaxis"] = v_scene.YAxisValidator()
        self._validators["zaxis"] = v_scene.ZAxisValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("annotations", None)
        self["annotations"] = annotations if annotations is not None else _v
        _v = arg.pop("annotationdefaults", None)
        self["annotationdefaults"] = (
            annotationdefaults if annotationdefaults is not None else _v
        )
        _v = arg.pop("aspectmode", None)
        self["aspectmode"] = aspectmode if aspectmode is not None else _v
        _v = arg.pop("aspectratio", None)
        self["aspectratio"] = aspectratio if aspectratio is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("camera", None)
        self["camera"] = camera if camera is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("dragmode", None)
        self["dragmode"] = dragmode if dragmode is not None else _v
        _v = arg.pop("hovermode", None)
        self["hovermode"] = hovermode if hovermode is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v
        _v = arg.pop("xaxis", None)
        self["xaxis"] = xaxis if xaxis is not None else _v
        _v = arg.pop("yaxis", None)
        self["yaxis"] = yaxis if yaxis is not None else _v
        _v = arg.pop("zaxis", None)
        self["zaxis"] = zaxis if zaxis is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class RadialAxis(_BaseLayoutHierarchyType):

    # domain
    # ------
    @property
    def domain(self):
        """
        Polar chart subplots are not supported yet. This key has
        currently no effect.
    
        The 'domain' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'domain[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'domain[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # endpadding
    # ----------
    @property
    def endpadding(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots.
    
        The 'endpadding' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["endpadding"]

    @endpadding.setter
    def endpadding(self, val):
        self["endpadding"] = val

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the orientation (an angle with respect to the
        origin) of the radial axis.
    
        The 'orientation' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Defines the start and end point of this radial axis.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not the line bounding this
        radial axis will be shown on the figure.
    
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
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not the radial axis ticks will
        feature tick labels.
    
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

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the color of the tick lines on this radial axis.
    
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

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the length of the tick lines on this radial
        axis.
    
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

    # tickorientation
    # ---------------
    @property
    def tickorientation(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the orientation (from the paper perspective) of
        the radial axis tick labels.
    
        The 'tickorientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['horizontal', 'vertical']

        Returns
        -------
        Any
        """
        return self["tickorientation"]

    @tickorientation.setter
    def tickorientation(self, val):
        self["tickorientation"] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the length of the tick lines on this radial
        axis.
    
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

    # visible
    # -------
    @property
    def visible(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not this axis will be visible.
    
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
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots.
        orientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (an angle with
            respect to the origin) of the radial axis.
        range
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Defines the start and end point of
            this radial axis.
        showline
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the line
            bounding this radial axis will be shown on the figure.
        showticklabels
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the radial
            axis ticks will feature tick labels.
        tickcolor
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the color of the tick lines on
            this radial axis.
        ticklen
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this radial axis.
        tickorientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (from the paper
            perspective) of the radial axis tick labels.
        ticksuffix
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this radial axis.
        visible
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not this axis
            will be visible.
        """

    def __init__(
        self,
        arg=None,
        domain=None,
        endpadding=None,
        orientation=None,
        range=None,
        showline=None,
        showticklabels=None,
        tickcolor=None,
        ticklen=None,
        tickorientation=None,
        ticksuffix=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new RadialAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.RadialAxis
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots.
        orientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (an angle with
            respect to the origin) of the radial axis.
        range
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Defines the start and end point of
            this radial axis.
        showline
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the line
            bounding this radial axis will be shown on the figure.
        showticklabels
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the radial
            axis ticks will feature tick labels.
        tickcolor
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the color of the tick lines on
            this radial axis.
        ticklen
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this radial axis.
        tickorientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (from the paper
            perspective) of the radial axis tick labels.
        ticksuffix
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this radial axis.
        visible
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not this axis
            will be visible.

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
The first argument to the plotly.graph_objs.layout.RadialAxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.RadialAxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import radialaxis as v_radialaxis

        # Initialize validators
        # ---------------------
        self._validators["domain"] = v_radialaxis.DomainValidator()
        self._validators["endpadding"] = v_radialaxis.EndpaddingValidator()
        self._validators["orientation"] = v_radialaxis.OrientationValidator()
        self._validators["range"] = v_radialaxis.RangeValidator()
        self._validators["showline"] = v_radialaxis.ShowlineValidator()
        self._validators["showticklabels"] = v_radialaxis.ShowticklabelsValidator()
        self._validators["tickcolor"] = v_radialaxis.TickcolorValidator()
        self._validators["ticklen"] = v_radialaxis.TicklenValidator()
        self._validators["tickorientation"] = v_radialaxis.TickorientationValidator()
        self._validators["ticksuffix"] = v_radialaxis.TicksuffixValidator()
        self._validators["visible"] = v_radialaxis.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("endpadding", None)
        self["endpadding"] = endpadding if endpadding is not None else _v
        _v = arg.pop("orientation", None)
        self["orientation"] = orientation if orientation is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("showline", None)
        self["showline"] = showline if showline is not None else _v
        _v = arg.pop("showticklabels", None)
        self["showticklabels"] = showticklabels if showticklabels is not None else _v
        _v = arg.pop("tickcolor", None)
        self["tickcolor"] = tickcolor if tickcolor is not None else _v
        _v = arg.pop("ticklen", None)
        self["ticklen"] = ticklen if ticklen is not None else _v
        _v = arg.pop("tickorientation", None)
        self["tickorientation"] = tickorientation if tickorientation is not None else _v
        _v = arg.pop("ticksuffix", None)
        self["ticksuffix"] = ticksuffix if ticksuffix is not None else _v
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


class Polar(_BaseLayoutHierarchyType):

    # angularaxis
    # -----------
    @property
    def angularaxis(self):
        """
        The 'angularaxis' property is an instance of AngularAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.polar.AngularAxis
          - A dict of string/value properties that will be passed
            to the AngularAxis constructor
    
            Supported dict properties:
                
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`. Set
                    `categoryorder` to *total ascending* or *total
                    descending* if order should be determined by
                    the numerical order of the values. Similarly,
                    the order can be determined by the min, max,
                    sum, mean or median of all the values.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                direction
                    Sets the direction corresponding to positive
                    angles.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                period
                    Set the angular period. Has an effect only when
                    `angularaxis.type` is "category".
                rotation
                    Sets that start position (in degrees) of the
                    angular axis By default, polar subplots with
                    `direction` set to "counterclockwise" get a
                    `rotation` of 0 which corresponds to due East
                    (like what mathematicians prefer). In turn,
                    polar with `direction` set to "clockwise" get a
                    rotation of 90 which corresponds to due North
                    (like on a compass),
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
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
                thetaunit
                    Sets the format unit of the formatted "theta"
                    values. Has an effect only when
                    `angularaxis.type` is "linear".
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.polar.an
                    gularaxis.Tickformatstop instances or dicts
                    with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.polar.angularaxis.tickformatstopdefaults),
                    sets the default property values to use for
                    elements of
                    layout.polar.angularaxis.tickformatstops
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
                type
                    Sets the angular axis type. If "linear", set
                    `thetaunit` to determine the unit in which axis
                    value are shown. If *category, use `period` to
                    set the number of integer coordinates around
                    polar axis.
                uirevision
                    Controls persistence of user-driven changes in
                    axis `rotation`. Defaults to
                    `polar<N>.uirevision`.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false

        Returns
        -------
        plotly.graph_objs.layout.polar.AngularAxis
        """
        return self["angularaxis"]

    @angularaxis.setter
    def angularaxis(self, val):
        self["angularaxis"] = val

    # bargap
    # ------
    @property
    def bargap(self):
        """
        Sets the gap between bars of adjacent location coordinates.
        Values are unitless, they represent fractions of the minimum
        difference in bar positions in the data.
    
        The 'bargap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["bargap"]

    @bargap.setter
    def bargap(self, val):
        self["bargap"] = val

    # barmode
    # -------
    @property
    def barmode(self):
        """
        Determines how bars at the same location coordinate are
        displayed on the graph. With "stack", the bars are stacked on
        top of one another With "overlay", the bars are plotted over
        one another, you might need to an "opacity" to see multiple
        bars.
    
        The 'barmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['stack', 'overlay']

        Returns
        -------
        Any
        """
        return self["barmode"]

    @barmode.setter
    def barmode(self, val):
        self["barmode"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Set the background color of the subplot
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.polar.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this polar subplot
                    .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this polar subplot .
                x
                    Sets the horizontal domain of this polar
                    subplot (in plot fraction).
                y
                    Sets the vertical domain of this polar subplot
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.layout.polar.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # gridshape
    # ---------
    @property
    def gridshape(self):
        """
        Determines if the radial axis grid lines and angular axis line
        are drawn as "circular" sectors or as "linear" (polygon)
        sectors. Has an effect only when the angular axis has `type`
        "category". Note that `radialaxis.angle` is snapped to the
        angle of the closest vertex when `gridshape` is "circular" (so
        that radial axis scale is the same as the data scale).
    
        The 'gridshape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['circular', 'linear']

        Returns
        -------
        Any
        """
        return self["gridshape"]

    @gridshape.setter
    def gridshape(self, val):
        self["gridshape"] = val

    # hole
    # ----
    @property
    def hole(self):
        """
        Sets the fraction of the radius to cut out of the polar
        subplot.
    
        The 'hole' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["hole"]

    @hole.setter
    def hole(self, val):
        self["hole"] = val

    # radialaxis
    # ----------
    @property
    def radialaxis(self):
        """
        The 'radialaxis' property is an instance of RadialAxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.polar.RadialAxis
          - A dict of string/value properties that will be passed
            to the RadialAxis constructor
    
            Supported dict properties:
                
                angle
                    Sets the angle (in degrees) from which the
                    radial axis is drawn. Note that by default,
                    radial axis line on the theta=0 line
                    corresponds to a line pointing right (like what
                    mathematicians prefer). Defaults to the first
                    `polar.sector` angle.
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
                calendar
                    Sets the calendar system to use for `range` and
                    `tick0` if this is a date axis. This does not
                    set the calendar for interpreting data on this
                    axis, that's specified in the trace or via the
                    global `layout.calendar`
                categoryarray
                    Sets the order in which categories on this axis
                    appear. Only has an effect if `categoryorder`
                    is set to "array". Used with `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the case of
                    categorical variables. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`. Set
                    `categoryorder` to *total ascending* or *total
                    descending* if order should be determined by
                    the numerical order of the values. Similarly,
                    the order can be determined by the min, max,
                    sum, mean or median of all the values.
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
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
                gridcolor
                    Sets the color of the grid lines.
                gridwidth
                    Sets the width (in px) of the grid lines.
                hoverformat
                    Sets the hover text formatting rule using d3
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
                layer
                    Sets the layer on which this axis is displayed.
                    If *above traces*, this axis is displayed above
                    all the subplot's traces If *below traces*,
                    this axis is displayed below all the subplot's
                    traces, but above the grid lines. Useful when
                    used together with scatter-like traces with
                    `cliponaxis` set to False to show markers
                    and/or text nodes above this axis.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                range
                    Sets the range of this axis. If the axis `type`
                    is "log", then you must take the log of your
                    desired range (e.g. to set the range from 1 to
                    100, set the range from 0 to 2). If the axis
                    `type` is "date", it should be date strings,
                    like date data, though Date objects and unix
                    milliseconds will be accepted and converted to
                    strings. If the axis `type` is "category", it
                    should be numbers, using the scale where each
                    category is assigned a serial number from zero
                    in the order it appears.
                rangemode
                    If *tozero*`, the range extends to 0,
                    regardless of the input data If "nonnegative",
                    the range is non-negative, regardless of the
                    input data. If "normal", the range is computed
                    in relation to the extrema of the input data
                    (same behavior as for cartesian axes).
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showgrid
                    Determines whether or not grid lines are drawn.
                    If True, the grid lines are drawn at every tick
                    mark.
                showline
                    Determines whether or not a line bounding this
                    axis is drawn.
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
                side
                    Determines on which side of radial axis line
                    the tick and tick labels appear.
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
                    Sets the tick font.
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
                    A tuple of plotly.graph_objects.layout.polar.ra
                    dialaxis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.polar.radialaxis.tickformatstopdefaults),
                    sets the default property values to use for
                    elements of
                    layout.polar.radialaxis.tickformatstops
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
                    plotly.graph_objects.layout.polar.radialaxis.Ti
                    tle instance or dict with compatible properties
                titlefont
                    Deprecated: Please use
                    layout.polar.radialaxis.title.font instead.
                    Sets this axis' title font. Note that the
                    title's font used to be customized by the now
                    deprecated `titlefont` attribute.
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.
                uirevision
                    Controls persistence of user-driven changes in
                    axis `range`, `autorange`, `angle`, and `title`
                    if in `editable: true` configuration. Defaults
                    to `polar<N>.uirevision`.
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false

        Returns
        -------
        plotly.graph_objs.layout.polar.RadialAxis
        """
        return self["radialaxis"]

    @radialaxis.setter
    def radialaxis(self, val):
        self["radialaxis"] = val

    # sector
    # ------
    @property
    def sector(self):
        """
        Sets angular span of this polar subplot with two angles (in
        degrees). Sector are assumed to be spanned in the
        counterclockwise direction with 0 corresponding to rightmost
        limit of the polar subplot.
    
        The 'sector' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'sector[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'sector[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self["sector"]

    @sector.setter
    def sector(self, val):
        self["sector"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in axis attributes,
        if not overridden in the individual axes. Defaults to
        `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        angularaxis
            plotly.graph_objects.layout.polar.AngularAxis instance
            or dict with compatible properties
        bargap
            Sets the gap between bars of adjacent location
            coordinates. Values are unitless, they represent
            fractions of the minimum difference in bar positions in
            the data.
        barmode
            Determines how bars at the same location coordinate are
            displayed on the graph. With "stack", the bars are
            stacked on top of one another With "overlay", the bars
            are plotted over one another, you might need to an
            "opacity" to see multiple bars.
        bgcolor
            Set the background color of the subplot
        domain
            plotly.graph_objects.layout.polar.Domain instance or
            dict with compatible properties
        gridshape
            Determines if the radial axis grid lines and angular
            axis line are drawn as "circular" sectors or as
            "linear" (polygon) sectors. Has an effect only when the
            angular axis has `type` "category". Note that
            `radialaxis.angle` is snapped to the angle of the
            closest vertex when `gridshape` is "circular" (so that
            radial axis scale is the same as the data scale).
        hole
            Sets the fraction of the radius to cut out of the polar
            subplot.
        radialaxis
            plotly.graph_objects.layout.polar.RadialAxis instance
            or dict with compatible properties
        sector
            Sets angular span of this polar subplot with two angles
            (in degrees). Sector are assumed to be spanned in the
            counterclockwise direction with 0 corresponding to
            rightmost limit of the polar subplot.
        uirevision
            Controls persistence of user-driven changes in axis
            attributes, if not overridden in the individual axes.
            Defaults to `layout.uirevision`.
        """

    def __init__(
        self,
        arg=None,
        angularaxis=None,
        bargap=None,
        barmode=None,
        bgcolor=None,
        domain=None,
        gridshape=None,
        hole=None,
        radialaxis=None,
        sector=None,
        uirevision=None,
        **kwargs
    ):
        """
        Construct a new Polar object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Polar
        angularaxis
            plotly.graph_objects.layout.polar.AngularAxis instance
            or dict with compatible properties
        bargap
            Sets the gap between bars of adjacent location
            coordinates. Values are unitless, they represent
            fractions of the minimum difference in bar positions in
            the data.
        barmode
            Determines how bars at the same location coordinate are
            displayed on the graph. With "stack", the bars are
            stacked on top of one another With "overlay", the bars
            are plotted over one another, you might need to an
            "opacity" to see multiple bars.
        bgcolor
            Set the background color of the subplot
        domain
            plotly.graph_objects.layout.polar.Domain instance or
            dict with compatible properties
        gridshape
            Determines if the radial axis grid lines and angular
            axis line are drawn as "circular" sectors or as
            "linear" (polygon) sectors. Has an effect only when the
            angular axis has `type` "category". Note that
            `radialaxis.angle` is snapped to the angle of the
            closest vertex when `gridshape` is "circular" (so that
            radial axis scale is the same as the data scale).
        hole
            Sets the fraction of the radius to cut out of the polar
            subplot.
        radialaxis
            plotly.graph_objects.layout.polar.RadialAxis instance
            or dict with compatible properties
        sector
            Sets angular span of this polar subplot with two angles
            (in degrees). Sector are assumed to be spanned in the
            counterclockwise direction with 0 corresponding to
            rightmost limit of the polar subplot.
        uirevision
            Controls persistence of user-driven changes in axis
            attributes, if not overridden in the individual axes.
            Defaults to `layout.uirevision`.

        Returns
        -------
        Polar
        """
        super(Polar, self).__init__("polar")

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
The first argument to the plotly.graph_objs.layout.Polar 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Polar"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import polar as v_polar

        # Initialize validators
        # ---------------------
        self._validators["angularaxis"] = v_polar.AngularAxisValidator()
        self._validators["bargap"] = v_polar.BargapValidator()
        self._validators["barmode"] = v_polar.BarmodeValidator()
        self._validators["bgcolor"] = v_polar.BgcolorValidator()
        self._validators["domain"] = v_polar.DomainValidator()
        self._validators["gridshape"] = v_polar.GridshapeValidator()
        self._validators["hole"] = v_polar.HoleValidator()
        self._validators["radialaxis"] = v_polar.RadialAxisValidator()
        self._validators["sector"] = v_polar.SectorValidator()
        self._validators["uirevision"] = v_polar.UirevisionValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("angularaxis", None)
        self["angularaxis"] = angularaxis if angularaxis is not None else _v
        _v = arg.pop("bargap", None)
        self["bargap"] = bargap if bargap is not None else _v
        _v = arg.pop("barmode", None)
        self["barmode"] = barmode if barmode is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("gridshape", None)
        self["gridshape"] = gridshape if gridshape is not None else _v
        _v = arg.pop("hole", None)
        self["hole"] = hole if hole is not None else _v
        _v = arg.pop("radialaxis", None)
        self["radialaxis"] = radialaxis if radialaxis is not None else _v
        _v = arg.pop("sector", None)
        self["sector"] = sector if sector is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Modebar(_BaseLayoutHierarchyType):

    # activecolor
    # -----------
    @property
    def activecolor(self):
        """
        Sets the color of the active or hovered on icons in the
        modebar.
    
        The 'activecolor' property is a color and may be specified as:
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
        return self["activecolor"]

    @activecolor.setter
    def activecolor(self, val):
        self["activecolor"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the modebar.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the color of the icons in the modebar.
    
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

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Sets the orientation of the modebar.
    
        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes related to the
        modebar, including `hovermode`, `dragmode`, and `showspikes` at
        both the root level and inside subplots. Defaults to
        `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        activecolor
            Sets the color of the active or hovered on icons in the
            modebar.
        bgcolor
            Sets the background color of the modebar.
        color
            Sets the color of the icons in the modebar.
        orientation
            Sets the orientation of the modebar.
        uirevision
            Controls persistence of user-driven changes related to
            the modebar, including `hovermode`, `dragmode`, and
            `showspikes` at both the root level and inside
            subplots. Defaults to `layout.uirevision`.
        """

    def __init__(
        self,
        arg=None,
        activecolor=None,
        bgcolor=None,
        color=None,
        orientation=None,
        uirevision=None,
        **kwargs
    ):
        """
        Construct a new Modebar object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Modebar
        activecolor
            Sets the color of the active or hovered on icons in the
            modebar.
        bgcolor
            Sets the background color of the modebar.
        color
            Sets the color of the icons in the modebar.
        orientation
            Sets the orientation of the modebar.
        uirevision
            Controls persistence of user-driven changes related to
            the modebar, including `hovermode`, `dragmode`, and
            `showspikes` at both the root level and inside
            subplots. Defaults to `layout.uirevision`.

        Returns
        -------
        Modebar
        """
        super(Modebar, self).__init__("modebar")

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
The first argument to the plotly.graph_objs.layout.Modebar 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Modebar"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import modebar as v_modebar

        # Initialize validators
        # ---------------------
        self._validators["activecolor"] = v_modebar.ActivecolorValidator()
        self._validators["bgcolor"] = v_modebar.BgcolorValidator()
        self._validators["color"] = v_modebar.ColorValidator()
        self._validators["orientation"] = v_modebar.OrientationValidator()
        self._validators["uirevision"] = v_modebar.UirevisionValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("activecolor", None)
        self["activecolor"] = activecolor if activecolor is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("orientation", None)
        self["orientation"] = orientation if orientation is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Margin(_BaseLayoutHierarchyType):

    # autoexpand
    # ----------
    @property
    def autoexpand(self):
        """
        The 'autoexpand' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autoexpand"]

    @autoexpand.setter
    def autoexpand(self, val):
        self["autoexpand"] = val

    # b
    # -
    @property
    def b(self):
        """
        Sets the bottom margin (in px).
    
        The 'b' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["b"]

    @b.setter
    def b(self, val):
        self["b"] = val

    # l
    # -
    @property
    def l(self):
        """
        Sets the left margin (in px).
    
        The 'l' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["l"]

    @l.setter
    def l(self, val):
        self["l"] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Sets the amount of padding (in px) between the plotting area
        and the axis lines
    
        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["pad"]

    @pad.setter
    def pad(self, val):
        self["pad"] = val

    # r
    # -
    @property
    def r(self):
        """
        Sets the right margin (in px).
    
        The 'r' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["r"]

    @r.setter
    def r(self, val):
        self["r"] = val

    # t
    # -
    @property
    def t(self):
        """
        Sets the top margin (in px).
    
        The 't' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["t"]

    @t.setter
    def t(self, val):
        self["t"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autoexpand

        b
            Sets the bottom margin (in px).
        l
            Sets the left margin (in px).
        pad
            Sets the amount of padding (in px) between the plotting
            area and the axis lines
        r
            Sets the right margin (in px).
        t
            Sets the top margin (in px).
        """

    def __init__(
        self,
        arg=None,
        autoexpand=None,
        b=None,
        l=None,
        pad=None,
        r=None,
        t=None,
        **kwargs
    ):
        """
        Construct a new Margin object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Margin
        autoexpand

        b
            Sets the bottom margin (in px).
        l
            Sets the left margin (in px).
        pad
            Sets the amount of padding (in px) between the plotting
            area and the axis lines
        r
            Sets the right margin (in px).
        t
            Sets the top margin (in px).

        Returns
        -------
        Margin
        """
        super(Margin, self).__init__("margin")

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
The first argument to the plotly.graph_objs.layout.Margin 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Margin"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import margin as v_margin

        # Initialize validators
        # ---------------------
        self._validators["autoexpand"] = v_margin.AutoexpandValidator()
        self._validators["b"] = v_margin.BValidator()
        self._validators["l"] = v_margin.LValidator()
        self._validators["pad"] = v_margin.PadValidator()
        self._validators["r"] = v_margin.RValidator()
        self._validators["t"] = v_margin.TValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autoexpand", None)
        self["autoexpand"] = autoexpand if autoexpand is not None else _v
        _v = arg.pop("b", None)
        self["b"] = b if b is not None else _v
        _v = arg.pop("l", None)
        self["l"] = l if l is not None else _v
        _v = arg.pop("pad", None)
        self["pad"] = pad if pad is not None else _v
        _v = arg.pop("r", None)
        self["r"] = r if r is not None else _v
        _v = arg.pop("t", None)
        self["t"] = t if t is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Mapbox(_BaseLayoutHierarchyType):

    # accesstoken
    # -----------
    @property
    def accesstoken(self):
        """
        Sets the mapbox access token to be used for this mapbox map.
        Alternatively, the mapbox access token can be set in the
        configuration options under `mapboxAccessToken`. Note that
        accessToken are only required when `style` (e.g with values :
        basic, streets, outdoors, light, dark, satellite, satellite-
        streets ) and/or a layout layer references the Mapbox server.
    
        The 'accesstoken' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["accesstoken"]

    @accesstoken.setter
    def accesstoken(self, val):
        self["accesstoken"] = val

    # bearing
    # -------
    @property
    def bearing(self):
        """
        Sets the bearing angle of the map in degrees counter-clockwise
        from North (mapbox.bearing).
    
        The 'bearing' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["bearing"]

    @bearing.setter
    def bearing(self, val):
        self["bearing"] = val

    # center
    # ------
    @property
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.Center
          - A dict of string/value properties that will be passed
            to the Center constructor
    
            Supported dict properties:
                
                lat
                    Sets the latitude of the center of the map (in
                    degrees North).
                lon
                    Sets the longitude of the center of the map (in
                    degrees East).

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Center
        """
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
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

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # layers
    # ------
    @property
    def layers(self):
        """
        The 'layers' property is a tuple of instances of
        Layer that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.mapbox.Layer
          - A list or tuple of dicts of string/value properties that
            will be passed to the Layer constructor
    
            Supported dict properties:
                
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
                coordinates
                    Sets the coordinates array contains [longitude,
                    latitude] pairs for the image corners listed in
                    clockwise order: top left, top right, bottom
                    right, bottom left. Only has an effect for
                    "image" `sourcetype`.
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
                    (mapbox.layer.source). When `sourcetype` is set
                    to "geojson", `source` can be a URL to a
                    GeoJSON or a GeoJSON object. When `sourcetype`
                    is set to "vector" or "raster", `source` can be
                    a URL or an array of tile URLs. When
                    `sourcetype` is set to "image", `source` can be
                    a URL to an image.
                sourceattribution
                    Sets the attribution for this source.
                sourcelayer
                    Specifies the layer to use from a vector tile
                    source (mapbox.layer.source-layer). Required
                    for "vector" source type that supports multiple
                    layers.
                sourcetype
                    Sets the source type for this layer, that is
                    the type of the layer data.
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
                    Sets the layer type, that is the how the layer
                    data set in `source` will be rendered With
                    `sourcetype` set to "geojson", the following
                    values are allowed: "circle", "line", "fill"
                    and "symbol". but note that "line" and "fill"
                    are not compatible with Point GeoJSON
                    geometries. With `sourcetype` set to "vector",
                    the following values are allowed:  "circle",
                    "line", "fill" and "symbol". With `sourcetype`
                    set to "raster" or `*image*`, only the "raster"
                    value is allowed.
                visible
                    Determines whether this layer is displayed

        Returns
        -------
        tuple[plotly.graph_objs.layout.mapbox.Layer]
        """
        return self["layers"]

    @layers.setter
    def layers(self, val):
        self["layers"] = val

    # layerdefaults
    # -------------
    @property
    def layerdefaults(self):
        """
        When used in a template (as
        layout.template.layout.mapbox.layerdefaults), sets the default
        property values to use for elements of layout.mapbox.layers
    
        The 'layerdefaults' property is an instance of Layer
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.Layer
          - A dict of string/value properties that will be passed
            to the Layer constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Layer
        """
        return self["layerdefaults"]

    @layerdefaults.setter
    def layerdefaults(self, val):
        self["layerdefaults"] = val

    # pitch
    # -----
    @property
    def pitch(self):
        """
        Sets the pitch angle of the map (in degrees, where 0 means
        perpendicular to the surface of the map) (mapbox.pitch).
    
        The 'pitch' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["pitch"]

    @pitch.setter
    def pitch(self, val):
        self["pitch"] = val

    # style
    # -----
    @property
    def style(self):
        """
        Defines the map layers that are rendered by default below the
        trace layers defined in `data`, which are themselves by default
        rendered below the layers defined in `layout.mapbox.layers`.
        These layers can be defined either explicitly as a Mapbox Style
        object which can contain multiple layer definitions that load
        data from any public or private Tile Map Service (TMS or XYZ)
        or Web Map Service (WMS) or implicitly by using one of the
        built-in style objects which use WMSes which do not require any
        access tokens, or by using a default Mapbox style or custom
        Mapbox style URL, both of which require a Mapbox access token
        Note that Mapbox access token can be set in the `accesstoken`
        attribute or in the `mapboxAccessToken` config option.  Mapbox
        Style objects are of the form described in the Mapbox GL JS
        documentation available at https://docs.mapbox.com/mapbox-gl-
        js/style-spec  The built-in plotly.js styles objects are: open-
        street-map, white-bg, carto-positron, carto-darkmatter, stamen-
        terrain, stamen-toner, stamen-watercolor  The built-in Mapbox
        styles are: basic, streets, outdoors, light, dark, satellite,
        satellite-streets  Mapbox style URLs are of the form:
        mapbox://mapbox.mapbox-<name>-<version>
    
        The 'style' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["style"]

    @style.setter
    def style(self, val):
        self["style"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in the view:
        `center`, `zoom`, `bearing`, `pitch`. Defaults to
        `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # zoom
    # ----
    @property
    def zoom(self):
        """
        Sets the zoom level of the map (mapbox.zoom).
    
        The 'zoom' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["zoom"]

    @zoom.setter
    def zoom(self, val):
        self["zoom"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        accesstoken
            Sets the mapbox access token to be used for this mapbox
            map. Alternatively, the mapbox access token can be set
            in the configuration options under `mapboxAccessToken`.
            Note that accessToken are only required when `style`
            (e.g with values : basic, streets, outdoors, light,
            dark, satellite, satellite-streets ) and/or a layout
            layer references the Mapbox server.
        bearing
            Sets the bearing angle of the map in degrees counter-
            clockwise from North (mapbox.bearing).
        center
            plotly.graph_objects.layout.mapbox.Center instance or
            dict with compatible properties
        domain
            plotly.graph_objects.layout.mapbox.Domain instance or
            dict with compatible properties
        layers
            A tuple of plotly.graph_objects.layout.mapbox.Layer
            instances or dicts with compatible properties
        layerdefaults
            When used in a template (as
            layout.template.layout.mapbox.layerdefaults), sets the
            default property values to use for elements of
            layout.mapbox.layers
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map)
            (mapbox.pitch).
        style
            Defines the map layers that are rendered by default
            below the trace layers defined in `data`, which are
            themselves by default rendered below the layers defined
            in `layout.mapbox.layers`.  These layers can be defined
            either explicitly as a Mapbox Style object which can
            contain multiple layer definitions that load data from
            any public or private Tile Map Service (TMS or XYZ) or
            Web Map Service (WMS) or implicitly by using one of the
            built-in style objects which use WMSes which do not
            require any access tokens, or by using a default Mapbox
            style or custom Mapbox style URL, both of which require
            a Mapbox access token  Note that Mapbox access token
            can be set in the `accesstoken` attribute or in the
            `mapboxAccessToken` config option.  Mapbox Style
            objects are of the form described in the Mapbox GL JS
            documentation available at
            https://docs.mapbox.com/mapbox-gl-js/style-spec  The
            built-in plotly.js styles objects are: open-street-map,
            white-bg, carto-positron, carto-darkmatter, stamen-
            terrain, stamen-toner, stamen-watercolor  The built-in
            Mapbox styles are: basic, streets, outdoors, light,
            dark, satellite, satellite-streets  Mapbox style URLs
            are of the form:
            mapbox://mapbox.mapbox-<name>-<version>
        uirevision
            Controls persistence of user-driven changes in the
            view: `center`, `zoom`, `bearing`, `pitch`. Defaults to
            `layout.uirevision`.
        zoom
            Sets the zoom level of the map (mapbox.zoom).
        """

    def __init__(
        self,
        arg=None,
        accesstoken=None,
        bearing=None,
        center=None,
        domain=None,
        layers=None,
        layerdefaults=None,
        pitch=None,
        style=None,
        uirevision=None,
        zoom=None,
        **kwargs
    ):
        """
        Construct a new Mapbox object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Mapbox
        accesstoken
            Sets the mapbox access token to be used for this mapbox
            map. Alternatively, the mapbox access token can be set
            in the configuration options under `mapboxAccessToken`.
            Note that accessToken are only required when `style`
            (e.g with values : basic, streets, outdoors, light,
            dark, satellite, satellite-streets ) and/or a layout
            layer references the Mapbox server.
        bearing
            Sets the bearing angle of the map in degrees counter-
            clockwise from North (mapbox.bearing).
        center
            plotly.graph_objects.layout.mapbox.Center instance or
            dict with compatible properties
        domain
            plotly.graph_objects.layout.mapbox.Domain instance or
            dict with compatible properties
        layers
            A tuple of plotly.graph_objects.layout.mapbox.Layer
            instances or dicts with compatible properties
        layerdefaults
            When used in a template (as
            layout.template.layout.mapbox.layerdefaults), sets the
            default property values to use for elements of
            layout.mapbox.layers
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map)
            (mapbox.pitch).
        style
            Defines the map layers that are rendered by default
            below the trace layers defined in `data`, which are
            themselves by default rendered below the layers defined
            in `layout.mapbox.layers`.  These layers can be defined
            either explicitly as a Mapbox Style object which can
            contain multiple layer definitions that load data from
            any public or private Tile Map Service (TMS or XYZ) or
            Web Map Service (WMS) or implicitly by using one of the
            built-in style objects which use WMSes which do not
            require any access tokens, or by using a default Mapbox
            style or custom Mapbox style URL, both of which require
            a Mapbox access token  Note that Mapbox access token
            can be set in the `accesstoken` attribute or in the
            `mapboxAccessToken` config option.  Mapbox Style
            objects are of the form described in the Mapbox GL JS
            documentation available at
            https://docs.mapbox.com/mapbox-gl-js/style-spec  The
            built-in plotly.js styles objects are: open-street-map,
            white-bg, carto-positron, carto-darkmatter, stamen-
            terrain, stamen-toner, stamen-watercolor  The built-in
            Mapbox styles are: basic, streets, outdoors, light,
            dark, satellite, satellite-streets  Mapbox style URLs
            are of the form:
            mapbox://mapbox.mapbox-<name>-<version>
        uirevision
            Controls persistence of user-driven changes in the
            view: `center`, `zoom`, `bearing`, `pitch`. Defaults to
            `layout.uirevision`.
        zoom
            Sets the zoom level of the map (mapbox.zoom).

        Returns
        -------
        Mapbox
        """
        super(Mapbox, self).__init__("mapbox")

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
The first argument to the plotly.graph_objs.layout.Mapbox 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Mapbox"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import mapbox as v_mapbox

        # Initialize validators
        # ---------------------
        self._validators["accesstoken"] = v_mapbox.AccesstokenValidator()
        self._validators["bearing"] = v_mapbox.BearingValidator()
        self._validators["center"] = v_mapbox.CenterValidator()
        self._validators["domain"] = v_mapbox.DomainValidator()
        self._validators["layers"] = v_mapbox.LayersValidator()
        self._validators["layerdefaults"] = v_mapbox.LayerValidator()
        self._validators["pitch"] = v_mapbox.PitchValidator()
        self._validators["style"] = v_mapbox.StyleValidator()
        self._validators["uirevision"] = v_mapbox.UirevisionValidator()
        self._validators["zoom"] = v_mapbox.ZoomValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("accesstoken", None)
        self["accesstoken"] = accesstoken if accesstoken is not None else _v
        _v = arg.pop("bearing", None)
        self["bearing"] = bearing if bearing is not None else _v
        _v = arg.pop("center", None)
        self["center"] = center if center is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("layers", None)
        self["layers"] = layers if layers is not None else _v
        _v = arg.pop("layerdefaults", None)
        self["layerdefaults"] = layerdefaults if layerdefaults is not None else _v
        _v = arg.pop("pitch", None)
        self["pitch"] = pitch if pitch is not None else _v
        _v = arg.pop("style", None)
        self["style"] = style if style is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v
        _v = arg.pop("zoom", None)
        self["zoom"] = zoom if zoom is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Legend(_BaseLayoutHierarchyType):

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the legend background color.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the legend.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the legend.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used to text the legend items.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.legend.Font
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
        plotly.graph_objs.layout.legend.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # itemclick
    # ---------
    @property
    def itemclick(self):
        """
        Determines the behavior on legend item click. "toggle" toggles
        the visibility of the item clicked on the graph. "toggleothers"
        makes the clicked item the sole visible item on the graph.
        False disable legend item click interactions.
    
        The 'itemclick' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['toggle', 'toggleothers', False]

        Returns
        -------
        Any
        """
        return self["itemclick"]

    @itemclick.setter
    def itemclick(self, val):
        self["itemclick"] = val

    # itemdoubleclick
    # ---------------
    @property
    def itemdoubleclick(self):
        """
        Determines the behavior on legend item double-click. "toggle"
        toggles the visibility of the item clicked on the graph.
        "toggleothers" makes the clicked item the sole visible item on
        the graph. False disable legend item double-click interactions.
    
        The 'itemdoubleclick' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['toggle', 'toggleothers', False]

        Returns
        -------
        Any
        """
        return self["itemdoubleclick"]

    @itemdoubleclick.setter
    def itemdoubleclick(self, val):
        self["itemdoubleclick"] = val

    # itemsizing
    # ----------
    @property
    def itemsizing(self):
        """
        Determines if the legend items symbols scale with their
        corresponding "trace" attributes or remain "constant"
        independent of the symbol size on the graph.
    
        The 'itemsizing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'constant']

        Returns
        -------
        Any
        """
        return self["itemsizing"]

    @itemsizing.setter
    def itemsizing(self, val):
        self["itemsizing"] = val

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Sets the orientation of the legend.
    
        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        return self["orientation"]

    @orientation.setter
    def orientation(self, val):
        self["orientation"] = val

    # tracegroupgap
    # -------------
    @property
    def tracegroupgap(self):
        """
        Sets the amount of vertical space (in px) between legend
        groups.
    
        The 'tracegroupgap' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["tracegroupgap"]

    @tracegroupgap.setter
    def tracegroupgap(self, val):
        self["tracegroupgap"] = val

    # traceorder
    # ----------
    @property
    def traceorder(self):
        """
        Determines the order at which the legend items are displayed.
        If "normal", the items are displayed top-to-bottom in the same
        order as the input data. If "reversed", the items are displayed
        in the opposite order as "normal". If "grouped", the items are
        displayed in groups (when a trace `legendgroup` is provided).
        if "grouped+reversed", the items are displayed in the opposite
        order as "grouped".
    
        The 'traceorder' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['reversed', 'grouped'] joined with '+' characters
            (e.g. 'reversed+grouped')
            OR exactly one of ['normal'] (e.g. 'normal')

        Returns
        -------
        Any
        """
        return self["traceorder"]

    @traceorder.setter
    def traceorder(self, val):
        self["traceorder"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of legend-driven changes in trace and pie
        label visibility. Defaults to `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # valign
    # ------
    @property
    def valign(self):
        """
        Sets the vertical alignment of the symbols with respect to
        their associated text.
    
        The 'valign' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["valign"]

    @valign.setter
    def valign(self, val):
        self["valign"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the legend.
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the legend's horizontal position anchor. This anchor binds
        the `x` position to the "left", "center" or "right" of the
        legend.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the legend.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the legend's vertical position anchor This anchor binds
        the `y` position to the "top", "middle" or "bottom" of the
        legend.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Sets the legend background color.
        bordercolor
            Sets the color of the border enclosing the legend.
        borderwidth
            Sets the width (in px) of the border enclosing the
            legend.
        font
            Sets the font used to text the legend items.
        itemclick
            Determines the behavior on legend item click. "toggle"
            toggles the visibility of the item clicked on the
            graph. "toggleothers" makes the clicked item the sole
            visible item on the graph. False disable legend item
            click interactions.
        itemdoubleclick
            Determines the behavior on legend item double-click.
            "toggle" toggles the visibility of the item clicked on
            the graph. "toggleothers" makes the clicked item the
            sole visible item on the graph. False disable legend
            item double-click interactions.
        itemsizing
            Determines if the legend items symbols scale with their
            corresponding "trace" attributes or remain "constant"
            independent of the symbol size on the graph.
        orientation
            Sets the orientation of the legend.
        tracegroupgap
            Sets the amount of vertical space (in px) between
            legend groups.
        traceorder
            Determines the order at which the legend items are
            displayed. If "normal", the items are displayed top-to-
            bottom in the same order as the input data. If
            "reversed", the items are displayed in the opposite
            order as "normal". If "grouped", the items are
            displayed in groups (when a trace `legendgroup` is
            provided). if "grouped+reversed", the items are
            displayed in the opposite order as "grouped".
        uirevision
            Controls persistence of legend-driven changes in trace
            and pie label visibility. Defaults to
            `layout.uirevision`.
        valign
            Sets the vertical alignment of the symbols with respect
            to their associated text.
        x
            Sets the x position (in normalized coordinates) of the
            legend.
        xanchor
            Sets the legend's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the legend.
        y
            Sets the y position (in normalized coordinates) of the
            legend.
        yanchor
            Sets the legend's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the legend.
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        font=None,
        itemclick=None,
        itemdoubleclick=None,
        itemsizing=None,
        orientation=None,
        tracegroupgap=None,
        traceorder=None,
        uirevision=None,
        valign=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs
    ):
        """
        Construct a new Legend object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Legend
        bgcolor
            Sets the legend background color.
        bordercolor
            Sets the color of the border enclosing the legend.
        borderwidth
            Sets the width (in px) of the border enclosing the
            legend.
        font
            Sets the font used to text the legend items.
        itemclick
            Determines the behavior on legend item click. "toggle"
            toggles the visibility of the item clicked on the
            graph. "toggleothers" makes the clicked item the sole
            visible item on the graph. False disable legend item
            click interactions.
        itemdoubleclick
            Determines the behavior on legend item double-click.
            "toggle" toggles the visibility of the item clicked on
            the graph. "toggleothers" makes the clicked item the
            sole visible item on the graph. False disable legend
            item double-click interactions.
        itemsizing
            Determines if the legend items symbols scale with their
            corresponding "trace" attributes or remain "constant"
            independent of the symbol size on the graph.
        orientation
            Sets the orientation of the legend.
        tracegroupgap
            Sets the amount of vertical space (in px) between
            legend groups.
        traceorder
            Determines the order at which the legend items are
            displayed. If "normal", the items are displayed top-to-
            bottom in the same order as the input data. If
            "reversed", the items are displayed in the opposite
            order as "normal". If "grouped", the items are
            displayed in groups (when a trace `legendgroup` is
            provided). if "grouped+reversed", the items are
            displayed in the opposite order as "grouped".
        uirevision
            Controls persistence of legend-driven changes in trace
            and pie label visibility. Defaults to
            `layout.uirevision`.
        valign
            Sets the vertical alignment of the symbols with respect
            to their associated text.
        x
            Sets the x position (in normalized coordinates) of the
            legend.
        xanchor
            Sets the legend's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the legend.
        y
            Sets the y position (in normalized coordinates) of the
            legend.
        yanchor
            Sets the legend's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the legend.

        Returns
        -------
        Legend
        """
        super(Legend, self).__init__("legend")

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
The first argument to the plotly.graph_objs.layout.Legend 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Legend"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import legend as v_legend

        # Initialize validators
        # ---------------------
        self._validators["bgcolor"] = v_legend.BgcolorValidator()
        self._validators["bordercolor"] = v_legend.BordercolorValidator()
        self._validators["borderwidth"] = v_legend.BorderwidthValidator()
        self._validators["font"] = v_legend.FontValidator()
        self._validators["itemclick"] = v_legend.ItemclickValidator()
        self._validators["itemdoubleclick"] = v_legend.ItemdoubleclickValidator()
        self._validators["itemsizing"] = v_legend.ItemsizingValidator()
        self._validators["orientation"] = v_legend.OrientationValidator()
        self._validators["tracegroupgap"] = v_legend.TracegroupgapValidator()
        self._validators["traceorder"] = v_legend.TraceorderValidator()
        self._validators["uirevision"] = v_legend.UirevisionValidator()
        self._validators["valign"] = v_legend.ValignValidator()
        self._validators["x"] = v_legend.XValidator()
        self._validators["xanchor"] = v_legend.XanchorValidator()
        self._validators["y"] = v_legend.YValidator()
        self._validators["yanchor"] = v_legend.YanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("itemclick", None)
        self["itemclick"] = itemclick if itemclick is not None else _v
        _v = arg.pop("itemdoubleclick", None)
        self["itemdoubleclick"] = itemdoubleclick if itemdoubleclick is not None else _v
        _v = arg.pop("itemsizing", None)
        self["itemsizing"] = itemsizing if itemsizing is not None else _v
        _v = arg.pop("orientation", None)
        self["orientation"] = orientation if orientation is not None else _v
        _v = arg.pop("tracegroupgap", None)
        self["tracegroupgap"] = tracegroupgap if tracegroupgap is not None else _v
        _v = arg.pop("traceorder", None)
        self["traceorder"] = traceorder if traceorder is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v
        _v = arg.pop("valign", None)
        self["valign"] = valign if valign is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Image(_BaseLayoutHierarchyType):

    # layer
    # -----
    @property
    def layer(self):
        """
        Specifies whether images are drawn below or above traces. When
        `xref` and `yref` are both set to `paper`, image is drawn below
        the entire plot area.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['below', 'above']

        Returns
        -------
        Any
        """
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the image.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # sizex
    # -----
    @property
    def sizex(self):
        """
        Sets the image container size horizontally. The image will be
        sized based on the `position` value. When `xref` is set to
        `paper`, units are sized relative to the plot width.
    
        The 'sizex' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["sizex"]

    @sizex.setter
    def sizex(self, val):
        self["sizex"] = val

    # sizey
    # -----
    @property
    def sizey(self):
        """
        Sets the image container size vertically. The image will be
        sized based on the `position` value. When `yref` is set to
        `paper`, units are sized relative to the plot height.
    
        The 'sizey' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["sizey"]

    @sizey.setter
    def sizey(self, val):
        self["sizey"] = val

    # sizing
    # ------
    @property
    def sizing(self):
        """
        Specifies which dimension of the image to constrain.
    
        The 'sizing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fill', 'contain', 'stretch']

        Returns
        -------
        Any
        """
        return self["sizing"]

    @sizing.setter
    def sizing(self, val):
        self["sizing"] = val

    # source
    # ------
    @property
    def source(self):
        """
        Specifies the URL of the image to be used. The URL must be
        accessible from the domain where the plot code is run, and can
        be either relative or absolute.
    
        The 'source' property is an image URI that may be specified as:
          - A remote image URI string
            (e.g. 'http://www.somewhere.com/image.png')
          - A data URI image string
            (e.g. 'data:image/png;base64,iVBORw0KGgoAAAANSU')
          - A PIL.Image.Image object which will be immediately converted
            to a data URI image string
            See http://pillow.readthedocs.io/en/latest/reference/Image.html

        Returns
        -------
        str
        """
        return self["source"]

    @source.setter
    def source(self, val):
        self["source"] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this image is visible.
    
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

    # x
    # -
    @property
    def x(self):
        """
        Sets the image's x position. When `xref` is set to `paper`,
        units are sized relative to the plot height. See `xref` for
        more info
    
        The 'x' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the anchor for the x position
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the images's x coordinate axis. If set to a x axis id
        (e.g. "x" or "x2"), the `x` position refers to an x data
        coordinate If set to "paper", the `x` position refers to the
        distance from the left of plot in normalized coordinates where
        0 (1) corresponds to the left (right).
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the image's y position. When `yref` is set to `paper`,
        units are sized relative to the plot height. See `yref` for
        more info
    
        The 'y' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the anchor for the y position.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the images's y coordinate axis. If set to a y axis id
        (e.g. "y" or "y2"), the `y` position refers to a y data
        coordinate. If set to "paper", the `y` position refers to the
        distance from the bottom of the plot in normalized coordinates
        where 0 (1) corresponds to the bottom (top).
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        layer
            Specifies whether images are drawn below or above
            traces. When `xref` and `yref` are both set to `paper`,
            image is drawn below the entire plot area.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the image.
        sizex
            Sets the image container size horizontally. The image
            will be sized based on the `position` value. When
            `xref` is set to `paper`, units are sized relative to
            the plot width.
        sizey
            Sets the image container size vertically. The image
            will be sized based on the `position` value. When
            `yref` is set to `paper`, units are sized relative to
            the plot height.
        sizing
            Specifies which dimension of the image to constrain.
        source
            Specifies the URL of the image to be used. The URL must
            be accessible from the domain where the plot code is
            run, and can be either relative or absolute.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this image is visible.
        x
            Sets the image's x position. When `xref` is set to
            `paper`, units are sized relative to the plot height.
            See `xref` for more info
        xanchor
            Sets the anchor for the x position
        xref
            Sets the images's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            data coordinate If set to "paper", the `x` position
            refers to the distance from the left of plot in
            normalized coordinates where 0 (1) corresponds to the
            left (right).
        y
            Sets the image's y position. When `yref` is set to
            `paper`, units are sized relative to the plot height.
            See `yref` for more info
        yanchor
            Sets the anchor for the y position.
        yref
            Sets the images's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            data coordinate. If set to "paper", the `y` position
            refers to the distance from the bottom of the plot in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top).
        """

    def __init__(
        self,
        arg=None,
        layer=None,
        name=None,
        opacity=None,
        sizex=None,
        sizey=None,
        sizing=None,
        source=None,
        templateitemname=None,
        visible=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        **kwargs
    ):
        """
        Construct a new Image object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Image
        layer
            Specifies whether images are drawn below or above
            traces. When `xref` and `yref` are both set to `paper`,
            image is drawn below the entire plot area.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the image.
        sizex
            Sets the image container size horizontally. The image
            will be sized based on the `position` value. When
            `xref` is set to `paper`, units are sized relative to
            the plot width.
        sizey
            Sets the image container size vertically. The image
            will be sized based on the `position` value. When
            `yref` is set to `paper`, units are sized relative to
            the plot height.
        sizing
            Specifies which dimension of the image to constrain.
        source
            Specifies the URL of the image to be used. The URL must
            be accessible from the domain where the plot code is
            run, and can be either relative or absolute.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this image is visible.
        x
            Sets the image's x position. When `xref` is set to
            `paper`, units are sized relative to the plot height.
            See `xref` for more info
        xanchor
            Sets the anchor for the x position
        xref
            Sets the images's x coordinate axis. If set to a x axis
            id (e.g. "x" or "x2"), the `x` position refers to an x
            data coordinate If set to "paper", the `x` position
            refers to the distance from the left of plot in
            normalized coordinates where 0 (1) corresponds to the
            left (right).
        y
            Sets the image's y position. When `yref` is set to
            `paper`, units are sized relative to the plot height.
            See `yref` for more info
        yanchor
            Sets the anchor for the y position.
        yref
            Sets the images's y coordinate axis. If set to a y axis
            id (e.g. "y" or "y2"), the `y` position refers to a y
            data coordinate. If set to "paper", the `y` position
            refers to the distance from the bottom of the plot in
            normalized coordinates where 0 (1) corresponds to the
            bottom (top).

        Returns
        -------
        Image
        """
        super(Image, self).__init__("images")

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
The first argument to the plotly.graph_objs.layout.Image 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Image"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import image as v_image

        # Initialize validators
        # ---------------------
        self._validators["layer"] = v_image.LayerValidator()
        self._validators["name"] = v_image.NameValidator()
        self._validators["opacity"] = v_image.OpacityValidator()
        self._validators["sizex"] = v_image.SizexValidator()
        self._validators["sizey"] = v_image.SizeyValidator()
        self._validators["sizing"] = v_image.SizingValidator()
        self._validators["source"] = v_image.SourceValidator()
        self._validators["templateitemname"] = v_image.TemplateitemnameValidator()
        self._validators["visible"] = v_image.VisibleValidator()
        self._validators["x"] = v_image.XValidator()
        self._validators["xanchor"] = v_image.XanchorValidator()
        self._validators["xref"] = v_image.XrefValidator()
        self._validators["y"] = v_image.YValidator()
        self._validators["yanchor"] = v_image.YanchorValidator()
        self._validators["yref"] = v_image.YrefValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("layer", None)
        self["layer"] = layer if layer is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("opacity", None)
        self["opacity"] = opacity if opacity is not None else _v
        _v = arg.pop("sizex", None)
        self["sizex"] = sizex if sizex is not None else _v
        _v = arg.pop("sizey", None)
        self["sizey"] = sizey if sizey is not None else _v
        _v = arg.pop("sizing", None)
        self["sizing"] = sizing if sizing is not None else _v
        _v = arg.pop("source", None)
        self["source"] = source if source is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("xref", None)
        self["xref"] = xref if xref is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v
        _v = arg.pop("yref", None)
        self["yref"] = yref if yref is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Hoverlabel(_BaseLayoutHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the text content within hover
        label box. Has an effect only if the hover label text spans
        more two or more lines
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'auto']

        Returns
        -------
        Any
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of all hover labels on graph
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the border color of all hover labels on graph.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the default hover label font used by all traces on the
        graph.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.hoverlabel.Font
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
        plotly.graph_objs.layout.hoverlabel.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # namelength
    # ----------
    @property
    def namelength(self):
        """
        Sets the default length (in number of characters) of the trace
        name in the hover labels for all traces. -1 shows the whole
        name regardless of length. 0-3 shows the first 0-3 characters,
        and an integer >3 will show the whole name if it is less than
        that many characters, but if it is longer, will truncate to
        `namelength - 3` characters and add an ellipsis.
    
        The 'namelength' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["namelength"]

    @namelength.setter
    def namelength(self, val):
        self["namelength"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        bgcolor
            Sets the background color of all hover labels on graph
        bordercolor
            Sets the border color of all hover labels on graph.
        font
            Sets the default hover label font used by all traces on
            the graph.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.
        """

    def __init__(
        self,
        arg=None,
        align=None,
        bgcolor=None,
        bordercolor=None,
        font=None,
        namelength=None,
        **kwargs
    ):
        """
        Construct a new Hoverlabel object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Hoverlabel
        align
            Sets the horizontal alignment of the text content
            within hover label box. Has an effect only if the hover
            label text spans more two or more lines
        bgcolor
            Sets the background color of all hover labels on graph
        bordercolor
            Sets the border color of all hover labels on graph.
        font
            Sets the default hover label font used by all traces on
            the graph.
        namelength
            Sets the default length (in number of characters) of
            the trace name in the hover labels for all traces. -1
            shows the whole name regardless of length. 0-3 shows
            the first 0-3 characters, and an integer >3 will show
            the whole name if it is less than that many characters,
            but if it is longer, will truncate to `namelength - 3`
            characters and add an ellipsis.

        Returns
        -------
        Hoverlabel
        """
        super(Hoverlabel, self).__init__("hoverlabel")

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
The first argument to the plotly.graph_objs.layout.Hoverlabel 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Hoverlabel"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import hoverlabel as v_hoverlabel

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_hoverlabel.AlignValidator()
        self._validators["bgcolor"] = v_hoverlabel.BgcolorValidator()
        self._validators["bordercolor"] = v_hoverlabel.BordercolorValidator()
        self._validators["font"] = v_hoverlabel.FontValidator()
        self._validators["namelength"] = v_hoverlabel.NamelengthValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("namelength", None)
        self["namelength"] = namelength if namelength is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Grid(_BaseLayoutHierarchyType):

    # columns
    # -------
    @property
    def columns(self):
        """
        The number of columns in the grid. If you provide a 2D
        `subplots` array, the length of its longest row is used as the
        default. If you give an `xaxes` array, its length is used as
        the default. But it's also possible to have a different length,
        if you want to leave a row at the end for non-cartesian
        subplots.
    
        The 'columns' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["columns"]

    @columns.setter
    def columns(self, val):
        self["columns"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.grid.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                x
                    Sets the horizontal domain of this grid subplot
                    (in plot fraction). The first and last cells
                    end exactly at the domain edges, with no grout
                    around the edges.
                y
                    Sets the vertical domain of this grid subplot
                    (in plot fraction). The first and last cells
                    end exactly at the domain edges, with no grout
                    around the edges.

        Returns
        -------
        plotly.graph_objs.layout.grid.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # pattern
    # -------
    @property
    def pattern(self):
        """
        If no `subplots`, `xaxes`, or `yaxes` are given but we do have
        `rows` and `columns`, we can generate defaults using
        consecutive axis IDs, in two ways: "coupled" gives one x axis
        per column and one y axis per row. "independent" uses a new xy
        pair for each cell, left-to-right across each row then
        iterating rows according to `roworder`.
    
        The 'pattern' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['independent', 'coupled']

        Returns
        -------
        Any
        """
        return self["pattern"]

    @pattern.setter
    def pattern(self, val):
        self["pattern"] = val

    # roworder
    # --------
    @property
    def roworder(self):
        """
        Is the first row the top or the bottom? Note that columns are
        always enumerated from left to right.
    
        The 'roworder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top to bottom', 'bottom to top']

        Returns
        -------
        Any
        """
        return self["roworder"]

    @roworder.setter
    def roworder(self, val):
        self["roworder"] = val

    # rows
    # ----
    @property
    def rows(self):
        """
        The number of rows in the grid. If you provide a 2D `subplots`
        array or a `yaxes` array, its length is used as the default.
        But it's also possible to have a different length, if you want
        to leave a row at the end for non-cartesian subplots.
    
        The 'rows' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["rows"]

    @rows.setter
    def rows(self, val):
        self["rows"] = val

    # subplots
    # --------
    @property
    def subplots(self):
        """
        Used for freeform grids, where some axes may be shared across
        subplots but others are not. Each entry should be a cartesian
        subplot id, like "xy" or "x3y2", or "" to leave that cell
        empty. You may reuse x axes within the same column, and y axes
        within the same row. Non-cartesian subplots and traces that
        support `domain` can place themselves in this grid separately
        using the `gridcell` attribute.
    
        The 'subplots' property is an info array that may be specified as:
        * a 2D list where:
          The 'subplots[i][j]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        return self["subplots"]

    @subplots.setter
    def subplots(self, val):
        self["subplots"] = val

    # xaxes
    # -----
    @property
    def xaxes(self):
        """
        Used with `yaxes` when the x and y axes are shared across
        columns and rows. Each entry should be an x axis id like "x",
        "x2", etc., or "" to not put an x axis in that column. Entries
        other than "" must be unique. Ignored if `subplots` is present.
        If missing but `yaxes` is present, will generate consecutive
        IDs.
    
        The 'xaxes' property is an info array that may be specified as:
        * a list of elements where:
          The 'xaxes[i]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        return self["xaxes"]

    @xaxes.setter
    def xaxes(self, val):
        self["xaxes"] = val

    # xgap
    # ----
    @property
    def xgap(self):
        """
        Horizontal space between grid cells, expressed as a fraction of
        the total width available to one cell. Defaults to 0.1 for
        coupled-axes grids and 0.2 for independent grids.
    
        The 'xgap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["xgap"]

    @xgap.setter
    def xgap(self, val):
        self["xgap"] = val

    # xside
    # -----
    @property
    def xside(self):
        """
        Sets where the x axis labels and titles go. "bottom" means the
        very bottom of the grid. "bottom plot" is the lowest plot that
        each x axis is used in. "top" and "top plot" are similar.
    
        The 'xside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['bottom', 'bottom plot', 'top plot', 'top']

        Returns
        -------
        Any
        """
        return self["xside"]

    @xside.setter
    def xside(self, val):
        self["xside"] = val

    # yaxes
    # -----
    @property
    def yaxes(self):
        """
        Used with `yaxes` when the x and y axes are shared across
        columns and rows. Each entry should be an y axis id like "y",
        "y2", etc., or "" to not put a y axis in that row. Entries
        other than "" must be unique. Ignored if `subplots` is present.
        If missing but `xaxes` is present, will generate consecutive
        IDs.
    
        The 'yaxes' property is an info array that may be specified as:
        * a list of elements where:
          The 'yaxes[i]' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        list
        """
        return self["yaxes"]

    @yaxes.setter
    def yaxes(self, val):
        self["yaxes"] = val

    # ygap
    # ----
    @property
    def ygap(self):
        """
        Vertical space between grid cells, expressed as a fraction of
        the total height available to one cell. Defaults to 0.1 for
        coupled-axes grids and 0.3 for independent grids.
    
        The 'ygap' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["ygap"]

    @ygap.setter
    def ygap(self, val):
        self["ygap"] = val

    # yside
    # -----
    @property
    def yside(self):
        """
        Sets where the y axis labels and titles go. "left" means the
        very left edge of the grid. *left plot* is the leftmost plot
        that each y axis is used in. "right" and *right plot* are
        similar.
    
        The 'yside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'left plot', 'right plot', 'right']

        Returns
        -------
        Any
        """
        return self["yside"]

    @yside.setter
    def yside(self, val):
        self["yside"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        columns
            The number of columns in the grid. If you provide a 2D
            `subplots` array, the length of its longest row is used
            as the default. If you give an `xaxes` array, its
            length is used as the default. But it's also possible
            to have a different length, if you want to leave a row
            at the end for non-cartesian subplots.
        domain
            plotly.graph_objects.layout.grid.Domain instance or
            dict with compatible properties
        pattern
            If no `subplots`, `xaxes`, or `yaxes` are given but we
            do have `rows` and `columns`, we can generate defaults
            using consecutive axis IDs, in two ways: "coupled"
            gives one x axis per column and one y axis per row.
            "independent" uses a new xy pair for each cell, left-
            to-right across each row then iterating rows according
            to `roworder`.
        roworder
            Is the first row the top or the bottom? Note that
            columns are always enumerated from left to right.
        rows
            The number of rows in the grid. If you provide a 2D
            `subplots` array or a `yaxes` array, its length is used
            as the default. But it's also possible to have a
            different length, if you want to leave a row at the end
            for non-cartesian subplots.
        subplots
            Used for freeform grids, where some axes may be shared
            across subplots but others are not. Each entry should
            be a cartesian subplot id, like "xy" or "x3y2", or ""
            to leave that cell empty. You may reuse x axes within
            the same column, and y axes within the same row. Non-
            cartesian subplots and traces that support `domain` can
            place themselves in this grid separately using the
            `gridcell` attribute.
        xaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an x axis
            id like "x", "x2", etc., or "" to not put an x axis in
            that column. Entries other than "" must be unique.
            Ignored if `subplots` is present. If missing but
            `yaxes` is present, will generate consecutive IDs.
        xgap
            Horizontal space between grid cells, expressed as a
            fraction of the total width available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.2 for
            independent grids.
        xside
            Sets where the x axis labels and titles go. "bottom"
            means the very bottom of the grid. "bottom plot" is the
            lowest plot that each x axis is used in. "top" and "top
            plot" are similar.
        yaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an y axis
            id like "y", "y2", etc., or "" to not put a y axis in
            that row. Entries other than "" must be unique. Ignored
            if `subplots` is present. If missing but `xaxes` is
            present, will generate consecutive IDs.
        ygap
            Vertical space between grid cells, expressed as a
            fraction of the total height available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.3 for
            independent grids.
        yside
            Sets where the y axis labels and titles go. "left"
            means the very left edge of the grid. *left plot* is
            the leftmost plot that each y axis is used in. "right"
            and *right plot* are similar.
        """

    def __init__(
        self,
        arg=None,
        columns=None,
        domain=None,
        pattern=None,
        roworder=None,
        rows=None,
        subplots=None,
        xaxes=None,
        xgap=None,
        xside=None,
        yaxes=None,
        ygap=None,
        yside=None,
        **kwargs
    ):
        """
        Construct a new Grid object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Grid
        columns
            The number of columns in the grid. If you provide a 2D
            `subplots` array, the length of its longest row is used
            as the default. If you give an `xaxes` array, its
            length is used as the default. But it's also possible
            to have a different length, if you want to leave a row
            at the end for non-cartesian subplots.
        domain
            plotly.graph_objects.layout.grid.Domain instance or
            dict with compatible properties
        pattern
            If no `subplots`, `xaxes`, or `yaxes` are given but we
            do have `rows` and `columns`, we can generate defaults
            using consecutive axis IDs, in two ways: "coupled"
            gives one x axis per column and one y axis per row.
            "independent" uses a new xy pair for each cell, left-
            to-right across each row then iterating rows according
            to `roworder`.
        roworder
            Is the first row the top or the bottom? Note that
            columns are always enumerated from left to right.
        rows
            The number of rows in the grid. If you provide a 2D
            `subplots` array or a `yaxes` array, its length is used
            as the default. But it's also possible to have a
            different length, if you want to leave a row at the end
            for non-cartesian subplots.
        subplots
            Used for freeform grids, where some axes may be shared
            across subplots but others are not. Each entry should
            be a cartesian subplot id, like "xy" or "x3y2", or ""
            to leave that cell empty. You may reuse x axes within
            the same column, and y axes within the same row. Non-
            cartesian subplots and traces that support `domain` can
            place themselves in this grid separately using the
            `gridcell` attribute.
        xaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an x axis
            id like "x", "x2", etc., or "" to not put an x axis in
            that column. Entries other than "" must be unique.
            Ignored if `subplots` is present. If missing but
            `yaxes` is present, will generate consecutive IDs.
        xgap
            Horizontal space between grid cells, expressed as a
            fraction of the total width available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.2 for
            independent grids.
        xside
            Sets where the x axis labels and titles go. "bottom"
            means the very bottom of the grid. "bottom plot" is the
            lowest plot that each x axis is used in. "top" and "top
            plot" are similar.
        yaxes
            Used with `yaxes` when the x and y axes are shared
            across columns and rows. Each entry should be an y axis
            id like "y", "y2", etc., or "" to not put a y axis in
            that row. Entries other than "" must be unique. Ignored
            if `subplots` is present. If missing but `xaxes` is
            present, will generate consecutive IDs.
        ygap
            Vertical space between grid cells, expressed as a
            fraction of the total height available to one cell.
            Defaults to 0.1 for coupled-axes grids and 0.3 for
            independent grids.
        yside
            Sets where the y axis labels and titles go. "left"
            means the very left edge of the grid. *left plot* is
            the leftmost plot that each y axis is used in. "right"
            and *right plot* are similar.

        Returns
        -------
        Grid
        """
        super(Grid, self).__init__("grid")

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
The first argument to the plotly.graph_objs.layout.Grid 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Grid"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import grid as v_grid

        # Initialize validators
        # ---------------------
        self._validators["columns"] = v_grid.ColumnsValidator()
        self._validators["domain"] = v_grid.DomainValidator()
        self._validators["pattern"] = v_grid.PatternValidator()
        self._validators["roworder"] = v_grid.RoworderValidator()
        self._validators["rows"] = v_grid.RowsValidator()
        self._validators["subplots"] = v_grid.SubplotsValidator()
        self._validators["xaxes"] = v_grid.XaxesValidator()
        self._validators["xgap"] = v_grid.XgapValidator()
        self._validators["xside"] = v_grid.XsideValidator()
        self._validators["yaxes"] = v_grid.YaxesValidator()
        self._validators["ygap"] = v_grid.YgapValidator()
        self._validators["yside"] = v_grid.YsideValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("columns", None)
        self["columns"] = columns if columns is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("pattern", None)
        self["pattern"] = pattern if pattern is not None else _v
        _v = arg.pop("roworder", None)
        self["roworder"] = roworder if roworder is not None else _v
        _v = arg.pop("rows", None)
        self["rows"] = rows if rows is not None else _v
        _v = arg.pop("subplots", None)
        self["subplots"] = subplots if subplots is not None else _v
        _v = arg.pop("xaxes", None)
        self["xaxes"] = xaxes if xaxes is not None else _v
        _v = arg.pop("xgap", None)
        self["xgap"] = xgap if xgap is not None else _v
        _v = arg.pop("xside", None)
        self["xside"] = xside if xside is not None else _v
        _v = arg.pop("yaxes", None)
        self["yaxes"] = yaxes if yaxes is not None else _v
        _v = arg.pop("ygap", None)
        self["ygap"] = ygap if ygap is not None else _v
        _v = arg.pop("yside", None)
        self["yside"] = yside if yside is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Geo(_BaseLayoutHierarchyType):

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Set the background color of the map
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # center
    # ------
    @property
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of plotly.graph_objs.layout.geo.Center
          - A dict of string/value properties that will be passed
            to the Center constructor
    
            Supported dict properties:
                
                lat
                    Sets the latitude of the map's center. For all
                    projection types, the map's latitude center
                    lies at the middle of the latitude range by
                    default.
                lon
                    Sets the longitude of the map's center. By
                    default, the map's longitude center lies at the
                    middle of the longitude range for scoped
                    projection and above `projection.rotation.lon`
                    otherwise.

        Returns
        -------
        plotly.graph_objs.layout.geo.Center
        """
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    # coastlinecolor
    # --------------
    @property
    def coastlinecolor(self):
        """
        Sets the coastline color.
    
        The 'coastlinecolor' property is a color and may be specified as:
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
        return self["coastlinecolor"]

    @coastlinecolor.setter
    def coastlinecolor(self, val):
        self["coastlinecolor"] = val

    # coastlinewidth
    # --------------
    @property
    def coastlinewidth(self):
        """
        Sets the coastline stroke width (in px).
    
        The 'coastlinewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["coastlinewidth"]

    @coastlinewidth.setter
    def coastlinewidth(self, val):
        self["coastlinewidth"] = val

    # countrycolor
    # ------------
    @property
    def countrycolor(self):
        """
        Sets line color of the country boundaries.
    
        The 'countrycolor' property is a color and may be specified as:
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
        return self["countrycolor"]

    @countrycolor.setter
    def countrycolor(self, val):
        self["countrycolor"] = val

    # countrywidth
    # ------------
    @property
    def countrywidth(self):
        """
        Sets line width (in px) of the country boundaries.
    
        The 'countrywidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["countrywidth"]

    @countrywidth.setter
    def countrywidth(self, val):
        self["countrywidth"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.geo.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this geo subplot .
                    Note that geo subplots are constrained by
                    domain. In general, when `projection.scale` is
                    set to 1. a map will fit either its x or y
                    domain, but not both.
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this geo subplot .
                    Note that geo subplots are constrained by
                    domain. In general, when `projection.scale` is
                    set to 1. a map will fit either its x or y
                    domain, but not both.
                x
                    Sets the horizontal domain of this geo subplot
                    (in plot fraction). Note that geo subplots are
                    constrained by domain. In general, when
                    `projection.scale` is set to 1. a map will fit
                    either its x or y domain, but not both.
                y
                    Sets the vertical domain of this geo subplot
                    (in plot fraction). Note that geo subplots are
                    constrained by domain. In general, when
                    `projection.scale` is set to 1. a map will fit
                    either its x or y domain, but not both.

        Returns
        -------
        plotly.graph_objs.layout.geo.Domain
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # framecolor
    # ----------
    @property
    def framecolor(self):
        """
        Sets the color the frame.
    
        The 'framecolor' property is a color and may be specified as:
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
        return self["framecolor"]

    @framecolor.setter
    def framecolor(self, val):
        self["framecolor"] = val

    # framewidth
    # ----------
    @property
    def framewidth(self):
        """
        Sets the stroke width (in px) of the frame.
    
        The 'framewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["framewidth"]

    @framewidth.setter
    def framewidth(self, val):
        self["framewidth"] = val

    # lakecolor
    # ---------
    @property
    def lakecolor(self):
        """
        Sets the color of the lakes.
    
        The 'lakecolor' property is a color and may be specified as:
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
        return self["lakecolor"]

    @lakecolor.setter
    def lakecolor(self, val):
        self["lakecolor"] = val

    # landcolor
    # ---------
    @property
    def landcolor(self):
        """
        Sets the land mass color.
    
        The 'landcolor' property is a color and may be specified as:
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
        return self["landcolor"]

    @landcolor.setter
    def landcolor(self, val):
        self["landcolor"] = val

    # lataxis
    # -------
    @property
    def lataxis(self):
        """
        The 'lataxis' property is an instance of Lataxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.geo.Lataxis
          - A dict of string/value properties that will be passed
            to the Lataxis constructor
    
            Supported dict properties:
                
                dtick
                    Sets the graticule's longitude/latitude tick
                    step.
                gridcolor
                    Sets the graticule's stroke color.
                gridwidth
                    Sets the graticule's stroke width (in px).
                range
                    Sets the range of this axis (in degrees), sets
                    the map's clipped coordinates.
                showgrid
                    Sets whether or not graticule are shown on the
                    map.
                tick0
                    Sets the graticule's starting tick
                    longitude/latitude.

        Returns
        -------
        plotly.graph_objs.layout.geo.Lataxis
        """
        return self["lataxis"]

    @lataxis.setter
    def lataxis(self, val):
        self["lataxis"] = val

    # lonaxis
    # -------
    @property
    def lonaxis(self):
        """
        The 'lonaxis' property is an instance of Lonaxis
        that may be specified as:
          - An instance of plotly.graph_objs.layout.geo.Lonaxis
          - A dict of string/value properties that will be passed
            to the Lonaxis constructor
    
            Supported dict properties:
                
                dtick
                    Sets the graticule's longitude/latitude tick
                    step.
                gridcolor
                    Sets the graticule's stroke color.
                gridwidth
                    Sets the graticule's stroke width (in px).
                range
                    Sets the range of this axis (in degrees), sets
                    the map's clipped coordinates.
                showgrid
                    Sets whether or not graticule are shown on the
                    map.
                tick0
                    Sets the graticule's starting tick
                    longitude/latitude.

        Returns
        -------
        plotly.graph_objs.layout.geo.Lonaxis
        """
        return self["lonaxis"]

    @lonaxis.setter
    def lonaxis(self, val):
        self["lonaxis"] = val

    # oceancolor
    # ----------
    @property
    def oceancolor(self):
        """
        Sets the ocean color
    
        The 'oceancolor' property is a color and may be specified as:
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
        return self["oceancolor"]

    @oceancolor.setter
    def oceancolor(self, val):
        self["oceancolor"] = val

    # projection
    # ----------
    @property
    def projection(self):
        """
        The 'projection' property is an instance of Projection
        that may be specified as:
          - An instance of plotly.graph_objs.layout.geo.Projection
          - A dict of string/value properties that will be passed
            to the Projection constructor
    
            Supported dict properties:
                
                parallels
                    For conic projection types only. Sets the
                    parallels (tangent, secant) where the cone
                    intersects the sphere.
                rotation
                    plotly.graph_objects.layout.geo.projection.Rota
                    tion instance or dict with compatible
                    properties
                scale
                    Zooms in or out on the map view. A scale of 1
                    corresponds to the largest zoom level that fits
                    the map's lon and lat ranges.
                type
                    Sets the projection type.

        Returns
        -------
        plotly.graph_objs.layout.geo.Projection
        """
        return self["projection"]

    @projection.setter
    def projection(self, val):
        self["projection"] = val

    # resolution
    # ----------
    @property
    def resolution(self):
        """
        Sets the resolution of the base layers. The values have units
        of km/mm e.g. 110 corresponds to a scale ratio of
        1:110,000,000.
    
        The 'resolution' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [110, 50]

        Returns
        -------
        Any
        """
        return self["resolution"]

    @resolution.setter
    def resolution(self, val):
        self["resolution"] = val

    # rivercolor
    # ----------
    @property
    def rivercolor(self):
        """
        Sets color of the rivers.
    
        The 'rivercolor' property is a color and may be specified as:
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
        return self["rivercolor"]

    @rivercolor.setter
    def rivercolor(self, val):
        self["rivercolor"] = val

    # riverwidth
    # ----------
    @property
    def riverwidth(self):
        """
        Sets the stroke width (in px) of the rivers.
    
        The 'riverwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["riverwidth"]

    @riverwidth.setter
    def riverwidth(self, val):
        self["riverwidth"] = val

    # scope
    # -----
    @property
    def scope(self):
        """
        Set the scope of the map.
    
        The 'scope' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['world', 'usa', 'europe', 'asia', 'africa', 'north
                america', 'south america']

        Returns
        -------
        Any
        """
        return self["scope"]

    @scope.setter
    def scope(self, val):
        self["scope"] = val

    # showcoastlines
    # --------------
    @property
    def showcoastlines(self):
        """
        Sets whether or not the coastlines are drawn.
    
        The 'showcoastlines' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showcoastlines"]

    @showcoastlines.setter
    def showcoastlines(self, val):
        self["showcoastlines"] = val

    # showcountries
    # -------------
    @property
    def showcountries(self):
        """
        Sets whether or not country boundaries are drawn.
    
        The 'showcountries' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showcountries"]

    @showcountries.setter
    def showcountries(self, val):
        self["showcountries"] = val

    # showframe
    # ---------
    @property
    def showframe(self):
        """
        Sets whether or not a frame is drawn around the map.
    
        The 'showframe' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showframe"]

    @showframe.setter
    def showframe(self, val):
        self["showframe"] = val

    # showlakes
    # ---------
    @property
    def showlakes(self):
        """
        Sets whether or not lakes are drawn.
    
        The 'showlakes' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showlakes"]

    @showlakes.setter
    def showlakes(self, val):
        self["showlakes"] = val

    # showland
    # --------
    @property
    def showland(self):
        """
        Sets whether or not land masses are filled in color.
    
        The 'showland' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showland"]

    @showland.setter
    def showland(self, val):
        self["showland"] = val

    # showocean
    # ---------
    @property
    def showocean(self):
        """
        Sets whether or not oceans are filled in color.
    
        The 'showocean' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showocean"]

    @showocean.setter
    def showocean(self, val):
        self["showocean"] = val

    # showrivers
    # ----------
    @property
    def showrivers(self):
        """
        Sets whether or not rivers are drawn.
    
        The 'showrivers' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showrivers"]

    @showrivers.setter
    def showrivers(self, val):
        self["showrivers"] = val

    # showsubunits
    # ------------
    @property
    def showsubunits(self):
        """
        Sets whether or not boundaries of subunits within countries
        (e.g. states, provinces) are drawn.
    
        The 'showsubunits' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showsubunits"]

    @showsubunits.setter
    def showsubunits(self, val):
        self["showsubunits"] = val

    # subunitcolor
    # ------------
    @property
    def subunitcolor(self):
        """
        Sets the color of the subunits boundaries.
    
        The 'subunitcolor' property is a color and may be specified as:
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
        return self["subunitcolor"]

    @subunitcolor.setter
    def subunitcolor(self, val):
        self["subunitcolor"] = val

    # subunitwidth
    # ------------
    @property
    def subunitwidth(self):
        """
        Sets the stroke width (in px) of the subunits boundaries.
    
        The 'subunitwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["subunitwidth"]

    @subunitwidth.setter
    def subunitwidth(self, val):
        self["subunitwidth"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in the view
        (projection and center). Defaults to `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Set the background color of the map
        center
            plotly.graph_objects.layout.geo.Center instance or dict
            with compatible properties
        coastlinecolor
            Sets the coastline color.
        coastlinewidth
            Sets the coastline stroke width (in px).
        countrycolor
            Sets line color of the country boundaries.
        countrywidth
            Sets line width (in px) of the country boundaries.
        domain
            plotly.graph_objects.layout.geo.Domain instance or dict
            with compatible properties
        framecolor
            Sets the color the frame.
        framewidth
            Sets the stroke width (in px) of the frame.
        lakecolor
            Sets the color of the lakes.
        landcolor
            Sets the land mass color.
        lataxis
            plotly.graph_objects.layout.geo.Lataxis instance or
            dict with compatible properties
        lonaxis
            plotly.graph_objects.layout.geo.Lonaxis instance or
            dict with compatible properties
        oceancolor
            Sets the ocean color
        projection
            plotly.graph_objects.layout.geo.Projection instance or
            dict with compatible properties
        resolution
            Sets the resolution of the base layers. The values have
            units of km/mm e.g. 110 corresponds to a scale ratio of
            1:110,000,000.
        rivercolor
            Sets color of the rivers.
        riverwidth
            Sets the stroke width (in px) of the rivers.
        scope
            Set the scope of the map.
        showcoastlines
            Sets whether or not the coastlines are drawn.
        showcountries
            Sets whether or not country boundaries are drawn.
        showframe
            Sets whether or not a frame is drawn around the map.
        showlakes
            Sets whether or not lakes are drawn.
        showland
            Sets whether or not land masses are filled in color.
        showocean
            Sets whether or not oceans are filled in color.
        showrivers
            Sets whether or not rivers are drawn.
        showsubunits
            Sets whether or not boundaries of subunits within
            countries (e.g. states, provinces) are drawn.
        subunitcolor
            Sets the color of the subunits boundaries.
        subunitwidth
            Sets the stroke width (in px) of the subunits
            boundaries.
        uirevision
            Controls persistence of user-driven changes in the view
            (projection and center). Defaults to
            `layout.uirevision`.
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        center=None,
        coastlinecolor=None,
        coastlinewidth=None,
        countrycolor=None,
        countrywidth=None,
        domain=None,
        framecolor=None,
        framewidth=None,
        lakecolor=None,
        landcolor=None,
        lataxis=None,
        lonaxis=None,
        oceancolor=None,
        projection=None,
        resolution=None,
        rivercolor=None,
        riverwidth=None,
        scope=None,
        showcoastlines=None,
        showcountries=None,
        showframe=None,
        showlakes=None,
        showland=None,
        showocean=None,
        showrivers=None,
        showsubunits=None,
        subunitcolor=None,
        subunitwidth=None,
        uirevision=None,
        **kwargs
    ):
        """
        Construct a new Geo object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Geo
        bgcolor
            Set the background color of the map
        center
            plotly.graph_objects.layout.geo.Center instance or dict
            with compatible properties
        coastlinecolor
            Sets the coastline color.
        coastlinewidth
            Sets the coastline stroke width (in px).
        countrycolor
            Sets line color of the country boundaries.
        countrywidth
            Sets line width (in px) of the country boundaries.
        domain
            plotly.graph_objects.layout.geo.Domain instance or dict
            with compatible properties
        framecolor
            Sets the color the frame.
        framewidth
            Sets the stroke width (in px) of the frame.
        lakecolor
            Sets the color of the lakes.
        landcolor
            Sets the land mass color.
        lataxis
            plotly.graph_objects.layout.geo.Lataxis instance or
            dict with compatible properties
        lonaxis
            plotly.graph_objects.layout.geo.Lonaxis instance or
            dict with compatible properties
        oceancolor
            Sets the ocean color
        projection
            plotly.graph_objects.layout.geo.Projection instance or
            dict with compatible properties
        resolution
            Sets the resolution of the base layers. The values have
            units of km/mm e.g. 110 corresponds to a scale ratio of
            1:110,000,000.
        rivercolor
            Sets color of the rivers.
        riverwidth
            Sets the stroke width (in px) of the rivers.
        scope
            Set the scope of the map.
        showcoastlines
            Sets whether or not the coastlines are drawn.
        showcountries
            Sets whether or not country boundaries are drawn.
        showframe
            Sets whether or not a frame is drawn around the map.
        showlakes
            Sets whether or not lakes are drawn.
        showland
            Sets whether or not land masses are filled in color.
        showocean
            Sets whether or not oceans are filled in color.
        showrivers
            Sets whether or not rivers are drawn.
        showsubunits
            Sets whether or not boundaries of subunits within
            countries (e.g. states, provinces) are drawn.
        subunitcolor
            Sets the color of the subunits boundaries.
        subunitwidth
            Sets the stroke width (in px) of the subunits
            boundaries.
        uirevision
            Controls persistence of user-driven changes in the view
            (projection and center). Defaults to
            `layout.uirevision`.

        Returns
        -------
        Geo
        """
        super(Geo, self).__init__("geo")

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
The first argument to the plotly.graph_objs.layout.Geo 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Geo"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import geo as v_geo

        # Initialize validators
        # ---------------------
        self._validators["bgcolor"] = v_geo.BgcolorValidator()
        self._validators["center"] = v_geo.CenterValidator()
        self._validators["coastlinecolor"] = v_geo.CoastlinecolorValidator()
        self._validators["coastlinewidth"] = v_geo.CoastlinewidthValidator()
        self._validators["countrycolor"] = v_geo.CountrycolorValidator()
        self._validators["countrywidth"] = v_geo.CountrywidthValidator()
        self._validators["domain"] = v_geo.DomainValidator()
        self._validators["framecolor"] = v_geo.FramecolorValidator()
        self._validators["framewidth"] = v_geo.FramewidthValidator()
        self._validators["lakecolor"] = v_geo.LakecolorValidator()
        self._validators["landcolor"] = v_geo.LandcolorValidator()
        self._validators["lataxis"] = v_geo.LataxisValidator()
        self._validators["lonaxis"] = v_geo.LonaxisValidator()
        self._validators["oceancolor"] = v_geo.OceancolorValidator()
        self._validators["projection"] = v_geo.ProjectionValidator()
        self._validators["resolution"] = v_geo.ResolutionValidator()
        self._validators["rivercolor"] = v_geo.RivercolorValidator()
        self._validators["riverwidth"] = v_geo.RiverwidthValidator()
        self._validators["scope"] = v_geo.ScopeValidator()
        self._validators["showcoastlines"] = v_geo.ShowcoastlinesValidator()
        self._validators["showcountries"] = v_geo.ShowcountriesValidator()
        self._validators["showframe"] = v_geo.ShowframeValidator()
        self._validators["showlakes"] = v_geo.ShowlakesValidator()
        self._validators["showland"] = v_geo.ShowlandValidator()
        self._validators["showocean"] = v_geo.ShowoceanValidator()
        self._validators["showrivers"] = v_geo.ShowriversValidator()
        self._validators["showsubunits"] = v_geo.ShowsubunitsValidator()
        self._validators["subunitcolor"] = v_geo.SubunitcolorValidator()
        self._validators["subunitwidth"] = v_geo.SubunitwidthValidator()
        self._validators["uirevision"] = v_geo.UirevisionValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("center", None)
        self["center"] = center if center is not None else _v
        _v = arg.pop("coastlinecolor", None)
        self["coastlinecolor"] = coastlinecolor if coastlinecolor is not None else _v
        _v = arg.pop("coastlinewidth", None)
        self["coastlinewidth"] = coastlinewidth if coastlinewidth is not None else _v
        _v = arg.pop("countrycolor", None)
        self["countrycolor"] = countrycolor if countrycolor is not None else _v
        _v = arg.pop("countrywidth", None)
        self["countrywidth"] = countrywidth if countrywidth is not None else _v
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("framecolor", None)
        self["framecolor"] = framecolor if framecolor is not None else _v
        _v = arg.pop("framewidth", None)
        self["framewidth"] = framewidth if framewidth is not None else _v
        _v = arg.pop("lakecolor", None)
        self["lakecolor"] = lakecolor if lakecolor is not None else _v
        _v = arg.pop("landcolor", None)
        self["landcolor"] = landcolor if landcolor is not None else _v
        _v = arg.pop("lataxis", None)
        self["lataxis"] = lataxis if lataxis is not None else _v
        _v = arg.pop("lonaxis", None)
        self["lonaxis"] = lonaxis if lonaxis is not None else _v
        _v = arg.pop("oceancolor", None)
        self["oceancolor"] = oceancolor if oceancolor is not None else _v
        _v = arg.pop("projection", None)
        self["projection"] = projection if projection is not None else _v
        _v = arg.pop("resolution", None)
        self["resolution"] = resolution if resolution is not None else _v
        _v = arg.pop("rivercolor", None)
        self["rivercolor"] = rivercolor if rivercolor is not None else _v
        _v = arg.pop("riverwidth", None)
        self["riverwidth"] = riverwidth if riverwidth is not None else _v
        _v = arg.pop("scope", None)
        self["scope"] = scope if scope is not None else _v
        _v = arg.pop("showcoastlines", None)
        self["showcoastlines"] = showcoastlines if showcoastlines is not None else _v
        _v = arg.pop("showcountries", None)
        self["showcountries"] = showcountries if showcountries is not None else _v
        _v = arg.pop("showframe", None)
        self["showframe"] = showframe if showframe is not None else _v
        _v = arg.pop("showlakes", None)
        self["showlakes"] = showlakes if showlakes is not None else _v
        _v = arg.pop("showland", None)
        self["showland"] = showland if showland is not None else _v
        _v = arg.pop("showocean", None)
        self["showocean"] = showocean if showocean is not None else _v
        _v = arg.pop("showrivers", None)
        self["showrivers"] = showrivers if showrivers is not None else _v
        _v = arg.pop("showsubunits", None)
        self["showsubunits"] = showsubunits if showsubunits is not None else _v
        _v = arg.pop("subunitcolor", None)
        self["subunitcolor"] = subunitcolor if subunitcolor is not None else _v
        _v = arg.pop("subunitwidth", None)
        self["subunitwidth"] = subunitwidth if subunitwidth is not None else _v
        _v = arg.pop("uirevision", None)
        self["uirevision"] = uirevision if uirevision is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Font(_BaseLayoutHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
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

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The plotly service (at https://plot.ly or on-
        premise) generates images on a server, where only a select
        number of fonts are installed and supported. These include
        "Arial", "Balto", "Courier New", "Droid Sans",, "Droid Serif",
        "Droid Sans Mono", "Gravitas One", "Old Standard TT", "Open
        Sans", "Overpass", "PT Sans Narrow", "Raleway", "Times New
        Roman".
    
        The 'family' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include "Arial", "Balto", "Courier New", "Droid Sans",,
            "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
            Standard TT", "Open Sans", "Overpass", "PT Sans
            Narrow", "Raleway", "Times New Roman".
        size

        """

    def __init__(self, arg=None, color=None, family=None, size=None, **kwargs):
        """
        Construct a new Font object
        
        Sets the global font. Note that fonts used in traces and other
        layout components inherit from the global font.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Font
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include "Arial", "Balto", "Courier New", "Droid Sans",,
            "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
            Standard TT", "Open Sans", "Overpass", "PT Sans
            Narrow", "Raleway", "Times New Roman".
        size


        Returns
        -------
        Font
        """
        super(Font, self).__init__("font")

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
The first argument to the plotly.graph_objs.layout.Font 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Font"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import font as v_font

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_font.ColorValidator()
        self._validators["family"] = v_font.FamilyValidator()
        self._validators["size"] = v_font.SizeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("family", None)
        self["family"] = family if family is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Colorscale(_BaseLayoutHierarchyType):

    # diverging
    # ---------
    @property
    def diverging(self):
        """
        Sets the default diverging colorscale. Note that
        `autocolorscale` must be true for this attribute to work.
    
        The 'diverging' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
                 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
                 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
                 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
                 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
                 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
                 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd']

        Returns
        -------
        str
        """
        return self["diverging"]

    @diverging.setter
    def diverging(self, val):
        self["diverging"] = val

    # sequential
    # ----------
    @property
    def sequential(self):
        """
        Sets the default sequential colorscale for positive values.
        Note that `autocolorscale` must be true for this attribute to
        work.
    
        The 'sequential' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
                 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
                 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
                 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
                 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
                 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
                 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd']

        Returns
        -------
        str
        """
        return self["sequential"]

    @sequential.setter
    def sequential(self, val):
        self["sequential"] = val

    # sequentialminus
    # ---------------
    @property
    def sequentialminus(self):
        """
        Sets the default sequential colorscale for negative values.
        Note that `autocolorscale` must be true for this attribute to
        work.
    
        The 'sequentialminus' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
                 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
                 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
                 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
                 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
                 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
                 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd']

        Returns
        -------
        str
        """
        return self["sequentialminus"]

    @sequentialminus.setter
    def sequentialminus(self, val):
        self["sequentialminus"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        diverging
            Sets the default diverging colorscale. Note that
            `autocolorscale` must be true for this attribute to
            work.
        sequential
            Sets the default sequential colorscale for positive
            values. Note that `autocolorscale` must be true for
            this attribute to work.
        sequentialminus
            Sets the default sequential colorscale for negative
            values. Note that `autocolorscale` must be true for
            this attribute to work.
        """

    def __init__(
        self, arg=None, diverging=None, sequential=None, sequentialminus=None, **kwargs
    ):
        """
        Construct a new Colorscale object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Colorscale
        diverging
            Sets the default diverging colorscale. Note that
            `autocolorscale` must be true for this attribute to
            work.
        sequential
            Sets the default sequential colorscale for positive
            values. Note that `autocolorscale` must be true for
            this attribute to work.
        sequentialminus
            Sets the default sequential colorscale for negative
            values. Note that `autocolorscale` must be true for
            this attribute to work.

        Returns
        -------
        Colorscale
        """
        super(Colorscale, self).__init__("colorscale")

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
The first argument to the plotly.graph_objs.layout.Colorscale 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Colorscale"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import colorscale as v_colorscale

        # Initialize validators
        # ---------------------
        self._validators["diverging"] = v_colorscale.DivergingValidator()
        self._validators["sequential"] = v_colorscale.SequentialValidator()
        self._validators["sequentialminus"] = v_colorscale.SequentialminusValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("diverging", None)
        self["diverging"] = diverging if diverging is not None else _v
        _v = arg.pop("sequential", None)
        self["sequential"] = sequential if sequential is not None else _v
        _v = arg.pop("sequentialminus", None)
        self["sequentialminus"] = sequentialminus if sequentialminus is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Coloraxis(_BaseLayoutHierarchyType):

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `colorscale`. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default  palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here corresponding trace color
        array(s)) or the bounds set in `cmin` and `cmax`  Defaults to
        `false` when `cmin` and `cmax` are set by the user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cauto"]

    @cauto.setter
    def cauto(self, val):
        self["cauto"] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Value should have the
        same units as corresponding trace color array(s) and if set,
        `cmin` must be set as well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmax"]

    @cmax.setter
    def cmax(self, val):
        self["cmax"] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `cmin` and/or
        `cmax` to be equidistant to this point. Value should have the
        same units as corresponding trace color array(s). Has no effect
        when `cauto` is `false`.
    
        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmid"]

    @cmid.setter
    def cmid(self, val):
        self["cmid"] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Value should have the
        same units as corresponding trace color array(s) and if set,
        `cmax` must be set as well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmin"]

    @cmin.setter
    def cmin(self, val):
        self["cmin"] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of plotly.graph_objs.layout.coloraxis.ColorBar
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
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
                    A tuple of plotly.graph_objects.layout.coloraxi
                    s.colorbar.Tickformatstop instances or dicts
                    with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.lay
                    out.coloraxis.colorbar.tickformatstopdefaults),
                    sets the default property values to use for
                    elements of
                    layout.coloraxis.colorbar.tickformatstops
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
                    plotly.graph_objects.layout.coloraxis.colorbar.
                    Title instance or dict with compatible
                    properties
                titlefont
                    Deprecated: Please use
                    layout.coloraxis.colorbar.title.font instead.
                    Sets this color bar's title font. Note that the
                    title's font used to be set by the now
                    deprecated `titlefont` attribute.
                titleside
                    Deprecated: Please use
                    layout.coloraxis.colorbar.title.side instead.
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

        Returns
        -------
        plotly.graph_objs.layout.coloraxis.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use`cmin` and `cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Bl
        ues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth,Electric,Vi
        ridis,Cividis.
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
                 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
                 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
                 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
                 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
                 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
                 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd']

        Returns
        -------
        str
        """
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. If true, `cmin` will
        correspond to the last color in the array and `cmax` will
        correspond to the first color.
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here corresponding
            trace color array(s)) or the bounds set in `cmin` and
            `cmax`  Defaults to `false` when `cmin` and `cmax` are
            set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as corresponding trace color
            array(s) and if set, `cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as corresponding trace
            color array(s). Has no effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as corresponding trace color
            array(s) and if set, `cmax` must be set as well.
        colorbar
            plotly.graph_objects.layout.coloraxis.ColorBar instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        """

    def __init__(
        self,
        arg=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        colorbar=None,
        colorscale=None,
        reversescale=None,
        showscale=None,
        **kwargs
    ):
        """
        Construct a new Coloraxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Coloraxis
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here corresponding
            trace color array(s)) or the bounds set in `cmin` and
            `cmax`  Defaults to `false` when `cmin` and `cmax` are
            set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as corresponding trace color
            array(s) and if set, `cmin` must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as corresponding trace
            color array(s). Has no effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as corresponding trace color
            array(s) and if set, `cmax` must be set as well.
        colorbar
            plotly.graph_objects.layout.coloraxis.ColorBar instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.

        Returns
        -------
        Coloraxis
        """
        super(Coloraxis, self).__init__("coloraxis")

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
The first argument to the plotly.graph_objs.layout.Coloraxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Coloraxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import coloraxis as v_coloraxis

        # Initialize validators
        # ---------------------
        self._validators["autocolorscale"] = v_coloraxis.AutocolorscaleValidator()
        self._validators["cauto"] = v_coloraxis.CautoValidator()
        self._validators["cmax"] = v_coloraxis.CmaxValidator()
        self._validators["cmid"] = v_coloraxis.CmidValidator()
        self._validators["cmin"] = v_coloraxis.CminValidator()
        self._validators["colorbar"] = v_coloraxis.ColorBarValidator()
        self._validators["colorscale"] = v_coloraxis.ColorscaleValidator()
        self._validators["reversescale"] = v_coloraxis.ReversescaleValidator()
        self._validators["showscale"] = v_coloraxis.ShowscaleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autocolorscale", None)
        self["autocolorscale"] = autocolorscale if autocolorscale is not None else _v
        _v = arg.pop("cauto", None)
        self["cauto"] = cauto if cauto is not None else _v
        _v = arg.pop("cmax", None)
        self["cmax"] = cmax if cmax is not None else _v
        _v = arg.pop("cmid", None)
        self["cmid"] = cmid if cmid is not None else _v
        _v = arg.pop("cmin", None)
        self["cmin"] = cmin if cmin is not None else _v
        _v = arg.pop("colorbar", None)
        self["colorbar"] = colorbar if colorbar is not None else _v
        _v = arg.pop("colorscale", None)
        self["colorscale"] = colorscale if colorscale is not None else _v
        _v = arg.pop("reversescale", None)
        self["reversescale"] = reversescale if reversescale is not None else _v
        _v = arg.pop("showscale", None)
        self["showscale"] = showscale if showscale is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Annotation(_BaseLayoutHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the `text` within the box. Has
        an effect only if `text` spans more two or more lines (i.e.
        `text` contains one or more <br> HTML tags) or if an explicit
        width is set to override the text width.
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["align"]

    @align.setter
    def align(self, val):
        self["align"] = val

    # arrowcolor
    # ----------
    @property
    def arrowcolor(self):
        """
        Sets the color of the annotation arrow.
    
        The 'arrowcolor' property is a color and may be specified as:
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
        return self["arrowcolor"]

    @arrowcolor.setter
    def arrowcolor(self, val):
        self["arrowcolor"] = val

    # arrowhead
    # ---------
    @property
    def arrowhead(self):
        """
        Sets the end annotation arrow head style.
    
        The 'arrowhead' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 8]

        Returns
        -------
        int
        """
        return self["arrowhead"]

    @arrowhead.setter
    def arrowhead(self, val):
        self["arrowhead"] = val

    # arrowside
    # ---------
    @property
    def arrowside(self):
        """
        Sets the annotation arrow head position.
    
        The 'arrowside' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['end', 'start'] joined with '+' characters
            (e.g. 'end+start')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self["arrowside"]

    @arrowside.setter
    def arrowside(self, val):
        self["arrowside"] = val

    # arrowsize
    # ---------
    @property
    def arrowsize(self):
        """
        Sets the size of the end annotation arrow head, relative to
        `arrowwidth`. A value of 1 (default) gives a head about 3x as
        wide as the line.
    
        The 'arrowsize' property is a number and may be specified as:
          - An int or float in the interval [0.3, inf]

        Returns
        -------
        int|float
        """
        return self["arrowsize"]

    @arrowsize.setter
    def arrowsize(self, val):
        self["arrowsize"] = val

    # arrowwidth
    # ----------
    @property
    def arrowwidth(self):
        """
        Sets the width (in px) of annotation arrow line.
    
        The 'arrowwidth' property is a number and may be specified as:
          - An int or float in the interval [0.1, inf]

        Returns
        -------
        int|float
        """
        return self["arrowwidth"]

    @arrowwidth.setter
    def arrowwidth(self, val):
        self["arrowwidth"] = val

    # ax
    # --
    @property
    def ax(self):
        """
        Sets the x component of the arrow tail about the arrow head. If
        `axref` is `pixel`, a positive (negative)  component
        corresponds to an arrow pointing from right to left (left to
        right). If `axref` is an axis, this is an absolute value on
        that axis, like `x`, NOT a relative value.
    
        The 'ax' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["ax"]

    @ax.setter
    def ax(self, val):
        self["ax"] = val

    # axref
    # -----
    @property
    def axref(self):
        """
        Indicates in what terms the tail of the annotation (ax,ay)  is
        specified. If `pixel`, `ax` is a relative offset in pixels
        from `x`. If set to an x axis id (e.g. "x" or "x2"), `ax` is
        specified in the same terms as that axis. This is useful  for
        trendline annotations which should continue to indicate  the
        correct trend when zoomed.
    
        The 'axref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['pixel']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["axref"]

    @axref.setter
    def axref(self, val):
        self["axref"] = val

    # ay
    # --
    @property
    def ay(self):
        """
        Sets the y component of the arrow tail about the arrow head. If
        `ayref` is `pixel`, a positive (negative)  component
        corresponds to an arrow pointing from bottom to top (top to
        bottom). If `ayref` is an axis, this is an absolute value on
        that axis, like `y`, NOT a relative value.
    
        The 'ay' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["ay"]

    @ay.setter
    def ay(self, val):
        self["ay"] = val

    # ayref
    # -----
    @property
    def ayref(self):
        """
        Indicates in what terms the tail of the annotation (ax,ay)  is
        specified. If `pixel`, `ay` is a relative offset in pixels
        from `y`. If set to a y axis id (e.g. "y" or "y2"), `ay` is
        specified in the same terms as that axis. This is useful  for
        trendline annotations which should continue to indicate  the
        correct trend when zoomed.
    
        The 'ayref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['pixel']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["ayref"]

    @ayref.setter
    def ayref(self, val):
        self["ayref"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the annotation.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the annotation `text`.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # borderpad
    # ---------
    @property
    def borderpad(self):
        """
        Sets the padding (in px) between the `text` and the enclosing
        border.
    
        The 'borderpad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["borderpad"]

    @borderpad.setter
    def borderpad(self, val):
        self["borderpad"] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the annotation
        `text`.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    # captureevents
    # -------------
    @property
    def captureevents(self):
        """
        Determines whether the annotation text box captures mouse move
        and click events, or allows those events to pass through to
        data points in the plot that may be behind the annotation. By
        default `captureevents` is False unless `hovertext` is
        provided. If you use the event `plotly_clickannotation` without
        `hovertext` you must explicitly enable `captureevents`.
    
        The 'captureevents' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["captureevents"]

    @captureevents.setter
    def captureevents(self, val):
        self["captureevents"] = val

    # clicktoshow
    # -----------
    @property
    def clicktoshow(self):
        """
        Makes this annotation respond to clicks on the plot. If you
        click a data point that exactly matches the `x` and `y` values
        of this annotation, and it is hidden (visible: false), it will
        appear. In "onoff" mode, you must click the same point again to
        make it disappear, so if you click multiple points, you can
        show multiple annotations. In "onout" mode, a click anywhere
        else in the plot (on another data point or not) will hide this
        annotation. If you need to show/hide this annotation in
        response to different `x` or `y` values, you can set `xclick`
        and/or `yclick`. This is useful for example to label the side
        of a bar. To label markers though, `standoff` is preferred over
        `xclick` and `yclick`.
    
        The 'clicktoshow' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [False, 'onoff', 'onout']

        Returns
        -------
        Any
        """
        return self["clicktoshow"]

    @clicktoshow.setter
    def clicktoshow(self, val):
        self["clicktoshow"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the annotation text font.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.annotation.Font
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
        plotly.graph_objs.layout.annotation.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # height
    # ------
    @property
    def height(self):
        """
        Sets an explicit height for the text box. null (default) lets
        the text set the box height. Taller text will be clipped.
    
        The 'height' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self["height"]

    @height.setter
    def height(self, val):
        self["height"] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.layout.annotation.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
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

        Returns
        -------
        plotly.graph_objs.layout.annotation.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Sets text to appear when hovering over this annotation. If
        omitted or blank, no hover label will appear.
    
        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the annotation (text + arrow).
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # showarrow
    # ---------
    @property
    def showarrow(self):
        """
        Determines whether or not the annotation is drawn with an
        arrow. If True, `text` is placed near the arrow's tail. If
        False, `text` lines up with the `x` and `y` provided.
    
        The 'showarrow' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showarrow"]

    @showarrow.setter
    def showarrow(self, val):
        self["showarrow"] = val

    # standoff
    # --------
    @property
    def standoff(self):
        """
        Sets a distance, in pixels, to move the end arrowhead away from
        the position it is pointing at, for example to point at the
        edge of a marker independent of zoom. Note that this shortens
        the arrow from the `ax` / `ay` vector, in contrast to `xshift`
        / `yshift` which moves everything by this amount.
    
        The 'standoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["standoff"]

    @standoff.setter
    def standoff(self, val):
        self["standoff"] = val

    # startarrowhead
    # --------------
    @property
    def startarrowhead(self):
        """
        Sets the start annotation arrow head style.
    
        The 'startarrowhead' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 8]

        Returns
        -------
        int
        """
        return self["startarrowhead"]

    @startarrowhead.setter
    def startarrowhead(self, val):
        self["startarrowhead"] = val

    # startarrowsize
    # --------------
    @property
    def startarrowsize(self):
        """
        Sets the size of the start annotation arrow head, relative to
        `arrowwidth`. A value of 1 (default) gives a head about 3x as
        wide as the line.
    
        The 'startarrowsize' property is a number and may be specified as:
          - An int or float in the interval [0.3, inf]

        Returns
        -------
        int|float
        """
        return self["startarrowsize"]

    @startarrowsize.setter
    def startarrowsize(self, val):
        self["startarrowsize"] = val

    # startstandoff
    # -------------
    @property
    def startstandoff(self):
        """
        Sets a distance, in pixels, to move the start arrowhead away
        from the position it is pointing at, for example to point at
        the edge of a marker independent of zoom. Note that this
        shortens the arrow from the `ax` / `ay` vector, in contrast to
        `xshift` / `yshift` which moves everything by this amount.
    
        The 'startstandoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["startstandoff"]

    @startstandoff.setter
    def startstandoff(self, val):
        self["startstandoff"] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text associated with this annotation. Plotly uses a
        subset of HTML tags to do things like newline (<br>), bold
        (<b></b>), italics (<i></i>), hyperlinks (<a href='...'></a>).
        Tags <em>, <sup>, <sub> <span> are also supported.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # textangle
    # ---------
    @property
    def textangle(self):
        """
        Sets the angle at which the `text` is drawn with respect to the
        horizontal.
    
        The 'textangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["textangle"]

    @textangle.setter
    def textangle(self, val):
        self["textangle"] = val

    # valign
    # ------
    @property
    def valign(self):
        """
        Sets the vertical alignment of the `text` within the box. Has
        an effect only if an explicit height is set to override the
        text height.
    
        The 'valign' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["valign"]

    @valign.setter
    def valign(self, val):
        self["valign"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this annotation is visible.
    
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

    # width
    # -----
    @property
    def width(self):
        """
        Sets an explicit width for the text box. null (default) lets
        the text set the box width. Wider text will be clipped. There
        is no automatic wrapping; use <br> to start a new line.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the annotation's x position. If the axis `type` is "log",
        then you must take the log of your desired range. If the axis
        `type` is "date", it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is "category", it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'x' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the text box's horizontal position anchor This anchor
        binds the `x` position to the "left", "center" or "right" of
        the annotation. For example, if `x` is set to 1, `xref` to
        "paper" and `xanchor` to "right" then the right-most portion of
        the annotation lines up with the right-most edge of the
        plotting area. If "auto", the anchor is equivalent to "center"
        for data-referenced annotations or if there is an arrow,
        whereas for paper-referenced with no arrow, the anchor picked
        corresponds to the closest side.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # xclick
    # ------
    @property
    def xclick(self):
        """
        Toggle this annotation when clicking a data point whose `x`
        value is `xclick` rather than the annotation's `x` value.
    
        The 'xclick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["xclick"]

    @xclick.setter
    def xclick(self, val):
        self["xclick"] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the annotation's x coordinate axis. If set to an x axis id
        (e.g. "x" or "x2"), the `x` position refers to an x coordinate
        If set to "paper", the `x` position refers to the distance from
        the left side of the plotting area in normalized coordinates
        where 0 (1) corresponds to the left (right) side.
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["xref"]

    @xref.setter
    def xref(self, val):
        self["xref"] = val

    # xshift
    # ------
    @property
    def xshift(self):
        """
        Shifts the position of the whole annotation and arrow to the
        right (positive) or left (negative) by this many pixels.
    
        The 'xshift' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["xshift"]

    @xshift.setter
    def xshift(self, val):
        self["xshift"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the annotation's y position. If the axis `type` is "log",
        then you must take the log of your desired range. If the axis
        `type` is "date", it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is "category", it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'y' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the text box's vertical position anchor This anchor binds
        the `y` position to the "top", "middle" or "bottom" of the
        annotation. For example, if `y` is set to 1, `yref` to "paper"
        and `yanchor` to "top" then the top-most portion of the
        annotation lines up with the top-most edge of the plotting
        area. If "auto", the anchor is equivalent to "middle" for data-
        referenced annotations or if there is an arrow, whereas for
        paper-referenced with no arrow, the anchor picked corresponds
        to the closest side.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # yclick
    # ------
    @property
    def yclick(self):
        """
        Toggle this annotation when clicking a data point whose `y`
        value is `yclick` rather than the annotation's `y` value.
    
        The 'yclick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["yclick"]

    @yclick.setter
    def yclick(self, val):
        self["yclick"] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the annotation's y coordinate axis. If set to an y axis id
        (e.g. "y" or "y2"), the `y` position refers to an y coordinate
        If set to "paper", the `y` position refers to the distance from
        the bottom of the plotting area in normalized coordinates where
        0 (1) corresponds to the bottom (top).
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self["yref"]

    @yref.setter
    def yref(self, val):
        self["yref"] = val

    # yshift
    # ------
    @property
    def yshift(self):
        """
        Shifts the position of the whole annotation and arrow up
        (positive) or down (negative) by this many pixels.
    
        The 'yshift' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["yshift"]

    @yshift.setter
    def yshift(self, val):
        self["yshift"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        arrowcolor
            Sets the color of the annotation arrow.
        arrowhead
            Sets the end annotation arrow head style.
        arrowside
            Sets the annotation arrow head position.
        arrowsize
            Sets the size of the end annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        arrowwidth
            Sets the width (in px) of annotation arrow line.
        ax
            Sets the x component of the arrow tail about the arrow
            head. If `axref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from right
            to left (left to right). If `axref` is an axis, this is
            an absolute value on that axis, like `x`, NOT a
            relative value.
        axref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ax` is a relative
            offset in pixels  from `x`. If set to an x axis id
            (e.g. "x" or "x2"), `ax` is  specified in the same
            terms as that axis. This is useful  for trendline
            annotations which should continue to indicate  the
            correct trend when zoomed.
        ay
            Sets the y component of the arrow tail about the arrow
            head. If `ayref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from bottom
            to top (top to bottom). If `ayref` is an axis, this is
            an absolute value on that axis, like `y`, NOT a
            relative value.
        ayref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ay` is a relative
            offset in pixels  from `y`. If set to a y axis id (e.g.
            "y" or "y2"), `ay` is  specified in the same terms as
            that axis. This is useful  for trendline annotations
            which should continue to indicate  the correct trend
            when zoomed.
        bgcolor
            Sets the background color of the annotation.
        bordercolor
            Sets the color of the border enclosing the annotation
            `text`.
        borderpad
            Sets the padding (in px) between the `text` and the
            enclosing border.
        borderwidth
            Sets the width (in px) of the border enclosing the
            annotation `text`.
        captureevents
            Determines whether the annotation text box captures
            mouse move and click events, or allows those events to
            pass through to data points in the plot that may be
            behind the annotation. By default `captureevents` is
            False unless `hovertext` is provided. If you use the
            event `plotly_clickannotation` without `hovertext` you
            must explicitly enable `captureevents`.
        clicktoshow
            Makes this annotation respond to clicks on the plot. If
            you click a data point that exactly matches the `x` and
            `y` values of this annotation, and it is hidden
            (visible: false), it will appear. In "onoff" mode, you
            must click the same point again to make it disappear,
            so if you click multiple points, you can show multiple
            annotations. In "onout" mode, a click anywhere else in
            the plot (on another data point or not) will hide this
            annotation. If you need to show/hide this annotation in
            response to different `x` or `y` values, you can set
            `xclick` and/or `yclick`. This is useful for example to
            label the side of a bar. To label markers though,
            `standoff` is preferred over `xclick` and `yclick`.
        font
            Sets the annotation text font.
        height
            Sets an explicit height for the text box. null
            (default) lets the text set the box height. Taller text
            will be clipped.
        hoverlabel
            plotly.graph_objects.layout.annotation.Hoverlabel
            instance or dict with compatible properties
        hovertext
            Sets text to appear when hovering over this annotation.
            If omitted or blank, no hover label will appear.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the annotation (text + arrow).
        showarrow
            Determines whether or not the annotation is drawn with
            an arrow. If True, `text` is placed near the arrow's
            tail. If False, `text` lines up with the `x` and `y`
            provided.
        standoff
            Sets a distance, in pixels, to move the end arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        startarrowhead
            Sets the start annotation arrow head style.
        startarrowsize
            Sets the size of the start annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        startstandoff
            Sets a distance, in pixels, to move the start arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        text
            Sets the text associated with this annotation. Plotly
            uses a subset of HTML tags to do things like newline
            (<br>), bold (<b></b>), italics (<i></i>), hyperlinks
            (<a href='...'></a>). Tags <em>, <sup>, <sub> <span>
            are also supported.
        textangle
            Sets the angle at which the `text` is drawn with
            respect to the horizontal.
        valign
            Sets the vertical alignment of the `text` within the
            box. Has an effect only if an explicit height is set to
            override the text height.
        visible
            Determines whether or not this annotation is visible.
        width
            Sets an explicit width for the text box. null (default)
            lets the text set the box width. Wider text will be
            clipped. There is no automatic wrapping; use <br> to
            start a new line.
        x
            Sets the annotation's x position. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        xanchor
            Sets the text box's horizontal position anchor This
            anchor binds the `x` position to the "left", "center"
            or "right" of the annotation. For example, if `x` is
            set to 1, `xref` to "paper" and `xanchor` to "right"
            then the right-most portion of the annotation lines up
            with the right-most edge of the plotting area. If
            "auto", the anchor is equivalent to "center" for data-
            referenced annotations or if there is an arrow, whereas
            for paper-referenced with no arrow, the anchor picked
            corresponds to the closest side.
        xclick
            Toggle this annotation when clicking a data point whose
            `x` value is `xclick` rather than the annotation's `x`
            value.
        xref
            Sets the annotation's x coordinate axis. If set to an x
            axis id (e.g. "x" or "x2"), the `x` position refers to
            an x coordinate If set to "paper", the `x` position
            refers to the distance from the left side of the
            plotting area in normalized coordinates where 0 (1)
            corresponds to the left (right) side.
        xshift
            Shifts the position of the whole annotation and arrow
            to the right (positive) or left (negative) by this many
            pixels.
        y
            Sets the annotation's y position. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        yanchor
            Sets the text box's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the annotation. For example, if `y` is set
            to 1, `yref` to "paper" and `yanchor` to "top" then the
            top-most portion of the annotation lines up with the
            top-most edge of the plotting area. If "auto", the
            anchor is equivalent to "middle" for data-referenced
            annotations or if there is an arrow, whereas for paper-
            referenced with no arrow, the anchor picked corresponds
            to the closest side.
        yclick
            Toggle this annotation when clicking a data point whose
            `y` value is `yclick` rather than the annotation's `y`
            value.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        yshift
            Shifts the position of the whole annotation and arrow
            up (positive) or down (negative) by this many pixels.
        """

    def __init__(
        self,
        arg=None,
        align=None,
        arrowcolor=None,
        arrowhead=None,
        arrowside=None,
        arrowsize=None,
        arrowwidth=None,
        ax=None,
        axref=None,
        ay=None,
        ayref=None,
        bgcolor=None,
        bordercolor=None,
        borderpad=None,
        borderwidth=None,
        captureevents=None,
        clicktoshow=None,
        font=None,
        height=None,
        hoverlabel=None,
        hovertext=None,
        name=None,
        opacity=None,
        showarrow=None,
        standoff=None,
        startarrowhead=None,
        startarrowsize=None,
        startstandoff=None,
        templateitemname=None,
        text=None,
        textangle=None,
        valign=None,
        visible=None,
        width=None,
        x=None,
        xanchor=None,
        xclick=None,
        xref=None,
        xshift=None,
        y=None,
        yanchor=None,
        yclick=None,
        yref=None,
        yshift=None,
        **kwargs
    ):
        """
        Construct a new Annotation object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Annotation
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        arrowcolor
            Sets the color of the annotation arrow.
        arrowhead
            Sets the end annotation arrow head style.
        arrowside
            Sets the annotation arrow head position.
        arrowsize
            Sets the size of the end annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        arrowwidth
            Sets the width (in px) of annotation arrow line.
        ax
            Sets the x component of the arrow tail about the arrow
            head. If `axref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from right
            to left (left to right). If `axref` is an axis, this is
            an absolute value on that axis, like `x`, NOT a
            relative value.
        axref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ax` is a relative
            offset in pixels  from `x`. If set to an x axis id
            (e.g. "x" or "x2"), `ax` is  specified in the same
            terms as that axis. This is useful  for trendline
            annotations which should continue to indicate  the
            correct trend when zoomed.
        ay
            Sets the y component of the arrow tail about the arrow
            head. If `ayref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from bottom
            to top (top to bottom). If `ayref` is an axis, this is
            an absolute value on that axis, like `y`, NOT a
            relative value.
        ayref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ay` is a relative
            offset in pixels  from `y`. If set to a y axis id (e.g.
            "y" or "y2"), `ay` is  specified in the same terms as
            that axis. This is useful  for trendline annotations
            which should continue to indicate  the correct trend
            when zoomed.
        bgcolor
            Sets the background color of the annotation.
        bordercolor
            Sets the color of the border enclosing the annotation
            `text`.
        borderpad
            Sets the padding (in px) between the `text` and the
            enclosing border.
        borderwidth
            Sets the width (in px) of the border enclosing the
            annotation `text`.
        captureevents
            Determines whether the annotation text box captures
            mouse move and click events, or allows those events to
            pass through to data points in the plot that may be
            behind the annotation. By default `captureevents` is
            False unless `hovertext` is provided. If you use the
            event `plotly_clickannotation` without `hovertext` you
            must explicitly enable `captureevents`.
        clicktoshow
            Makes this annotation respond to clicks on the plot. If
            you click a data point that exactly matches the `x` and
            `y` values of this annotation, and it is hidden
            (visible: false), it will appear. In "onoff" mode, you
            must click the same point again to make it disappear,
            so if you click multiple points, you can show multiple
            annotations. In "onout" mode, a click anywhere else in
            the plot (on another data point or not) will hide this
            annotation. If you need to show/hide this annotation in
            response to different `x` or `y` values, you can set
            `xclick` and/or `yclick`. This is useful for example to
            label the side of a bar. To label markers though,
            `standoff` is preferred over `xclick` and `yclick`.
        font
            Sets the annotation text font.
        height
            Sets an explicit height for the text box. null
            (default) lets the text set the box height. Taller text
            will be clipped.
        hoverlabel
            plotly.graph_objects.layout.annotation.Hoverlabel
            instance or dict with compatible properties
        hovertext
            Sets text to appear when hovering over this annotation.
            If omitted or blank, no hover label will appear.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the annotation (text + arrow).
        showarrow
            Determines whether or not the annotation is drawn with
            an arrow. If True, `text` is placed near the arrow's
            tail. If False, `text` lines up with the `x` and `y`
            provided.
        standoff
            Sets a distance, in pixels, to move the end arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        startarrowhead
            Sets the start annotation arrow head style.
        startarrowsize
            Sets the size of the start annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        startstandoff
            Sets a distance, in pixels, to move the start arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        text
            Sets the text associated with this annotation. Plotly
            uses a subset of HTML tags to do things like newline
            (<br>), bold (<b></b>), italics (<i></i>), hyperlinks
            (<a href='...'></a>). Tags <em>, <sup>, <sub> <span>
            are also supported.
        textangle
            Sets the angle at which the `text` is drawn with
            respect to the horizontal.
        valign
            Sets the vertical alignment of the `text` within the
            box. Has an effect only if an explicit height is set to
            override the text height.
        visible
            Determines whether or not this annotation is visible.
        width
            Sets an explicit width for the text box. null (default)
            lets the text set the box width. Wider text will be
            clipped. There is no automatic wrapping; use <br> to
            start a new line.
        x
            Sets the annotation's x position. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        xanchor
            Sets the text box's horizontal position anchor This
            anchor binds the `x` position to the "left", "center"
            or "right" of the annotation. For example, if `x` is
            set to 1, `xref` to "paper" and `xanchor` to "right"
            then the right-most portion of the annotation lines up
            with the right-most edge of the plotting area. If
            "auto", the anchor is equivalent to "center" for data-
            referenced annotations or if there is an arrow, whereas
            for paper-referenced with no arrow, the anchor picked
            corresponds to the closest side.
        xclick
            Toggle this annotation when clicking a data point whose
            `x` value is `xclick` rather than the annotation's `x`
            value.
        xref
            Sets the annotation's x coordinate axis. If set to an x
            axis id (e.g. "x" or "x2"), the `x` position refers to
            an x coordinate If set to "paper", the `x` position
            refers to the distance from the left side of the
            plotting area in normalized coordinates where 0 (1)
            corresponds to the left (right) side.
        xshift
            Shifts the position of the whole annotation and arrow
            to the right (positive) or left (negative) by this many
            pixels.
        y
            Sets the annotation's y position. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        yanchor
            Sets the text box's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the annotation. For example, if `y` is set
            to 1, `yref` to "paper" and `yanchor` to "top" then the
            top-most portion of the annotation lines up with the
            top-most edge of the plotting area. If "auto", the
            anchor is equivalent to "middle" for data-referenced
            annotations or if there is an arrow, whereas for paper-
            referenced with no arrow, the anchor picked corresponds
            to the closest side.
        yclick
            Toggle this annotation when clicking a data point whose
            `y` value is `yclick` rather than the annotation's `y`
            value.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. "y" or "y2"), the `y` position refers to
            an y coordinate If set to "paper", the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        yshift
            Shifts the position of the whole annotation and arrow
            up (positive) or down (negative) by this many pixels.

        Returns
        -------
        Annotation
        """
        super(Annotation, self).__init__("annotations")

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
The first argument to the plotly.graph_objs.layout.Annotation 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Annotation"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import annotation as v_annotation

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_annotation.AlignValidator()
        self._validators["arrowcolor"] = v_annotation.ArrowcolorValidator()
        self._validators["arrowhead"] = v_annotation.ArrowheadValidator()
        self._validators["arrowside"] = v_annotation.ArrowsideValidator()
        self._validators["arrowsize"] = v_annotation.ArrowsizeValidator()
        self._validators["arrowwidth"] = v_annotation.ArrowwidthValidator()
        self._validators["ax"] = v_annotation.AxValidator()
        self._validators["axref"] = v_annotation.AxrefValidator()
        self._validators["ay"] = v_annotation.AyValidator()
        self._validators["ayref"] = v_annotation.AyrefValidator()
        self._validators["bgcolor"] = v_annotation.BgcolorValidator()
        self._validators["bordercolor"] = v_annotation.BordercolorValidator()
        self._validators["borderpad"] = v_annotation.BorderpadValidator()
        self._validators["borderwidth"] = v_annotation.BorderwidthValidator()
        self._validators["captureevents"] = v_annotation.CaptureeventsValidator()
        self._validators["clicktoshow"] = v_annotation.ClicktoshowValidator()
        self._validators["font"] = v_annotation.FontValidator()
        self._validators["height"] = v_annotation.HeightValidator()
        self._validators["hoverlabel"] = v_annotation.HoverlabelValidator()
        self._validators["hovertext"] = v_annotation.HovertextValidator()
        self._validators["name"] = v_annotation.NameValidator()
        self._validators["opacity"] = v_annotation.OpacityValidator()
        self._validators["showarrow"] = v_annotation.ShowarrowValidator()
        self._validators["standoff"] = v_annotation.StandoffValidator()
        self._validators["startarrowhead"] = v_annotation.StartarrowheadValidator()
        self._validators["startarrowsize"] = v_annotation.StartarrowsizeValidator()
        self._validators["startstandoff"] = v_annotation.StartstandoffValidator()
        self._validators["templateitemname"] = v_annotation.TemplateitemnameValidator()
        self._validators["text"] = v_annotation.TextValidator()
        self._validators["textangle"] = v_annotation.TextangleValidator()
        self._validators["valign"] = v_annotation.ValignValidator()
        self._validators["visible"] = v_annotation.VisibleValidator()
        self._validators["width"] = v_annotation.WidthValidator()
        self._validators["x"] = v_annotation.XValidator()
        self._validators["xanchor"] = v_annotation.XanchorValidator()
        self._validators["xclick"] = v_annotation.XclickValidator()
        self._validators["xref"] = v_annotation.XrefValidator()
        self._validators["xshift"] = v_annotation.XshiftValidator()
        self._validators["y"] = v_annotation.YValidator()
        self._validators["yanchor"] = v_annotation.YanchorValidator()
        self._validators["yclick"] = v_annotation.YclickValidator()
        self._validators["yref"] = v_annotation.YrefValidator()
        self._validators["yshift"] = v_annotation.YshiftValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("arrowcolor", None)
        self["arrowcolor"] = arrowcolor if arrowcolor is not None else _v
        _v = arg.pop("arrowhead", None)
        self["arrowhead"] = arrowhead if arrowhead is not None else _v
        _v = arg.pop("arrowside", None)
        self["arrowside"] = arrowside if arrowside is not None else _v
        _v = arg.pop("arrowsize", None)
        self["arrowsize"] = arrowsize if arrowsize is not None else _v
        _v = arg.pop("arrowwidth", None)
        self["arrowwidth"] = arrowwidth if arrowwidth is not None else _v
        _v = arg.pop("ax", None)
        self["ax"] = ax if ax is not None else _v
        _v = arg.pop("axref", None)
        self["axref"] = axref if axref is not None else _v
        _v = arg.pop("ay", None)
        self["ay"] = ay if ay is not None else _v
        _v = arg.pop("ayref", None)
        self["ayref"] = ayref if ayref is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderpad", None)
        self["borderpad"] = borderpad if borderpad is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("captureevents", None)
        self["captureevents"] = captureevents if captureevents is not None else _v
        _v = arg.pop("clicktoshow", None)
        self["clicktoshow"] = clicktoshow if clicktoshow is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("height", None)
        self["height"] = height if height is not None else _v
        _v = arg.pop("hoverlabel", None)
        self["hoverlabel"] = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop("hovertext", None)
        self["hovertext"] = hovertext if hovertext is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("opacity", None)
        self["opacity"] = opacity if opacity is not None else _v
        _v = arg.pop("showarrow", None)
        self["showarrow"] = showarrow if showarrow is not None else _v
        _v = arg.pop("standoff", None)
        self["standoff"] = standoff if standoff is not None else _v
        _v = arg.pop("startarrowhead", None)
        self["startarrowhead"] = startarrowhead if startarrowhead is not None else _v
        _v = arg.pop("startarrowsize", None)
        self["startarrowsize"] = startarrowsize if startarrowsize is not None else _v
        _v = arg.pop("startstandoff", None)
        self["startstandoff"] = startstandoff if startstandoff is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("text", None)
        self["text"] = text if text is not None else _v
        _v = arg.pop("textangle", None)
        self["textangle"] = textangle if textangle is not None else _v
        _v = arg.pop("valign", None)
        self["valign"] = valign if valign is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("width", None)
        self["width"] = width if width is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("xclick", None)
        self["xclick"] = xclick if xclick is not None else _v
        _v = arg.pop("xref", None)
        self["xref"] = xref if xref is not None else _v
        _v = arg.pop("xshift", None)
        self["xshift"] = xshift if xshift is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v
        _v = arg.pop("yclick", None)
        self["yclick"] = yclick if yclick is not None else _v
        _v = arg.pop("yref", None)
        self["yref"] = yref if yref is not None else _v
        _v = arg.pop("yshift", None)
        self["yshift"] = yshift if yshift is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class AngularAxis(_BaseLayoutHierarchyType):

    # domain
    # ------
    @property
    def domain(self):
        """
        Polar chart subplots are not supported yet. This key has
        currently no effect.
    
        The 'domain' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'domain[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'domain[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # endpadding
    # ----------
    @property
    def endpadding(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots.
    
        The 'endpadding' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["endpadding"]

    @endpadding.setter
    def endpadding(self, val):
        self["endpadding"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Defines the start and end point of this angular axis.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not the line bounding this
        angular axis will be shown on the figure.
    
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
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not the angular axis ticks will
        feature tick labels.
    
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

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the color of the tick lines on this angular
        axis.
    
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

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the length of the tick lines on this angular
        axis.
    
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

    # tickorientation
    # ---------------
    @property
    def tickorientation(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the orientation (from the paper perspective) of
        the angular axis tick labels.
    
        The 'tickorientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['horizontal', 'vertical']

        Returns
        -------
        Any
        """
        return self["tickorientation"]

    @tickorientation.setter
    def tickorientation(self, val):
        self["tickorientation"] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the length of the tick lines on this angular
        axis.
    
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

    # visible
    # -------
    @property
    def visible(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not this axis will be visible.
    
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
        return "layout"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots.
        range
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Defines the start and end point of
            this angular axis.
        showline
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the line
            bounding this angular axis will be shown on the figure.
        showticklabels
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the angular
            axis ticks will feature tick labels.
        tickcolor
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the color of the tick lines on
            this angular axis.
        ticklen
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        tickorientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (from the paper
            perspective) of the angular axis tick labels.
        ticksuffix
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        visible
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not this axis
            will be visible.
        """

    def __init__(
        self,
        arg=None,
        domain=None,
        endpadding=None,
        range=None,
        showline=None,
        showticklabels=None,
        tickcolor=None,
        ticklen=None,
        tickorientation=None,
        ticksuffix=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new AngularAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.AngularAxis
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots.
        range
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Defines the start and end point of
            this angular axis.
        showline
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the line
            bounding this angular axis will be shown on the figure.
        showticklabels
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the angular
            axis ticks will feature tick labels.
        tickcolor
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the color of the tick lines on
            this angular axis.
        ticklen
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        tickorientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (from the paper
            perspective) of the angular axis tick labels.
        ticksuffix
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        visible
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not this axis
            will be visible.

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
The first argument to the plotly.graph_objs.layout.AngularAxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.AngularAxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout import angularaxis as v_angularaxis

        # Initialize validators
        # ---------------------
        self._validators["domain"] = v_angularaxis.DomainValidator()
        self._validators["endpadding"] = v_angularaxis.EndpaddingValidator()
        self._validators["range"] = v_angularaxis.RangeValidator()
        self._validators["showline"] = v_angularaxis.ShowlineValidator()
        self._validators["showticklabels"] = v_angularaxis.ShowticklabelsValidator()
        self._validators["tickcolor"] = v_angularaxis.TickcolorValidator()
        self._validators["ticklen"] = v_angularaxis.TicklenValidator()
        self._validators["tickorientation"] = v_angularaxis.TickorientationValidator()
        self._validators["ticksuffix"] = v_angularaxis.TicksuffixValidator()
        self._validators["visible"] = v_angularaxis.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("domain", None)
        self["domain"] = domain if domain is not None else _v
        _v = arg.pop("endpadding", None)
        self["endpadding"] = endpadding if endpadding is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("showline", None)
        self["showline"] = showline if showline is not None else _v
        _v = arg.pop("showticklabels", None)
        self["showticklabels"] = showticklabels if showticklabels is not None else _v
        _v = arg.pop("tickcolor", None)
        self["tickcolor"] = tickcolor if tickcolor is not None else _v
        _v = arg.pop("ticklen", None)
        self["ticklen"] = ticklen if ticklen is not None else _v
        _v = arg.pop("tickorientation", None)
        self["tickorientation"] = tickorientation if tickorientation is not None else _v
        _v = arg.pop("ticksuffix", None)
        self["ticksuffix"] = ticksuffix if ticksuffix is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.graph_objs.layout import yaxis
from plotly.graph_objs.layout import xaxis
from plotly.graph_objs.layout import updatemenu
from plotly.graph_objs.layout import title
from plotly.graph_objs.layout import ternary
from plotly.graph_objs.layout import template
from plotly.graph_objs.layout import slider
from plotly.graph_objs.layout import shape
from plotly.graph_objs.layout import scene
from plotly.graph_objs.layout import polar
from plotly.graph_objs.layout import mapbox
from plotly.graph_objs.layout import legend
from plotly.graph_objs.layout import hoverlabel
from plotly.graph_objs.layout import grid
from plotly.graph_objs.layout import geo
from plotly.graph_objs.layout import coloraxis
from plotly.graph_objs.layout import annotation
