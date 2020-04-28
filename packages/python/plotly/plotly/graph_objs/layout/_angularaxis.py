from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class AngularAxis(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout"
    _path_str = "layout.angularaxis"
    _valid_props = {
        "domain",
        "endpadding",
        "range",
        "showline",
        "showticklabels",
        "tickcolor",
        "ticklen",
        "tickorientation",
        "ticksuffix",
        "visible",
    }

    # domain
    # ------
    @property
    def domain(self):
        """
        Polar chart subplots are not supported yet. This key has
        currently no effect.
    
        The 'domain' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'domain[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'domain[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    # endpadding
    # ----------
    @property
    def endpadding(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots.
    
        The 'endpadding' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["endpadding"]

    @endpadding.setter
    def endpadding(self, val):
        self["endpadding"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Defines the start and end point of this angular axis.
    
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

    # showline
    # --------
    @property
    def showline(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not the line bounding this
        angular axis will be shown on the figure.
    
        The 'showline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showline"]

    @showline.setter
    def showline(self, val):
        self["showline"] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not the angular axis ticks will
        feature tick labels.
    
        The 'showticklabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showticklabels"]

    @showticklabels.setter
    def showticklabels(self, val):
        self["showticklabels"] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the color of the tick lines on this angular
        axis.
    
        The 'tickcolor' property is a color and may be specified as:
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
        return self["tickcolor"]

    @tickcolor.setter
    def tickcolor(self, val):
        self["tickcolor"] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the length of the tick lines on this angular
        axis.
    
        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["ticklen"]

    @ticklen.setter
    def ticklen(self, val):
        self["ticklen"] = val

    # tickorientation
    # ---------------
    @property
    def tickorientation(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the orientation (from the paper perspective) of
        the angular axis tick labels.
    
        The 'tickorientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['horizontal', 'vertical']

        Returns
        -------
        Any
        """
        return self["tickorientation"]

    @tickorientation.setter
    def tickorientation(self, val):
        self["tickorientation"] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Sets the length of the tick lines on this angular
        axis.
    
        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["ticksuffix"]

    @ticksuffix.setter
    def ticksuffix(self, val):
        self["ticksuffix"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Legacy polar charts are deprecated! Please switch to "polar"
        subplots. Determines whether or not this axis will be visible.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots.
        range
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Defines the start and end point of
            this angular axis.
        showline
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the line
            bounding this angular axis will be shown on the figure.
        showticklabels
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the angular
            axis ticks will feature tick labels.
        tickcolor
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the color of the tick lines on
            this angular axis.
        ticklen
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        tickorientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (from the paper
            perspective) of the angular axis tick labels.
        ticksuffix
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        visible
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not this axis
            will be visible.
        """

    def __init__(
        self,
        arg=None,
        domain=None,
        endpadding=None,
        range=None,
        showline=None,
        showticklabels=None,
        tickcolor=None,
        ticklen=None,
        tickorientation=None,
        ticksuffix=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new AngularAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.AngularAxis`
        domain
            Polar chart subplots are not supported yet. This key
            has currently no effect.
        endpadding
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots.
        range
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Defines the start and end point of
            this angular axis.
        showline
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the line
            bounding this angular axis will be shown on the figure.
        showticklabels
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not the angular
            axis ticks will feature tick labels.
        tickcolor
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the color of the tick lines on
            this angular axis.
        ticklen
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        tickorientation
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the orientation (from the paper
            perspective) of the angular axis tick labels.
        ticksuffix
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Sets the length of the tick lines on
            this angular axis.
        visible
            Legacy polar charts are deprecated! Please switch to
            "polar" subplots. Determines whether or not this axis
            will be visible.

        Returns
        -------
        AngularAxis
        """
        super(AngularAxis, self).__init__("angularaxis")

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
The first argument to the plotly.graph_objs.layout.AngularAxis 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.AngularAxis`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("endpadding", None)
        _v = endpadding if endpadding is not None else _v
        if _v is not None:
            self["endpadding"] = _v
        _v = arg.pop("range", None)
        _v = range if range is not None else _v
        if _v is not None:
            self["range"] = _v
        _v = arg.pop("showline", None)
        _v = showline if showline is not None else _v
        if _v is not None:
            self["showline"] = _v
        _v = arg.pop("showticklabels", None)
        _v = showticklabels if showticklabels is not None else _v
        if _v is not None:
            self["showticklabels"] = _v
        _v = arg.pop("tickcolor", None)
        _v = tickcolor if tickcolor is not None else _v
        if _v is not None:
            self["tickcolor"] = _v
        _v = arg.pop("ticklen", None)
        _v = ticklen if ticklen is not None else _v
        if _v is not None:
            self["ticklen"] = _v
        _v = arg.pop("tickorientation", None)
        _v = tickorientation if tickorientation is not None else _v
        if _v is not None:
            self["tickorientation"] = _v
        _v = arg.pop("ticksuffix", None)
        _v = ticksuffix if ticksuffix is not None else _v
        if _v is not None:
            self["ticksuffix"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
