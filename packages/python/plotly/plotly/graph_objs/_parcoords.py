from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Parcoords(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ""
    _path_str = "parcoords"
    _valid_props = {
        "customdata",
        "customdatasrc",
        "dimensions",
        "domain",
        "ids",
        "idssrc",
        "labelangle",
        "labelfont",
        "labelside",
        "line",
        "meta",
        "metasrc",
        "name",
        "rangefont",
        "stream",
        "tickfont",
        "type",
        "uid",
        "uirevision",
        "visible",
    }

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
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  customdata
        .
    
        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    # dimensions
    # ----------
    @property
    def dimensions(self):
        """
        The 'dimensions' property is an instance of Dimensions
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Dimensions`
          - A dict of string/value properties that will be passed
            to the Dimensions constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.parcoords.Dimensions
        """
        return self["dimensions"]

    @dimensions.setter
    def dimensions(self, val):
        self["dimensions"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Domain`
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
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

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
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  ids .
    
        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    # labelangle
    # ----------
    @property
    def labelangle(self):
        """
        Sets the angle of the labels with respect to the horizontal.
        For example, a `tickangle` of -90 draws the labels vertically.
        Tilted labels with "labelangle" may be positioned better inside
        margins when `labelposition` is set to "bottom".
    
        The 'labelangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self["labelangle"]

    @labelangle.setter
    def labelangle(self, val):
        self["labelangle"] = val

    # labelfont
    # ---------
    @property
    def labelfont(self):
        """
        Sets the font for the `dimension` labels.
    
        The 'labelfont' property is an instance of Labelfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Labelfont`
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
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.parcoords.Labelfont
        """
        return self["labelfont"]

    @labelfont.setter
    def labelfont(self, val):
        self["labelfont"] = val

    # labelside
    # ---------
    @property
    def labelside(self):
        """
        Specifies the location of the `label`. "top" positions labels
        above, next to the title "bottom" positions labels below the
        graph Tilted labels with "labelangle" may be positioned better
        inside margins when `labelposition` is set to "bottom".
    
        The 'labelside' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'bottom']

        Returns
        -------
        Any
        """
        return self["labelside"]

    @labelside.setter
    def labelside(self, val):
        self["labelside"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Line`
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
                cmid
                    Sets the mid-point of the color domain by
                    scaling `line.cmin` and/or `line.cmax` to be
                    equidistant to this point. Has an effect only
                    if in `line.color`is set to a numerical array.
                    Value should have the same units as in
                    `line.color`. Has no effect when `line.cauto`
                    is `false`.
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
                coloraxis
                    Sets a reference to a shared color axis.
                    References to these shared color axes are
                    "coloraxis", "coloraxis2", "coloraxis3", etc.
                    Settings for these shared color axes are set in
                    the layout, under `layout.coloraxis`,
                    `layout.coloraxis2`, etc. Note that multiple
                    color scales can be linked to the same color
                    axis.
                colorbar
                    :class:`plotly.graph_objects.parcoords.line.Col
                    orBar` instance or dict with compatible
                    properties
                colorscale
                    Sets the colorscale. Has an effect only if in
                    `line.color`is set to a numerical array. The
                    colorscale must be an array containing arrays
                    mapping a normalized value to an rgb, rgba,
                    hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                    To control the bounds of the colorscale in
                    color space, use`line.cmin` and `line.cmax`.
                    Alternatively, `colorscale` may be a palette
                    name string of the following list: Greys,YlGnBu
                    ,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,R
                    ainbow,Portland,Jet,Hot,Blackbody,Earth,Electri
                    c,Viridis,Cividis.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for  color .
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
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # meta
    # ----
    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.
    
        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    # metasrc
    # -------
    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  meta .
    
        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

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
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # rangefont
    # ---------
    @property
    def rangefont(self):
        """
        Sets the font for the `dimension` range values.
    
        The 'rangefont' property is an instance of Rangefont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Rangefont`
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
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.parcoords.Rangefont
        """
        return self["rangefont"]

    @rangefont.setter
    def rangefont(self, val):
        self["rangefont"] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Stream`
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
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.parcoords.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the font for the `dimension` tick values.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcoords.Tickfont`
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
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.parcoords.Tickfont
        """
        return self["tickfont"]

    @tickfont.setter
    def tickfont(self, val):
        self["tickfont"] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.
    
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

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
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # type
    # ----
    @property
    def type(self):
        return self._props["type"]

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
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dimensions
            :class:`plotly.graph_objects.parcoords.Dimensions`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.parcoords.Domain` instance
            or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        labelangle
            Sets the angle of the labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            labels vertically. Tilted labels with "labelangle" may
            be positioned better inside margins when
            `labelposition` is set to "bottom".
        labelfont
            Sets the font for the `dimension` labels.
        labelside
            Specifies the location of the `label`. "top" positions
            labels above, next to the title "bottom" positions
            labels below the graph Tilted labels with "labelangle"
            may be positioned better inside margins when
            `labelposition` is set to "bottom".
        line
            :class:`plotly.graph_objects.parcoords.Line` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        rangefont
            Sets the font for the `dimension` range values.
        stream
            :class:`plotly.graph_objects.parcoords.Stream` instance
            or dict with compatible properties
        tickfont
            Sets the font for the `dimension` tick values.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
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
        ids=None,
        idssrc=None,
        labelangle=None,
        labelfont=None,
        labelside=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        rangefont=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
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
            an instance of :class:`plotly.graph_objs.Parcoords`
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            customdata .
        dimensions
            :class:`plotly.graph_objects.parcoords.Dimensions`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.parcoords.Domain` instance
            or dict with compatible properties
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            ids .
        labelangle
            Sets the angle of the labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            labels vertically. Tilted labels with "labelangle" may
            be positioned better inside margins when
            `labelposition` is set to "bottom".
        labelfont
            Sets the font for the `dimension` labels.
        labelside
            Specifies the location of the `label`. "top" positions
            labels above, next to the title "bottom" positions
            labels below the graph Tilted labels with "labelangle"
            may be positioned better inside margins when
            `labelposition` is set to "bottom".
        line
            :class:`plotly.graph_objects.parcoords.Line` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            meta .
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        rangefont
            Sets the font for the `dimension` range values.
        stream
            :class:`plotly.graph_objects.parcoords.Stream` instance
            or dict with compatible properties
        tickfont
            Sets the font for the `dimension` tick values.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Parcoords
        """
        super(Parcoords, self).__init__("parcoords")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Parcoords 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.Parcoords`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("dimensions", None)
        _v = dimensions if dimensions is not None else _v
        if _v is not None:
            self["dimensions"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
        _v = arg.pop("labelangle", None)
        _v = labelangle if labelangle is not None else _v
        if _v is not None:
            self["labelangle"] = _v
        _v = arg.pop("labelfont", None)
        _v = labelfont if labelfont is not None else _v
        if _v is not None:
            self["labelfont"] = _v
        _v = arg.pop("labelside", None)
        _v = labelside if labelside is not None else _v
        if _v is not None:
            self["labelside"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("rangefont", None)
        _v = rangefont if rangefont is not None else _v
        if _v is not None:
            self["rangefont"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("tickfont", None)
        _v = tickfont if tickfont is not None else _v
        if _v is not None:
            self["tickfont"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v

        # Read-only literals
        # ------------------

        self._props["type"] = "parcoords"
        arg.pop("type", None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
