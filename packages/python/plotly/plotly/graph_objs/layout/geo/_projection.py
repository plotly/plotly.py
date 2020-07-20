from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Projection(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout.geo"
    _path_str = "layout.geo.projection"
    _valid_props = {"parallels", "rotation", "scale", "type"}

    # parallels
    # ---------
    @property
    def parallels(self):
        """
        For conic projection types only. Sets the parallels (tangent,
        secant) where the cone intersects the sphere.
    
        The 'parallels' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'parallels[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'parallels[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self["parallels"]

    @parallels.setter
    def parallels(self, val):
        self["parallels"] = val

    # rotation
    # --------
    @property
    def rotation(self):
        """
        The 'rotation' property is an instance of Rotation
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.projection.Rotation`
          - A dict of string/value properties that will be passed
            to the Rotation constructor
    
            Supported dict properties:
                
                lat
                    Rotates the map along meridians (in degrees
                    North).
                lon
                    Rotates the map along parallels (in degrees
                    East). Defaults to the center of the
                    `lonaxis.range` values.
                roll
                    Roll the map (in degrees) For example, a roll
                    of 180 makes the map appear upside down.

        Returns
        -------
        plotly.graph_objs.layout.geo.projection.Rotation
        """
        return self["rotation"]

    @rotation.setter
    def rotation(self, val):
        self["rotation"] = val

    # scale
    # -----
    @property
    def scale(self):
        """
        Zooms in or out on the map view. A scale of 1 corresponds to
        the largest zoom level that fits the map's lon and lat ranges.
    
        The 'scale' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["scale"]

    @scale.setter
    def scale(self, val):
        self["scale"] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the projection type.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['equirectangular', 'mercator', 'orthographic', 'natural
                earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4',
                'azimuthal equal area', 'azimuthal equidistant', 'conic
                equal area', 'conic conformal', 'conic equidistant',
                'gnomonic', 'stereographic', 'mollweide', 'hammer',
                'transverse mercator', 'albers usa', 'winkel tripel',
                'aitoff', 'sinusoidal']

        Returns
        -------
        Any
        """
        return self["type"]

    @type.setter
    def type(self, val):
        self["type"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        parallels
            For conic projection types only. Sets the parallels
            (tangent, secant) where the cone intersects the sphere.
        rotation
            :class:`plotly.graph_objects.layout.geo.projection.Rota
            tion` instance or dict with compatible properties
        scale
            Zooms in or out on the map view. A scale of 1
            corresponds to the largest zoom level that fits the
            map's lon and lat ranges.
        type
            Sets the projection type.
        """

    def __init__(
        self, arg=None, parallels=None, rotation=None, scale=None, type=None, **kwargs
    ):
        """
        Construct a new Projection object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.geo.Projection`
        parallels
            For conic projection types only. Sets the parallels
            (tangent, secant) where the cone intersects the sphere.
        rotation
            :class:`plotly.graph_objects.layout.geo.projection.Rota
            tion` instance or dict with compatible properties
        scale
            Zooms in or out on the map view. A scale of 1
            corresponds to the largest zoom level that fits the
            map's lon and lat ranges.
        type
            Sets the projection type.

        Returns
        -------
        Projection
        """
        super(Projection, self).__init__("projection")

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
The first argument to the plotly.graph_objs.layout.geo.Projection 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.geo.Projection`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("parallels", None)
        _v = parallels if parallels is not None else _v
        if _v is not None:
            self["parallels"] = _v
        _v = arg.pop("rotation", None)
        _v = rotation if rotation is not None else _v
        if _v is not None:
            self["rotation"] = _v
        _v = arg.pop("scale", None)
        _v = scale if scale is not None else _v
        if _v is not None:
            self["scale"] = _v
        _v = arg.pop("type", None)
        _v = type if type is not None else _v
        if _v is not None:
            self["type"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
