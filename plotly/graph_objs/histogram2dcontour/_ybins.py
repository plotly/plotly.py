from plotly.basedatatypes import BaseTraceHierarchyType
import copy


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

    def __init__(self, arg=None, end=None, size=None, start=None, **kwargs):
        """
        Construct a new YBins object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.histogram2dcontour.YBins
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
The first argument to the plotly.graph_objs.histogram2dcontour.YBins 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram2dcontour.YBins"""
            )

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
        _v = arg.pop('end', None)
        self.end = end if end is not None else _v
        _v = arg.pop('size', None)
        self.size = size if size is not None else _v
        _v = arg.pop('start', None)
        self.start = start if start is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
