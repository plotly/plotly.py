from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Projection(_BaseLayoutHierarchyType):

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
          - An instance of plotly.graph_objs.layout.geo.projection.Rotation
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

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.geo"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        parallels
            For conic projection types only. Sets the parallels
            (tangent, secant) where the cone intersects the sphere.
        rotation
            plotly.graph_objects.layout.geo.projection.Rotation
            instance or dict with compatible properties
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
            an instance of plotly.graph_objs.layout.geo.Projection
        parallels
            For conic projection types only. Sets the parallels
            (tangent, secant) where the cone intersects the sphere.
        rotation
            plotly.graph_objects.layout.geo.projection.Rotation
            instance or dict with compatible properties
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
an instance of plotly.graph_objs.layout.geo.Projection"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import projection as v_projection

        # Initialize validators
        # ---------------------
        self._validators["parallels"] = v_projection.ParallelsValidator()
        self._validators["rotation"] = v_projection.RotationValidator()
        self._validators["scale"] = v_projection.ScaleValidator()
        self._validators["type"] = v_projection.TypeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("parallels", None)
        self["parallels"] = parallels if parallels is not None else _v
        _v = arg.pop("rotation", None)
        self["rotation"] = rotation if rotation is not None else _v
        _v = arg.pop("scale", None)
        self["scale"] = scale if scale is not None else _v
        _v = arg.pop("type", None)
        self["type"] = type if type is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Lonaxis(_BaseLayoutHierarchyType):

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the graticule's longitude/latitude tick step.
    
        The 'dtick' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dtick"]

    @dtick.setter
    def dtick(self, val):
        self["dtick"] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the graticule's stroke color.
    
        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["gridcolor"]

    @gridcolor.setter
    def gridcolor(self, val):
        self["gridcolor"] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the graticule's stroke width (in px).
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["gridwidth"]

    @gridwidth.setter
    def gridwidth(self, val):
        self["gridwidth"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis (in degrees), sets the map's
        clipped coordinates.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Sets whether or not graticule are shown on the map.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showgrid"]

    @showgrid.setter
    def showgrid(self, val):
        self["showgrid"] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the graticule's starting tick longitude/latitude.
    
        The 'tick0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["tick0"]

    @tick0.setter
    def tick0(self, val):
        self["tick0"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.geo"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dtick
            Sets the graticule's longitude/latitude tick step.
        gridcolor
            Sets the graticule's stroke color.
        gridwidth
            Sets the graticule's stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map's clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule's starting tick longitude/latitude.
        """

    def __init__(
        self,
        arg=None,
        dtick=None,
        gridcolor=None,
        gridwidth=None,
        range=None,
        showgrid=None,
        tick0=None,
        **kwargs
    ):
        """
        Construct a new Lonaxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.geo.Lonaxis
        dtick
            Sets the graticule's longitude/latitude tick step.
        gridcolor
            Sets the graticule's stroke color.
        gridwidth
            Sets the graticule's stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map's clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule's starting tick longitude/latitude.

        Returns
        -------
        Lonaxis
        """
        super(Lonaxis, self).__init__("lonaxis")

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
The first argument to the plotly.graph_objs.layout.geo.Lonaxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.geo.Lonaxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import lonaxis as v_lonaxis

        # Initialize validators
        # ---------------------
        self._validators["dtick"] = v_lonaxis.DtickValidator()
        self._validators["gridcolor"] = v_lonaxis.GridcolorValidator()
        self._validators["gridwidth"] = v_lonaxis.GridwidthValidator()
        self._validators["range"] = v_lonaxis.RangeValidator()
        self._validators["showgrid"] = v_lonaxis.ShowgridValidator()
        self._validators["tick0"] = v_lonaxis.Tick0Validator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("dtick", None)
        self["dtick"] = dtick if dtick is not None else _v
        _v = arg.pop("gridcolor", None)
        self["gridcolor"] = gridcolor if gridcolor is not None else _v
        _v = arg.pop("gridwidth", None)
        self["gridwidth"] = gridwidth if gridwidth is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("showgrid", None)
        self["showgrid"] = showgrid if showgrid is not None else _v
        _v = arg.pop("tick0", None)
        self["tick0"] = tick0 if tick0 is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Lataxis(_BaseLayoutHierarchyType):

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the graticule's longitude/latitude tick step.
    
        The 'dtick' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["dtick"]

    @dtick.setter
    def dtick(self, val):
        self["dtick"] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the graticule's stroke color.
    
        The 'gridcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["gridcolor"]

    @gridcolor.setter
    def gridcolor(self, val):
        self["gridcolor"] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the graticule's stroke width (in px).
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["gridwidth"]

    @gridwidth.setter
    def gridwidth(self, val):
        self["gridwidth"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis (in degrees), sets the map's
        clipped coordinates.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Sets whether or not graticule are shown on the map.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showgrid"]

    @showgrid.setter
    def showgrid(self, val):
        self["showgrid"] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the graticule's starting tick longitude/latitude.
    
        The 'tick0' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["tick0"]

    @tick0.setter
    def tick0(self, val):
        self["tick0"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.geo"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dtick
            Sets the graticule's longitude/latitude tick step.
        gridcolor
            Sets the graticule's stroke color.
        gridwidth
            Sets the graticule's stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map's clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule's starting tick longitude/latitude.
        """

    def __init__(
        self,
        arg=None,
        dtick=None,
        gridcolor=None,
        gridwidth=None,
        range=None,
        showgrid=None,
        tick0=None,
        **kwargs
    ):
        """
        Construct a new Lataxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.geo.Lataxis
        dtick
            Sets the graticule's longitude/latitude tick step.
        gridcolor
            Sets the graticule's stroke color.
        gridwidth
            Sets the graticule's stroke width (in px).
        range
            Sets the range of this axis (in degrees), sets the
            map's clipped coordinates.
        showgrid
            Sets whether or not graticule are shown on the map.
        tick0
            Sets the graticule's starting tick longitude/latitude.

        Returns
        -------
        Lataxis
        """
        super(Lataxis, self).__init__("lataxis")

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
The first argument to the plotly.graph_objs.layout.geo.Lataxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.geo.Lataxis"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import lataxis as v_lataxis

        # Initialize validators
        # ---------------------
        self._validators["dtick"] = v_lataxis.DtickValidator()
        self._validators["gridcolor"] = v_lataxis.GridcolorValidator()
        self._validators["gridwidth"] = v_lataxis.GridwidthValidator()
        self._validators["range"] = v_lataxis.RangeValidator()
        self._validators["showgrid"] = v_lataxis.ShowgridValidator()
        self._validators["tick0"] = v_lataxis.Tick0Validator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("dtick", None)
        self["dtick"] = dtick if dtick is not None else _v
        _v = arg.pop("gridcolor", None)
        self["gridcolor"] = gridcolor if gridcolor is not None else _v
        _v = arg.pop("gridwidth", None)
        self["gridwidth"] = gridwidth if gridwidth is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("showgrid", None)
        self["showgrid"] = showgrid if showgrid is not None else _v
        _v = arg.pop("tick0", None)
        self["tick0"] = tick0 if tick0 is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Domain(_BaseLayoutHierarchyType):

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this geo subplot . Note that geo subplots are
        constrained by domain. In general, when `projection.scale` is
        set to 1. a map will fit either its x or y domain, but not
        both.
    
        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["column"]

    @column.setter
    def column(self, val):
        self["column"] = val

    # row
    # ---
    @property
    def row(self):
        """
        If there is a layout grid, use the domain for this row in the
        grid for this geo subplot . Note that geo subplots are
        constrained by domain. In general, when `projection.scale` is
        set to 1. a map will fit either its x or y domain, but not
        both.
    
        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["row"]

    @row.setter
    def row(self, val):
        self["row"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this geo subplot (in plot
        fraction). Note that geo subplots are constrained by domain. In
        general, when `projection.scale` is set to 1. a map will fit
        either its x or y domain, but not both.
    
        The 'x' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this geo subplot (in plot
        fraction). Note that geo subplots are constrained by domain. In
        general, when `projection.scale` is set to 1. a map will fit
        either its x or y domain, but not both.
    
        The 'y' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.geo"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this geo subplot . Note that geo
            subplots are constrained by domain. In general, when
            `projection.scale` is set to 1. a map will fit either
            its x or y domain, but not both.
        row
            If there is a layout grid, use the domain for this row
            in the grid for this geo subplot . Note that geo
            subplots are constrained by domain. In general, when
            `projection.scale` is set to 1. a map will fit either
            its x or y domain, but not both.
        x
            Sets the horizontal domain of this geo subplot (in plot
            fraction). Note that geo subplots are constrained by
            domain. In general, when `projection.scale` is set to
            1. a map will fit either its x or y domain, but not
            both.
        y
            Sets the vertical domain of this geo subplot (in plot
            fraction). Note that geo subplots are constrained by
            domain. In general, when `projection.scale` is set to
            1. a map will fit either its x or y domain, but not
            both.
        """

    def __init__(self, arg=None, column=None, row=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.geo.Domain
        column
            If there is a layout grid, use the domain for this
            column in the grid for this geo subplot . Note that geo
            subplots are constrained by domain. In general, when
            `projection.scale` is set to 1. a map will fit either
            its x or y domain, but not both.
        row
            If there is a layout grid, use the domain for this row
            in the grid for this geo subplot . Note that geo
            subplots are constrained by domain. In general, when
            `projection.scale` is set to 1. a map will fit either
            its x or y domain, but not both.
        x
            Sets the horizontal domain of this geo subplot (in plot
            fraction). Note that geo subplots are constrained by
            domain. In general, when `projection.scale` is set to
            1. a map will fit either its x or y domain, but not
            both.
        y
            Sets the vertical domain of this geo subplot (in plot
            fraction). Note that geo subplots are constrained by
            domain. In general, when `projection.scale` is set to
            1. a map will fit either its x or y domain, but not
            both.

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__("domain")

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
The first argument to the plotly.graph_objs.layout.geo.Domain 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.geo.Domain"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import domain as v_domain

        # Initialize validators
        # ---------------------
        self._validators["column"] = v_domain.ColumnValidator()
        self._validators["row"] = v_domain.RowValidator()
        self._validators["x"] = v_domain.XValidator()
        self._validators["y"] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("column", None)
        self["column"] = column if column is not None else _v
        _v = arg.pop("row", None)
        self["row"] = row if row is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Center(_BaseLayoutHierarchyType):

    # lat
    # ---
    @property
    def lat(self):
        """
        Sets the latitude of the map's center. For all projection
        types, the map's latitude center lies at the middle of the
        latitude range by default.
    
        The 'lat' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["lat"]

    @lat.setter
    def lat(self, val):
        self["lat"] = val

    # lon
    # ---
    @property
    def lon(self):
        """
        Sets the longitude of the map's center. By default, the map's
        longitude center lies at the middle of the longitude range for
        scoped projection and above `projection.rotation.lon`
        otherwise.
    
        The 'lon' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["lon"]

    @lon.setter
    def lon(self, val):
        self["lon"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.geo"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        lat
            Sets the latitude of the map's center. For all
            projection types, the map's latitude center lies at the
            middle of the latitude range by default.
        lon
            Sets the longitude of the map's center. By default, the
            map's longitude center lies at the middle of the
            longitude range for scoped projection and above
            `projection.rotation.lon` otherwise.
        """

    def __init__(self, arg=None, lat=None, lon=None, **kwargs):
        """
        Construct a new Center object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.geo.Center
        lat
            Sets the latitude of the map's center. For all
            projection types, the map's latitude center lies at the
            middle of the latitude range by default.
        lon
            Sets the longitude of the map's center. By default, the
            map's longitude center lies at the middle of the
            longitude range for scoped projection and above
            `projection.rotation.lon` otherwise.

        Returns
        -------
        Center
        """
        super(Center, self).__init__("center")

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
The first argument to the plotly.graph_objs.layout.geo.Center 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.geo.Center"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import center as v_center

        # Initialize validators
        # ---------------------
        self._validators["lat"] = v_center.LatValidator()
        self._validators["lon"] = v_center.LonValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("lat", None)
        self["lat"] = lat if lat is not None else _v
        _v = arg.pop("lon", None)
        self["lon"] = lon if lon is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.graph_objs.layout.geo import projection
