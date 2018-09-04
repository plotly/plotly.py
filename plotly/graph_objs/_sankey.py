from plotly.basedatatypes import BaseTraceType
import copy


class Sankey(BaseTraceType):

    # arrangement
    # -----------
    @property
    def arrangement(self):
        """
        If value is `snap` (the default), the node arrangement is
        assisted by automatic snapping of elements to preserve space
        between nodes specified via `nodepad`. If value is
        `perpendicular`, the nodes can only move along a line
        perpendicular to the flow. If value is `freeform`, the nodes
        can freely move on the plane. If value is `fixed`, the nodes
        are stationary.
    
        The 'arrangement' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['snap', 'perpendicular', 'freeform', 'fixed']

        Returns
        -------
        Any
        """
        return self['arrangement']

    @arrangement.setter
    def arrangement(self, val):
        self['arrangement'] = val

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

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.sankey.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this sankey trace .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this sankey trace .
                x
                    Sets the horizontal domain of this sankey trace
                    (in plot fraction).
                y
                    Sets the vertical domain of this sankey trace
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.sankey.Domain
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
          - Any combination of ['label', 'text', 'value', 'percent', 'name'] joined with '+' characters
            (e.g. 'label+text')
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
          - An instance of plotly.graph_objs.sankey.Hoverlabel
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
        plotly.graph_objs.sankey.Hoverlabel
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

    # link
    # ----
    @property
    def link(self):
        """
        The links of the Sankey plot.
    
        The 'link' property is an instance of Link
        that may be specified as:
          - An instance of plotly.graph_objs.sankey.Link
          - A dict of string/value properties that will be passed
            to the Link constructor
    
            Supported dict properties:
                
                color
                    Sets the `link` color. It can be a single
                    value, or an array for specifying color for
                    each `link`. If `link.color` is omitted, then
                    by default, a translucent grey link will be
                    used.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                label
                    The shown name of the link.
                labelsrc
                    Sets the source reference on plot.ly for  label
                    .
                line
                    plotly.graph_objs.sankey.link.Line instance or
                    dict with compatible properties
                source
                    An integer number `[0..nodes.length - 1]` that
                    represents the source node.
                sourcesrc
                    Sets the source reference on plot.ly for
                    source .
                target
                    An integer number `[0..nodes.length - 1]` that
                    represents the target node.
                targetsrc
                    Sets the source reference on plot.ly for
                    target .
                value
                    A numeric value representing the flow volume
                    value.
                valuesrc
                    Sets the source reference on plot.ly for  value
                    .

        Returns
        -------
        plotly.graph_objs.sankey.Link
        """
        return self['link']

    @link.setter
    def link(self, val):
        self['link'] = val

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

    # node
    # ----
    @property
    def node(self):
        """
        The nodes of the Sankey plot.
    
        The 'node' property is an instance of Node
        that may be specified as:
          - An instance of plotly.graph_objs.sankey.Node
          - A dict of string/value properties that will be passed
            to the Node constructor
    
            Supported dict properties:
                
                color
                    Sets the `node` color. It can be a single
                    value, or an array for specifying color for
                    each `node`. If `node.color` is omitted, then
                    the default `Plotly` color palette will be
                    cycled through to have a variety of colors.
                    These defaults are not fully opaque, to allow
                    some visibility of what is beneath the node.
                colorsrc
                    Sets the source reference on plot.ly for  color
                    .
                label
                    The shown name of the node.
                labelsrc
                    Sets the source reference on plot.ly for  label
                    .
                line
                    plotly.graph_objs.sankey.node.Line instance or
                    dict with compatible properties
                pad
                    Sets the padding (in px) between the `nodes`.
                thickness
                    Sets the thickness (in px) of the `nodes`.

        Returns
        -------
        plotly.graph_objs.sankey.Node
        """
        return self['node']

    @node.setter
    def node(self, val):
        self['node'] = val

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
        Sets the orientation of the Sankey diagram.
    
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
          - An instance of plotly.graph_objs.sankey.Stream
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
        plotly.graph_objs.sankey.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        Sets the font for node labels
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.sankey.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
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
        plotly.graph_objs.sankey.Textfont
        """
        return self['textfont']

    @textfont.setter
    def textfont(self, val):
        self['textfont'] = val

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

    # valueformat
    # -----------
    @property
    def valueformat(self):
        """
        Sets the value formatting rule using d3 formatting mini-
        language which is similar to those of Python. See https://githu
        b.com/d3/d3-format/blob/master/README.md#locale_format
    
        The 'valueformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['valueformat']

    @valueformat.setter
    def valueformat(self, val):
        self['valueformat'] = val

    # valuesuffix
    # -----------
    @property
    def valuesuffix(self):
        """
        Adds a unit to follow the value in the hover tooltip. Add a
        space if a separation is necessary from the value.
    
        The 'valuesuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['valuesuffix']

    @valuesuffix.setter
    def valuesuffix(self, val):
        self['valuesuffix'] = val

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
        arrangement
            If value is `snap` (the default), the node arrangement
            is assisted by automatic snapping of elements to
            preserve space between nodes specified via `nodepad`.
            If value is `perpendicular`, the nodes can only move
            along a line perpendicular to the flow. If value is
            `freeform`, the nodes can freely move on the plane. If
            value is `fixed`, the nodes are stationary.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.sankey.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.sankey.Hoverlabel instance or dict
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
        link
            The links of the Sankey plot.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        node
            The nodes of the Sankey plot.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the Sankey diagram.
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
            plotly.graph_objs.sankey.Stream instance or dict with
            compatible properties
        textfont
            Sets the font for node labels
        uid

        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        valuesuffix
            Adds a unit to follow the value in the hover tooltip.
            Add a space if a separation is necessary from the
            value.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        """

    def __init__(
        self,
        arg=None,
        arrangement=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        link=None,
        name=None,
        node=None,
        opacity=None,
        orientation=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        textfont=None,
        uid=None,
        valueformat=None,
        valuesuffix=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Sankey object
        
        Sankey plots for network flow data analysis. The nodes are
        specified in `nodes` and the links between sources and targets
        in `links`. The colors are set in `nodes[i].color` and
        `links[i].color`; otherwise defaults are used.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Sankey
        arrangement
            If value is `snap` (the default), the node arrangement
            is assisted by automatic snapping of elements to
            preserve space between nodes specified via `nodepad`.
            If value is `perpendicular`, the nodes can only move
            along a line perpendicular to the flow. If value is
            `freeform`, the nodes can freely move on the plane. If
            value is `fixed`, the nodes are stationary.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.sankey.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.sankey.Hoverlabel instance or dict
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
        link
            The links of the Sankey plot.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        node
            The nodes of the Sankey plot.
        opacity
            Sets the opacity of the trace.
        orientation
            Sets the orientation of the Sankey diagram.
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
            plotly.graph_objs.sankey.Stream instance or dict with
            compatible properties
        textfont
            Sets the font for node labels
        uid

        valueformat
            Sets the value formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        valuesuffix
            Adds a unit to follow the value in the hover tooltip.
            Add a space if a separation is necessary from the
            value.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Sankey
        """
        super(Sankey, self).__init__('sankey')

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
The first argument to the plotly.graph_objs.Sankey 
constructor must be a dict or 
an instance of plotly.graph_objs.Sankey"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (sankey as v_sankey)

        # Initialize validators
        # ---------------------
        self._validators['arrangement'] = v_sankey.ArrangementValidator()
        self._validators['customdata'] = v_sankey.CustomdataValidator()
        self._validators['customdatasrc'] = v_sankey.CustomdatasrcValidator()
        self._validators['domain'] = v_sankey.DomainValidator()
        self._validators['hoverinfo'] = v_sankey.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_sankey.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_sankey.HoverlabelValidator()
        self._validators['ids'] = v_sankey.IdsValidator()
        self._validators['idssrc'] = v_sankey.IdssrcValidator()
        self._validators['legendgroup'] = v_sankey.LegendgroupValidator()
        self._validators['link'] = v_sankey.LinkValidator()
        self._validators['name'] = v_sankey.NameValidator()
        self._validators['node'] = v_sankey.NodeValidator()
        self._validators['opacity'] = v_sankey.OpacityValidator()
        self._validators['orientation'] = v_sankey.OrientationValidator()
        self._validators['selectedpoints'] = v_sankey.SelectedpointsValidator()
        self._validators['showlegend'] = v_sankey.ShowlegendValidator()
        self._validators['stream'] = v_sankey.StreamValidator()
        self._validators['textfont'] = v_sankey.TextfontValidator()
        self._validators['uid'] = v_sankey.UidValidator()
        self._validators['valueformat'] = v_sankey.ValueformatValidator()
        self._validators['valuesuffix'] = v_sankey.ValuesuffixValidator()
        self._validators['visible'] = v_sankey.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('arrangement', None)
        self.arrangement = arrangement if arrangement is not None else _v
        _v = arg.pop('customdata', None)
        self.customdata = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self.customdatasrc = customdatasrc if customdatasrc is not None else _v
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
        _v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup if legendgroup is not None else _v
        _v = arg.pop('link', None)
        self.link = link if link is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('node', None)
        self.node = node if node is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('orientation', None)
        self.orientation = orientation if orientation is not None else _v
        _v = arg.pop('selectedpoints', None)
        self.selectedpoints = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self.showlegend = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self.stream = stream if stream is not None else _v
        _v = arg.pop('textfont', None)
        self.textfont = textfont if textfont is not None else _v
        _v = arg.pop('uid', None)
        self.uid = uid if uid is not None else _v
        _v = arg.pop('valueformat', None)
        self.valueformat = valueformat if valueformat is not None else _v
        _v = arg.pop('valuesuffix', None)
        self.valuesuffix = valuesuffix if valuesuffix is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'sankey'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='sankey', val='sankey'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
