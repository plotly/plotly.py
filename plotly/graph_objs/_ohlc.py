from plotly.basedatatypes import BaseTraceType
import copy


class Ohlc(BaseTraceType):

    # close
    # -----
    @property
    def close(self):
        """
        Sets the close values.
    
        The 'close' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['close']

    @close.setter
    def close(self, val):
        self['close'] = val

    # closesrc
    # --------
    @property
    def closesrc(self):
        """
        Sets the source reference on plot.ly for  close .
    
        The 'closesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['closesrc']

    @closesrc.setter
    def closesrc(self, val):
        self['closesrc'] = val

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

    # decreasing
    # ----------
    @property
    def decreasing(self):
        """
        The 'decreasing' property is an instance of Decreasing
        that may be specified as:
          - An instance of plotly.graph_objs.ohlc.Decreasing
          - A dict of string/value properties that will be passed
            to the Decreasing constructor
    
            Supported dict properties:
                
                line
                    plotly.graph_objs.ohlc.decreasing.Line instance
                    or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.ohlc.Decreasing
        """
        return self['decreasing']

    @decreasing.setter
    def decreasing(self, val):
        self['decreasing'] = val

    # high
    # ----
    @property
    def high(self):
        """
        Sets the high values.
    
        The 'high' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['high']

    @high.setter
    def high(self, val):
        self['high'] = val

    # highsrc
    # -------
    @property
    def highsrc(self):
        """
        Sets the source reference on plot.ly for  high .
    
        The 'highsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['highsrc']

    @highsrc.setter
    def highsrc(self, val):
        self['highsrc'] = val

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
          - An instance of plotly.graph_objs.ohlc.Hoverlabel
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
                split
                    Show hover information (open, close, high, low)
                    in separate labels.

        Returns
        -------
        plotly.graph_objs.ohlc.Hoverlabel
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

    # increasing
    # ----------
    @property
    def increasing(self):
        """
        The 'increasing' property is an instance of Increasing
        that may be specified as:
          - An instance of plotly.graph_objs.ohlc.Increasing
          - A dict of string/value properties that will be passed
            to the Increasing constructor
    
            Supported dict properties:
                
                line
                    plotly.graph_objs.ohlc.increasing.Line instance
                    or dict with compatible properties

        Returns
        -------
        plotly.graph_objs.ohlc.Increasing
        """
        return self['increasing']

    @increasing.setter
    def increasing(self, val):
        self['increasing'] = val

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
          - An instance of plotly.graph_objs.ohlc.Line
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                dash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                    Note that this style setting can also be set
                    per direction via `increasing.line.dash` and
                    `decreasing.line.dash`.
                width
                    [object Object] Note that this style setting
                    can also be set per direction via
                    `increasing.line.width` and
                    `decreasing.line.width`.

        Returns
        -------
        plotly.graph_objs.ohlc.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # low
    # ---
    @property
    def low(self):
        """
        Sets the low values.
    
        The 'low' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['low']

    @low.setter
    def low(self, val):
        self['low'] = val

    # lowsrc
    # ------
    @property
    def lowsrc(self):
        """
        Sets the source reference on plot.ly for  low .
    
        The 'lowsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['lowsrc']

    @lowsrc.setter
    def lowsrc(self, val):
        self['lowsrc'] = val

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

    # open
    # ----
    @property
    def open(self):
        """
        Sets the open values.
    
        The 'open' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['open']

    @open.setter
    def open(self, val):
        self['open'] = val

    # opensrc
    # -------
    @property
    def opensrc(self):
        """
        Sets the source reference on plot.ly for  open .
    
        The 'opensrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['opensrc']

    @opensrc.setter
    def opensrc(self, val):
        self['opensrc'] = val

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
          - An instance of plotly.graph_objs.ohlc.Stream
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
        plotly.graph_objs.ohlc.Stream
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
        Sets hover text elements associated with each sample point. If
        a single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        this trace's sample points.
    
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

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the width of the open/close tick marks relative to the "x"
        minimal interval.
    
        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, 0.5]

        Returns
        -------
        int|float
        """
        return self['tickwidth']

    @tickwidth.setter
    def tickwidth(self, val):
        self['tickwidth'] = val

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
        Sets the x coordinates. If absent, linear coordinate will be
        generated.
    
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
        close
            Sets the close values.
        closesrc
            Sets the source reference on plot.ly for  close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        decreasing
            plotly.graph_objs.ohlc.Decreasing instance or dict with
            compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on plot.ly for  high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.ohlc.Hoverlabel instance or dict with
            compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        increasing
            plotly.graph_objs.ohlc.Increasing instance or dict with
            compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.ohlc.Line instance or dict with
            compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on plot.ly for  low .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on plot.ly for  open .
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
            plotly.graph_objs.ohlc.Stream instance or dict with
            compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on plot.ly for  text .
        tickwidth
            Sets the width of the open/close tick marks relative to
            the "x" minimal interval.
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        """

    def __init__(
        self,
        arg=None,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legendgroup=None,
        line=None,
        low=None,
        lowsrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        tickwidth=None,
        uid=None,
        visible=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xsrc=None,
        yaxis=None,
        **kwargs
    ):
        """
        Construct a new Ohlc object
        
        The ohlc (short for Open-High-Low-Close) is a style of
        financial chart describing open, high, low and close for a
        given `x` coordinate (most likely time). The tip of the lines
        represent the `low` and `high` values and the horizontal
        segments represent the `open` and `close` values. Sample points
        where the close value is higher (lower) then the open value are
        called increasing (decreasing). By default, increasing items
        are drawn in green whereas decreasing are drawn in red.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Ohlc
        close
            Sets the close values.
        closesrc
            Sets the source reference on plot.ly for  close .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        decreasing
            plotly.graph_objs.ohlc.Decreasing instance or dict with
            compatible properties
        high
            Sets the high values.
        highsrc
            Sets the source reference on plot.ly for  high .
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.ohlc.Hoverlabel instance or dict with
            compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        increasing
            plotly.graph_objs.ohlc.Increasing instance or dict with
            compatible properties
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        line
            plotly.graph_objs.ohlc.Line instance or dict with
            compatible properties
        low
            Sets the low values.
        lowsrc
            Sets the source reference on plot.ly for  low .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        open
            Sets the open values.
        opensrc
            Sets the source reference on plot.ly for  open .
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
            plotly.graph_objs.ohlc.Stream instance or dict with
            compatible properties
        text
            Sets hover text elements associated with each sample
            point. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to this trace's sample points.
        textsrc
            Sets the source reference on plot.ly for  text .
        tickwidth
            Sets the width of the open/close tick marks relative to
            the "x" minimal interval.
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates. If absent, linear coordinate
            will be generated.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xsrc
            Sets the source reference on plot.ly for  x .
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.

        Returns
        -------
        Ohlc
        """
        super(Ohlc, self).__init__('ohlc')

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
The first argument to the plotly.graph_objs.Ohlc 
constructor must be a dict or 
an instance of plotly.graph_objs.Ohlc"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (ohlc as v_ohlc)

        # Initialize validators
        # ---------------------
        self._validators['close'] = v_ohlc.CloseValidator()
        self._validators['closesrc'] = v_ohlc.ClosesrcValidator()
        self._validators['customdata'] = v_ohlc.CustomdataValidator()
        self._validators['customdatasrc'] = v_ohlc.CustomdatasrcValidator()
        self._validators['decreasing'] = v_ohlc.DecreasingValidator()
        self._validators['high'] = v_ohlc.HighValidator()
        self._validators['highsrc'] = v_ohlc.HighsrcValidator()
        self._validators['hoverinfo'] = v_ohlc.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_ohlc.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_ohlc.HoverlabelValidator()
        self._validators['ids'] = v_ohlc.IdsValidator()
        self._validators['idssrc'] = v_ohlc.IdssrcValidator()
        self._validators['increasing'] = v_ohlc.IncreasingValidator()
        self._validators['legendgroup'] = v_ohlc.LegendgroupValidator()
        self._validators['line'] = v_ohlc.LineValidator()
        self._validators['low'] = v_ohlc.LowValidator()
        self._validators['lowsrc'] = v_ohlc.LowsrcValidator()
        self._validators['name'] = v_ohlc.NameValidator()
        self._validators['opacity'] = v_ohlc.OpacityValidator()
        self._validators['open'] = v_ohlc.OpenValidator()
        self._validators['opensrc'] = v_ohlc.OpensrcValidator()
        self._validators['selectedpoints'] = v_ohlc.SelectedpointsValidator()
        self._validators['showlegend'] = v_ohlc.ShowlegendValidator()
        self._validators['stream'] = v_ohlc.StreamValidator()
        self._validators['text'] = v_ohlc.TextValidator()
        self._validators['textsrc'] = v_ohlc.TextsrcValidator()
        self._validators['tickwidth'] = v_ohlc.TickwidthValidator()
        self._validators['uid'] = v_ohlc.UidValidator()
        self._validators['visible'] = v_ohlc.VisibleValidator()
        self._validators['x'] = v_ohlc.XValidator()
        self._validators['xaxis'] = v_ohlc.XAxisValidator()
        self._validators['xcalendar'] = v_ohlc.XcalendarValidator()
        self._validators['xsrc'] = v_ohlc.XsrcValidator()
        self._validators['yaxis'] = v_ohlc.YAxisValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('close', None)
        self['close'] = close if close is not None else _v
        _v = arg.pop('closesrc', None)
        self['closesrc'] = closesrc if closesrc is not None else _v
        _v = arg.pop('customdata', None)
        self['customdata'] = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self['customdatasrc'
            ] = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('decreasing', None)
        self['decreasing'] = decreasing if decreasing is not None else _v
        _v = arg.pop('high', None)
        self['high'] = high if high is not None else _v
        _v = arg.pop('highsrc', None)
        self['highsrc'] = highsrc if highsrc is not None else _v
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
        _v = arg.pop('increasing', None)
        self['increasing'] = increasing if increasing is not None else _v
        _v = arg.pop('legendgroup', None)
        self['legendgroup'] = legendgroup if legendgroup is not None else _v
        _v = arg.pop('line', None)
        self['line'] = line if line is not None else _v
        _v = arg.pop('low', None)
        self['low'] = low if low is not None else _v
        _v = arg.pop('lowsrc', None)
        self['lowsrc'] = lowsrc if lowsrc is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('open', None)
        self['open'] = open if open is not None else _v
        _v = arg.pop('opensrc', None)
        self['opensrc'] = opensrc if opensrc is not None else _v
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
        _v = arg.pop('tickwidth', None)
        self['tickwidth'] = tickwidth if tickwidth is not None else _v
        _v = arg.pop('uid', None)
        self['uid'] = uid if uid is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('xaxis', None)
        self['xaxis'] = xaxis if xaxis is not None else _v
        _v = arg.pop('xcalendar', None)
        self['xcalendar'] = xcalendar if xcalendar is not None else _v
        _v = arg.pop('xsrc', None)
        self['xsrc'] = xsrc if xsrc is not None else _v
        _v = arg.pop('yaxis', None)
        self['yaxis'] = yaxis if yaxis is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'ohlc'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='ohlc', val='ohlc'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
