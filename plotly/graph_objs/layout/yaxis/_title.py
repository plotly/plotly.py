

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Title(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout.yaxis'
    _path_str = 'layout.yaxis.title'
    _valid_props = {"font", "standoff", "text"}

    # font
    # ----
    @property
    def font(self):
        """
        Sets this axis' title font.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.yaxis.title.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.yaxis.title.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

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
        return self['standoff']

    @standoff.setter
    def standoff(self, val):
        self['standoff'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of this axis.

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
        font
            Sets this axis' title font.
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
            Sets the title of this axis.
        """
    def __init__(self,
            arg=None,
            font=None,
            standoff=None,
            text=None,
            **kwargs
        ):
        """
        Construct a new Title object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.yaxis.Title`
        font
            Sets this axis' title font.
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
            Sets the title of this axis.

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
The first argument to the plotly.graph_objs.layout.yaxis.Title
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.yaxis.Title`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('font', arg, font)
        self._init_provided('standoff', arg, standoff)
        self._init_provided('text', arg, text)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
