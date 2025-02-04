

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Marker(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'scatterternary.unselected'
    _path_str = 'scatterternary.unselected.marker'
    _valid_props = {"color", "opacity", "size"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker color of unselected points, applied only when a
        selection exists.

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

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the marker opacity of unselected points, applied only when
        a selection exists.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the marker size of unselected points, applied only when a
        selection exists.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the marker color of unselected points, applied
            only when a selection exists.
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.
        size
            Sets the marker size of unselected points, applied only
            when a selection exists.
        """
    def __init__(self,
            arg=None,
            color=None,
            opacity=None,
            size=None,
            **kwargs
        ):
        """
        Construct a new Marker object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.scatterternary
            .unselected.Marker`
        color
            Sets the marker color of unselected points, applied
            only when a selection exists.
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.
        size
            Sets the marker size of unselected points, applied only
            when a selection exists.

        Returns
        -------
        Marker
        """
        super().__init__('marker')
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
The first argument to the plotly.graph_objs.scatterternary.unselected.Marker
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatterternary.unselected.Marker`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('opacity', arg, opacity)
        self._init_provided('size', arg, size)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
