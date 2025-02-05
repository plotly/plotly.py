

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class X(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'surface.contours'
    _path_str = 'surface.contours.x'
    _valid_props = {"color", "end", "highlight", "highlightcolor", "highlightwidth", "project", "show", "size", "start", "usecolormap", "width"}

    # color
    # -----
    @property
    def color(self):
        """
        Sets the color of the contour lines.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # end
    # ---
    @property
    def end(self):
        """
        Sets the end contour level value. Must be more than
        `contours.start`

        The 'end' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['end']

    @end.setter
    def end(self, val):
        self['end'] = val

    # highlight
    # ---------
    @property
    def highlight(self):
        """
        Determines whether or not contour lines about the x dimension
        are highlighted on hover.

        The 'highlight' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['highlight']

    @highlight.setter
    def highlight(self, val):
        self['highlight'] = val

    # highlightcolor
    # --------------
    @property
    def highlightcolor(self):
        """
        Sets the color of the highlighted contour lines.

        The 'highlightcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['highlightcolor']

    @highlightcolor.setter
    def highlightcolor(self, val):
        self['highlightcolor'] = val

    # highlightwidth
    # --------------
    @property
    def highlightwidth(self):
        """
        Sets the width of the highlighted contour lines.

        The 'highlightwidth' property is a number and may be specified as:
          - An int or float in the interval [1, 16]

        Returns
        -------
        int|float
        """
        return self['highlightwidth']

    @highlightwidth.setter
    def highlightwidth(self, val):
        self['highlightwidth'] = val

    # project
    # -------
    @property
    def project(self):
        """
        The 'project' property is an instance of Project
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.surface.contours.x.Project`
          - A dict of string/value properties that will be passed
            to the Project constructor

        Returns
        -------
        plotly.graph_objs.surface.contours.x.Project
        """
        return self['project']

    @project.setter
    def project(self, val):
        self['project'] = val

    # show
    # ----
    @property
    def show(self):
        """
        Determines whether or not contour lines about the x dimension
        are drawn.

        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['show']

    @show.setter
    def show(self, val):
        self['show'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the step between each contour level. Must be positive.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # start
    # -----
    @property
    def start(self):
        """
        Sets the starting contour level value. Must be less than
        `contours.end`

        The 'start' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['start']

    @start.setter
    def start(self, val):
        self['start'] = val

    # usecolormap
    # -----------
    @property
    def usecolormap(self):
        """
        An alternate to "color". Determines whether or not the contour
        lines are colored using the trace "colorscale".

        The 'usecolormap' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['usecolormap']

    @usecolormap.setter
    def usecolormap(self, val):
        self['usecolormap'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width of the contour lines.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [1, 16]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the color of the contour lines.
        end
            Sets the end contour level value. Must be more than
            `contours.start`
        highlight
            Determines whether or not contour lines about the x
            dimension are highlighted on hover.
        highlightcolor
            Sets the color of the highlighted contour lines.
        highlightwidth
            Sets the width of the highlighted contour lines.
        project
            :class:`plotly.graph_objects.surface.contours.x.Project
            ` instance or dict with compatible properties
        show
            Determines whether or not contour lines about the x
            dimension are drawn.
        size
            Sets the step between each contour level. Must be
            positive.
        start
            Sets the starting contour level value. Must be less
            than `contours.end`
        usecolormap
            An alternate to "color". Determines whether or not the
            contour lines are colored using the trace "colorscale".
        width
            Sets the width of the contour lines.
        """
    def __init__(self,
            arg=None,
            color: str|None = None,
            end: int|float|None = None,
            highlight: bool|None = None,
            highlightcolor: str|None = None,
            highlightwidth: int|float|None = None,
            project: None|None = None,
            show: bool|None = None,
            size: int|float|None = None,
            start: int|float|None = None,
            usecolormap: bool|None = None,
            width: int|float|None = None,
            **kwargs
        ):
        """
        Construct a new X object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.surface.contours.X`
        color
            Sets the color of the contour lines.
        end
            Sets the end contour level value. Must be more than
            `contours.start`
        highlight
            Determines whether or not contour lines about the x
            dimension are highlighted on hover.
        highlightcolor
            Sets the color of the highlighted contour lines.
        highlightwidth
            Sets the width of the highlighted contour lines.
        project
            :class:`plotly.graph_objects.surface.contours.x.Project
            ` instance or dict with compatible properties
        show
            Determines whether or not contour lines about the x
            dimension are drawn.
        size
            Sets the step between each contour level. Must be
            positive.
        start
            Sets the starting contour level value. Must be less
            than `contours.end`
        usecolormap
            An alternate to "color". Determines whether or not the
            contour lines are colored using the trace "colorscale".
        width
            Sets the width of the contour lines.

        Returns
        -------
        X
        """
        super().__init__('x')
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
The first argument to the plotly.graph_objs.surface.contours.X
constructor must be a dict or
an instance of :class:`plotly.graph_objs.surface.contours.X`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('end', arg, end)
        self._init_provided('highlight', arg, highlight)
        self._init_provided('highlightcolor', arg, highlightcolor)
        self._init_provided('highlightwidth', arg, highlightwidth)
        self._init_provided('project', arg, project)
        self._init_provided('show', arg, show)
        self._init_provided('size', arg, size)
        self._init_provided('start', arg, start)
        self._init_provided('usecolormap', arg, usecolormap)
        self._init_provided('width', arg, width)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
