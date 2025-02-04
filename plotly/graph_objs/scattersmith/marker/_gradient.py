

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gradient(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'scattersmith.marker'
    _path_str = 'scattersmith.marker.gradient'
    _valid_props = {"color", "colorsrc", "type", "typesrc"}

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
          - A named CSS color
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
        Sets the source reference on Chart Studio Cloud for `color`.

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
        Sets the source reference on Chart Studio Cloud for `type`.

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
            Sets the source reference on Chart Studio Cloud for
            `color`.
        type
            Sets the type of gradient used to fill the markers
        typesrc
            Sets the source reference on Chart Studio Cloud for
            `type`.
        """
    def __init__(self,
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
            :class:`plotly.graph_objs.scattersmith.marker.Gradient`
        color
            Sets the final color of the gradient fill: the center
            color for radial, the right for horizontal, or the
            bottom for vertical.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        type
            Sets the type of gradient used to fill the markers
        typesrc
            Sets the source reference on Chart Studio Cloud for
            `type`.

        Returns
        -------
        Gradient
        """
        super().__init__('gradient')
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
The first argument to the plotly.graph_objs.scattersmith.marker.Gradient
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattersmith.marker.Gradient`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('colorsrc', arg, colorsrc)
        self._init_provided('type', arg, type)
        self._init_provided('typesrc', arg, typesrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
