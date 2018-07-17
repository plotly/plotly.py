from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Gradient(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the final color of the gradient fill: the center color for
        radial, the right for horizontal, or the bottom for vertical.
    
        The 'color' property is a color and may be specified as:
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
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
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

    # type
    # ----
    @property
    def type(self):
        """
        Sets the type of gradient used to fill the markers
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['radial', 'horizontal', 'vertical', 'none']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # typesrc
    # -------
    @property
    def typesrc(self):
        """
        Sets the source reference on plot.ly for  type .
    
        The 'typesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['typesrc']

    @typesrc.setter
    def typesrc(self, val):
        self['typesrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scattergeo.marker'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the final color of the gradient fill: the center
            color for radial, the right for horizontal, or the
            bottom for vertical.
        colorsrc
            Sets the source reference on plot.ly for  color .
        type
            Sets the type of gradient used to fill the markers
        typesrc
            Sets the source reference on plot.ly for  type .
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        type=None,
        typesrc=None,
        **kwargs
    ):
        """
        Construct a new Gradient object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.scattergeo.marker.Gradient
        color
            Sets the final color of the gradient fill: the center
            color for radial, the right for horizontal, or the
            bottom for vertical.
        colorsrc
            Sets the source reference on plot.ly for  color .
        type
            Sets the type of gradient used to fill the markers
        typesrc
            Sets the source reference on plot.ly for  type .

        Returns
        -------
        Gradient
        """
        super(Gradient, self).__init__('gradient')

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
The first argument to the plotly.graph_objs.scattergeo.marker.Gradient 
constructor must be a dict or 
an instance of plotly.graph_objs.scattergeo.marker.Gradient"""
            )

        # Import validators
        # -----------------
        from plotly.validators.scattergeo.marker import (
            gradient as v_gradient
        )

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_gradient.ColorValidator()
        self._validators['colorsrc'] = v_gradient.ColorsrcValidator()
        self._validators['type'] = v_gradient.TypeValidator()
        self._validators['typesrc'] = v_gradient.TypesrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v
        _v = arg.pop('colorsrc', None)
        self.colorsrc = colorsrc if colorsrc is not None else _v
        _v = arg.pop('type', None)
        self.type = type if type is not None else _v
        _v = arg.pop('typesrc', None)
        self.typesrc = typesrc if typesrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
