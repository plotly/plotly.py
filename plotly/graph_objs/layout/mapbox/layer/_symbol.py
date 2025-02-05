

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Symbol(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout.mapbox.layer'
    _path_str = 'layout.mapbox.layer.symbol'
    _valid_props = {"icon", "iconsize", "placement", "text", "textfont", "textposition"}

    # icon
    # ----
    @property
    def icon(self):
        """
        Sets the symbol icon image (mapbox.layer.layout.icon-image).
        Full list: https://www.mapbox.com/maki-icons/

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
        Sets the symbol icon size (mapbox.layer.layout.icon-size). Has
        an effect only when `type` is set to "symbol".

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

    # placement
    # ---------
    @property
    def placement(self):
        """
        Sets the symbol and/or text placement
        (mapbox.layer.layout.symbol-placement). If `placement` is
        "point", the label is placed where the geometry is located If
        `placement` is "line", the label is placed along the line of
        the geometry If `placement` is "line-center", the label is
        placed on the center of the geometry

        The 'placement' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['point', 'line', 'line-center']

        Returns
        -------
        Any
        """
        return self['placement']

    @placement.setter
    def placement(self, val):
        self['placement'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the symbol text (mapbox.layer.layout.text-field).

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
        Sets the icon text font (color=mapbox.layer.paint.text-color,
        size=mapbox.layer.layout.text-size). Has an effect only when
        `type` is set to "symbol".

        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.mapbox.layer.symbol.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor

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

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        icon
            Sets the symbol icon image (mapbox.layer.layout.icon-
            image). Full list: https://www.mapbox.com/maki-icons/
        iconsize
            Sets the symbol icon size (mapbox.layer.layout.icon-
            size). Has an effect only when `type` is set to
            "symbol".
        placement
            Sets the symbol and/or text placement
            (mapbox.layer.layout.symbol-placement). If `placement`
            is "point", the label is placed where the geometry is
            located If `placement` is "line", the label is placed
            along the line of the geometry If `placement` is "line-
            center", the label is placed on the center of the
            geometry
        text
            Sets the symbol text (mapbox.layer.layout.text-field).
        textfont
            Sets the icon text font (color=mapbox.layer.paint.text-
            color, size=mapbox.layer.layout.text-size). Has an
            effect only when `type` is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        """
    def __init__(self,
            arg=None,
            icon: str|None = None,
            iconsize: int|float|None = None,
            placement: Any|None = None,
            text: str|None = None,
            textfont: None|None = None,
            textposition: Any|None = None,
            **kwargs
        ):
        """
        Construct a new Symbol object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.mapbox.layer.Symbol`
        icon
            Sets the symbol icon image (mapbox.layer.layout.icon-
            image). Full list: https://www.mapbox.com/maki-icons/
        iconsize
            Sets the symbol icon size (mapbox.layer.layout.icon-
            size). Has an effect only when `type` is set to
            "symbol".
        placement
            Sets the symbol and/or text placement
            (mapbox.layer.layout.symbol-placement). If `placement`
            is "point", the label is placed where the geometry is
            located If `placement` is "line", the label is placed
            along the line of the geometry If `placement` is "line-
            center", the label is placed on the center of the
            geometry
        text
            Sets the symbol text (mapbox.layer.layout.text-field).
        textfont
            Sets the icon text font (color=mapbox.layer.paint.text-
            color, size=mapbox.layer.layout.text-size). Has an
            effect only when `type` is set to "symbol".
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.

        Returns
        -------
        Symbol
        """
        super().__init__('symbol')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
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
            raise ValueError("""\
The first argument to the plotly.graph_objs.layout.mapbox.layer.Symbol
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.mapbox.layer.Symbol`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('icon', arg, icon)
        self._init_provided('iconsize', arg, iconsize)
        self._init_provided('placement', arg, placement)
        self._init_provided('text', arg, text)
        self._init_provided('textfont', arg, textfont)
        self._init_provided('textposition', arg, textposition)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
