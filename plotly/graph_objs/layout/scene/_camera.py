from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Camera(BaseLayoutHierarchyType):

    # center
    # ------
    @property
    def center(self):
        """
        Sets the (x,y,z) components of the 'center' camera vector This
        vector determines the translation (x,y,z) space about the
        center of this scene. By default, there is no such translation.
    
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.camera.Center
          - A dict of string/value properties that will be passed
            to the Center constructor
    
            Supported dict properties:
                
                x
    
                y
    
                z

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Center
        """
        return self['center']

    @center.setter
    def center(self, val):
        self['center'] = val

    # eye
    # ---
    @property
    def eye(self):
        """
        Sets the (x,y,z) components of the 'eye' camera vector. This
        vector determines the view point about the origin of this
        scene.
    
        The 'eye' property is an instance of Eye
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.camera.Eye
          - A dict of string/value properties that will be passed
            to the Eye constructor
    
            Supported dict properties:
                
                x
    
                y
    
                z

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Eye
        """
        return self['eye']

    @eye.setter
    def eye(self, val):
        self['eye'] = val

    # up
    # --
    @property
    def up(self):
        """
        Sets the (x,y,z) components of the 'up' camera vector. This
        vector determines the up direction of this scene with respect
        to the page. The default is *{x: 0, y: 0, z: 1}* which means
        that the z axis points up.
    
        The 'up' property is an instance of Up
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.camera.Up
          - A dict of string/value properties that will be passed
            to the Up constructor
    
            Supported dict properties:
                
                x
    
                y
    
                z

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Up
        """
        return self['up']

    @up.setter
    def up(self, val):
        self['up'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.scene'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        center
            Sets the (x,y,z) components of the 'center' camera
            vector This vector determines the translation (x,y,z)
            space about the center of this scene. By default, there
            is no such translation.
        eye
            Sets the (x,y,z) components of the 'eye' camera vector.
            This vector determines the view point about the origin
            of this scene.
        up
            Sets the (x,y,z) components of the 'up' camera vector.
            This vector determines the up direction of this scene
            with respect to the page. The default is *{x: 0, y: 0,
            z: 1}* which means that the z axis points up.
        """

    def __init__(self, arg=None, center=None, eye=None, up=None, **kwargs):
        """
        Construct a new Camera object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.scene.Camera
        center
            Sets the (x,y,z) components of the 'center' camera
            vector This vector determines the translation (x,y,z)
            space about the center of this scene. By default, there
            is no such translation.
        eye
            Sets the (x,y,z) components of the 'eye' camera vector.
            This vector determines the view point about the origin
            of this scene.
        up
            Sets the (x,y,z) components of the 'up' camera vector.
            This vector determines the up direction of this scene
            with respect to the page. The default is *{x: 0, y: 0,
            z: 1}* which means that the z axis points up.

        Returns
        -------
        Camera
        """
        super(Camera, self).__init__('camera')

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
The first argument to the plotly.graph_objs.layout.scene.Camera 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.scene.Camera"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.scene import (camera as v_camera)

        # Initialize validators
        # ---------------------
        self._validators['center'] = v_camera.CenterValidator()
        self._validators['eye'] = v_camera.EyeValidator()
        self._validators['up'] = v_camera.UpValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('center', None)
        self['center'] = center if center is not None else _v
        _v = arg.pop('eye', None)
        self['eye'] = eye if eye is not None else _v
        _v = arg.pop('up', None)
        self['up'] = up if up is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
