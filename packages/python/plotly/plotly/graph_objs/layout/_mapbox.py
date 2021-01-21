from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Mapbox(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout"
    _path_str = "layout.mapbox"
    _valid_props = {
        "accesstoken",
        "bearing",
        "center",
        "domain",
        "layers",
        "pitch",
        "style",
        "uirevision",
        "zoom",
    }

    # accesstoken
    # -----------
    @property
    def accesstoken(self):
        """
        Sets the mapbox access token to be used for this mapbox map.
        Alternatively, the mapbox access token can be set in the
        configuration options under `mapboxAccessToken`. Note that
        accessToken are only required when `style` (e.g with values :
        basic, streets, outdoors, light, dark, satellite, satellite-
        streets ) and/or a layout layer references the Mapbox server.
    
        The 'accesstoken' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["accesstoken"]

    @accesstoken.setter
    def accesstoken(self, val):
        self["accesstoken"] = val

    # bearing
    # -------
    @property
    def bearing(self):
        """
        Sets the bearing angle of the map in degrees counter-clockwise
        from North (mapbox.bearing).
    
        The 'bearing' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["bearing"]

    @bearing.setter
    def bearing(self, val):
        self["bearing"] = val

    # center
    # ------
    @property
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.mapbox.Center`
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
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.mapbox.Domain`
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
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # layers
    # ------
    @property
    def layers(self):
        """
        The 'layers' property is an instance of Layers
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.mapbox.Layers`
          - A dict of string/value properties that will be passed
            to the Layers constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.mapbox.Layers
        """
        return self["layers"]

    @layers.setter
    def layers(self, val):
        self["layers"] = val

    # pitch
    # -----
    @property
    def pitch(self):
        """
        Sets the pitch angle of the map (in degrees, where 0 means
        perpendicular to the surface of the map) (mapbox.pitch).
    
        The 'pitch' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["pitch"]

    @pitch.setter
    def pitch(self, val):
        self["pitch"] = val

    # style
    # -----
    @property
    def style(self):
        """
        Defines the map layers that are rendered by default below the
        trace layers defined in `data`, which are themselves by default
        rendered below the layers defined in `layout.mapbox.layers`.
        These layers can be defined either explicitly as a Mapbox Style
        object which can contain multiple layer definitions that load
        data from any public or private Tile Map Service (TMS or XYZ)
        or Web Map Service (WMS) or implicitly by using one of the
        built-in style objects which use WMSes which do not require any
        access tokens, or by using a default Mapbox style or custom
        Mapbox style URL, both of which require a Mapbox access token
        Note that Mapbox access token can be set in the `accesstoken`
        attribute or in the `mapboxAccessToken` config option.  Mapbox
        Style objects are of the form described in the Mapbox GL JS
        documentation available at https://docs.mapbox.com/mapbox-gl-
        js/style-spec  The built-in plotly.js styles objects are: open-
        street-map, white-bg, carto-positron, carto-darkmatter, stamen-
        terrain, stamen-toner, stamen-watercolor  The built-in Mapbox
        styles are: basic, streets, outdoors, light, dark, satellite,
        satellite-streets  Mapbox style URLs are of the form:
        mapbox://mapbox.mapbox-<name>-<version>
    
        The 'style' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["style"]

    @style.setter
    def style(self, val):
        self["style"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in the view:
        `center`, `zoom`, `bearing`, `pitch`. Defaults to
        `layout.uirevision`.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # zoom
    # ----
    @property
    def zoom(self):
        """
        Sets the zoom level of the map (mapbox.zoom).
    
        The 'zoom' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["zoom"]

    @zoom.setter
    def zoom(self, val):
        self["zoom"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        accesstoken
            Sets the mapbox access token to be used for this mapbox
            map. Alternatively, the mapbox access token can be set
            in the configuration options under `mapboxAccessToken`.
            Note that accessToken are only required when `style`
            (e.g with values : basic, streets, outdoors, light,
            dark, satellite, satellite-streets ) and/or a layout
            layer references the Mapbox server.
        bearing
            Sets the bearing angle of the map in degrees counter-
            clockwise from North (mapbox.bearing).
        center
            :class:`plotly.graph_objects.layout.mapbox.Center`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.mapbox.Domain`
            instance or dict with compatible properties
        layers
            :class:`plotly.graph_objects.layout.mapbox.Layers`
            instance or dict with compatible properties
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map)
            (mapbox.pitch).
        style
            Defines the map layers that are rendered by default
            below the trace layers defined in `data`, which are
            themselves by default rendered below the layers defined
            in `layout.mapbox.layers`.  These layers can be defined
            either explicitly as a Mapbox Style object which can
            contain multiple layer definitions that load data from
            any public or private Tile Map Service (TMS or XYZ) or
            Web Map Service (WMS) or implicitly by using one of the
            built-in style objects which use WMSes which do not
            require any access tokens, or by using a default Mapbox
            style or custom Mapbox style URL, both of which require
            a Mapbox access token  Note that Mapbox access token
            can be set in the `accesstoken` attribute or in the
            `mapboxAccessToken` config option.  Mapbox Style
            objects are of the form described in the Mapbox GL JS
            documentation available at
            https://docs.mapbox.com/mapbox-gl-js/style-spec  The
            built-in plotly.js styles objects are: open-street-map,
            white-bg, carto-positron, carto-darkmatter, stamen-
            terrain, stamen-toner, stamen-watercolor  The built-in
            Mapbox styles are: basic, streets, outdoors, light,
            dark, satellite, satellite-streets  Mapbox style URLs
            are of the form:
            mapbox://mapbox.mapbox-<name>-<version>
        uirevision
            Controls persistence of user-driven changes in the
            view: `center`, `zoom`, `bearing`, `pitch`. Defaults to
            `layout.uirevision`.
        zoom
            Sets the zoom level of the map (mapbox.zoom).
        """

    def __init__(
        self,
        arg=None,
        accesstoken=None,
        bearing=None,
        center=None,
        domain=None,
        layers=None,
        pitch=None,
        style=None,
        uirevision=None,
        zoom=None,
        **kwargs
    ):
        """
        Construct a new Mapbox object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Mapbox`
        accesstoken
            Sets the mapbox access token to be used for this mapbox
            map. Alternatively, the mapbox access token can be set
            in the configuration options under `mapboxAccessToken`.
            Note that accessToken are only required when `style`
            (e.g with values : basic, streets, outdoors, light,
            dark, satellite, satellite-streets ) and/or a layout
            layer references the Mapbox server.
        bearing
            Sets the bearing angle of the map in degrees counter-
            clockwise from North (mapbox.bearing).
        center
            :class:`plotly.graph_objects.layout.mapbox.Center`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.mapbox.Domain`
            instance or dict with compatible properties
        layers
            :class:`plotly.graph_objects.layout.mapbox.Layers`
            instance or dict with compatible properties
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map)
            (mapbox.pitch).
        style
            Defines the map layers that are rendered by default
            below the trace layers defined in `data`, which are
            themselves by default rendered below the layers defined
            in `layout.mapbox.layers`.  These layers can be defined
            either explicitly as a Mapbox Style object which can
            contain multiple layer definitions that load data from
            any public or private Tile Map Service (TMS or XYZ) or
            Web Map Service (WMS) or implicitly by using one of the
            built-in style objects which use WMSes which do not
            require any access tokens, or by using a default Mapbox
            style or custom Mapbox style URL, both of which require
            a Mapbox access token  Note that Mapbox access token
            can be set in the `accesstoken` attribute or in the
            `mapboxAccessToken` config option.  Mapbox Style
            objects are of the form described in the Mapbox GL JS
            documentation available at
            https://docs.mapbox.com/mapbox-gl-js/style-spec  The
            built-in plotly.js styles objects are: open-street-map,
            white-bg, carto-positron, carto-darkmatter, stamen-
            terrain, stamen-toner, stamen-watercolor  The built-in
            Mapbox styles are: basic, streets, outdoors, light,
            dark, satellite, satellite-streets  Mapbox style URLs
            are of the form:
            mapbox://mapbox.mapbox-<name>-<version>
        uirevision
            Controls persistence of user-driven changes in the
            view: `center`, `zoom`, `bearing`, `pitch`. Defaults to
            `layout.uirevision`.
        zoom
            Sets the zoom level of the map (mapbox.zoom).

        Returns
        -------
        Mapbox
        """
        super(Mapbox, self).__init__("mapbox")

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
The first argument to the plotly.graph_objs.layout.Mapbox 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.Mapbox`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("accesstoken", None)
        _v = accesstoken if accesstoken is not None else _v
        if _v is not None:
            self["accesstoken"] = _v
        _v = arg.pop("bearing", None)
        _v = bearing if bearing is not None else _v
        if _v is not None:
            self["bearing"] = _v
        _v = arg.pop("center", None)
        _v = center if center is not None else _v
        if _v is not None:
            self["center"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("layers", None)
        _v = layers if layers is not None else _v
        if _v is not None:
            self["layers"] = _v
        _v = arg.pop("pitch", None)
        _v = pitch if pitch is not None else _v
        if _v is not None:
            self["pitch"] = _v
        _v = arg.pop("style", None)
        _v = style if style is not None else _v
        if _v is not None:
            self["style"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("zoom", None)
        _v = zoom if zoom is not None else _v
        if _v is not None:
            self["zoom"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
