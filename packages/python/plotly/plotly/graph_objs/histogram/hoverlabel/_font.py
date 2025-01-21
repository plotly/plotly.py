

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Font(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'histogram.hoverlabel'
    _path_str = 'histogram.hoverlabel.font'
    _valid_props = {"color", "colorsrc", "family", "familysrc", "lineposition", "linepositionsrc", "shadow", "shadowsrc", "size", "sizesrc", "style", "stylesrc", "textcase", "textcasesrc", "variant", "variantsrc", "weight", "weightsrc"}

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
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

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
        "Droid Sans", "Droid Serif", "Droid Sans Mono", "Gravitas One",
        "Old Standard TT", "Open Sans", "Overpass", "PT Sans Narrow",
        "Raleway", "Times New Roman".

        The 'family' property is a string and must be specified as:
          - A non-empty string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['family']

    @family.setter
    def family(self, val):
        self['family'] = val

    # familysrc
    # ---------
    @property
    def familysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `family`.

        The 'familysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['familysrc']

    @familysrc.setter
    def familysrc(self, val):
        self['familysrc'] = val

    # lineposition
    # ------------
    @property
    def lineposition(self):
        """
        Sets the kind of decoration line(s) with text, such as an
        "under", "over" or "through" as well as combinations e.g.
        "under+over", etc.

        The 'lineposition' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['under', 'over', 'through'] joined with '+' characters
            (e.g. 'under+over')
            OR exactly one of ['none'] (e.g. 'none')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['lineposition']

    @lineposition.setter
    def lineposition(self, val):
        self['lineposition'] = val

    # linepositionsrc
    # ---------------
    @property
    def linepositionsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `lineposition`.

        The 'linepositionsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['linepositionsrc']

    @linepositionsrc.setter
    def linepositionsrc(self, val):
        self['linepositionsrc'] = val

    # shadow
    # ------
    @property
    def shadow(self):
        """
        Sets the shape and color of the shadow behind text. "auto"
        places minimal shadow and applies contrast text font color. See
        https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow
        for additional options.

        The 'shadow' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['shadow']

    @shadow.setter
    def shadow(self, val):
        self['shadow'] = val

    # shadowsrc
    # ---------
    @property
    def shadowsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `shadow`.

        The 'shadowsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['shadowsrc']

    @shadowsrc.setter
    def shadowsrc(self, val):
        self['shadowsrc'] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `size`.

        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['sizesrc']

    @sizesrc.setter
    def sizesrc(self, val):
        self['sizesrc'] = val

    # style
    # -----
    @property
    def style(self):
        """
        Sets whether a font should be styled with a normal or italic
        face from its family.

        The 'style' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'italic']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['style']

    @style.setter
    def style(self, val):
        self['style'] = val

    # stylesrc
    # --------
    @property
    def stylesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `style`.

        The 'stylesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['stylesrc']

    @stylesrc.setter
    def stylesrc(self, val):
        self['stylesrc'] = val

    # textcase
    # --------
    @property
    def textcase(self):
        """
        Sets capitalization of text. It can be used to make text appear
        in all-uppercase or all-lowercase, or with each word
        capitalized.

        The 'textcase' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'word caps', 'upper', 'lower']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['textcase']

    @textcase.setter
    def textcase(self, val):
        self['textcase'] = val

    # textcasesrc
    # -----------
    @property
    def textcasesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `textcase`.

        The 'textcasesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['textcasesrc']

    @textcasesrc.setter
    def textcasesrc(self, val):
        self['textcasesrc'] = val

    # variant
    # -------
    @property
    def variant(self):
        """
        Sets the variant of the font.

        The 'variant' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'small-caps', 'all-small-caps',
                'all-petite-caps', 'petite-caps', 'unicase']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self['variant']

    @variant.setter
    def variant(self, val):
        self['variant'] = val

    # variantsrc
    # ----------
    @property
    def variantsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `variant`.

        The 'variantsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['variantsrc']

    @variantsrc.setter
    def variantsrc(self, val):
        self['variantsrc'] = val

    # weight
    # ------
    @property
    def weight(self):
        """
        Sets the weight (or boldness) of the font.

        The 'weight' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 1000]
            OR exactly one of ['normal', 'bold'] (e.g. 'bold')
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|numpy.ndarray
        """
        return self['weight']

    @weight.setter
    def weight(self, val):
        self['weight'] = val

    # weightsrc
    # ---------
    @property
    def weightsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `weight`.

        The 'weightsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['weightsrc']

    @weightsrc.setter
    def weightsrc(self, val):
        self['weightsrc'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
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
            Sans", "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            `family`.
        lineposition
            Sets the kind of decoration line(s) with text, such as
            an "under", "over" or "through" as well as combinations
            e.g. "under+over", etc.
        linepositionsrc
            Sets the source reference on Chart Studio Cloud for
            `lineposition`.
        shadow
            Sets the shape and color of the shadow behind text.
            "auto" places minimal shadow and applies contrast text
            font color. See https://developer.mozilla.org/en-
            US/docs/Web/CSS/text-shadow for additional options.
        shadowsrc
            Sets the source reference on Chart Studio Cloud for
            `shadow`.
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        stylesrc
            Sets the source reference on Chart Studio Cloud for
            `style`.
        textcase
            Sets capitalization of text. It can be used to make
            text appear in all-uppercase or all-lowercase, or with
            each word capitalized.
        textcasesrc
            Sets the source reference on Chart Studio Cloud for
            `textcase`.
        variant
            Sets the variant of the font.
        variantsrc
            Sets the source reference on Chart Studio Cloud for
            `variant`.
        weight
            Sets the weight (or boldness) of the font.
        weightsrc
            Sets the source reference on Chart Studio Cloud for
            `weight`.
        """
    def __init__(self,
            arg=None,
            color=None,
            colorsrc=None,
            family=None,
            familysrc=None,
            lineposition=None,
            linepositionsrc=None,
            shadow=None,
            shadowsrc=None,
            size=None,
            sizesrc=None,
            style=None,
            stylesrc=None,
            textcase=None,
            textcasesrc=None,
            variant=None,
            variantsrc=None,
            weight=None,
            weightsrc=None,
            **kwargs
        ):
        """
        Construct a new Font object

        Sets the font used in hover labels.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.histogram.hoverlabel.Font`
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
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
            Sans", "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            `family`.
        lineposition
            Sets the kind of decoration line(s) with text, such as
            an "under", "over" or "through" as well as combinations
            e.g. "under+over", etc.
        linepositionsrc
            Sets the source reference on Chart Studio Cloud for
            `lineposition`.
        shadow
            Sets the shape and color of the shadow behind text.
            "auto" places minimal shadow and applies contrast text
            font color. See https://developer.mozilla.org/en-
            US/docs/Web/CSS/text-shadow for additional options.
        shadowsrc
            Sets the source reference on Chart Studio Cloud for
            `shadow`.
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        stylesrc
            Sets the source reference on Chart Studio Cloud for
            `style`.
        textcase
            Sets capitalization of text. It can be used to make
            text appear in all-uppercase or all-lowercase, or with
            each word capitalized.
        textcasesrc
            Sets the source reference on Chart Studio Cloud for
            `textcase`.
        variant
            Sets the variant of the font.
        variantsrc
            Sets the source reference on Chart Studio Cloud for
            `variant`.
        weight
            Sets the weight (or boldness) of the font.
        weightsrc
            Sets the source reference on Chart Studio Cloud for
            `weight`.

        Returns
        -------
        Font
        """
        super(Font, self).__init__('font')

        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.histogram.hoverlabel.Font
constructor must be a dict or
an instance of :class:`plotly.graph_objs.histogram.hoverlabel.Font`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('colorsrc', arg, colorsrc)
        self._init_provided('family', arg, family)
        self._init_provided('familysrc', arg, familysrc)
        self._init_provided('lineposition', arg, lineposition)
        self._init_provided('linepositionsrc', arg, linepositionsrc)
        self._init_provided('shadow', arg, shadow)
        self._init_provided('shadowsrc', arg, shadowsrc)
        self._init_provided('size', arg, size)
        self._init_provided('sizesrc', arg, sizesrc)
        self._init_provided('style', arg, style)
        self._init_provided('stylesrc', arg, stylesrc)
        self._init_provided('textcase', arg, textcase)
        self._init_provided('textcasesrc', arg, textcasesrc)
        self._init_provided('variant', arg, variant)
        self._init_provided('variantsrc', arg, variantsrc)
        self._init_provided('weight', arg, weight)
        self._init_provided('weightsrc', arg, weightsrc)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
