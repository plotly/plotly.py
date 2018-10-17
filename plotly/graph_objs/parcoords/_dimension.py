from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Dimension(BaseTraceHierarchyType):

    # constraintrange
    # ---------------
    @property
    def constraintrange(self):
        """
        The domain range to which the filter on the dimension is
        constrained. Must be an array of `[fromValue, toValue]` with
        `fromValue <= toValue`, or if `multiselect` is not disabled,
        you may give an array of arrays, where each inner array is
        `[fromValue, toValue]`.
    
        The 'constraintrange' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'constraintrange[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'constraintrange[1]' property is a number and may be specified as:
          - An int or float
    
        * a 2D list where:
    (0) The 'constraintrange[i][0]' property is a number and may be specified as:
          - An int or float
    (1) The 'constraintrange[i][1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self['constraintrange']

    @constraintrange.setter
    def constraintrange(self, val):
        self['constraintrange'] = val

    # label
    # -----
    @property
    def label(self):
        """
        The shown name of the dimension.
    
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

    # multiselect
    # -----------
    @property
    def multiselect(self):
        """
        Do we allow multiple selection ranges or just a single range?
    
        The 'multiselect' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['multiselect']

    @multiselect.setter
    def multiselect(self, val):
        self['multiselect'] = val

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

    # range
    # -----
    @property
    def range(self):
        """
        The domain range that represents the full, shown axis extent.
        Defaults to the `values` extent. Must be an array of
        `[fromValue, toValue]` with finite numbers as elements.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property is a number and may be specified as:
          - An int or float
    (1) The 'range[1]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

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

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        language which is similar to those of Python. See https://githu
        b.com/d3/d3-format/blob/master/README.md#locale_format
    
        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickformat']

    @tickformat.setter
    def tickformat(self, val):
        self['tickformat'] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to "array". Used with
        `tickvals`.
    
        The 'ticktext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ticktext']

    @ticktext.setter
    def ticktext(self, val):
        self['ticktext'] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on plot.ly for  ticktext .
    
        The 'ticktextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['ticktextsrc']

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self['ticktextsrc'] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to "array". Used with `ticktext`.
    
        The 'tickvals' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['tickvals']

    @tickvals.setter
    def tickvals(self, val):
        self['tickvals'] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on plot.ly for  tickvals .
    
        The 'tickvalssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['tickvalssrc']

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self['tickvalssrc'] = val

    # values
    # ------
    @property
    def values(self):
        """
        Dimension values. `values[n]` represents the value of the `n`th
        point in the dataset, therefore the `values` vector for all
        dimensions must be the same (longer vectors will be truncated).
        Each value must be a finite number.
    
        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['values']

    @values.setter
    def values(self, val):
        self['values'] = val

    # valuessrc
    # ---------
    @property
    def valuessrc(self):
        """
        Sets the source reference on plot.ly for  values .
    
        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['valuessrc']

    @valuessrc.setter
    def valuessrc(self, val):
        self['valuessrc'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Shows the dimension when set to `true` (the default). Hides the
        dimension for `false`.
    
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
        return 'parcoords'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        constraintrange
            The domain range to which the filter on the dimension
            is constrained. Must be an array of `[fromValue,
            toValue]` with `fromValue <= toValue`, or if
            `multiselect` is not disabled, you may give an array of
            arrays, where each inner array is `[fromValue,
            toValue]`.
        label
            The shown name of the dimension.
        multiselect
            Do we allow multiple selection ranges or just a single
            range?
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        range
            The domain range that represents the full, shown axis
            extent. Defaults to the `values` extent. Must be an
            array of `[fromValue, toValue]` with finite numbers as
            elements.
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
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        values
            Dimension values. `values[n]` represents the value of
            the `n`th point in the dataset, therefore the `values`
            vector for all dimensions must be the same (longer
            vectors will be truncated). Each value must be a finite
            number.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Shows the dimension when set to `true` (the default).
            Hides the dimension for `false`.
        """

    def __init__(
        self,
        arg=None,
        constraintrange=None,
        label=None,
        multiselect=None,
        name=None,
        range=None,
        templateitemname=None,
        tickformat=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        values=None,
        valuessrc=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Dimension object
        
        The dimensions (variables) of the parallel coordinates chart.
        2..60 dimensions are supported.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.parcoords.Dimension
        constraintrange
            The domain range to which the filter on the dimension
            is constrained. Must be an array of `[fromValue,
            toValue]` with `fromValue <= toValue`, or if
            `multiselect` is not disabled, you may give an array of
            arrays, where each inner array is `[fromValue,
            toValue]`.
        label
            The shown name of the dimension.
        multiselect
            Do we allow multiple selection ranges or just a single
            range?
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        range
            The domain range that represents the full, shown axis
            extent. Defaults to the `values` extent. Must be an
            array of `[fromValue, toValue]` with finite numbers as
            elements.
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
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-language which is similar to those of Python. See 
            https://github.com/d3/d3-format/blob/master/README.md#l
            ocale_format
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            "array". Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to "array".
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        values
            Dimension values. `values[n]` represents the value of
            the `n`th point in the dataset, therefore the `values`
            vector for all dimensions must be the same (longer
            vectors will be truncated). Each value must be a finite
            number.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Shows the dimension when set to `true` (the default).
            Hides the dimension for `false`.

        Returns
        -------
        Dimension
        """
        super(Dimension, self).__init__('dimensions')

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
The first argument to the plotly.graph_objs.parcoords.Dimension 
constructor must be a dict or 
an instance of plotly.graph_objs.parcoords.Dimension"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.parcoords import (dimension as v_dimension)

        # Initialize validators
        # ---------------------
        self._validators['constraintrange'
                        ] = v_dimension.ConstraintrangeValidator()
        self._validators['label'] = v_dimension.LabelValidator()
        self._validators['multiselect'] = v_dimension.MultiselectValidator()
        self._validators['name'] = v_dimension.NameValidator()
        self._validators['range'] = v_dimension.RangeValidator()
        self._validators['templateitemname'
                        ] = v_dimension.TemplateitemnameValidator()
        self._validators['tickformat'] = v_dimension.TickformatValidator()
        self._validators['ticktext'] = v_dimension.TicktextValidator()
        self._validators['ticktextsrc'] = v_dimension.TicktextsrcValidator()
        self._validators['tickvals'] = v_dimension.TickvalsValidator()
        self._validators['tickvalssrc'] = v_dimension.TickvalssrcValidator()
        self._validators['values'] = v_dimension.ValuesValidator()
        self._validators['valuessrc'] = v_dimension.ValuessrcValidator()
        self._validators['visible'] = v_dimension.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('constraintrange', None)
        self['constraintrange'
            ] = constraintrange if constraintrange is not None else _v
        _v = arg.pop('label', None)
        self['label'] = label if label is not None else _v
        _v = arg.pop('multiselect', None)
        self['multiselect'] = multiselect if multiselect is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('range', None)
        self['range'] = range if range is not None else _v
        _v = arg.pop('templateitemname', None)
        self['templateitemname'
            ] = templateitemname if templateitemname is not None else _v
        _v = arg.pop('tickformat', None)
        self['tickformat'] = tickformat if tickformat is not None else _v
        _v = arg.pop('ticktext', None)
        self['ticktext'] = ticktext if ticktext is not None else _v
        _v = arg.pop('ticktextsrc', None)
        self['ticktextsrc'] = ticktextsrc if ticktextsrc is not None else _v
        _v = arg.pop('tickvals', None)
        self['tickvals'] = tickvals if tickvals is not None else _v
        _v = arg.pop('tickvalssrc', None)
        self['tickvalssrc'] = tickvalssrc if tickvalssrc is not None else _v
        _v = arg.pop('values', None)
        self['values'] = values if values is not None else _v
        _v = arg.pop('valuessrc', None)
        self['valuessrc'] = valuessrc if valuessrc is not None else _v
        _v = arg.pop('visible', None)
        self['visible'] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
