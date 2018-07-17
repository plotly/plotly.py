from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class X(BaseTraceHierarchyType):

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the projection color.
    
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

    # scale
    # -----
    @property
    def scale(self):
        """
        Sets the scale factor determining the size of the projection
        marker points.
    
        The 'scale' property is a number and may be specified as:
          - An int or float in the interval [0, 10]

        Returns
        -------
        int|float
        """
        return self['scale']

    @scale.setter
    def scale(self, val):
        self['scale'] = val

    # show
    # ----
    @property
    def show(self):
        """
        Sets whether or not projections are shown along the x axis.
    
        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['show']

    @show.setter
    def show(self, val):
        self['show'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scatter3d.projection'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        opacity
            Sets the projection color.
        scale
            Sets the scale factor determining the size of the
            projection marker points.
        show
            Sets whether or not projections are shown along the x
            axis.
        """

    def __init__(
        self, arg=None, opacity=None, scale=None, show=None, **kwargs
    ):
        """
        Construct a new X object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.scatter3d.projection.X
        opacity
            Sets the projection color.
        scale
            Sets the scale factor determining the size of the
            projection marker points.
        show
            Sets whether or not projections are shown along the x
            axis.

        Returns
        -------
        X
        """
        super(X, self).__init__('x')

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
The first argument to the plotly.graph_objs.scatter3d.projection.X 
constructor must be a dict or 
an instance of plotly.graph_objs.scatter3d.projection.X"""
            )

        # Import validators
        # -----------------
        from plotly.validators.scatter3d.projection import (x as v_x)

        # Initialize validators
        # ---------------------
        self._validators['opacity'] = v_x.OpacityValidator()
        self._validators['scale'] = v_x.ScaleValidator()
        self._validators['show'] = v_x.ShowValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('scale', None)
        self.scale = scale if scale is not None else _v
        _v = arg.pop('show', None)
        self.show = show if show is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
