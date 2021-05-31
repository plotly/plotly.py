from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Pattern(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "barpolar.marker"
    _path_str = "barpolar.marker.pattern"
    _valid_props = {
        "bgcolor",
        "bgcolorsrc",
        "shape",
        "shapesrc",
        "size",
        "sizesrc",
        "solidity",
        "soliditysrc",
    }

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the pattern fill. Defaults to a
        transparent background.
    
        The 'bgcolor' property is a color and may be specified as:
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bgcolorsrc
    # ----------
    @property
    def bgcolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  bgcolor .
    
        The 'bgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bgcolorsrc"]

    @bgcolorsrc.setter
    def bgcolorsrc(self, val):
        self["bgcolorsrc"] = val

    # shape
    # -----
    @property
    def shape(self):
        """
        Sets the shape of the pattern fill. By default, no pattern is
        used for filling the area.
    
        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['', '\\', 'x', '-', '|', '+', '.']
          - A string that matches one of the following regular expressions:
                ['']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    # shapesrc
    # --------
    @property
    def shapesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  shape .
    
        The 'shapesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["shapesrc"]

    @shapesrc.setter
    def shapesrc(self, val):
        self["shapesrc"] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the size of unit squares of the pattern fill in pixels,
        which corresponds to the interval of repetition of the pattern.
    
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  size .
    
        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

    # solidity
    # --------
    @property
    def solidity(self):
        """
        Sets the solidity of the pattern fill. Solidity is roughly the
        fraction of the area filled by the pattern. Solidity of 0 shows
        only the background color without pattern and solidty of 1
        shows only the foreground color without pattern.
    
        The 'solidity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["solidity"]

    @solidity.setter
    def solidity(self, val):
        self["solidity"] = val

    # soliditysrc
    # -----------
    @property
    def soliditysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for  solidity .
    
        The 'soliditysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["soliditysrc"]

    @soliditysrc.setter
    def soliditysrc(self, val):
        self["soliditysrc"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Sets the background color of the pattern fill. Defaults
            to a transparent background.
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            bgcolor .
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        shapesrc
            Sets the source reference on Chart Studio Cloud for
            shape .
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.
        soliditysrc
            Sets the source reference on Chart Studio Cloud for
            solidity .
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        bgcolorsrc=None,
        shape=None,
        shapesrc=None,
        size=None,
        sizesrc=None,
        solidity=None,
        soliditysrc=None,
        **kwargs
    ):
        """
        Construct a new Pattern object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.barpolar.marker.Pattern`
        bgcolor
            Sets the background color of the pattern fill. Defaults
            to a transparent background.
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            bgcolor .
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        shapesrc
            Sets the source reference on Chart Studio Cloud for
            shape .
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            size .
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.
        soliditysrc
            Sets the source reference on Chart Studio Cloud for
            solidity .

        Returns
        -------
        Pattern
        """
        super(Pattern, self).__init__("pattern")

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
The first argument to the plotly.graph_objs.barpolar.marker.Pattern 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.barpolar.marker.Pattern`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("bgcolorsrc", None)
        _v = bgcolorsrc if bgcolorsrc is not None else _v
        if _v is not None:
            self["bgcolorsrc"] = _v
        _v = arg.pop("shape", None)
        _v = shape if shape is not None else _v
        if _v is not None:
            self["shape"] = _v
        _v = arg.pop("shapesrc", None)
        _v = shapesrc if shapesrc is not None else _v
        if _v is not None:
            self["shapesrc"] = _v
        _v = arg.pop("size", None)
        _v = size if size is not None else _v
        if _v is not None:
            self["size"] = _v
        _v = arg.pop("sizesrc", None)
        _v = sizesrc if sizesrc is not None else _v
        if _v is not None:
            self["sizesrc"] = _v
        _v = arg.pop("solidity", None)
        _v = solidity if solidity is not None else _v
        if _v is not None:
            self["solidity"] = _v
        _v = arg.pop("soliditysrc", None)
        _v = soliditysrc if soliditysrc is not None else _v
        if _v is not None:
            self["soliditysrc"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
