from collections import deque
import json
import os
import uuid

# TODO: protected imports?
from IPython.html import widgets
from IPython.utils.traitlets import Unicode
from IPython.display import Javascript, display

import plotly

# Load JS widget code
# No officially recommended way to do this in any other way
# http://mail.scipy.org/pipermail/ipython-dev/2014-April/013835.html
directory = os.path.dirname(os.path.realpath(__file__))
js_widget_file = os.path.join(directory, 'graphWidget.js')
with open(js_widget_file) as f:
    js_widget_code = f.read()

display(Javascript(js_widget_code))

__all__ = None


class Graph(widgets.DOMWidget):
    """An interactive Plotly graph widget for use in IPython
    Notebooks.
    """
    _view_name = Unicode('GraphView', sync=True)
    _message = Unicode(sync=True)
    _graph_url = Unicode(sync=True)
    _plotly_domain = Unicode(
        sync=True, default_value=plotly.plotly.get_config()['plotly_domain']
    )

    def __init__(self, graph_url, **kwargs):
        """Initialize a plotly graph object.
        Parameters
        ----------
        graph_url: The url of a Plotly graph

        Examples
        --------
        GraphWidget('https://plot.ly/~chris/3375')
        """
        super(Graph, self).__init__(**kwargs)

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
        # isn't possible (https://github.com/ipython/ipython/wiki/IPEP-21:-Widget-Messages#caveats)
        # so we'll just cue up messages until they're ready to be sent
        self._clientMessages = deque()

    def _handle_msg(self, message):
        """Handle a msg from the front-end.
        Parameters
        ----------
        content: dict
            Content of the msg."""
        content = message['content']['data']['content']
        if content.get('event', '') == 'pong':
            self._graphId = content['graphId']

            # ready to recieve - pop out all of the items in the deque
            while self._clientMessages:
                _message = self._clientMessages.popleft()
                _message['graphId'] = self._graphId
                _message = json.dumps(_message)
                self._message = _message

        if content.get('event', '') in ['click', 'hover', 'zoom']:
            self._event_handlers[content['event']](self, content)

    def _handle_registration(self, event_type, callback, remove):
        self._event_handlers[event_type].register_callback(callback,
                                                           remove=remove)
        event_callbacks = self._event_handlers[event_type].callbacks
        if (len(event_callbacks) and event_type not in self._listener_set):
            self._listener_set.add(event_type)
            message = {'task': 'listen', 'events': list(self._listener_set)}
            self._handle_outgoing_message(message)

    def _handle_outgoing_message(self, message):
        message['plotlyDomain'] = self._plotly_domain
        if self._graphId == '':
            self._clientMessages.append(message)
        else:
            message['graphId'] = self._graphId
            message['uid'] = str(uuid.uuid4())
            self._message = json.dumps(message)

    def on_click(self, callback, remove=False):
        """Register a callback to execute when the graph is clicked.
        Parameters
        ----------
        remove : bool (optional)
            Set to true to remove the callback from the list of callbacks."""
        self._handle_registration('click', callback, remove)

    def on_hover(self, callback, remove=False):
        """Register a callback to execute when you hover over points in the graph.
        Parameters
        ----------
        remove : bool (optional)
            Set to true to remove the callback from the list of callbacks."""
        self._handle_registration('hover', callback, remove)

    def on_zoom(self, callback, remove=False):
        """Register a callback to execute when you zoom in the graph.
        Parameters
        ----------
        remove : bool (optional)
            Set to true to remove the callback from the list of callbacks."""
        self._handle_registration('zoom', callback, remove)

    def restyle(self, data, indices=None):
        message = {'task': 'restyle', 'update': data, 'graphId': self._graphId}
        if indices:
            message['indices'] = indices
        self._handle_outgoing_message(message)

    def relayout(self, layout):
        message = {
            'task': 'relayout', 'update': layout, 'graphId': self._graphId
        }
        self._handle_outgoing_message(message)

    def hover(self, hover_obj, subplot=None):
        message = {
            'task': 'hover', 'selection': hover_obj, 'graphId': self._graphId
        }
        if subplot is not None:
            message['subplot'] = subplot
        self._handle_outgoing_message(message)

    def add_traces(self, traces, new_indices=None):
        """
        Add new data traces to a graph.

        If `new_indices` isn't specified, they are simply appended.

        :param (list[dict]) traces: The list of trace dicts
        :param (list[int]|None|optional) new_indices: The final indices the
            added traces should occupy.

        """
        message = {
            'task': 'addTraces', 'traces': traces, 'graphId': self._graphId
        }
        if new_indices is not None:
            message['newIndices'] = new_indices
        self._handle_outgoing_message(message)

    def delete_traces(self, indices):
        """
        Delete data traces from a graph.

        :param (list[int]) indices: The indices of the traces to be removed

        """
        message = {
            'task': 'deleteTraces',
            'indices': indices,
            'graphId': self._graphId
        }
        self._handle_outgoing_message(message)

    def move_traces(self, current_indices, new_indices=None):
        """
        Move data traces around in a graph.

        If new_indices isn't specified, the traces at the locations specified
        in current_indices are moved to the end of the data array.

        :param (list[int]) current_indices: The initial indices the traces to
        be moved occupy.
        :param (list[int]|None|optional) new_indices: The final indices the
            traces to be moved will occupy.

        """
        message = {
            'task': 'moveTraces',
            'currentIndices': current_indices,
            'graphId': self._graphId
            }
        if new_indices is not None:
            message['newIndices'] = new_indices
        self._handle_outgoing_message(message)
