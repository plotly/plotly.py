from plotly.basedatatypes import BaseTraceType
import copy


class Table(BaseTraceType):

    # cells
    # -----
    @property
    def cells(self):
        """
        The 'cells' property is an instance of Cells
        that may be specified as:
          - An instance of plotly.graph_objs.table.Cells
          - A dict of string/value properties that will be passed
            to the Cells constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the `text`
                    within the box. Has an effect only if `text`
                    spans more two or more lines (i.e. `text`
                    contains one or more <br> HTML tags) or if an
                    explicit width is set to override the text
                    width.
                alignsrc
                    Sets the source reference on plot.ly for  align
                    .
                fill
                    plotly.graph_objs.table.cells.Fill instance or
                    dict with compatible properties
                font
                    plotly.graph_objs.table.cells.Font instance or
                    dict with compatible properties
                format
                    Sets the cell value formatting rule using d3
                    formatting mini-language which is similar to
                    those of Python. See https://github.com/d3/d3-f
                    ormat/blob/master/README.md#locale_format
                formatsrc
                    Sets the source reference on plot.ly for
                    format .
                height
                    The height of cells.
                line
                    plotly.graph_objs.table.cells.Line instance or
                    dict with compatible properties
                prefix
                    Prefix for cell values.
                prefixsrc
                    Sets the source reference on plot.ly for
                    prefix .
                suffix
                    Suffix for cell values.
                suffixsrc
                    Sets the source reference on plot.ly for
                    suffix .
                values
                    Cell values. `values[m][n]` represents the
                    value of the `n`th point in column `m`,
                    therefore the `values[m]` vector length for all
                    columns must be the same (longer vectors will
                    be truncated). Each value must be a finite
                    number or a string.
                valuessrc
                    Sets the source reference on plot.ly for
                    values .

        Returns
        -------
        plotly.graph_objs.table.Cells
        """
        return self['cells']

    @cells.setter
    def cells(self, val):
        self['cells'] = val

    # columnorder
    # -----------
    @property
    def columnorder(self):
        """
        Specifies the rendered order of the data columns; for example,
        a value `2` at position `0` means that column index `0` in the
        data will be rendered as the third column, as columns have an
        index base of zero.
    
        The 'columnorder' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['columnorder']

    @columnorder.setter
    def columnorder(self, val):
        self['columnorder'] = val

    # columnordersrc
    # --------------
    @property
    def columnordersrc(self):
        """
        Sets the source reference on plot.ly for  columnorder .
    
        The 'columnordersrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['columnordersrc']

    @columnordersrc.setter
    def columnordersrc(self, val):
        self['columnordersrc'] = val

    # columnwidth
    # -----------
    @property
    def columnwidth(self):
        """
        The width of columns expressed as a ratio. Columns fill the
        available width in proportion of their specified column widths.
    
        The 'columnwidth' property is a number and may be specified as:
          - An int or float
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['columnwidth']

    @columnwidth.setter
    def columnwidth(self, val):
        self['columnwidth'] = val

    # columnwidthsrc
    # --------------
    @property
    def columnwidthsrc(self):
        """
        Sets the source reference on plot.ly for  columnwidth .
    
        The 'columnwidthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['columnwidthsrc']

    @columnwidthsrc.setter
    def columnwidthsrc(self, val):
        self['columnwidthsrc'] = val

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
          - An instance of plotly.graph_objs.table.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this table trace .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this table trace .
                x
                    Sets the horizontal domain of this table trace
                    (in plot fraction).
                y
                    Sets the vertical domain of this table trace
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.table.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # header
    # ------
    @property
    def header(self):
        """
        The 'header' property is an instance of Header
        that may be specified as:
          - An instance of plotly.graph_objs.table.Header
          - A dict of string/value properties that will be passed
            to the Header constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the `text`
                    within the box. Has an effect only if `text`
                    spans more two or more lines (i.e. `text`
                    contains one or more <br> HTML tags) or if an
                    explicit width is set to override the text
                    width.
                alignsrc
                    Sets the source reference on plot.ly for  align
                    .
                fill
                    plotly.graph_objs.table.header.Fill instance or
                    dict with compatible properties
                font
                    plotly.graph_objs.table.header.Font instance or
                    dict with compatible properties
                format
                    Sets the cell value formatting rule using d3
                    formatting mini-language which is similar to
                    those of Python. See https://github.com/d3/d3-f
                    ormat/blob/master/README.md#locale_format
                formatsrc
                    Sets the source reference on plot.ly for
                    format .
                height
                    The height of cells.
                line
                    plotly.graph_objs.table.header.Line instance or
                    dict with compatible properties
                prefix
                    Prefix for cell values.
                prefixsrc
                    Sets the source reference on plot.ly for
                    prefix .
                suffix
                    Suffix for cell values.
                suffixsrc
                    Sets the source reference on plot.ly for
                    suffix .
                values
                    Header cell values. `values[m][n]` represents
                    the value of the `n`th point in column `m`,
                    therefore the `values[m]` vector length for all
                    columns must be the same (longer vectors will
                    be truncated). Each value must be a finite
                    number or a string.
                valuessrc
                    Sets the source reference on plot.ly for
                    values .

        Returns
        -------
        plotly.graph_objs.table.Header
        """
        return self['header']

    @header.setter
    def header(self, val):
        self['header'] = val

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
          - An instance of plotly.graph_objs.table.Hoverlabel
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
        plotly.graph_objs.table.Hoverlabel
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
          - An instance of plotly.graph_objs.table.Stream
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
        plotly.graph_objs.table.Stream
        """
        return self['stream']

    @stream.setter
    def stream(self, val):
        self['stream'] = val

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
        cells
            plotly.graph_objs.table.Cells instance or dict with
            compatible properties
        columnorder
            Specifies the rendered order of the data columns; for
            example, a value `2` at position `0` means that column
            index `0` in the data will be rendered as the third
            column, as columns have an index base of zero.
        columnordersrc
            Sets the source reference on plot.ly for  columnorder .
        columnwidth
            The width of columns expressed as a ratio. Columns fill
            the available width in proportion of their specified
            column widths.
        columnwidthsrc
            Sets the source reference on plot.ly for  columnwidth .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.table.Domain instance or dict with
            compatible properties
        header
            plotly.graph_objs.table.Header instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.table.Hoverlabel instance or dict
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
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
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
            plotly.graph_objs.table.Stream instance or dict with
            compatible properties
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
        cells=None,
        columnorder=None,
        columnordersrc=None,
        columnwidth=None,
        columnwidthsrc=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        header=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legendgroup=None,
        name=None,
        opacity=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        uid=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Table object
        
        Table view for detailed data viewing. The data are arranged in
        a grid of rows and columns. Most styling can be specified for
        columns, rows or individual cells. Table is using a column-
        major order, ie. the grid is represented as a vector of column
        vectors.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Table
        cells
            plotly.graph_objs.table.Cells instance or dict with
            compatible properties
        columnorder
            Specifies the rendered order of the data columns; for
            example, a value `2` at position `0` means that column
            index `0` in the data will be rendered as the third
            column, as columns have an index base of zero.
        columnordersrc
            Sets the source reference on plot.ly for  columnorder .
        columnwidth
            The width of columns expressed as a ratio. Columns fill
            the available width in proportion of their specified
            column widths.
        columnwidthsrc
            Sets the source reference on plot.ly for  columnwidth .
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        domain
            plotly.graph_objs.table.Domain instance or dict with
            compatible properties
        header
            plotly.graph_objs.table.Header instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.table.Hoverlabel instance or dict
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
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
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
            plotly.graph_objs.table.Stream instance or dict with
            compatible properties
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Table
        """
        super(Table, self).__init__('table')

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
The first argument to the plotly.graph_objs.Table 
constructor must be a dict or 
an instance of plotly.graph_objs.Table"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (table as v_table)

        # Initialize validators
        # ---------------------
        self._validators['cells'] = v_table.CellsValidator()
        self._validators['columnorder'] = v_table.ColumnorderValidator()
        self._validators['columnordersrc'] = v_table.ColumnordersrcValidator()
        self._validators['columnwidth'] = v_table.ColumnwidthValidator()
        self._validators['columnwidthsrc'] = v_table.ColumnwidthsrcValidator()
        self._validators['customdata'] = v_table.CustomdataValidator()
        self._validators['customdatasrc'] = v_table.CustomdatasrcValidator()
        self._validators['domain'] = v_table.DomainValidator()
        self._validators['header'] = v_table.HeaderValidator()
        self._validators['hoverinfo'] = v_table.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_table.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_table.HoverlabelValidator()
        self._validators['ids'] = v_table.IdsValidator()
        self._validators['idssrc'] = v_table.IdssrcValidator()
        self._validators['legendgroup'] = v_table.LegendgroupValidator()
        self._validators['name'] = v_table.NameValidator()
        self._validators['opacity'] = v_table.OpacityValidator()
        self._validators['selectedpoints'] = v_table.SelectedpointsValidator()
        self._validators['showlegend'] = v_table.ShowlegendValidator()
        self._validators['stream'] = v_table.StreamValidator()
        self._validators['uid'] = v_table.UidValidator()
        self._validators['visible'] = v_table.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('cells', None)
        self['cells'] = cells if cells is not None else _v
        _v = arg.pop('columnorder', None)
        self['columnorder'] = columnorder if columnorder is not None else _v
        _v = arg.pop('columnordersrc', None)
        self['columnordersrc'
            ] = columnordersrc if columnordersrc is not None else _v
        _v = arg.pop('columnwidth', None)
        self['columnwidth'] = columnwidth if columnwidth is not None else _v
        _v = arg.pop('columnwidthsrc', None)
        self['columnwidthsrc'
            ] = columnwidthsrc if columnwidthsrc is not None else _v
        _v = arg.pop('customdata', None)
        self['customdata'] = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self['customdatasrc'
            ] = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('domain', None)
        self['domain'] = domain if domain is not None else _v
        _v = arg.pop('header', None)
        self['header'] = header if header is not None else _v
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
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self['opacity'] = opacity if opacity is not None else _v
        _v = arg.pop('selectedpoints', None)
        self['selectedpoints'
            ] = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self['showlegend'] = showlegend if showlegend is not None else _v
        _v = arg.pop('stream', None)
        self['stream'] = stream if stream is not None else _v
        _v = arg.pop('uid', None)
        self['uid'] = uid if uid is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'table'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='table', val='table'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
