from plotly.basedatatypes import BaseTraceHierarchyType


class YBins(BaseTraceHierarchyType):

    # end
    # ---
    @property
    def end(self):
        """
        Sets the end value for the y axis bins.
    
        The 'end' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['end']

    @end.setter
    def end(self, val):
        self['end'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the step in-between value each y axis bin.
    
        The 'size' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # start
    # -----
    @property
    def start(self):
        """
        Sets the starting value for the y axis bins.
    
        The 'start' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['start']

    @start.setter
    def start(self, val):
        self['start'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'histogram2dcontour'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        end
            Sets the end value for the y axis bins.
        size
            Sets the step in-between value each y axis bin.
        start
            Sets the starting value for the y axis bins.
        """

    def __init__(self, end=None, size=None, start=None, **kwargs):
        """
        Construct a new YBins object
        
        Parameters
        ----------
        end
            Sets the end value for the y axis bins.
        size
            Sets the step in-between value each y axis bin.
        start
            Sets the starting value for the y axis bins.

        Returns
        -------
        YBins
        """
        super(YBins, self).__init__('ybins')

        # Import validators
        # -----------------
        from plotly.validators.histogram2dcontour import (ybins as v_ybins)

        # Initialize validators
        # ---------------------
        self._validators['end'] = v_ybins.EndValidator()
        self._validators['size'] = v_ybins.SizeValidator()
        self._validators['start'] = v_ybins.StartValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.end = end
        self.size = size
        self.start = start

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
