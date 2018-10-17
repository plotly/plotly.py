from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Pad(BaseLayoutHierarchyType):

    # b
    # -
    @property
    def b(self):
        """
        The amount of padding (in px) along the bottom of the
        component.
    
        The 'b' property is a number and may be specified as:
          - An int or float

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
        The amount of padding (in px) on the left side of the
        component.
    
        The 'l' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['l']

    @l.setter
    def l(self, val):
        self['l'] = val

    # r
    # -
    @property
    def r(self):
        """
        The amount of padding (in px) on the right side of the
        component.
    
        The 'r' property is a number and may be specified as:
          - An int or float

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
        The amount of padding (in px) along the top of the component.
    
        The 't' property is a number and may be specified as:
          - An int or float

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
        return 'layout.slider'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.
        """

    def __init__(self, arg=None, b=None, l=None, r=None, t=None, **kwargs):
        """
        Construct a new Pad object
        
        Set the padding of the slider component along each side.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.slider.Pad
        b
            The amount of padding (in px) along the bottom of the
            component.
        l
            The amount of padding (in px) on the left side of the
            component.
        r
            The amount of padding (in px) on the right side of the
            component.
        t
            The amount of padding (in px) along the top of the
            component.

        Returns
        -------
        Pad
        """
        super(Pad, self).__init__('pad')

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
The first argument to the plotly.graph_objs.layout.slider.Pad 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Pad"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import (pad as v_pad)

        # Initialize validators
        # ---------------------
        self._validators['b'] = v_pad.BValidator()
        self._validators['l'] = v_pad.LValidator()
        self._validators['r'] = v_pad.RValidator()
        self._validators['t'] = v_pad.TValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('b', None)
        self['b'] = b if b is not None else _v
        _v = arg.pop('l', None)
        self['l'] = l if l is not None else _v
        _v = arg.pop('r', None)
        self['r'] = r if r is not None else _v
        _v = arg.pop('t', None)
        self['t'] = t if t is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
