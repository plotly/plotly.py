from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Spaceframe(BaseTraceHierarchyType):

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the fill ratio of the `spaceframe` elements. The default
        fill value is 0.15 meaning that only 15% of the area of every
        faces of tetras would be shaded. Applying a greater `fill`
        ratio would allow the creation of stronger elements or could be
        sued to have entirely closed areas (in case of using 1).
    
        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['fill']

    @fill.setter
    def fill(self, val):
        self['fill'] = val

    # show
    # ----
    @property
    def show(self):
        """
        Displays/hides tetrahedron shapes between minimum and maximum
        iso-values. Often useful when either caps or surfaces are
        disabled or filled with values less than 1.
    
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
        return 'isosurface'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `spaceframe` elements. The
            default fill value is 0.15 meaning that only 15% of the
            area of every faces of tetras would be shaded. Applying
            a greater `fill` ratio would allow the creation of
            stronger elements or could be sued to have entirely
            closed areas (in case of using 1).
        show
            Displays/hides tetrahedron shapes between minimum and
            maximum iso-values. Often useful when either caps or
            surfaces are disabled or filled with values less than
            1.
        """

    def __init__(self, arg=None, fill=None, show=None, **kwargs):
        """
        Construct a new Spaceframe object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.isosurface.Spaceframe
        fill
            Sets the fill ratio of the `spaceframe` elements. The
            default fill value is 0.15 meaning that only 15% of the
            area of every faces of tetras would be shaded. Applying
            a greater `fill` ratio would allow the creation of
            stronger elements or could be sued to have entirely
            closed areas (in case of using 1).
        show
            Displays/hides tetrahedron shapes between minimum and
            maximum iso-values. Often useful when either caps or
            surfaces are disabled or filled with values less than
            1.

        Returns
        -------
        Spaceframe
        """
        super(Spaceframe, self).__init__('spaceframe')

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
The first argument to the plotly.graph_objs.isosurface.Spaceframe 
constructor must be a dict or 
an instance of plotly.graph_objs.isosurface.Spaceframe"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.isosurface import (spaceframe as v_spaceframe)

        # Initialize validators
        # ---------------------
        self._validators['fill'] = v_spaceframe.FillValidator()
        self._validators['show'] = v_spaceframe.ShowValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('fill', None)
        self['fill'] = fill if fill is not None else _v
        _v = arg.pop('show', None)
        self['show'] = show if show is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
