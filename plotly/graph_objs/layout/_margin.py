from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Margin(BaseLayoutHierarchyType):

    # autoexpand
    # ----------
    @property
    def autoexpand(self):
        """
        The 'autoexpand' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['autoexpand']

    @autoexpand.setter
    def autoexpand(self, val):
        self['autoexpand'] = val

    # b
    # -
    @property
    def b(self):
        """
        Sets the bottom margin (in px).
    
        The 'b' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['b']

    @b.setter
    def b(self, val):
        self['b'] = val

    # l
    # -
    @property
    def l(self):
        """
        Sets the left margin (in px).
    
        The 'l' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['l']

    @l.setter
    def l(self, val):
        self['l'] = val

    # pad
    # ---
    @property
    def pad(self):
        """
        Sets the amount of padding (in px) between the plotting area
        and the axis lines
    
        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['pad']

    @pad.setter
    def pad(self, val):
        self['pad'] = val

    # r
    # -
    @property
    def r(self):
        """
        Sets the right margin (in px).
    
        The 'r' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['r']

    @r.setter
    def r(self, val):
        self['r'] = val

    # t
    # -
    @property
    def t(self):
        """
        Sets the top margin (in px).
    
        The 't' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['t']

    @t.setter
    def t(self, val):
        self['t'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autoexpand

        b
            Sets the bottom margin (in px).
        l
            Sets the left margin (in px).
        pad
            Sets the amount of padding (in px) between the plotting
            area and the axis lines
        r
            Sets the right margin (in px).
        t
            Sets the top margin (in px).
        """

    def __init__(
        self,
        arg=None,
        autoexpand=None,
        b=None,
        l=None,
        pad=None,
        r=None,
        t=None,
        **kwargs
    ):
        """
        Construct a new Margin object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Margin
        autoexpand

        b
            Sets the bottom margin (in px).
        l
            Sets the left margin (in px).
        pad
            Sets the amount of padding (in px) between the plotting
            area and the axis lines
        r
            Sets the right margin (in px).
        t
            Sets the top margin (in px).

        Returns
        -------
        Margin
        """
        super(Margin, self).__init__('margin')

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
The first argument to the plotly.graph_objs.layout.Margin 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Margin"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout import (margin as v_margin)

        # Initialize validators
        # ---------------------
        self._validators['autoexpand'] = v_margin.AutoexpandValidator()
        self._validators['b'] = v_margin.BValidator()
        self._validators['l'] = v_margin.LValidator()
        self._validators['pad'] = v_margin.PadValidator()
        self._validators['r'] = v_margin.RValidator()
        self._validators['t'] = v_margin.TValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('autoexpand', None)
        self.autoexpand = autoexpand if autoexpand is not None else _v
        _v = arg.pop('b', None)
        self.b = b if b is not None else _v
        _v = arg.pop('l', None)
        self.l = l if l is not None else _v
        _v = arg.pop('pad', None)
        self.pad = pad if pad is not None else _v
        _v = arg.pop('r', None)
        self.r = r if r is not None else _v
        _v = arg.pop('t', None)
        self.t = t if t is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
