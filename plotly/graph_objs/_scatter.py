from plotly.basedatatypes import BaseTraceType
import copy


class Scatter(BaseTraceType):

    # cliponaxis
    # ----------
    @property
    def cliponaxis(self):
        """
        Determines whether or not markers and text nodes are clipped
        about the subplot axes. To show markers and text nodes above
        axis lines and tick labels, make sure to set `xaxis.layer` and
        `yaxis.layer` to *below traces*.
    
        The 'cliponaxis' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['cliponaxis']

    @cliponaxis.setter
    def cliponaxis(self, val):
        self['cliponaxis'] = val

    # connectgaps
    # -----------
    @property
    def connectgaps(self):
        """
        Determines whether or not gaps (i.e. {nan} or missing values)
        in the provided data arrays are connected.
    
        The 'connectgaps' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['connectgaps']

    @connectgaps.setter
    def connectgaps(self, val):
        self['connectgaps'] = val

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

    # dx
    # --
    @property
    def dx(self):
        """
        Sets the x coordinate step. See `x0` for more info.
    
        The 'dx' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dx']

    @dx.setter
    def dx(self, val):
        self['dx'] = val

    # dy
    # --
    @property
    def dy(self):
        """
        Sets the y coordinate step. See `y0` for more info.
    
        The 'dy' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dy']

    @dy.setter
    def dy(self, val):
        self['dy'] = val

    # error_x
    # -------
    @property
    def error_x(self):
        """
        The 'error_x' property is an instance of ErrorX
        that may be specified as:
          - An instance of plotly.graph_objs.scatter.ErrorX
          - A dict of string/value properties that will be passed
            to the ErrorX constructor
    
            Supported dict properties:
                
                array
                    Sets the data corresponding the length of each
                    error bar. Values are plotted relative to the
                    underlying data.
                arrayminus
                    Sets the data corresponding the length of each
                    error bar in the bottom (left) direction for
                    vertical (horizontal) bars Values are plotted
                    relative to the underlying data.
                arrayminussrc
                    Sets the source reference on plot.ly for
                    arrayminus .
                arraysrc
                    Sets the source reference on plot.ly for  array
                    .
                color
                    Sets the stoke color of the error bars.
                copy_ystyle
    
                symmetric
                    Determines whether or not the error bars have
                    the same length in both direction (top/bottom
                    for vertical bars, left/right for horizontal
                    bars.
                thickness
                    Sets the thickness (in px) of the error bars.
                traceref
    
                tracerefminus
    
                type
                    Determines the rule used to generate the error
                    bars. If *constant`, the bar lengths are of a
                    constant value. Set this constant in `value`.
                    If "percent", the bar lengths correspond to a
                    percentage of underlying data. Set this
                    percentage in `value`. If "sqrt", the bar
                    lengths correspond to the sqaure of the
                    underlying data. If "array", the bar lengths
                    are set with data set `array`.
                value
                    Sets the value of either the percentage (if
                    `type` is set to "percent") or the constant (if
                    `type` is set to "constant") corresponding to
                    the lengths of the error bars.
                valueminus
                    Sets the value of either the percentage (if
                    `type` is set to "percent") or the constant (if
                    `type` is set to "constant") corresponding to
                    the lengths of the error bars in the bottom
                    (left) direction for vertical (horizontal) bars
                visible
                    Determines whether or not this set of error
                    bars is visible.
                width
                    Sets the width (in px) of the cross-bar at both
                    ends of the error bars.

        Returns
        -------
        plotly.graph_objs.scatter.ErrorX
        """
        return self['error_x']

    @error_x.setter
    def error_x(self, val):
        self['error_x'] = val

    # error_y
    # -------
    @property
    def error_y(self):
        """
        The 'error_y' property is an instance of ErrorY
        that may be specified as:
          - An instance of plotly.graph_objs.scatter.ErrorY
          - A dict of string/value properties that will be passed
            to the ErrorY constructor
    
            Supported dict properties:
                
                array
                    Sets the data corresponding the length of each
                    error bar. Values are plotted relative to the
                    underlying data.
                arrayminus
                    Sets the data corresponding the length of each
                    error bar in the bottom (left) direction for
                    vertical (horizontal) bars Values are plotted
                    relative to the underlying data.
                arrayminussrc
                    Sets the source reference on plot.ly for
                    arrayminus .
                arraysrc
                    Sets the source reference on plot.ly for  array
                    .
                color
                    Sets the stoke color of the error bars.
                symmetric
                    Determines whether or not the error bars have
                    the same length in both direction (top/bottom
                    for vertical bars, left/right for horizontal
                    bars.
                thickness
                    Sets the thickness (in px) of the error bars.
                traceref
    
                tracerefminus
    
                type
                    Determines the rule used to generate the error
                    bars. If *constant`, the bar lengths are of a
                    constant value. Set this constant in `value`.
                    If "percent", the bar lengths correspond to a
                    percentage of underlying data. Set this
                    percentage in `value`. If "sqrt", the bar
                    lengths correspond to the sqaure of the
                    underlying data. If "array", the bar lengths
                    are set with data set `array`.
                value
                    Sets the value of either the percentage (if
                    `type` is set to "percent") or the constant (if
                    `type` is set to "constant") corresponding to
                    the lengths of the error bars.
                valueminus
                    Sets the value of either the percentage (if
                    `type` is set to "percent") or the constant (if
                    `type` is set to "constant") corresponding to
                    the lengths of the error bars in the bottom
                    (left) direction for vertical (horizontal) bars
                visible
                    Determines whether or not this set of error
                    bars is visible.
                width
                    Sets the width (in px) of the cross-bar at both
                    ends of the error bars.

        Returns
        -------
        plotly.graph_objs.scatter.ErrorY
        """
        return self['error_y']

    @error_y.setter
    def error_y(self, val):
        self['error_y'] = val

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the area to fill with a solid color. Use with `fillcolor`
        if not "none". "tozerox" and "tozeroy" fill to x=0 and y=0
        respectively. "tonextx" and "tonexty" fill between the
        endpoints of this trace and the endpoints of the trace before
        it, connecting those endpoints with straight lines (to make a
        stacked area graph); if there is no trace before it, they
        behave like "tozerox" and "tozeroy". "toself" connects the
        endpoints of the trace (or each segment of the trace if it has
        gaps) into a closed shape. "tonext" fills the space between two
        traces if one completely encloses the other (eg consecutive
        contour lines), and behaves like "toself" if there is no trace
        before it. "tonext" should not be used if one trace does not
        enclose the other.
    
        The 'fill' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'tozeroy', 'tozerox', 'tonexty', 'tonextx',
                'toself', 'tonext']

        Returns
        -------
        Any
        """
        return self['fill']

    @fill.setter
    def fill(self, val):
        self['fill'] = val

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
          - An instance of plotly.graph_objs.scatter.Hoverlabel
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
        plotly.graph_objs.scatter.Hoverlabel
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
        Do the hover effects highlight individual points (markers or
        line points) or do they highlight filled regions? If the fill
        is "toself" or "tonext" and there are no markers or text, then
        the default is "fills", otherwise it is "points".
    
        The 'hoveron' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['points', 'fills'] joined with '+' characters
            (e.g. 'points+fills')

        Returns
        -------
        Any
        """
        return self['hoveron']

    @hoveron.setter
    def hoveron(self, val):
        self['hoveron'] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Sets hover text elements associated with each (x,y) pair. If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (x,y) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.
    
        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['hovertext']

    @hovertext.setter
    def hovertext(self, val):
        self['hovertext'] = val

    # hovertextsrc
    # ------------
    @property
    def hovertextsrc(self):
        """
        Sets the source reference on plot.ly for  hovertext .
    
        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hovertextsrc']

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self['hovertextsrc'] = val

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

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.scatter.Line
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
                shape
                    Determines the line shape. With "spline" the
                    lines are drawn using spline interpolation. The
                    other available values correspond to step-wise
                    line shapes.
                simplify
                    Simplifies lines by removing nearly-collinear
                    points. When transitioning lines, it may be
                    desirable to disable this so that the number of
                    points along the resulting SVG path is
                    unaffected.
                smoothing
                    Has an effect only if `shape` is set to
                    "spline" Sets the amount of smoothing. 0
                    corresponds to no smoothing (equivalent to a
                    "linear" shape).
                width
                    Sets the line width (in px).

        Returns
        -------
        plotly.graph_objs.scatter.Line
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
          - An instance of plotly.graph_objs.scatter.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                autocolorscale
                    Determines whether the colorscale is a default
                    palette (`autocolorscale: true`) or the palette
                    determined by `marker.colorscale`. Has an
                    effect only if in `marker.color`is set to a
                    numerical array. In case `colorscale` is
                    unspecified or `autocolorscale` is true, the
                    default  palette will be chosen according to
                    whether numbers in the `color` array are all
                    positive, all negative or mixed.
                cauto
                    Determines whether or not the color domain is
                    computed with respect to the input data (here
                    in `marker.color`) or the bounds set in
                    `marker.cmin` and `marker.cmax`  Has an effect
                    only if in `marker.color`is set to a numerical
                    array. Defaults to `false` when `marker.cmin`
                    and `marker.cmax` are set by the user.
                cmax
                    Sets the upper bound of the color domain. Has
                    an effect only if in `marker.color`is set to a
                    numerical array. Value should have the same
                    units as in `marker.color` and if set,
                    `marker.cmin` must be set as well.
                cmin
                    Sets the lower bound of the color domain. Has
                    an effect only if in `marker.color`is set to a
                    numerical array. Value should have the same
                    units as in `marker.color` and if set,
                    `marker.cmax` must be set as well.
                color
                    Sets themarkercolor. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `marker.cmin` and `marker.cmax` if set.
                colorbar
                    plotly.graph_objs.scatter.marker.ColorBar
                    instance or dict with compatible properties
                colorscale
                    Sets the colorscale. Has an effect only if in
                    `marker.color`is set to a numerical array. The
                    colorscale must be an array containing arrays
                    mapping a normalized value to an rgb, rgba,
                    hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                    control the bounds of the colorscale in color
                    space, use`marker.cmin` and `marker.cmax`.
                    Alternatively, `colorscale` may be a palette
                    name string of the following list: Greys,YlGnBu
                    ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,R
                    ainbow,Portland,Jet,Hot,Blackbody,Earth,Electri
                    c,Viridis,Cividis.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                gradient
                    plotly.graph_objs.scatter.marker.Gradient
                    instance or dict with compatible properties
                line
                    plotly.graph_objs.scatter.marker.Line instance
                    or dict with compatible properties
                maxdisplayed
                    Sets a maximum number of points to be drawn on
                    the graph. 0 corresponds to no limit.
                opacity
                    Sets the marker opacity.
                opacitysrc
                    Sets the source reference on plot.ly for
                    opacity .
                reversescale
                    Reverses the color mapping if true. Has an
                    effect only if in `marker.color`is set to a
                    numerical array. If true, `marker.cmin` will
                    correspond to the last color in the array and
                    `marker.cmax` will correspond to the first
                    color.
                showscale
                    Determines whether or not a colorbar is
                    displayed for this trace. Has an effect only if
                    in `marker.color`is set to a numerical array.
                size
                    Sets the marker size (in px).
                sizemin
                    Has an effect only if `marker.size` is set to a
                    numerical array. Sets the minimum size (in px)
                    of the rendered marker points.
                sizemode
                    Has an effect only if `marker.size` is set to a
                    numerical array. Sets the rule for which the
                    data in `size` is converted to pixels.
                sizeref
                    Has an effect only if `marker.size` is set to a
                    numerical array. Sets the scale factor used to
                    determine the rendered size of marker points.
                    Use with `sizemin` and `sizemode`.
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .
                symbol
                    Sets the marker symbol type. Adding 100 is
                    equivalent to appending "-open" to a symbol
                    name. Adding 200 is equivalent to appending
                    "-dot" to a symbol name. Adding 300 is
                    equivalent to appending "-open-dot" or "dot-
                    open" to a symbol name.
                symbolsrc
                    Sets the source reference on plot.ly for
                    symbol .

        Returns
        -------
        plotly.graph_objs.scatter.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # mode
    # ----
    @property
    def mode(self):
        """
        Determines the drawing mode for this scatter trace. If the
        provided `mode` includes "text" then the `text` elements appear
        at the coordinates. Otherwise, the `text` elements appear on
        hover. If there are less than 20 points, then the default is
        "lines+markers". Otherwise, "lines".
    
        The 'mode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['lines', 'markers', 'text'] joined with '+' characters
            (e.g. 'lines+markers')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self['mode']

    @mode.setter
    def mode(self, val):
        self['mode'] = val

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

    # r
    # -
    @property
    def r(self):
        """
        For legacy polar chart only.Please switch to "scatterpolar"
        trace type.Sets the radial coordinates.
    
        The 'r' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['r']

    @r.setter
    def r(self, val):
        self['r'] = val

    # rsrc
    # ----
    @property
    def rsrc(self):
        """
        Sets the source reference on plot.ly for  r .
    
        The 'rsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['rsrc']

    @rsrc.setter
    def rsrc(self, val):
        self['rsrc'] = val

    # selected
    # --------
    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of plotly.graph_objs.scatter.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.scatter.selected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.scatter.selected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.scatter.Selected
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
          - An instance of plotly.graph_objs.scatter.Stream
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
        plotly.graph_objs.scatter.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # t
    # -
    @property
    def t(self):
        """
        For legacy polar chart only.Please switch to "scatterpolar"
        trace type.Sets the angular coordinates.
    
        The 't' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['t']

    @t.setter
    def t(self, val):
        self['t'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets text elements associated with each (x,y) pair. If a single
        string, the same string appears over all the data points. If an
        array of string, the items are mapped in order to the this
        trace's (x,y) coordinates. If trace `hoverinfo` contains a
        "text" flag and "hovertext" is not set, these elements will be
        seen in the hover labels.
    
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

    # textfont
    # --------
    @property
    def textfont(self):
        """
        Sets the text font.
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.scatter.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
            Supported dict properties:
                
                color
    
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
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
                familysrc
                    Sets the source reference on plot.ly for
                    family .
                size
    
                sizesrc
                    Sets the source reference on plot.ly for  size
                    .

        Returns
        -------
        plotly.graph_objs.scatter.Textfont
        """
        return self['textfont']

    @textfont.setter
    def textfont(self, val):
        self['textfont'] = val

    # textposition
    # ------------
    @property
    def textposition(self):
        """
        Sets the positions of the `text` elements with respects to the
        (x,y) coordinates.
    
        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['textposition']

    @textposition.setter
    def textposition(self, val):
        self['textposition'] = val

    # textpositionsrc
    # ---------------
    @property
    def textpositionsrc(self):
        """
        Sets the source reference on plot.ly for  textposition .
    
        The 'textpositionsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['textpositionsrc']

    @textpositionsrc.setter
    def textpositionsrc(self, val):
        self['textpositionsrc'] = val

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

    # tsrc
    # ----
    @property
    def tsrc(self):
        """
        Sets the source reference on plot.ly for  t .
    
        The 'tsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['tsrc']

    @tsrc.setter
    def tsrc(self, val):
        self['tsrc'] = val

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
          - An instance of plotly.graph_objs.scatter.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.scatter.unselected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.scatter.unselected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.scatter.Unselected
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
        Sets the x coordinates.
    
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
        Alternate to `x`. Builds a linear space of x coordinates. Use
        with `dx` where `x0` is the starting coordinate and `dx` the
        step.
    
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
        Sets the y coordinates.
    
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
        Alternate to `y`. Builds a linear space of y coordinates. Use
        with `dy` where `y0` is the starting coordinate and `dy` the
        step.
    
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
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            plotly.graph_objs.scatter.ErrorX instance or dict with
            compatible properties
        error_y
            plotly.graph_objs.scatter.ErrorY instance or dict with
            compatible properties
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". "tozerox" and "tozeroy" fill
            to x=0 and y=0 respectively. "tonextx" and "tonexty"
            fill between the endpoints of this trace and the
            endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other.
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
            plotly.graph_objs.scatter.Hoverlabel instance or dict
            with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
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
        line
            plotly.graph_objs.scatter.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.scatter.Marker instance or dict with
            compatible properties
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points, then the default is "lines+markers".
            Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            For legacy polar chart only.Please switch to
            "scatterpolar" trace type.Sets the radial coordinates.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.scatter.Selected instance or dict
            with compatible properties
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
            plotly.graph_objs.scatter.Stream instance or dict with
            compatible properties
        t
            For legacy polar chart only.Please switch to
            "scatterpolar" trace type.Sets the angular coordinates.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        tsrc
            Sets the source reference on plot.ly for  t .
        uid

        unselected
            plotly.graph_objs.scatter.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
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
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
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
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        line=None,
        marker=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        t=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        tsrc=None,
        uid=None,
        unselected=None,
        visible=None,
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
        Construct a new Scatter object
        
        The scatter trace type encompasses line charts, scatter charts,
        text charts, and bubble charts. The data visualized as scatter
        point or lines is set in `x` and `y`. Text (appearing either on
        the chart or on hover only) is via `text`. Bubble charts are
        achieved by setting `marker.size` and/or `marker.color` to
        numerical arrays.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Scatter
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            plotly.graph_objs.scatter.ErrorX instance or dict with
            compatible properties
        error_y
            plotly.graph_objs.scatter.ErrorY instance or dict with
            compatible properties
        fill
            Sets the area to fill with a solid color. Use with
            `fillcolor` if not "none". "tozerox" and "tozeroy" fill
            to x=0 and y=0 respectively. "tonextx" and "tonexty"
            fill between the endpoints of this trace and the
            endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other.
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
            plotly.graph_objs.scatter.Hoverlabel instance or dict
            with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
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
        line
            plotly.graph_objs.scatter.Line instance or dict with
            compatible properties
        marker
            plotly.graph_objs.scatter.Marker instance or dict with
            compatible properties
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points, then the default is "lines+markers".
            Otherwise, "lines".
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        r
            For legacy polar chart only.Please switch to
            "scatterpolar" trace type.Sets the radial coordinates.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.scatter.Selected instance or dict
            with compatible properties
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
            plotly.graph_objs.scatter.Stream instance or dict with
            compatible properties
        t
            For legacy polar chart only.Please switch to
            "scatterpolar" trace type.Sets the angular coordinates.
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        tsrc
            Sets the source reference on plot.ly for  t .
        uid

        unselected
            plotly.graph_objs.scatter.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
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
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
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
        Scatter
        """
        super(Scatter, self).__init__('scatter')

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
The first argument to the plotly.graph_objs.Scatter 
constructor must be a dict or 
an instance of plotly.graph_objs.Scatter"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (scatter as v_scatter)

        # Initialize validators
        # ---------------------
        self._validators['cliponaxis'] = v_scatter.CliponaxisValidator()
        self._validators['connectgaps'] = v_scatter.ConnectgapsValidator()
        self._validators['customdata'] = v_scatter.CustomdataValidator()
        self._validators['customdatasrc'] = v_scatter.CustomdatasrcValidator()
        self._validators['dx'] = v_scatter.DxValidator()
        self._validators['dy'] = v_scatter.DyValidator()
        self._validators['error_x'] = v_scatter.ErrorXValidator()
        self._validators['error_y'] = v_scatter.ErrorYValidator()
        self._validators['fill'] = v_scatter.FillValidator()
        self._validators['fillcolor'] = v_scatter.FillcolorValidator()
        self._validators['hoverinfo'] = v_scatter.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_scatter.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_scatter.HoverlabelValidator()
        self._validators['hoveron'] = v_scatter.HoveronValidator()
        self._validators['hovertext'] = v_scatter.HovertextValidator()
        self._validators['hovertextsrc'] = v_scatter.HovertextsrcValidator()
        self._validators['ids'] = v_scatter.IdsValidator()
        self._validators['idssrc'] = v_scatter.IdssrcValidator()
        self._validators['legendgroup'] = v_scatter.LegendgroupValidator()
        self._validators['line'] = v_scatter.LineValidator()
        self._validators['marker'] = v_scatter.MarkerValidator()
        self._validators['mode'] = v_scatter.ModeValidator()
        self._validators['name'] = v_scatter.NameValidator()
        self._validators['opacity'] = v_scatter.OpacityValidator()
        self._validators['r'] = v_scatter.RValidator()
        self._validators['rsrc'] = v_scatter.RsrcValidator()
        self._validators['selected'] = v_scatter.SelectedValidator()
        self._validators['selectedpoints'
                        ] = v_scatter.SelectedpointsValidator()
        self._validators['showlegend'] = v_scatter.ShowlegendValidator()
        self._validators['stream'] = v_scatter.StreamValidator()
        self._validators['t'] = v_scatter.TValidator()
        self._validators['text'] = v_scatter.TextValidator()
        self._validators['textfont'] = v_scatter.TextfontValidator()
        self._validators['textposition'] = v_scatter.TextpositionValidator()
        self._validators['textpositionsrc'
                        ] = v_scatter.TextpositionsrcValidator()
        self._validators['textsrc'] = v_scatter.TextsrcValidator()
        self._validators['tsrc'] = v_scatter.TsrcValidator()
        self._validators['uid'] = v_scatter.UidValidator()
        self._validators['unselected'] = v_scatter.UnselectedValidator()
        self._validators['visible'] = v_scatter.VisibleValidator()
        self._validators['x'] = v_scatter.XValidator()
        self._validators['x0'] = v_scatter.X0Validator()
        self._validators['xaxis'] = v_scatter.XAxisValidator()
        self._validators['xcalendar'] = v_scatter.XcalendarValidator()
        self._validators['xsrc'] = v_scatter.XsrcValidator()
        self._validators['y'] = v_scatter.YValidator()
        self._validators['y0'] = v_scatter.Y0Validator()
        self._validators['yaxis'] = v_scatter.YAxisValidator()
        self._validators['ycalendar'] = v_scatter.YcalendarValidator()
        self._validators['ysrc'] = v_scatter.YsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('cliponaxis', None)
        self.cliponaxis = cliponaxis if cliponaxis is not None else _v
        _v = arg.pop('connectgaps', None)
        self.connectgaps = connectgaps if connectgaps is not None else _v
        _v = arg.pop('customdata', None)
        self.customdata = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self.customdatasrc = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('dx', None)
        self.dx = dx if dx is not None else _v
        _v = arg.pop('dy', None)
        self.dy = dy if dy is not None else _v
        _v = arg.pop('error_x', None)
        self.error_x = error_x if error_x is not None else _v
        _v = arg.pop('error_y', None)
        self.error_y = error_y if error_y is not None else _v
        _v = arg.pop('fill', None)
        self.fill = fill if fill is not None else _v
        _v = arg.pop('fillcolor', None)
        self.fillcolor = fillcolor if fillcolor is not None else _v
        _v = arg.pop('hoverinfo', None)
        self.hoverinfo = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoverinfosrc', None)
        self.hoverinfosrc = hoverinfosrc if hoverinfosrc is not None else _v
        _v = arg.pop('hoverlabel', None)
        self.hoverlabel = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('hoveron', None)
        self.hoveron = hoveron if hoveron is not None else _v
        _v = arg.pop('hovertext', None)
        self.hovertext = hovertext if hovertext is not None else _v
        _v = arg.pop('hovertextsrc', None)
        self.hovertextsrc = hovertextsrc if hovertextsrc is not None else _v
        _v = arg.pop('ids', None)
        self.ids = ids if ids is not None else _v
        _v = arg.pop('idssrc', None)
        self.idssrc = idssrc if idssrc is not None else _v
        _v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup if legendgroup is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('marker', None)
        self.marker = marker if marker is not None else _v
        _v = arg.pop('mode', None)
        self.mode = mode if mode is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('r', None)
        self.r = r if r is not None else _v
        _v = arg.pop('rsrc', None)
        self.rsrc = rsrc if rsrc is not None else _v
        _v = arg.pop('selected', None)
        self.selected = selected if selected is not None else _v
        _v = arg.pop('selectedpoints', None)
        self.selectedpoints = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self.showlegend = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self.stream = stream if stream is not None else _v
        _v = arg.pop('t', None)
        self.t = t if t is not None else _v
        _v = arg.pop('text', None)
        self.text = text if text is not None else _v
        _v = arg.pop('textfont', None)
        self.textfont = textfont if textfont is not None else _v
        _v = arg.pop('textposition', None)
        self.textposition = textposition if textposition is not None else _v
        _v = arg.pop('textpositionsrc', None)
        self.textpositionsrc = textpositionsrc if textpositionsrc is not None else _v
        _v = arg.pop('textsrc', None)
        self.textsrc = textsrc if textsrc is not None else _v
        _v = arg.pop('tsrc', None)
        self.tsrc = tsrc if tsrc is not None else _v
        _v = arg.pop('uid', None)
        self.uid = uid if uid is not None else _v
        _v = arg.pop('unselected', None)
        self.unselected = unselected if unselected is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v
        _v = arg.pop('x', None)
        self.x = x if x is not None else _v
        _v = arg.pop('x0', None)
        self.x0 = x0 if x0 is not None else _v
        _v = arg.pop('xaxis', None)
        self.xaxis = xaxis if xaxis is not None else _v
        _v = arg.pop('xcalendar', None)
        self.xcalendar = xcalendar if xcalendar is not None else _v
        _v = arg.pop('xsrc', None)
        self.xsrc = xsrc if xsrc is not None else _v
        _v = arg.pop('y', None)
        self.y = y if y is not None else _v
        _v = arg.pop('y0', None)
        self.y0 = y0 if y0 is not None else _v
        _v = arg.pop('yaxis', None)
        self.yaxis = yaxis if yaxis is not None else _v
        _v = arg.pop('ycalendar', None)
        self.ycalendar = ycalendar if ycalendar is not None else _v
        _v = arg.pop('ysrc', None)
        self.ysrc = ysrc if ysrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'scatter'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='scatter', val='scatter'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
