from plotly.basedatatypes import BaseLayoutHierarchyType


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
        return 'layout.updatemenu'

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

    def __init__(self, b=None, l=None, r=None, t=None, **kwargs):
        """
        Construct a new Pad object
        
        Sets the padding around the buttons or dropdown menu.

        Parameters
        ----------
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

        # Import validators
        # -----------------
        from plotly.validators.layout.updatemenu import (pad as v_pad)

        # Initialize validators
        # ---------------------
        self._validators['b'] = v_pad.BValidator()
        self._validators['l'] = v_pad.LValidator()
        self._validators['r'] = v_pad.RValidator()
        self._validators['t'] = v_pad.TValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.b = b
        self.l = l
        self.r = r
        self.t = t

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
