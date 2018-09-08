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

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

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
        Sets the range update mode. If "backward", the range update
        shifts the start of range back "count" times "step"
        milliseconds. If "todate", the range update shifts the start of
        range back to the first timestamp from "count" times "step"
        milliseconds back. For example, with `step` set to "year" and
        `count` set to 1 the range update shifts the start of the range
        back to January 01 of the current year. Month and year "todate"
        are currently available only for the built-in (Gregorian)
        calendar.
    
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

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['templateitemname']

    @templateitemname.setter
    def templateitemname(self, val):
        self['templateitemname'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this button is visible.
    
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
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        step
            The unit of measurement that the `count` value will set
            the range by.
        stepmode
            Sets the range update mode. If "backward", the range
            update shifts the start of range back "count" times
            "step" milliseconds. If "todate", the range update
            shifts the start of range back to the first timestamp
            from "count" times "step" milliseconds back. For
            example, with `step` set to "year" and `count` set to 1
            the range update shifts the start of the range back to
            January 01 of the current year. Month and year "todate"
            are currently available only for the built-in
            (Gregorian) calendar.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this button is visible.
        """

    def __init__(
        self,
        arg=None,
        count=None,
        label=None,
        name=None,
        step=None,
        stepmode=None,
        templateitemname=None,
        visible=None,
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
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        step
            The unit of measurement that the `count` value will set
            the range by.
        stepmode
            Sets the range update mode. If "backward", the range
            update shifts the start of range back "count" times
            "step" milliseconds. If "todate", the range update
            shifts the start of range back to the first timestamp
            from "count" times "step" milliseconds back. For
            example, with `step` set to "year" and `count` set to 1
            the range update shifts the start of the range back to
            January 01 of the current year. Month and year "todate"
            are currently available only for the built-in
            (Gregorian) calendar.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        visible
            Determines whether or not this button is visible.

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

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis.rangeselector import (
            button as v_button
        )

        # Initialize validators
        # ---------------------
        self._validators['count'] = v_button.CountValidator()
        self._validators['label'] = v_button.LabelValidator()
        self._validators['name'] = v_button.NameValidator()
        self._validators['step'] = v_button.StepValidator()
        self._validators['stepmode'] = v_button.StepmodeValidator()
        self._validators['templateitemname'
                        ] = v_button.TemplateitemnameValidator()
        self._validators['visible'] = v_button.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('count', None)
        self['count'] = count if count is not None else _v
        _v = arg.pop('label', None)
        self['label'] = label if label is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('step', None)
        self['step'] = step if step is not None else _v
        _v = arg.pop('stepmode', None)
        self['stepmode'] = stepmode if stepmode is not None else _v
        _v = arg.pop('templateitemname', None)
        self['templateitemname'
            ] = templateitemname if templateitemname is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
