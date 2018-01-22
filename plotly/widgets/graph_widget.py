"""
Module to allow Plotly graphs to interact with IPython widgets.

"""
import uuid
from collections import deque
from pkg_resources import resource_string

from requests.compat import json as _json

# TODO: protected imports?
import ipywidgets as widgets
from traitlets import Unicode
from IPython.display import Javascript, display

import plotly.plotly.plotly as py
from plotly import utils, tools
from plotly.graph_objs import Figure

# Load JS widget code
# No officially recommended way to do this in any other way
# http://mail.scipy.org/pipermail/ipython-dev/2014-April/013835.html
js_widget_code = resource_string('plotly',
                                 'package_data/graphWidget.js').decode('utf-8')

display(Javascript(js_widget_code))

__all__ = None


class GraphWidget(widgets.DOMWidget):
    """An interactive Plotly graph widget for use in IPython
    Notebooks.
    """
    _view_name = Unicode('GraphView', sync=True)
    _view_module = Unicode('graphWidget', sync=True)
    _message = Unicode(sync=True)
    _graph_url = Unicode(sync=True)
    _new_url = Unicode(sync=True)
    _filename = ''
    _flags = {
        'save_pending': False
    }

    # TODO: URL for offline enterprise
    def __init__(self, graph_url='https://plot.ly/~playground/7', **kwargs):
        """Initialize a plotly graph widget

        Args:
            graph_url: The url of a Plotly graph

        Example:
            ```
            GraphWidget('https://plot.ly/~chris/3375')
            ```
        """
        super(GraphWidget, self).__init__(**kwargs)

        # TODO: Validate graph_url
        self._graph_url = graph_url
        self._listener_set = set()
        self._event_handlers = {
            'click': widgets.CallbackDispatcher(),
            'hover': widgets.CallbackDispatcher(),
            'zoom': widgets.CallbackDispatcher()
        }

        self._graphId = ''
        self.on_msg(self._handle_msg)

        # messages to the iframe client need to wait for the
        # iframe to communicate that it is ready
        # unfortunately, this two-way blocking communication
        # isn't possible
        # (https://github.com/ipython/ipython/wiki/IPEP-21:-Widget-Messages#caveats)
        # so we'll just cue up messages until they're ready to be sent
        self._clientMessages = deque()

    @property
    def url(self):
        return self._new_url or ''

    def _handle_msg(self, message):
        """Handle a msg from the front-end.

        Args:
            content (dict): Content of the msg.
        """
        content = message['content']['data']['content']
        if content.get('event', '') == 'pong':
            self._graphId = content['graphId']

            # ready to recieve - pop out all of the items in the deque
            while self._clientMessages:
                _message = self._clientMessages.popleft()
                _message['graphId'] = self._graphId
                _message = _json.dumps(_message)
                self._message = _message

        if content.get('event', '') in ['click', 'hover', 'zoom']:
            # De-nest the message
            if content['event'] == 'click' or content['event'] == 'hover':
                message = content['message']['points']
            elif content['event'] == 'zoom':
                message = content['message']['ranges']

            self._event_handlers[content['event']](self, message)

        if content.get('event', '') == 'getAttributes':
            self._attributes = content.get('response', {})

            # there might be a save pending, use the plotly module to save
            if self._flags['save_pending']:
                self._flags['save_pending'] = False
                url = py.plot(self._attributes, auto_open=False,
                              filename=self._filename, validate=False)
                self._new_url = url
                self._fade_to('slow', 1)

    def _handle_registration(self, event_type, callback, remove):
        self._event_handlers[event_type].register_callback(callback,
                                                           remove=remove)
        event_callbacks = self._event_handlers[event_type].callbacks
        if (len(event_callbacks) and event_type not in self._listener_set):
            self._listener_set.add(event_type)
            message = {'task': 'listen', 'events': list(self._listener_set)}
            self._handle_outgoing_message(message)

    def _handle_outgoing_message(self, message):
        if self._graphId == '':
            self._clientMessages.append(message)
        else:
            message['graphId'] = self._graphId
            message['uid'] = str(uuid.uuid4())
            self._message = _json.dumps(message, cls=utils.PlotlyJSONEncoder)

    def on_click(self, callback, remove=False):
        """ Assign a callback to click events propagated
        by clicking on point(s) in the Plotly graph.

        Args:
            callback (function): Callback function this is called
                on click events with the signature:
                callback(widget, hover_obj) -> None

                Args:
                    widget (GraphWidget): The current instance
                    of the graph widget that this callback is assigned to.

                    click_obj (dict): a nested dict that describes
                    which point(s) were clicked on.

                    click_obj example:
                    [
                        {
                            'curveNumber': 1,
                            'pointNumber': 2,
                            'x': 4,
                            'y': 14
                        }
                    ]

            remove (bool, optional): If False, attach the callback.
                If True, remove the callback. Defaults to False.


        Returns:
            None

        Example:
        ```
        from IPython.display import display
        def message_handler(widget, msg):
            display(widget._graph_url)
            display(msg)

        g = GraphWidget('https://plot.ly/~chris/3375')
        display(g)

        g.on_click(message_handler)
        ```
        """
        self._handle_registration('click', callback, remove)

    def on_hover(self, callback, remove=False):
        """ Assign a callback to hover events propagated
        by hovering over points in the Plotly graph.

        Args:
            callback (function): Callback function this is called
                on hover events with the signature:
                callback(widget, hover_obj) -> None

                Args:
                    widget (GraphWidget): The current instance
                    of the graph widget that this callback is assigned to.

                    hover_obj (dict): a nested dict that describes
                    which point(s) was hovered over.

                    hover_obj example:
                    [
                        {
                                    'curveNumber': 1,
                                    'pointNumber': 2,
                                    'x': 4,
                                    'y': 14
                        }
                    ]

            remove (bool, optional): If False, attach the callback.
                If True, remove the callback. Defaults to False.


        Returns:
            None

        Example:
        ```
        from IPython.display import display
        def message_handler(widget, hover_msg):
            display(widget._graph_url)
            display(hover_msg)

        g = GraphWidget('https://plot.ly/~chris/3375')
        display(g)

        g.on_hover(message_handler)
        ```

        """
        self._handle_registration('hover', callback, remove)

    def on_zoom(self, callback, remove=False):
        """ Assign a callback to zoom events propagated
        by zooming in regions in the Plotly graph.

        Args:
            callback (function): Callback function this is called
                on zoom events with the signature:
                callback(widget, ranges) -> None

                Args:
                    widget (GraphWidget): The current instance
                    of the graph widget that this callback is assigned to.

                    ranges (dict): A description of the
                        region that was zoomed into.

                        ranges example:
                        {
                            'x': [1.8399058038561549, 2.16443359662],
                            'y': [4.640902872777017, 7.855677154582]
                        }

                    remove (bool, optional): If False, attach the callback.
                        If True, remove the callback. Defaults to False.

        Returns:
            None

        Example:
        ```
        from IPython.display import display
        def message_handler(widget, ranges):
            display(widget._graph_url)
            display(ranges)

        g = GraphWidget('https://plot.ly/~chris/3375')
        display(g)

        g.on_zoom(message_handler)
        ```
        """
        self._handle_registration('zoom', callback, remove)

    def plot(self, figure_or_data, validate=True):
        """Plot figure_or_data in the Plotly graph widget.

        Args:
            figure_or_data (dict, list, or plotly.graph_obj object):
                The standard Plotly graph object that describes Plotly
                graphs as used in `plotly.plotly.plot`. See examples
                of the figure_or_data in https://plot.ly/python/

        Returns: None

        Example 1 - Graph a scatter plot:
        ```
        from plotly.graph_objs import Scatter
        g = GraphWidget()
        g.plot([Scatter(x=[1, 2, 3], y=[10, 15, 13])])
        ```

        Example 2 - Graph a scatter plot with a title:
        ```
        from plotly.graph_objs import Scatter, Figure, Data
        fig = Figure(
            data = Data([
                Scatter(x=[1, 2, 3], y=[20, 15, 13])
            ]),
            layout = Layout(title='Experimental Data')
        )

        g = GraphWidget()
        g.plot(fig)
        ```

        Example 3 - Clear a graph widget
        ```
        from plotly.graph_objs import Scatter, Figure
        g = GraphWidget()
        g.plot([Scatter(x=[1, 2, 3], y=[10, 15, 13])])

        # Now clear it
        g.plot({}) # alternatively, g.plot(Figure())
        ```
        """
        if figure_or_data == {} or figure_or_data == Figure():
            validate = False

        figure = tools.return_figure_from_figure_or_data(figure_or_data,
                                                         validate)
        message = {
            'task': 'newPlot',
            'data': figure.get('data', []),
            'layout': figure.get('layout', {}),
            'graphId': self._graphId
        }
        self._handle_outgoing_message(message)

    def restyle(self, update, indices=None):
        """Update the style of existing traces in the Plotly graph.

        Args:
            update (dict):
                dict where keys are the graph attribute strings
                and values are the value of the graph attribute.

                To update graph objects that are nested, like
                a marker's color, combine the keys with a period,
                e.g. `marker.color`. To replace an entire nested object,
                like `marker`, set the value to the object.
                See Example 2 below.

                To update an attribute of multiple traces, set the
                value to an list of values. If the list is shorter
                than the number of traces, the values will wrap around.
                Note: this means that for values that are naturally an array,
                like `x` or `colorscale`, you need to wrap the value
                in an extra array,
                i.e. {'colorscale': [[[0, 'red'], [1, 'green']]]}

                You can also supply values to different traces with the
                indices argument.

                See all of the graph attributes in our reference documentation
                here: https://plot.ly/python/reference or by calling `help` on
                graph objects in `plotly.graph_objs`.

            indices (list, optional):
                Specify which traces to apply the update dict to.
                Negative indices are supported.
                If indices are not given, the update will apply to
                *all* traces.

        Examples:
            Initialization - Start each example below with this setup:
            ```
            from plotly.widgets import GraphWidget
            from IPython.display import display

            graph = GraphWidget()
            display(graph)
            ```

            Example 1 - Set `marker.color` to red in every trace in the graph
            ```
            graph.restyle({'marker.color': 'red'})
            ```

            Example 2 - Replace `marker` with {'color': 'red'}
            ```
            graph.restyle({'marker': {'color': red'}})
            ```

            Example 3 - Set `marker.color` to red
                        in the first trace of the graph
            ```
            graph.restyle({'marker.color': 'red'}, indices=[0])
            ```

            Example 4 - Set `marker.color` of all of the traces to
                alternating sequences of red and green
            ```
            graph.restyle({'marker.color': ['red', 'green']})
            ```

            Example 5 - Set just `marker.color` of the first two traces
                        to red and green
            ```
            graph.restyle({'marker.color': ['red', 'green']}, indices=[0, 1])
            ```

            Example 6 - Set multiple attributes of all of the traces
            ```
            graph.restyle({
                'marker.color': 'red',
                'line.color': 'green'
            })
            ```

            Example 7 - Update the data of the first trace
            ```
            graph.restyle({
                'x': [[1, 2, 3]],
                'y': [[10, 20, 30]],
            }, indices=[0])
            ```

            Example 8 - Update the data of the first two traces
            ```
            graph.restyle({
                'x': [[1, 2, 3],
                      [1, 2, 4]],
                'y': [[10, 20, 30],
                      [5, 8, 14]],
            }, indices=[0, 1])
            ```
        """
        # TODO: Add flat traces to graph_objs
        message = {
            'task': 'restyle',
            'update': update,
            'graphId': self._graphId
        }
        if indices:
            message['indices'] = indices
        self._handle_outgoing_message(message)

    def relayout(self, layout):
        """Update the layout of the Plotly graph.

        Args:
            layout (dict):
                dict where keys are the graph attribute strings
                and values are the value of the graph attribute.

                To update graph objects that are nested, like
                the title of an axis, combine the keys with a period
                e.g. `xaxis.title`. To set a value of an element in an array,
                like an axis's range, use brackets, e.g. 'xaxis.range[0]'.
                To replace an entire nested object, just specify the value to
                the sub-object. See example 4 below.

                See all of the layout attributes in our reference documentation
                https://plot.ly/python/reference/#Layout
                Or by calling `help` on `plotly.graph_objs.Layout`

        Examples - Start each example below with this setup:
            Initialization:
            ```
            from plotly.widgets import GraphWidget
            from IPython.display import display

            graph = GraphWidget('https://plot.ly/~chris/3979')
            display(graph)
            ```

            Example 1 - Update the title
            ```
            graph.relayout({'title': 'Experimental results'})
            ```

            Example 2 - Update the xaxis range
            ```
            graph.relayout({'xaxis.range': [-1, 6]})
            ```

            Example 3 - Update the first element of the xaxis range
            ```
            graph.relayout({'xaxis.range[0]': -3})
            ```

            Example 4 - Replace the entire xaxis object
            ```
            graph.relayout({'xaxis': {'title': 'Experimental results'}})
            ```
        """
        # TODO: Add flat layout to graph_objs
        message = {
            'task': 'relayout', 'update': layout, 'graphId': self._graphId
        }
        self._handle_outgoing_message(message)

    def hover(self, *hover_objs):
        """Show hover labels over the points specified in hover_obj.

        Hover labels are the labels that normally appear when the
        mouse hovers over points in the plotly graph.

        Args:
            hover_objs (tuple of dicts):
                Specifies which points to place hover labels over.

                The location of the hover labels is described by a dict with
                keys and'xval' and/or 'yval' or 'curveNumber' and 'pointNumber'
                and optional keys 'hovermode' and 'subplot'

                'xval' and 'yval' specify the (x, y) coordinates to
                place the label.
                'xval' and 'yval need to be close to a point drawn in a graph.

                'curveNumber' and 'pointNumber' specify the trace number and
                the index theof the point in that trace respectively.

                'subplot' describes which axes to the coordinates refer to.
                By default, it is equal to 'xy'. For example, to specify the
                second x-axis and the third y-axis, set 'subplot' to 'x2y3'

                'hovermode' is either 'closest', 'x', or 'y'.
                When set to 'x', all data sharing the same 'x' coordinate will
                be shown on screen with corresponding trace labels.
                When set to 'y' all data sharing the same 'y' coordinates will
                be shown on the screen with corresponding trace labels.
                When set to 'closest', information about the data point closest
                to where the viewer is hovering will appear.

                Note: If 'hovermode' is 'x', only 'xval' needs to be set.
                      If 'hovermode' is 'y', only 'yval' needs to be set.
                      If 'hovermode' is 'closest', 'xval' and 'yval' both
                      need to be set.

                Note: 'hovermode' can be toggled by the user in the graph
                      toolbar.

                Note: It is not currently possible to apply multiple hover
                      labels to points on different axes.

                Note: `hover` can only be called with multiple dicts if
                      'curveNumber' and 'pointNumber' are the keys of the dicts

        Examples:
            Initialization - Start each example below with this setup:
            ```
            from plotly.widgets import GraphWidget
            from IPython.display import display

            graph = GraphWidget('https://plot.ly/~chris/3979')
            display(graph)
            ```

            Example 1 - Apply a label to the (x, y) point (3, 2)
            ```
            graph.hover({'xval': 3, 'yval': 2, 'hovermode': 'closest'})
            ```

            Example 2 -Apply a labels to all the points with the x coordinate 3
            ```
            graph.hover({'xval': 3, 'hovermode': 'x'})
            ```

            Example 3 - Apply a label to the first point of the first trace
                        and the second point of the second trace.
            ```
            graph.hover({'curveNumber': 0, 'pointNumber': 0},
                        {'curveNumber': 1, 'pointNumber': 1})
            ```
        """
        # TODO: Add to graph objects

        if len(hover_objs) == 1:
            hover_objs = hover_objs[0]

        message = {
            'task': 'hover', 'selection': hover_objs, 'graphId': self._graphId
        }

        self._handle_outgoing_message(message)

    def add_traces(self, traces, new_indices=None):
        """ Add new data traces to a graph.

        If `new_indices` isn't specified, they are simply appended.

        Args:
            traces (dict or list of dicts, or class of plotly.graph_objs):trace
            new_indices (list[int]|None), optional: The final indices the
                added traces should occupy in the graph.

        Examples:
            Initialization - Start each example below with this setup:
            ```
            from plotly.widgets import GraphWidget
            from plotly.graph_objs import Scatter
            from IPython.display import display

            graph = GraphWidget('https://plot.ly/~chris/3979')
            display(graph)
            ```

            Example 1 - Add a scatter/line trace to the graph
            ```
            graph.add_traces(Scatter(x = [1, 2, 3], y = [5, 4, 5]))
            ```

            Example 2 - Add a scatter trace and set it to to be the
                        second trace. This will appear as the second
                        item in the legend.
            ```
            graph.add_traces(Scatter(x = [1, 2, 3], y = [5, 6, 5]),
                             new_indices=[1])
            ```

            Example 3 - Add multiple traces to the graph
            ```
            graph.add_traces([
                Scatter(x = [1, 2, 3], y = [5, 6, 5]),
                Scatter(x = [1, 2.5, 3], y = [5, 8, 5])
            ])
            ```
        """
        # TODO: Validate traces with graph_objs
        message = {
            'task': 'addTraces', 'traces': traces, 'graphId': self._graphId
        }
        if new_indices is not None:
            message['newIndices'] = new_indices
        self._handle_outgoing_message(message)

    def delete_traces(self, indices):
        """Delete data traces from a graph.

        Args:
            indices (list[int]): The indices of the traces to be removed

        Example - Delete the 2nd trace:
            ```
            from plotly.widgets import GraphWidget
            from IPython.display import display

            graph = GraphWidget('https://plot.ly/~chris/3979')
            display(graph)


            graph.delete_traces([1])
            ```

        """
        message = {
            'task': 'deleteTraces',
            'indices': indices,
            'graphId': self._graphId
        }
        self._handle_outgoing_message(message)

    def reorder_traces(self, current_indices, new_indices=None):
        """Reorder the traces in a graph.

        The order of the traces determines the order of the legend entries
        and the layering of the objects drawn in the graph, i.e. the first
        trace is drawn first and the second trace is drawn on top of the
        first trace.

        Args:
            current_indices (list[int]): The index of the traces to reorder.

            new_indices (list[int], optional): The index of the traces
                specified by `current_indices` after ordering.
                If None, then move the traces to the end.

        Examples:
            Example 1 - Move the first trace to the second to last
                position, the second trace to the last position
            ```
            graph.move_traces([0, 1])
            ```

            Example 2 - Move the first trace to the second position,
                the second trace to the first position.
            ```
            graph.move_traces([0], [1])
            ```
        """

        message = {
            'task': 'moveTraces',
            'currentIndices': current_indices,
            'graphId': self._graphId
        }
        if new_indices is not None:
            message['newIndices'] = new_indices
        self._handle_outgoing_message(message)

    def save(self, ignore_defaults=False, filename=''):
        """
        Save a copy of the current state of the widget in plotly.

        :param (bool) ignore_defaults: Auto-fill in unspecified figure keys?
        :param (str) filename: Name of the file on plotly.

        """
        self._flags['save_pending'] = True
        self._filename = filename
        message = {'task': 'getAttributes', 'ignoreDefaults': ignore_defaults}
        self._handle_outgoing_message(message)
        self._fade_to('slow', 0.1)

    def extend_traces(self, update, indices=(0,), max_points=None):
        """ Append data points to existing traces in the Plotly graph.

        Args:
            update (dict):
                dict where keys are the graph attribute strings
                and values are arrays of arrays with values to extend.

                Each array in the array will extend a trace.

                Valid keys include:
                    'x', 'y', 'text,
                    'marker.color', 'marker.size', 'marker.symbol',
                    'marker.line.color', 'marker.line.width'

            indices (list, int):
                Specify which traces to apply the `update` dict to.
                If indices are not given, the update will apply to
                the traces in order.

            max_points (int or dict, optional):
                If specified, then only show the `max_points` most
                recent points in the graph.
                This is useful to prevent traces from becoming too
                large (and slow) or for creating "windowed" graphs
                in monitoring applications.

                To set max_points to different values for each trace
                or attribute, set max_points to a dict mapping keys
                to max_points values. See the examples below.

            Examples:
                Initialization - Start each example below with this setup:
                ```
                from plotly.widgets import GraphWidget
                from IPython.display import display

                graph = GraphWidget()
                graph.plot([
                    {'x': [], 'y': []},
                    {'x': [], 'y': []}
                ])

                display(graph)
                ```

                Example 1 - Extend the first trace with x and y data
                ```
                graph.extend_traces({'x': [[1, 2, 3]], 'y': [[10, 20, 30]]},
                                    indices=[0])
                ```

                Example 2 - Extend the second trace with x and y data
                ```
                graph.extend_traces({'x': [[1, 2, 3]], 'y': [[10, 20, 30]]},
                                    indices=[1])
                ```

                Example 3 - Extend the first two traces with x and y data
                ```
                graph.extend_traces({
                    'x': [[1, 2, 3], [2, 3, 4]],
                    'y': [[10, 20, 30], [3, 4, 3]]
                }, indices=[0, 1])
                ```

                Example 4 - Extend the first trace with x and y data and
                            limit the length of data in that trace to 50
                            points.
                ```

                graph.extend_traces({
                    'x': [range(100)],
                    'y': [range(100)]
                }, indices=[0, 1], max_points=50)
                ```

                Example 5 - Extend the first and second trace with x and y data
                            and limit the length of data in the first trace to
                            25 points and the second trace to 50 points.
                ```
                new_points = range(100)
                graph.extend_traces({
                        'x': [new_points, new_points],
                        'y': [new_points, new_points]
                    },
                    indices=[0, 1],
                    max_points={
                        'x': [25, 50],
                        'y': [25, 50]
                    }
                )
                ```

                Example 6 - Update other attributes, like marker colors and
                            sizes and text
                ```
                # Initialize a plot with some empty attributes
                graph.plot([{
                    'x': [],
                    'y': [],
                    'text': [],
                    'marker': {
                        'size': [],
                        'color': []
                    }
                }])
                # Append some data into those attributes
                graph.extend_traces({
                    'x': [[1, 2, 3]],
                    'y': [[10, 20, 30]],
                    'text': [['A', 'B', 'C']],
                    'marker.size': [[10, 15, 20]],
                    'marker.color': [['blue', 'red', 'orange']]
                }, indices=[0])
                ```

                Example 7 - Live-update a graph over a few seconds
                ```
                import time

                graph.plot([{'x': [], 'y': []}])
                for i in range(10):
                    graph.extend_traces({
                        'x': [[i]],
                        'y': [[i]]
                    }, indices=[0])

                    time.sleep(0.5)
                ```

        """
        message = {
            'task': 'extendTraces',
            'update': update,
            'graphId': self._graphId,
            'indices': indices
        }
        if max_points is not None:
            message['maxPoints'] = max_points
        self._handle_outgoing_message(message)

    def _fade_to(self, duration, opacity):
        """
        Change the opacity to give a visual signal to users.

        """
        message = {'fadeTo': True, 'duration': duration, 'opacity': opacity}
        self._handle_outgoing_message(message)
