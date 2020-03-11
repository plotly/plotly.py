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
          - An instance of :class:`plotly.graph_objs.layout.xaxis.title.Font`
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
        plotly.graph_objs.layout.xaxis.title.Font
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
        return "layout.xaxis"

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
            :class:`plotly.graph_objs.layout.xaxis.Title`
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
The first argument to the plotly.graph_objs.layout.xaxis.Title 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.xaxis.Title`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis import title as v_title

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
        return "layout.xaxis"

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
            :class:`plotly.graph_objs.layout.xaxis.Tickformatstop`
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
The first argument to the plotly.graph_objs.layout.xaxis.Tickformatstop 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.xaxis.Tickformatstop`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis import tickformatstop as v_tickformatstop

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
        return "layout.xaxis"

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
        Construct a new Tickfont object
        
        Sets the tick font.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.xaxis.Tickfont`
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
The first argument to the plotly.graph_objs.layout.xaxis.Tickfont 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.xaxis.Tickfont`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis import tickfont as v_tickfont

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


class Rangeslider(_BaseLayoutHierarchyType):

    # autorange
    # ---------
    @property
    def autorange(self):
        """
        Determines whether or not the range slider range is computed in
        relation to the input data. If `range` is provided, then
        `autorange` is set to False.
    
        The 'autorange' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autorange"]

    @autorange.setter
    def autorange(self, val):
        self["autorange"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the range slider.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the border color of the range slider.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the border width of the range slider.
    
        The 'borderwidth' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of the range slider. If not set, defaults to the
        full xaxis range. If the axis `type` is "log", then you must
        take the log of your desired range. If the axis `type` is
        "date", it should be date strings, like date data, though Date
        objects and unix milliseconds will be accepted and converted to
        strings. If the axis `type` is "category", it should be
        numbers, using the scale where each category is assigned a
        serial number from zero in the order it appears.
    
        The 'range' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'range[0]' property accepts values of any type
    (1) The 'range[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self["range"]

    @range.setter
    def range(self, val):
        self["range"] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        The height of the range slider as a fraction of the total plot
        area height.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["thickness"]

    @thickness.setter
    def thickness(self, val):
        self["thickness"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not the range slider will be visible. If
        visible, perpendicular axes will be set to `fixedrange`
    
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

    # yaxis
    # -----
    @property
    def yaxis(self):
        """
        The 'yaxis' property is an instance of YAxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.xaxis.rangeslider.YAxis`
          - A dict of string/value properties that will be passed
            to the YAxis constructor
    
            Supported dict properties:
                
                range
                    Sets the range of this axis for the
                    rangeslider.
                rangemode
                    Determines whether or not the range of this
                    axis in the rangeslider use the same value than
                    in the main plot when zooming in/out. If
                    "auto", the autorange will be used. If "fixed",
                    the `range` is used. If "match", the current
                    range of the corresponding y-axis on the main
                    subplot is used.

        Returns
        -------
        plotly.graph_objs.layout.xaxis.rangeslider.YAxis
        """
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.xaxis"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autorange
            Determines whether or not the range slider range is
            computed in relation to the input data. If `range` is
            provided, then `autorange` is set to False.
        bgcolor
            Sets the background color of the range slider.
        bordercolor
            Sets the border color of the range slider.
        borderwidth
            Sets the border width of the range slider.
        range
            Sets the range of the range slider. If not set,
            defaults to the full xaxis range. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        thickness
            The height of the range slider as a fraction of the
            total plot area height.
        visible
            Determines whether or not the range slider will be
            visible. If visible, perpendicular axes will be set to
            `fixedrange`
        yaxis
            :class:`plotly.graph_objects.layout.xaxis.rangeslider.Y
            Axis` instance or dict with compatible properties
        """

    def __init__(
        self,
        arg=None,
        autorange=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        range=None,
        thickness=None,
        visible=None,
        yaxis=None,
        **kwargs
    ):
        """
        Construct a new Rangeslider object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.xaxis.Rangeslider`
        autorange
            Determines whether or not the range slider range is
            computed in relation to the input data. If `range` is
            provided, then `autorange` is set to False.
        bgcolor
            Sets the background color of the range slider.
        bordercolor
            Sets the border color of the range slider.
        borderwidth
            Sets the border width of the range slider.
        range
            Sets the range of the range slider. If not set,
            defaults to the full xaxis range. If the axis `type` is
            "log", then you must take the log of your desired
            range. If the axis `type` is "date", it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is "category", it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        thickness
            The height of the range slider as a fraction of the
            total plot area height.
        visible
            Determines whether or not the range slider will be
            visible. If visible, perpendicular axes will be set to
            `fixedrange`
        yaxis
            :class:`plotly.graph_objects.layout.xaxis.rangeslider.Y
            Axis` instance or dict with compatible properties

        Returns
        -------
        Rangeslider
        """
        super(Rangeslider, self).__init__("rangeslider")

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
The first argument to the plotly.graph_objs.layout.xaxis.Rangeslider 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.xaxis.Rangeslider`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis import rangeslider as v_rangeslider

        # Initialize validators
        # ---------------------
        self._validators["autorange"] = v_rangeslider.AutorangeValidator()
        self._validators["bgcolor"] = v_rangeslider.BgcolorValidator()
        self._validators["bordercolor"] = v_rangeslider.BordercolorValidator()
        self._validators["borderwidth"] = v_rangeslider.BorderwidthValidator()
        self._validators["range"] = v_rangeslider.RangeValidator()
        self._validators["thickness"] = v_rangeslider.ThicknessValidator()
        self._validators["visible"] = v_rangeslider.VisibleValidator()
        self._validators["yaxis"] = v_rangeslider.YAxisValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("autorange", None)
        self["autorange"] = autorange if autorange is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("range", None)
        self["range"] = range if range is not None else _v
        _v = arg.pop("thickness", None)
        self["thickness"] = thickness if thickness is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("yaxis", None)
        self["yaxis"] = yaxis if yaxis is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Rangeselector(_BaseLayoutHierarchyType):

    # activecolor
    # -----------
    @property
    def activecolor(self):
        """
        Sets the background color of the active range selector button.
    
        The 'activecolor' property is a color and may be specified as:
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
        return self["activecolor"]

    @activecolor.setter
    def activecolor(self, val):
        self["activecolor"] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the range selector buttons.
    
        The 'bgcolor' property is a color and may be specified as:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the range selector.
    
        The 'bordercolor' property is a color and may be specified as:
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
        return self["bordercolor"]

    @bordercolor.setter
    def bordercolor(self, val):
        self["bordercolor"] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the range
        selector.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self["borderwidth"]

    @borderwidth.setter
    def borderwidth(self, val):
        self["borderwidth"] = val

    # buttons
    # -------
    @property
    def buttons(self):
        """
        Sets the specifications for each buttons. By default, a range
        selector comes with no buttons.
    
        The 'buttons' property is a tuple of instances of
        Button that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.xaxis.rangeselector.Button
          - A list or tuple of dicts of string/value properties that
            will be passed to the Button constructor
    
            Supported dict properties:
                
                count
                    Sets the number of steps to take to update the
                    range. Use with `step` to specify the update
                    interval.
                label
                    Sets the text label to appear on the button.
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                step
                    The unit of measurement that the `count` value
                    will set the range by.
                stepmode
                    Sets the range update mode. If "backward", the
                    range update shifts the start of range back
                    "count" times "step" milliseconds. If "todate",
                    the range update shifts the start of range back
                    to the first timestamp from "count" times
                    "step" milliseconds back. For example, with
                    `step` set to "year" and `count` set to 1 the
                    range update shifts the start of the range back
                    to January 01 of the current year. Month and
                    year "todate" are currently available only for
                    the built-in (Gregorian) calendar.
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
                visible
                    Determines whether or not this button is
                    visible.

        Returns
        -------
        tuple[plotly.graph_objs.layout.xaxis.rangeselector.Button]
        """
        return self["buttons"]

    @buttons.setter
    def buttons(self, val):
        self["buttons"] = val

    # buttondefaults
    # --------------
    @property
    def buttondefaults(self):
        """
        When used in a template (as
        layout.template.layout.xaxis.rangeselector.buttondefaults),
        sets the default property values to use for elements of
        layout.xaxis.rangeselector.buttons
    
        The 'buttondefaults' property is an instance of Button
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.xaxis.rangeselector.Button`
          - A dict of string/value properties that will be passed
            to the Button constructor
    
            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.xaxis.rangeselector.Button
        """
        return self["buttondefaults"]

    @buttondefaults.setter
    def buttondefaults(self, val):
        self["buttondefaults"] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the range selector button text.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.xaxis.rangeselector.Font`
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
        plotly.graph_objs.layout.xaxis.rangeselector.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this range selector is visible. Note
        that range selectors are only available for x axes of `type`
        set to or auto-typed to "date".
    
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

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the range
        selector.
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the range selector's horizontal position anchor. This
        anchor binds the `x` position to the "left", "center" or
        "right" of the range selector.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self["xanchor"]

    @xanchor.setter
    def xanchor(self, val):
        self["xanchor"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the range
        selector.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the range selector's vertical position anchor This anchor
        binds the `y` position to the "top", "middle" or "bottom" of
        the range selector.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self["yanchor"]

    @yanchor.setter
    def yanchor(self, val):
        self["yanchor"] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return "layout.xaxis"

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        activecolor
            Sets the background color of the active range selector
            button.
        bgcolor
            Sets the background color of the range selector
            buttons.
        bordercolor
            Sets the color of the border enclosing the range
            selector.
        borderwidth
            Sets the width (in px) of the border enclosing the
            range selector.
        buttons
            Sets the specifications for each buttons. By default, a
            range selector comes with no buttons.
        buttondefaults
            When used in a template (as layout.template.layout.xaxi
            s.rangeselector.buttondefaults), sets the default
            property values to use for elements of
            layout.xaxis.rangeselector.buttons
        font
            Sets the font of the range selector button text.
        visible
            Determines whether or not this range selector is
            visible. Note that range selectors are only available
            for x axes of `type` set to or auto-typed to "date".
        x
            Sets the x position (in normalized coordinates) of the
            range selector.
        xanchor
            Sets the range selector's horizontal position anchor.
            This anchor binds the `x` position to the "left",
            "center" or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            range selector.
        yanchor
            Sets the range selector's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.
        """

    def __init__(
        self,
        arg=None,
        activecolor=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        buttons=None,
        buttondefaults=None,
        font=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs
    ):
        """
        Construct a new Rangeselector object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.xaxis.Rangeselector`
        activecolor
            Sets the background color of the active range selector
            button.
        bgcolor
            Sets the background color of the range selector
            buttons.
        bordercolor
            Sets the color of the border enclosing the range
            selector.
        borderwidth
            Sets the width (in px) of the border enclosing the
            range selector.
        buttons
            Sets the specifications for each buttons. By default, a
            range selector comes with no buttons.
        buttondefaults
            When used in a template (as layout.template.layout.xaxi
            s.rangeselector.buttondefaults), sets the default
            property values to use for elements of
            layout.xaxis.rangeselector.buttons
        font
            Sets the font of the range selector button text.
        visible
            Determines whether or not this range selector is
            visible. Note that range selectors are only available
            for x axes of `type` set to or auto-typed to "date".
        x
            Sets the x position (in normalized coordinates) of the
            range selector.
        xanchor
            Sets the range selector's horizontal position anchor.
            This anchor binds the `x` position to the "left",
            "center" or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            range selector.
        yanchor
            Sets the range selector's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.

        Returns
        -------
        Rangeselector
        """
        super(Rangeselector, self).__init__("rangeselector")

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
The first argument to the plotly.graph_objs.layout.xaxis.Rangeselector 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.layout.xaxis.Rangeselector`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis import rangeselector as v_rangeselector

        # Initialize validators
        # ---------------------
        self._validators["activecolor"] = v_rangeselector.ActivecolorValidator()
        self._validators["bgcolor"] = v_rangeselector.BgcolorValidator()
        self._validators["bordercolor"] = v_rangeselector.BordercolorValidator()
        self._validators["borderwidth"] = v_rangeselector.BorderwidthValidator()
        self._validators["buttons"] = v_rangeselector.ButtonsValidator()
        self._validators["buttondefaults"] = v_rangeselector.ButtonValidator()
        self._validators["font"] = v_rangeselector.FontValidator()
        self._validators["visible"] = v_rangeselector.VisibleValidator()
        self._validators["x"] = v_rangeselector.XValidator()
        self._validators["xanchor"] = v_rangeselector.XanchorValidator()
        self._validators["y"] = v_rangeselector.YValidator()
        self._validators["yanchor"] = v_rangeselector.YanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("activecolor", None)
        self["activecolor"] = activecolor if activecolor is not None else _v
        _v = arg.pop("bgcolor", None)
        self["bgcolor"] = bgcolor if bgcolor is not None else _v
        _v = arg.pop("bordercolor", None)
        self["bordercolor"] = bordercolor if bordercolor is not None else _v
        _v = arg.pop("borderwidth", None)
        self["borderwidth"] = borderwidth if borderwidth is not None else _v
        _v = arg.pop("buttons", None)
        self["buttons"] = buttons if buttons is not None else _v
        _v = arg.pop("buttondefaults", None)
        self["buttondefaults"] = buttondefaults if buttondefaults is not None else _v
        _v = arg.pop("font", None)
        self["font"] = font if font is not None else _v
        _v = arg.pop("visible", None)
        self["visible"] = visible if visible is not None else _v
        _v = arg.pop("x", None)
        self["x"] = x if x is not None else _v
        _v = arg.pop("xanchor", None)
        self["xanchor"] = xanchor if xanchor is not None else _v
        _v = arg.pop("y", None)
        self["y"] = y if y is not None else _v
        _v = arg.pop("yanchor", None)
        self["yanchor"] = yanchor if yanchor is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False


__all__ = [
    "Rangeselector",
    "Rangeslider",
    "Tickfont",
    "Tickformatstop",
    "Tickformatstop",
    "Title",
    "rangeselector",
    "rangeslider",
    "title",
]

from plotly.graph_objs.layout.xaxis import title
from plotly.graph_objs.layout.xaxis import rangeslider
from plotly.graph_objs.layout.xaxis import rangeselector
