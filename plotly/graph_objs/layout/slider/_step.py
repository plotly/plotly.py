from plotly.basedatatypes import BaseLayoutHierarchyType


class Step(BaseLayoutHierarchyType):

    # args
    # ----
    @property
    def args(self):
        """
        Sets the arguments values to be passed to the Plotly method set
        in `method` on slide.
    
        The 'args' property is an info array that may be specified as a
        list or tuple of up to 3 elements where:
    
    (0) The 'args[0]' property accepts values of any type
    (1) The 'args[1]' property accepts values of any type
    (2) The 'args[2]' property accepts values of any type

        Returns
        -------
        list
        """
        return self['args']

    @args.setter
    def args(self, val):
        self['args'] = val

    # execute
    # -------
    @property
    def execute(self):
        """
        When true, the API method is executed. When false, all other
        behaviors are the same and command execution is skipped. This
        may be useful when hooking into, for example, the
        `plotly_sliderchange` method and executing the API command
        manually without losing the benefit of the slider automatically
        binding to the state of the plot through the specification of
        `method` and `args`.
    
        The 'execute' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['execute']

    @execute.setter
    def execute(self, val):
        self['execute'] = val

    # label
    # -----
    @property
    def label(self):
        """
        Sets the text label to appear on the slider
    
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

    # method
    # ------
    @property
    def method(self):
        """
        Sets the Plotly method to be called when the slider value is
        changed. If the `skip` method is used, the API slider will
        function as normal but will perform no API calls and will not
        bind automatically to state updates. This may be used to create
        a component interface and attach to slider events manually via
        JavaScript.
    
        The 'method' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['restyle', 'relayout', 'animate', 'update', 'skip']

        Returns
        -------
        Any
        """
        return self['method']

    @method.setter
    def method(self, val):
        self['method'] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the value of the slider step, used to refer to the step
        programatically. Defaults to the slider label if not provided.
    
        The 'value' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

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
        args
            Sets the arguments values to be passed to the Plotly
            method set in `method` on slide.
        execute
            When true, the API method is executed. When false, all
            other behaviors are the same and command execution is
            skipped. This may be useful when hooking into, for
            example, the `plotly_sliderchange` method and executing
            the API command manually without losing the benefit of
            the slider automatically binding to the state of the
            plot through the specification of `method` and `args`.
        label
            Sets the text label to appear on the slider
        method
            Sets the Plotly method to be called when the slider
            value is changed. If the `skip` method is used, the API
            slider will function as normal but will perform no API
            calls and will not bind automatically to state updates.
            This may be used to create a component interface and
            attach to slider events manually via JavaScript.
        value
            Sets the value of the slider step, used to refer to the
            step programatically. Defaults to the slider label if
            not provided.
        """

    def __init__(
        self,
        args=None,
        execute=None,
        label=None,
        method=None,
        value=None,
        **kwargs
    ):
        """
        Construct a new Step object
        
        Parameters
        ----------
        args
            Sets the arguments values to be passed to the Plotly
            method set in `method` on slide.
        execute
            When true, the API method is executed. When false, all
            other behaviors are the same and command execution is
            skipped. This may be useful when hooking into, for
            example, the `plotly_sliderchange` method and executing
            the API command manually without losing the benefit of
            the slider automatically binding to the state of the
            plot through the specification of `method` and `args`.
        label
            Sets the text label to appear on the slider
        method
            Sets the Plotly method to be called when the slider
            value is changed. If the `skip` method is used, the API
            slider will function as normal but will perform no API
            calls and will not bind automatically to state updates.
            This may be used to create a component interface and
            attach to slider events manually via JavaScript.
        value
            Sets the value of the slider step, used to refer to the
            step programatically. Defaults to the slider label if
            not provided.

        Returns
        -------
        Step
        """
        super(Step, self).__init__('steps')

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import (step as v_step)

        # Initialize validators
        # ---------------------
        self._validators['args'] = v_step.ArgsValidator()
        self._validators['execute'] = v_step.ExecuteValidator()
        self._validators['label'] = v_step.LabelValidator()
        self._validators['method'] = v_step.MethodValidator()
        self._validators['value'] = v_step.ValueValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.args = args
        self.execute = execute
        self.label = label
        self.method = method
        self.value = value

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
