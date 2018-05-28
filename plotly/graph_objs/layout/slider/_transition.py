from plotly.basedatatypes import BaseLayoutHierarchyType


class Transition(BaseLayoutHierarchyType):

    # duration
    # --------
    @property
    def duration(self):
        """
        Sets the duration of the slider transition
    
        The 'duration' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['duration']

    @duration.setter
    def duration(self, val):
        self['duration'] = val

    # easing
    # ------
    @property
    def easing(self):
        """
        Sets the easing function of the slider transition
    
        The 'easing' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['linear', 'quad', 'cubic', 'sin', 'exp', 'circle',
                'elastic', 'back', 'bounce', 'linear-in', 'quad-in',
                'cubic-in', 'sin-in', 'exp-in', 'circle-in', 'elastic-in',
                'back-in', 'bounce-in', 'linear-out', 'quad-out',
                'cubic-out', 'sin-out', 'exp-out', 'circle-out',
                'elastic-out', 'back-out', 'bounce-out', 'linear-in-out',
                'quad-in-out', 'cubic-in-out', 'sin-in-out', 'exp-in-out',
                'circle-in-out', 'elastic-in-out', 'back-in-out',
                'bounce-in-out']

        Returns
        -------
        Any
        """
        return self['easing']

    @easing.setter
    def easing(self, val):
        self['easing'] = val

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
        duration
            Sets the duration of the slider transition
        easing
            Sets the easing function of the slider transition
        """

    def __init__(self, duration=None, easing=None, **kwargs):
        """
        Construct a new Transition object
        
        Parameters
        ----------
        duration
            Sets the duration of the slider transition
        easing
            Sets the easing function of the slider transition

        Returns
        -------
        Transition
        """
        super(Transition, self).__init__('transition')

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import (
            transition as v_transition
        )

        # Initialize validators
        # ---------------------
        self._validators['duration'] = v_transition.DurationValidator()
        self._validators['easing'] = v_transition.EasingValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.duration = duration
        self.easing = easing

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
