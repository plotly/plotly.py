from plotly.basedatatypes import BaseTraceHierarchyType


class Line(BaseTraceHierarchyType):

    # dash
    # ----
    @property
    def dash(self):
        """
        Sets the dash style of lines. Set to a dash type string
        (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
        *longdashdot*) or a dash length list in px (eg
        *5px,10px,2px,2px*). Note that this style setting can also be
        set per direction via `increasing.line.dash` and
        `decreasing.line.dash`.
    
        The 'dash' property is a string and must be specified as:
          - One of the following strings:
                ['solid', 'dot', 'dash', 'longdash', 'dashdot',
                'longdashdot']
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['dash']

    @dash.setter
    def dash(self, val):
        self['dash'] = val

    # width
    # -----
    @property
    def width(self):
        """
        [object Object] Note that this style setting can also be set
        per direction via `increasing.line.width` and
        `decreasing.line.width`.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'ohlc'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dash
            Sets the dash style of lines. Set to a dash type string
            (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
            *longdashdot*) or a dash length list in px (eg
            *5px,10px,2px,2px*). Note that this style setting can
            also be set per direction via `increasing.line.dash`
            and `decreasing.line.dash`.
        width
            [object Object] Note that this style setting can also
            be set per direction via `increasing.line.width` and
            `decreasing.line.width`.
        """

    def __init__(self, dash=None, width=None, **kwargs):
        """
        Construct a new Line object
        
        Parameters
        ----------
        dash
            Sets the dash style of lines. Set to a dash type string
            (*solid*, *dot*, *dash*, *longdash*, *dashdot*, or
            *longdashdot*) or a dash length list in px (eg
            *5px,10px,2px,2px*). Note that this style setting can
            also be set per direction via `increasing.line.dash`
            and `decreasing.line.dash`.
        width
            [object Object] Note that this style setting can also
            be set per direction via `increasing.line.width` and
            `decreasing.line.width`.

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

        # Import validators
        # -----------------
        from plotly.validators.ohlc import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['dash'] = v_line.DashValidator()
        self._validators['width'] = v_line.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.dash = dash
        self.width = width

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
