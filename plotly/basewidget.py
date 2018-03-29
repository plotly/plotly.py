from pprint import pprint
import uuid
from importlib import import_module
import os
import numbers
from urllib import parse

import ipywidgets as widgets
from traitlets import List, Unicode, Dict, observe, Integer, Undefined
from plotly.basedatatypes import BaseFigure, BasePlotlyType
from plotly.callbacks import BoxSelector, LassoSelector, InputDeviceState, Points
from plotly.serializers import custom_serializers


@widgets.register
class BaseFigureWidget(BaseFigure, widgets.DOMWidget):

    # Widget Traits
    # -------------
    _view_name = Unicode('FigureView').tag(sync=True)
    _view_module = Unicode('plotlywidget').tag(sync=True)
    _view_module_version = Unicode('0.1.0').tag(sync=True)

    _model_name = Unicode('FigureModel').tag(sync=True)
    _model_module = Unicode('plotlywidget').tag(sync=True)
    _model_module_version = Unicode('0.1.0').tag(sync=True)


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
    _py2js_svgRequest = Dict(allow_none=True).tag(sync=True)

    # JS -> Python message properties
    _js2py_traceDeltas = Dict(allow_none=True).tag(sync=True,
                                                   **custom_serializers)
    _js2py_layoutDelta = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_restyle = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_relayout = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_update = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    # For plotly_select/hover/unhover/click
    _js2py_pointsCallback = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    _js2py_svgResponse = Dict(allow_none=True).tag(sync=True, **custom_serializers)

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


        # Message States
        # --------------
        self._layout_edit_in_process = False
        self._waiting_relayout_callbacks = []
        self._last_layout_edit_id = 0

        self._trace_edit_in_process = False
        self._waiting_restyle_callbacks = []
        self._last_trace_edit_id = 0

        # View count
        # ----------
        # ipywidgets populates this if initialized.
        self._view_count = 0

        # SVG
        # ---
        self._svg_requests = {}


    def save_image(self, filename, image_type=None, scale_factor=2):
        """
        Save figure to a static image file

        Parameters
        ----------
        filename : str
            Image output file name
        image_type : str
            Image file type. One of: 'svg', 'png', 'pdf', or 'ps'. If not set, file type
            is inferred from the filename extension
        scale_factor : number
            (For png image type) Factor by which to increase the number of pixels in each
            dimension. A scale factor of 1 will result in a image with pixel dimensions
            (layout.width, layout.height).  A scale factor of 2 will result in an image
            with dimensions (2*layout.width, 2*layout.height), doubling image's DPI.
            (Default 2)
        """

        # Validate / infer image_type
        supported_image_types = ['svg', 'png', 'pdf', 'ps']
        cairo_image_types = ['png', 'pdf', 'ps']
        supported_types_csv = ', '.join(supported_image_types)

        if not image_type:
            # Infer image type from extension
            _, extension = os.path.splitext(filename)

            if not extension:
                raise ValueError('No image_type specified and file extension has no extension '
                                 'from which to infer an image type '
                                 'Supported image types are: {image_types}'
                                 .format(image_types=supported_types_csv))

            image_type = extension[1:]

        image_type = image_type.lower()
        if image_type not in supported_image_types:
            raise ValueError("Unsupported image type '{image_type}'\n"
                             "Supported image types are: {image_types}"
                             .format(image_type=image_type,
                                     image_types=supported_types_csv))

        # Validate cairo dependency
        if image_type in cairo_image_types:
            # Check whether we have cairosvg available
            try:
                import_module('cairosvg')
            except ModuleNotFoundError:
                raise ImportError('Exporting to {image_type} requires cairosvg'
                                  .format(image_type=image_type))

        # Validate scale_factor
        if not isinstance(scale_factor, numbers.Number) or scale_factor <= 0:
            raise ValueError('scale_factor must be a positive number.\n'
                             '    Received: {scale_factor}'.format(scale_factor=scale_factor))

        req_id = str(uuid.uuid1())

        # Register request
        self._svg_requests[req_id] = {'filename': filename,
                                      'image_type': image_type,
                                      'scale_factor': scale_factor}

        self._py2js_svgRequest = {'request_id': req_id}
        self._py2js_svgRequest = None

    def _do_save_image(self, req_id, svg_uri):
        req_info = self._svg_requests.pop(req_id, None)
        if not req_info:
            return

        # Remove svg header
        if not svg_uri.startswith('data:image/svg+xml,'):
            raise ValueError('Invalid svg data URI: ' + svg_uri[:20])

        svg = svg_uri.replace('data:image/svg+xml,', '')

        # Unquote characters (e.g. '%3Csvg%20' -> '<svg ')
        svg_bytes = parse.unquote(svg).encode('utf-8')
        filename = req_info['filename']
        image_type = req_info['image_type']
        scale_factor = req_info['scale_factor']
        if image_type == 'svg':
            with open(filename, 'wb') as f:
                f.write(svg_bytes)
        else:
            # We already made sure cairosvg is available in save_image
            cairosvg = import_module('cairosvg')

            if image_type == 'png':
                cairosvg.svg2png(
                    bytestring=svg_bytes, write_to=filename, scale=scale_factor)
            elif image_type == 'pdf':
                cairosvg.svg2pdf(
                    bytestring=svg_bytes, write_to=filename)
            elif image_type == 'ps':
                cairosvg.svg2ps(
                    bytestring=svg_bytes, write_to=filename)

    # ### Python -> JavaScript messages ###
    def _send_relayout_msg(self, layout, source_view_id=None):

        # Update layout edit message id
        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id

        msg_data = {
            'relayout_data': layout,
            'layout_edit_id': layout_edit_id,
            'source_view_id': source_view_id
        }

        self._py2js_relayout = msg_data
        self._py2js_relayout = None

    def _send_restyle_msg(self, style, trace_indexes=None,
                          source_view_id=None):
        if not isinstance(trace_indexes, (list, tuple)):
            trace_indexes = [trace_indexes]

        # Add and update message ids
        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True

        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True

        restyle_msg = {
            'restyle_data': style,
            'restyle_traces': trace_indexes,
            'trace_edit_id': trace_edit_id,
            'layout_edit_id': layout_edit_id,
            'source_view_id': source_view_id,
        }

        self._py2js_restyle = restyle_msg
        self._py2js_restyle = None

    def _send_addTraces_msg(self, new_traces_data):
        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True
        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True
        # Send to front end
        add_traces_msg = {
            'trace_data': new_traces_data,
            'trace_edit_id': trace_edit_id,
            'layout_edit_id': layout_edit_id
        }
        self._py2js_addTraces = add_traces_msg
        self._py2js_addTraces = None

    def _send_moveTraces_msg(self, current_inds, new_inds):
        move_msg = {
            'current_trace_inds': current_inds,
            'new_trace_inds': new_inds
        }
        self._py2js_moveTraces = move_msg
        self._py2js_moveTraces = None

    def _send_update_msg(self,
                         style,
                         layout,
                         trace_indexes=None,
                         source_view_id=None):

        if not isinstance(trace_indexes, (list, tuple)):
            trace_indexes = [trace_indexes]

        # Add restyle message id
        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True

        # Add relayout message id
        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True

        update_msg = {
            'style_data': style,
            'layout_data': layout,
            'style_traces': trace_indexes,
            'trace_edit_id': trace_edit_id,
            'layout_edit_id': layout_edit_id,
            'source_view_id': source_view_id
        }

        self._py2js_update = update_msg
        self._py2js_update = None

    def _send_animate_msg(self, styles, layout, trace_indexes, animation_opts):
        # print(styles, layout, trace_indexes, animation_opts)
        if not isinstance(trace_indexes, (list, tuple)):
            trace_indexes = [trace_indexes]

        # Add restyle message id
        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True

        # Add relayout message id
        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True

        animate_msg = {
            'style_data': styles,
            'layout_data': layout,
            'style_traces': trace_indexes,
            'animation_opts': animation_opts,
            'trace_edit_id': trace_edit_id,
            'layout_edit_id': layout_edit_id,
            'source_view_id': None
        }

        self._py2js_animate = animate_msg
        self._py2js_animate = None

    def _send_deleteTraces_msg(self, delete_inds):
        relayout_msg_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = relayout_msg_id
        self._layout_edit_in_process = True
        for di in reversed(delete_inds):
            # Modify in-place so we don't trigger serialization
            del self._data[di]
        self._py2js_deleteTraces = {
            'delete_inds': delete_inds,
            '_relayout_msg_id ': relayout_msg_id
        }
        self._py2js_deleteTraces = None

    # ### Callbacks ###
    def on_relayout_completed(self, fn):
        if self._layout_edit_in_process:
            self._waiting_relayout_callbacks.append(fn)
        else:
            fn()

    def on_restyle_completed(self, fn):
        if self._trace_edit_in_process:
            self._waiting_restyle_callbacks.append(fn)
        else:
            fn()

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
                delta_transform = BaseFigureWidget._transform_data(
                    uid_trace._prop_defaults, delta)

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

            self._trace_edit_in_process = False
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
        self.plotly_restyle(restyle_data=style_data,
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

        self.plotly_update(restyle_data=style, relayout_data=layout,
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
            delta_transform = BaseFigureWidget._transform_data(
                self._layout_defaults, layout_delta)
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
            self._layout_edit_in_process = False
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

        self.plotly_relayout(relayout_data=relayout_data,
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

    @observe('_js2py_svgResponse')
    def handler_svgResponse(self, change):
        response_data = change['new']
        self._js2py_svgResponse = None

        if not response_data:
            return

        req_id = response_data['request_id']
        svg_uri = response_data['svg_uri']

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

    # Static Helpers
    # --------------
    @staticmethod
    def _remove_overlapping_props(input_data, delta_data, prop_path=()):
        """
        Remove properties in input_data that are also in delta_data, and do so
        recursively.

        Exception: Never remove uid from input_data

        Parameters
        ----------
        input_data : dict|list
        delta_data : dict|list

        Returns
        -------
        list[tuple[str|int]]
            List of removed property path tuples
        """

        # Initialize removed
        # ------------------
        # This is the list of path tuples to the properties that were
        # removed from input_data
        removed = []
        if isinstance(input_data, dict):
            assert isinstance(delta_data, dict)

            for p, delta_val in delta_data.items():
                if isinstance(delta_val,
                              dict) or BaseFigure._is_dict_list(delta_val):
                    if p in input_data:
                        input_val = input_data[p]
                        removed.extend(
                            BaseFigureWidget._remove_overlapping_props(
                                input_val, delta_val, prop_path + (p,)))
                elif p in input_data and p != 'uid':
                    input_data.pop(p)
                    removed.append(prop_path + (p,))

        elif isinstance(input_data, list):
            assert isinstance(delta_data, list)

            for i, delta_val in enumerate(delta_data):
                if i >= len(input_data):
                    break

                input_val = input_data[i]
                if input_val is not None and isinstance(
                        delta_val,
                        dict) or BaseFigure._is_dict_list(delta_val):
                    removed.extend(
                        BaseFigureWidget._remove_overlapping_props(
                            input_val, delta_val, prop_path + (i,)))

        return removed


    @staticmethod
    def _transform_data(to_data,
                        from_data,
                        should_remove=True,
                        relayout_path=()):
        """
        Transform to_data into from_data and return relayout-style
        description of transformation

        Parameters
        ----------
        to_data :
        from_data :

        Returns
        -------

        """
        relayout_terms = {}
        if isinstance(to_data, dict):
            if not isinstance(from_data, dict):
                raise ValueError(
                    'Mismatched data types: to_data: {to_dict} {from_data}'.
                    format(to_dict=to_data, from_data=from_data))

            # Handle addition / modification of terms
            for from_prop, from_val in from_data.items():
                if isinstance(from_val,
                              dict) or BaseFigure._is_dict_list(from_val):
                    if from_prop not in to_data:
                        to_data[from_prop] = {} if isinstance(from_val,
                                                              dict) else []

                    input_val = to_data[from_prop]
                    relayout_terms.update(
                        BaseFigureWidget._transform_data(
                            input_val,
                            from_val,
                            should_remove=should_remove,
                            relayout_path=relayout_path + (from_prop, )))
                else:
                    if from_prop not in to_data or not BasePlotlyType._vals_equal(
                            to_data[from_prop], from_val):
                        # if from_prop in to_data:
                        #     print(f'to_data[from_prop] != from_val -- {to_data}[{from_prop}] != {from_val}:')
                        to_data[from_prop] = from_val
                        relayout_terms[relayout_path
                                       + (from_prop, )] = from_val

            # Handle removal of terms
            if should_remove:
                for remove_prop in set(to_data.keys()).difference(
                        set(from_data.keys())):
                    to_data.pop(remove_prop)

        elif isinstance(to_data, list):
            if not isinstance(from_data, list):
                raise ValueError(
                    'Mismatched data types: to_data: {to_data} {from_data}'.
                    format(to_data=to_data, from_data=from_data))

            for i, from_val in enumerate(from_data):
                if i >= len(to_data):
                    to_data.append(None)

                input_val = to_data[i]
                if input_val is not None and isinstance(
                        from_val,
                        dict) or BaseFigure._is_dict_list(from_val):
                    relayout_terms.update(
                        BaseFigureWidget._transform_data(
                            input_val,
                            from_val,
                            should_remove=should_remove,
                            relayout_path=relayout_path + (i, )))
                else:
                    if not BasePlotlyType._vals_equal(to_data[i], from_val):
                        to_data[i] = from_val
                        relayout_terms[relayout_path + (i, )] = from_val

        return relayout_terms
