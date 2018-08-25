from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Axis(BaseTraceHierarchyType):

    # type
    # ----
    @property
    def type(self):
        """
        Sets the axis type for this dimension's generated x and y axes.
        Note that the axis `type` values set in layout take precedence
        over this attribute.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'log', 'date', 'category']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'splom.dimension'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        type
            Sets the axis type for this dimension's generated x and
            y axes. Note that the axis `type` values set in layout
            take precedence over this attribute.
        """

    def __init__(self, arg=None, type=None, **kwargs):
        """
        Construct a new Axis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.splom.dimension.Axis
        type
            Sets the axis type for this dimension's generated x and
            y axes. Note that the axis `type` values set in layout
            take precedence over this attribute.

        Returns
        -------
        Axis
        """
        super(Axis, self).__init__('axis')

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
The first argument to the plotly.graph_objs.splom.dimension.Axis 
constructor must be a dict or 
an instance of plotly.graph_objs.splom.dimension.Axis"""
            )

        # Import validators
        # -----------------
        from plotly.validators.splom.dimension import (axis as v_axis)

        # Initialize validators
        # ---------------------
        self._validators['type'] = v_axis.TypeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('type', None)
        self.type = type if type is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
