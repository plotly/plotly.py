from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class YAxis(BaseLayoutHierarchyType):

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis for the rangeslider.
    
        The 'range' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'range[0]' property accepts values of any type
    (1) The 'range[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

    # rangemode
    # ---------
    @property
    def rangemode(self):
        """
        Determines whether or not the range of this axis in the
        rangeslider use the same value than in the main plot when
        zooming in/out. If "auto", the autorange will be used. If
        "fixed", the `range` is used. If "match", the current range of
        the corresponding y-axis on the main subplot is used.
    
        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'fixed', 'match']

        Returns
        -------
        Any
        """
        return self['rangemode']

    @rangemode.setter
    def rangemode(self, val):
        self['rangemode'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.xaxis.rangeslider'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        range
            Sets the range of this axis for the rangeslider.
        rangemode
            Determines whether or not the range of this axis in the
            rangeslider use the same value than in the main plot
            when zooming in/out. If "auto", the autorange will be
            used. If "fixed", the `range` is used. If "match", the
            current range of the corresponding y-axis on the main
            subplot is used.
        """

    def __init__(self, arg=None, range=None, rangemode=None, **kwargs):
        """
        Construct a new YAxis object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.xaxis.rangeslider.YAxis
        range
            Sets the range of this axis for the rangeslider.
        rangemode
            Determines whether or not the range of this axis in the
            rangeslider use the same value than in the main plot
            when zooming in/out. If "auto", the autorange will be
            used. If "fixed", the `range` is used. If "match", the
            current range of the corresponding y-axis on the main
            subplot is used.

        Returns
        -------
        YAxis
        """
        super(YAxis, self).__init__('yaxis')

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
The first argument to the plotly.graph_objs.layout.xaxis.rangeslider.YAxis 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.xaxis.rangeslider.YAxis"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis.rangeslider import (
            yaxis as v_yaxis
        )

        # Initialize validators
        # ---------------------
        self._validators['range'] = v_yaxis.RangeValidator()
        self._validators['rangemode'] = v_yaxis.RangemodeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('range', None)
        self.range = range if range is not None else _v
        _v = arg.pop('rangemode', None)
        self.rangemode = rangemode if rangemode is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
