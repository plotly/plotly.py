from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Border(BaseTraceHierarchyType):

    # arearatio
    # ---------
    @property
    def arearatio(self):
        """
        Specifies what fraction of the marker area is covered with the
        border.
    
        The 'arearatio' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['arearatio']

    @arearatio.setter
    def arearatio(self, val):
        self['arearatio'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the stroke color. It accepts a specific color. If the
        color is not fully opaque and there are hundreds of thousands
        of points, it may cause slower zooming and panning.
    
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

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'pointcloud.marker'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        arearatio
            Specifies what fraction of the marker area is covered
            with the border.
        color
            Sets the stroke color. It accepts a specific color. If
            the color is not fully opaque and there are hundreds of
            thousands of points, it may cause slower zooming and
            panning.
        """

    def __init__(self, arg=None, arearatio=None, color=None, **kwargs):
        """
        Construct a new Border object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.pointcloud.marker.Border
        arearatio
            Specifies what fraction of the marker area is covered
            with the border.
        color
            Sets the stroke color. It accepts a specific color. If
            the color is not fully opaque and there are hundreds of
            thousands of points, it may cause slower zooming and
            panning.

        Returns
        -------
        Border
        """
        super(Border, self).__init__('border')

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
The first argument to the plotly.graph_objs.pointcloud.marker.Border 
constructor must be a dict or 
an instance of plotly.graph_objs.pointcloud.marker.Border"""
            )

        # Import validators
        # -----------------
        from plotly.validators.pointcloud.marker import (border as v_border)

        # Initialize validators
        # ---------------------
        self._validators['arearatio'] = v_border.ArearatioValidator()
        self._validators['color'] = v_border.ColorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('arearatio', None)
        self.arearatio = arearatio if arearatio is not None else _v
        _v = arg.pop('color', None)
        self.color = color if color is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
