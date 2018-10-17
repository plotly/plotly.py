from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Currentvalue(BaseLayoutHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the current value label text.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.currentvalue.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.slider.currentvalue.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # offset
    # ------
    @property
    def offset(self):
        """
        The amount of space, in pixels, between the current value label
        and the slider.
    
        The 'offset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['offset']

    @offset.setter
    def offset(self, val):
        self['offset'] = val

    # prefix
    # ------
    @property
    def prefix(self):
        """
        When currentvalue.visible is true, this sets the prefix of the
        label.
    
        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['prefix']

    @prefix.setter
    def prefix(self, val):
        self['prefix'] = val

    # suffix
    # ------
    @property
    def suffix(self):
        """
        When currentvalue.visible is true, this sets the suffix of the
        label.
    
        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['suffix']

    @suffix.setter
    def suffix(self, val):
        self['suffix'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Shows the currently-selected value above the slider.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        The alignment of the value readout relative to the length of
        the slider.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.slider'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.
        """

    def __init__(
        self,
        arg=None,
        font=None,
        offset=None,
        prefix=None,
        suffix=None,
        visible=None,
        xanchor=None,
        **kwargs
    ):
        """
        Construct a new Currentvalue object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.slider.Currentvalue
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.

        Returns
        -------
        Currentvalue
        """
        super(Currentvalue, self).__init__('currentvalue')

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
The first argument to the plotly.graph_objs.layout.slider.Currentvalue 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Currentvalue"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import (
            currentvalue as v_currentvalue
        )

        # Initialize validators
        # ---------------------
        self._validators['font'] = v_currentvalue.FontValidator()
        self._validators['offset'] = v_currentvalue.OffsetValidator()
        self._validators['prefix'] = v_currentvalue.PrefixValidator()
        self._validators['suffix'] = v_currentvalue.SuffixValidator()
        self._validators['visible'] = v_currentvalue.VisibleValidator()
        self._validators['xanchor'] = v_currentvalue.XanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('font', None)
        self['font'] = font if font is not None else _v
        _v = arg.pop('offset', None)
        self['offset'] = offset if offset is not None else _v
        _v = arg.pop('prefix', None)
        self['prefix'] = prefix if prefix is not None else _v
        _v = arg.pop('suffix', None)
        self['suffix'] = suffix if suffix is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v
        _v = arg.pop('xanchor', None)
        self['xanchor'] = xanchor if xanchor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
