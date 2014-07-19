"""
plotly
======

A module that contains the plotly class, a liaison between the user
and ploty's servers.

1. get DEFAULT_PLOT_OPTIONS for options

2. update plot_options with .plotly/ dir

3. update plot_options with _plot_options

4. update plot_options with kwargs!

"""
from __future__ import absolute_import

import json
import warnings
import copy
import os
import six

import requests

from plotly.plotly import chunked_requests
from plotly import utils
from plotly import tools
from plotly import exceptions
from plotly import version


__all__ = ["sign_in", "update_plot_options", "get_plot_options",
           "get_credentials", "iplot", "plot", "iplot_mpl", "plot_mpl",
           "get_figure", "Stream", "image"]

_DEFAULT_PLOT_OPTIONS = dict(
    filename="plot from API",
    fileopt="new",
    world_readable=True,
    auto_open=True,
    validate=True)

_credentials = dict()

_plot_options = dict()

### test file permissions and make sure nothing is corrupted ###
tools.ensure_local_plotly_files()

### _credentials stuff ###


def sign_in(username, api_key):
    """Set module-scoped _credentials for session. Verify with plotly."""
    global _credentials
    _credentials['username'], _credentials['api_key'] = username, api_key
    # TODO: verify these _credentials with plotly


### plot options stuff ###

def update_plot_options(**kwargs):
    """ Update the module-level _plot_options
    """
    global _plot_options
    _plot_options.update(kwargs)


def get_plot_options():
    """ Returns a copy of the user supplied plot options.
    Use `update_plot_options()` to change.
    """
    global _plot_options
    return copy.copy(_plot_options)


def get_credentials():
    """ Returns a copy of the user supplied credentials.
    """
    global _credentials
    if ('username' in _credentials) and ('api_key' in _credentials):
        return copy.copy(_credentials)
    else:
        return tools.get_credentials_file()


### plot stuff ###

def iplot(figure_or_data, **plot_options):
    """Create a unique url for this plot in Plotly and open in IPython.

    plot_options keyword agruments:
    filename (string) -- the name that will be associated with this figure
    fileopt ('new' | 'overwrite' | 'extend' | 'append') -- 'new' creates a
        'new': create a new, unique url for this plot
        'overwrite': overwrite the file associated with `filename` with this
        'extend': add additional numbers (data) to existing traces
        'append': add additional traces to existing data lists
    world_readable (default=True) -- make this figure private/public

    """
    if 'auto_open' not in plot_options:
        plot_options['auto_open'] = False
    res = plot(figure_or_data, **plot_options)
    urlsplit = res.split('/')
    username, plot_id = urlsplit[-2][1:], urlsplit[-1]  # TODO: HACKY!

    embed_options = dict()
    if 'width' in plot_options:
        embed_options['width'] = plot_options['width']
    if 'height' in plot_options:
        embed_options['height'] = plot_options['height']

    return tools.embed(username, plot_id, **embed_options)


def _plot_option_logic(plot_options):
    """Sets plot_options via a precedence hierarchy."""
    options = dict()
    options.update(_DEFAULT_PLOT_OPTIONS)
    options.update(_plot_options)
    options.update(plot_options)
    if ('filename' in plot_options
       and 'fileopt' not in _plot_options
       and 'fileopt' not in plot_options):
        options['fileopt'] = 'overwrite'
    return options


