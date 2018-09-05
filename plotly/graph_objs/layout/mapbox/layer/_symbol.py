from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Symbol(BaseLayoutHierarchyType):

    # icon
    # ----
    @property
    def icon(self):
        """
        Sets the symbol icon image. Full list:
        https://www.mapbox.com/maki-icons/
    
        The 'icon' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['icon']

    @icon.setter
    def icon(self, val):
        self['icon'] = val

    # iconsize
    # --------
    @property
    def iconsize(self):
        """
        Sets the symbol icon size. Has an effect only when `type` is
        set to "symbol".
    
        The 'iconsize' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['iconsize']

    @iconsize.setter
    def iconsize(self, val):
        self['iconsize'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the symbol text.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        Sets the icon text font. Has an effect only when `type` is set
        to "symbol".
    
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.layout.mapbox.layer.symbol.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
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
        plotly.graph_objs.layout.mapbox.layer.symbol.Textfont
        """
        return self['textfont']

    @textfont.setter
    def textfont(self, val):
        self['textfont'] = val

    # textposition
    # ------------
    @property
    def textposition(self):
        """
        Sets the positions of the `text` elements with respects to the
        (x,y) coordinates.
    
        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right']

        Returns
        -------
        Any
        """
        return self['textposition']

    @textposition.setter
    def textposition(self, val):
        self['textposition'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.mapbox.layer'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        icon
            Sets the symbol icon image. Full list:
            https://www.mapbox.com/maki-icons/
        iconsize
            Sets the symbol icon size. Has an effect only when
            `type` is set to "symbol".
        text
            Sets the symbol text.
        textfont
            Sets the icon text font. Has an effect only when `type`
            is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        """

    def __init__(
        self,
        arg=None,
        icon=None,
        iconsize=None,
        text=None,
        textfont=None,
        textposition=None,
        **kwargs
    ):
        """
        Construct a new Symbol object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Symbol
        icon
            Sets the symbol icon image. Full list:
            https://www.mapbox.com/maki-icons/
        iconsize
            Sets the symbol icon size. Has an effect only when
            `type` is set to "symbol".
        text
            Sets the symbol text.
        textfont
            Sets the icon text font. Has an effect only when `type`
            is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.

        Returns
        -------
        Symbol
        """
        super(Symbol, self).__init__('symbol')

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Symbol 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Symbol"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import (symbol as v_symbol)

        # Initialize validators
        # ---------------------
        self._validators['icon'] = v_symbol.IconValidator()
        self._validators['iconsize'] = v_symbol.IconsizeValidator()
        self._validators['text'] = v_symbol.TextValidator()
        self._validators['textfont'] = v_symbol.TextfontValidator()
        self._validators['textposition'] = v_symbol.TextpositionValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('icon', None)
        self.icon = icon if icon is not None else _v
        _v = arg.pop('iconsize', None)
        self.iconsize = iconsize if iconsize is not None else _v
        _v = arg.pop('text', None)
        self.text = text if text is not None else _v
        _v = arg.pop('textfont', None)
        self.textfont = textfont if textfont is not None else _v
        _v = arg.pop('textposition', None)
        self.textposition = textposition if textposition is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
