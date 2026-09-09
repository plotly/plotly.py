#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Pattern(_BaseTraceHierarchyType):
    _parent_path_str = "bar.marker"
    _path_str = "bar.marker.pattern"
    _valid_props = {
        "bgcolor",
        "fgcolor",
        "fgopacity",
        "fillmode",
        "path",
        "shape",
        "size",
        "solidity",
    }

    @property
    def bgcolor(self):
        """
        When there is no colorscale sets the color of background
        pattern fill. Defaults to a `marker.color` background when
        `fillmode` is "overlay". Otherwise, defaults to a transparent
        background.

        The 'bgcolor' property is a color and may be specified as a string in the following formats:
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
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def fgcolor(self):
        """
        When there is no colorscale sets the color of foreground
        pattern fill. Defaults to a `marker.color` background when
        `fillmode` is "replace". Otherwise, defaults to dark grey or
        white to increase contrast with the `bgcolor`.

        The 'fgcolor' property is a color and may be specified as a string in the following formats:
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
        return self["fgcolor"]

    @fgcolor.setter
    def fgcolor(self, val):
        self["fgcolor"] = val

    @property
    def fgopacity(self):
        """
        Sets the opacity of the foreground pattern fill. Defaults to a
        0.5 when `fillmode` is "overlay". Otherwise, defaults to 1.

        The 'fgopacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["fgopacity"]

    @fgopacity.setter
    def fgopacity(self, val):
        self["fgopacity"] = val

    @property
    def fillmode(self):
        """
        Determines whether `marker.color` should be used as a default
        to `bgcolor` or a `fgcolor`.

        The 'fillmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['replace', 'overlay']

        Returns
        -------
        Any
        """
        return self["fillmode"]

    @fillmode.setter
    def fillmode(self, val):
        self["fillmode"] = val

    @property
    def path(self):
        """
        Sets a custom path for pattern fill. Use with no `shape` or
        `solidity`, provide an SVG path string for the regions of the
        square from (0,0) to (`size`,`size`) to color.

        The 'path' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["path"]

    @path.setter
    def path(self, val):
        self["path"] = val

    @property
    def shape(self):
        """
        Sets the shape of the pattern fill. By default, no pattern is
        used for filling the area.

        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['', '/', '\\', 'x', '-', '|', '+', '.']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    @property
    def size(self):
        """
        Sets the size of unit squares of the pattern fill in pixels,
        which corresponds to the interval of repetition of the pattern.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
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
    def solidity(self):
        """
        Sets the solidity of the pattern fill. Solidity is roughly the
        fraction of the area filled by the pattern. Solidity of 0 shows
        only the background color without pattern and solidty of 1
        shows only the foreground color without pattern.

        The 'solidity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self["solidity"]

    @solidity.setter
    def solidity(self, val):
        self["solidity"] = val

    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            When there is no colorscale sets the color of
            background pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "overlay". Otherwise,
            defaults to a transparent background.
        fgcolor
            When there is no colorscale sets the color of
            foreground pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "replace". Otherwise,
            defaults to dark grey or white to increase contrast
            with the `bgcolor`.
        fgopacity
            Sets the opacity of the foreground pattern fill.
            Defaults to a 0.5 when `fillmode` is "overlay".
            Otherwise, defaults to 1.
        fillmode
            Determines whether `marker.color` should be used as a
            default to `bgcolor` or a `fgcolor`.
        path
            Sets a custom path for pattern fill. Use with no
            `shape` or `solidity`, provide an SVG path string for
            the regions of the square from (0,0) to (`size`,`size`)
            to color.
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        fgcolor=None,
        fgopacity=None,
        fillmode=None,
        path=None,
        shape=None,
        size=None,
        solidity=None,
        **kwargs,
    ):
        """
        Construct a new Pattern object

        Sets the pattern within the marker.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.bar.marker.Pattern`
        bgcolor
            When there is no colorscale sets the color of
            background pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "overlay". Otherwise,
            defaults to a transparent background.
        fgcolor
            When there is no colorscale sets the color of
            foreground pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "replace". Otherwise,
            defaults to dark grey or white to increase contrast
            with the `bgcolor`.
        fgopacity
            Sets the opacity of the foreground pattern fill.
            Defaults to a 0.5 when `fillmode` is "overlay".
            Otherwise, defaults to 1.
        fillmode
            Determines whether `marker.color` should be used as a
            default to `bgcolor` or a `fgcolor`.
        path
            Sets a custom path for pattern fill. Use with no
            `shape` or `solidity`, provide an SVG path string for
            the regions of the square from (0,0) to (`size`,`size`)
            to color.
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.

        Returns
        -------
        Pattern
        """
        super().__init__("pattern")
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
The first argument to the plotly.graph_objs.bar.marker.Pattern
constructor must be a dict or
an instance of :class:`plotly.graph_objs.bar.marker.Pattern`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("bgcolor", arg, bgcolor)
        self._set_property("fgcolor", arg, fgcolor)
        self._set_property("fgopacity", arg, fgopacity)
        self._set_property("fillmode", arg, fillmode)
        self._set_property("path", arg, path)
        self._set_property("shape", arg, shape)
        self._set_property("size", arg, size)
        self._set_property("solidity", arg, solidity)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
