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
    _widget_data = List().tag(sync=True, **custom_serializers)
    _config = Dict().tag(sync=True, **custom_serializers)
    _js2py_pointsCallback = Dict(allow_none=True).tag(sync=True, **custom_serializers)

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
        self._widget_data = deepcopy(self._data)

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

    def _send_react_msg(self):
        self._widget_layout = deepcopy(self._layout_obj._props)
        self._widget_data = deepcopy(self._data)


    def _send_animate_msg(
        self, styles_data, relayout_data, trace_indexes, animation_opts
    ):
        """
        Send Plotly.update message to the frontend
        Note: there is no source_view_id parameter because animations
        triggered by the fontend are not currently supported
        Parameters
        ----------
        styles_data : list[dict]
            Plotly.animate styles data
        relayout_data : dict
            Plotly.animate relayout data
        trace_indexes : list[int]
            List of trace indexes that the animate operation applies to
        """
        print('sending animate message')

        # Validate / normalize inputs
        # ---------------------------
        trace_indexes = self._normalize_trace_indexes(trace_indexes)

        # Increment layout/trace edit message IDs
        # ---------------------------------------
        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True

        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True

        # Build message
        # -------------
        animate_msg = {
            "style_data": styles_data,
            "layout_data": relayout_data,
            "style_traces": trace_indexes,
            "animation_opts": animation_opts,
            "trace_edit_id": trace_edit_id,
            "layout_edit_id": layout_edit_id,
            "source_view_id": None,
        }

        # Send message
        # ------------
        self._py2js_animate = animate_msg
        self._py2js_animate = None

    @observe("_js2py_pointsCallback")
    def _handler_js2py_pointsCallback(self, change):
        """
        Process points callback message from the frontend
        """
        # Receive message
        # ---------------
        callback_data = change["new"]

        if not callback_data:
            self._js2py_pointsCallback = None
            return

        # Get event type
        # --------------
        event_type = callback_data["event_type"]

        # Build Selector Object
        # ---------------------
        if callback_data.get("selector", None):
            selector_data = callback_data["selector"]
            selector_type = selector_data["type"]
            selector_state = selector_data["selector_state"]
            if selector_type == "box":
                selector = BoxSelector(**selector_state)
            elif selector_type == "lasso":
                selector = LassoSelector(**selector_state)
            else:
                raise ValueError("Unsupported selector type: %s" % selector_type)
        else:
            selector = None

        # Build Input Device State Object
        # -------------------------------
        if callback_data.get("device_state", None):
            device_state_data = callback_data["device_state"]
            state = InputDeviceState(**device_state_data)
        else:
            state = None

        # Build Trace Points Dictionary
        # -----------------------------
        points_data = callback_data["points"]
        trace_points = {
            trace_ind: {
                "point_inds": [],
                "xs": [],
                "ys": [],
                "trace_name": self._data_objs[trace_ind].name,
                "trace_index": trace_ind,
            }
            for trace_ind in range(len(self._data_objs))
        }

        for x, y, point_ind, trace_ind in zip(
            points_data["xs"],
            points_data["ys"],
            points_data["point_indexes"],
            points_data["trace_indexes"],
        ):

            trace_dict = trace_points[trace_ind]
            trace_dict["xs"].append(x)
            trace_dict["ys"].append(y)
            trace_dict["point_inds"].append(point_ind)

        # Dispatch callbacks
        # ------------------
        for trace_ind, trace_points_data in trace_points.items():
            points = Points(**trace_points_data)
            trace = self.data[trace_ind]

            if event_type == "plotly_click":
                trace._dispatch_on_click(points, state)
            elif event_type == "plotly_hover":
                trace._dispatch_on_hover(points, state)
            elif event_type == "plotly_unhover":
                trace._dispatch_on_unhover(points, state)
            elif event_type == "plotly_selected":
                trace._dispatch_on_selection(points, selector)
            elif event_type == "plotly_deselect":
                trace._dispatch_on_deselect(points)

        self._js2py_pointsCallback = None


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
