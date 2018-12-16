from plotly.basedatatypes import BaseTraceType
import copy


class Carpet(BaseTraceType):

    # a
    # -
    @property
    def a(self):
        """
        An array containing values of the first parameter value
    
        The 'a' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['a']

    @a.setter
    def a(self, val):
        self['a'] = val

    # a0
    # --
    @property
    def a0(self):
        """
        Alternate to `a`. Builds a linear space of a coordinates. Use
        with `da` where `a0` is the starting coordinate and `da` the
        step.
    
        The 'a0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['a0']

    @a0.setter
    def a0(self, val):
        self['a0'] = val

    # aaxis
    # -----
    @property
    def aaxis(self):
        """
        The 'aaxis' property is an instance of Aaxis
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.Aaxis
          - A dict of string/value properties that will be passed
            to the Aaxis constructor
    
            Supported dict properties:
                
                arraydtick
                    The stride between grid lines along the axis
                arraytick0
                    The starting index of grid lines along the axis
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
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
                    follow the categories in `categoryarray`.
                cheatertype
    
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                dtick
                    The stride between grid lines along the axis
                endline
                    Determines whether or not a line is drawn at
                    along the final value of this axis. If True,
                    the end line is drawn on top of the grid lines.
                endlinecolor
                    Sets the line color of the end line.
                endlinewidth
                    Sets the width (in px) of the end line.
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                fixedrange
                    Determines whether or not this axis is zoom-
                    able. If true, then zoom is disabled.
                gridcolor
                    Sets the axis line color.
                gridwidth
                    Sets the width (in px) of the axis line.
                labelpadding
                    Extra padding between label and the axis
                labelprefix
                    Sets a axis label prefix.
                labelsuffix
                    Sets a axis label suffix.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                minorgridcolor
                    Sets the color of the grid lines.
                minorgridcount
                    Sets the number of minor grid ticks per major
                    grid tick
                minorgridwidth
                    Sets the width (in px) of the grid lines.
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
                    negative, regardless of the input data.
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
                    Determines whether axis labels are drawn on the
                    low side, the high side, both, or neither side
                    of the axis.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                smoothing
    
                startline
                    Determines whether or not a line is drawn at
                    along the starting value of this axis. If True,
                    the start line is drawn on top of the grid
                    lines.
                startlinecolor
                    Sets the line color of the start line.
                startlinewidth
                    Sets the width (in px) of the start line.
                tick0
                    The starting index of grid lines along the axis
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    plotly.graph_objs.carpet.aaxis.Tickformatstop
                    instance or dict with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.carpet.aaxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of carpet.aaxis.tickformatstops
                tickmode
    
                tickprefix
                    Sets a tick label prefix.
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
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                titleoffset
                    An additional amount by which to offset the
                    title from the tick labels, given in pixels
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.

        Returns
        -------
        plotly.graph_objs.carpet.Aaxis
        """
        return self['aaxis']

    @aaxis.setter
    def aaxis(self, val):
        self['aaxis'] = val

    # asrc
    # ----
    @property
    def asrc(self):
        """
        Sets the source reference on plot.ly for  a .
    
        The 'asrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['asrc']

    @asrc.setter
    def asrc(self, val):
        self['asrc'] = val

    # b
    # -
    @property
    def b(self):
        """
        A two dimensional array of y coordinates at each carpet point.
    
        The 'b' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['b']

    @b.setter
    def b(self, val):
        self['b'] = val

    # b0
    # --
    @property
    def b0(self):
        """
        Alternate to `b`. Builds a linear space of a coordinates. Use
        with `db` where `b0` is the starting coordinate and `db` the
        step.
    
        The 'b0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['b0']

    @b0.setter
    def b0(self, val):
        self['b0'] = val

    # baxis
    # -----
    @property
    def baxis(self):
        """
        The 'baxis' property is an instance of Baxis
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.Baxis
          - A dict of string/value properties that will be passed
            to the Baxis constructor
    
            Supported dict properties:
                
                arraydtick
                    The stride between grid lines along the axis
                arraytick0
                    The starting index of grid lines along the axis
                autorange
                    Determines whether or not the range of this
                    axis is computed in relation to the input data.
                    See `rangemode` for more info. If `range` is
                    provided, then `autorange` is set to False.
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
                    follow the categories in `categoryarray`.
                cheatertype
    
                color
                    Sets default for all colors associated with
                    this axis all at once: line, font, tick, and
                    grid colors. Grid color is lightened by
                    blending this with the plot background
                    Individual pieces can override this.
                dtick
                    The stride between grid lines along the axis
                endline
                    Determines whether or not a line is drawn at
                    along the final value of this axis. If True,
                    the end line is drawn on top of the grid lines.
                endlinecolor
                    Sets the line color of the end line.
                endlinewidth
                    Sets the width (in px) of the end line.
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                fixedrange
                    Determines whether or not this axis is zoom-
                    able. If true, then zoom is disabled.
                gridcolor
                    Sets the axis line color.
                gridwidth
                    Sets the width (in px) of the axis line.
                labelpadding
                    Extra padding between label and the axis
                labelprefix
                    Sets a axis label prefix.
                labelsuffix
                    Sets a axis label suffix.
                linecolor
                    Sets the axis line color.
                linewidth
                    Sets the width (in px) of the axis line.
                minorgridcolor
                    Sets the color of the grid lines.
                minorgridcount
                    Sets the number of minor grid ticks per major
                    grid tick
                minorgridwidth
                    Sets the width (in px) of the grid lines.
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
                    negative, regardless of the input data.
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
                    Determines whether axis labels are drawn on the
                    low side, the high side, both, or neither side
                    of the axis.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                smoothing
    
                startline
                    Determines whether or not a line is drawn at
                    along the starting value of this axis. If True,
                    the start line is drawn on top of the grid
                    lines.
                startlinecolor
                    Sets the line color of the start line.
                startlinewidth
                    Sets the width (in px) of the start line.
                tick0
                    The starting index of grid lines along the axis
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickfont
                    Sets the tick font.
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/blob/master/READ
                    ME.md#locale_format And for dates see:
                    https://github.com/d3/d3-time-
                    format/blob/master/README.md#locale_format We
                    add one item to d3's date formatter: "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    plotly.graph_objs.carpet.baxis.Tickformatstop
                    instance or dict with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.carpet.baxis.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of carpet.baxis.tickformatstops
                tickmode
    
                tickprefix
                    Sets a tick label prefix.
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
                title
                    Sets the title of this axis.
                titlefont
                    Sets this axis' title font.
                titleoffset
                    An additional amount by which to offset the
                    title from the tick labels, given in pixels
                type
                    Sets the axis type. By default, plotly attempts
                    to determined the axis type by looking into the
                    data of the traces that referenced the axis in
                    question.

        Returns
        -------
        plotly.graph_objs.carpet.Baxis
        """
        return self['baxis']

    @baxis.setter
    def baxis(self, val):
        self['baxis'] = val

    # bsrc
    # ----
    @property
    def bsrc(self):
        """
        Sets the source reference on plot.ly for  b .
    
        The 'bsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['bsrc']

    @bsrc.setter
    def bsrc(self, val):
        self['bsrc'] = val

    # carpet
    # ------
    @property
    def carpet(self):
        """
        An identifier for this carpet, so that `scattercarpet` and
        `scattercontour` traces can specify a carpet plot on which they
        lie
    
        The 'carpet' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['carpet']

    @carpet.setter
    def carpet(self, val):
        self['carpet'] = val

    # cheaterslope
    # ------------
    @property
    def cheaterslope(self):
        """
        The shift applied to each successive row of data in creating a
        cheater plot. Only used if `x` is been ommitted.
    
        The 'cheaterslope' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cheaterslope']

    @cheaterslope.setter
    def cheaterslope(self, val):
        self['cheaterslope'] = val

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
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements
    
        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['customdata']

    @customdata.setter
    def customdata(self, val):
        self['customdata'] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on plot.ly for  customdata .
    
        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['customdatasrc']

    @customdatasrc.setter
    def customdatasrc(self, val):
        self['customdatasrc'] = val

    # da
    # --
    @property
    def da(self):
        """
        Sets the a coordinate step. See `a0` for more info.
    
        The 'da' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['da']

    @da.setter
    def da(self, val):
        self['da'] = val

    # db
    # --
    @property
    def db(self):
        """
        Sets the b coordinate step. See `b0` for more info.
    
        The 'db' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['db']

    @db.setter
    def db(self, val):
        self['db'] = val

    # font
    # ----
    @property
    def font(self):
        """
        The default font used for axis & tick labels on this carpet
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.Font
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
        plotly.graph_objs.carpet.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.
    
        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on plot.ly for  hoverinfo .
    
        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hoverinfosrc']

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self['hoverinfosrc'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
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
                    Sets the length (in number of characters) of
                    the trace name in the hover labels for this
                    trace. -1 shows the whole name regardless of
                    length. 0-3 shows the first 0-3 characters, and
                    an integer >3 will show the whole name if it is
                    less than that many characters, but if it is
                    longer, will truncate to `namelength - 3`
                    characters and add an ellipsis.
                namelengthsrc
                    Sets the source reference on plot.ly for
                    namelength .

        Returns
        -------
        plotly.graph_objs.carpet.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.
    
        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ids']

    @ids.setter
    def ids(self, val):
        self['ids'] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on plot.ly for  ids .
    
        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['idssrc']

    @idssrc.setter
    def idssrc(self, val):
        self['idssrc'] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.
    
        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['legendgroup']

    @legendgroup.setter
    def legendgroup(self, val):
        self['legendgroup'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the trace.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # selectedpoints
    # --------------
    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.
    
        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['selectedpoints']

    @selectedpoints.setter
    def selectedpoints(self, val):
        self['selectedpoints'] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showlegend']

    @showlegend.setter
    def showlegend(self, val):
        self['showlegend'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.carpet.Stream
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See
                    https://plot.ly/settings for more details.

        Returns
        -------
        plotly.graph_objs.carpet.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['uid']

    @uid.setter
    def uid(self, val):
        self['uid'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).
    
        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        A two dimensional array of x coordinates at each carpet point.
        If ommitted, the plot is a cheater plot and the xaxis is hidden
        by default.
    
        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xaxis
    # -----
    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.
    
        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        return self['xaxis']

    @xaxis.setter
    def xaxis(self, val):
        self['xaxis'] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on plot.ly for  x .
    
        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['xsrc']

    @xsrc.setter
    def xsrc(self, val):
        self['xsrc'] = val

    # y
    # -
    @property
    def y(self):
        """
        A two dimensional array of y coordinates at each carpet point.
    
        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.
    
        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        return self['yaxis']

    @yaxis.setter
    def yaxis(self, val):
        self['yaxis'] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on plot.ly for  y .
    
        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ysrc']

    @ysrc.setter
    def ysrc(self, val):
        self['ysrc'] = val

    # type
    # ----
    @property
    def type(self):
        return self._props['type']

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return ''

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        a
            An array containing values of the first parameter value
        a0
            Alternate to `a`. Builds a linear space of a
            coordinates. Use with `da` where `a0` is the starting
            coordinate and `da` the step.
        aaxis
            plotly.graph_objs.carpet.Aaxis instance or dict with
            compatible properties
        asrc
            Sets the source reference on plot.ly for  a .
        b
            A two dimensional array of y coordinates at each carpet
            point.
        b0
            Alternate to `b`. Builds a linear space of a
            coordinates. Use with `db` where `b0` is the starting
            coordinate and `db` the step.
        baxis
            plotly.graph_objs.carpet.Baxis instance or dict with
            compatible properties
        bsrc
            Sets the source reference on plot.ly for  b .
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `scattercontour` traces can specify a carpet plot
            on which they lie
        cheaterslope
            The shift applied to each successive row of data in
            creating a cheater plot. Only used if `x` is been
            ommitted.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        da
            Sets the a coordinate step. See `a0` for more info.
        db
            Sets the b coordinate step. See `b0` for more info.
        font
            The default font used for axis & tick labels on this
            carpet
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.carpet.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.carpet.Stream instance or dict with
            compatible properties
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            A two dimensional array of x coordinates at each carpet
            point. If ommitted, the plot is a cheater plot and the
            xaxis is hidden by default.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            A two dimensional array of y coordinates at each carpet
            point.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .
        """

    def __init__(
        self,
        arg=None,
        a=None,
        a0=None,
        aaxis=None,
        asrc=None,
        b=None,
        b0=None,
        baxis=None,
        bsrc=None,
        carpet=None,
        cheaterslope=None,
        color=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        font=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        name=None,
        opacity=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        uid=None,
        visible=None,
        x=None,
        xaxis=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ysrc=None,
        **kwargs
    ):
        """
        Construct a new Carpet object
        
        The data describing carpet axis layout is set in `y` and
        (optionally) also `x`. If only `y` is present, `x` the plot is
        interpreted as a cheater plot and is filled in using the `y`
        values. `x` and `y` may either be 2D arrays matching with each
        dimension matching that of `a` and `b`, or they may be 1D
        arrays with total length equal to that of `a` and `b`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Carpet
        a
            An array containing values of the first parameter value
        a0
            Alternate to `a`. Builds a linear space of a
            coordinates. Use with `da` where `a0` is the starting
            coordinate and `da` the step.
        aaxis
            plotly.graph_objs.carpet.Aaxis instance or dict with
            compatible properties
        asrc
            Sets the source reference on plot.ly for  a .
        b
            A two dimensional array of y coordinates at each carpet
            point.
        b0
            Alternate to `b`. Builds a linear space of a
            coordinates. Use with `db` where `b0` is the starting
            coordinate and `db` the step.
        baxis
            plotly.graph_objs.carpet.Baxis instance or dict with
            compatible properties
        bsrc
            Sets the source reference on plot.ly for  b .
        carpet
            An identifier for this carpet, so that `scattercarpet`
            and `scattercontour` traces can specify a carpet plot
            on which they lie
        cheaterslope
            The shift applied to each successive row of data in
            creating a cheater plot. Only used if `x` is been
            ommitted.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        da
            Sets the a coordinate step. See `a0` for more info.
        db
            Sets the b coordinate step. See `b0` for more info.
        font
            The default font used for axis & tick labels on this
            carpet
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.carpet.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stream
            plotly.graph_objs.carpet.Stream instance or dict with
            compatible properties
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            A two dimensional array of x coordinates at each carpet
            point. If ommitted, the plot is a cheater plot and the
            xaxis is hidden by default.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            A two dimensional array of y coordinates at each carpet
            point.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ysrc
            Sets the source reference on plot.ly for  y .

        Returns
        -------
        Carpet
        """
        super(Carpet, self).__init__('carpet')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Carpet 
constructor must be a dict or 
an instance of plotly.graph_objs.Carpet"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (carpet as v_carpet)

        # Initialize validators
        # ---------------------
        self._validators['a'] = v_carpet.AValidator()
        self._validators['a0'] = v_carpet.A0Validator()
        self._validators['aaxis'] = v_carpet.AaxisValidator()
        self._validators['asrc'] = v_carpet.AsrcValidator()
        self._validators['b'] = v_carpet.BValidator()
        self._validators['b0'] = v_carpet.B0Validator()
        self._validators['baxis'] = v_carpet.BaxisValidator()
        self._validators['bsrc'] = v_carpet.BsrcValidator()
        self._validators['carpet'] = v_carpet.CarpetValidator()
        self._validators['cheaterslope'] = v_carpet.CheaterslopeValidator()
        self._validators['color'] = v_carpet.ColorValidator()
        self._validators['customdata'] = v_carpet.CustomdataValidator()
        self._validators['customdatasrc'] = v_carpet.CustomdatasrcValidator()
        self._validators['da'] = v_carpet.DaValidator()
        self._validators['db'] = v_carpet.DbValidator()
        self._validators['font'] = v_carpet.FontValidator()
        self._validators['hoverinfo'] = v_carpet.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_carpet.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_carpet.HoverlabelValidator()
        self._validators['ids'] = v_carpet.IdsValidator()
        self._validators['idssrc'] = v_carpet.IdssrcValidator()
        self._validators['legendgroup'] = v_carpet.LegendgroupValidator()
        self._validators['name'] = v_carpet.NameValidator()
        self._validators['opacity'] = v_carpet.OpacityValidator()
        self._validators['selectedpoints'] = v_carpet.SelectedpointsValidator()
        self._validators['showlegend'] = v_carpet.ShowlegendValidator()
        self._validators['stream'] = v_carpet.StreamValidator()
        self._validators['uid'] = v_carpet.UidValidator()
        self._validators['visible'] = v_carpet.VisibleValidator()
        self._validators['x'] = v_carpet.XValidator()
        self._validators['xaxis'] = v_carpet.XAxisValidator()
        self._validators['xsrc'] = v_carpet.XsrcValidator()
        self._validators['y'] = v_carpet.YValidator()
        self._validators['yaxis'] = v_carpet.YAxisValidator()
        self._validators['ysrc'] = v_carpet.YsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('a', None)
        self['a'] = a if a is not None else _v
        _v = arg.pop('a0', None)
        self['a0'] = a0 if a0 is not None else _v
        _v = arg.pop('aaxis', None)
        self['aaxis'] = aaxis if aaxis is not None else _v
        _v = arg.pop('asrc', None)
        self['asrc'] = asrc if asrc is not None else _v
        _v = arg.pop('b', None)
        self['b'] = b if b is not None else _v
        _v = arg.pop('b0', None)
        self['b0'] = b0 if b0 is not None else _v
        _v = arg.pop('baxis', None)
        self['baxis'] = baxis if baxis is not None else _v
        _v = arg.pop('bsrc', None)
        self['bsrc'] = bsrc if bsrc is not None else _v
        _v = arg.pop('carpet', None)
        self['carpet'] = carpet if carpet is not None else _v
        _v = arg.pop('cheaterslope', None)
        self['cheaterslope'] = cheaterslope if cheaterslope is not None else _v
        _v = arg.pop('color', None)
        self['color'] = color if color is not None else _v
        _v = arg.pop('customdata', None)
        self['customdata'] = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self['customdatasrc'
            ] = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('da', None)
        self['da'] = da if da is not None else _v
        _v = arg.pop('db', None)
        self['db'] = db if db is not None else _v
        _v = arg.pop('font', None)
        self['font'] = font if font is not None else _v
        _v = arg.pop('hoverinfo', None)
        self['hoverinfo'] = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoverinfosrc', None)
        self['hoverinfosrc'] = hoverinfosrc if hoverinfosrc is not None else _v
        _v = arg.pop('hoverlabel', None)
        self['hoverlabel'] = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('ids', None)
        self['ids'] = ids if ids is not None else _v
        _v = arg.pop('idssrc', None)
        self['idssrc'] = idssrc if idssrc is not None else _v
        _v = arg.pop('legendgroup', None)
        self['legendgroup'] = legendgroup if legendgroup is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('selectedpoints', None)
        self['selectedpoints'
            ] = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self['showlegend'] = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self['stream'] = stream if stream is not None else _v
        _v = arg.pop('uid', None)
        self['uid'] = uid if uid is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('xaxis', None)
        self['xaxis'] = xaxis if xaxis is not None else _v
        _v = arg.pop('xsrc', None)
        self['xsrc'] = xsrc if xsrc is not None else _v
        _v = arg.pop('y', None)
        self['y'] = y if y is not None else _v
        _v = arg.pop('yaxis', None)
        self['yaxis'] = yaxis if yaxis is not None else _v
        _v = arg.pop('ysrc', None)
        self['ysrc'] = ysrc if ysrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'carpet'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='carpet', val='carpet'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
