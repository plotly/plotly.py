from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


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
        arg=None,
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
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.slider.Step
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
The first argument to the plotly.graph_objs.layout.slider.Step 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Step"""
            )

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
        v = arg.pop('args', None)
        self.args = args if args is not None else v
        v = arg.pop('execute', None)
        self.execute = execute if execute is not None else v
        v = arg.pop('label', None)
        self.label = label if label is not None else v
        v = arg.pop('method', None)
        self.method = method if method is not None else v
        v = arg.pop('value', None)
        self.value = value if value is not None else v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
