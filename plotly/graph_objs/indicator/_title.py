

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Title(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'indicator'
    _path_str = 'indicator.title'
    _valid_props = {"align", "font", "text"}

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the title. It defaults to
        `center` except for bullet charts for which it defaults to
        right.

        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['align']

    @align.setter
    def align(self, val):
        self['align'] = val

    # font
    # ----
    @property
    def font(self):
        """
        Set the font used to display the title

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.title.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.indicator.title.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of this indicator.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the title. It defaults
            to `center` except for bullet charts for which it
            defaults to right.
        font
            Set the font used to display the title
        text
            Sets the title of this indicator.
        """
    def __init__(self,
            arg=None,
            align: Any|None = None,
            font: None|None = None,
            text: str|None = None,
            **kwargs
        ):
        """
        Construct a new Title object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.indicator.Title`
        align
            Sets the horizontal alignment of the title. It defaults
            to `center` except for bullet charts for which it
            defaults to right.
        font
            Set the font used to display the title
        text
            Sets the title of this indicator.

        Returns
        -------
        Title
        """
        super().__init__('title')
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
The first argument to the plotly.graph_objs.indicator.Title
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.Title`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('align', arg, align)
        self._init_provided('font', arg, font)
        self._init_provided('text', arg, text)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
