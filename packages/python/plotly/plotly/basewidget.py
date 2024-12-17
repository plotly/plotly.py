from copy import deepcopy
import pathlib
import pdb
from traitlets import List, Dict, observe, Integer
from plotly.io._renderers import display_jupyter_version_warnings

from .basedatatypes import BaseFigure, BasePlotlyType
from .callbacks import BoxSelector, LassoSelector, InputDeviceState, Points
from .serializers import custom_serializers
from .version import __frontend_version__
import anywidget


class BaseFigureWidget(BaseFigure, anywidget.AnyWidget):
    """
    Base class for FigureWidget. The FigureWidget class is code-generated as a
    subclass
    """

    _esm = pathlib.Path(__file__).parent / "package_data" / "widgetbundle.js"

    # ### _data and _layout ###
    # These properties store the current state of the traces and
    # layout as JSON-style dicts. These dicts do not store any subclasses of
    # `BasePlotlyType`
    _widget_layout = Dict().tag(sync=True, **custom_serializers)
    _data = List().tag(sync=True, **custom_serializers)
    _config = Dict().tag(sync=True, **custom_serializers)

    _frame_objs = []

    # Constructor
    # -----------
    def __init__(
        self, data=None, layout=None, frames=None, skip_invalid=False, **kwargs
    ):

        # Call superclass constructors
        # ----------------------------
        # Note: We rename layout to layout_plotly to deconflict it
        # with the `layout` constructor parameter of the `widgets.DOMWidget`
        # ipywidgets class
        super(BaseFigureWidget, self).__init__(
            data=data,
            layout_plotly=layout,
            frames=frames,
            skip_invalid=skip_invalid,
            **kwargs,
        )

        self._widget_layout = deepcopy(self._layout_obj._props)

    def show(self, *args, **kwargs):
        return self

    # Display
    # -------
    def _repr_html_(self):
        """
        Customize html representation
        """
        raise NotImplementedError  # Prefer _repr_mimebundle_

    def _repr_mimebundle_(self, include=None, exclude=None, validate=True, **kwargs):
        """
        Return mimebundle corresponding to default renderer.
        """
        display_jupyter_version_warnings()
        return {
            "application/vnd.jupyter.widget-view+json": {
                "version_major": 2,
                "version_minor": 0,
                "model_id": self._model_id,
            },
        }

    def _ipython_display_(self):
        """
        Handle rich display of figures in ipython contexts
        """
        raise NotImplementedError  # Prefer _repr_mimebundle_

    def notify_change(self, change):
        # print('notify_change', change)
        return super().notify_change(change)

    def _send_relayout_msg(self, layout, source_view_id=None):
        new_layout = deepcopy(self._layout_obj._props)
        # del new_layout['template']['layout']['font']
        self._widget_layout = deepcopy(self._layout_obj._props)

    # Validate No Frames
    # ------------------
    @property
    def frames(self):
        # Note: This property getter is identical to that of the superclass,
        # but it must be included here because we're overriding the setter
        # below.
        return self._frame_objs

    @frames.setter
    def frames(self, new_frames):
        if new_frames:
            BaseFigureWidget._display_frames_error()

    @staticmethod
    def _display_frames_error():
        """
        Display an informative error when user attempts to set frames on a
        FigureWidget

        Raises
        ------
        ValueError
            always
        """
        msg = """
Frames are not supported by the plotly.graph_objs.FigureWidget class.
Note: Frames are supported by the plotly.graph_objs.Figure class"""
        raise ValueError(msg)
