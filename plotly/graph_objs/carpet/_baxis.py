

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Baxis(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'carpet'
    _path_str = 'carpet.baxis'
    _valid_props = {"arraydtick", "arraytick0", "autorange", "autotypenumbers", "categoryarray", "categoryarraysrc", "categoryorder", "cheatertype", "color", "dtick", "endline", "endlinecolor", "endlinewidth", "exponentformat", "fixedrange", "gridcolor", "griddash", "gridwidth", "labelalias", "labelpadding", "labelprefix", "labelsuffix", "linecolor", "linewidth", "minexponent", "minorgridcolor", "minorgridcount", "minorgriddash", "minorgridwidth", "nticks", "range", "rangemode", "separatethousands", "showexponent", "showgrid", "showline", "showticklabels", "showtickprefix", "showticksuffix", "smoothing", "startline", "startlinecolor", "startlinewidth", "tick0", "tickangle", "tickfont", "tickformat", "tickformatstopdefaults", "tickformatstops", "tickmode", "tickprefix", "ticksuffix", "ticktext", "ticktextsrc", "tickvals", "tickvalssrc", "title", "type"}

    # arraydtick
    # ----------
    @property
    def arraydtick(self):
        """
        The stride between grid lines along the axis

        The 'arraydtick' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['arraydtick']

    @arraydtick.setter
    def arraydtick(self, val):
        self['arraydtick'] = val

    # arraytick0
    # ----------
    @property
    def arraytick0(self):
        """
        The starting index of grid lines along the axis

        The 'arraytick0' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['arraytick0']

    @arraytick0.setter
    def arraytick0(self, val):
        self['arraytick0'] = val

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
        return self['autorange']

    @autorange.setter
    def autorange(self, val):
        self['autorange'] = val

    # autotypenumbers
    # ---------------
    @property
    def autotypenumbers(self):
        """
        Using "strict" a numeric string in trace data is not converted
        to a number. Using *convert types* a numeric string in trace
        data may be treated as a number during automatic axis `type`
        detection. Defaults to layout.autotypenumbers.

        The 'autotypenumbers' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['convert types', 'strict']

        Returns
        -------
        Any
        """
        return self['autotypenumbers']

    @autotypenumbers.setter
    def autotypenumbers(self, val):
        self['autotypenumbers'] = val

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
        NDArray
        """
        return self['categoryarray']

    @categoryarray.setter
    def categoryarray(self, val):
        self['categoryarray'] = val

    # categoryarraysrc
    # ----------------
    @property
    def categoryarraysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `categoryarray`.

        The 'categoryarraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['categoryarraysrc']

    @categoryarraysrc.setter
    def categoryarraysrc(self, val):
        self['categoryarraysrc'] = val

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
        `categoryarray`.

        The 'categoryorder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'category ascending', 'category descending',
                'array']

        Returns
        -------
        Any
        """
        return self['categoryorder']

    @categoryorder.setter
    def categoryorder(self, val):
        self['categoryorder'] = val

    # cheatertype
    # -----------
    @property
    def cheatertype(self):
        """
        The 'cheatertype' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['index', 'value']

        Returns
        -------
        Any
        """
        return self['cheatertype']

    @cheatertype.setter
    def cheatertype(self, val):
        self['cheatertype'] = val

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
          - A named CSS color

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        The stride between grid lines along the axis

        The 'dtick' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['dtick']

    @dtick.setter
    def dtick(self, val):
        self['dtick'] = val

    # endline
    # -------
    @property
    def endline(self):
        """
        Determines whether or not a line is drawn at along the final
        value of this axis. If True, the end line is drawn on top of
        the grid lines.

        The 'endline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['endline']

    @endline.setter
    def endline(self, val):
        self['endline'] = val

    # endlinecolor
    # ------------
    @property
    def endlinecolor(self):
        """
        Sets the line color of the end line.

        The 'endlinecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['endlinecolor']

    @endlinecolor.setter
    def endlinecolor(self, val):
        self['endlinecolor'] = val

    # endlinewidth
    # ------------
    @property
    def endlinewidth(self):
        """
        Sets the width (in px) of the end line.

        The 'endlinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['endlinewidth']

    @endlinewidth.setter
    def endlinewidth(self, val):
        self['endlinewidth'] = val

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
        return self['exponentformat']

    @exponentformat.setter
    def exponentformat(self, val):
        self['exponentformat'] = val

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
        return self['fixedrange']

    @fixedrange.setter
    def fixedrange(self, val):
        self['fixedrange'] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the axis line color.

        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['gridcolor']

    @gridcolor.setter
    def gridcolor(self, val):
        self['gridcolor'] = val

    # griddash
    # --------
    @property
    def griddash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The 'griddash' property is an enumeration that may be specified as:
          - One of the following dash styles:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
          - A string containing a dash length list in pixels or percentages
                (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)

        Returns
        -------
        str
        """
        return self['griddash']

    @griddash.setter
    def griddash(self, val):
        self['griddash'] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the width (in px) of the axis line.

        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['gridwidth']

    @gridwidth.setter
    def gridwidth(self, val):
        self['gridwidth'] = val

    # labelalias
    # ----------
    @property
    def labelalias(self):
        """
        Replacement text for specific tick or hover labels. For example
        using {US: 'USA', CA: 'Canada'} changes US to USA and CA to
        Canada. The labels we would have shown must match the keys
        exactly, after adding any tickprefix or ticksuffix. For
        negative numbers the minus sign symbol used (U+2212) is wider
        than the regular ascii dash. That means you need to use −1
        instead of -1. labelalias can be used with any axis type, and
        both keys (if needed) and values (if desired) can include html-
        like tags or MathJax.

        The 'labelalias' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['labelalias']

    @labelalias.setter
    def labelalias(self, val):
        self['labelalias'] = val

    # labelpadding
    # ------------
    @property
    def labelpadding(self):
        """
        Extra padding between label and the axis

        The 'labelpadding' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        return self['labelpadding']

    @labelpadding.setter
    def labelpadding(self, val):
        self['labelpadding'] = val

    # labelprefix
    # -----------
    @property
    def labelprefix(self):
        """
        Sets a axis label prefix.

        The 'labelprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['labelprefix']

    @labelprefix.setter
    def labelprefix(self, val):
        self['labelprefix'] = val

    # labelsuffix
    # -----------
    @property
    def labelsuffix(self):
        """
        Sets a axis label suffix.

        The 'labelsuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['labelsuffix']

    @labelsuffix.setter
    def labelsuffix(self, val):
        self['labelsuffix'] = val

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
          - A named CSS color

        Returns
        -------
        str
        """
        return self['linecolor']

    @linecolor.setter
    def linecolor(self, val):
        self['linecolor'] = val

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
        return self['linewidth']

    @linewidth.setter
    def linewidth(self, val):
        self['linewidth'] = val

    # minexponent
    # -----------
    @property
    def minexponent(self):
        """
        Hide SI prefix for 10^n if |n| is below this number

        The 'minexponent' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['minexponent']

    @minexponent.setter
    def minexponent(self, val):
        self['minexponent'] = val

    # minorgridcolor
    # --------------
    @property
    def minorgridcolor(self):
        """
        Sets the color of the grid lines.

        The 'minorgridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['minorgridcolor']

    @minorgridcolor.setter
    def minorgridcolor(self, val):
        self['minorgridcolor'] = val

    # minorgridcount
    # --------------
    @property
    def minorgridcount(self):
        """
        Sets the number of minor grid ticks per major grid tick

        The 'minorgridcount' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['minorgridcount']

    @minorgridcount.setter
    def minorgridcount(self, val):
        self['minorgridcount'] = val

    # minorgriddash
    # -------------
    @property
    def minorgriddash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        ("solid", "dot", "dash", "longdash", "dashdot", or
        "longdashdot") or a dash length list in px (eg
        "5px,10px,2px,2px").

        The 'minorgriddash' property is an enumeration that may be specified as:
          - One of the following dash styles:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
          - A string containing a dash length list in pixels or percentages
                (e.g. '5px 10px 2px 2px', '5, 10, 2, 2', '10% 20% 40%', etc.)

        Returns
        -------
        str
        """
        return self['minorgriddash']

    @minorgriddash.setter
    def minorgriddash(self, val):
        self['minorgriddash'] = val

    # minorgridwidth
    # --------------
    @property
    def minorgridwidth(self):
        """
        Sets the width (in px) of the grid lines.

        The 'minorgridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['minorgridwidth']

    @minorgridwidth.setter
    def minorgridwidth(self, val):
        self['minorgridwidth'] = val

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
        return self['nticks']

    @nticks.setter
    def nticks(self, val):
        self['nticks'] = val

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
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

    # rangemode
    # ---------
    @property
    def rangemode(self):
        """
        If "normal", the range is computed in relation to the extrema
        of the input data. If "tozero", the range extends to 0,
        regardless of the input data If "nonnegative", the range is
        non-negative, regardless of the input data.

        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'tozero', 'nonnegative']

        Returns
        -------
        Any
        """
        return self['rangemode']

    @rangemode.setter
    def rangemode(self, val):
        self['rangemode'] = val

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
        return self['showexponent']

    @showexponent.setter
    def showexponent(self, val):
        self['showexponent'] = val

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
        return self['showgrid']

    @showgrid.setter
    def showgrid(self, val):
        self['showgrid'] = val

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
        return self['showline']

    @showline.setter
    def showline(self, val):
        self['showline'] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether axis labels are drawn on the low side, the
        high side, both, or neither side of the axis.

        The 'showticklabels' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'end', 'both', 'none']

        Returns
        -------
        Any
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

    # smoothing
    # ---------
    @property
    def smoothing(self):
        """
        The 'smoothing' property is a number and may be specified as:
          - An int or float in the interval [0, 1.3]

        Returns
        -------
        int|float
        """
        return self['smoothing']

    @smoothing.setter
    def smoothing(self, val):
        self['smoothing'] = val

    # startline
    # ---------
    @property
    def startline(self):
        """
        Determines whether or not a line is drawn at along the starting
        value of this axis. If True, the start line is drawn on top of
        the grid lines.

        The 'startline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['startline']

    @startline.setter
    def startline(self, val):
        self['startline'] = val

    # startlinecolor
    # --------------
    @property
    def startlinecolor(self):
        """
        Sets the line color of the start line.

        The 'startlinecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['startlinecolor']

    @startlinecolor.setter
    def startlinecolor(self, val):
        self['startlinecolor'] = val

    # startlinewidth
    # --------------
    @property
    def startlinewidth(self):
        """
        Sets the width (in px) of the start line.

        The 'startlinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['startlinewidth']

    @startlinewidth.setter
    def startlinewidth(self, val):
        self['startlinewidth'] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        The starting index of grid lines along the axis

        The 'tick0' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
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
        specified as a number between -180 and 180.
        Numeric values outside this range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self['tickangle']

    @tickangle.setter
    def tickangle(self, val):
        self['tickangle'] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the tick font.

        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.baxis.Tickfont`
          - A dict of string/value properties that will be passed
            to the Tickfont constructor

        Returns
        -------
        plotly.graph_objs.carpet.baxis.Tickfont
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
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display "09~15~23.46"

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
          - A list or tuple of instances of plotly.graph_objs.carpet.baxis.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor

        Returns
        -------
        tuple[plotly.graph_objs.carpet.baxis.Tickformatstop]
        """
        return self['tickformatstops']

    @tickformatstops.setter
    def tickformatstops(self, val):
        self['tickformatstops'] = val

    # tickformatstopdefaults
    # ----------------------
    @property
    def tickformatstopdefaults(self):
        """
        When used in a template (as
        layout.template.data.carpet.baxis.tickformatstopdefaults), sets
        the default property values to use for elements of
        carpet.baxis.tickformatstops

        The 'tickformatstopdefaults' property is an instance of Tickformatstop
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.baxis.Tickformatstop`
          - A dict of string/value properties that will be passed
            to the Tickformatstop constructor

        Returns
        -------
        plotly.graph_objs.carpet.baxis.Tickformatstop
        """
        return self['tickformatstopdefaults']

    @tickformatstopdefaults.setter
    def tickformatstopdefaults(self, val):
        self['tickformatstopdefaults'] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'array']

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
        Only has an effect if `tickmode` is set to "array". Used with
        `tickvals`.

        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
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
        Sets the source reference on Chart Studio Cloud for `ticktext`.

        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

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
        effect if `tickmode` is set to "array". Used with `ticktext`.

        The 'tickvals' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
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
        Sets the source reference on Chart Studio Cloud for `tickvals`.

        The 'tickvalssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['tickvalssrc']

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self['tickvalssrc'] = val

    # title
    # -----
    @property
    def title(self):
        """
        The 'title' property is an instance of Title
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.carpet.baxis.Title`
          - A dict of string/value properties that will be passed
            to the Title constructor

        Returns
        -------
        plotly.graph_objs.carpet.baxis.Title
        """
        return self['title']

    @title.setter
    def title(self, val):
        self['title'] = val

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
                ['-', 'linear', 'date', 'category']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        arraydtick
            The stride between grid lines along the axis
        arraytick0
            The starting index of grid lines along the axis
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to False.
        autotypenumbers
            Using "strict" a numeric string in trace data is not
            converted to a number. Using *convert types* a numeric
            string in trace data may be treated as a number during
            automatic axis `type` detection. Defaults to
            layout.autotypenumbers.
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on Chart Studio Cloud for
            `categoryarray`.
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
            the categories in `categoryarray`.
        cheatertype

        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            The stride between grid lines along the axis
        endline
            Determines whether or not a line is drawn at along the
            final value of this axis. If True, the end line is
            drawn on top of the grid lines.
        endlinecolor
            Sets the line color of the end line.
        endlinewidth
            Sets the width (in px) of the end line.
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
            Sets the axis line color.
        griddash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        gridwidth
            Sets the width (in px) of the axis line.
        labelalias
            Replacement text for specific tick or hover labels. For
            example using {US: 'USA', CA: 'Canada'} changes US to
            USA and CA to Canada. The labels we would have shown
            must match the keys exactly, after adding any
            tickprefix or ticksuffix. For negative numbers the
            minus sign symbol used (U+2212) is wider than the
            regular ascii dash. That means you need to use −1
            instead of -1. labelalias can be used with any axis
            type, and both keys (if needed) and values (if desired)
            can include html-like tags or MathJax.
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
        minexponent
            Hide SI prefix for 10^n if |n| is below this number
        minorgridcolor
            Sets the color of the grid lines.
        minorgridcount
            Sets the number of minor grid ticks per major grid tick
        minorgriddash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        minorgridwidth
            Sets the width (in px) of the grid lines.
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
            If "normal", the range is computed in relation to the
            extrema of the input data. If "tozero", the range
            extends to 0, regardless of the input data If
            "nonnegative", the range is non-negative, regardless of
            the input data.
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
            Determines whether axis labels are drawn on the low
            side, the high side, both, or neither side of the axis.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        smoothing

        startline
            Determines whether or not a line is drawn at along the
            starting value of this axis. If True, the start line is
            drawn on top of the grid lines.
        startlinecolor
            Sets the line color of the start line.
        startlinewidth
            Sets the width (in px) of the start line.
        tick0
            The starting index of grid lines along the axis
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.carpet.baxis.Ti
            ckformatstop` instances or dicts with compatible
            properties
        tickformatstopdefaults
            When used in a template (as layout.template.data.carpet
            .baxis.tickformatstopdefaults), sets the default
            property values to use for elements of
            carpet.baxis.tickformatstops
        tickmode

        tickprefix
            Sets a tick label prefix.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on Chart Studio Cloud for
            `ticktext`.
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on Chart Studio Cloud for
            `tickvals`.
        title
            :class:`plotly.graph_objects.carpet.baxis.Title`
            instance or dict with compatible properties
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        """
    def __init__(self,
            arg=None,
            arraydtick: int|None = None,
            arraytick0: int|None = None,
            autorange: Any|None = None,
            autotypenumbers: Any|None = None,
            categoryarray: NDArray|None = None,
            categoryarraysrc: str|None = None,
            categoryorder: Any|None = None,
            cheatertype: Any|None = None,
            color: str|None = None,
            dtick: int|float|None = None,
            endline: bool|None = None,
            endlinecolor: str|None = None,
            endlinewidth: int|float|None = None,
            exponentformat: Any|None = None,
            fixedrange: bool|None = None,
            gridcolor: str|None = None,
            griddash: str|None = None,
            gridwidth: int|float|None = None,
            labelalias: Any|None = None,
            labelpadding: int|None = None,
            labelprefix: str|None = None,
            labelsuffix: str|None = None,
            linecolor: str|None = None,
            linewidth: int|float|None = None,
            minexponent: int|float|None = None,
            minorgridcolor: str|None = None,
            minorgridcount: int|None = None,
            minorgriddash: str|None = None,
            minorgridwidth: int|float|None = None,
            nticks: int|None = None,
            range: list|None = None,
            rangemode: Any|None = None,
            separatethousands: bool|None = None,
            showexponent: Any|None = None,
            showgrid: bool|None = None,
            showline: bool|None = None,
            showticklabels: Any|None = None,
            showtickprefix: Any|None = None,
            showticksuffix: Any|None = None,
            smoothing: int|float|None = None,
            startline: bool|None = None,
            startlinecolor: str|None = None,
            startlinewidth: int|float|None = None,
            tick0: int|float|None = None,
            tickangle: int|float|None = None,
            tickfont: None|None = None,
            tickformat: str|None = None,
            tickformatstops: None|None = None,
            tickformatstopdefaults: None|None = None,
            tickmode: Any|None = None,
            tickprefix: str|None = None,
            ticksuffix: str|None = None,
            ticktext: NDArray|None = None,
            ticktextsrc: str|None = None,
            tickvals: NDArray|None = None,
            tickvalssrc: str|None = None,
            title: None|None = None,
            type: Any|None = None,
            **kwargs
        ):
        """
        Construct a new Baxis object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.carpet.Baxis`
        arraydtick
            The stride between grid lines along the axis
        arraytick0
            The starting index of grid lines along the axis
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to False.
        autotypenumbers
            Using "strict" a numeric string in trace data is not
            converted to a number. Using *convert types* a numeric
            string in trace data may be treated as a number during
            automatic axis `type` detection. Defaults to
            layout.autotypenumbers.
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            "array". Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on Chart Studio Cloud for
            `categoryarray`.
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
            the categories in `categoryarray`.
        cheatertype

        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            The stride between grid lines along the axis
        endline
            Determines whether or not a line is drawn at along the
            final value of this axis. If True, the end line is
            drawn on top of the grid lines.
        endlinecolor
            Sets the line color of the end line.
        endlinewidth
            Sets the width (in px) of the end line.
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
            Sets the axis line color.
        griddash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        gridwidth
            Sets the width (in px) of the axis line.
        labelalias
            Replacement text for specific tick or hover labels. For
            example using {US: 'USA', CA: 'Canada'} changes US to
            USA and CA to Canada. The labels we would have shown
            must match the keys exactly, after adding any
            tickprefix or ticksuffix. For negative numbers the
            minus sign symbol used (U+2212) is wider than the
            regular ascii dash. That means you need to use −1
            instead of -1. labelalias can be used with any axis
            type, and both keys (if needed) and values (if desired)
            can include html-like tags or MathJax.
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
        minexponent
            Hide SI prefix for 10^n if |n| is below this number
        minorgridcolor
            Sets the color of the grid lines.
        minorgridcount
            Sets the number of minor grid ticks per major grid tick
        minorgriddash
            Sets the dash style of lines. Set to a dash type string
            ("solid", "dot", "dash", "longdash", "dashdot", or
            "longdashdot") or a dash length list in px (eg
            "5px,10px,2px,2px").
        minorgridwidth
            Sets the width (in px) of the grid lines.
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
            If "normal", the range is computed in relation to the
            extrema of the input data. If "tozero", the range
            extends to 0, regardless of the input data If
            "nonnegative", the range is non-negative, regardless of
            the input data.
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
            Determines whether axis labels are drawn on the low
            side, the high side, both, or neither side of the axis.
        showtickprefix
            If "all", all tick labels are displayed with a prefix.
            If "first", only the first tick is displayed with a
            prefix. If "last", only the last tick is displayed with
            a suffix. If "none", tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        smoothing

        startline
            Determines whether or not a line is drawn at along the
            starting value of this axis. If True, the start line is
            drawn on top of the grid lines.
        startlinecolor
            Sets the line color of the start line.
        startlinewidth
            Sets the width (in px) of the start line.
        tick0
            The starting index of grid lines along the axis
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display "09~15~23.46"
        tickformatstops
            A tuple of :class:`plotly.graph_objects.carpet.baxis.Ti
            ckformatstop` instances or dicts with compatible
            properties
        tickformatstopdefaults
            When used in a template (as layout.template.data.carpet
            .baxis.tickformatstopdefaults), sets the default
            property values to use for elements of
            carpet.baxis.tickformatstops
        tickmode

        tickprefix
            Sets a tick label prefix.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on Chart Studio Cloud for
            `ticktext`.
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on Chart Studio Cloud for
            `tickvals`.
        title
            :class:`plotly.graph_objects.carpet.baxis.Title`
            instance or dict with compatible properties
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.

        Returns
        -------
        Baxis
        """
        super().__init__('baxis')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.carpet.Baxis
constructor must be a dict or
an instance of :class:`plotly.graph_objs.carpet.Baxis`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('arraydtick', arg, arraydtick)
        self._init_provided('arraytick0', arg, arraytick0)
        self._init_provided('autorange', arg, autorange)
        self._init_provided('autotypenumbers', arg, autotypenumbers)
        self._init_provided('categoryarray', arg, categoryarray)
        self._init_provided('categoryarraysrc', arg, categoryarraysrc)
        self._init_provided('categoryorder', arg, categoryorder)
        self._init_provided('cheatertype', arg, cheatertype)
        self._init_provided('color', arg, color)
        self._init_provided('dtick', arg, dtick)
        self._init_provided('endline', arg, endline)
        self._init_provided('endlinecolor', arg, endlinecolor)
        self._init_provided('endlinewidth', arg, endlinewidth)
        self._init_provided('exponentformat', arg, exponentformat)
        self._init_provided('fixedrange', arg, fixedrange)
        self._init_provided('gridcolor', arg, gridcolor)
        self._init_provided('griddash', arg, griddash)
        self._init_provided('gridwidth', arg, gridwidth)
        self._init_provided('labelalias', arg, labelalias)
        self._init_provided('labelpadding', arg, labelpadding)
        self._init_provided('labelprefix', arg, labelprefix)
        self._init_provided('labelsuffix', arg, labelsuffix)
        self._init_provided('linecolor', arg, linecolor)
        self._init_provided('linewidth', arg, linewidth)
        self._init_provided('minexponent', arg, minexponent)
        self._init_provided('minorgridcolor', arg, minorgridcolor)
        self._init_provided('minorgridcount', arg, minorgridcount)
        self._init_provided('minorgriddash', arg, minorgriddash)
        self._init_provided('minorgridwidth', arg, minorgridwidth)
        self._init_provided('nticks', arg, nticks)
        self._init_provided('range', arg, range)
        self._init_provided('rangemode', arg, rangemode)
        self._init_provided('separatethousands', arg, separatethousands)
        self._init_provided('showexponent', arg, showexponent)
        self._init_provided('showgrid', arg, showgrid)
        self._init_provided('showline', arg, showline)
        self._init_provided('showticklabels', arg, showticklabels)
        self._init_provided('showtickprefix', arg, showtickprefix)
        self._init_provided('showticksuffix', arg, showticksuffix)
        self._init_provided('smoothing', arg, smoothing)
        self._init_provided('startline', arg, startline)
        self._init_provided('startlinecolor', arg, startlinecolor)
        self._init_provided('startlinewidth', arg, startlinewidth)
        self._init_provided('tick0', arg, tick0)
        self._init_provided('tickangle', arg, tickangle)
        self._init_provided('tickfont', arg, tickfont)
        self._init_provided('tickformat', arg, tickformat)
        self._init_provided('tickformatstops', arg, tickformatstops)
        self._init_provided('tickformatstopdefaults', arg, tickformatstopdefaults)
        self._init_provided('tickmode', arg, tickmode)
        self._init_provided('tickprefix', arg, tickprefix)
        self._init_provided('ticksuffix', arg, ticksuffix)
        self._init_provided('ticktext', arg, ticktext)
        self._init_provided('ticktextsrc', arg, ticktextsrc)
        self._init_provided('tickvals', arg, tickvals)
        self._init_provided('tickvalssrc', arg, tickvalssrc)
        self._init_provided('title', arg, title)
        self._init_provided('type', arg, type)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
