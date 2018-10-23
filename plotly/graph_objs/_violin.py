from plotly.basedatatypes import BaseTraceType
import copy


class Violin(BaseTraceType):

    # bandwidth
    # ---------
    @property
    def bandwidth(self):
        """
        Sets the bandwidth used to compute the kernel density estimate.
        By default, the bandwidth is determined by Silverman's rule of
        thumb.
    
        The 'bandwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['bandwidth']

    @bandwidth.setter
    def bandwidth(self, val):
        self['bandwidth'] = val

    # box
    # ---
    @property
    def box(self):
        """
        The 'box' property is an instance of Box
        that may be specified as:
          - An instance of plotly.graph_objs.violin.Box
          - A dict of string/value properties that will be passed
            to the Box constructor
    
            Supported dict properties:
                
                fillcolor
                    Sets the inner box plot fill color.
                line
                    plotly.graph_objs.violin.box.Line instance or
                    dict with compatible properties
                visible
                    Determines if an miniature box plot is drawn
                    inside the violins.
                width
                    Sets the width of the inner box plots relative
                    to the violins' width. For example, with 1, the
                    inner box plots are as wide as the violins.

        Returns
        -------
        plotly.graph_objs.violin.Box
        """
        return self['box']

    @box.setter
    def box(self, val):
        self['box'] = val

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
          - An instance of plotly.graph_objs.violin.Hoverlabel
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
        plotly.graph_objs.violin.Hoverlabel
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
        Do the hover effects highlight individual violins or sample
        points or the kernel density estimate or any combination of
        them?
    
        The 'hoveron' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['violins', 'points', 'kde'] joined with '+' characters
            (e.g. 'violins+points')
            OR exactly one of ['all'] (e.g. 'all')

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
        the width of the violins.
    
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
          - An instance of plotly.graph_objs.violin.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the color of line bounding the violin(s).
                width
                    Sets the width (in px) of line bounding the
                    violin(s).

        Returns
        -------
        plotly.graph_objs.violin.Line
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
          - An instance of plotly.graph_objs.violin.Marker
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
                    plotly.graph_objs.violin.marker.Line instance
                    or dict with compatible properties
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
        plotly.graph_objs.violin.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # meanline
    # --------
    @property
    def meanline(self):
        """
        The 'meanline' property is an instance of Meanline
        that may be specified as:
          - An instance of plotly.graph_objs.violin.Meanline
          - A dict of string/value properties that will be passed
            to the Meanline constructor
    
            Supported dict properties:
                
                color
                    Sets the mean line color.
                visible
                    Determines if a line corresponding to the
                    sample's mean is shown inside the violins. If
                    `box.visible` is turned on, the mean line is
                    drawn inside the inner box. Otherwise, the mean
                    line is drawn from one side of the violin to
                    other.
                width
                    Sets the mean line width.

        Returns
        -------
        plotly.graph_objs.violin.Meanline
        """
        return self['meanline']

    @meanline.setter
    def meanline(self, val):
        self['meanline'] = val

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
        Sets the orientation of the violin(s). If "v" ("h"), the
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
        violins. If 0, the sample points are places over the center of
        the violins. Positive (negative) values correspond to positions
        to the right (left) for vertical violins and above (below) for
        horizontal violins.
    
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

    # points
    # ------
    @property
    def points(self):
        """
        If "outliers", only the sample points lying outside the
        whiskers are shown If "suspectedoutliers", the outlier points
        are shown and points either less than 4*Q1-3*Q3 or greater than
        4*Q3-3*Q1 are highlighted (see `outliercolor`) If "all", all
        sample points are shown If False, only the violins are shown
        with no sample points
    
        The 'points' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'outliers', 'suspectedoutliers', False]

        Returns
        -------
        Any
        """
        return self['points']

    @points.setter
    def points(self, val):
        self['points'] = val

    # scalegroup
    # ----------
    @property
    def scalegroup(self):
        """
        If there are multiple violins that should be sized according to
        to some metric (see `scalemode`), link them by providing a non-
        empty group id here shared by every trace in the same group.
    
        The 'scalegroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['scalegroup']

    @scalegroup.setter
    def scalegroup(self, val):
        self['scalegroup'] = val

    # scalemode
    # ---------
    @property
    def scalemode(self):
        """
        Sets the metric by which the width of each violin is
        determined."width" means each violin has the same (max)
        width*count* means the violins are scaled by the number of
        sample points makingup each violin.
    
        The 'scalemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['width', 'count']

        Returns
        -------
        Any
        """
        return self['scalemode']

    @scalemode.setter
    def scalemode(self, val):
        self['scalemode'] = val

    # selected
    # --------
    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of plotly.graph_objs.violin.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.violin.selected.Marker
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.violin.Selected
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

    # side
    # ----
    @property
    def side(self):
        """
        Determines on which side of the position value the density
        function making up one half of a violin is plotted. Useful when
        comparing two violin traces under "overlay" mode, where one
        trace has `side` set to "positive" and the other to "negative".
    
        The 'side' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['both', 'positive', 'negative']

        Returns
        -------
        Any
        """
        return self['side']

    @side.setter
    def side(self, val):
        self['side'] = val

    # span
    # ----
    @property
    def span(self):
        """
        Sets the span in data space for which the density function will
        be computed. Has an effect only when `spanmode` is set to
        "manual".
    
        The 'span' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'span[0]' property accepts values of any type
    (1) The 'span[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self['span']

    @span.setter
    def span(self, val):
        self['span'] = val

    # spanmode
    # --------
    @property
    def spanmode(self):
        """
        Sets the method by which the span in data space where the
        density function will be computed. "soft" means the span goes
        from the sample's minimum value minus two bandwidths to the
        sample's maximum value plus two bandwidths. "hard" means the
        span goes from the sample's minimum to its maximum value. For
        custom span settings, use mode "manual" and fill in the `span`
        attribute.
    
        The 'spanmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['soft', 'hard', 'manual']

        Returns
        -------
        Any
        """
        return self['spanmode']

    @spanmode.setter
    def spanmode(self, val):
        self['spanmode'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.violin.Stream
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
        plotly.graph_objs.violin.Stream
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
          - An instance of plotly.graph_objs.violin.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.violin.unselected.Marker
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.violin.Unselected
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
        bandwidth
            Sets the bandwidth used to compute the kernel density
            estimate. By default, the bandwidth is determined by
            Silverman's rule of thumb.
        box
            plotly.graph_objs.violin.Box instance or dict with
            compatible properties
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
            plotly.graph_objs.violin.Hoverlabel instance or dict
            with compatible properties
        hoveron
            Do the hover effects highlight individual violins or
            sample points or the kernel density estimate or any
            combination of them?
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
            jitter of width equal to the width of the violins.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.violin.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.violin.Marker instance or dict with
            compatible properties
        meanline
            plotly.graph_objs.violin.Meanline instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For box traces, the name will
            also be used for the position coordinate, if `x` and
            `x0` (`y` and `y0` if horizontal) are missing and the
            position axis is categorical
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the violin(s). If "v" ("h"),
            the distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the violins. If 0, the sample points are places over
            the center of the violins. Positive (negative) values
            correspond to positions to the right (left) for
            vertical violins and above (below) for horizontal
            violins.
        points
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the violins are shown with no sample
            points
        scalegroup
            If there are multiple violins that should be sized
            according to to some metric (see `scalemode`), link
            them by providing a non-empty group id here shared by
            every trace in the same group.
        scalemode
            Sets the metric by which the width of each violin is
            determined."width" means each violin has the same (max)
            width*count* means the violins are scaled by the number
            of sample points makingup each violin.
        selected
            plotly.graph_objs.violin.Selected instance or dict with
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
        side
            Determines on which side of the position value the
            density function making up one half of a violin is
            plotted. Useful when comparing two violin traces under
            "overlay" mode, where one trace has `side` set to
            "positive" and the other to "negative".
        span
            Sets the span in data space for which the density
            function will be computed. Has an effect only when
            `spanmode` is set to "manual".
        spanmode
            Sets the method by which the span in data space where
            the density function will be computed. "soft" means the
            span goes from the sample's minimum value minus two
            bandwidths to the sample's maximum value plus two
            bandwidths. "hard" means the span goes from the
            sample's minimum to its maximum value. For custom span
            settings, use mode "manual" and fill in the `span`
            attribute.
        stream
            plotly.graph_objs.violin.Stream instance or dict with
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
            plotly.graph_objs.violin.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
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
        ysrc
            Sets the source reference on plot.ly for  y .
        """

    def __init__(
        self,
        arg=None,
        bandwidth=None,
        box=None,
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
        meanline=None,
        name=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        points=None,
        scalegroup=None,
        scalemode=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        side=None,
        span=None,
        spanmode=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ysrc=None,
        **kwargs
    ):
        """
        Construct a new Violin object
        
        In vertical (horizontal) violin plots, statistics are computed
        using `y` (`x`) values. By supplying an `x` (`y`) array, one
        violin per distinct x (y) value is drawn If no `x` (`y`) list
        is provided, a single violin is drawn. That violin position is
        then positioned with with `name` or with `x0` (`y0`) if
        provided.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Violin
        bandwidth
            Sets the bandwidth used to compute the kernel density
            estimate. By default, the bandwidth is determined by
            Silverman's rule of thumb.
        box
            plotly.graph_objs.violin.Box instance or dict with
            compatible properties
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
            plotly.graph_objs.violin.Hoverlabel instance or dict
            with compatible properties
        hoveron
            Do the hover effects highlight individual violins or
            sample points or the kernel density estimate or any
            combination of them?
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
            jitter of width equal to the width of the violins.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.violin.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.violin.Marker instance or dict with
            compatible properties
        meanline
            plotly.graph_objs.violin.Meanline instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover. For box traces, the name will
            also be used for the position coordinate, if `x` and
            `x0` (`y` and `y0` if horizontal) are missing and the
            position axis is categorical
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the violin(s). If "v" ("h"),
            the distribution is visualized along the vertical
            (horizontal).
        pointpos
            Sets the position of the sample points in relation to
            the violins. If 0, the sample points are places over
            the center of the violins. Positive (negative) values
            correspond to positions to the right (left) for
            vertical violins and above (below) for horizontal
            violins.
        points
            If "outliers", only the sample points lying outside the
            whiskers are shown If "suspectedoutliers", the outlier
            points are shown and points either less than 4*Q1-3*Q3
            or greater than 4*Q3-3*Q1 are highlighted (see
            `outliercolor`) If "all", all sample points are shown
            If False, only the violins are shown with no sample
            points
        scalegroup
            If there are multiple violins that should be sized
            according to to some metric (see `scalemode`), link
            them by providing a non-empty group id here shared by
            every trace in the same group.
        scalemode
            Sets the metric by which the width of each violin is
            determined."width" means each violin has the same (max)
            width*count* means the violins are scaled by the number
            of sample points makingup each violin.
        selected
            plotly.graph_objs.violin.Selected instance or dict with
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
        side
            Determines on which side of the position value the
            density function making up one half of a violin is
            plotted. Useful when comparing two violin traces under
            "overlay" mode, where one trace has `side` set to
            "positive" and the other to "negative".
        span
            Sets the span in data space for which the density
            function will be computed. Has an effect only when
            `spanmode` is set to "manual".
        spanmode
            Sets the method by which the span in data space where
            the density function will be computed. "soft" means the
            span goes from the sample's minimum value minus two
            bandwidths to the sample's maximum value plus two
            bandwidths. "hard" means the span goes from the
            sample's minimum to its maximum value. For custom span
            settings, use mode "manual" and fill in the `span`
            attribute.
        stream
            plotly.graph_objs.violin.Stream instance or dict with
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
            plotly.graph_objs.violin.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
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
        ysrc
            Sets the source reference on plot.ly for  y .

        Returns
        -------
        Violin
        """
        super(Violin, self).__init__('violin')

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
The first argument to the plotly.graph_objs.Violin 
constructor must be a dict or 
an instance of plotly.graph_objs.Violin"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (violin as v_violin)

        # Initialize validators
        # ---------------------
        self._validators['bandwidth'] = v_violin.BandwidthValidator()
        self._validators['box'] = v_violin.BoxValidator()
        self._validators['customdata'] = v_violin.CustomdataValidator()
        self._validators['customdatasrc'] = v_violin.CustomdatasrcValidator()
        self._validators['fillcolor'] = v_violin.FillcolorValidator()
        self._validators['hoverinfo'] = v_violin.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_violin.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_violin.HoverlabelValidator()
        self._validators['hoveron'] = v_violin.HoveronValidator()
        self._validators['ids'] = v_violin.IdsValidator()
        self._validators['idssrc'] = v_violin.IdssrcValidator()
        self._validators['jitter'] = v_violin.JitterValidator()
        self._validators['legendgroup'] = v_violin.LegendgroupValidator()
        self._validators['line'] = v_violin.LineValidator()
        self._validators['marker'] = v_violin.MarkerValidator()
        self._validators['meanline'] = v_violin.MeanlineValidator()
        self._validators['name'] = v_violin.NameValidator()
        self._validators['opacity'] = v_violin.OpacityValidator()
        self._validators['orientation'] = v_violin.OrientationValidator()
        self._validators['pointpos'] = v_violin.PointposValidator()
        self._validators['points'] = v_violin.PointsValidator()
        self._validators['scalegroup'] = v_violin.ScalegroupValidator()
        self._validators['scalemode'] = v_violin.ScalemodeValidator()
        self._validators['selected'] = v_violin.SelectedValidator()
        self._validators['selectedpoints'] = v_violin.SelectedpointsValidator()
        self._validators['showlegend'] = v_violin.ShowlegendValidator()
        self._validators['side'] = v_violin.SideValidator()
        self._validators['span'] = v_violin.SpanValidator()
        self._validators['spanmode'] = v_violin.SpanmodeValidator()
        self._validators['stream'] = v_violin.StreamValidator()
        self._validators['text'] = v_violin.TextValidator()
        self._validators['textsrc'] = v_violin.TextsrcValidator()
        self._validators['uid'] = v_violin.UidValidator()
        self._validators['unselected'] = v_violin.UnselectedValidator()
        self._validators['visible'] = v_violin.VisibleValidator()
        self._validators['x'] = v_violin.XValidator()
        self._validators['x0'] = v_violin.X0Validator()
        self._validators['xaxis'] = v_violin.XAxisValidator()
        self._validators['xsrc'] = v_violin.XsrcValidator()
        self._validators['y'] = v_violin.YValidator()
        self._validators['y0'] = v_violin.Y0Validator()
        self._validators['yaxis'] = v_violin.YAxisValidator()
        self._validators['ysrc'] = v_violin.YsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('bandwidth', None)
        self['bandwidth'] = bandwidth if bandwidth is not None else _v
        _v = arg.pop('box', None)
        self['box'] = box if box is not None else _v
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
        _v = arg.pop('meanline', None)
        self['meanline'] = meanline if meanline is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('orientation', None)
        self['orientation'] = orientation if orientation is not None else _v
        _v = arg.pop('pointpos', None)
        self['pointpos'] = pointpos if pointpos is not None else _v
        _v = arg.pop('points', None)
        self['points'] = points if points is not None else _v
        _v = arg.pop('scalegroup', None)
        self['scalegroup'] = scalegroup if scalegroup is not None else _v
        _v = arg.pop('scalemode', None)
        self['scalemode'] = scalemode if scalemode is not None else _v
        _v = arg.pop('selected', None)
        self['selected'] = selected if selected is not None else _v
        _v = arg.pop('selectedpoints', None)
        self['selectedpoints'
            ] = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self['showlegend'] = showlegend if showlegend is not None else _v
        _v = arg.pop('side', None)
        self['side'] = side if side is not None else _v
        _v = arg.pop('span', None)
        self['span'] = span if span is not None else _v
        _v = arg.pop('spanmode', None)
        self['spanmode'] = spanmode if spanmode is not None else _v
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
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('x0', None)
        self['x0'] = x0 if x0 is not None else _v
        _v = arg.pop('xaxis', None)
        self['xaxis'] = xaxis if xaxis is not None else _v
        _v = arg.pop('xsrc', None)
        self['xsrc'] = xsrc if xsrc is not None else _v
        _v = arg.pop('y', None)
        self['y'] = y if y is not None else _v
        _v = arg.pop('y0', None)
        self['y0'] = y0 if y0 is not None else _v
        _v = arg.pop('yaxis', None)
        self['yaxis'] = yaxis if yaxis is not None else _v
        _v = arg.pop('ysrc', None)
        self['ysrc'] = ysrc if ysrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'violin'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='violin', val='violin'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
