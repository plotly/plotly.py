from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Lighting(BaseTraceHierarchyType):

    # ambient
    # -------
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
        return self['ambient']

    @ambient.setter
    def ambient(self, val):
        self['ambient'] = val

    # diffuse
    # -------
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
        return self['diffuse']

    @diffuse.setter
    def diffuse(self, val):
        self['diffuse'] = val

    # fresnel
    # -------
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
        return self['fresnel']

    @fresnel.setter
    def fresnel(self, val):
        self['fresnel'] = val

    # roughness
    # ---------
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
        return self['roughness']

    @roughness.setter
    def roughness(self, val):
        self['roughness'] = val

    # specular
    # --------
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
        return self['specular']

    @specular.setter
    def specular(self, val):
        self['specular'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'surface'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
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
        """

    def __init__(
        self,
        arg=None,
        ambient=None,
        diffuse=None,
        fresnel=None,
        roughness=None,
        specular=None,
        **kwargs
    ):
        """
        Construct a new Lighting object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.surface.Lighting
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
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

        Returns
        -------
        Lighting
        """
        super(Lighting, self).__init__('lighting')

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
The first argument to the plotly.graph_objs.surface.Lighting 
constructor must be a dict or 
an instance of plotly.graph_objs.surface.Lighting"""
            )

        # Import validators
        # -----------------
        from plotly.validators.surface import (lighting as v_lighting)

        # Initialize validators
        # ---------------------
        self._validators['ambient'] = v_lighting.AmbientValidator()
        self._validators['diffuse'] = v_lighting.DiffuseValidator()
        self._validators['fresnel'] = v_lighting.FresnelValidator()
        self._validators['roughness'] = v_lighting.RoughnessValidator()
        self._validators['specular'] = v_lighting.SpecularValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('ambient', None)
        self.ambient = ambient if ambient is not None else _v
        _v = arg.pop('diffuse', None)
        self.diffuse = diffuse if diffuse is not None else _v
        _v = arg.pop('fresnel', None)
        self.fresnel = fresnel if fresnel is not None else _v
        _v = arg.pop('roughness', None)
        self.roughness = roughness if roughness is not None else _v
        _v = arg.pop('specular', None)
        self.specular = specular if specular is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
