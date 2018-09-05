from plotly.basedatatypes import BaseTraceType
import copy


class Parcoords(BaseTraceType):

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

    # dimensions
    # ----------
    @property
    def dimensions(self):
        """
        The dimensions (variables) of the parallel coordinates chart.
        2..60 dimensions are supported.
    
        The 'dimensions' property is a tuple of instances of
        Dimension that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.parcoords.Dimension
          - A list or tuple of dicts of string/value properties that
            will be passed to the Dimension constructor
    
            Supported dict properties:
                
                constraintrange
                    The domain range to which the filter on the
                    dimension is constrained. Must be an array of
                    `[fromValue, toValue]` with `fromValue <=
                    toValue`, or if `multiselect` is not disabled,
                    you may give an array of arrays, where each
                    inner array is `[fromValue, toValue]`.
                label
                    The shown name of the dimension.
                multiselect
                    Do we allow multiple selection ranges or just a
                    single range?
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
                    The domain range that represents the full,
                    shown axis extent. Defaults to the `values`
                    extent. Must be an array of `[fromValue,
                    toValue]` with finite numbers as elements.
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
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-language which is similar to
                    those of Python. See https://github.com/d3/d3-f
                    ormat/blob/master/README.md#locale_format
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
                values
                    Dimension values. `values[n]` represents the
                    value of the `n`th point in the dataset,
                    therefore the `values` vector for all
                    dimensions must be the same (longer vectors
                    will be truncated). Each value must be a finite
                    number.
                valuessrc
                    Sets the source reference on plot.ly for
                    values .
                visible
                    Shows the dimension when set to `true` (the
                    default). Hides the dimension for `false`.

        Returns
        -------
        tuple[plotly.graph_objs.parcoords.Dimension]
        """
        return self['dimensions']

    @dimensions.setter
    def dimensions(self, val):
        self['dimensions'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.parcoords.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this parcoords
                    trace .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this parcoords trace .
                x
                    Sets the horizontal domain of this parcoords
                    trace (in plot fraction).
                y
                    Sets the vertical domain of this parcoords
                    trace (in plot fraction).

        Returns
        -------
        plotly.graph_objs.parcoords.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

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
          - An instance of plotly.graph_objs.parcoords.Hoverlabel
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
        plotly.graph_objs.parcoords.Hoverlabel
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

    # labelfont
    # ---------
    @property
    def labelfont(self):
        """
        Sets the font for the `dimension` labels.
    
        The 'labelfont' property is an instance of Labelfont
        that may be specified as:
          - An instance of plotly.graph_objs.parcoords.Labelfont
          - A dict of string/value properties that will be passed
            to the Labelfont constructor
    
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
        plotly.graph_objs.parcoords.Labelfont
        """
        return self['labelfont']

    @labelfont.setter
    def labelfont(self, val):
        self['labelfont'] = val

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
          - An instance of plotly.graph_objs.parcoords.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                autocolorscale
                    Determines whether the colorscale is a default
                    palette (`autocolorscale: true`) or the palette
                    determined by `line.colorscale`. Has an effect
                    only if in `line.color`is set to a numerical
                    array. In case `colorscale` is unspecified or
                    `autocolorscale` is true, the default  palette
                    will be chosen according to whether numbers in
                    the `color` array are all positive, all
                    negative or mixed.
                cauto
                    Determines whether or not the color domain is
                    computed with respect to the input data (here
                    in `line.color`) or the bounds set in
                    `line.cmin` and `line.cmax`  Has an effect only
                    if in `line.color`is set to a numerical array.
                    Defaults to `false` when `line.cmin` and
                    `line.cmax` are set by the user.
                cmax
                    Sets the upper bound of the color domain. Has
                    an effect only if in `line.color`is set to a
                    numerical array. Value should have the same
                    units as in `line.color` and if set,
                    `line.cmin` must be set as well.
                cmin
                    Sets the lower bound of the color domain. Has
                    an effect only if in `line.color`is set to a
                    numerical array. Value should have the same
                    units as in `line.color` and if set,
                    `line.cmax` must be set as well.
                color
                    Sets thelinecolor. It accepts either a specific
                    color or an array of numbers that are mapped to
                    the colorscale relative to the max and min
                    values of the array or relative to `line.cmin`
                    and `line.cmax` if set.
                colorbar
                    plotly.graph_objs.parcoords.line.ColorBar
                    instance or dict with compatible properties
                colorscale
                    Sets the colorscale. Has an effect only if in
                    `line.color`is set to a numerical array. The
                    colorscale must be an array containing arrays
                    mapping a normalized value to an rgb, rgba,
                    hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To
                    control the bounds of the colorscale in color
                    space, use`line.cmin` and `line.cmax`.
                    Alternatively, `colorscale` may be a palette
                    name string of the following list: Greys,YlGnBu
                    ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,R
                    ainbow,Portland,Jet,Hot,Blackbody,Earth,Electri
                    c,Viridis,Cividis.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                reversescale
                    Reverses the color mapping if true. Has an
                    effect only if in `line.color`is set to a
                    numerical array. If true, `line.cmin` will
                    correspond to the last color in the array and
                    `line.cmax` will correspond to the first color.
                showscale
                    Determines whether or not a colorbar is
                    displayed for this trace. Has an effect only if
                    in `line.color`is set to a numerical array.

        Returns
        -------
        plotly.graph_objs.parcoords.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

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

    # rangefont
    # ---------
    @property
    def rangefont(self):
        """
        Sets the font for the `dimension` range values.
    
        The 'rangefont' property is an instance of Rangefont
        that may be specified as:
          - An instance of plotly.graph_objs.parcoords.Rangefont
          - A dict of string/value properties that will be passed
            to the Rangefont constructor
    
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
        plotly.graph_objs.parcoords.Rangefont
        """
        return self['rangefont']

    @rangefont.setter
    def rangefont(self, val):
        self['rangefont'] = val

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
          - An instance of plotly.graph_objs.parcoords.Stream
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
        plotly.graph_objs.parcoords.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the font for the `dimension` tick values.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of plotly.graph_objs.parcoords.Tickfont
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
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.parcoords.Tickfont
        """
        return self['tickfont']

    @tickfont.setter
    def tickfont(self, val):
        self['tickfont'] = val

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
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dimensions
            The dimensions (variables) of the parallel coordinates
            chart. 2..60 dimensions are supported.
        domain
            plotly.graph_objs.parcoords.Domain instance or dict
            with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.parcoords.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        labelfont
            Sets the font for the `dimension` labels.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.parcoords.Line instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        rangefont
            Sets the font for the `dimension` range values.
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
            plotly.graph_objs.parcoords.Stream instance or dict
            with compatible properties
        tickfont
            Sets the font for the `dimension` tick values.
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        """

    def __init__(
        self,
        arg=None,
        customdata=None,
        customdatasrc=None,
        dimensions=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        labelfont=None,
        legendgroup=None,
        line=None,
        name=None,
        opacity=None,
        rangefont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        tickfont=None,
        uid=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Parcoords object
        
        Parallel coordinates for multidimensional exploratory data
        analysis. The samples are specified in `dimensions`. The colors
        are set in `line.color`.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Parcoords
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        dimensions
            The dimensions (variables) of the parallel coordinates
            chart. 2..60 dimensions are supported.
        domain
            plotly.graph_objs.parcoords.Domain instance or dict
            with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.parcoords.Hoverlabel instance or dict
            with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        labelfont
            Sets the font for the `dimension` labels.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.parcoords.Line instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        rangefont
            Sets the font for the `dimension` range values.
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
            plotly.graph_objs.parcoords.Stream instance or dict
            with compatible properties
        tickfont
            Sets the font for the `dimension` tick values.
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Parcoords
        """
        super(Parcoords, self).__init__('parcoords')

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
The first argument to the plotly.graph_objs.Parcoords 
constructor must be a dict or 
an instance of plotly.graph_objs.Parcoords"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (parcoords as v_parcoords)

        # Initialize validators
        # ---------------------
        self._validators['customdata'] = v_parcoords.CustomdataValidator()
        self._validators['customdatasrc'
                        ] = v_parcoords.CustomdatasrcValidator()
        self._validators['dimensions'] = v_parcoords.DimensionsValidator()
        self._validators['domain'] = v_parcoords.DomainValidator()
        self._validators['hoverinfo'] = v_parcoords.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_parcoords.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_parcoords.HoverlabelValidator()
        self._validators['ids'] = v_parcoords.IdsValidator()
        self._validators['idssrc'] = v_parcoords.IdssrcValidator()
        self._validators['labelfont'] = v_parcoords.LabelfontValidator()
        self._validators['legendgroup'] = v_parcoords.LegendgroupValidator()
        self._validators['line'] = v_parcoords.LineValidator()
        self._validators['name'] = v_parcoords.NameValidator()
        self._validators['opacity'] = v_parcoords.OpacityValidator()
        self._validators['rangefont'] = v_parcoords.RangefontValidator()
        self._validators['selectedpoints'
                        ] = v_parcoords.SelectedpointsValidator()
        self._validators['showlegend'] = v_parcoords.ShowlegendValidator()
        self._validators['stream'] = v_parcoords.StreamValidator()
        self._validators['tickfont'] = v_parcoords.TickfontValidator()
        self._validators['uid'] = v_parcoords.UidValidator()
        self._validators['visible'] = v_parcoords.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('customdata', None)
        self.customdata = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self.customdatasrc = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('dimensions', None)
        self.dimensions = dimensions if dimensions is not None else _v
        _v = arg.pop('domain', None)
        self.domain = domain if domain is not None else _v
        _v = arg.pop('hoverinfo', None)
        self.hoverinfo = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoverinfosrc', None)
        self.hoverinfosrc = hoverinfosrc if hoverinfosrc is not None else _v
        _v = arg.pop('hoverlabel', None)
        self.hoverlabel = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('ids', None)
        self.ids = ids if ids is not None else _v
        _v = arg.pop('idssrc', None)
        self.idssrc = idssrc if idssrc is not None else _v
        _v = arg.pop('labelfont', None)
        self.labelfont = labelfont if labelfont is not None else _v
        _v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup if legendgroup is not None else _v
        _v = arg.pop('line', None)
        self.line = line if line is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('rangefont', None)
        self.rangefont = rangefont if rangefont is not None else _v
        _v = arg.pop('selectedpoints', None)
        self.selectedpoints = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self.showlegend = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self.stream = stream if stream is not None else _v
        _v = arg.pop('tickfont', None)
        self.tickfont = tickfont if tickfont is not None else _v
        _v = arg.pop('uid', None)
        self.uid = uid if uid is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'parcoords'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='parcoords', val='parcoords'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
