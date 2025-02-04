

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Link(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'sankey'
    _path_str = 'sankey.link'
    _valid_props = {"arrowlen", "color", "colorscaledefaults", "colorscales", "colorsrc", "customdata", "customdatasrc", "hovercolor", "hovercolorsrc", "hoverinfo", "hoverlabel", "hovertemplate", "hovertemplatesrc", "label", "labelsrc", "line", "source", "sourcesrc", "target", "targetsrc", "value", "valuesrc"}

    # arrowlen
    # --------
    @property
    def arrowlen(self):
        """
        Sets the length (in px) of the links arrow, if 0 no arrow will
        be drawn.

        The 'arrowlen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['arrowlen']

    @arrowlen.setter
    def arrowlen(self, val):
        self['arrowlen'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the `link` color. It can be a single value, or an array
        for specifying color for each `link`. If `link.color` is
        omitted, then by default, a translucent grey link will be used.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorscales
    # -----------
    @property
    def colorscales(self):
        """
        The 'colorscales' property is a tuple of instances of
        Colorscale that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.sankey.link.Colorscale
          - A list or tuple of dicts of string/value properties that
            will be passed to the Colorscale constructor

        Returns
        -------
        tuple[plotly.graph_objs.sankey.link.Colorscale]
        """
        return self['colorscales']

    @colorscales.setter
    def colorscales(self, val):
        self['colorscales'] = val

    # colorscaledefaults
    # ------------------
    @property
    def colorscaledefaults(self):
        """
        When used in a template (as
        layout.template.data.sankey.link.colorscaledefaults), sets the
        default property values to use for elements of
        sankey.link.colorscales

        The 'colorscaledefaults' property is an instance of Colorscale
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Colorscale`
          - A dict of string/value properties that will be passed
            to the Colorscale constructor

        Returns
        -------
        plotly.graph_objs.sankey.link.Colorscale
        """
        return self['colorscaledefaults']

    @colorscaledefaults.setter
    def colorscaledefaults(self, val):
        self['colorscaledefaults'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data to each link.

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
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

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

    # hovercolor
    # ----------
    @property
    def hovercolor(self):
        """
        Sets the `link` hover color. It can be a single value, or an
        array for specifying hover colors for each `link`. If
        `link.hovercolor` is omitted, then by default, links will
        become slightly more opaque when hovered over.

        The 'hovercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['hovercolor']

    @hovercolor.setter
    def hovercolor(self, val):
        self['hovercolor'] = val

    # hovercolorsrc
    # -------------
    @property
    def hovercolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovercolor`.

        The 'hovercolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hovercolorsrc']

    @hovercolorsrc.setter
    def hovercolorsrc(self, val):
        self['hovercolorsrc'] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear when hovering links.
        If `none` or `skip` are set, no information is displayed upon
        hovering. But, if `none` is set, click and hover events are
        still fired.

        The 'hoverinfo' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'none', 'skip']

        Returns
        -------
        Any
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.sankey.link.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # hovertemplate
    # -------------
    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available.  Variables
        `source` and `target` are node objects.Finally, the template
        string has access to variables `value` and `label`. Anything
        contained in tag `<extra>` is displayed in the secondary box,
        for example "<extra>{fullData.name}</extra>". To hide the
        secondary box completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['hovertemplate']

    @hovertemplate.setter
    def hovertemplate(self, val):
        self['hovertemplate'] = val

    # hovertemplatesrc
    # ----------------
    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['hovertemplatesrc']

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self['hovertemplatesrc'] = val

    # label
    # -----
    @property
    def label(self):
        """
        The shown name of the link.

        The 'label' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['label']

    @label.setter
    def label(self, val):
        self['label'] = val

    # labelsrc
    # --------
    @property
    def labelsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `label`.

        The 'labelsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['labelsrc']

    @labelsrc.setter
    def labelsrc(self, val):
        self['labelsrc'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.sankey.link.Line
        """
        return self['line']

    @line.setter
    def line(self, val):
        self['line'] = val

    # source
    # ------
    @property
    def source(self):
        """
        An integer number `[0..nodes.length - 1]` that represents the
        source node.

        The 'source' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['source']

    @source.setter
    def source(self, val):
        self['source'] = val

    # sourcesrc
    # ---------
    @property
    def sourcesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `source`.

        The 'sourcesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['sourcesrc']

    @sourcesrc.setter
    def sourcesrc(self, val):
        self['sourcesrc'] = val

    # target
    # ------
    @property
    def target(self):
        """
        An integer number `[0..nodes.length - 1]` that represents the
        target node.

        The 'target' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['target']

    @target.setter
    def target(self, val):
        self['target'] = val

    # targetsrc
    # ---------
    @property
    def targetsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `target`.

        The 'targetsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['targetsrc']

    @targetsrc.setter
    def targetsrc(self, val):
        self['targetsrc'] = val

    # value
    # -----
    @property
    def value(self):
        """
        A numeric value representing the flow volume value.

        The 'value' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # valuesrc
    # --------
    @property
    def valuesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `value`.

        The 'valuesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['valuesrc']

    @valuesrc.setter
    def valuesrc(self, val):
        self['valuesrc'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        arrowlen
            Sets the length (in px) of the links arrow, if 0 no
            arrow will be drawn.
        color
            Sets the `link` color. It can be a single value, or an
            array for specifying color for each `link`. If
            `link.color` is omitted, then by default, a translucent
            grey link will be used.
        colorscales
            A tuple of
            :class:`plotly.graph_objects.sankey.link.Colorscale`
            instances or dicts with compatible properties
        colorscaledefaults
            When used in a template (as
            layout.template.data.sankey.link.colorscaledefaults),
            sets the default property values to use for elements of
            sankey.link.colorscales
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        customdata
            Assigns extra data to each link.
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hovercolor
            Sets the `link` hover color. It can be a single value,
            or an array for specifying hover colors for each
            `link`. If `link.hovercolor` is omitted, then by
            default, links will become slightly more opaque when
            hovered over.
        hovercolorsrc
            Sets the source reference on Chart Studio Cloud for
            `hovercolor`.
        hoverinfo
            Determines which trace information appear when hovering
            links. If `none` or `skip` are set, no information is
            displayed upon hovering. But, if `none` is set, click
            and hover events are still fired.
        hoverlabel
            :class:`plotly.graph_objects.sankey.link.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Variables `source` and `target` are
            node objects.Finally, the template string has access to
            variables `value` and `label`. Anything contained in
            tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        label
            The shown name of the link.
        labelsrc
            Sets the source reference on Chart Studio Cloud for
            `label`.
        line
            :class:`plotly.graph_objects.sankey.link.Line` instance
            or dict with compatible properties
        source
            An integer number `[0..nodes.length - 1]` that
            represents the source node.
        sourcesrc
            Sets the source reference on Chart Studio Cloud for
            `source`.
        target
            An integer number `[0..nodes.length - 1]` that
            represents the target node.
        targetsrc
            Sets the source reference on Chart Studio Cloud for
            `target`.
        value
            A numeric value representing the flow volume value.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            `value`.
        """
    def __init__(self,
            arg=None,
            arrowlen=None,
            color=None,
            colorscales=None,
            colorscaledefaults=None,
            colorsrc=None,
            customdata=None,
            customdatasrc=None,
            hovercolor=None,
            hovercolorsrc=None,
            hoverinfo=None,
            hoverlabel=None,
            hovertemplate=None,
            hovertemplatesrc=None,
            label=None,
            labelsrc=None,
            line=None,
            source=None,
            sourcesrc=None,
            target=None,
            targetsrc=None,
            value=None,
            valuesrc=None,
            **kwargs
        ):
        """
        Construct a new Link object

        The links of the Sankey plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.sankey.Link`
        arrowlen
            Sets the length (in px) of the links arrow, if 0 no
            arrow will be drawn.
        color
            Sets the `link` color. It can be a single value, or an
            array for specifying color for each `link`. If
            `link.color` is omitted, then by default, a translucent
            grey link will be used.
        colorscales
            A tuple of
            :class:`plotly.graph_objects.sankey.link.Colorscale`
            instances or dicts with compatible properties
        colorscaledefaults
            When used in a template (as
            layout.template.data.sankey.link.colorscaledefaults),
            sets the default property values to use for elements of
            sankey.link.colorscales
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        customdata
            Assigns extra data to each link.
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hovercolor
            Sets the `link` hover color. It can be a single value,
            or an array for specifying hover colors for each
            `link`. If `link.hovercolor` is omitted, then by
            default, links will become slightly more opaque when
            hovered over.
        hovercolorsrc
            Sets the source reference on Chart Studio Cloud for
            `hovercolor`.
        hoverinfo
            Determines which trace information appear when hovering
            links. If `none` or `skip` are set, no information is
            displayed upon hovering. But, if `none` is set, click
            and hover events are still fired.
        hoverlabel
            :class:`plotly.graph_objects.sankey.link.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Variables `source` and `target` are
            node objects.Finally, the template string has access to
            variables `value` and `label`. Anything contained in
            tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        label
            The shown name of the link.
        labelsrc
            Sets the source reference on Chart Studio Cloud for
            `label`.
        line
            :class:`plotly.graph_objects.sankey.link.Line` instance
            or dict with compatible properties
        source
            An integer number `[0..nodes.length - 1]` that
            represents the source node.
        sourcesrc
            Sets the source reference on Chart Studio Cloud for
            `source`.
        target
            An integer number `[0..nodes.length - 1]` that
            represents the target node.
        targetsrc
            Sets the source reference on Chart Studio Cloud for
            `target`.
        value
            A numeric value representing the flow volume value.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            `value`.

        Returns
        -------
        Link
        """
        super().__init__('link')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
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
            raise ValueError("""\
The first argument to the plotly.graph_objs.sankey.Link
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sankey.Link`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('arrowlen', arg, arrowlen)
        self._init_provided('color', arg, color)
        self._init_provided('colorscales', arg, colorscales)
        self._init_provided('colorscaledefaults', arg, colorscaledefaults)
        self._init_provided('colorsrc', arg, colorsrc)
        self._init_provided('customdata', arg, customdata)
        self._init_provided('customdatasrc', arg, customdatasrc)
        self._init_provided('hovercolor', arg, hovercolor)
        self._init_provided('hovercolorsrc', arg, hovercolorsrc)
        self._init_provided('hoverinfo', arg, hoverinfo)
        self._init_provided('hoverlabel', arg, hoverlabel)
        self._init_provided('hovertemplate', arg, hovertemplate)
        self._init_provided('hovertemplatesrc', arg, hovertemplatesrc)
        self._init_provided('label', arg, label)
        self._init_provided('labelsrc', arg, labelsrc)
        self._init_provided('line', arg, line)
        self._init_provided('source', arg, source)
        self._init_provided('sourcesrc', arg, sourcesrc)
        self._init_provided('target', arg, target)
        self._init_provided('targetsrc', arg, targetsrc)
        self._init_provided('value', arg, value)
        self._init_provided('valuesrc', arg, valuesrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