def plot(figure_or_data, validate=True, **plot_options):
    """Create a unique url for this plot in Plotly and optionally open url.

    plot_options keyword agruments:
    filename (string) -- the name that will be associated with this figure
    fileopt ('new' | 'overwrite' | 'extend' | 'append') -- 'new' creates a
        'new': create a new, unique url for this plot
        'overwrite': overwrite the file associated with `filename` with this
        'extend': add additional numbers (data) to existing traces
        'append': add additional traces to existing data lists
    world_readable (default=True) -- make this figure private/public
    auto_open (default=True) -- Toggle browser options
        True: open this plot in a new browser tab
        False: do not open plot in the browser, but do return the unique url

    """
    if isinstance(figure_or_data, dict):
        figure = figure_or_data
    elif isinstance(figure_or_data, list):
        figure = {'data': figure_or_data}
    else:
        raise exceptions.PlotlyError("The `figure_or_data` positional argument "
                                     "must be either `dict`-like or "
                                     "`list`-like.")
    if validate:
        try:
            tools.validate(figure, obj_type='Figure')
        except exceptions.PlotlyError as err:
            raise exceptions.PlotlyError("Invalid 'figure_or_data' argument. "
                                         "Plotly will not be able to properly "
                                         "parse the resulting JSON. If you "
                                         "want to send this 'figure_or_data' "
                                         "to Plotly anyway (not recommended), "
                                         "you can set 'validate=False' as a "
                                         "plot option.\nHere's why you're "
                                         "seeing this error:\n\n{0}"
                                         "".format(err))
    for entry in figure['data']:
        for key, val in list(entry.items()):
            try:
                if len(val) > 40000:
                    msg = ("Woah there! Look at all those points! Due to "
                           "browser limitations, Plotly has a hard time "
                           "graphing more than 500k data points for line "
                           "charts, or 40k points for other types of charts. "
                           "Here are some suggestions:\n"
                           "(1) Trying using the image API to return an image "
                           "instead of a graph URL\n"
                           "(2) Use matplotlib\n"
                           "(3) See if you can create your visualization with "
                           "fewer data points\n\n"
                           "If the visualization you're using aggregates "
                           "points (e.g., box plot, histogram, etc.) you can "
                           "disregard this warning.")
                    warnings.warn(msg)
            except TypeError:
                pass
    plot_options = _plot_option_logic(plot_options)
    res = _send_to_plotly(figure, **plot_options)
    if res['error'] == '':
        if plot_options['auto_open']:
            try:
                from webbrowser import open as wbopen
                wbopen(res['url'])
            except:  # TODO: what should we except here? this is dangerous
                pass
        return res['url']
    else:
        raise exceptions.PlotlyAccountError(res['error'])


def iplot_mpl(fig, resize=True, strip_style=False, update=None, **plot_options):
    """Replot a matplotlib figure with plotly in IPython.

    This function:
    1. converts the mpl figure into JSON (run help(plolty.tools.mpl_to_plotly))
    2. makes a request to Plotly to save this figure in your account
    3. displays the image in your IPython output cell

    Positional agruments:
    fig -- a figure object from matplotlib

    Keyword arguments:
    resize (default=True) -- allow plotly to choose the figure size
    strip_style (default=False) -- allow plotly to choose style options
    update (default=None) -- update the resulting figure with an 'update'
        dictionary-like object resembling a plotly 'Figure' object

    Additional keyword arguments:
    plot_options -- run help(plotly.plotly.iplot)

    """
    fig = tools.mpl_to_plotly(fig, resize=resize, strip_style=strip_style)
    if update and isinstance(update, dict):
        try:
            fig.update(update)
            fig.validate()
        except exceptions.PlotlyGraphObjectError as err:
            err.add_note("Your updated figure could not be properly validated.")
            err.prepare()
            raise
    elif update is not None:
        raise exceptions.PlotlyGraphObjectError(
            "'update' must be dictionary-like and a valid plotly Figure "
            "object. Run 'help(plotly.graph_objs.Figure)' for more info."
        )
    return iplot(fig, **plot_options)


def plot_mpl(fig, resize=True, strip_style=False, update=None, **plot_options):
    """Replot a matplotlib figure with plotly.

    This function:
    1. converts the mpl figure into JSON (run help(plolty.tools.mpl_to_plotly))
    2. makes a request to Plotly to save this figure in your account
    3. opens your figure in a browser tab OR returns the unique figure url

    Positional agruments:
    fig -- a figure object from matplotlib

    Keyword arguments:
    resize (default=True) -- allow plotly to choose the figure size
    strip_style (default=False) -- allow plotly to choose style options
    update (default=None) -- update the resulting figure with an 'update'
        dictionary-like object resembling a plotly 'Figure' object

    Additional keyword arguments:
    plot_options -- run help(plotly.plotly.plot)

    """
    fig = tools.mpl_to_plotly(fig, resize=resize, strip_style=strip_style)
    if update and isinstance(update, dict):
        try:
            fig.update(update)
            fig.validate()
        except exceptions.PlotlyGraphObjectError as err:
            err.add_note("Your updated figure could not be properly validated.")
            err.prepare()
            raise
    elif update is not None:
        raise exceptions.PlotlyGraphObjectError(
            "'update' must be dictionary-like and a valid plotly Figure "
            "object. Run 'help(plotly.graph_objs.Figure)' for more info."
        )
    return plot(fig, **plot_options)


