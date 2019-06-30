from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Transition(_BaseLayoutHierarchyType):

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
        return self["duration"]

    @duration.setter
    def duration(self, val):
        self["duration"] = val

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
        return self["easing"]

    @easing.setter
    def easing(self, val):
        self["easing"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.slider"

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

    def __init__(self, arg=None, duration=None, easing=None, **kwargs):
        """
        Construct a new Transition object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.slider.Transition
        duration
            Sets the duration of the slider transition
        easing
            Sets the easing function of the slider transition

        Returns
        -------
        Transition
        """
        super(Transition, self).__init__("transition")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.slider.Transition 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Transition"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import transition as v_transition

        # Initialize validators
        # ---------------------
        self._validators["duration"] = v_transition.DurationValidator()
        self._validators["easing"] = v_transition.EasingValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("duration", None)
        self["duration"] = duration if duration is not None else _v
        _v = arg.pop("easing", None)
        self["easing"] = easing if easing is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Step(_BaseLayoutHierarchyType):

    # args
    # ----
    @property
    def args(self):
        """
        Sets the arguments values to be passed to the Plotly method set
        in `method` on slide.
    
        The 'args' property is an info array that may be specified as:
    
        * a list or tuple of up to 3 elements where:
    (0) The 'args[0]' property accepts values of any type
    (1) The 'args[1]' property accepts values of any type
    (2) The 'args[2]' property accepts values of any type

        Returns
        -------
        list
        """
        return self["args"]

    @args.setter
    def args(self, val):
        self["args"] = val

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
        return self["execute"]

    @execute.setter
    def execute(self, val):
        self["execute"] = val

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
        return self["label"]

    @label.setter
    def label(self, val):
        self["label"] = val

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
        return self["method"]

    @method.setter
    def method(self, val):
        self["method"] = val

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
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

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
        return self["templateitemname"]

    @templateitemname.setter
    def templateitemname(self, val):
        self["templateitemname"] = val

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
        return self["value"]

    @value.setter
    def value(self, val):
        self["value"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this step is included in the slider.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.slider"

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
        value
            Sets the value of the slider step, used to refer to the
            step programatically. Defaults to the slider label if
            not provided.
        visible
            Determines whether or not this step is included in the
            slider.
        """

    def __init__(
        self,
        arg=None,
        args=None,
        execute=None,
        label=None,
        method=None,
        name=None,
        templateitemname=None,
        value=None,
        visible=None,
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
        value
            Sets the value of the slider step, used to refer to the
            step programatically. Defaults to the slider label if
            not provided.
        visible
            Determines whether or not this step is included in the
            slider.

        Returns
        -------
        Step
        """
        super(Step, self).__init__("steps")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.slider.Step 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Step"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import step as v_step

        # Initialize validators
        # ---------------------
        self._validators["args"] = v_step.ArgsValidator()
        self._validators["execute"] = v_step.ExecuteValidator()
        self._validators["label"] = v_step.LabelValidator()
        self._validators["method"] = v_step.MethodValidator()
        self._validators["name"] = v_step.NameValidator()
        self._validators["templateitemname"] = v_step.TemplateitemnameValidator()
        self._validators["value"] = v_step.ValueValidator()
        self._validators["visible"] = v_step.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("args", None)
        self["args"] = args if args is not None else _v
        _v = arg.pop("execute", None)
        self["execute"] = execute if execute is not None else _v
        _v = arg.pop("label", None)
        self["label"] = label if label is not None else _v
        _v = arg.pop("method", None)
        self["method"] = method if method is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("value", None)
        self["value"] = value if value is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Pad(_BaseLayoutHierarchyType):

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
        return self["b"]

    @b.setter
    def b(self, val):
        self["b"] = val

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
        return self["l"]

    @l.setter
    def l(self, val):
        self["l"] = val

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
        return self["r"]

    @r.setter
    def r(self, val):
        self["r"] = val

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
        return self["t"]

    @t.setter
    def t(self, val):
        self["t"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.slider"

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
        super(Pad, self).__init__("pad")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.slider.Pad 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Pad"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import pad as v_pad

        # Initialize validators
        # ---------------------
        self._validators["b"] = v_pad.BValidator()
        self._validators["l"] = v_pad.LValidator()
        self._validators["r"] = v_pad.RValidator()
        self._validators["t"] = v_pad.TValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("b", None)
        self["b"] = b if b is not None else _v
        _v = arg.pop("l", None)
        self["l"] = l if l is not None else _v
        _v = arg.pop("r", None)
        self["r"] = r if r is not None else _v
        _v = arg.pop("t", None)
        self["t"] = t if t is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Font(_BaseLayoutHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The plotly service (at https://plot.ly or on-
        premise) generates images on a server, where only a select
        number of fonts are installed and supported. These include
        "Arial", "Balto", "Courier New", "Droid Sans",, "Droid Serif",
        "Droid Sans Mono", "Gravitas One", "Old Standard TT", "Open
        Sans", "Overpass", "PT Sans Narrow", "Raleway", "Times New
        Roman".
    
        The 'family' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.slider"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include "Arial", "Balto", "Courier New", "Droid Sans",,
            "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
            Standard TT", "Open Sans", "Overpass", "PT Sans
            Narrow", "Raleway", "Times New Roman".
        size

        """

    def __init__(self, arg=None, color=None, family=None, size=None, **kwargs):
        """
        Construct a new Font object
        
        Sets the font of the slider step labels.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.slider.Font
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include "Arial", "Balto", "Courier New", "Droid Sans",,
            "Droid Serif", "Droid Sans Mono", "Gravitas One", "Old
            Standard TT", "Open Sans", "Overpass", "PT Sans
            Narrow", "Raleway", "Times New Roman".
        size


        Returns
        -------
        Font
        """
        super(Font, self).__init__("font")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.slider.Font 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Font"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import font as v_font

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_font.ColorValidator()
        self._validators["family"] = v_font.FamilyValidator()
        self._validators["size"] = v_font.SizeValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("color", None)
        self["color"] = color if color is not None else _v
        _v = arg.pop("family", None)
        self["family"] = family if family is not None else _v
        _v = arg.pop("size", None)
        self["size"] = size if size is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Currentvalue(_BaseLayoutHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the current value label text.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.slider.currentvalue.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include "Arial",
                    "Balto", "Courier New", "Droid Sans",, "Droid
                    Serif", "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.slider.currentvalue.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # offset
    # ------
    @property
    def offset(self):
        """
        The amount of space, in pixels, between the current value label
        and the slider.
    
        The 'offset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["offset"]

    @offset.setter
    def offset(self, val):
        self["offset"] = val

    # prefix
    # ------
    @property
    def prefix(self):
        """
        When currentvalue.visible is true, this sets the prefix of the
        label.
    
        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["prefix"]

    @prefix.setter
    def prefix(self, val):
        self["prefix"] = val

    # suffix
    # ------
    @property
    def suffix(self):
        """
        When currentvalue.visible is true, this sets the suffix of the
        label.
    
        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["suffix"]

    @suffix.setter
    def suffix(self, val):
        self["suffix"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Shows the currently-selected value above the slider.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        The alignment of the value readout relative to the length of
        the slider.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.slider"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.
        """

    def __init__(
        self,
        arg=None,
        font=None,
        offset=None,
        prefix=None,
        suffix=None,
        visible=None,
        xanchor=None,
        **kwargs
    ):
        """
        Construct a new Currentvalue object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.slider.Currentvalue
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.

        Returns
        -------
        Currentvalue
        """
        super(Currentvalue, self).__init__("currentvalue")

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.slider.Currentvalue 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.slider.Currentvalue"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.slider import currentvalue as v_currentvalue

        # Initialize validators
        # ---------------------
        self._validators["font"] = v_currentvalue.FontValidator()
        self._validators["offset"] = v_currentvalue.OffsetValidator()
        self._validators["prefix"] = v_currentvalue.PrefixValidator()
        self._validators["suffix"] = v_currentvalue.SuffixValidator()
        self._validators["visible"] = v_currentvalue.VisibleValidator()
        self._validators["xanchor"] = v_currentvalue.XanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("offset", None)
        self["offset"] = offset if offset is not None else _v
        _v = arg.pop("prefix", None)
        self["prefix"] = prefix if prefix is not None else _v
        _v = arg.pop("suffix", None)
        self["suffix"] = suffix if suffix is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.graph_objs.layout.slider import currentvalue
