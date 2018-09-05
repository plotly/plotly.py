from plotly.basedatatypes import BaseTraceType
import copy


class Bar(BaseTraceType):

    # base
    # ----
    @property
    def base(self):
        """
        Sets where the bar base is drawn (in position axis units). In
        "stack" or "relative" barmode, traces that set "base" will be
        excluded and drawn in "overlay" mode instead.
    
        The 'base' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['base']

    @base.setter
    def base(self, val):
        self['base'] = val

    # basesrc
    # -------
    @property
    def basesrc(self):
        """
        Sets the source reference on plot.ly for  base .
    
        The 'basesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['basesrc']

    @basesrc.setter
    def basesrc(self, val):
        self['basesrc'] = val

    # cliponaxis
    # ----------
    @property
    def cliponaxis(self):
        """
        Determines whether the text nodes are clipped about the subplot
        axes. To show the text nodes above axis lines and tick labels,
        make sure to set `xaxis.layer` and `yaxis.layer` to *below
        traces*.
    
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

    # constraintext
    # -------------
    @property
    def constraintext(self):
        """
        Constrain the size of text inside or outside a bar to be no
        larger than the bar itself.
    
        The 'constraintext' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['inside', 'outside', 'both', 'none']

        Returns
        -------
        Any
        """
        return self['constraintext']

    @constraintext.setter
    def constraintext(self, val):
        self['constraintext'] = val

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
          - An instance of plotly.graph_objs.bar.ErrorX
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
        plotly.graph_objs.bar.ErrorX
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
          - An instance of plotly.graph_objs.bar.ErrorY
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
        plotly.graph_objs.bar.ErrorY
        """
        return self['error_y']

    @error_y.setter
    def error_y(self, val):
        self['error_y'] = val

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
          - An instance of plotly.graph_objs.bar.Hoverlabel
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
        plotly.graph_objs.bar.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

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

    # insidetextfont
    # --------------
    @property
    def insidetextfont(self):
        """
        Sets the font used for `text` lying inside the bar.
    
        The 'insidetextfont' property is an instance of Insidetextfont
        that may be specified as:
          - An instance of plotly.graph_objs.bar.Insidetextfont
          - A dict of string/value properties that will be passed
            to the Insidetextfont constructor
    
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
        plotly.graph_objs.bar.Insidetextfont
        """
        return self['insidetextfont']

    @insidetextfont.setter
    def insidetextfont(self, val):
        self['insidetextfont'] = val

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
          - An instance of plotly.graph_objs.bar.Marker
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
                    plotly.graph_objs.bar.marker.ColorBar instance
                    or dict with compatible properties
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
                    plotly.graph_objs.bar.marker.Line instance or
                    dict with compatible properties
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
        plotly.graph_objs.bar.Marker
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

    # offset
    # ------
    @property
    def offset(self):
        """
        Shifts the position where the bar is drawn (in position axis
        units). In "group" barmode, traces that set "offset" will be
        excluded and drawn in "overlay" mode instead.
    
        The 'offset' property is a number and may be specified as:
          - An int or float
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['offset']

    @offset.setter
    def offset(self, val):
        self['offset'] = val

    # offsetsrc
    # ---------
    @property
    def offsetsrc(self):
        """
        Sets the source reference on plot.ly for  offset .
    
        The 'offsetsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['offsetsrc']

    @offsetsrc.setter
    def offsetsrc(self, val):
        self['offsetsrc'] = val

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

    # outsidetextfont
    # ---------------
    @property
    def outsidetextfont(self):
        """
        Sets the font used for `text` lying outside the bar.
    
        The 'outsidetextfont' property is an instance of Outsidetextfont
        that may be specified as:
          - An instance of plotly.graph_objs.bar.Outsidetextfont
          - A dict of string/value properties that will be passed
            to the Outsidetextfont constructor
    
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
        plotly.graph_objs.bar.Outsidetextfont
        """
        return self['outsidetextfont']

    @outsidetextfont.setter
    def outsidetextfont(self, val):
        self['outsidetextfont'] = val

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
          - An instance of plotly.graph_objs.bar.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.bar.selected.Marker instance
                    or dict with compatible properties
                textfont
                    plotly.graph_objs.bar.selected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.bar.Selected
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
          - An instance of plotly.graph_objs.bar.Stream
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
        plotly.graph_objs.bar.Stream
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
        Sets the font used for `text`.
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.bar.Textfont
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
        plotly.graph_objs.bar.Textfont
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
        Specifies the location of the `text`. "inside" positions `text`
        inside, next to the bar end (rotated and scaled if needed).
        "outside" positions `text` outside, next to the bar end (scaled
        if needed). "auto" positions `text` inside or outside so that
        `text` size is maximized.
    
        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['inside', 'outside', 'auto', 'none']
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
          - An instance of plotly.graph_objs.bar.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.bar.unselected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.bar.unselected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.bar.Unselected
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

    # width
    # -----
    @property
    def width(self):
        """
        Sets the bar width (in position axis units).
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # widthsrc
    # --------
    @property
    def widthsrc(self):
        """
        Sets the source reference on plot.ly for  width .
    
        The 'widthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['widthsrc']

    @widthsrc.setter
    def widthsrc(self, val):
        self['widthsrc'] = val

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
        base
            Sets where the bar base is drawn (in position axis
            units). In "stack" or "relative" barmode, traces that
            set "base" will be excluded and drawn in "overlay" mode
            instead.
        basesrc
            Sets the source reference on plot.ly for  base .
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
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
            plotly.graph_objs.bar.ErrorX instance or dict with
            compatible properties
        error_y
            plotly.graph_objs.bar.ErrorY instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.bar.Hoverlabel instance or dict with
            compatible properties
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
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.bar.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        r
            For legacy polar chart only.Please switch to
            "scatterpolar" trace type.Sets the radial coordinates.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.bar.Selected instance or dict with
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
            plotly.graph_objs.bar.Stream instance or dict with
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
            Sets the font used for `text`.
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed). "auto"
            positions `text` inside or outside so that `text` size
            is maximized.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        tsrc
            Sets the source reference on plot.ly for  t .
        uid

        unselected
            plotly.graph_objs.bar.Unselected instance or dict with
            compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        widthsrc
            Sets the source reference on plot.ly for  width .
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
        base=None,
        basesrc=None,
        cliponaxis=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        legendgroup=None,
        marker=None,
        name=None,
        offset=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
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
        width=None,
        widthsrc=None,
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
        Construct a new Bar object
        
        The data visualized by the span of the bars is set in `y` if
        `orientation` is set th "v" (the default) and the labels are
        set in `x`. By setting `orientation` to "h", the roles are
        interchanged.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Bar
        base
            Sets where the bar base is drawn (in position axis
            units). In "stack" or "relative" barmode, traces that
            set "base" will be excluded and drawn in "overlay" mode
            instead.
        basesrc
            Sets the source reference on plot.ly for  base .
        cliponaxis
            Determines whether the text nodes are clipped about the
            subplot axes. To show the text nodes above axis lines
            and tick labels, make sure to set `xaxis.layer` and
            `yaxis.layer` to *below traces*.
        constraintext
            Constrain the size of text inside or outside a bar to
            be no larger than the bar itself.
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
            plotly.graph_objs.bar.ErrorX instance or dict with
            compatible properties
        error_y
            plotly.graph_objs.bar.ErrorY instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.bar.Hoverlabel instance or dict with
            compatible properties
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
        insidetextfont
            Sets the font used for `text` lying inside the bar.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.bar.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the position where the bar is drawn (in position
            axis units). In "group" barmode, traces that set
            "offset" will be excluded and drawn in "overlay" mode
            instead.
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the bars. With "v" ("h"), the
            value of the each bar spans along the vertical
            (horizontal).
        outsidetextfont
            Sets the font used for `text` lying outside the bar.
        r
            For legacy polar chart only.Please switch to
            "scatterpolar" trace type.Sets the radial coordinates.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.bar.Selected instance or dict with
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
            plotly.graph_objs.bar.Stream instance or dict with
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
            Sets the font used for `text`.
        textposition
            Specifies the location of the `text`. "inside"
            positions `text` inside, next to the bar end (rotated
            and scaled if needed). "outside" positions `text`
            outside, next to the bar end (scaled if needed). "auto"
            positions `text` inside or outside so that `text` size
            is maximized.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        tsrc
            Sets the source reference on plot.ly for  t .
        uid

        unselected
            plotly.graph_objs.bar.Unselected instance or dict with
            compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar width (in position axis units).
        widthsrc
            Sets the source reference on plot.ly for  width .
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
        Bar
        """
        super(Bar, self).__init__('bar')

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
The first argument to the plotly.graph_objs.Bar 
constructor must be a dict or 
an instance of plotly.graph_objs.Bar"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (bar as v_bar)

        # Initialize validators
        # ---------------------
        self._validators['base'] = v_bar.BaseValidator()
        self._validators['basesrc'] = v_bar.BasesrcValidator()
        self._validators['cliponaxis'] = v_bar.CliponaxisValidator()
        self._validators['constraintext'] = v_bar.ConstraintextValidator()
        self._validators['customdata'] = v_bar.CustomdataValidator()
        self._validators['customdatasrc'] = v_bar.CustomdatasrcValidator()
        self._validators['dx'] = v_bar.DxValidator()
        self._validators['dy'] = v_bar.DyValidator()
        self._validators['error_x'] = v_bar.ErrorXValidator()
        self._validators['error_y'] = v_bar.ErrorYValidator()
        self._validators['hoverinfo'] = v_bar.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_bar.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_bar.HoverlabelValidator()
        self._validators['hovertext'] = v_bar.HovertextValidator()
        self._validators['hovertextsrc'] = v_bar.HovertextsrcValidator()
        self._validators['ids'] = v_bar.IdsValidator()
        self._validators['idssrc'] = v_bar.IdssrcValidator()
        self._validators['insidetextfont'] = v_bar.InsidetextfontValidator()
        self._validators['legendgroup'] = v_bar.LegendgroupValidator()
        self._validators['marker'] = v_bar.MarkerValidator()
        self._validators['name'] = v_bar.NameValidator()
        self._validators['offset'] = v_bar.OffsetValidator()
        self._validators['offsetsrc'] = v_bar.OffsetsrcValidator()
        self._validators['opacity'] = v_bar.OpacityValidator()
        self._validators['orientation'] = v_bar.OrientationValidator()
        self._validators['outsidetextfont'] = v_bar.OutsidetextfontValidator()
        self._validators['r'] = v_bar.RValidator()
        self._validators['rsrc'] = v_bar.RsrcValidator()
        self._validators['selected'] = v_bar.SelectedValidator()
        self._validators['selectedpoints'] = v_bar.SelectedpointsValidator()
        self._validators['showlegend'] = v_bar.ShowlegendValidator()
        self._validators['stream'] = v_bar.StreamValidator()
        self._validators['t'] = v_bar.TValidator()
        self._validators['text'] = v_bar.TextValidator()
        self._validators['textfont'] = v_bar.TextfontValidator()
        self._validators['textposition'] = v_bar.TextpositionValidator()
        self._validators['textpositionsrc'] = v_bar.TextpositionsrcValidator()
        self._validators['textsrc'] = v_bar.TextsrcValidator()
        self._validators['tsrc'] = v_bar.TsrcValidator()
        self._validators['uid'] = v_bar.UidValidator()
        self._validators['unselected'] = v_bar.UnselectedValidator()
        self._validators['visible'] = v_bar.VisibleValidator()
        self._validators['width'] = v_bar.WidthValidator()
        self._validators['widthsrc'] = v_bar.WidthsrcValidator()
        self._validators['x'] = v_bar.XValidator()
        self._validators['x0'] = v_bar.X0Validator()
        self._validators['xaxis'] = v_bar.XAxisValidator()
        self._validators['xcalendar'] = v_bar.XcalendarValidator()
        self._validators['xsrc'] = v_bar.XsrcValidator()
        self._validators['y'] = v_bar.YValidator()
        self._validators['y0'] = v_bar.Y0Validator()
        self._validators['yaxis'] = v_bar.YAxisValidator()
        self._validators['ycalendar'] = v_bar.YcalendarValidator()
        self._validators['ysrc'] = v_bar.YsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('base', None)
        self.base = base if base is not None else _v
        _v = arg.pop('basesrc', None)
        self.basesrc = basesrc if basesrc is not None else _v
        _v = arg.pop('cliponaxis', None)
        self.cliponaxis = cliponaxis if cliponaxis is not None else _v
        _v = arg.pop('constraintext', None)
        self.constraintext = constraintext if constraintext is not None else _v
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
        _v = arg.pop('hoverinfo', None)
        self.hoverinfo = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoverinfosrc', None)
        self.hoverinfosrc = hoverinfosrc if hoverinfosrc is not None else _v
        _v = arg.pop('hoverlabel', None)
        self.hoverlabel = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('hovertext', None)
        self.hovertext = hovertext if hovertext is not None else _v
        _v = arg.pop('hovertextsrc', None)
        self.hovertextsrc = hovertextsrc if hovertextsrc is not None else _v
        _v = arg.pop('ids', None)
        self.ids = ids if ids is not None else _v
        _v = arg.pop('idssrc', None)
        self.idssrc = idssrc if idssrc is not None else _v
        _v = arg.pop('insidetextfont', None)
        self.insidetextfont = insidetextfont if insidetextfont is not None else _v
        _v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup if legendgroup is not None else _v
        _v = arg.pop('marker', None)
        self.marker = marker if marker is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('offset', None)
        self.offset = offset if offset is not None else _v
        _v = arg.pop('offsetsrc', None)
        self.offsetsrc = offsetsrc if offsetsrc is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('orientation', None)
        self.orientation = orientation if orientation is not None else _v
        _v = arg.pop('outsidetextfont', None)
        self.outsidetextfont = outsidetextfont if outsidetextfont is not None else _v
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
        _v = arg.pop('width', None)
        self.width = width if width is not None else _v
        _v = arg.pop('widthsrc', None)
        self.widthsrc = widthsrc if widthsrc is not None else _v
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
        self._props['type'] = 'bar'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='bar', val='bar'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
