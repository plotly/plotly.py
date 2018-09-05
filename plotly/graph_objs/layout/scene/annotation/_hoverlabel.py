from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Hoverlabel(BaseLayoutHierarchyType):

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the hover label. By default uses
        the annotation's `bgcolor` made opaque, or white if it was
        transparent.
    
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
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the border color of the hover label. By default uses
        either dark grey or white, for maximum contrast with
        `hoverlabel.bgcolor`.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self['bordercolor']

    @bordercolor.setter
    def bordercolor(self, val):
        self['bordercolor'] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the hover label text font. By default uses the global
        hover font and size, with color from `hoverlabel.bordercolor`.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.annotation.hoverlabel.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
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
        plotly.graph_objs.layout.scene.annotation.hoverlabel.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.scene.annotation'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            Sets the background color of the hover label. By
            default uses the annotation's `bgcolor` made opaque, or
            white if it was transparent.
        bordercolor
            Sets the border color of the hover label. By default
            uses either dark grey or white, for maximum contrast
            with `hoverlabel.bgcolor`.
        font
            Sets the hover label text font. By default uses the
            global hover font and size, with color from
            `hoverlabel.bordercolor`.
        """

    def __init__(
        self, arg=None, bgcolor=None, bordercolor=None, font=None, **kwargs
    ):
        """
        Construct a new Hoverlabel object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.scene.annotation.Hoverlabel
        bgcolor
            Sets the background color of the hover label. By
            default uses the annotation's `bgcolor` made opaque, or
            white if it was transparent.
        bordercolor
            Sets the border color of the hover label. By default
            uses either dark grey or white, for maximum contrast
            with `hoverlabel.bgcolor`.
        font
            Sets the hover label text font. By default uses the
            global hover font and size, with color from
            `hoverlabel.bordercolor`.

        Returns
        -------
        Hoverlabel
        """
        super(Hoverlabel, self).__init__('hoverlabel')

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
The first argument to the plotly.graph_objs.layout.scene.annotation.Hoverlabel 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.scene.annotation.Hoverlabel"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.scene.annotation import (
            hoverlabel as v_hoverlabel
        )

        # Initialize validators
        # ---------------------
        self._validators['bgcolor'] = v_hoverlabel.BgcolorValidator()
        self._validators['bordercolor'] = v_hoverlabel.BordercolorValidator()
        self._validators['font'] = v_hoverlabel.FontValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('bgcolor', None)
        self.bgcolor = bgcolor if bgcolor is not None else _v
        _v = arg.pop('bordercolor', None)
        self.bordercolor = bordercolor if bordercolor is not None else _v
        _v = arg.pop('font', None)
        self.font = font if font is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
