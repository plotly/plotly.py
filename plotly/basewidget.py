from pprint import pprint

import ipywidgets as widgets
from traitlets import List, Unicode, Dict, observe, Integer, Undefined
from plotly.basedatatypes import BaseFigure
from plotly.callbacks import BoxSelector, LassoSelector, InputDeviceState, Points
from plotly.serializers import custom_serializers


@widgets.register
class BaseFigureWidget(BaseFigure, widgets.DOMWidget):

    # Widget Traits
    # -------------
    _view_name = Unicode('FigureView').tag(sync=True)
    _view_module = Unicode('plotlywidget').tag(sync=True)
    _model_name = Unicode('FigureModel').tag(sync=True)
    _model_module = Unicode('plotlywidget').tag(sync=True)

    # Data properties for front end
    # Note: These are only automatically synced on full assignment, not on mutation
    _layout = Dict().tag(sync=True, **custom_serializers)
    _data = List().tag(sync=True, **custom_serializers)

    # Python -> JS message properties
    _py2js_addTraces = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    _py2js_restyle = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_relayout = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_update = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_animate = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    _py2js_deleteTraces = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_moveTraces = Dict(allow_none=True).tag(sync=True,
                                                  **custom_serializers)

    _py2js_removeLayoutProps = Dict(allow_none=True).tag(sync=True,
                                                         **custom_serializers)
    _py2js_removeTraceProps = Dict(allow_none=True).tag(sync=True,
                                                        **custom_serializers)
    _py2js_requestSvg = Unicode(allow_none=True).tag(sync=True)

    # JS -> Python message properties
    _js2py_traceDeltas = Dict(allow_none=True).tag(sync=True,
                                                   **custom_serializers)
    _js2py_layoutDelta = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_restyle = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_relayout = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_update = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    # For plotly_select/hover/unhover/click
    _js2py_pointsCallback = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    # Message tracking
    _last_layout_edit_id = Integer(0).tag(sync=True)
    _last_trace_edit_id = Integer(0).tag(sync=True)

    # Constructor
    # -----------
    def __init__(self, data=None, layout=None, frames=None):
        # TODO: error if frames is not None
        # Validate Frames
        # ---------------
        if frames:
            BaseFigureWidget._display_frames_error()

        self._frame_objs = None

        # Call superclass constructors
        # ----------------------------
        # Note: We rename layout to layout_plotly because ipywidget also accepts a layout parameter
        # We map a layout_ipywidget property to the layout property of the ipywidget
        super().__init__(data=data, layout_plotly=layout)

        # Messages
        # --------
        self.on_msg(self._handler_messages)

    # ### Trait methods ###
    @observe('_js2py_traceDeltas')
    def handler_plotly_traceDeltas(self, change):

        # Unpack message
        msg_data = change['new']

        if not msg_data:
            return

        trace_deltas = msg_data['trace_deltas']
        trace_edit_id = msg_data['trace_edit_id']
        self._js2py_traceDeltas = None

        # print(f'traceDeltas: {trace_edit_id} == {self._last_trace_edit_id}')
        if trace_edit_id == self._last_trace_edit_id:
            for delta in trace_deltas:
                trace_uid = delta['uid']

                trace_uids = [trace.uid for trace in self.data]
                trace_index = trace_uids.index(trace_uid)
                uid_trace = self.data[trace_index]
                delta_transform = BaseFigure._transform_data(uid_trace._prop_defaults, delta)

                remove_props = self._remove_overlapping_props(uid_trace._props, uid_trace._prop_defaults)

                if remove_props:
                    # print(f'Removed_props: {remove_props}')
                    remove_trace_props_msg = {
                        'remove_trace': trace_index,
                        'remove_props': remove_props
                    }
                    self._py2js_removeTraceProps = remove_trace_props_msg
                    self._py2js_removeTraceProps = None

                # print(delta_transform)
                self._dispatch_change_callbacks_restyle(delta_transform, [trace_index])

            self._restyle_in_process = False
            while self._waiting_restyle_callbacks:
                # Call callbacks
                self._waiting_restyle_callbacks.pop()()

    @observe('_js2py_restyle')
    def handler_js2py_restyle(self, change):
        restyle_msg = change['new']
        self._js2py_restyle = None

        if not restyle_msg:
            return

        style_data = restyle_msg['style_data']
        style_traces = restyle_msg['style_traces']
        source_view_id = restyle_msg['source_view_id']
        self.plotly_restyle(style=style_data,
                            trace_indexes=style_traces,
                            source_view_id=source_view_id)

    @observe('_js2py_update')
    def handler_js2py_update(self, change):
        update_msg = change['new']
        self._js2py_update = None

        if not update_msg:
            return

        # print('Update (JS->Py):')
        # pprint(update_msg)

        style = update_msg['style_data']
        trace_indexes = update_msg['style_traces']
        layout = update_msg['layout_data']
        source_view_id = update_msg['source_view_id']

        self.plotly_update(style=style, layout=layout,
                           trace_indexes=trace_indexes,
                           source_view_id=source_view_id)

    @observe('_js2py_layoutDelta')
    def handler_plotly_layoutDelta(self, change):

        # Unpack message
        msg_data = change['new']

        self._js2py_layoutDelta = None

        if not msg_data:
            return

        layout_delta = msg_data['layout_delta']
        layout_edit_id = msg_data['layout_edit_id']

        # print(f'layoutDelta: {layout_edit_id} == {self._last_layout_edit_id}')
        if layout_edit_id == self._last_layout_edit_id:

            # print('Processing layoutDelta')
            # print('layoutDelta: {deltas}'.format(deltas=layout_delta))
            delta_transform = self._transform_data(self._layout_defaults, layout_delta)
            # print(f'delta_transform: {delta_transform}')

            # No relayout messages in process. Handle removing overlapping properties
            removed_props = self._remove_overlapping_props(self._layout, self._layout_defaults)

            if removed_props:
                # print(f'Removed_props: {removed_props}')
                remove_props_msg = {
                    'remove_props': removed_props
                }

                self._py2js_removeLayoutProps = remove_props_msg
                self._py2js_removeLayoutProps = None

            self._dispatch_change_callbacks_relayout(delta_transform)
            self._relayout_in_process = False
            while self._waiting_relayout_callbacks:
                # Call callbacks
                self._waiting_relayout_callbacks.pop()()

    @observe('_js2py_relayout')
    def handler_js2py_relayout(self, change):
        relayout_msg = change['new']

        self._js2py_relayout = None

        if not relayout_msg:
            return

        relayout_data = relayout_msg['relayout_data']
        source_view_id = relayout_msg['source_view_id']

        if 'lastInputTime' in relayout_data:
            # Remove 'lastInputTime'. Seems to be an internal plotly
            # property that is introduced for some plot types
            relayout_data.pop('lastInputTime')

        self.plotly_relayout(layout=relayout_data,
                             source_view_id=source_view_id)

    @observe('_js2py_pointsCallback')
    def handler_plotly_pointsCallback(self, change):
        callback_data = change['new']
        self._js2py_pointsCallback = None

        if not callback_data:
            return

        # Get event type
        # --------------
        event_type = callback_data['event_type']

        # Build Selector Object
        # ---------------------
        if callback_data.get('selector', None):
            selector_data = callback_data['selector']
            selector_type = selector_data['type']
            selector_state = selector_data['selector_state']
            if selector_type == 'box':
                selector = BoxSelector(**selector_state)
            elif selector_type == 'lasso':
                selector = LassoSelector(**selector_state)
            else:
                raise ValueError('Unsupported selector type: %s' % selector_type)
        else:
            selector = None

        # Build Input Device State Object
        # -------------------------
        if callback_data.get('device_state', None):
            device_state_data = callback_data['device_state']
            state = InputDeviceState(**device_state_data)
        else:
            state = None

        # Build Trace Points Dictionary
        # -----------------------------
        points_data = callback_data['points']
        trace_points = {trace_ind: {'point_inds': [],
                                    'xs': [],
                                    'ys': [],
                                    'trace_name': self._data_objs[trace_ind].plotly_name,
                                    'trace_index': trace_ind}
                        for trace_ind in range(len(self._data_objs))}

        for x, y, point_ind, trace_ind in zip(points_data['xs'],
                                              points_data['ys'],
                                              points_data['point_indexes'],
                                              points_data['trace_indexes']):

            trace_dict = trace_points[trace_ind]
            trace_dict['xs'].append(x)
            trace_dict['ys'].append(y)
            trace_dict['point_inds'].append(point_ind)

        # Dispatch callbacks
        # ------------------
        for trace_ind, trace_points_data in trace_points.items():
            points = Points(**trace_points_data)
            trace = self.data[trace_ind]  # type: BaseTraceType

            if event_type == 'plotly_click':
                trace._dispatch_on_click(points, state)
            elif event_type == 'plotly_hover':
                trace._dispatch_on_hover(points, state)
            elif event_type == 'plotly_unhover':
                trace._dispatch_on_unhover(points, state)
            elif event_type == 'plotly_selected':
                # TODO: check if state is valid for selections
                trace._dispatch_on_selected(points, selector)

    # Custom Messages
    # ---------------
    def _handler_messages(self, widget, content, buffers):
        """Handle a msg from the front-end.
        """
        if content.get('event', '') == 'svg':
            req_id = content['req_id']
            svg_uri = content['svg_uri']
            self._do_save_image(req_id, svg_uri)

    # Validate No Frames
    # ------------------
    @property
    def frames(self):
        return self._frame_objs

    @frames.setter
    def frames(self, new_frames):
        if new_frames:
            BaseFigureWidget._display_frames_error()

    @staticmethod
    def _display_frames_error():
        msg = ("Frames are not supported by the datatypes.FigureWidget class.\n"
               "Note: Frames are supported by the datatypes.Figure class")

        raise ValueError(msg)
