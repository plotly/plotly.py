from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Circle(BaseLayoutHierarchyType):

    # radius
    # ------
    @property
    def radius(self):
        """
        Sets the circle radius. Has an effect only when `type` is set
        to "circle".
    
        The 'radius' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['radius']

    @radius.setter
    def radius(self, val):
        self['radius'] = val

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
        radius
            Sets the circle radius. Has an effect only when `type`
            is set to "circle".
        """

    def __init__(self, arg=None, radius=None, **kwargs):
        """
        Construct a new Circle object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Circle
        radius
            Sets the circle radius. Has an effect only when `type`
            is set to "circle".

        Returns
        -------
        Circle
        """
        super(Circle, self).__init__('circle')

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
The first argument to the plotly.graph_objs.layout.mapbox.layer.Circle 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Circle"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import (circle as v_circle)

        # Initialize validators
        # ---------------------
        self._validators['radius'] = v_circle.RadiusValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('radius', None)
        self.radius = radius if radius is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
