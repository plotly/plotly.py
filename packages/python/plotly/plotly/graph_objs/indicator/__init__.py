from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Title(_BaseTraceHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the title. It defaults to
        `center` except for bullet charts for which it defaults to
        right.
    
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

    # font
    # ----
    @property
    def font(self):
        """
        Set the font used to display the title
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.title.Font
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
        plotly.graph_objs.indicator.title.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of this indicator.
    
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

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "indicator"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the title. It defaults
            to `center` except for bullet charts for which it
            defaults to right.
        font
            Set the font used to display the title
        text
            Sets the title of this indicator.
        """

    def __init__(self, arg=None, align=None, font=None, text=None, **kwargs):
        """
        Construct a new Title object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.indicator.Title
        align
            Sets the horizontal alignment of the title. It defaults
            to `center` except for bullet charts for which it
            defaults to right.
        font
            Set the font used to display the title
        text
            Sets the title of this indicator.

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
The first argument to the plotly.graph_objs.indicator.Title 
constructor must be a dict or 
an instance of plotly.graph_objs.indicator.Title"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.indicator import title as v_title

        # Initialize validators
        # ---------------------
        self._validators["align"] = v_title.AlignValidator()
        self._validators["font"] = v_title.FontValidator()
        self._validators["text"] = v_title.TextValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("align", None)
        self["align"] = align if align is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("text", None)
        self["text"] = text if text is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Stream(_BaseTraceHierarchyType):

    # maxpoints
    # ---------
    @property
    def maxpoints(self):
        """
        Sets the maximum number of points to keep on the plots from an
        incoming stream. If `maxpoints` is set to 50, only the newest
        50 points will be displayed on the plot.
    
        The 'maxpoints' property is a number and may be specified as:
          - An int or float in the interval [0, 10000]

        Returns
        -------
        int|float
        """
        return self["maxpoints"]

    @maxpoints.setter
    def maxpoints(self, val):
        self["maxpoints"] = val

    # token
    # -----
    @property
    def token(self):
        """
        The stream id number links a data trace on a plot with a
        stream. See https://plot.ly/settings for more details.
    
        The 'token' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["token"]

    @token.setter
    def token(self, val):
        self["token"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "indicator"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.
        """

    def __init__(self, arg=None, maxpoints=None, token=None, **kwargs):
        """
        Construct a new Stream object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.indicator.Stream
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.

        Returns
        -------
        Stream
        """
        super(Stream, self).__init__("stream")

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
The first argument to the plotly.graph_objs.indicator.Stream 
constructor must be a dict or 
an instance of plotly.graph_objs.indicator.Stream"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.indicator import stream as v_stream

        # Initialize validators
        # ---------------------
        self._validators["maxpoints"] = v_stream.MaxpointsValidator()
        self._validators["token"] = v_stream.TokenValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("maxpoints", None)
        self["maxpoints"] = maxpoints if maxpoints is not None else _v
        _v = arg.pop("token", None)
        self["token"] = token if token is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Number(_BaseTraceHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Set the font used to display main number
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.number.Font
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
        plotly.graph_objs.indicator.number.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # prefix
    # ------
    @property
    def prefix(self):
        """
        Sets a prefix appearing before the number.
    
        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    # suffix
    # ------
    @property
    def suffix(self):
        """
        Sets a suffix appearing next to the number.
    
        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    # valueformat
    # -----------
    @property
    def valueformat(self):
        """
        Sets the value formatting rule using d3 formatting mini-
        language which is similar to those of Python. See
        https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format
    
        The 'valueformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["valueformat"]

    @valueformat.setter
    def valueformat(self, val):
        self["valueformat"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "indicator"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Set the font used to display main number
        prefix
            Sets a prefix appearing before the number.
        suffix
            Sets a suffix appearing next to the number.
        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        """

    def __init__(
        self, arg=None, font=None, prefix=None, suffix=None, valueformat=None, **kwargs
    ):
        """
        Construct a new Number object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.indicator.Number
        font
            Set the font used to display main number
        prefix
            Sets a prefix appearing before the number.
        suffix
            Sets a suffix appearing next to the number.
        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format

        Returns
        -------
        Number
        """
        super(Number, self).__init__("number")

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
The first argument to the plotly.graph_objs.indicator.Number 
constructor must be a dict or 
an instance of plotly.graph_objs.indicator.Number"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.indicator import number as v_number

        # Initialize validators
        # ---------------------
        self._validators["font"] = v_number.FontValidator()
        self._validators["prefix"] = v_number.PrefixValidator()
        self._validators["suffix"] = v_number.SuffixValidator()
        self._validators["valueformat"] = v_number.ValueformatValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("prefix", None)
        self["prefix"] = prefix if prefix is not None else _v
        _v = arg.pop("suffix", None)
        self["suffix"] = suffix if suffix is not None else _v
        _v = arg.pop("valueformat", None)
        self["valueformat"] = valueformat if valueformat is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gauge(_BaseTraceHierarchyType):

    # axis
    # ----
    @property
    def axis(self):
        """
        The 'axis' property is an instance of Axis
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.gauge.Axis
          - A dict of string/value properties that will be passed
            to the Axis constructor
    
            Supported dict properties:
                
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
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                range
                    Sets the range of this axis.
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
                    A tuple of plotly.graph_objects.indicator.gauge
                    .axis.Tickformatstop instances or dicts with
                    compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.indicator.gauge.axis.tickformatstopdefaults),
                    sets the default property values to use for
                    elements of
                    indicator.gauge.axis.tickformatstops
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
                visible
                    A single toggle to hide the axis while
                    preserving interaction like dragging. Default
                    is true when a cheater plot is present on the
                    axis, otherwise false

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Axis
        """
        return self["axis"]

    @axis.setter
    def axis(self, val):
        self["axis"] = val

    # bar
    # ---
    @property
    def bar(self):
        """
        Set the appearance of the gauge's value
    
        The 'bar' property is an instance of Bar
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.gauge.Bar
          - A dict of string/value properties that will be passed
            to the Bar constructor
    
            Supported dict properties:
                
                color
                    Sets the background color of the arc.
                line
                    plotly.graph_objects.indicator.gauge.bar.Line
                    instance or dict with compatible properties
                thickness
                    Sets the thickness of the bar as a fraction of
                    the total thickness of the gauge.

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Bar
        """
        return self["bar"]

    @bar.setter
    def bar(self, val):
        self["bar"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the gauge background color.
    
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
        Sets the color of the border enclosing the gauge.
    
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
        Sets the width (in px) of the border enclosing the gauge.
    
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

    # shape
    # -----
    @property
    def shape(self):
        """
        Set the shape of the gauge
    
        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['angular', 'bullet']

        Returns
        -------
        Any
        """
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    # steps
    # -----
    @property
    def steps(self):
        """
        The 'steps' property is a tuple of instances of
        Step that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.indicator.gauge.Step
          - A list or tuple of dicts of string/value properties that
            will be passed to the Step constructor
    
            Supported dict properties:
                
                color
                    Sets the background color of the arc.
                line
                    plotly.graph_objects.indicator.gauge.step.Line
                    instance or dict with compatible properties
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
                range
                    Sets the range of this axis.
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
                thickness
                    Sets the thickness of the bar as a fraction of
                    the total thickness of the gauge.

        Returns
        -------
        tuple[plotly.graph_objs.indicator.gauge.Step]
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
        layout.template.data.indicator.gauge.stepdefaults), sets the
        default property values to use for elements of
        indicator.gauge.steps
    
        The 'stepdefaults' property is an instance of Step
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.gauge.Step
          - A dict of string/value properties that will be passed
            to the Step constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Step
        """
        return self["stepdefaults"]

    @stepdefaults.setter
    def stepdefaults(self, val):
        self["stepdefaults"] = val

    # threshold
    # ---------
    @property
    def threshold(self):
        """
        The 'threshold' property is an instance of Threshold
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.gauge.Threshold
          - A dict of string/value properties that will be passed
            to the Threshold constructor
    
            Supported dict properties:
                
                line
                    plotly.graph_objects.indicator.gauge.threshold.
                    Line instance or dict with compatible
                    properties
                thickness
                    Sets the thickness of the threshold line as a
                    fraction of the thickness of the gauge.
                value
                    Sets a treshold value drawn as a line.

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Threshold
        """
        return self["threshold"]

    @threshold.setter
    def threshold(self, val):
        self["threshold"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "indicator"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        axis
            plotly.graph_objects.indicator.gauge.Axis instance or
            dict with compatible properties
        bar
            Set the appearance of the gauge's value
        bgcolor
            Sets the gauge background color.
        bordercolor
            Sets the color of the border enclosing the gauge.
        borderwidth
            Sets the width (in px) of the border enclosing the
            gauge.
        shape
            Set the shape of the gauge
        steps
            A tuple of plotly.graph_objects.indicator.gauge.Step
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.data.indicator.gauge.stepdefaults),
            sets the default property values to use for elements of
            indicator.gauge.steps
        threshold
            plotly.graph_objects.indicator.gauge.Threshold instance
            or dict with compatible properties
        """

    def __init__(
        self,
        arg=None,
        axis=None,
        bar=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        shape=None,
        steps=None,
        stepdefaults=None,
        threshold=None,
        **kwargs
    ):
        """
        Construct a new Gauge object
        
        The gauge of the Indicator plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.indicator.Gauge
        axis
            plotly.graph_objects.indicator.gauge.Axis instance or
            dict with compatible properties
        bar
            Set the appearance of the gauge's value
        bgcolor
            Sets the gauge background color.
        bordercolor
            Sets the color of the border enclosing the gauge.
        borderwidth
            Sets the width (in px) of the border enclosing the
            gauge.
        shape
            Set the shape of the gauge
        steps
            A tuple of plotly.graph_objects.indicator.gauge.Step
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.data.indicator.gauge.stepdefaults),
            sets the default property values to use for elements of
            indicator.gauge.steps
        threshold
            plotly.graph_objects.indicator.gauge.Threshold instance
            or dict with compatible properties

        Returns
        -------
        Gauge
        """
        super(Gauge, self).__init__("gauge")

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
The first argument to the plotly.graph_objs.indicator.Gauge 
constructor must be a dict or 
an instance of plotly.graph_objs.indicator.Gauge"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.indicator import gauge as v_gauge

        # Initialize validators
        # ---------------------
        self._validators["axis"] = v_gauge.AxisValidator()
        self._validators["bar"] = v_gauge.BarValidator()
        self._validators["bgcolor"] = v_gauge.BgcolorValidator()
        self._validators["bordercolor"] = v_gauge.BordercolorValidator()
        self._validators["borderwidth"] = v_gauge.BorderwidthValidator()
        self._validators["shape"] = v_gauge.ShapeValidator()
        self._validators["steps"] = v_gauge.StepsValidator()
        self._validators["stepdefaults"] = v_gauge.StepValidator()
        self._validators["threshold"] = v_gauge.ThresholdValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("axis", None)
        self["axis"] = axis if axis is not None else _v
        _v = arg.pop("bar", None)
        self["bar"] = bar if bar is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("shape", None)
        self["shape"] = shape if shape is not None else _v
        _v = arg.pop("steps", None)
        self["steps"] = steps if steps is not None else _v
        _v = arg.pop("stepdefaults", None)
        self["stepdefaults"] = stepdefaults if stepdefaults is not None else _v
        _v = arg.pop("threshold", None)
        self["threshold"] = threshold if threshold is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Domain(_BaseTraceHierarchyType):

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this indicator trace .
    
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
        grid for this indicator trace .
    
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
        Sets the horizontal domain of this indicator trace (in plot
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
        Sets the vertical domain of this indicator trace (in plot
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
        return "indicator"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this indicator trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this indicator trace .
        x
            Sets the horizontal domain of this indicator trace (in
            plot fraction).
        y
            Sets the vertical domain of this indicator trace (in
            plot fraction).
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.indicator.Domain
        column
            If there is a layout grid, use the domain for this
            column in the grid for this indicator trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this indicator trace .
        x
            Sets the horizontal domain of this indicator trace (in
            plot fraction).
        y
            Sets the vertical domain of this indicator trace (in
            plot fraction).

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
The first argument to the plotly.graph_objs.indicator.Domain 
constructor must be a dict or 
an instance of plotly.graph_objs.indicator.Domain"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.indicator import domain as v_domain

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


from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Delta(_BaseTraceHierarchyType):

    # decreasing
    # ----------
    @property
    def decreasing(self):
        """
        The 'decreasing' property is an instance of Decreasing
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.delta.Decreasing
          - A dict of string/value properties that will be passed
            to the Decreasing constructor
    
            Supported dict properties:
                
                color
                    Sets the color for increasing value.
                symbol
                    Sets the symbol to display for increasing value

        Returns
        -------
        plotly.graph_objs.indicator.delta.Decreasing
        """
        return self["decreasing"]

    @decreasing.setter
    def decreasing(self, val):
        self["decreasing"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Set the font used to display the delta
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.delta.Font
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
        plotly.graph_objs.indicator.delta.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # increasing
    # ----------
    @property
    def increasing(self):
        """
        The 'increasing' property is an instance of Increasing
        that may be specified as:
          - An instance of plotly.graph_objs.indicator.delta.Increasing
          - A dict of string/value properties that will be passed
            to the Increasing constructor
    
            Supported dict properties:
                
                color
                    Sets the color for increasing value.
                symbol
                    Sets the symbol to display for increasing value

        Returns
        -------
        plotly.graph_objs.indicator.delta.Increasing
        """
        return self["increasing"]

    @increasing.setter
    def increasing(self, val):
        self["increasing"] = val

    # position
    # --------
    @property
    def position(self):
        """
        Sets the position of delta with respect to the number.
    
        The 'position' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'bottom', 'left', 'right']

        Returns
        -------
        Any
        """
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

    # reference
    # ---------
    @property
    def reference(self):
        """
        Sets the reference value to compute the delta. By default, it
        is set to the current value.
    
        The 'reference' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["reference"]

    @reference.setter
    def reference(self, val):
        self["reference"] = val

    # relative
    # --------
    @property
    def relative(self):
        """
        Show relative change
    
        The 'relative' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["relative"]

    @relative.setter
    def relative(self, val):
        self["relative"] = val

    # valueformat
    # -----------
    @property
    def valueformat(self):
        """
        Sets the value formatting rule using d3 formatting mini-
        language which is similar to those of Python. See
        https://github.com/d3/d3-3.x-api-
        reference/blob/master/Formatting.md#d3_format
    
        The 'valueformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["valueformat"]

    @valueformat.setter
    def valueformat(self, val):
        self["valueformat"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "indicator"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        decreasing
            plotly.graph_objects.indicator.delta.Decreasing
            instance or dict with compatible properties
        font
            Set the font used to display the delta
        increasing
            plotly.graph_objects.indicator.delta.Increasing
            instance or dict with compatible properties
        position
            Sets the position of delta with respect to the number.
        reference
            Sets the reference value to compute the delta. By
            default, it is set to the current value.
        relative
            Show relative change
        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format
        """

    def __init__(
        self,
        arg=None,
        decreasing=None,
        font=None,
        increasing=None,
        position=None,
        reference=None,
        relative=None,
        valueformat=None,
        **kwargs
    ):
        """
        Construct a new Delta object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.indicator.Delta
        decreasing
            plotly.graph_objects.indicator.delta.Decreasing
            instance or dict with compatible properties
        font
            Set the font used to display the delta
        increasing
            plotly.graph_objects.indicator.delta.Increasing
            instance or dict with compatible properties
        position
            Sets the position of delta with respect to the number.
        reference
            Sets the reference value to compute the delta. By
            default, it is set to the current value.
        relative
            Show relative change
        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See
            https://github.com/d3/d3-3.x-api-
            reference/blob/master/Formatting.md#d3_format

        Returns
        -------
        Delta
        """
        super(Delta, self).__init__("delta")

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
The first argument to the plotly.graph_objs.indicator.Delta 
constructor must be a dict or 
an instance of plotly.graph_objs.indicator.Delta"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.indicator import delta as v_delta

        # Initialize validators
        # ---------------------
        self._validators["decreasing"] = v_delta.DecreasingValidator()
        self._validators["font"] = v_delta.FontValidator()
        self._validators["increasing"] = v_delta.IncreasingValidator()
        self._validators["position"] = v_delta.PositionValidator()
        self._validators["reference"] = v_delta.ReferenceValidator()
        self._validators["relative"] = v_delta.RelativeValidator()
        self._validators["valueformat"] = v_delta.ValueformatValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("decreasing", None)
        self["decreasing"] = decreasing if decreasing is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("increasing", None)
        self["increasing"] = increasing if increasing is not None else _v
        _v = arg.pop("position", None)
        self["position"] = position if position is not None else _v
        _v = arg.pop("reference", None)
        self["reference"] = reference if reference is not None else _v
        _v = arg.pop("relative", None)
        self["relative"] = relative if relative is not None else _v
        _v = arg.pop("valueformat", None)
        self["valueformat"] = valueformat if valueformat is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = [
    "Delta",
    "Domain",
    "Gauge",
    "Number",
    "Stream",
    "Title",
    "delta",
    "gauge",
    "number",
    "title",
]

from plotly.graph_objs.indicator import title
from plotly.graph_objs.indicator import number
from plotly.graph_objs.indicator import gauge
from plotly.graph_objs.indicator import delta
