from plotly.basedatatypes import BaseLayoutHierarchyType


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

    def __init__(self, center=None, eye=None, up=None, **kwargs):
        """
        Construct a new Camera object
        
        Parameters
        ----------
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
        self.center = center
        self.eye = eye
        self.up = up

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