def get_figure(file_owner_or_url, file_id=None, raw=False):
    """Returns a JSON figure representation for the specified file

    Plotly uniquely identifies figures with a 'file_owner'/'file_id' pair.
    Since each file is given a corresponding unique url, you may also simply
    pass a valid plotly url as the first argument.

    Note, if you're using a file_owner string as the first argument, you MUST
    specify a `file_id` keyword argument. Else, if you're using a url string
    as the first argument, you MUST NOT specify a `file_id` keyword argument, or
    file_id must be set to Python's None value.

    Positional arguments:
    file_owner_or_url (string) -- a valid plotly username OR a valid plotly url

    Keyword arguments:
    file_id (default=None) -- an int or string that can be converted to int
                              if you're using a url, don't fill this in!
    raw (default=False) -- if true, return unicode JSON string verbatim**

    **by default, plotly will return a Figure object (run help(plotly
    .graph_objs.Figure)). This representation decodes the keys and values from
    unicode (if possible), removes information irrelevant to the figure
    representation, and converts the JSON dictionary objects to plotly
    `graph objects`.

    """
    plotly_rest_url = tools.get_config_file()['plotly_domain']
    if file_id is None:  # assume we're using a url
        url = file_owner_or_url
        if url[:len(plotly_rest_url)] != plotly_rest_url:
            raise exceptions.PlotlyError(
                "Because you didn't supply a 'file_id' in the call, "
                "we're assuming you're trying to snag a figure from a url. "
                "You supplied the url, '{0}', we expected it to start with "
                "'{1}'."
                "\nRun help on this function for more information."
                "".format(url, plotly_rest_url))
        head = plotly_rest_url + "/~"
        file_owner = url.replace(head, "").split('/')[0]
        file_id = url.replace(head, "").split('/')[1]
    else:
        file_owner = file_owner_or_url
    resource = "/apigetfile/{username}/{file_id}".format(username=file_owner,
                                                         file_id=file_id)
    (username, api_key) = _validation_key_logic()
    headers = {'plotly-username': username,
               'plotly-apikey': api_key,
               'plotly-version': version.__version__,
               'plotly-platform': 'python'}
    try:
        test_if_int = int(file_id)
    except ValueError:
        raise exceptions.PlotlyError(
            "The 'file_id' argument was not able to be converted into an "
            "integer number. Make sure that the positional 'file_id' argument "
            "is a number that can be converted into an integer or a string "
            "that can be converted into an integer."
        )
    if int(file_id) < 0:
        raise exceptions.PlotlyError(
            "The 'file_id' argument must be a non-negative number."
        )
    response = requests.get(plotly_rest_url + resource, headers=headers)
    if response.status_code == 200:
        if six.PY3:
            content = json.loads(response.content.decode('unicode_escape'))
        else:
            content = json.loads(response.content)
        response_payload = content['payload']
        figure = response_payload['figure']
        utils.decode_unicode(figure)
        if raw:
            return figure
        else:
            return tools.get_valid_graph_obj(figure, obj_type='Figure')
    else:
        try:
            content = json.loads(response.content)
            raise exceptions.PlotlyError(content)
        except:
            raise exceptions.PlotlyError(
                "There was an error retrieving this file")


