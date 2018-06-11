from plotly.basedatatypes import BaseTraceHierarchyType


class Stream(BaseTraceHierarchyType):

    # maxpoints
    # ---------
    @property
    def maxpoints(self):
        """
        Sets the maximum number of points to keep on the plots from an
        incoming stream. If `maxpoints` is set to *50*, only the newest
        50 points will be displayed on the plot.
    
        The 'maxpoints' property is a number and may be specified as:
          - An int or float in the interval [0, 10000]

        Returns
        -------
        int|float
        """
        return self['maxpoints']

    @maxpoints.setter
    def maxpoints(self, val):
        self['maxpoints'] = val

    # token
    # -----
    @property
    def token(self):
        """
        The stream id number links a data trace on a plot with a
        stream. See https://plot.ly/settings for more details.
    
        The 'token' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self['token']

    @token.setter
    def token(self, val):
        self['token'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'splom'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to *50*,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.
        """

    def __init__(self, maxpoints=None, token=None, **kwargs):
        """
        Construct a new Stream object
        
        Parameters
        ----------
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to *50*,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://plot.ly/settings for more
            details.

        Returns
        -------
        Stream
        """
        super(Stream, self).__init__('stream')

        # Import validators
        # -----------------
        from plotly.validators.splom import (stream as v_stream)

        # Initialize validators
        # ---------------------
        self._validators['maxpoints'] = v_stream.MaxpointsValidator()
        self._validators['token'] = v_stream.TokenValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.maxpoints = maxpoints
        self.token = token

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
