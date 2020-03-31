from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Title(_BaseLayoutHierarchyType):

    # font
    # ----
    @property
    def font(self):
        """
        Sets this axis' title font. Note that the title's font used to
        be customized by the now deprecated `titlefont` attribute.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.yaxis.title.Font`
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
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.yaxis.title.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # standoff
    # --------
    @property
    def standoff(self):
        """
        Sets the standoff distance (in px) between the axis labels and
        the title text The default value is a function of the axis tick
        labels, the title `font.size` and the axis `linewidth`. Note
        that the axis title position is always constrained within the
        margins, so the actual standoff distance is always less than
        the set or default value. By setting `standoff` and turning on
        `automargin`, plotly.js will push the margins to fit the axis
        title at given standoff distance.
    
        The 'standoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["standoff"]

    @standoff.setter
    def standoff(self, val):
        self["standoff"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of this axis. Note that before the existence of
        `title.text`, the title's contents used to be defined as the
        `title` attribute itself. This behavior has been deprecated.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.yaxis"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        standoff
            Sets the standoff distance (in px) between the axis
            labels and the title text The default value is a
            function of the axis tick labels, the title `font.size`
            and the axis `linewidth`. Note that the axis title
            position is always constrained within the margins, so
            the actual standoff distance is always less than the
            set or default value. By setting `standoff` and turning
            on `automargin`, plotly.js will push the margins to fit
            the axis title at given standoff distance.
        text
            Sets the title of this axis. Note that before the
            existence of `title.text`, the title's contents used to
            be defined as the `title` attribute itself. This
            behavior has been deprecated.
        """

    def __init__(self, arg=None, font=None, standoff=None, text=None, **kwargs):
        """
        Construct a new Title object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.yaxis.Title`
        font
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        standoff
            Sets the standoff distance (in px) between the axis
            labels and the title text The default value is a
            function of the axis tick labels, the title `font.size`
            and the axis `linewidth`. Note that the axis title
            position is always constrained within the margins, so
            the actual standoff distance is always less than the
            set or default value. By setting `standoff` and turning
            on `automargin`, plotly.js will push the margins to fit
            the axis title at given standoff distance.
        text
            Sets the title of this axis. Note that before the
            existence of `title.text`, the title's contents used to
            be defined as the `title` attribute itself. This
            behavior has been deprecated.

        Returns
        -------
        Title
        """
        super(Title, self).__init__("title")

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
The first argument to the plotly.graph_objs.layout.yaxis.Title 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.yaxis.Title`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.yaxis import title as v_title

        # Initialize validators
        # ---------------------
        self._validators["font"] = v_title.FontValidator()
        self._validators["standoff"] = v_title.StandoffValidator()
        self._validators["text"] = v_title.TextValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("standoff", None)
        self["standoff"] = standoff if standoff is not None else _v
        _v = arg.pop("text", None)
        self["text"] = text if text is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Tickformatstop(_BaseLayoutHierarchyType):

    # dtickrange
    # ----------
    @property
    def dtickrange(self):
        """
        range [*min*, *max*], where "min", "max" - dtick values which
        describe some zoom level, it is possible to omit "min" or "max"
        value by passing "null"
    
        The 'dtickrange' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'dtickrange[0]' property accepts values of any type
    (1) The 'dtickrange[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self["dtickrange"]

    @dtickrange.setter
    def dtickrange(self, val):
        self["dtickrange"] = val

    # enabled
    # -------
    @property
    def enabled(self):
        """
        Determines whether or not this stop is used. If `false`, this
        stop is ignored even within its `dtickrange`.
    
        The 'enabled' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

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
        string - dtickformat for described zoom level, the same as
        "tickformat"
    
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

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.yaxis"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        dtickrange
            range [*min*, *max*], where "min", "max" - dtick values
            which describe some zoom level, it is possible to omit
            "min" or "max" value by passing "null"
        enabled
            Determines whether or not this stop is used. If
            `false`, this stop is ignored even within its
            `dtickrange`.
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
            string - dtickformat for described zoom level, the same
            as "tickformat"
        """

    def __init__(
        self,
        arg=None,
        dtickrange=None,
        enabled=None,
        name=None,
        templateitemname=None,
        value=None,
        **kwargs
    ):
        """
        Construct a new Tickformatstop object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.yaxis.Tickformatstop`
        dtickrange
            range [*min*, *max*], where "min", "max" - dtick values
            which describe some zoom level, it is possible to omit
            "min" or "max" value by passing "null"
        enabled
            Determines whether or not this stop is used. If
            `false`, this stop is ignored even within its
            `dtickrange`.
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
            string - dtickformat for described zoom level, the same
            as "tickformat"

        Returns
        -------
        Tickformatstop
        """
        super(Tickformatstop, self).__init__("tickformatstops")

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
The first argument to the plotly.graph_objs.layout.yaxis.Tickformatstop 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.yaxis.Tickformatstop`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.yaxis import tickformatstop as v_tickformatstop

        # Initialize validators
        # ---------------------
        self._validators["dtickrange"] = v_tickformatstop.DtickrangeValidator()
        self._validators["enabled"] = v_tickformatstop.EnabledValidator()
        self._validators["name"] = v_tickformatstop.NameValidator()
        self._validators[
            "templateitemname"
        ] = v_tickformatstop.TemplateitemnameValidator()
        self._validators["value"] = v_tickformatstop.ValueValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("dtickrange", None)
        self["dtickrange"] = dtickrange if dtickrange is not None else _v
        _v = arg.pop("enabled", None)
        self["enabled"] = enabled if enabled is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("value", None)
        self["value"] = value if value is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Tickfont(_BaseLayoutHierarchyType):

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
        the system. The Chart Studio Cloud (at https://chart-
        studio.plotly.com or on-premise) generates images on a server,
        where only a select number of fonts are installed and
        supported. These include "Arial", "Balto", "Courier New",
        "Droid Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
        One", "Old Standard TT", "Open Sans", "Overpass", "PT Sans
        Narrow", "Raleway", "Times New Roman".
    
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
        return "layout.yaxis"

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
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        size

        """

    def __init__(self, arg=None, color=None, family=None, size=None, **kwargs):
        """
        Construct a new Tickfont object
        
        Sets the tick font.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.yaxis.Tickfont`
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans",, "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        size


        Returns
        -------
        Tickfont
        """
        super(Tickfont, self).__init__("tickfont")

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
The first argument to the plotly.graph_objs.layout.yaxis.Tickfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.yaxis.Tickfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.yaxis import tickfont as v_tickfont

        # Initialize validators
        # ---------------------
        self._validators["color"] = v_tickfont.ColorValidator()
        self._validators["family"] = v_tickfont.FamilyValidator()
        self._validators["size"] = v_tickfont.SizeValidator()

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


class Rangebreak(_BaseLayoutHierarchyType):

    # bounds
    # ------
    @property
    def bounds(self):
        """
        Sets the lower and upper bounds of this axis rangebreak. Can be
        used with `pattern`.
    
        The 'bounds' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'bounds[0]' property accepts values of any type
    (1) The 'bounds[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self["bounds"]

    @bounds.setter
    def bounds(self, val):
        self["bounds"] = val

    # dvalue
    # ------
    @property
    def dvalue(self):
        """
        Sets the size of each `values` item. The default is one day in
        milliseconds.
    
        The 'dvalue' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["dvalue"]

    @dvalue.setter
    def dvalue(self, val):
        self["dvalue"] = val

    # enabled
    # -------
    @property
    def enabled(self):
        """
        Determines whether this axis rangebreak is enabled or disabled.
        Please note that `rangebreaks` only work for "date" axis type.
    
        The 'enabled' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["enabled"]

    @enabled.setter
    def enabled(self, val):
        self["enabled"] = val

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

    # pattern
    # -------
    @property
    def pattern(self):
        """
        Determines a pattern on the time line that generates breaks. If
        *day of week* - days of the week in English e.g. 'Sunday' or
        `sun` (matching is case-insensitive and considers only the
        first three characters), as well as Sunday-based integers
        between 0 and 6. If "hour" - hour (24-hour clock) as decimal
        numbers between 0 and 24. for more info. Examples: - { pattern:
        'day of week', bounds: [6, 1] }  or simply { bounds: ['sat',
        'mon'] }   breaks from Saturday to Monday (i.e. skips the
        weekends). - { pattern: 'hour', bounds: [17, 8] }   breaks from
        5pm to 8am (i.e. skips non-work hours).
    
        The 'pattern' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['day of week', 'hour', '']

        Returns
        -------
        Any
        """
        return self["pattern"]

    @pattern.setter
    def pattern(self, val):
        self["pattern"] = val

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

    # values
    # ------
    @property
    def values(self):
        """
        Sets the coordinate values corresponding to the rangebreaks. An
        alternative to `bounds`. Use `dvalue` to set the size of the
        values along the axis.
    
        The 'values' property is an info array that may be specified as:
        * a list of elements where:
          The 'values[i]' property accepts values of any type

        Returns
        -------
        list
        """
        return self["values"]

    @values.setter
    def values(self, val):
        self["values"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.yaxis"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        bounds
            Sets the lower and upper bounds of this axis
            rangebreak. Can be used with `pattern`.
        dvalue
            Sets the size of each `values` item. The default is one
            day in milliseconds.
        enabled
            Determines whether this axis rangebreak is enabled or
            disabled. Please note that `rangebreaks` only work for
            "date" axis type.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pattern
            Determines a pattern on the time line that generates
            breaks. If *day of week* - days of the week in English
            e.g. 'Sunday' or `sun` (matching is case-insensitive
            and considers only the first three characters), as well
            as Sunday-based integers between 0 and 6. If "hour" -
            hour (24-hour clock) as decimal numbers between 0 and
            24. for more info. Examples: - { pattern: 'day of
            week', bounds: [6, 1] }  or simply { bounds: ['sat',
            'mon'] }   breaks from Saturday to Monday (i.e. skips
            the weekends). - { pattern: 'hour', bounds: [17, 8] }
            breaks from 5pm to 8am (i.e. skips non-work hours).
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
        values
            Sets the coordinate values corresponding to the
            rangebreaks. An alternative to `bounds`. Use `dvalue`
            to set the size of the values along the axis.
        """

    def __init__(
        self,
        arg=None,
        bounds=None,
        dvalue=None,
        enabled=None,
        name=None,
        pattern=None,
        templateitemname=None,
        values=None,
        **kwargs
    ):
        """
        Construct a new Rangebreak object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.yaxis.Rangebreak`
        bounds
            Sets the lower and upper bounds of this axis
            rangebreak. Can be used with `pattern`.
        dvalue
            Sets the size of each `values` item. The default is one
            day in milliseconds.
        enabled
            Determines whether this axis rangebreak is enabled or
            disabled. Please note that `rangebreaks` only work for
            "date" axis type.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pattern
            Determines a pattern on the time line that generates
            breaks. If *day of week* - days of the week in English
            e.g. 'Sunday' or `sun` (matching is case-insensitive
            and considers only the first three characters), as well
            as Sunday-based integers between 0 and 6. If "hour" -
            hour (24-hour clock) as decimal numbers between 0 and
            24. for more info. Examples: - { pattern: 'day of
            week', bounds: [6, 1] }  or simply { bounds: ['sat',
            'mon'] }   breaks from Saturday to Monday (i.e. skips
            the weekends). - { pattern: 'hour', bounds: [17, 8] }
            breaks from 5pm to 8am (i.e. skips non-work hours).
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
        values
            Sets the coordinate values corresponding to the
            rangebreaks. An alternative to `bounds`. Use `dvalue`
            to set the size of the values along the axis.

        Returns
        -------
        Rangebreak
        """
        super(Rangebreak, self).__init__("rangebreaks")

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
The first argument to the plotly.graph_objs.layout.yaxis.Rangebreak 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.yaxis.Rangebreak`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.yaxis import rangebreak as v_rangebreak

        # Initialize validators
        # ---------------------
        self._validators["bounds"] = v_rangebreak.BoundsValidator()
        self._validators["dvalue"] = v_rangebreak.DvalueValidator()
        self._validators["enabled"] = v_rangebreak.EnabledValidator()
        self._validators["name"] = v_rangebreak.NameValidator()
        self._validators["pattern"] = v_rangebreak.PatternValidator()
        self._validators["templateitemname"] = v_rangebreak.TemplateitemnameValidator()
        self._validators["values"] = v_rangebreak.ValuesValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("bounds", None)
        self["bounds"] = bounds if bounds is not None else _v
        _v = arg.pop("dvalue", None)
        self["dvalue"] = dvalue if dvalue is not None else _v
        _v = arg.pop("enabled", None)
        self["enabled"] = enabled if enabled is not None else _v
        _v = arg.pop("name", None)
        self["name"] = name if name is not None else _v
        _v = arg.pop("pattern", None)
        self["pattern"] = pattern if pattern is not None else _v
        _v = arg.pop("templateitemname", None)
        self["templateitemname"] = (
            templateitemname if templateitemname is not None else _v
        )
        _v = arg.pop("values", None)
        self["values"] = values if values is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = [
    "Rangebreak",
    "Rangebreak",
    "Tickfont",
    "Tickformatstop",
    "Tickformatstop",
    "Title",
    "title",
]

from plotly.graph_objs.layout.yaxis import title
