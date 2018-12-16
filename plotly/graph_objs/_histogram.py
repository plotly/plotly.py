from plotly.basedatatypes import BaseTraceType
import copy


class Histogram(BaseTraceType):

    # autobinx
    # --------
    @property
    def autobinx(self):
        """
        Obsolete: since v1.42 each bin attribute is auto-determined
        separately and `autobinx` is not needed. However, we accept
        `autobinx: true` or `false` and will update `xbins` accordingly
        before deleting `autobinx` from the trace.
    
        The 'autobinx' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autobinx']

    @autobinx.setter
    def autobinx(self, val):
        self['autobinx'] = val

    # autobiny
    # --------
    @property
    def autobiny(self):
        """
        Obsolete: since v1.42 each bin attribute is auto-determined
        separately and `autobiny` is not needed. However, we accept
        `autobiny: true` or `false` and will update `ybins` accordingly
        before deleting `autobiny` from the trace.
    
        The 'autobiny' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autobiny']

    @autobiny.setter
    def autobiny(self, val):
        self['autobiny'] = val

    # cumulative
    # ----------
    @property
    def cumulative(self):
        """
        The 'cumulative' property is an instance of Cumulative
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.Cumulative
          - A dict of string/value properties that will be passed
            to the Cumulative constructor
    
            Supported dict properties:
                
                currentbin
                    Only applies if cumulative is enabled. Sets
                    whether the current bin is included, excluded,
                    or has half of its value included in the
                    current cumulative value. "include" is the
                    default for compatibility with various other
                    tools, however it introduces a half-bin bias to
                    the results. "exclude" makes the opposite half-
                    bin bias, and "half" removes it.
                direction
                    Only applies if cumulative is enabled. If
                    "increasing" (default) we sum all prior bins,
                    so the result increases from left to right. If
                    "decreasing" we sum later bins so the result
                    decreases from left to right.
                enabled
                    If true, display the cumulative distribution by
                    summing the binned values. Use the `direction`
                    and `centralbin` attributes to tune the
                    accumulation method. Note: in this mode, the
                    "density" `histnorm` settings behave the same
                    as their equivalents without "density": "" and
                    "density" both rise to the number of data
                    points, and "probability" and *probability
                    density* both rise to the number of sample
                    points.

        Returns
        -------
        plotly.graph_objs.histogram.Cumulative
        """
        return self['cumulative']

    @cumulative.setter
    def cumulative(self, val):
        self['cumulative'] = val

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

    # error_x
    # -------
    @property
    def error_x(self):
        """
        The 'error_x' property is an instance of ErrorX
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.ErrorX
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
        plotly.graph_objs.histogram.ErrorX
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
          - An instance of plotly.graph_objs.histogram.ErrorY
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
        plotly.graph_objs.histogram.ErrorY
        """
        return self['error_y']

    @error_y.setter
    def error_y(self, val):
        self['error_y'] = val

    # histfunc
    # --------
    @property
    def histfunc(self):
        """
        Specifies the binning function used for this histogram trace.
        If "count", the histogram values are computed by counting the
        number of values lying inside each bin. If "sum", "avg", "min",
        "max", the histogram values are computed using the sum, the
        average, the minimum or the maximum of the values lying inside
        each bin respectively.
    
        The 'histfunc' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['count', 'sum', 'avg', 'min', 'max']

        Returns
        -------
        Any
        """
        return self['histfunc']

    @histfunc.setter
    def histfunc(self, val):
        self['histfunc'] = val

    # histnorm
    # --------
    @property
    def histnorm(self):
        """
        Specifies the type of normalization used for this histogram
        trace. If "", the span of each bar corresponds to the number of
        occurrences (i.e. the number of data points lying inside the
        bins). If "percent" / "probability", the span of each bar
        corresponds to the percentage / fraction of occurrences with
        respect to the total number of sample points (here, the sum of
        all bin HEIGHTS equals 100% / 1). If "density", the span of
        each bar corresponds to the number of occurrences in a bin
        divided by the size of the bin interval (here, the sum of all
        bin AREAS equals the total number of sample points). If
        *probability density*, the area of each bar corresponds to the
        probability that an event will fall into the corresponding bin
        (here, the sum of all bin AREAS equals 1).
    
        The 'histnorm' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['', 'percent', 'probability', 'density', 'probability
                density']

        Returns
        -------
        Any
        """
        return self['histnorm']

    @histnorm.setter
    def histnorm(self, val):
        self['histnorm'] = val

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
          - An instance of plotly.graph_objs.histogram.Hoverlabel
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
        plotly.graph_objs.histogram.Hoverlabel
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

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.Marker
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
                    plotly.graph_objs.histogram.marker.ColorBar
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
                line
                    plotly.graph_objs.histogram.marker.Line
                    instance or dict with compatible properties
                opacity
                    Sets the opacity of the bars.
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

        Returns
        -------
        plotly.graph_objs.histogram.Marker
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

    # nbinsx
    # ------
    @property
    def nbinsx(self):
        """
        Specifies the maximum number of desired bins. This value will
        be used in an algorithm that will decide the optimal bin size
        such that the histogram best visualizes the distribution of the
        data. Ignored if `xbins.size` is provided.
    
        The 'nbinsx' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['nbinsx']

    @nbinsx.setter
    def nbinsx(self, val):
        self['nbinsx'] = val

    # nbinsy
    # ------
    @property
    def nbinsy(self):
        """
        Specifies the maximum number of desired bins. This value will
        be used in an algorithm that will decide the optimal bin size
        such that the histogram best visualizes the distribution of the
        data. Ignored if `ybins.size` is provided.
    
        The 'nbinsy' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['nbinsy']

    @nbinsy.setter
    def nbinsy(self, val):
        self['nbinsy'] = val

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
        Sets the orientation of the bars. With "v" ("h"), the value of
        the each bar spans along the vertical (horizontal).
    
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

    # selected
    # --------
    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.histogram.selected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.histogram.selected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.histogram.Selected
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
          - An instance of plotly.graph_objs.histogram.Stream
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
        plotly.graph_objs.histogram.Stream
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
          - An instance of plotly.graph_objs.histogram.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.histogram.unselected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.histogram.unselected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.histogram.Unselected
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
        Sets the sample data to be binned on the x axis.
    
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

    # xbins
    # -----
    @property
    def xbins(self):
        """
        The 'xbins' property is an instance of XBins
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.XBins
          - A dict of string/value properties that will be passed
            to the XBins constructor
    
            Supported dict properties:
                
                end
                    Sets the end value for the x axis bins. The
                    last bin may not end exactly at this value, we
                    increment the bin edge by `size` from `start`
                    until we reach or exceed `end`. Defaults to the
                    maximum data value. Like `start`, for dates use
                    a date string, and for category data `end` is
                    based on the category serial numbers.
                size
                    Sets the size of each x axis bin. Default
                    behavior: If `nbinsx` is 0 or omitted, we
                    choose a nice round bin size such that the
                    number of bins is about the same as the typical
                    number of samples in each bin. If `nbinsx` is
                    provided, we choose a nice round bin size
                    giving no more than that many bins. For date
                    data, use milliseconds or "M<n>" for months, as
                    in `axis.dtick`. For category data, the number
                    of categories to bin together (always defaults
                    to 1). If multiple non-overlaying histograms
                    share a subplot, the first explicit `size` is
                    used and all others discarded. If no `size` is
                    provided,the sample data from all traces is
                    combined to determine `size` as described
                    above.
                start
                    Sets the starting value for the x axis bins.
                    Defaults to the minimum data value, shifted
                    down if necessary to make nice round values and
                    to remove ambiguous bin edges. For example, if
                    most of the data is integers we shift the bin
                    edges 0.5 down, so a `size` of 5 would have a
                    default `start` of -0.5, so it is clear that
                    0-4 are in the first bin, 5-9 in the second,
                    but continuous data gets a start of 0 and bins
                    [0,5), [5,10) etc. Dates behave similarly, and
                    `start` should be a date string. For category
                    data, `start` is based on the category serial
                    numbers, and defaults to -0.5. If multiple non-
                    overlaying histograms share a subplot, the
                    first explicit `start` is used exactly and all
                    others are shifted down (if necessary) to
                    differ from that one by an integer number of
                    bins.

        Returns
        -------
        plotly.graph_objs.histogram.XBins
        """
        return self['xbins']

    @xbins.setter
    def xbins(self, val):
        self['xbins'] = val

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
        Sets the sample data to be binned on the y axis.
    
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

    # ybins
    # -----
    @property
    def ybins(self):
        """
        The 'ybins' property is an instance of YBins
        that may be specified as:
          - An instance of plotly.graph_objs.histogram.YBins
          - A dict of string/value properties that will be passed
            to the YBins constructor
    
            Supported dict properties:
                
                end
                    Sets the end value for the y axis bins. The
                    last bin may not end exactly at this value, we
                    increment the bin edge by `size` from `start`
                    until we reach or exceed `end`. Defaults to the
                    maximum data value. Like `start`, for dates use
                    a date string, and for category data `end` is
                    based on the category serial numbers.
                size
                    Sets the size of each y axis bin. Default
                    behavior: If `nbinsy` is 0 or omitted, we
                    choose a nice round bin size such that the
                    number of bins is about the same as the typical
                    number of samples in each bin. If `nbinsy` is
                    provided, we choose a nice round bin size
                    giving no more than that many bins. For date
                    data, use milliseconds or "M<n>" for months, as
                    in `axis.dtick`. For category data, the number
                    of categories to bin together (always defaults
                    to 1). If multiple non-overlaying histograms
                    share a subplot, the first explicit `size` is
                    used and all others discarded. If no `size` is
                    provided,the sample data from all traces is
                    combined to determine `size` as described
                    above.
                start
                    Sets the starting value for the y axis bins.
                    Defaults to the minimum data value, shifted
                    down if necessary to make nice round values and
                    to remove ambiguous bin edges. For example, if
                    most of the data is integers we shift the bin
                    edges 0.5 down, so a `size` of 5 would have a
                    default `start` of -0.5, so it is clear that
                    0-4 are in the first bin, 5-9 in the second,
                    but continuous data gets a start of 0 and bins
                    [0,5), [5,10) etc. Dates behave similarly, and
                    `start` should be a date string. For category
                    data, `start` is based on the category serial
                    numbers, and defaults to -0.5. If multiple non-
                    overlaying histograms share a subplot, the
                    first explicit `start` is used exactly and all
                    others are shifted down (if necessary) to
                    differ from that one by an integer number of
                    bins.

        Returns
        -------
        plotly.graph_objs.histogram.YBins
        """
        return self['ybins']

    @ybins.setter
    def ybins(self, val):
        self['ybins'] = val

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
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        cumulative
            plotly.graph_objs.histogram.Cumulative instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        error_x
            plotly.graph_objs.histogram.ErrorX instance or dict
            with compatible properties
        error_y
            plotly.graph_objs.histogram.ErrorY instance or dict
            with compatible properties
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.histogram.Hoverlabel instance or dict
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
        marker
            plotly.graph_objs.histogram.Marker instance or dict
            with compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        selected
            plotly.graph_objs.histogram.Selected instance or dict
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
            plotly.graph_objs.histogram.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        unselected
            plotly.graph_objs.histogram.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbins
            plotly.graph_objs.histogram.XBins instance or dict with
            compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybins
            plotly.graph_objs.histogram.YBins instance or dict with
            compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .
        """

    def __init__(
        self,
        arg=None,
        autobinx=None,
        autobiny=None,
        cumulative=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        opacity=None,
        orientation=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        unselected=None,
        visible=None,
        x=None,
        xaxis=None,
        xbins=None,
        xcalendar=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybins=None,
        ycalendar=None,
        ysrc=None,
        **kwargs
    ):
        """
        Construct a new Histogram object
        
        The sample data from which statistics are computed is set in
        `x` for vertically spanning histograms and in `y` for
        horizontally spanning histograms. Binning options are set
        `xbins` and `ybins` respectively if no aggregation data is
        provided.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Histogram
        autobinx
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobinx` is not needed.
            However, we accept `autobinx: true` or `false` and will
            update `xbins` accordingly before deleting `autobinx`
            from the trace.
        autobiny
            Obsolete: since v1.42 each bin attribute is auto-
            determined separately and `autobiny` is not needed.
            However, we accept `autobiny: true` or `false` and will
            update `ybins` accordingly before deleting `autobiny`
            from the trace.
        cumulative
            plotly.graph_objs.histogram.Cumulative instance or dict
            with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        error_x
            plotly.graph_objs.histogram.ErrorX instance or dict
            with compatible properties
        error_y
            plotly.graph_objs.histogram.ErrorY instance or dict
            with compatible properties
        histfunc
            Specifies the binning function used for this histogram
            trace. If "count", the histogram values are computed by
            counting the number of values lying inside each bin. If
            "sum", "avg", "min", "max", the histogram values are
            computed using the sum, the average, the minimum or the
            maximum of the values lying inside each bin
            respectively.
        histnorm
            Specifies the type of normalization used for this
            histogram trace. If "", the span of each bar
            corresponds to the number of occurrences (i.e. the
            number of data points lying inside the bins). If
            "percent" / "probability", the span of each bar
            corresponds to the percentage / fraction of occurrences
            with respect to the total number of sample points
            (here, the sum of all bin HEIGHTS equals 100% / 1). If
            "density", the span of each bar corresponds to the
            number of occurrences in a bin divided by the size of
            the bin interval (here, the sum of all bin AREAS equals
            the total number of sample points). If *probability
            density*, the area of each bar corresponds to the
            probability that an event will fall into the
            corresponding bin (here, the sum of all bin AREAS
            equals 1).
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.histogram.Hoverlabel instance or dict
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
        marker
            plotly.graph_objs.histogram.Marker instance or dict
            with compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        nbinsx
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `xbins.size` is provided.
        nbinsy
            Specifies the maximum number of desired bins. This
            value will be used in an algorithm that will decide the
            optimal bin size such that the histogram best
            visualizes the distribution of the data. Ignored if
            `ybins.size` is provided.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        selected
            plotly.graph_objs.histogram.Selected instance or dict
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
            plotly.graph_objs.histogram.Stream instance or dict
            with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        unselected
            plotly.graph_objs.histogram.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the sample data to be binned on the x axis.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xbins
            plotly.graph_objs.histogram.XBins instance or dict with
            compatible properties
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the sample data to be binned on the y axis.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ybins
            plotly.graph_objs.histogram.YBins instance or dict with
            compatible properties
        ycalendar
            Sets the calendar system to use with `y` date data.
        ysrc
            Sets the source reference on plot.ly for  y .

        Returns
        -------
        Histogram
        """
        super(Histogram, self).__init__('histogram')

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
The first argument to the plotly.graph_objs.Histogram 
constructor must be a dict or 
an instance of plotly.graph_objs.Histogram"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (histogram as v_histogram)

        # Initialize validators
        # ---------------------
        self._validators['autobinx'] = v_histogram.AutobinxValidator()
        self._validators['autobiny'] = v_histogram.AutobinyValidator()
        self._validators['cumulative'] = v_histogram.CumulativeValidator()
        self._validators['customdata'] = v_histogram.CustomdataValidator()
        self._validators['customdatasrc'
                        ] = v_histogram.CustomdatasrcValidator()
        self._validators['error_x'] = v_histogram.ErrorXValidator()
        self._validators['error_y'] = v_histogram.ErrorYValidator()
        self._validators['histfunc'] = v_histogram.HistfuncValidator()
        self._validators['histnorm'] = v_histogram.HistnormValidator()
        self._validators['hoverinfo'] = v_histogram.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_histogram.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_histogram.HoverlabelValidator()
        self._validators['ids'] = v_histogram.IdsValidator()
        self._validators['idssrc'] = v_histogram.IdssrcValidator()
        self._validators['legendgroup'] = v_histogram.LegendgroupValidator()
        self._validators['marker'] = v_histogram.MarkerValidator()
        self._validators['name'] = v_histogram.NameValidator()
        self._validators['nbinsx'] = v_histogram.NbinsxValidator()
        self._validators['nbinsy'] = v_histogram.NbinsyValidator()
        self._validators['opacity'] = v_histogram.OpacityValidator()
        self._validators['orientation'] = v_histogram.OrientationValidator()
        self._validators['selected'] = v_histogram.SelectedValidator()
        self._validators['selectedpoints'
                        ] = v_histogram.SelectedpointsValidator()
        self._validators['showlegend'] = v_histogram.ShowlegendValidator()
        self._validators['stream'] = v_histogram.StreamValidator()
        self._validators['text'] = v_histogram.TextValidator()
        self._validators['textsrc'] = v_histogram.TextsrcValidator()
        self._validators['uid'] = v_histogram.UidValidator()
        self._validators['unselected'] = v_histogram.UnselectedValidator()
        self._validators['visible'] = v_histogram.VisibleValidator()
        self._validators['x'] = v_histogram.XValidator()
        self._validators['xaxis'] = v_histogram.XAxisValidator()
        self._validators['xbins'] = v_histogram.XBinsValidator()
        self._validators['xcalendar'] = v_histogram.XcalendarValidator()
        self._validators['xsrc'] = v_histogram.XsrcValidator()
        self._validators['y'] = v_histogram.YValidator()
        self._validators['yaxis'] = v_histogram.YAxisValidator()
        self._validators['ybins'] = v_histogram.YBinsValidator()
        self._validators['ycalendar'] = v_histogram.YcalendarValidator()
        self._validators['ysrc'] = v_histogram.YsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('autobinx', None)
        self['autobinx'] = autobinx if autobinx is not None else _v
        _v = arg.pop('autobiny', None)
        self['autobiny'] = autobiny if autobiny is not None else _v
        _v = arg.pop('cumulative', None)
        self['cumulative'] = cumulative if cumulative is not None else _v
        _v = arg.pop('customdata', None)
        self['customdata'] = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self['customdatasrc'
            ] = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('error_x', None)
        self['error_x'] = error_x if error_x is not None else _v
        _v = arg.pop('error_y', None)
        self['error_y'] = error_y if error_y is not None else _v
        _v = arg.pop('histfunc', None)
        self['histfunc'] = histfunc if histfunc is not None else _v
        _v = arg.pop('histnorm', None)
        self['histnorm'] = histnorm if histnorm is not None else _v
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
        _v = arg.pop('marker', None)
        self['marker'] = marker if marker is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('nbinsx', None)
        self['nbinsx'] = nbinsx if nbinsx is not None else _v
        _v = arg.pop('nbinsy', None)
        self['nbinsy'] = nbinsy if nbinsy is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('orientation', None)
        self['orientation'] = orientation if orientation is not None else _v
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
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('xaxis', None)
        self['xaxis'] = xaxis if xaxis is not None else _v
        _v = arg.pop('xbins', None)
        self['xbins'] = xbins if xbins is not None else _v
        _v = arg.pop('xcalendar', None)
        self['xcalendar'] = xcalendar if xcalendar is not None else _v
        _v = arg.pop('xsrc', None)
        self['xsrc'] = xsrc if xsrc is not None else _v
        _v = arg.pop('y', None)
        self['y'] = y if y is not None else _v
        _v = arg.pop('yaxis', None)
        self['yaxis'] = yaxis if yaxis is not None else _v
        _v = arg.pop('ybins', None)
        self['ybins'] = ybins if ybins is not None else _v
        _v = arg.pop('ycalendar', None)
        self['ycalendar'] = ycalendar if ycalendar is not None else _v
        _v = arg.pop('ysrc', None)
        self['ysrc'] = ysrc if ysrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'histogram'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='histogram', val='histogram'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
