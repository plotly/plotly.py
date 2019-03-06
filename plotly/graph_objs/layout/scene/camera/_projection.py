from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Projection(BaseLayoutHierarchyType):

    # type
    # ----
    @property
    def type(self):
        """
        Sets the projection type. The projection type could be either
        "perspective" or "orthographic". The default is "perspective".
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['perspective', 'orthographic']

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
        return 'layout.scene.camera'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        type
            Sets the projection type. The projection type could be
            either "perspective" or "orthographic". The default is
            "perspective".
        """

    def __init__(self, arg=None, type=None, **kwargs):
        """
        Construct a new Projection object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.scene.camera.Projection
        type
            Sets the projection type. The projection type could be
            either "perspective" or "orthographic". The default is
            "perspective".

        Returns
        -------
        Projection
        """
        super(Projection, self).__init__('projection')

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
The first argument to the plotly.graph_objs.layout.scene.camera.Projection 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.scene.camera.Projection"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.scene.camera import (
            projection as v_projection
        )

        # Initialize validators
        # ---------------------
        self._validators['type'] = v_projection.TypeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('type', None)
        self['type'] = type if type is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
