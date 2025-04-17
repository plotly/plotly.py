from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Lighting(_BaseTraceHierarchyType):

    _parent_path_str = "mesh3d"
    _path_str = "mesh3d.lighting"
    _valid_props = {
        "ambient",
        "diffuse",
        "facenormalsepsilon",
        "fresnel",
        "roughness",
        "specular",
        "vertexnormalsepsilon",
    }

    @property
    def ambient(self):
        """
        Ambient light increases overall color visibility but can wash
        out the image.

        The 'ambient' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["ambient"]

    @ambient.setter
    def ambient(self, val):
        self["ambient"] = val

    @property
    def diffuse(self):
        """
        Represents the extent that incident rays are reflected in a
        range of angles.

        The 'diffuse' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["diffuse"]

    @diffuse.setter
    def diffuse(self, val):
        self["diffuse"] = val

    @property
    def facenormalsepsilon(self):
        """
        Epsilon for face normals calculation avoids math issues arising
        from degenerate geometry.

        The 'facenormalsepsilon' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["facenormalsepsilon"]

    @facenormalsepsilon.setter
    def facenormalsepsilon(self, val):
        self["facenormalsepsilon"] = val

    @property
    def fresnel(self):
        """
        Represents the reflectance as a dependency of the viewing
        angle; e.g. paper is reflective when viewing it from the edge
        of the paper (almost 90 degrees), causing shine.

        The 'fresnel' property is a number and may be specified as:
          - An int or float in the interval [0, 5]

        Returns
        -------
        int|float
        """
        return self["fresnel"]

    @fresnel.setter
    def fresnel(self, val):
        self["fresnel"] = val

    @property
    def roughness(self):
        """
        Alters specular reflection; the rougher the surface, the wider
        and less contrasty the shine.

        The 'roughness' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["roughness"]

    @roughness.setter
    def roughness(self, val):
        self["roughness"] = val

    @property
    def specular(self):
        """
        Represents the level that incident rays are reflected in a
        single direction, causing shine.

        The 'specular' property is a number and may be specified as:
          - An int or float in the interval [0, 2]

        Returns
        -------
        int|float
        """
        return self["specular"]

    @specular.setter
    def specular(self, val):
        self["specular"] = val

    @property
    def vertexnormalsepsilon(self):
        """
        Epsilon for vertex normals calculation avoids math issues
        arising from degenerate geometry.

        The 'vertexnormalsepsilon' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["vertexnormalsepsilon"]

    @vertexnormalsepsilon.setter
    def vertexnormalsepsilon(self, val):
        self["vertexnormalsepsilon"] = val

    @property
    def _prop_descriptions(self):
        return """\
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
        facenormalsepsilon
            Epsilon for face normals calculation avoids math issues
            arising from degenerate geometry.
        fresnel
            Represents the reflectance as a dependency of the
            viewing angle; e.g. paper is reflective when viewing it
            from the edge of the paper (almost 90 degrees), causing
            shine.
        roughness
            Alters specular reflection; the rougher the surface,
            the wider and less contrasty the shine.
        specular
            Represents the level that incident rays are reflected
            in a single direction, causing shine.
        vertexnormalsepsilon
            Epsilon for vertex normals calculation avoids math
            issues arising from degenerate geometry.
        """

    def __init__(
        self,
        arg=None,
        ambient: int | float | None = None,
        diffuse: int | float | None = None,
        facenormalsepsilon: int | float | None = None,
        fresnel: int | float | None = None,
        roughness: int | float | None = None,
        specular: int | float | None = None,
        vertexnormalsepsilon: int | float | None = None,
        **kwargs,
    ):
        """
        Construct a new Lighting object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.mesh3d.Lighting`
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
        facenormalsepsilon
            Epsilon for face normals calculation avoids math issues
            arising from degenerate geometry.
        fresnel
            Represents the reflectance as a dependency of the
            viewing angle; e.g. paper is reflective when viewing it
            from the edge of the paper (almost 90 degrees), causing
            shine.
        roughness
            Alters specular reflection; the rougher the surface,
            the wider and less contrasty the shine.
        specular
            Represents the level that incident rays are reflected
            in a single direction, causing shine.
        vertexnormalsepsilon
            Epsilon for vertex normals calculation avoids math
            issues arising from degenerate geometry.

        Returns
        -------
        Lighting
        """
        super().__init__("lighting")
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
The first argument to the plotly.graph_objs.mesh3d.Lighting
constructor must be a dict or
an instance of :class:`plotly.graph_objs.mesh3d.Lighting`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("ambient", arg, ambient)
        self._init_provided("diffuse", arg, diffuse)
        self._init_provided("facenormalsepsilon", arg, facenormalsepsilon)
        self._init_provided("fresnel", arg, fresnel)
        self._init_provided("roughness", arg, roughness)
        self._init_provided("specular", arg, specular)
        self._init_provided("vertexnormalsepsilon", arg, vertexnormalsepsilon)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
