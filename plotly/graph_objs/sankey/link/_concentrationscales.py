from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Concentrationscales(BaseTraceHierarchyType):

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmax']

    @cmax.setter
    def cmax(self, val):
        self['cmax'] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['cmin']

    @cmin.setter
    def cmin(self, val):
        self['cmin'] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use`cmin` and `cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Bl
        ues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth,Electric,Vi
        ridis,Cividis.
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1), 
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']

        Returns
        -------
        str
        """
        return self['colorscale']

    @colorscale.setter
    def colorscale(self, val):
        self['colorscale'] = val

    # label
    # -----
    @property
    def label(self):
        """
        The label of the links to color based on their concentration
        within a flow.
    
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

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'sankey.link'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        cmax
            Sets the upper bound of the color domain.
        cmin
            Sets the lower bound of the color domain.
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        label
            The label of the links to color based on their
            concentration within a flow.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
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
        """

    def __init__(
        self,
        arg=None,
        cmax=None,
        cmin=None,
        colorscale=None,
        label=None,
        name=None,
        templateitemname=None,
        **kwargs
    ):
        """
        Construct a new Concentrationscales object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.sankey.link.Concentrationscales
        cmax
            Sets the upper bound of the color domain.
        cmin
            Sets the lower bound of the color domain.
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)', [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Greys,YlGnBu,Greens,YlOrR
            d,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,H
            ot,Blackbody,Earth,Electric,Viridis,Cividis.
        label
            The label of the links to color based on their
            concentration within a flow.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
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

        Returns
        -------
        Concentrationscales
        """
        super(Concentrationscales, self).__init__('concentrationscaless')

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
The first argument to the plotly.graph_objs.sankey.link.Concentrationscales 
constructor must be a dict or 
an instance of plotly.graph_objs.sankey.link.Concentrationscales"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)

        # Import validators
        # -----------------
        from plotly.validators.sankey.link import (
            concentrationscales as v_concentrationscales
        )

        # Initialize validators
        # ---------------------
        self._validators['cmax'] = v_concentrationscales.CmaxValidator()
        self._validators['cmin'] = v_concentrationscales.CminValidator()
        self._validators['colorscale'
                        ] = v_concentrationscales.ColorscaleValidator()
        self._validators['label'] = v_concentrationscales.LabelValidator()
        self._validators['name'] = v_concentrationscales.NameValidator()
        self._validators['templateitemname'
                        ] = v_concentrationscales.TemplateitemnameValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('cmax', None)
        self['cmax'] = cmax if cmax is not None else _v
        _v = arg.pop('cmin', None)
        self['cmin'] = cmin if cmin is not None else _v
        _v = arg.pop('colorscale', None)
        self['colorscale'] = colorscale if colorscale is not None else _v
        _v = arg.pop('label', None)
        self['label'] = label if label is not None else _v
        _v = arg.pop('name', None)
        self['name'] = name if name is not None else _v
        _v = arg.pop('templateitemname', None)
        self['templateitemname'
            ] = templateitemname if templateitemname is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
