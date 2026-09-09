#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Textfont(_BaseTraceHierarchyType):
    _parent_path_str = "scatter3d"
    _path_str = "scatter3d.textfont"
    _valid_props = {"color", "family", "size", "style", "variant", "weight"}

    @property
    def color(self):
        """
        The 'color' property is a color and may be specified as a string in the following formats:
          - hex or short hex (e.g. '#d3d3d3', '#d3d')
          - hex or short hex with alpha (e.g. '#d3d3d380', '#d3d8')
          - rgb (e.g. 'rgb(255, 0, 0)', 'rgb(255 0 0)')
          - rgba (e.g. 'rgba(255, 0, 0, 0.5)', 'rgba(255 0 0 / 0.5)')
          - hsl (e.g. 'hsl(0, 100%, 50%)', 'hsl(0deg 100% 50%)')
          - hsla (e.g. 'hsla(0, 100%, 50%, 0.5)', 'hsla(0deg 100% 50% / 0.5)')
          - hwb (e.g. 'hwb(0 0% 100%)')
          - lab/lch/oklab/oklch (e.g. 'oklch(0.7 0.15 180)')
          - color (e.g. 'color(display-p3 1 0 0)')
          - named colors (full list: https://www.w3.org/TR/css-color-4/#named-color)
          - Any other supported CSS 4 color format: https://www.w3.org/TR/css-color-4/
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser can only apply a font if it is
        available on the system where it runs. Provide multiple font
        families, separated by commas, to indicate the order in which
        to apply fonts if they aren't available.

        The 'family' property is a string and must be specified as:
          - A non-empty string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["family"]

    @family.setter
    def family(self, val):
        self["family"] = val

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
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

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
        return self["style"]

    @style.setter
    def style(self, val):
        self["style"] = val

    @property
    def variant(self):
        """
        Sets the variant of the font.

        The 'variant' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'small-caps']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["variant"]

    @variant.setter
    def variant(self, val):
        self["variant"] = val

    @property
    def weight(self):
        """
        Sets the weight (or boldness) of the font.

        The 'weight' property is an integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 1000]
            OR exactly one of ['normal', 'bold'] (e.g. 'bold')
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|numpy.ndarray
        """
        return self["weight"]

    @weight.setter
    def weight(self, val):
        self["weight"] = val

    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser can only apply a font
            if it is available on the system where it runs. Provide
            multiple font families, separated by commas, to
            indicate the order in which to apply fonts if they
            aren't available.
        size

        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        variant
            Sets the variant of the font.
        weight
            Sets the weight (or boldness) of the font.
        """

    def __init__(
        self,
        arg=None,
        color=None,
        family=None,
        size=None,
        style=None,
        variant=None,
        weight=None,
        **kwargs,
    ):
        """
        Construct a new Textfont object

        Sets the text font.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatter3d.Textfont`
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser can only apply a font
            if it is available on the system where it runs. Provide
            multiple font families, separated by commas, to
            indicate the order in which to apply fonts if they
            aren't available.
        size

        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        variant
            Sets the variant of the font.
        weight
            Sets the weight (or boldness) of the font.

        Returns
        -------
        Textfont
        """
        super().__init__("textfont")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.scatter3d.Textfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scatter3d.Textfont`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("color", arg, color)
        self._set_property("family", arg, family)
        self._set_property("size", arg, size)
        self._set_property("style", arg, style)
        self._set_property("variant", arg, variant)
        self._set_property("weight", arg, weight)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
