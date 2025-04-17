from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Camera(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.scene"
    _path_str = "layout.scene.camera"
    _valid_props = {"center", "eye", "projection", "up"}

    @property
    def center(self):
        """
        Sets the (x,y,z) components of the 'center' camera vector This
        vector determines the translation (x,y,z) space about the
        center of this scene. By default, there is no such translation.

        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.camera.Center`
          - A dict of string/value properties that will be passed
            to the Center constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Center
        """
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    @property
    def eye(self):
        """
        Sets the (x,y,z) components of the 'eye' camera vector. This
        vector determines the view point about the origin of this
        scene.

        The 'eye' property is an instance of Eye
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.camera.Eye`
          - A dict of string/value properties that will be passed
            to the Eye constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Eye
        """
        return self["eye"]

    @eye.setter
    def eye(self, val):
        self["eye"] = val

    @property
    def projection(self):
        """
        The 'projection' property is an instance of Projection
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.camera.Projection`
          - A dict of string/value properties that will be passed
            to the Projection constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Projection
        """
        return self["projection"]

    @projection.setter
    def projection(self, val):
        self["projection"] = val

    @property
    def up(self):
        """
        Sets the (x,y,z) components of the 'up' camera vector. This
        vector determines the up direction of this scene with respect
        to the page. The default is *{x: 0, y: 0, z: 1}* which means
        that the z axis points up.

        The 'up' property is an instance of Up
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.camera.Up`
          - A dict of string/value properties that will be passed
            to the Up constructor

        Returns
        -------
        plotly.graph_objs.layout.scene.camera.Up
        """
        return self["up"]

    @up.setter
    def up(self, val):
        self["up"] = val

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
        projection
            :class:`plotly.graph_objects.layout.scene.camera.Projec
            tion` instance or dict with compatible properties
        up
            Sets the (x,y,z) components of the 'up' camera vector.
            This vector determines the up direction of this scene
            with respect to the page. The default is *{x: 0, y: 0,
            z: 1}* which means that the z axis points up.
        """

    def __init__(
        self,
        arg=None,
        center: None | None = None,
        eye: None | None = None,
        projection: None | None = None,
        up: None | None = None,
        **kwargs,
    ):
        """
        Construct a new Camera object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.scene.Camera`
        center
            Sets the (x,y,z) components of the 'center' camera
            vector This vector determines the translation (x,y,z)
            space about the center of this scene. By default, there
            is no such translation.
        eye
            Sets the (x,y,z) components of the 'eye' camera vector.
            This vector determines the view point about the origin
            of this scene.
        projection
            :class:`plotly.graph_objects.layout.scene.camera.Projec
            tion` instance or dict with compatible properties
        up
            Sets the (x,y,z) components of the 'up' camera vector.
            This vector determines the up direction of this scene
            with respect to the page. The default is *{x: 0, y: 0,
            z: 1}* which means that the z axis points up.

        Returns
        -------
        Camera
        """
        super().__init__("camera")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.scene.Camera
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.scene.Camera`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("center", arg, center)
        self._init_provided("eye", arg, eye)
        self._init_provided("projection", arg, projection)
        self._init_provided("up", arg, up)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