@utils.template_doc(**tools.get_config_file())
class Stream:
    """ Interface to Plotly's real-time graphing API.

    Initialize a Stream object with a stream_id
    found in {plotly_domain}/settings.
    Real-time graphs are initialized with a call to `plot` that embeds
    your unique `stream_id`s in each of the graph's traces. The `Stream`
    interface plots data to these traces, as identified with the unique
    stream_id, in real-time.
    Every viewer of the graph sees the same data at the same time.

    View examples and tutorials here:
    http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/s7_streaming/s7_streaming.ipynb

    Stream example:
    # Initialize a streaming graph
    # by embedding stream_id's in the graph's traces
    >>> stream_id = "your_stream_id" # See {plotly_domain}/settings
    >>> py.plot(Data([Scatter(x=[],
                              y=[],
                              stream=dict(token=stream_id, maxpoints=100))])
    # Stream data to the import trace
    >>> stream = Stream(stream_id) # Initialize a stream object
    >>> stream.open() # Open the stream
    >>> stream.write(dict(x=1, y=1)) # Plot (1, 1) in your graph
    """

    @utils.template_doc(**tools.get_config_file())
    def __init__(self, stream_id):
        """ Initialize a Stream object with your unique stream_id.
        Find your stream_id at {plotly_domain}/settings.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/s7_streaming/s7_streaming.ipynb
        """
        self.stream_id = stream_id
        self.connected = False

    def open(self):
        """Open streaming connection to plotly.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/s7_streaming/s7_streaming.ipynb
        """

        streaming_url = tools.get_config_file()['plotly_streaming_domain']
        self._stream = chunked_requests.Stream(streaming_url,
                                               80,
                                               {'Host': streaming_url,
                                                'plotly-streamtoken': self.stream_id})

    def write(self, trace, layout=None, validate=True,
              reconnect_on=(200, '', 408)):
        """Write to an open stream.

        Once you've instantiated a 'Stream' object with a 'stream_id',
        you can 'write' to it in real time.

        positional arguments:
        trace - A valid plotly trace object (e.g., Scatter, Heatmap, etc.).
                Not all keys in these are `stremable` run help(Obj) on the type
                of trace your trying to stream, for each valid key, if the key
                is streamable, it will say 'streamable = True'. Trace objects
                must be dictionary-like.

        keyword arguments:
        layout (default=None) - A valid Layout object
                                Run help(plotly.graph_objs.Layout)
        validate (default = True) - Validate this stream before sending?
                                    This will catch local errors if set to True.

        Some valid keys for trace dictionaries:
            'x', 'y', 'text', 'z', 'marker', 'line'

        Examples:
        >>> write(dict(x=1, y=2))  # assumes 'scatter' type
        >>> write(Bar(x=[1, 2, 3], y=[10, 20, 30]))
        >>> write(Scatter(x=1, y=2, text='scatter text'))
        >>> write(Scatter(x=1, y=3, marker=Marker(color='blue')))
        >>> write(Heatmap(z=[[1, 2, 3], [4, 5, 6]]))

        The connection to plotly's servers is checked before writing
        and reconnected if disconnected and if the response status code
        is in `reconnect_on`.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/s7_streaming/s7_streaming.ipynb
        """
        stream_object = dict()
        stream_object.update(trace)
        if 'type' not in stream_object:
            stream_object['type'] = 'scatter'
        if validate:
            try:
                tools.validate(stream_object, stream_object['type'])
            except exceptions.PlotlyError as err:
                raise exceptions.PlotlyError(
                    "Part of the data object with type, '{0}', is invalid. "
                    "This will default to 'scatter' if you do not supply a "
                    "'type'. If you do not want to validate your data objects "
                    "when streaming, you can set 'validate=False' in the call "
                    "to 'your_stream.write()'. Here's why the object is "
                    "invalid:\n\n{1}".format(stream_object['type'], err)
                )
            try:
                tools.validate_stream(stream_object, stream_object['type'])
            except exceptions.PlotlyError as err:
                raise exceptions.PlotlyError(
                    "Part of the data object with type, '{0}', cannot yet be "
                    "streamed into Plotly. If you do not want to validate your "
                    "data objects when streaming, you can set 'validate=False' "
                    "in the call to 'your_stream.write()'. Here's why the "
                    "object cannot be streamed:\n\n{1}"
                    "".format(stream_object['type'], err)
                )
            if layout is not None:
                try:
                    tools.validate(layout, 'Layout')
                except exceptions.PlotlyError as err:
                    raise exceptions.PlotlyError(
                        "Your layout kwarg was invalid. "
                        "Here's why:\n\n{0}".format(err)
                    )
        del stream_object['type']

        if layout is not None:
            stream_object.update(dict(layout=layout))

        # TODO: allow string version of this?
        jdata = json.dumps(stream_object, cls=utils._plotlyJSONEncoder)
        jdata += "\n"

        try:
            self._stream.write(jdata, reconnect_on=reconnect_on)
        except AttributeError:
            raise exceptions.PlotlyError("Stream has not been opened yet, "
                                         "cannot write to a closed connection. "
                                         "Call `open()` on the stream to open the stream.")

    def close(self):
        """ Close the stream connection to plotly's streaming servers.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        http://nbviewer.ipython.org/github/plotly/python-user-guide/blob/master/s7_streaming/s7_streaming.ipynb
        """
        try:
            self._stream.close()
        except AttributeError:
            raise exceptions.PlotlyError("Stream has not been opened yet.")


