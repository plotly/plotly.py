from plotly.basedatatypes import BaseTraceType
import copy


class Parcats(BaseTraceType):

    # arrangement
    # -----------
    @property
    def arrangement(self):
        """
        Sets the drag interaction mode for categories and dimensions.
        If `perpendicular`, the categories can only move along a line
        perpendicular to the paths. If `freeform`, the categories can
        freely move on the plane. If `fixed`, the categories and
        dimensions are stationary.
    
        The 'arrangement' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['perpendicular', 'freeform', 'fixed']

        Returns
        -------
        Any
        """
        return self['arrangement']

    @arrangement.setter
    def arrangement(self, val):
        self['arrangement'] = val

    # bundlecolors
    # ------------
    @property
    def bundlecolors(self):
        """
        Sort paths so that like colors are bundled together within each
        category.
    
        The 'bundlecolors' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['bundlecolors']

    @bundlecolors.setter
    def bundlecolors(self, val):
        self['bundlecolors'] = val

    # counts
    # ------
    @property
    def counts(self):
        """
        The number of observations represented by each state. Defaults
        to 1 so that each state represents one observation
    
        The 'counts' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['counts']

    @counts.setter
    def counts(self, val):
        self['counts'] = val

    # countssrc
    # ---------
    @property
    def countssrc(self):
        """
        Sets the source reference on plot.ly for  counts .
    
        The 'countssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['countssrc']

    @countssrc.setter
    def countssrc(self, val):
        self['countssrc'] = val

    # dimensions
    # ----------
    @property
    def dimensions(self):
        """
        The dimensions (variables) of the parallel categories diagram.
    
        The 'dimensions' property is a tuple of instances of
        Dimension that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.parcats.Dimension
          - A list or tuple of dicts of string/value properties that
            will be passed to the Dimension constructor
    
            Supported dict properties:
                
                categoryarray
                    Sets the order in which categories in this
                    dimension appear. Only has an effect if
                    `categoryorder` is set to "array". Used with
                    `categoryorder`.
                categoryarraysrc
                    Sets the source reference on plot.ly for
                    categoryarray .
                categoryorder
                    Specifies the ordering logic for the categories
                    in the dimension. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                displayindex
                    The display index of dimension, from left to
                    right, zero indexed, defaults to dimension
                    index.
                label
                    The shown name of the dimension.
                ticktext
                    Sets alternative tick labels for the categories
                    in this dimension. Only has an effect if
                    `categoryorder` is set to "array". Should be an
                    array the same length as `categoryarray` Used
                    with `categoryorder`.
                ticktextsrc
                    Sets the source reference on plot.ly for
                    ticktext .
                values
                    Dimension values. `values[n]` represents the
                    category value of the `n`th point in the
                    dataset, therefore the `values` vector for all
                    dimensions must be the same (longer vectors
                    will be truncated).
                valuessrc
                    Sets the source reference on plot.ly for
                    values .
                visible
                    Shows the dimension when set to `true` (the
                    default). Hides the dimension for `false`.

        Returns
        -------
        tuple[plotly.graph_objs.parcats.Dimension]
        """
        return self['dimensions']

    @dimensions.setter
    def dimensions(self, val):
        self['dimensions'] = val

    # dimensiondefaults
    # -----------------
    @property
    def dimensiondefaults(self):
        """
        When used in a template (as
        layout.template.data.parcats.dimensiondefaults), sets the
        default property values to use for elements of
        parcats.dimensions
    
        The 'dimensiondefaults' property is an instance of Dimension
        that may be specified as:
          - An instance of plotly.graph_objs.parcats.Dimension
          - A dict of string/value properties that will be passed
            to the Dimension constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.parcats.Dimension
        """
        return self['dimensiondefaults']

    @dimensiondefaults.setter
    def dimensiondefaults(self, val):
        self['dimensiondefaults'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.parcats.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this parcats trace
                    .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this parcats trace .
                x
                    Sets the horizontal domain of this parcats
                    trace (in plot fraction).
                y
                    Sets the vertical domain of this parcats trace
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.parcats.Domain
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
          - Any combination of ['count', 'probability'] joined with '+' characters
            (e.g. 'count+probability')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')

        Returns
        -------
        Any
        """
        return self['hoverinfo']

    @hoverinfo.setter
    def hoverinfo(self, val):
        self['hoverinfo'] = val

    # hoveron
    # -------
    @property
    def hoveron(self):
        """
        Sets the hover interaction mode for the parcats diagram. If
        `category`, hover interaction take place per category. If
        `color`, hover interactions take place per color per category.
        If `dimension`, hover interactions take place across all
        categories per dimension.
    
        The 'hoveron' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['category', 'color', 'dimension']

        Returns
        -------
        Any
        """
        return self['hoveron']

    @hoveron.setter
    def hoveron(self, val):
        self['hoveron'] = val

    # labelfont
    # ---------
    @property
    def labelfont(self):
        """
        Sets the font for the `dimension` labels.
    
        The 'labelfont' property is an instance of Labelfont
        that may be specified as:
          - An instance of plotly.graph_objs.parcats.Labelfont
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
        plotly.graph_objs.parcats.Labelfont
        """
        return self['labelfont']

    @labelfont.setter
    def labelfont(self, val):
        self['labelfont'] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of plotly.graph_objs.parcats.Line
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
                    plotly.graph_objs.parcats.line.ColorBar
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
                shape
                    Sets the shape of the paths. If `linear`, paths
                    are composed of straight lines. If `hspline`,
                    paths are composed of horizontal curved splines
                showscale
                    Determines whether or not a colorbar is
                    displayed for this trace. Has an effect only if
                    in `line.color`is set to a numerical array.

        Returns
        -------
        plotly.graph_objs.parcats.Line
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

    # sortpaths
    # ---------
    @property
    def sortpaths(self):
        """
        Sets the path sorting algorithm. If `forward`, sort paths based
        on dimension categories from left to right. If `backward`, sort
        paths based on dimensions categories from right to left.
    
        The 'sortpaths' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['forward', 'backward']

        Returns
        -------
        Any
        """
        return self['sortpaths']

    @sortpaths.setter
    def sortpaths(self, val):
        self['sortpaths'] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of plotly.graph_objs.parcats.Stream
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
        plotly.graph_objs.parcats.Stream
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
        Sets the font for the `category` labels.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of plotly.graph_objs.parcats.Tickfont
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
        plotly.graph_objs.parcats.Tickfont
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
        arrangement
            Sets the drag interaction mode for categories and
            dimensions. If `perpendicular`, the categories can only
            move along a line perpendicular to the paths. If
            `freeform`, the categories can freely move on the
            plane. If `fixed`, the categories and dimensions are
            stationary.
        bundlecolors
            Sort paths so that like colors are bundled together
            within each category.
        counts
            The number of observations represented by each state.
            Defaults to 1 so that each state represents one
            observation
        countssrc
            Sets the source reference on plot.ly for  counts .
        dimensions
            The dimensions (variables) of the parallel categories
            diagram.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcats.dimensiondefaults), sets
            the default property values to use for elements of
            parcats.dimensions
        domain
            plotly.graph_objs.parcats.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoveron
            Sets the hover interaction mode for the parcats
            diagram. If `category`, hover interaction take place
            per category. If `color`, hover interactions take place
            per color per category. If `dimension`, hover
            interactions take place across all categories per
            dimension.
        labelfont
            Sets the font for the `dimension` labels.
        line
            plotly.graph_objs.parcats.Line instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        sortpaths
            Sets the path sorting algorithm. If `forward`, sort
            paths based on dimension categories from left to right.
            If `backward`, sort paths based on dimensions
            categories from right to left.
        stream
            plotly.graph_objs.parcats.Stream instance or dict with
            compatible properties
        tickfont
            Sets the font for the `category` labels.
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
        arrangement=None,
        bundlecolors=None,
        counts=None,
        countssrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        hoverinfo=None,
        hoveron=None,
        labelfont=None,
        line=None,
        name=None,
        sortpaths=None,
        stream=None,
        tickfont=None,
        uid=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Parcats object
        
        Parallel categories diagram for multidimensional categorical
        data.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.Parcats
        arrangement
            Sets the drag interaction mode for categories and
            dimensions. If `perpendicular`, the categories can only
            move along a line perpendicular to the paths. If
            `freeform`, the categories can freely move on the
            plane. If `fixed`, the categories and dimensions are
            stationary.
        bundlecolors
            Sort paths so that like colors are bundled together
            within each category.
        counts
            The number of observations represented by each state.
            Defaults to 1 so that each state represents one
            observation
        countssrc
            Sets the source reference on plot.ly for  counts .
        dimensions
            The dimensions (variables) of the parallel categories
            diagram.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcats.dimensiondefaults), sets
            the default property values to use for elements of
            parcats.dimensions
        domain
            plotly.graph_objs.parcats.Domain instance or dict with
            compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoveron
            Sets the hover interaction mode for the parcats
            diagram. If `category`, hover interaction take place
            per category. If `color`, hover interactions take place
            per color per category. If `dimension`, hover
            interactions take place across all categories per
            dimension.
        labelfont
            Sets the font for the `dimension` labels.
        line
            plotly.graph_objs.parcats.Line instance or dict with
            compatible properties
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        sortpaths
            Sets the path sorting algorithm. If `forward`, sort
            paths based on dimension categories from left to right.
            If `backward`, sort paths based on dimensions
            categories from right to left.
        stream
            plotly.graph_objs.parcats.Stream instance or dict with
            compatible properties
        tickfont
            Sets the font for the `category` labels.
        uid

        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Parcats
        """
        super(Parcats, self).__init__('parcats')

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
The first argument to the plotly.graph_objs.Parcats 
constructor must be a dict or 
an instance of plotly.graph_objs.Parcats"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators import (parcats as v_parcats)

        # Initialize validators
        # ---------------------
        self._validators['arrangement'] = v_parcats.ArrangementValidator()
        self._validators['bundlecolors'] = v_parcats.BundlecolorsValidator()
        self._validators['counts'] = v_parcats.CountsValidator()
        self._validators['countssrc'] = v_parcats.CountssrcValidator()
        self._validators['dimensions'] = v_parcats.DimensionsValidator()
        self._validators['dimensiondefaults'] = v_parcats.DimensionValidator()
        self._validators['domain'] = v_parcats.DomainValidator()
        self._validators['hoverinfo'] = v_parcats.HoverinfoValidator()
        self._validators['hoveron'] = v_parcats.HoveronValidator()
        self._validators['labelfont'] = v_parcats.LabelfontValidator()
        self._validators['line'] = v_parcats.LineValidator()
        self._validators['name'] = v_parcats.NameValidator()
        self._validators['sortpaths'] = v_parcats.SortpathsValidator()
        self._validators['stream'] = v_parcats.StreamValidator()
        self._validators['tickfont'] = v_parcats.TickfontValidator()
        self._validators['uid'] = v_parcats.UidValidator()
        self._validators['visible'] = v_parcats.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('arrangement', None)
        self['arrangement'] = arrangement if arrangement is not None else _v
        _v = arg.pop('bundlecolors', None)
        self['bundlecolors'] = bundlecolors if bundlecolors is not None else _v
        _v = arg.pop('counts', None)
        self['counts'] = counts if counts is not None else _v
        _v = arg.pop('countssrc', None)
        self['countssrc'] = countssrc if countssrc is not None else _v
        _v = arg.pop('dimensions', None)
        self['dimensions'] = dimensions if dimensions is not None else _v
        _v = arg.pop('dimensiondefaults', None)
        self['dimensiondefaults'
            ] = dimensiondefaults if dimensiondefaults is not None else _v
        _v = arg.pop('domain', None)
        self['domain'] = domain if domain is not None else _v
        _v = arg.pop('hoverinfo', None)
        self['hoverinfo'] = hoverinfo if hoverinfo is not None else _v
        _v = arg.pop('hoveron', None)
        self['hoveron'] = hoveron if hoveron is not None else _v
        _v = arg.pop('labelfont', None)
        self['labelfont'] = labelfont if labelfont is not None else _v
        _v = arg.pop('line', None)
        self['line'] = line if line is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('sortpaths', None)
        self['sortpaths'] = sortpaths if sortpaths is not None else _v
        _v = arg.pop('stream', None)
        self['stream'] = stream if stream is not None else _v
        _v = arg.pop('tickfont', None)
        self['tickfont'] = tickfont if tickfont is not None else _v
        _v = arg.pop('uid', None)
        self['uid'] = uid if uid is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v

        # Read-only literals
        # ------------------
        from _plotly_utils.basevalidators import LiteralValidator
        self._props['type'] = 'parcats'
        self._validators['type'] = LiteralValidator(
            plotly_name='type', parent_name='parcats', val='parcats'
        )
        arg.pop('type', None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
