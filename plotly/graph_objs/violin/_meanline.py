

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Meanline(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'violin'
    _path_str = 'violin.meanline'
    _valid_props = {"color", "visible", "width"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the mean line color.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines if a line corresponding to the sample's mean is
        shown inside the violins. If `box.visible` is turned on, the
        mean line is drawn inside the inner box. Otherwise, the mean
        line is drawn from one side of the violin to other.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the mean line width.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the mean line color.
        visible
            Determines if a line corresponding to the sample's mean
            is shown inside the violins. If `box.visible` is turned
            on, the mean line is drawn inside the inner box.
            Otherwise, the mean line is drawn from one side of the
            violin to other.
        width
            Sets the mean line width.
        """
    def __init__(self,
            arg=None,
            color: str|None = None,
            visible: bool|None = None,
            width: int|float|None = None,
            **kwargs
        ):
        """
        Construct a new Meanline object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.violin.Meanline`
        color
            Sets the mean line color.
        visible
            Determines if a line corresponding to the sample's mean
            is shown inside the violins. If `box.visible` is turned
            on, the mean line is drawn inside the inner box.
            Otherwise, the mean line is drawn from one side of the
            violin to other.
        width
            Sets the mean line width.

        Returns
        -------
        Meanline
        """
        super().__init__('meanline')
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
The first argument to the plotly.graph_objs.violin.Meanline
constructor must be a dict or
an instance of :class:`plotly.graph_objs.violin.Meanline`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('visible', arg, visible)
        self._init_provided('width', arg, width)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