class image:
    ''' Helper functions wrapped around plotly's static image generation api.
    '''

    @staticmethod
    def get(figure_or_data, format='png', width=None, height=None):
        """ Return a static image of the plot described by `figure`.

        Valid formats: 'png', 'svg', 'jpeg', 'pdf'
        """
        if isinstance(figure_or_data, dict):
            figure = figure_or_data
        elif isinstance(figure_or_data, list):
            figure = {'data': figure_or_data}

        if format not in ['png', 'svg', 'jpeg', 'pdf']:
            raise exceptions.PlotlyError("Invalid format. "
                                         "This version of your Plotly-Python "
                                         "package currently only supports "
                                         "png, svg, jpeg, and pdf. "
                                         "Learn more about image exporting, "
                                         "and the currently supported file "
                                         "types here: "
                                         "https://plot.ly/python/static-image-export/")

        (username, api_key) = _validation_key_logic()
        headers = {'plotly-username': username,
                   'plotly-apikey': api_key,
                   'plotly-version': version.__version__,
                   'plotly-platform': 'python'}

        payload = {
            'figure': figure,
            'format': format
        }

        if width is not None:
            payload['width'] = width
        if height is not None:
            payload['height'] = height

        url = tools.get_config_file()['plotly_domain'] + "/apigenimage/"
        res = requests.post(url,
                            data=json.dumps(payload,
                                            cls=utils._plotlyJSONEncoder),
                            headers=headers)

        headers = res.headers

        if res.status_code == 200:
            if ('content-type' in headers and
                headers['content-type'] in ['image/png', 'image/jpeg',
                                            'application/pdf',
                                            'image/svg+xml']):
                return res.content

            elif ('content-type' in headers and
                  'json' in headers['content-type']):
                return_data = json.loads(res.content)
                return return_data['image']
        else:
            try:
                if ('content-type' in headers and
                    'json' in headers['content-type']):
                    return_data = json.loads(res.content)
                else:
                    return_data = {'error': res.content}
            except:
                raise exceptions.PlotlyError("The response "
                                             "from plotly could "
                                             "not be translated.")
            raise exceptions.PlotlyError(return_data['error'])


    @classmethod
    def ishow(cls, figure_or_data, format='png', width=None, height=None):
        """ Display a static image of the plot described by `figure`
        in an IPython Notebook.
        """
        if format == 'pdf':
            raise exceptions.PlotlyError("Aw, snap! "
                "It's not currently possible to embed a pdf into "
                "an IPython notebook. You can save the pdf "
                "with the `image.save_as` or you can "
                "embed an png, jpeg, or svg.")
        img = cls.get(figure_or_data, format, width, height)
        from IPython.display import display, Image, SVG
        if format == 'svg':
            display(SVG(img))
        else:
            display(Image(img))

    @classmethod
    def save_as(cls, figure_or_data, filename, format=None, width=None, height=None):
        """ Save a static image of the plot described by `figure` locally as `filename`.
            Valid image formats are 'png', 'svg', 'jpeg', and 'pdf'.
            The format is taken as the extension of the filename or as the supplied format.
        """
        (base, ext) = os.path.splitext(filename)
        if not ext and not format:
            filename += '.png'
        elif ext and not format:
            format = ext[1:]
        elif not ext and format:
            filename += '.'+format
        else:
            filename += '.'+format

        img = cls.get(figure_or_data, format, width, height)

        f = open(filename, 'wb')
        f.write(img)
        f.close()


def _send_to_plotly(figure, **plot_options):
    """
    """
    fig = tools._replace_newline(figure)  # does not mutate figure
    data = json.dumps(fig['data'] if 'data' in fig else [],
                      cls=utils._plotlyJSONEncoder)
    file_credentials = tools.get_credentials_file()
    if ('username' in _credentials) and ('api_key' in _credentials):
        username, api_key = _credentials['username'], _credentials['api_key']
    elif ('username' in file_credentials) and ('api_key' in file_credentials):
        (username, api_key) = (file_credentials['username'],
                               file_credentials['api_key'])
    else:
        raise exceptions.PlotlyLocalCredentialsError()

    kwargs = json.dumps(dict(filename=plot_options['filename'],
                             fileopt=plot_options['fileopt'],
                             world_readable=plot_options['world_readable'],
                             layout=fig['layout'] if 'layout' in fig
                             else {}),
                        cls=utils._plotlyJSONEncoder)


    payload = dict(platform='python', # TODO: It'd be cool to expose the platform for RaspPi and others
                   version=version.__version__,
                   args=data,
                   un=username,
                   key=api_key,
                   origin='plot',
                   kwargs=kwargs)

    url = tools.get_config_file()['plotly_domain'] + "/clientresp"

    r = requests.post(url, data=payload)
    r.raise_for_status()
    r = json.loads(r.text)
    if 'error' in r and r['error'] != '':
        print((r['error']))
    if 'warning' in r and r['warning'] != '':
        warnings.warn(r['warning'])
    if 'message' in r and r['message'] != '':
        print((r['message']))

    return r


def _validation_key_logic():
    creds_on_file = tools.get_credentials_file()
    if 'username' in _credentials:
        username = _credentials['username']
    elif 'username' in creds_on_file:
        username = creds_on_file['username']
    else:
        username = None
    if 'api_key' in _credentials:
        api_key = _credentials['api_key']
    elif 'api_key' in creds_on_file:
        api_key = creds_on_file['api_key']
    else:
        api_key = None
    if username is None or api_key is None:
        raise exceptions.PlotlyLocalCredentialsError()
    return (username, api_key)
