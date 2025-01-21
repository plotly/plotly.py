

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Starts(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'streamtube'
    _path_str = 'streamtube.starts'
    _valid_props = {"x", "xsrc", "y", "ysrc", "z", "zsrc"}

    # x
    # -
    @property
    def x(self):
        """
        Sets the x components of the starting position of the
        streamtubes

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['xsrc']

    @xsrc.setter
    def xsrc(self, val):
        self['xsrc'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y components of the starting position of the
        streamtubes

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ysrc']

    @ysrc.setter
    def ysrc(self, val):
        self['ysrc'] = val

    # z
    # -
    @property
    def z(self):
        """
        Sets the z components of the starting position of the
        streamtubes

        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # zsrc
    # ----
    @property
    def zsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `z`.

        The 'zsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['zsrc']

    @zsrc.setter
    def zsrc(self, val):
        self['zsrc'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            Sets the x components of the starting position of the
            streamtubes
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y components of the starting position of the
            streamtubes
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the z components of the starting position of the
            streamtubes
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.
        """
    def __init__(self,
            arg=None,
            x=None,
            xsrc=None,
            y=None,
            ysrc=None,
            z=None,
            zsrc=None,
            **kwargs
        ):
        """
        Construct a new Starts object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.streamtube.Starts`
        x
            Sets the x components of the starting position of the
            streamtubes
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y components of the starting position of the
            streamtubes
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the z components of the starting position of the
            streamtubes
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Starts
        """
        super(Starts, self).__init__('starts')

        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.streamtube.Starts
constructor must be a dict or
an instance of :class:`plotly.graph_objs.streamtube.Starts`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('x', arg, x)
        self._init_provided('xsrc', arg, xsrc)
        self._init_provided('y', arg, y)
        self._init_provided('ysrc', arg, ysrc)
        self._init_provided('z', arg, z)
        self._init_provided('zsrc', arg, zsrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
