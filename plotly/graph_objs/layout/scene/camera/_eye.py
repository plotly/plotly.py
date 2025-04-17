from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Eye(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.scene.camera"
    _path_str = "layout.scene.camera.eye"
    _valid_props = {"x", "y", "z"}

    @property
    def x(self):
        """
        The 'x' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    @property
    def y(self):
        """
        The 'y' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    @property
    def z(self):
        """
        The 'z' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["z"]

    @z.setter
    def z(self, val):
        self["z"] = val

    @property
    def _prop_descriptions(self):
        return """\
        x

        y

        z

        """

    def __init__(
        self,
        arg=None,
        x: int | float | None = None,
        y: int | float | None = None,
        z: int | float | None = None,
        **kwargs,
    ):
        """
        Construct a new Eye object

        Sets the (x,y,z) components of the 'eye' camera vector. This
        vector determines the view point about the origin of this
        scene.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.scene.camera.Eye`
        x

        y

        z


        Returns
        -------
        Eye
        """
        super().__init__("eye")
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
The first argument to the plotly.graph_objs.layout.scene.camera.Eye
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.scene.camera.Eye`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("x", arg, x)
        self._init_provided("y", arg, y)
        self._init_provided("z", arg, z)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
