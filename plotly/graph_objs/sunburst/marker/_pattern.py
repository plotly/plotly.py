from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Pattern(_BaseTraceHierarchyType):

    _parent_path_str = "sunburst.marker"
    _path_str = "sunburst.marker.pattern"
    _valid_props = {
        "bgcolor",
        "bgcolorsrc",
        "fgcolor",
        "fgcolorsrc",
        "fgopacity",
        "fillmode",
        "shape",
        "shapesrc",
        "size",
        "sizesrc",
        "solidity",
        "soliditysrc",
    }

    @property
    def bgcolor(self):
        """
        When there is no colorscale sets the color of background
        pattern fill. Defaults to a `marker.color` background when
        `fillmode` is "overlay". Otherwise, defaults to a transparent
        background.

        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|NDArray
        """
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def bgcolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `bgcolor`.

        The 'bgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["bgcolorsrc"]

    @bgcolorsrc.setter
    def bgcolorsrc(self, val):
        self["bgcolorsrc"] = val

    @property
    def fgcolor(self):
        """
        When there is no colorscale sets the color of foreground
        pattern fill. Defaults to a `marker.color` background when
        `fillmode` is "replace". Otherwise, defaults to dark grey or
        white to increase contrast with the `bgcolor`.

        The 'fgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color
          - A list or array of any of the above

        Returns
        -------
        str|NDArray
        """
        return self["fgcolor"]

    @fgcolor.setter
    def fgcolor(self, val):
        self["fgcolor"] = val

    @property
    def fgcolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `fgcolor`.

        The 'fgcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["fgcolorsrc"]

    @fgcolorsrc.setter
    def fgcolorsrc(self, val):
        self["fgcolorsrc"] = val

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
        Any|NDArray
        """
        return self["shape"]

    @shape.setter
    def shape(self, val):
        self["shape"] = val

    @property
    def shapesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `shape`.

        The 'shapesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["shapesrc"]

    @shapesrc.setter
    def shapesrc(self, val):
        self["shapesrc"] = val

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
        int|float|NDArray
        """
        return self["size"]

    @size.setter
    def size(self, val):
        self["size"] = val

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
        return self["sizesrc"]

    @sizesrc.setter
    def sizesrc(self, val):
        self["sizesrc"] = val

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
        int|float|NDArray
        """
        return self["solidity"]

    @solidity.setter
    def solidity(self, val):
        self["solidity"] = val

    @property
    def soliditysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `solidity`.

        The 'soliditysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["soliditysrc"]

    @soliditysrc.setter
    def soliditysrc(self, val):
        self["soliditysrc"] = val

    @property
    def _prop_descriptions(self):
        return """\
        bgcolor
            When there is no colorscale sets the color of
            background pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "overlay". Otherwise,
            defaults to a transparent background.
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `bgcolor`.
        fgcolor
            When there is no colorscale sets the color of
            foreground pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "replace". Otherwise,
            defaults to dark grey or white to increase contrast
            with the `bgcolor`.
        fgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `fgcolor`.
        fgopacity
            Sets the opacity of the foreground pattern fill.
            Defaults to a 0.5 when `fillmode` is "overlay".
            Otherwise, defaults to 1.
        fillmode
            Determines whether `marker.color` should be used as a
            default to `bgcolor` or a `fgcolor`.
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        shapesrc
            Sets the source reference on Chart Studio Cloud for
            `shape`.
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.
        soliditysrc
            Sets the source reference on Chart Studio Cloud for
            `solidity`.
        """

    def __init__(
        self,
        arg=None,
        bgcolor: str | None = None,
        bgcolorsrc: str | None = None,
        fgcolor: str | None = None,
        fgcolorsrc: str | None = None,
        fgopacity: int | float | None = None,
        fillmode: Any | None = None,
        shape: Any | None = None,
        shapesrc: str | None = None,
        size: int | float | None = None,
        sizesrc: str | None = None,
        solidity: int | float | None = None,
        soliditysrc: str | None = None,
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
            :class:`plotly.graph_objs.sunburst.marker.Pattern`
        bgcolor
            When there is no colorscale sets the color of
            background pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "overlay". Otherwise,
            defaults to a transparent background.
        bgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `bgcolor`.
        fgcolor
            When there is no colorscale sets the color of
            foreground pattern fill. Defaults to a `marker.color`
            background when `fillmode` is "replace". Otherwise,
            defaults to dark grey or white to increase contrast
            with the `bgcolor`.
        fgcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `fgcolor`.
        fgopacity
            Sets the opacity of the foreground pattern fill.
            Defaults to a 0.5 when `fillmode` is "overlay".
            Otherwise, defaults to 1.
        fillmode
            Determines whether `marker.color` should be used as a
            default to `bgcolor` or a `fgcolor`.
        shape
            Sets the shape of the pattern fill. By default, no
            pattern is used for filling the area.
        shapesrc
            Sets the source reference on Chart Studio Cloud for
            `shape`.
        size
            Sets the size of unit squares of the pattern fill in
            pixels, which corresponds to the interval of repetition
            of the pattern.
        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        solidity
            Sets the solidity of the pattern fill. Solidity is
            roughly the fraction of the area filled by the pattern.
            Solidity of 0 shows only the background color without
            pattern and solidty of 1 shows only the foreground
            color without pattern.
        soliditysrc
            Sets the source reference on Chart Studio Cloud for
            `solidity`.

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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.sunburst.marker.Pattern
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sunburst.marker.Pattern`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._init_provided("bgcolor", arg, bgcolor)
        self._init_provided("bgcolorsrc", arg, bgcolorsrc)
        self._init_provided("fgcolor", arg, fgcolor)
        self._init_provided("fgcolorsrc", arg, fgcolorsrc)
        self._init_provided("fgopacity", arg, fgopacity)
        self._init_provided("fillmode", arg, fillmode)
        self._init_provided("shape", arg, shape)
        self._init_provided("shapesrc", arg, shapesrc)
        self._init_provided("size", arg, size)
        self._init_provided("sizesrc", arg, sizesrc)
        self._init_provided("solidity", arg, solidity)
        self._init_provided("soliditysrc", arg, soliditysrc)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
