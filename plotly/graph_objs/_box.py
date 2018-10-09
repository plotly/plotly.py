from plotly.basedatatypes import BaseTraceType
import copy


class Box(BaseTraceType):

    # boxmean
    # -------
    @property
    def boxmean(self):
        """
        If True, the mean of the box(es)' underlying distribution is
        drawn as a dashed line inside the box(es). If "sd" the standard
        deviation is also drawn.
    
        The 'boxmean' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, 'sd', False]

        Returns
        -------
        Any
        """
        return self['boxmean']

    @boxmean.setter
    def boxmean(self, val):
        self['boxmean'] = val

    # boxpoints
    # ---------
    @property
    def boxpoints(self):
        """
        If "outliers", only the sample points lying outside the
        whiskers are shown If "suspectedoutliers", the outlier points
        are shown and points either less than 4*Q1-3*Q3 or greater than
        4*Q3-3*Q1 are highlighted (see `outliercolor`) If "all", all
        sample points are shown If False, only the box(es) are shown
        with no sample points
    
        The 'boxpoints' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'outliers', 'suspectedoutliers', False]

        Returns
        -------
        Any
        """
        return self['boxpoints']

    @boxpoints.setter
    def boxpoints(self, val):
        self['boxpoints'] = val

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

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the fill color. Defaults to a half-transparent variant of
        the line color, marker color, or marker line color, whichever
        is available.
    
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
        return self['fillcolor']

    @fillcolor.setter
    def fillcolor(self, val):
        self['fillcolor'] = val

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
          - An instance of plotly.graph_objs.box.Hoverlabel
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
        plotly.graph_objs.box.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # hoveron
    # -------
    @property
    def hoveron(self):
        """
        Do the hover effects highlight individual boxes  or sample
        points or both?
    
        The 'hoveron' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['boxes', 'points'] joined with '+' characters
            (e.g. 'boxes+points')

        Returns
        -------
        Any
        """
        return self['hoveron']

    @hoveron.setter
    def hoveron(self, val):
        self['hoveron'] = val

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

    # jitter
    # ------
    @property
    def jitter(self):
        """
        Sets the amount of jitter in the sample points drawn. If 0, the
        sample points align along the distribution axis. If 1, the
        sample points are drawn in a random jitter of width equal to
        the width of the box(es).
    
        The 'jitter' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['jitter']

    @jitter.setter
    def jitter(self, val):
        self['jitter'] = val

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

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.box.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of line bounding the box(es).
                width
                    Sets the width (in px) of line bounding the
                    box(es).

        Returns
        -------
        plotly.graph_objs.box.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.box.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets themarkercolor. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `marker.cmin` and `marker.cmax` if set.
                line
                    plotly.graph_objs.box.marker.Line instance or
                    dict with compatible properties
                opacity
                    Sets the marker opacity.
                outliercolor
                    Sets the color of the outlier sample points.
                size
                    Sets the marker size (in px).
                symbol
                    Sets the marker symbol type. Adding 100 is
                    equivalent to appending "-open" to a symbol
                    name. Adding 200 is equivalent to appending
                    "-dot" to a symbol name. Adding 300 is
                    equivalent to appending "-open-dot" or "dot-
                    open" to a symbol name.

        Returns
        -------
        plotly.graph_objs.box.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover. For box traces, the name will also be used for
        the position coordinate, if `x` and `x0` (`y` and `y0` if
        horizontal) are missing and the position axis is categorical
    
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

    # notched
    # -------
    @property
    def notched(self):
        """
        Determines whether or not notches should be drawn.
    
        The 'notched' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['notched']

    @notched.setter
    def notched(self, val):
        self['notched'] = val

    # notchwidth
    # ----------
    @property
    def notchwidth(self):
        """
        Sets the width of the notches relative to the box' width. For
        example, with 0, the notches are as wide as the box(es).
    
        The 'notchwidth' property is a number and may be specified as:
          - An int or float in the interval [0, 0.5]

        Returns
        -------
        int|float
        """
        return self['notchwidth']

    @notchwidth.setter
    def notchwidth(self, val):
        self['notchwidth'] = val

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

    # orientation
    # -----------
    @property
    def orientation(self):
        """
        Sets the orientation of the box(es). If "v" ("h"), the
        distribution is visualized along the vertical (horizontal).
    
        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        return self['orientation']

    @orientation.setter
    def orientation(self, val):
        self['orientation'] = val

    # pointpos
    # --------
    @property
    def pointpos(self):
        """
        Sets the position of the sample points in relation to the
        box(es). If 0, the sample points are places over the center of
        the box(es). Positive (negative) values correspond to positions
        to the right (left) for vertical boxes and above (below) for
        horizontal boxes
    
        The 'pointpos' property is a number and may be specified as:
          - An int or float in the interval [-2, 2]

        Returns
        -------
        int|float
        """
        return self['pointpos']

    @pointpos.setter
    def pointpos(self, val):
        self['pointpos'] = val

    # selected
    # --------
    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of plotly.graph_objs.box.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.box.selected.Marker instance
                    or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.box.Selected
        """
        return self['selected']

    @selected.setter
    def selected(self, val):
        self['selected'] = val

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
          - An instance of plotly.graph_objs.box.Stream
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
        plotly.graph_objs.box.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text elements associated with each sample value. If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (x,y) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on plot.ly for  text .
    
        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['textsrc']

    @textsrc.setter
    def textsrc(self, val):
        self['textsrc'] = val

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

    # unselected
    # ----------
    @property
    def unselected(self):
        """
        The 'unselected' property is an instance of Unselected
        that may be specified as:
          - An instance of plotly.graph_objs.box.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.box.unselected.Marker
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.box.Unselected
        """
        return self['unselected']

    @unselected.setter
    def unselected(self, val):
        self['unselected'] = val

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

    # whiskerwidth
    # ------------
    @property
    def whiskerwidth(self):
        """
        Sets the width of the whiskers relative to the box' width. For
        example, with 1, the whiskers are as wide as the box(es).
    
        The 'whiskerwidth' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['whiskerwidth']

    @whiskerwidth.setter
    def whiskerwidth(self, val):
        self['whiskerwidth'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x sample data or coordinates. See overview for more
        info.
    
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

    # x0
    # --
    @property
    def x0(self):
        """
        Sets the x coordinate of the box. See overview for more info.
    
        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x0']

    @x0.setter
    def x0(self, val):
        self['x0'] = val

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

    # xcalendar
    # ---------
    @property
    def xcalendar(self):
        """
        Sets the calendar system to use with `x` date data.
    
        The 'xcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['xcalendar']

    @xcalendar.setter
    def xcalendar(self, val):
        self['xcalendar'] = val

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
        Sets the y sample data or coordinates. See overview for more
        info.
    
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

    # y0
    # --
    @property
    def y0(self):
        """
        Sets the y coordinate of the box. See overview for more info.
    
        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y0']

    @y0.setter
    def y0(self, val):
        self['y0'] = val

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

    # ycalendar
    # ---------
    @property
    def ycalendar(self):
        """
        Sets the calendar system to use with `y` date data.
    
        The 'ycalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['ycalendar']

    @ycalendar.setter
    def ycalendar(self, val):
        self['ycalendar'] = val

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
        boxmean
            If True, the mean of the box(es)' underlying
            distribution is drawn as a dashed line inside the
            box(es). If "sd" the standard deviation is also drawn.
        boxpoints
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the box(es) are shown with no sample
            points
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.box.Hoverlabel instance or dict with
            compatible properties
        hoveron
            Do the hover effects highlight individual boxes  or
            sample points or both?
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the box(es).
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.box.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.box.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For box traces, the name will
            also be used for the position coordinate, if `x` and
            `x0` (`y` and `y0` if horizontal) are missing and the
            position axis is categorical
        notched
            Determines whether or not notches should be drawn.
        notchwidth
            Sets the width of the notches relative to the box'
            width. For example, with 0, the notches are as wide as
            the box(es).
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the box(es). If "v" ("h"), the
            distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the box(es). If 0, the sample points are places over
            the center of the box(es). Positive (negative) values
            correspond to positions to the right (left) for
            vertical boxes and above (below) for horizontal boxes
        selected
            plotly.graph_objs.box.Selected instance or dict with
            compatible properties
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
            plotly.graph_objs.box.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        unselected
            plotly.graph_objs.box.Unselected instance or dict with
            compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        whiskerwidth
            Sets the width of the whiskers relative to the box'
            width. For example, with 1, the whiskers are as wide as
            the box(es).
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate of the box. See overview for more
            info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate of the box. See overview for more
            info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        """

    def __init__(
        self,
        arg=None,
        boxmean=None,
        boxpoints=None,
        customdata=None,
        customdatasrc=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legendgroup=None,
        line=None,
        marker=None,
        name=None,
        notched=None,
        notchwidth=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        unselected=None,
        visible=None,
        whiskerwidth=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ysrc=None,
        **kwargs
    ):
        """
        Construct a new Box object
        
        In vertical (horizontal) box plots, statistics are computed
        using `y` (`x`) values. By supplying an `x` (`y`) array, one
        box per distinct x (y) value is drawn If no `x` (`y`) list is
        provided, a single box is drawn. That box position is then
        positioned with with `name` or with `x0` (`y0`) if provided.
        Each box spans from quartile 1 (Q1) to quartile 3 (Q3). The
        second quartile (Q2) is marked by a line inside the box. By
        default, the whiskers correspond to the box' edges +/- 1.5
        times the interquartile range (IQR = Q3-Q1), see "boxpoints"
        for other options.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Box
        boxmean
            If True, the mean of the box(es)' underlying
            distribution is drawn as a dashed line inside the
            box(es). If "sd" the standard deviation is also drawn.
        boxpoints
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the box(es) are shown with no sample
            points
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.box.Hoverlabel instance or dict with
            compatible properties
        hoveron
            Do the hover effects highlight individual boxes  or
            sample points or both?
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        jitter
            Sets the amount of jitter in the sample points drawn.
            If 0, the sample points align along the distribution
            axis. If 1, the sample points are drawn in a random
            jitter of width equal to the width of the box(es).
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.box.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.box.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For box traces, the name will
            also be used for the position coordinate, if `x` and
            `x0` (`y` and `y0` if horizontal) are missing and the
            position axis is categorical
        notched
            Determines whether or not notches should be drawn.
        notchwidth
            Sets the width of the notches relative to the box'
            width. For example, with 0, the notches are as wide as
            the box(es).
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the box(es). If "v" ("h"), the
            distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the box(es). If 0, the sample points are places over
            the center of the box(es). Positive (negative) values
            correspond to positions to the right (left) for
            vertical boxes and above (below) for horizontal boxes
        selected
            plotly.graph_objs.box.Selected instance or dict with
            compatible properties
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
            plotly.graph_objs.box.Stream instance or dict with
            compatible properties
        text
            Sets the text elements associated with each sample
            value. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        unselected
            plotly.graph_objs.box.Unselected instance or dict with
            compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        whiskerwidth
            Sets the width of the whiskers relative to the box'
            width. For example, with 1, the whiskers are as wide as
            the box(es).
        x
            Sets the x sample data or coordinates. See overview for
            more info.
        x0
            Sets the x coordinate of the box. See overview for more
            info.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y sample data or coordinates. See overview for
            more info.
        y0
            Sets the y coordinate of the box. See overview for more
            info.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .

        Returns
        -------
        Box
        """
        super(Box, self).__init__('box')

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
The first argument to the plotly.graph_objs.Box 
constructor must be a dict or 
an instance of plotly.graph_objs.Box"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (box as v_box)

        # Initialize validators
        # ---------------------
        self._validators['boxmean'] = v_box.BoxmeanValidator()
        self._validators['boxpoints'] = v_box.BoxpointsValidator()
        self._validators['customdata'] = v_box.CustomdataValidator()
        self._validators['customdatasrc'] = v_box.CustomdatasrcValidator()
        self._validators['fillcolor'] = v_box.FillcolorValidator()
        self._validators['hoverinfo'] = v_box.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_box.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_box.HoverlabelValidator()
        self._validators['hoveron'] = v_box.HoveronValidator()
        self._validators['ids'] = v_box.IdsValidator()
        self._validators['idssrc'] = v_box.IdssrcValidator()
        self._validators['jitter'] = v_box.JitterValidator()
        self._validators['legendgroup'] = v_box.LegendgroupValidator()
        self._validators['line'] = v_box.LineValidator()
        self._validators['marker'] = v_box.MarkerValidator()
        self._validators['name'] = v_box.NameValidator()
        self._validators['notched'] = v_box.NotchedValidator()
        self._validators['notchwidth'] = v_box.NotchwidthValidator()
        self._validators['opacity'] = v_box.OpacityValidator()
        self._validators['orientation'] = v_box.OrientationValidator()
        self._validators['pointpos'] = v_box.PointposValidator()
        self._validators['selected'] = v_box.SelectedValidator()
        self._validators['selectedpoints'] = v_box.SelectedpointsValidator()
        self._validators['showlegend'] = v_box.ShowlegendValidator()
        self._validators['stream'] = v_box.StreamValidator()
        self._validators['text'] = v_box.TextValidator()
        self._validators['textsrc'] = v_box.TextsrcValidator()
        self._validators['uid'] = v_box.UidValidator()
        self._validators['unselected'] = v_box.UnselectedValidator()
        self._validators['visible'] = v_box.VisibleValidator()
        self._validators['whiskerwidth'] = v_box.WhiskerwidthValidator()
        self._validators['x'] = v_box.XValidator()
        self._validators['x0'] = v_box.X0Validator()
        self._validators['xaxis'] = v_box.XAxisValidator()
        self._validators['xcalendar'] = v_box.XcalendarValidator()
        self._validators['xsrc'] = v_box.XsrcValidator()
        self._validators['y'] = v_box.YValidator()
        self._validators['y0'] = v_box.Y0Validator()
        self._validators['yaxis'] = v_box.YAxisValidator()
        self._validators['ycalendar'] = v_box.YcalendarValidator()
        self._validators['ysrc'] = v_box.YsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('boxmean', None)
        self['boxmean'] = boxmean if boxmean is not None else _v
        _v = arg.pop('boxpoints', None)
        self['boxpoints'] = boxpoints if boxpoints is not None else _v
        _v = arg.pop('customdata', None)
        self['customdata'] = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self['customdatasrc'
            ] = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('fillcolor', None)
        self['fillcolor'] = fillcolor if fillcolor is not None else _v
        _v = arg.pop('hoverinfo', None)
        self['hoverinfo'] = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoverinfosrc', None)
        self['hoverinfosrc'] = hoverinfosrc if hoverinfosrc is not None else _v
        _v = arg.pop('hoverlabel', None)
        self['hoverlabel'] = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('hoveron', None)
        self['hoveron'] = hoveron if hoveron is not None else _v
        _v = arg.pop('ids', None)
        self['ids'] = ids if ids is not None else _v
        _v = arg.pop('idssrc', None)
        self['idssrc'] = idssrc if idssrc is not None else _v
        _v = arg.pop('jitter', None)
        self['jitter'] = jitter if jitter is not None else _v
        _v = arg.pop('legendgroup', None)
        self['legendgroup'] = legendgroup if legendgroup is not None else _v
        _v = arg.pop('line', None)
        self['line'] = line if line is not None else _v
        _v = arg.pop('marker', None)
        self['marker'] = marker if marker is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('notched', None)
        self['notched'] = notched if notched is not None else _v
        _v = arg.pop('notchwidth', None)
        self['notchwidth'] = notchwidth if notchwidth is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('orientation', None)
        self['orientation'] = orientation if orientation is not None else _v
        _v = arg.pop('pointpos', None)
        self['pointpos'] = pointpos if pointpos is not None else _v
        _v = arg.pop('selected', None)
        self['selected'] = selected if selected is not None else _v
        _v = arg.pop('selectedpoints', None)
        self['selectedpoints'
            ] = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self['showlegend'] = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self['stream'] = stream if stream is not None else _v
        _v = arg.pop('text', None)
        self['text'] = text if text is not None else _v
        _v = arg.pop('textsrc', None)
        self['textsrc'] = textsrc if textsrc is not None else _v
        _v = arg.pop('uid', None)
        self['uid'] = uid if uid is not None else _v
        _v = arg.pop('unselected', None)
        self['unselected'] = unselected if unselected is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v
        _v = arg.pop('whiskerwidth', None)
        self['whiskerwidth'] = whiskerwidth if whiskerwidth is not None else _v
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('x0', None)
        self['x0'] = x0 if x0 is not None else _v
        _v = arg.pop('xaxis', None)
        self['xaxis'] = xaxis if xaxis is not None else _v
        _v = arg.pop('xcalendar', None)
        self['xcalendar'] = xcalendar if xcalendar is not None else _v
        _v = arg.pop('xsrc', None)
        self['xsrc'] = xsrc if xsrc is not None else _v
        _v = arg.pop('y', None)
        self['y'] = y if y is not None else _v
        _v = arg.pop('y0', None)
        self['y0'] = y0 if y0 is not None else _v
        _v = arg.pop('yaxis', None)
        self['yaxis'] = yaxis if yaxis is not None else _v
        _v = arg.pop('ycalendar', None)
        self['ycalendar'] = ycalendar if ycalendar is not None else _v
        _v = arg.pop('ysrc', None)
        self['ysrc'] = ysrc if ysrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'box'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='box', val='box'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
