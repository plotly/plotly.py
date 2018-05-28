from plotly.basedatatypes import BaseTraceHierarchyType


class ColorBar(BaseTraceHierarchyType):

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the color of padded area.
    
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
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the axis line color.
    
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
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bordercolor']

    @bordercolor.setter
    def bordercolor(self, val):
        self['bordercolor'] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) or the border enclosing this color bar.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['borderwidth']

    @borderwidth.setter
    def borderwidth(self, val):
        self['borderwidth'] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to
        *log* and *date* axes. If the axis `type` is *log*, then ticks
        are set every 10^(n*dtick) where n is the tick number. For
        example, to set a tick mark at 1, 10, 100, 1000, ... set dtick
        to 1. To set tick marks at 1, 100, 10000, ... set dtick to 2.
        To set tick marks at 1, 5, 25, 125, 625, 3125, ... set dtick to
        log_10(5), or 0.69897000433. *log* has several special values;
        *L<f>*, where `f` is a positive number, gives ticks linearly
        spaced in value (but not position). For example `tick0` = 0.1,
        `dtick` = *L0.5* will put ticks at 0.1, 0.6, 1.1, 1.6 etc. To
        show powers of 10 plus small digits between, use *D1* (all
        digits) or *D2* (only 2 and 5). `tick0` is ignored for *D1* and
        *D2*. If the axis `type` is *date*, then you must convert the
        time to milliseconds. For example, to set the interval between
        ticks to one day, set `dtick` to 86400000.0. *date* also has
        special values *M<n>* gives ticks spaced by a number of months.
        `n` must be a positive integer. To set ticks on the 15th of
        every third month, set `tick0` to *2000-01-15* and `dtick` to
        *M3*. To set ticks every 4 years, set `dtick` to *M48*
    
        The 'dtick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['dtick']

    @dtick.setter
    def dtick(self, val):
        self['dtick'] = val

    # exponentformat
    # --------------
    @property
    def exponentformat(self):
        """
        Determines a formatting rule for the tick exponents. For
        example, consider the number 1,000,000,000. If *none*, it
        appears as 1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
        *power*, 1x10^9 (with 9 in a super script). If *SI*, 1G. If
        *B*, 1B.
    
        The 'exponentformat' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'e', 'E', 'power', 'SI', 'B']

        Returns
        -------
        Any
        """
        return self['exponentformat']

    @exponentformat.setter
    def exponentformat(self, val):
        self['exponentformat'] = val

    # len
    # ---
    @property
    def len(self):
        """
        Sets the length of the color bar This measure excludes the
        padding of both ends. That is, the color bar length is this
        length minus the padding on both ends.
    
        The 'len' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['len']

    @len.setter
    def len(self, val):
        self['len'] = val

    # lenmode
    # -------
    @property
    def lenmode(self):
        """
        Determines whether this color bar's length (i.e. the measure in
        the color variation direction) is set in units of plot
        *fraction* or in *pixels. Use `len` to set the value.
    
        The 'lenmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        return self['lenmode']

    @lenmode.setter
    def lenmode(self, val):
        self['lenmode'] = val

    # nticks
    # ------
    @property
    def nticks(self):
        """
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to *auto*.
    
        The 'nticks' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['nticks']

    @nticks.setter
    def nticks(self, val):
        self['nticks'] = val

    # outlinecolor
    # ------------
    @property
    def outlinecolor(self):
        """
        Sets the axis line color.
    
        The 'outlinecolor' property is a color and may be specified as:
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
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['outlinecolor']

    @outlinecolor.setter
    def outlinecolor(self, val):
        self['outlinecolor'] = val

    # outlinewidth
    # ------------
    @property
    def outlinewidth(self):
        """
        Sets the width (in px) of the axis line.
    
        The 'outlinewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['outlinewidth']

    @outlinewidth.setter
    def outlinewidth(self, val):
        self['outlinewidth'] = val

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
        return self['separatethousands']

    @separatethousands.setter
    def separatethousands(self, val):
        self['separatethousands'] = val

    # showexponent
    # ------------
    @property
    def showexponent(self):
        """
        If *all*, all exponents are shown besides their significands.
        If *first*, only the exponent of the first tick is shown. If
        *last*, only the exponent of the last tick is shown. If *none*,
        no exponents appear.
    
        The 'showexponent' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showexponent']

    @showexponent.setter
    def showexponent(self, val):
        self['showexponent'] = val

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
        return self['showticklabels']

    @showticklabels.setter
    def showticklabels(self, val):
        self['showticklabels'] = val

    # showtickprefix
    # --------------
    @property
    def showtickprefix(self):
        """
        If *all*, all tick labels are displayed with a prefix. If
        *first*, only the first tick is displayed with a prefix. If
        *last*, only the last tick is displayed with a suffix. If
        *none*, tick prefixes are hidden.
    
        The 'showtickprefix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showtickprefix']

    @showtickprefix.setter
    def showtickprefix(self, val):
        self['showtickprefix'] = val

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
        return self['showticksuffix']

    @showticksuffix.setter
    def showticksuffix(self, val):
        self['showticksuffix'] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness of the color bar This measure excludes the
        size of the padding, ticks and labels.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['thickness']

    @thickness.setter
    def thickness(self, val):
        self['thickness'] = val

    # thicknessmode
    # -------------
    @property
    def thicknessmode(self):
        """
        Determines whether this color bar's thickness (i.e. the measure
        in the constant color direction) is set in units of plot
        *fraction* or in *pixels*. Use `thickness` to set the value.
    
        The 'thicknessmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        return self['thicknessmode']

    @thicknessmode.setter
    def thicknessmode(self, val):
        self['thicknessmode'] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the placement of the first tick on this axis. Use with
        `dtick`. If the axis `type` is *log*, then you must take the
        log of your starting tick (e.g. to set the starting tick to
        100, set the `tick0` to 2) except when `dtick`=*L<f>* (see
        `dtick` for more info). If the axis `type` is *date*, it should
        be a date string, like date data. If the axis `type` is
        *category*, it should be a number, using the scale where each
        category is assigned a serial number from zero in the order it
        appears.
    
        The 'tick0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['tick0']

    @tick0.setter
    def tick0(self, val):
        self['tick0'] = val

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
        return self['tickangle']

    @tickangle.setter
    def tickangle(self, val):
        self['tickangle'] = val

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
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['tickcolor']

    @tickcolor.setter
    def tickcolor(self, val):
        self['tickcolor'] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the color bar's tick label font
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.colorbar.Tickfont
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
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.mesh3d.colorbar.Tickfont
        """
        return self['tickfont']

    @tickfont.setter
    def tickfont(self, val):
        self['tickfont'] = val

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-format/blob/master/READM
        E.md#locale_format And for dates see:
        https://github.com/d3/d3-time-
        format/blob/master/README.md#locale_format We add one item to
        d3's date formatter: *%{n}f* for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        *%H~%M~%S.%2f* would display *09~15~23.46*
    
        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickformat']

    @tickformat.setter
    def tickformat(self, val):
        self['tickformat'] = val

    # tickformatstops
    # ---------------
    @property
    def tickformatstops(self):
        """
        The 'tickformatstops' property is a tuple of instances of
        Tickformatstop that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.mesh3d.colorbar.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor
    
            Supported dict properties:
                
                dtickrange
                    range [*min*, *max*], where *min*, *max* -
                    dtick values which describe some zoom level, it
                    is possible to omit *min* or *max* value by
                    passing *null*
                value
                    string - dtickformat for described zoom level,
                    the same as *tickformat*

        Returns
        -------
        tuple[plotly.graph_objs.mesh3d.colorbar.Tickformatstop]
        """
        return self['tickformatstops']

    @tickformatstops.setter
    def tickformatstops(self, val):
        self['tickformatstops'] = val

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
        return self['ticklen']

    @ticklen.setter
    def ticklen(self, val):
        self['ticklen'] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        Sets the tick mode for this axis. If *auto*, the number of
        ticks is set via `nticks`. If *linear*, the placement of the
        ticks is determined by a starting position `tick0` and a tick
        step `dtick` (*linear* is the default value if `tick0` and
        `dtick` are provided). If *array*, the placement of the ticks
        is set via `tickvals` and the tick text is `ticktext`. (*array*
        is the default value if `tickvals` is provided).
    
        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'linear', 'array']

        Returns
        -------
        Any
        """
        return self['tickmode']

    @tickmode.setter
    def tickmode(self, val):
        self['tickmode'] = val

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
        return self['tickprefix']

    @tickprefix.setter
    def tickprefix(self, val):
        self['tickprefix'] = val

    # ticks
    # -----
    @property
    def ticks(self):
        """
        Determines whether ticks are drawn or not. If **, this axis'
        ticks are not drawn. If *outside* (*inside*), this axis' are
        drawn outside (inside) the axis lines.
    
        The 'ticks' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['outside', 'inside', '']

        Returns
        -------
        Any
        """
        return self['ticks']

    @ticks.setter
    def ticks(self, val):
        self['ticks'] = val

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
        return self['ticksuffix']

    @ticksuffix.setter
    def ticksuffix(self, val):
        self['ticksuffix'] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to *array*. Used with
        `tickvals`.
    
        The 'ticktext' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ticktext']

    @ticktext.setter
    def ticktext(self, val):
        self['ticktext'] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on plot.ly for  ticktext .
    
        The 'ticktextsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ticktextsrc']

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self['ticktextsrc'] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to *array*. Used with `ticktext`.
    
        The 'tickvals' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['tickvals']

    @tickvals.setter
    def tickvals(self, val):
        self['tickvals'] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on plot.ly for  tickvals .
    
        The 'tickvalssrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickvalssrc']

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self['tickvalssrc'] = val

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
        return self['tickwidth']

    @tickwidth.setter
    def tickwidth(self, val):
        self['tickwidth'] = val

    # title
    # -----
    @property
    def title(self):
        """
        Sets the title of the color bar.
    
        The 'title' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['title']

    @title.setter
    def title(self, val):
        self['title'] = val

    # titlefont
    # ---------
    @property
    def titlefont(self):
        """
        Sets this color bar's title font.
    
        The 'titlefont' property is an instance of Titlefont
        that may be specified as:
          - An instance of plotly.graph_objs.mesh3d.colorbar.Titlefont
          - A dict of string/value properties that will be passed
            to the Titlefont constructor
    
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
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.mesh3d.colorbar.Titlefont
        """
        return self['titlefont']

    @titlefont.setter
    def titlefont(self, val):
        self['titlefont'] = val

    # titleside
    # ---------
    @property
    def titleside(self):
        """
        Determines the location of the colorbar title with respect to
        the color bar.
    
        The 'titleside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['right', 'top', 'bottom']

        Returns
        -------
        Any
        """
        return self['titleside']

    @titleside.setter
    def titleside(self, val):
        self['titleside'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position of the color bar (in plot fraction).
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets this color bar's horizontal position anchor. This anchor
        binds the `x` position to the *left*, *center* or *right* of
        the color bar.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # xpad
    # ----
    @property
    def xpad(self):
        """
        Sets the amount of padding (in px) along the x direction.
    
        The 'xpad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['xpad']

    @xpad.setter
    def xpad(self, val):
        self['xpad'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position of the color bar (in plot fraction).
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets this color bar's vertical position anchor This anchor
        binds the `y` position to the *top*, *middle* or *bottom* of
        the color bar.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # ypad
    # ----
    @property
    def ypad(self):
        """
        Sets the amount of padding (in px) along the y direction.
    
        The 'ypad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['ypad']

    @ypad.setter
    def ypad(self, val):
        self['ypad'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'mesh3d'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Sets the color of padded area.
        bordercolor
            Sets the axis line color.
        borderwidth
            Sets the width (in px) or the border enclosing this
            color bar.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to *log* and *date* axes. If the axis `type`
            is *log*, then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. *log* has several special
            values; *L<f>*, where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = *L0.5* will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use *D1* (all digits) or *D2*
            (only 2 and 5). `tick0` is ignored for *D1* and *D2*.
            If the axis `type` is *date*, then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            *date* also has special values *M<n>* gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to *2000-01-15* and `dtick` to *M3*. To set
            ticks every 4 years, set `dtick` to *M48*
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            *none*, it appears as 1,000,000,000. If *e*, 1e+9. If
            *E*, 1E+9. If *power*, 1x10^9 (with 9 in a super
            script). If *SI*, 1G. If *B*, 1B.
        len
            Sets the length of the color bar This measure excludes
            the padding of both ends. That is, the color bar length
            is this length minus the padding on both ends.
        lenmode
            Determines whether this color bar's length (i.e. the
            measure in the color variation direction) is set in
            units of plot *fraction* or in *pixels. Use `len` to
            set the value.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            *auto*.
        outlinecolor
            Sets the axis line color.
        outlinewidth
            Sets the width (in px) of the axis line.
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If *all*, all exponents are shown besides their
            significands. If *first*, only the exponent of the
            first tick is shown. If *last*, only the exponent of
            the last tick is shown. If *none*, no exponents appear.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If *all*, all tick labels are displayed with a prefix.
            If *first*, only the first tick is displayed with a
            prefix. If *last*, only the last tick is displayed with
            a suffix. If *none*, tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        thickness
            Sets the thickness of the color bar This measure
            excludes the size of the padding, ticks and labels.
        thicknessmode
            Determines whether this color bar's thickness (i.e. the
            measure in the constant color direction) is set in
            units of plot *fraction* or in *pixels*. Use
            `thickness` to set the value.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is *log*, then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is *date*, it should be a date string, like
            date data. If the axis `type` is *category*, it should
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
            Sets the color bar's tick label font
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        tickformatstops
            plotly.graph_objs.mesh3d.colorbar.Tickformatstop
            instance or dict with compatible properties
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If *auto*, the number
            of ticks is set via `nticks`. If *linear*, the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` (*linear* is
            the default value if `tick0` and `dtick` are provided).
            If *array*, the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. (*array* is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If **, this
            axis' ticks are not drawn. If *outside* (*inside*),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            *array*. Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to *array*.
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        title
            Sets the title of the color bar.
        titlefont
            Sets this color bar's title font.
        titleside
            Determines the location of the colorbar title with
            respect to the color bar.
        x
            Sets the x position of the color bar (in plot
            fraction).
        xanchor
            Sets this color bar's horizontal position anchor. This
            anchor binds the `x` position to the *left*, *center*
            or *right* of the color bar.
        xpad
            Sets the amount of padding (in px) along the x
            direction.
        y
            Sets the y position of the color bar (in plot
            fraction).
        yanchor
            Sets this color bar's vertical position anchor This
            anchor binds the `y` position to the *top*, *middle* or
            *bottom* of the color bar.
        ypad
            Sets the amount of padding (in px) along the y
            direction.
        """

    def __init__(
        self,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        dtick=None,
        exponentformat=None,
        len=None,
        lenmode=None,
        nticks=None,
        outlinecolor=None,
        outlinewidth=None,
        separatethousands=None,
        showexponent=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        thickness=None,
        thicknessmode=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
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
        titleside=None,
        x=None,
        xanchor=None,
        xpad=None,
        y=None,
        yanchor=None,
        ypad=None,
        **kwargs
    ):
        """
        Construct a new ColorBar object
        
        Parameters
        ----------
        bgcolor
            Sets the color of padded area.
        bordercolor
            Sets the axis line color.
        borderwidth
            Sets the width (in px) or the border enclosing this
            color bar.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to *log* and *date* axes. If the axis `type`
            is *log*, then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. *log* has several special
            values; *L<f>*, where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = *L0.5* will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use *D1* (all digits) or *D2*
            (only 2 and 5). `tick0` is ignored for *D1* and *D2*.
            If the axis `type` is *date*, then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            *date* also has special values *M<n>* gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to *2000-01-15* and `dtick` to *M3*. To set
            ticks every 4 years, set `dtick` to *M48*
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            *none*, it appears as 1,000,000,000. If *e*, 1e+9. If
            *E*, 1E+9. If *power*, 1x10^9 (with 9 in a super
            script). If *SI*, 1G. If *B*, 1B.
        len
            Sets the length of the color bar This measure excludes
            the padding of both ends. That is, the color bar length
            is this length minus the padding on both ends.
        lenmode
            Determines whether this color bar's length (i.e. the
            measure in the color variation direction) is set in
            units of plot *fraction* or in *pixels. Use `len` to
            set the value.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            *auto*.
        outlinecolor
            Sets the axis line color.
        outlinewidth
            Sets the width (in px) of the axis line.
        separatethousands
            If "true", even 4-digit integers are separated
        showexponent
            If *all*, all exponents are shown besides their
            significands. If *first*, only the exponent of the
            first tick is shown. If *last*, only the exponent of
            the last tick is shown. If *none*, no exponents appear.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If *all*, all tick labels are displayed with a prefix.
            If *first*, only the first tick is displayed with a
            prefix. If *last*, only the last tick is displayed with
            a suffix. If *none*, tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        thickness
            Sets the thickness of the color bar This measure
            excludes the size of the padding, ticks and labels.
        thicknessmode
            Determines whether this color bar's thickness (i.e. the
            measure in the constant color direction) is set in
            units of plot *fraction* or in *pixels*. Use
            `thickness` to set the value.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is *log*, then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is *date*, it should be a date string, like
            date data. If the axis `type` is *category*, it should
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
            Sets the color bar's tick label font
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        tickformatstops
            plotly.graph_objs.mesh3d.colorbar.Tickformatstop
            instance or dict with compatible properties
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If *auto*, the number
            of ticks is set via `nticks`. If *linear*, the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` (*linear* is
            the default value if `tick0` and `dtick` are provided).
            If *array*, the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. (*array* is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If **, this
            axis' ticks are not drawn. If *outside* (*inside*),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            *array*. Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to *array*.
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        title
            Sets the title of the color bar.
        titlefont
            Sets this color bar's title font.
        titleside
            Determines the location of the colorbar title with
            respect to the color bar.
        x
            Sets the x position of the color bar (in plot
            fraction).
        xanchor
            Sets this color bar's horizontal position anchor. This
            anchor binds the `x` position to the *left*, *center*
            or *right* of the color bar.
        xpad
            Sets the amount of padding (in px) along the x
            direction.
        y
            Sets the y position of the color bar (in plot
            fraction).
        yanchor
            Sets this color bar's vertical position anchor This
            anchor binds the `y` position to the *top*, *middle* or
            *bottom* of the color bar.
        ypad
            Sets the amount of padding (in px) along the y
            direction.

        Returns
        -------
        ColorBar
        """
        super(ColorBar, self).__init__('colorbar')

        # Import validators
        # -----------------
        from plotly.validators.mesh3d import (colorbar as v_colorbar)

        # Initialize validators
        # ---------------------
        self._validators['bgcolor'] = v_colorbar.BgcolorValidator()
        self._validators['bordercolor'] = v_colorbar.BordercolorValidator()
        self._validators['borderwidth'] = v_colorbar.BorderwidthValidator()
        self._validators['dtick'] = v_colorbar.DtickValidator()
        self._validators['exponentformat'
                        ] = v_colorbar.ExponentformatValidator()
        self._validators['len'] = v_colorbar.LenValidator()
        self._validators['lenmode'] = v_colorbar.LenmodeValidator()
        self._validators['nticks'] = v_colorbar.NticksValidator()
        self._validators['outlinecolor'] = v_colorbar.OutlinecolorValidator()
        self._validators['outlinewidth'] = v_colorbar.OutlinewidthValidator()
        self._validators['separatethousands'
                        ] = v_colorbar.SeparatethousandsValidator()
        self._validators['showexponent'] = v_colorbar.ShowexponentValidator()
        self._validators['showticklabels'
                        ] = v_colorbar.ShowticklabelsValidator()
        self._validators['showtickprefix'
                        ] = v_colorbar.ShowtickprefixValidator()
        self._validators['showticksuffix'
                        ] = v_colorbar.ShowticksuffixValidator()
        self._validators['thickness'] = v_colorbar.ThicknessValidator()
        self._validators['thicknessmode'] = v_colorbar.ThicknessmodeValidator()
        self._validators['tick0'] = v_colorbar.Tick0Validator()
        self._validators['tickangle'] = v_colorbar.TickangleValidator()
        self._validators['tickcolor'] = v_colorbar.TickcolorValidator()
        self._validators['tickfont'] = v_colorbar.TickfontValidator()
        self._validators['tickformat'] = v_colorbar.TickformatValidator()
        self._validators['tickformatstops'
                        ] = v_colorbar.TickformatstopsValidator()
        self._validators['ticklen'] = v_colorbar.TicklenValidator()
        self._validators['tickmode'] = v_colorbar.TickmodeValidator()
        self._validators['tickprefix'] = v_colorbar.TickprefixValidator()
        self._validators['ticks'] = v_colorbar.TicksValidator()
        self._validators['ticksuffix'] = v_colorbar.TicksuffixValidator()
        self._validators['ticktext'] = v_colorbar.TicktextValidator()
        self._validators['ticktextsrc'] = v_colorbar.TicktextsrcValidator()
        self._validators['tickvals'] = v_colorbar.TickvalsValidator()
        self._validators['tickvalssrc'] = v_colorbar.TickvalssrcValidator()
        self._validators['tickwidth'] = v_colorbar.TickwidthValidator()
        self._validators['title'] = v_colorbar.TitleValidator()
        self._validators['titlefont'] = v_colorbar.TitlefontValidator()
        self._validators['titleside'] = v_colorbar.TitlesideValidator()
        self._validators['x'] = v_colorbar.XValidator()
        self._validators['xanchor'] = v_colorbar.XanchorValidator()
        self._validators['xpad'] = v_colorbar.XpadValidator()
        self._validators['y'] = v_colorbar.YValidator()
        self._validators['yanchor'] = v_colorbar.YanchorValidator()
        self._validators['ypad'] = v_colorbar.YpadValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.bgcolor = bgcolor
        self.bordercolor = bordercolor
        self.borderwidth = borderwidth
        self.dtick = dtick
        self.exponentformat = exponentformat
        self.len = len
        self.lenmode = lenmode
        self.nticks = nticks
        self.outlinecolor = outlinecolor
        self.outlinewidth = outlinewidth
        self.separatethousands = separatethousands
        self.showexponent = showexponent
        self.showticklabels = showticklabels
        self.showtickprefix = showtickprefix
        self.showticksuffix = showticksuffix
        self.thickness = thickness
        self.thicknessmode = thicknessmode
        self.tick0 = tick0
        self.tickangle = tickangle
        self.tickcolor = tickcolor
        self.tickfont = tickfont
        self.tickformat = tickformat
        self.tickformatstops = tickformatstops
        self.ticklen = ticklen
        self.tickmode = tickmode
        self.tickprefix = tickprefix
        self.ticks = ticks
        self.ticksuffix = ticksuffix
        self.ticktext = ticktext
        self.ticktextsrc = ticktextsrc
        self.tickvals = tickvals
        self.tickvalssrc = tickvalssrc
        self.tickwidth = tickwidth
        self.title = title
        self.titlefont = titlefont
        self.titleside = titleside
        self.x = x
        self.xanchor = xanchor
        self.xpad = xpad
        self.y = y
        self.yanchor = yanchor
        self.ypad = ypad

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
