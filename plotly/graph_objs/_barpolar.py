from plotly.basedatatypes import BaseTraceType
import copy


class Barpolar(BaseTraceType):

    # base
    # ----
    @property
    def base(self):
        """
        Sets where the bar base is drawn (in radial axis units). In
        "stack" barmode, traces that set "base" will be excluded and
        drawn in "overlay" mode instead.
    
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

    # dr
    # --
    @property
    def dr(self):
        """
        Sets the r coordinate step.
    
        The 'dr' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dr']

    @dr.setter
    def dr(self, val):
        self['dr'] = val

    # dtheta
    # ------
    @property
    def dtheta(self):
        """
        Sets the theta coordinate step. By default, the `dtheta` step
        equals the subplot's period divided by the length of the `r`
        coordinates.
    
        The 'dtheta' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dtheta']

    @dtheta.setter
    def dtheta(self, val):
        self['dtheta'] = val

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
          - Any combination of ['r', 'theta', 'text', 'name'] joined with '+' characters
            (e.g. 'r+theta')
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
          - An instance of plotly.graph_objs.barpolar.Hoverlabel
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
        plotly.graph_objs.barpolar.Hoverlabel
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
          - An instance of plotly.graph_objs.barpolar.Marker
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
                    plotly.graph_objs.barpolar.marker.ColorBar
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
                    plotly.graph_objs.barpolar.marker.Line instance
                    or dict with compatible properties
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
        plotly.graph_objs.barpolar.Marker
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
        Shifts the angular position where the bar is drawn (in
        "thetatunit" units).
    
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

    # r
    # -
    @property
    def r(self):
        """
        Sets the radial coordinates
    
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

    # r0
    # --
    @property
    def r0(self):
        """
        Alternate to `r`. Builds a linear space of r coordinates. Use
        with `dr` where `r0` is the starting coordinate and `dr` the
        step.
    
        The 'r0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['r0']

    @r0.setter
    def r0(self, val):
        self['r0'] = val

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
          - An instance of plotly.graph_objs.barpolar.Selected
          - A dict of string/value properties that will be passed
            to the Selected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.barpolar.selected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.barpolar.selected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.barpolar.Selected
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
          - An instance of plotly.graph_objs.barpolar.Stream
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
        plotly.graph_objs.barpolar.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # subplot
    # -------
    @property
    def subplot(self):
        """
        Sets a reference between this trace's data coordinates and a
        polar subplot. If "polar" (the default value), the data refer
        to `layout.polar`. If "polar2", the data refer to
        `layout.polar2`, and so on.
    
        The 'subplot' property is an identifier of a particular
        subplot, of type 'polar', that may be specified as the string 'polar'
        optionally followed by an integer >= 1
        (e.g. 'polar', 'polar1', 'polar2', 'polar3', etc.)

        Returns
        -------
        str
        """
        return self['subplot']

    @subplot.setter
    def subplot(self, val):
        self['subplot'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets hover text elements associated with each bar. If a single
        string, the same string appears over all bars. If an array of
        string, the items are mapped in order to the this trace's
        coordinates.
    
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

    # theta
    # -----
    @property
    def theta(self):
        """
        Sets the angular coordinates
    
        The 'theta' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['theta']

    @theta.setter
    def theta(self, val):
        self['theta'] = val

    # theta0
    # ------
    @property
    def theta0(self):
        """
        Alternate to `theta`. Builds a linear space of theta
        coordinates. Use with `dtheta` where `theta0` is the starting
        coordinate and `dtheta` the step.
    
        The 'theta0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['theta0']

    @theta0.setter
    def theta0(self, val):
        self['theta0'] = val

    # thetasrc
    # --------
    @property
    def thetasrc(self):
        """
        Sets the source reference on plot.ly for  theta .
    
        The 'thetasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['thetasrc']

    @thetasrc.setter
    def thetasrc(self, val):
        self['thetasrc'] = val

    # thetaunit
    # ---------
    @property
    def thetaunit(self):
        """
        Sets the unit of input "theta" values. Has an effect only when
        on "linear" angular axes.
    
        The 'thetaunit' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['radians', 'degrees', 'gradians']

        Returns
        -------
        Any
        """
        return self['thetaunit']

    @thetaunit.setter
    def thetaunit(self, val):
        self['thetaunit'] = val

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
          - An instance of plotly.graph_objs.barpolar.Unselected
          - A dict of string/value properties that will be passed
            to the Unselected constructor
    
            Supported dict properties:
                
                marker
                    plotly.graph_objs.barpolar.unselected.Marker
                    instance or dict with compatible properties
                textfont
                    plotly.graph_objs.barpolar.unselected.Textfont
                    instance or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.barpolar.Unselected
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
        Sets the bar angular width (in "thetaunit" units).
    
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
            Sets where the bar base is drawn (in radial axis
            units). In "stack" barmode, traces that set "base" will
            be excluded and drawn in "overlay" mode instead.
        basesrc
            Sets the source reference on plot.ly for  base .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.barpolar.Hoverlabel instance or dict
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
            plotly.graph_objs.barpolar.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the angular position where the bar is drawn (in
            "thetatunit" units).
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.barpolar.Selected instance or dict
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
            plotly.graph_objs.barpolar.Stream instance or dict with
            compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets hover text elements associated with each bar. If a
            single string, the same string appears over all bars.
            If an array of string, the items are mapped in order to
            the this trace's coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on plot.ly for  theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid

        unselected
            plotly.graph_objs.barpolar.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar angular width (in "thetaunit" units).
        widthsrc
            Sets the source reference on plot.ly for  width .
        """

    def __init__(
        self,
        arg=None,
        base=None,
        basesrc=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        marker=None,
        name=None,
        offset=None,
        offsetsrc=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        **kwargs
    ):
        """
        Construct a new Barpolar object
        
        The data visualized by the radial span of the bars is set in
        `r`

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Barpolar
        base
            Sets where the bar base is drawn (in radial axis
            units). In "stack" barmode, traces that set "base" will
            be excluded and drawn in "overlay" mode instead.
        basesrc
            Sets the source reference on plot.ly for  base .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dr
            Sets the r coordinate step.
        dtheta
            Sets the theta coordinate step. By default, the
            `dtheta` step equals the subplot's period divided by
            the length of the `r` coordinates.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.barpolar.Hoverlabel instance or dict
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
            plotly.graph_objs.barpolar.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        offset
            Shifts the angular position where the bar is drawn (in
            "thetatunit" units).
        offsetsrc
            Sets the source reference on plot.ly for  offset .
        opacity
            Sets the opacity of the trace.
        r
            Sets the radial coordinates
        r0
            Alternate to `r`. Builds a linear space of r
            coordinates. Use with `dr` where `r0` is the starting
            coordinate and `dr` the step.
        rsrc
            Sets the source reference on plot.ly for  r .
        selected
            plotly.graph_objs.barpolar.Selected instance or dict
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
            plotly.graph_objs.barpolar.Stream instance or dict with
            compatible properties
        subplot
            Sets a reference between this trace's data coordinates
            and a polar subplot. If "polar" (the default value),
            the data refer to `layout.polar`. If "polar2", the data
            refer to `layout.polar2`, and so on.
        text
            Sets hover text elements associated with each bar. If a
            single string, the same string appears over all bars.
            If an array of string, the items are mapped in order to
            the this trace's coordinates.
        textsrc
            Sets the source reference on plot.ly for  text .
        theta
            Sets the angular coordinates
        theta0
            Alternate to `theta`. Builds a linear space of theta
            coordinates. Use with `dtheta` where `theta0` is the
            starting coordinate and `dtheta` the step.
        thetasrc
            Sets the source reference on plot.ly for  theta .
        thetaunit
            Sets the unit of input "theta" values. Has an effect
            only when on "linear" angular axes.
        uid

        unselected
            plotly.graph_objs.barpolar.Unselected instance or dict
            with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        width
            Sets the bar angular width (in "thetaunit" units).
        widthsrc
            Sets the source reference on plot.ly for  width .

        Returns
        -------
        Barpolar
        """
        super(Barpolar, self).__init__('barpolar')

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
The first argument to the plotly.graph_objs.Barpolar 
constructor must be a dict or 
an instance of plotly.graph_objs.Barpolar"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (barpolar as v_barpolar)

        # Initialize validators
        # ---------------------
        self._validators['base'] = v_barpolar.BaseValidator()
        self._validators['basesrc'] = v_barpolar.BasesrcValidator()
        self._validators['customdata'] = v_barpolar.CustomdataValidator()
        self._validators['customdatasrc'] = v_barpolar.CustomdatasrcValidator()
        self._validators['dr'] = v_barpolar.DrValidator()
        self._validators['dtheta'] = v_barpolar.DthetaValidator()
        self._validators['hoverinfo'] = v_barpolar.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_barpolar.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_barpolar.HoverlabelValidator()
        self._validators['ids'] = v_barpolar.IdsValidator()
        self._validators['idssrc'] = v_barpolar.IdssrcValidator()
        self._validators['legendgroup'] = v_barpolar.LegendgroupValidator()
        self._validators['marker'] = v_barpolar.MarkerValidator()
        self._validators['name'] = v_barpolar.NameValidator()
        self._validators['offset'] = v_barpolar.OffsetValidator()
        self._validators['offsetsrc'] = v_barpolar.OffsetsrcValidator()
        self._validators['opacity'] = v_barpolar.OpacityValidator()
        self._validators['r'] = v_barpolar.RValidator()
        self._validators['r0'] = v_barpolar.R0Validator()
        self._validators['rsrc'] = v_barpolar.RsrcValidator()
        self._validators['selected'] = v_barpolar.SelectedValidator()
        self._validators['selectedpoints'
                        ] = v_barpolar.SelectedpointsValidator()
        self._validators['showlegend'] = v_barpolar.ShowlegendValidator()
        self._validators['stream'] = v_barpolar.StreamValidator()
        self._validators['subplot'] = v_barpolar.SubplotValidator()
        self._validators['text'] = v_barpolar.TextValidator()
        self._validators['textsrc'] = v_barpolar.TextsrcValidator()
        self._validators['theta'] = v_barpolar.ThetaValidator()
        self._validators['theta0'] = v_barpolar.Theta0Validator()
        self._validators['thetasrc'] = v_barpolar.ThetasrcValidator()
        self._validators['thetaunit'] = v_barpolar.ThetaunitValidator()
        self._validators['uid'] = v_barpolar.UidValidator()
        self._validators['unselected'] = v_barpolar.UnselectedValidator()
        self._validators['visible'] = v_barpolar.VisibleValidator()
        self._validators['width'] = v_barpolar.WidthValidator()
        self._validators['widthsrc'] = v_barpolar.WidthsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('base', None)
        self['base'] = base if base is not None else _v
        _v = arg.pop('basesrc', None)
        self['basesrc'] = basesrc if basesrc is not None else _v
        _v = arg.pop('customdata', None)
        self['customdata'] = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self['customdatasrc'
            ] = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('dr', None)
        self['dr'] = dr if dr is not None else _v
        _v = arg.pop('dtheta', None)
        self['dtheta'] = dtheta if dtheta is not None else _v
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
        _v = arg.pop('offset', None)
        self['offset'] = offset if offset is not None else _v
        _v = arg.pop('offsetsrc', None)
        self['offsetsrc'] = offsetsrc if offsetsrc is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('r', None)
        self['r'] = r if r is not None else _v
        _v = arg.pop('r0', None)
        self['r0'] = r0 if r0 is not None else _v
        _v = arg.pop('rsrc', None)
        self['rsrc'] = rsrc if rsrc is not None else _v
        _v = arg.pop('selected', None)
        self['selected'] = selected if selected is not None else _v
        _v = arg.pop('selectedpoints', None)
        self['selectedpoints'
            ] = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self['showlegend'] = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self['stream'] = stream if stream is not None else _v
        _v = arg.pop('subplot', None)
        self['subplot'] = subplot if subplot is not None else _v
        _v = arg.pop('text', None)
        self['text'] = text if text is not None else _v
        _v = arg.pop('textsrc', None)
        self['textsrc'] = textsrc if textsrc is not None else _v
        _v = arg.pop('theta', None)
        self['theta'] = theta if theta is not None else _v
        _v = arg.pop('theta0', None)
        self['theta0'] = theta0 if theta0 is not None else _v
        _v = arg.pop('thetasrc', None)
        self['thetasrc'] = thetasrc if thetasrc is not None else _v
        _v = arg.pop('thetaunit', None)
        self['thetaunit'] = thetaunit if thetaunit is not None else _v
        _v = arg.pop('uid', None)
        self['uid'] = uid if uid is not None else _v
        _v = arg.pop('unselected', None)
        self['unselected'] = unselected if unselected is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v
        _v = arg.pop('width', None)
        self['width'] = width if width is not None else _v
        _v = arg.pop('widthsrc', None)
        self['widthsrc'] = widthsrc if widthsrc is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'barpolar'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='barpolar', val='barpolar'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
