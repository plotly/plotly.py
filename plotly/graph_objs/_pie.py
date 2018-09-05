from plotly.basedatatypes import BaseTraceType
import copy


class Pie(BaseTraceType):

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

    # direction
    # ---------
    @property
    def direction(self):
        """
        Specifies the direction at which succeeding sectors follow one
        another.
    
        The 'direction' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['clockwise', 'counterclockwise']

        Returns
        -------
        Any
        """
        return self['direction']

    @direction.setter
    def direction(self, val):
        self['direction'] = val

    # dlabel
    # ------
    @property
    def dlabel(self):
        """
        Sets the label step. See `label0` for more info.
    
        The 'dlabel' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['dlabel']

    @dlabel.setter
    def dlabel(self, val):
        self['dlabel'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.pie.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this pie trace .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this pie trace .
                x
                    Sets the horizontal domain of this pie trace
                    (in plot fraction).
                y
                    Sets the vertical domain of this pie trace (in
                    plot fraction).

        Returns
        -------
        plotly.graph_objs.pie.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # hole
    # ----
    @property
    def hole(self):
        """
        Sets the fraction of the radius to cut out of the pie. Use this
        to make a donut chart.
    
        The 'hole' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['hole']

    @hole.setter
    def hole(self, val):
        self['hole'] = val

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
          - An instance of plotly.graph_objs.pie.Hoverlabel
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
        plotly.graph_objs.pie.Hoverlabel
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
        Sets hover text elements associated with each sector. If a
        single string, the same string appears for all data points. If
        an array of string, the items are mapped in order of this
        trace's sectors. To be seen, trace `hoverinfo` must contain a
        "text" flag.
    
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
        Sets the font used for `textinfo` lying inside the pie.
    
        The 'insidetextfont' property is an instance of Insidetextfont
        that may be specified as:
          - An instance of plotly.graph_objs.pie.Insidetextfont
          - A dict of string/value properties that will be passed
            to the Insidetextfont constructor
    
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
        plotly.graph_objs.pie.Insidetextfont
        """
        return self['insidetextfont']

    @insidetextfont.setter
    def insidetextfont(self, val):
        self['insidetextfont'] = val

    # label0
    # ------
    @property
    def label0(self):
        """
        Alternate to `labels`. Builds a numeric set of labels. Use with
        `dlabel` where `label0` is the starting label and `dlabel` the
        step.
    
        The 'label0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['label0']

    @label0.setter
    def label0(self, val):
        self['label0'] = val

    # labels
    # ------
    @property
    def labels(self):
        """
        Sets the sector labels. If `labels` entries are duplicated, we
        sum associated `values` or simply count occurrences if `values`
        is not provided. For other array attributes (including color)
        we use the first non-empty entry among all occurrences of the
        label.
    
        The 'labels' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['labels']

    @labels.setter
    def labels(self, val):
        self['labels'] = val

    # labelssrc
    # ---------
    @property
    def labelssrc(self):
        """
        Sets the source reference on plot.ly for  labels .
    
        The 'labelssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['labelssrc']

    @labelssrc.setter
    def labelssrc(self, val):
        self['labelssrc'] = val

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
          - An instance of plotly.graph_objs.pie.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                colors
                    Sets the color of each sector of this pie
                    chart. If not specified, the default trace
                    color set is used to pick the sector colors.
                colorssrc
                    Sets the source reference on plot.ly for
                    colors .
                line
                    plotly.graph_objs.pie.marker.Line instance or
                    dict with compatible properties

        Returns
        -------
        plotly.graph_objs.pie.Marker
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

    # outsidetextfont
    # ---------------
    @property
    def outsidetextfont(self):
        """
        Sets the font used for `textinfo` lying outside the pie.
    
        The 'outsidetextfont' property is an instance of Outsidetextfont
        that may be specified as:
          - An instance of plotly.graph_objs.pie.Outsidetextfont
          - A dict of string/value properties that will be passed
            to the Outsidetextfont constructor
    
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
        plotly.graph_objs.pie.Outsidetextfont
        """
        return self['outsidetextfont']

    @outsidetextfont.setter
    def outsidetextfont(self, val):
        self['outsidetextfont'] = val

    # pull
    # ----
    @property
    def pull(self):
        """
        Sets the fraction of larger radius to pull the sectors out from
        the center. This can be a constant to pull all slices apart
        from each other equally or an array to highlight one or more
        slices.
    
        The 'pull' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['pull']

    @pull.setter
    def pull(self, val):
        self['pull'] = val

    # pullsrc
    # -------
    @property
    def pullsrc(self):
        """
        Sets the source reference on plot.ly for  pull .
    
        The 'pullsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['pullsrc']

    @pullsrc.setter
    def pullsrc(self, val):
        self['pullsrc'] = val

    # rotation
    # --------
    @property
    def rotation(self):
        """
        Instead of the first slice starting at 12 o'clock, rotate to
        some other angle.
    
        The 'rotation' property is a number and may be specified as:
          - An int or float in the interval [-360, 360]

        Returns
        -------
        int|float
        """
        return self['rotation']

    @rotation.setter
    def rotation(self, val):
        self['rotation'] = val

    # scalegroup
    # ----------
    @property
    def scalegroup(self):
        """
        If there are multiple pies that should be sized according to
        their totals, link them by providing a non-empty group id here
        shared by every trace in the same group.
    
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

    # sort
    # ----
    @property
    def sort(self):
        """
        Determines whether or not the sectors are reordered from
        largest to smallest.
    
        The 'sort' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['sort']

    @sort.setter
    def sort(self, val):
        self['sort'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.pie.Stream
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
        plotly.graph_objs.pie.Stream
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
        Sets text elements associated with each sector. If trace
        `textinfo` contains a "text" flag, these elements will seen on
        the chart. If trace `hoverinfo` contains a "text" flag and
        "hovertext" is not set, these elements will be seen in the
        hover labels.
    
        The 'text' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
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
        Sets the font used for `textinfo`.
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.pie.Textfont
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
        plotly.graph_objs.pie.Textfont
        """
        return self['textfont']

    @textfont.setter
    def textfont(self, val):
        self['textfont'] = val

    # textinfo
    # --------
    @property
    def textinfo(self):
        """
        Determines which trace information appear on the graph.
    
        The 'textinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['label', 'text', 'value', 'percent'] joined with '+' characters
            (e.g. 'label+text')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self['textinfo']

    @textinfo.setter
    def textinfo(self, val):
        self['textinfo'] = val

    # textposition
    # ------------
    @property
    def textposition(self):
        """
        Specifies the location of the `textinfo`.
    
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

    # values
    # ------
    @property
    def values(self):
        """
        Sets the values of the sectors of this pie chart. If omitted,
        we count occurrences of each label.
    
        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['values']

    @values.setter
    def values(self, val):
        self['values'] = val

    # valuessrc
    # ---------
    @property
    def valuessrc(self):
        """
        Sets the source reference on plot.ly for  values .
    
        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['valuessrc']

    @valuessrc.setter
    def valuessrc(self, val):
        self['valuessrc'] = val

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
        direction
            Specifies the direction at which succeeding sectors
            follow one another.
        dlabel
            Sets the label step. See `label0` for more info.
        domain
            plotly.graph_objs.pie.Domain instance or dict with
            compatible properties
        hole
            Sets the fraction of the radius to cut out of the pie.
            Use this to make a donut chart.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.pie.Hoverlabel instance or dict with
            compatible properties
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the pie.
        label0
            Alternate to `labels`. Builds a numeric set of labels.
            Use with `dlabel` where `label0` is the starting label
            and `dlabel` the step.
        labels
            Sets the sector labels. If `labels` entries are
            duplicated, we sum associated `values` or simply count
            occurrences if `values` is not provided. For other
            array attributes (including color) we use the first
            non-empty entry among all occurrences of the label.
        labelssrc
            Sets the source reference on plot.ly for  labels .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.pie.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            pie.
        pull
            Sets the fraction of larger radius to pull the sectors
            out from the center. This can be a constant to pull all
            slices apart from each other equally or an array to
            highlight one or more slices.
        pullsrc
            Sets the source reference on plot.ly for  pull .
        rotation
            Instead of the first slice starting at 12 o'clock,
            rotate to some other angle.
        scalegroup
            If there are multiple pies that should be sized
            according to their totals, link them by providing a
            non-empty group id here shared by every trace in the
            same group.
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
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            plotly.graph_objs.pie.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will seen on the chart. If trace `hoverinfo` contains a
            "text" flag and "hovertext" is not set, these elements
            will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Specifies the location of the `textinfo`.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        values
            Sets the values of the sectors of this pie chart. If
            omitted, we count occurrences of each label.
        valuessrc
            Sets the source reference on plot.ly for  values .
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
        direction=None,
        dlabel=None,
        domain=None,
        hole=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legendgroup=None,
        marker=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        pull=None,
        pullsrc=None,
        rotation=None,
        scalegroup=None,
        selectedpoints=None,
        showlegend=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        uid=None,
        values=None,
        valuessrc=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Pie object
        
        A data visualized by the sectors of the pie is set in `values`.
        The sector labels are set in `labels`. The sector colors are
        set in `marker.colors`

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Pie
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on plot.ly for  customdata .
        direction
            Specifies the direction at which succeeding sectors
            follow one another.
        dlabel
            Sets the label step. See `label0` for more info.
        domain
            plotly.graph_objs.pie.Domain instance or dict with
            compatible properties
        hole
            Sets the fraction of the radius to cut out of the pie.
            Use this to make a donut chart.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on plot.ly for  hoverinfo .
        hoverlabel
            plotly.graph_objs.pie.Hoverlabel instance or dict with
            compatible properties
        hovertext
            Sets hover text elements associated with each sector.
            If a single string, the same string appears for all
            data points. If an array of string, the items are
            mapped in order of this trace's sectors. To be seen,
            trace `hoverinfo` must contain a "text" flag.
        hovertextsrc
            Sets the source reference on plot.ly for  hovertext .
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on plot.ly for  ids .
        insidetextfont
            Sets the font used for `textinfo` lying inside the pie.
        label0
            Alternate to `labels`. Builds a numeric set of labels.
            Use with `dlabel` where `label0` is the starting label
            and `dlabel` the step.
        labels
            Sets the sector labels. If `labels` entries are
            duplicated, we sum associated `values` or simply count
            occurrences if `values` is not provided. For other
            array attributes (including color) we use the first
            non-empty entry among all occurrences of the label.
        labelssrc
            Sets the source reference on plot.ly for  labels .
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        marker
            plotly.graph_objs.pie.Marker instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the trace.
        outsidetextfont
            Sets the font used for `textinfo` lying outside the
            pie.
        pull
            Sets the fraction of larger radius to pull the sectors
            out from the center. This can be a constant to pull all
            slices apart from each other equally or an array to
            highlight one or more slices.
        pullsrc
            Sets the source reference on plot.ly for  pull .
        rotation
            Instead of the first slice starting at 12 o'clock,
            rotate to some other angle.
        scalegroup
            If there are multiple pies that should be sized
            according to their totals, link them by providing a
            non-empty group id here shared by every trace in the
            same group.
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
        sort
            Determines whether or not the sectors are reordered
            from largest to smallest.
        stream
            plotly.graph_objs.pie.Stream instance or dict with
            compatible properties
        text
            Sets text elements associated with each sector. If
            trace `textinfo` contains a "text" flag, these elements
            will seen on the chart. If trace `hoverinfo` contains a
            "text" flag and "hovertext" is not set, these elements
            will be seen in the hover labels.
        textfont
            Sets the font used for `textinfo`.
        textinfo
            Determines which trace information appear on the graph.
        textposition
            Specifies the location of the `textinfo`.
        textpositionsrc
            Sets the source reference on plot.ly for  textposition
            .
        textsrc
            Sets the source reference on plot.ly for  text .
        uid

        values
            Sets the values of the sectors of this pie chart. If
            omitted, we count occurrences of each label.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Pie
        """
        super(Pie, self).__init__('pie')

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
The first argument to the plotly.graph_objs.Pie 
constructor must be a dict or 
an instance of plotly.graph_objs.Pie"""
            )

        # Import validators
        # -----------------
        from plotly.validators import (pie as v_pie)

        # Initialize validators
        # ---------------------
        self._validators['customdata'] = v_pie.CustomdataValidator()
        self._validators['customdatasrc'] = v_pie.CustomdatasrcValidator()
        self._validators['direction'] = v_pie.DirectionValidator()
        self._validators['dlabel'] = v_pie.DlabelValidator()
        self._validators['domain'] = v_pie.DomainValidator()
        self._validators['hole'] = v_pie.HoleValidator()
        self._validators['hoverinfo'] = v_pie.HoverinfoValidator()
        self._validators['hoverinfosrc'] = v_pie.HoverinfosrcValidator()
        self._validators['hoverlabel'] = v_pie.HoverlabelValidator()
        self._validators['hovertext'] = v_pie.HovertextValidator()
        self._validators['hovertextsrc'] = v_pie.HovertextsrcValidator()
        self._validators['ids'] = v_pie.IdsValidator()
        self._validators['idssrc'] = v_pie.IdssrcValidator()
        self._validators['insidetextfont'] = v_pie.InsidetextfontValidator()
        self._validators['label0'] = v_pie.Label0Validator()
        self._validators['labels'] = v_pie.LabelsValidator()
        self._validators['labelssrc'] = v_pie.LabelssrcValidator()
        self._validators['legendgroup'] = v_pie.LegendgroupValidator()
        self._validators['marker'] = v_pie.MarkerValidator()
        self._validators['name'] = v_pie.NameValidator()
        self._validators['opacity'] = v_pie.OpacityValidator()
        self._validators['outsidetextfont'] = v_pie.OutsidetextfontValidator()
        self._validators['pull'] = v_pie.PullValidator()
        self._validators['pullsrc'] = v_pie.PullsrcValidator()
        self._validators['rotation'] = v_pie.RotationValidator()
        self._validators['scalegroup'] = v_pie.ScalegroupValidator()
        self._validators['selectedpoints'] = v_pie.SelectedpointsValidator()
        self._validators['showlegend'] = v_pie.ShowlegendValidator()
        self._validators['sort'] = v_pie.SortValidator()
        self._validators['stream'] = v_pie.StreamValidator()
        self._validators['text'] = v_pie.TextValidator()
        self._validators['textfont'] = v_pie.TextfontValidator()
        self._validators['textinfo'] = v_pie.TextinfoValidator()
        self._validators['textposition'] = v_pie.TextpositionValidator()
        self._validators['textpositionsrc'] = v_pie.TextpositionsrcValidator()
        self._validators['textsrc'] = v_pie.TextsrcValidator()
        self._validators['uid'] = v_pie.UidValidator()
        self._validators['values'] = v_pie.ValuesValidator()
        self._validators['valuessrc'] = v_pie.ValuessrcValidator()
        self._validators['visible'] = v_pie.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('customdata', None)
        self.customdata = customdata if customdata is not None else _v
        _v = arg.pop('customdatasrc', None)
        self.customdatasrc = customdatasrc if customdatasrc is not None else _v
        _v = arg.pop('direction', None)
        self.direction = direction if direction is not None else _v
        _v = arg.pop('dlabel', None)
        self.dlabel = dlabel if dlabel is not None else _v
        _v = arg.pop('domain', None)
        self.domain = domain if domain is not None else _v
        _v = arg.pop('hole', None)
        self.hole = hole if hole is not None else _v
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
        _v = arg.pop('label0', None)
        self.label0 = label0 if label0 is not None else _v
        _v = arg.pop('labels', None)
        self.labels = labels if labels is not None else _v
        _v = arg.pop('labelssrc', None)
        self.labelssrc = labelssrc if labelssrc is not None else _v
        _v = arg.pop('legendgroup', None)
        self.legendgroup = legendgroup if legendgroup is not None else _v
        _v = arg.pop('marker', None)
        self.marker = marker if marker is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('outsidetextfont', None)
        self.outsidetextfont = outsidetextfont if outsidetextfont is not None else _v
        _v = arg.pop('pull', None)
        self.pull = pull if pull is not None else _v
        _v = arg.pop('pullsrc', None)
        self.pullsrc = pullsrc if pullsrc is not None else _v
        _v = arg.pop('rotation', None)
        self.rotation = rotation if rotation is not None else _v
        _v = arg.pop('scalegroup', None)
        self.scalegroup = scalegroup if scalegroup is not None else _v
        _v = arg.pop('selectedpoints', None)
        self.selectedpoints = selectedpoints if selectedpoints is not None else _v
        _v = arg.pop('showlegend', None)
        self.showlegend = showlegend if showlegend is not None else _v
        _v = arg.pop('sort', None)
        self.sort = sort if sort is not None else _v
        _v = arg.pop('stream', None)
        self.stream = stream if stream is not None else _v
        _v = arg.pop('text', None)
        self.text = text if text is not None else _v
        _v = arg.pop('textfont', None)
        self.textfont = textfont if textfont is not None else _v
        _v = arg.pop('textinfo', None)
        self.textinfo = textinfo if textinfo is not None else _v
        _v = arg.pop('textposition', None)
        self.textposition = textposition if textposition is not None else _v
        _v = arg.pop('textpositionsrc', None)
        self.textpositionsrc = textpositionsrc if textpositionsrc is not None else _v
        _v = arg.pop('textsrc', None)
        self.textsrc = textsrc if textsrc is not None else _v
        _v = arg.pop('uid', None)
        self.uid = uid if uid is not None else _v
        _v = arg.pop('values', None)
        self.values = values if values is not None else _v
        _v = arg.pop('valuessrc', None)
        self.valuessrc = valuessrc if valuessrc is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'pie'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='pie', val='pie'
        )

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
