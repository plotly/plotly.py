from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Mapbox(BaseLayoutHierarchyType):

    # accesstoken
    # -----------
    @property
    def accesstoken(self):
        """
        Sets the mapbox access token to be used for this mapbox map.
        Alternatively, the mapbox access token can be set in the
        configuration options under `mapboxAccessToken`.
    
        The 'accesstoken' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self['accesstoken']

    @accesstoken.setter
    def accesstoken(self, val):
        self['accesstoken'] = val

    # bearing
    # -------
    @property
    def bearing(self):
        """
        Sets the bearing angle of the map (in degrees counter-clockwise
        from North).
    
        The 'bearing' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['bearing']

    @bearing.setter
    def bearing(self, val):
        self['bearing'] = val

    # center
    # ------
    @property
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.Center
          - A dict of string/value properties that will be passed
            to the Center constructor
    
            Supported dict properties:
                
                lat
                    Sets the latitude of the center of the map (in
                    degrees North).
                lon
                    Sets the longitude of the center of the map (in
                    degrees East).

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Center
        """
        return self['center']

    @center.setter
    def center(self, val):
        self['center'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.Domain
          - A dict of string/value properties that will be passed
            to the Domain constructor
    
            Supported dict properties:
                
                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this mapbox subplot
                    .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this mapbox subplot .
                x
                    Sets the horizontal domain of this mapbox
                    subplot (in plot fraction).
                y
                    Sets the vertical domain of this mapbox subplot
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # layers
    # ------
    @property
    def layers(self):
        """
        The 'layers' property is a tuple of instances of
        Layer that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.mapbox.Layer
          - A list or tuple of dicts of string/value properties that
            will be passed to the Layer constructor
    
            Supported dict properties:
                
                below
                    Determines if the layer will be inserted before
                    the layer with the specified ID. If omitted or
                    set to '', the layer will be inserted above
                    every existing layer.
                circle
                    plotly.graph_objs.layout.mapbox.layer.Circle
                    instance or dict with compatible properties
                color
                    Sets the primary layer color. If `type` is
                    "circle", color corresponds to the circle color
                    If `type` is "line", color corresponds to the
                    line color If `type` is "fill", color
                    corresponds to the fill color If `type` is
                    "symbol", color corresponds to the icon color
                fill
                    plotly.graph_objs.layout.mapbox.layer.Fill
                    instance or dict with compatible properties
                line
                    plotly.graph_objs.layout.mapbox.layer.Line
                    instance or dict with compatible properties
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
                opacity
                    Sets the opacity of the layer.
                source
                    Sets the source data for this layer. Source can
                    be either a URL, a geojson object (with
                    `sourcetype` set to "geojson") or an array of
                    tile URLS (with `sourcetype` set to "vector").
                sourcelayer
                    Specifies the layer to use from a vector tile
                    source. Required for "vector" source type that
                    supports multiple layers.
                sourcetype
                    Sets the source type for this layer. Support
                    for "raster", "image" and "video" source types
                    is coming soon.
                symbol
                    plotly.graph_objs.layout.mapbox.layer.Symbol
                    instance or dict with compatible properties
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
                type
                    Sets the layer type. Support for "raster",
                    "background" types is coming soon. Note that
                    "line" and "fill" are not compatible with Point
                    GeoJSON geometries.
                visible
                    Determines whether this layer is displayed

        Returns
        -------
        tuple[plotly.graph_objs.layout.mapbox.Layer]
        """
        return self['layers']

    @layers.setter
    def layers(self, val):
        self['layers'] = val

    # layerdefaults
    # -------------
    @property
    def layerdefaults(self):
        """
        When used in a template (as
        layout.template.layout.mapbox.layerdefaults), sets the default
        property values to use for elements of layout.mapbox.layers
    
        The 'layerdefaults' property is an instance of Layer
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.Layer
          - A dict of string/value properties that will be passed
            to the Layer constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Layer
        """
        return self['layerdefaults']

    @layerdefaults.setter
    def layerdefaults(self, val):
        self['layerdefaults'] = val

    # pitch
    # -----
    @property
    def pitch(self):
        """
        Sets the pitch angle of the map (in degrees, where 0 means
        perpendicular to the surface of the map).
    
        The 'pitch' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['pitch']

    @pitch.setter
    def pitch(self, val):
        self['pitch'] = val

    # style
    # -----
    @property
    def style(self):
        """
        Sets the Mapbox map style. Either input one of the default
        Mapbox style names or the URL to a custom style or a valid
        Mapbox style JSON.
    
        The 'style' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['style']

    @style.setter
    def style(self, val):
        self['style'] = val

    # zoom
    # ----
    @property
    def zoom(self):
        """
        Sets the zoom level of the map.
    
        The 'zoom' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zoom']

    @zoom.setter
    def zoom(self, val):
        self['zoom'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        accesstoken
            Sets the mapbox access token to be used for this mapbox
            map. Alternatively, the mapbox access token can be set
            in the configuration options under `mapboxAccessToken`.
        bearing
            Sets the bearing angle of the map (in degrees counter-
            clockwise from North).
        center
            plotly.graph_objs.layout.mapbox.Center instance or dict
            with compatible properties
        domain
            plotly.graph_objs.layout.mapbox.Domain instance or dict
            with compatible properties
        layers
            plotly.graph_objs.layout.mapbox.Layer instance or dict
            with compatible properties
        layerdefaults
            When used in a template (as
            layout.template.layout.mapbox.layerdefaults), sets the
            default property values to use for elements of
            layout.mapbox.layers
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map).
        style
            Sets the Mapbox map style. Either input one of the
            default Mapbox style names or the URL to a custom style
            or a valid Mapbox style JSON.
        zoom
            Sets the zoom level of the map.
        """

    def __init__(
        self,
        arg=None,
        accesstoken=None,
        bearing=None,
        center=None,
        domain=None,
        layers=None,
        layerdefaults=None,
        pitch=None,
        style=None,
        zoom=None,
        **kwargs
    ):
        """
        Construct a new Mapbox object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Mapbox
        accesstoken
            Sets the mapbox access token to be used for this mapbox
            map. Alternatively, the mapbox access token can be set
            in the configuration options under `mapboxAccessToken`.
        bearing
            Sets the bearing angle of the map (in degrees counter-
            clockwise from North).
        center
            plotly.graph_objs.layout.mapbox.Center instance or dict
            with compatible properties
        domain
            plotly.graph_objs.layout.mapbox.Domain instance or dict
            with compatible properties
        layers
            plotly.graph_objs.layout.mapbox.Layer instance or dict
            with compatible properties
        layerdefaults
            When used in a template (as
            layout.template.layout.mapbox.layerdefaults), sets the
            default property values to use for elements of
            layout.mapbox.layers
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map).
        style
            Sets the Mapbox map style. Either input one of the
            default Mapbox style names or the URL to a custom style
            or a valid Mapbox style JSON.
        zoom
            Sets the zoom level of the map.

        Returns
        -------
        Mapbox
        """
        super(Mapbox, self).__init__('mapbox')

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
The first argument to the plotly.graph_objs.layout.Mapbox 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Mapbox"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout import (mapbox as v_mapbox)

        # Initialize validators
        # ---------------------
        self._validators['accesstoken'] = v_mapbox.AccesstokenValidator()
        self._validators['bearing'] = v_mapbox.BearingValidator()
        self._validators['center'] = v_mapbox.CenterValidator()
        self._validators['domain'] = v_mapbox.DomainValidator()
        self._validators['layers'] = v_mapbox.LayersValidator()
        self._validators['layerdefaults'] = v_mapbox.LayerValidator()
        self._validators['pitch'] = v_mapbox.PitchValidator()
        self._validators['style'] = v_mapbox.StyleValidator()
        self._validators['zoom'] = v_mapbox.ZoomValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('accesstoken', None)
        self['accesstoken'] = accesstoken if accesstoken is not None else _v
        _v = arg.pop('bearing', None)
        self['bearing'] = bearing if bearing is not None else _v
        _v = arg.pop('center', None)
        self['center'] = center if center is not None else _v
        _v = arg.pop('domain', None)
        self['domain'] = domain if domain is not None else _v
        _v = arg.pop('layers', None)
        self['layers'] = layers if layers is not None else _v
        _v = arg.pop('layerdefaults', None)
        self['layerdefaults'
            ] = layerdefaults if layerdefaults is not None else _v
        _v = arg.pop('pitch', None)
        self['pitch'] = pitch if pitch is not None else _v
        _v = arg.pop('style', None)
        self['style'] = style if style is not None else _v
        _v = arg.pop('zoom', None)
        self['zoom'] = zoom if zoom is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
