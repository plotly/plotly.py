from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Button(BaseLayoutHierarchyType):

    # count
    # -----
    @property
    def count(self):
        """
        Sets the number of steps to take to update the range. Use with
        `step` to specify the update interval.
    
        The 'count' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['count']

    @count.setter
    def count(self, val):
        self['count'] = val

    # label
    # -----
    @property
    def label(self):
        """
        Sets the text label to appear on the button.
    
        The 'label' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['label']

    @label.setter
    def label(self, val):
        self['label'] = val

    # step
    # ----
    @property
    def step(self):
        """
        The unit of measurement that the `count` value will set the
        range by.
    
        The 'step' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['month', 'year', 'day', 'hour', 'minute', 'second',
                'all']

        Returns
        -------
        Any
        """
        return self['step']

    @step.setter
    def step(self, val):
        self['step'] = val

    # stepmode
    # --------
    @property
    def stepmode(self):
        """
        Sets the range update mode. If *backward*, the range update
        shifts the start of range back *count* times *step*
        milliseconds. If *todate*, the range update shifts the start of
        range back to the first timestamp from *count* times *step*
        milliseconds back. For example, with `step` set to *year* and
        `count` set to *1* the range update shifts the start of the
        range back to January 01 of the current year. Month and year
        *todate* are currently available only for the built-in
        (Gregorian) calendar.
    
        The 'stepmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['backward', 'todate']

        Returns
        -------
        Any
        """
        return self['stepmode']

    @stepmode.setter
    def stepmode(self, val):
        self['stepmode'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.xaxis.rangeselector'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        count
            Sets the number of steps to take to update the range.
            Use with `step` to specify the update interval.
        label
            Sets the text label to appear on the button.
        step
            The unit of measurement that the `count` value will set
            the range by.
        stepmode
            Sets the range update mode. If *backward*, the range
            update shifts the start of range back *count* times
            *step* milliseconds. If *todate*, the range update
            shifts the start of range back to the first timestamp
            from *count* times *step* milliseconds back. For
            example, with `step` set to *year* and `count` set to
            *1* the range update shifts the start of the range back
            to January 01 of the current year. Month and year
            *todate* are currently available only for the built-in
            (Gregorian) calendar.
        """

    def __init__(
        self,
        arg=None,
        count=None,
        label=None,
        step=None,
        stepmode=None,
        **kwargs
    ):
        """
        Construct a new Button object
        
        Sets the specifications for each buttons. By default, a range
        selector comes with no buttons.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.xaxis.rangeselector.Button
        count
            Sets the number of steps to take to update the range.
            Use with `step` to specify the update interval.
        label
            Sets the text label to appear on the button.
        step
            The unit of measurement that the `count` value will set
            the range by.
        stepmode
            Sets the range update mode. If *backward*, the range
            update shifts the start of range back *count* times
            *step* milliseconds. If *todate*, the range update
            shifts the start of range back to the first timestamp
            from *count* times *step* milliseconds back. For
            example, with `step` set to *year* and `count` set to
            *1* the range update shifts the start of the range back
            to January 01 of the current year. Month and year
            *todate* are currently available only for the built-in
            (Gregorian) calendar.

        Returns
        -------
        Button
        """
        super(Button, self).__init__('buttons')

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
The first argument to the plotly.graph_objs.layout.xaxis.rangeselector.Button 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.xaxis.rangeselector.Button"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis.rangeselector import (
            button as v_button
        )

        # Initialize validators
        # ---------------------
        self._validators['count'] = v_button.CountValidator()
        self._validators['label'] = v_button.LabelValidator()
        self._validators['step'] = v_button.StepValidator()
        self._validators['stepmode'] = v_button.StepmodeValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('count', None)
        self.count = count if count is not None else v
        v = arg.pop('label', None)
        self.label = label if label is not None else v
        v = arg.pop('step', None)
        self.step = step if step is not None else v
        v = arg.pop('stepmode', None)
        self.stepmode = stepmode if stepmode is not None else v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
