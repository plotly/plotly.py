from plotly.basedatatypes import BaseLayoutHierarchyType


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
        zooming in/out. If *auto*, the autorange will be used. If
        *fixed*, the `range` is used. If *match*, the current range of
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
            when zooming in/out. If *auto*, the autorange will be
            used. If *fixed*, the `range` is used. If *match*, the
            current range of the corresponding y-axis on the main
            subplot is used.
        """

    def __init__(self, range=None, rangemode=None, **kwargs):
        """
        Construct a new YAxis object
        
        Parameters
        ----------
        range
            Sets the range of this axis for the rangeslider.
        rangemode
            Determines whether or not the range of this axis in the
            rangeslider use the same value than in the main plot
            when zooming in/out. If *auto*, the autorange will be
            used. If *fixed*, the `range` is used. If *match*, the
            current range of the corresponding y-axis on the main
            subplot is used.

        Returns
        -------
        YAxis
        """
        super(YAxis, self).__init__('yaxis')

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
        self.range = range
        self.rangemode = rangemode

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
