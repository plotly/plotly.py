from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Starts(BaseTraceHierarchyType):

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
        Sets the source reference on plot.ly for  x .
    
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
        Sets the source reference on plot.ly for  y .
    
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
        Sets the source reference on plot.ly for  z .
    
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

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'streamtube'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            Sets the x components of the starting position of the
            streamtubes
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y components of the starting position of the
            streamtubes
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the z components of the starting position of the
            streamtubes
        zsrc
            Sets the source reference on plot.ly for  z .
        """

    def __init__(
        self,
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
            an instance of plotly.graph_objs.streamtube.Starts
        x
            Sets the x components of the starting position of the
            streamtubes
        xsrc
            Sets the source reference on plot.ly for  x .
        y
            Sets the y components of the starting position of the
            streamtubes
        ysrc
            Sets the source reference on plot.ly for  y .
        z
            Sets the z components of the starting position of the
            streamtubes
        zsrc
            Sets the source reference on plot.ly for  z .

        Returns
        -------
        Starts
        """
        super(Starts, self).__init__('starts')

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
The first argument to the plotly.graph_objs.streamtube.Starts 
constructor must be a dict or 
an instance of plotly.graph_objs.streamtube.Starts"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.streamtube import (starts as v_starts)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_starts.XValidator()
        self._validators['xsrc'] = v_starts.XsrcValidator()
        self._validators['y'] = v_starts.YValidator()
        self._validators['ysrc'] = v_starts.YsrcValidator()
        self._validators['z'] = v_starts.ZValidator()
        self._validators['zsrc'] = v_starts.ZsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('x', None)
        self['x'] = x if x is not None else _v
        _v = arg.pop('xsrc', None)
        self['xsrc'] = xsrc if xsrc is not None else _v
        _v = arg.pop('y', None)
        self['y'] = y if y is not None else _v
        _v = arg.pop('ysrc', None)
        self['ysrc'] = ysrc if ysrc is not None else _v
        _v = arg.pop('z', None)
        self['z'] = z if z is not None else _v
        _v = arg.pop('zsrc', None)
        self['zsrc'] = zsrc if zsrc is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
