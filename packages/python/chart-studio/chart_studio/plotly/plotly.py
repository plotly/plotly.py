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

import base64
import copy
import json
import os
import time
import warnings
import webbrowser

import six
import six.moves
import json as _json

import _plotly_utils.utils
import _plotly_utils.exceptions
from _plotly_utils.basevalidators import CompoundValidator, is_array
from _plotly_utils.utils import PlotlyJSONEncoder

from chart_studio import files, session, tools, utils, exceptions
from chart_studio.api import v2
from chart_studio.plotly import chunked_requests
from chart_studio.grid_objs import Grid
from chart_studio.dashboard_objs import dashboard_objs as dashboard

# This is imported like this for backwards compat. Careful if changing.
from chart_studio.config import get_config, get_credentials

__all__ = None

DEFAULT_PLOT_OPTIONS = {
    "world_readable": files.FILE_CONTENT[files.CONFIG_FILE]["world_readable"],
    "auto_open": files.FILE_CONTENT[files.CONFIG_FILE]["auto_open"],
    "validate": True,
    "sharing": files.FILE_CONTENT[files.CONFIG_FILE]["sharing"],
}

SHARING_ERROR_MSG = (
    "Whoops, sharing can only be set to either 'public', 'private', or " "'secret'."
)


# don't break backwards compatibility
def sign_in(username, api_key, **kwargs):
    session.sign_in(username, api_key, **kwargs)
    try:
        # The only way this can succeed is if the user can be authenticated
        # with the given, username, api_key, and plotly_api_domain.
        v2.users.current()
    except exceptions.PlotlyRequestError:
        raise _plotly_utils.exceptions.PlotlyError("Sign in failed.")


update_plot_options = session.update_session_plot_options


def _plot_option_logic(plot_options_from_args):
    """
    Given some plot_options as part of a plot call, decide on final options.
    Precedence:
        1 - Start with DEFAULT_PLOT_OPTIONS
        2 - Update each key with ~/.plotly/.config options (tls.get_config)
        3 - Update each key with session plot options (set by py.sign_in)
        4 - Update each key with plot, iplot call signature options

    """
    default_plot_options = copy.deepcopy(DEFAULT_PLOT_OPTIONS)
    file_options = tools.get_config_file()
    session_options = session.get_session_plot_options()
    plot_options_from_args = copy.deepcopy(plot_options_from_args)

    # Validate options and fill in defaults w world_readable and sharing
    for option_set in [plot_options_from_args, session_options, file_options]:
        utils.validate_world_readable_and_sharing_settings(option_set)
        utils.set_sharing_and_world_readable(option_set)

    user_plot_options = {}
    user_plot_options.update(default_plot_options)
    user_plot_options.update(file_options)
    user_plot_options.update(session_options)
    user_plot_options.update(plot_options_from_args)
    user_plot_options = {
        k: v
        for k, v in user_plot_options.items()
        if k in default_plot_options or k == "filename"
    }

    return user_plot_options


def iplot(figure_or_data, **plot_options):
    """Create a unique url for this plot in Plotly and open in IPython.

    plot_options keyword arguments:
    filename (string) -- the name that will be associated with this figure
    sharing ('public' | 'private' | 'secret') -- Toggle who can view this graph
        - 'public': Anyone can view this graph. It will appear in your profile
                    and can appear in search engines. You do not need to be
                    logged in to Plotly to view this chart.
        - 'private': Only you can view this plot. It will not appear in the
                     Plotly feed, your profile, or search engines. You must be
                     logged in to Plotly to view this graph. You can privately
                     share this graph with other Plotly users in your online
                     Plotly account and they will need to be logged in to
                     view this plot.
        - 'secret': Anyone with this secret link can view this chart. It will
                    not appear in the Plotly feed, your profile, or search
                    engines. If it is embedded inside a webpage or an IPython
                    notebook, anybody who is viewing that page will be able to
                    view the graph. You do not need to be logged in to view
                    this plot.
    world_readable (default=True) -- Deprecated: use "sharing".
                                     Make this figure private/public
    """
    from plotly.basedatatypes import BaseFigure, BaseLayoutType

    if "auto_open" not in plot_options:
        plot_options["auto_open"] = False
    url = plot(figure_or_data, **plot_options)

    if isinstance(figure_or_data, dict):
        layout = figure_or_data.get("layout", {})
        if isinstance(layout, BaseLayoutType):
            layout = layout.to_plotly_json()
    elif isinstance(figure_or_data, BaseFigure):
        layout = figure_or_data.layout.to_plotly_json()
    else:
        layout = {}

    embed_options = dict()
    embed_options["width"] = layout.get("width", "100%")
    embed_options["height"] = layout.get("height", 525)
    try:
        float(embed_options["width"])
    except (ValueError, TypeError):
        pass
    else:
        embed_options["width"] = str(embed_options["width"]) + "px"

    try:
        float(embed_options["height"])
    except (ValueError, TypeError):
        pass
    else:
        embed_options["height"] = str(embed_options["height"]) + "px"

    return tools.embed(url, **embed_options)


def plot(figure_or_data, validate=True, **plot_options):
    """Create a unique url for this plot in Plotly and optionally open url.

    plot_options keyword arguments:
    filename (string) -- the name that will be associated with this figure
    auto_open (default=True) -- Toggle browser options
        True: open this plot in a new browser tab
        False: do not open plot in the browser, but do return the unique url
    sharing ('public' | 'private' | 'secret') -- Toggle who can view this
                                                  graph
        - 'public': Anyone can view this graph. It will appear in your profile
                    and can appear in search engines. You do not need to be
                    logged in to Plotly to view this chart.
        - 'private': Only you can view this plot. It will not appear in the
                     Plotly feed, your profile, or search engines. You must be
                     logged in to Plotly to view this graph. You can privately
                     share this graph with other Plotly users in your online
                     Plotly account and they will need to be logged in to
                     view this plot.
        - 'secret': Anyone with this secret link can view this chart. It will
                    not appear in the Plotly feed, your profile, or search
                    engines. If it is embedded inside a webpage or an IPython
                    notebook, anybody who is viewing that page will be able to
                    view the graph. You do not need to be logged in to view
                    this plot.
    world_readable (default=True) -- Deprecated: use "sharing".
                                     Make this figure private/public

    """
    import plotly.tools

    figure = plotly.tools.return_figure_from_figure_or_data(figure_or_data, validate)
    for entry in figure["data"]:
        if ("type" in entry) and (entry["type"] == "scattergl"):
            continue
        for key, val in list(entry.items()):
            try:
                if len(val) > 40000:
                    msg = (
                        "Woah there! Look at all those points! Due to "
                        "browser limitations, the Plotly SVG drawing "
                        "functions have a hard time "
                        "graphing more than 500k data points for line "
                        "charts, or 40k points for other types of charts. "
                        "Here are some suggestions:\n"
                        "(1) Use the `plotly.graph_objs.Scattergl` "
                        "trace object to generate a WebGl graph.\n"
                        "(2) Trying using the image API to return an image "
                        "instead of a graph URL\n"
                        "(3) Use matplotlib\n"
                        "(4) See if you can create your visualization with "
                        "fewer data points\n\n"
                        "If the visualization you're using aggregates "
                        "points (e.g., box plot, histogram, etc.) you can "
                        "disregard this warning."
                    )
                    warnings.warn(msg)
            except TypeError:
                pass

    plot_options = _plot_option_logic(plot_options)

    # Initialize API payload
    payload = {"figure": figure, "world_readable": True}

    # Process filename
    filename = plot_options.get("filename", None)
    if filename:
        # Strip trailing slash
        if filename[-1] == "/":
            filename = filename[0:-1]

        # split off any parent directory
        paths = filename.split("/")
        parent_path = "/".join(paths[0:-1])
        filename = paths[-1]

        # Create parent directory
        if parent_path:
            file_ops.ensure_dirs(parent_path)
            payload["parent_path"] = parent_path

        payload["filename"] = filename
    else:
        parent_path = ""

    # Process sharing
    sharing = plot_options.get("sharing", None)
    if sharing == "public":
        payload["world_readable"] = True
    elif sharing == "private":
        payload["world_readable"] = False
    elif sharing == "secret":
        payload["world_readable"] = False
        payload["share_key_enabled"] = True
    else:
        raise _plotly_utils.exceptions.PlotlyError(SHARING_ERROR_MSG)

    # Extract grid
    figure, grid = _extract_grid_from_fig_like(figure)

    # Upload grid if anything was extracted
    if len(grid) > 0:
        if not filename:
            grid_filename = None
        elif parent_path:
            grid_filename = parent_path + "/" + filename + "_grid"
        else:
            grid_filename = filename + "_grid"

        grid_ops.upload(
            grid=grid,
            filename=grid_filename,
            world_readable=payload["world_readable"],
            auto_open=False,
        )

        _set_grid_column_references(figure, grid)
        payload["figure"] = figure

    file_info = _create_or_update(payload, "plot")

    # Compute viewing URL
    if sharing == "secret":
        web_url = file_info["web_url"][:-1] + "?share_key=" + file_info["share_key"]
    else:
        web_url = file_info["web_url"]

    # Handle auto_open
    auto_open = plot_options.get("auto_open", None)
    if auto_open:
        _open_url(web_url)

    # Return URL
    return web_url


def iplot_mpl(fig, resize=True, strip_style=False, update=None, **plot_options):
    """Replot a matplotlib figure with plotly in IPython.

    This function:
    1. converts the mpl figure into JSON (run help(plotly.tools.mpl_to_plotly))
    2. makes a request to Plotly to save this figure in your account
    3. displays the image in your IPython output cell

    Positional arguments:
    fig -- a figure object from matplotlib

    Keyword arguments:
    resize (default=True) -- allow plotly to choose the figure size
    strip_style (default=False) -- allow plotly to choose style options
    update (default=None) -- update the resulting figure with an 'update'
        dictionary-like object resembling a plotly 'Figure' object

    Additional keyword arguments:
    plot_options -- run help(plotly.plotly.iplot)

    """
    import plotly.tools

    fig = plotly.tools.mpl_to_plotly(fig, resize=resize, strip_style=strip_style)
    if update and isinstance(update, dict):
        fig.update(update)
    elif update is not None:
        raise _plotly_utils.exceptions.PlotlyGraphObjectError(
            "'update' must be dictionary-like and a valid plotly Figure "
            "object. Run 'help(plotly.graph_objs.Figure)' for more info."
        )
    return iplot(fig, **plot_options)


def plot_mpl(fig, resize=True, strip_style=False, update=None, **plot_options):
    """Replot a matplotlib figure with plotly.

    This function:
    1. converts the mpl figure into JSON (run help(plotly.tools.mpl_to_plotly))
    2. makes a request to Plotly to save this figure in your account
    3. opens your figure in a browser tab OR returns the unique figure url

    Positional arguments:
    fig -- a figure object from matplotlib

    Keyword arguments:
    resize (default=True) -- allow plotly to choose the figure size
    strip_style (default=False) -- allow plotly to choose style options
    update (default=None) -- update the resulting figure with an 'update'
        dictionary-like object resembling a plotly 'Figure' object

    Additional keyword arguments:
    plot_options -- run help(plotly.plotly.plot)

    """
    import plotly.tools

    fig = plotly.tools.mpl_to_plotly(fig, resize=resize, strip_style=strip_style)
    if update and isinstance(update, dict):
        fig.update(update)
    elif update is not None:
        raise _plotly_utils.exceptions.PlotlyGraphObjectError(
            "'update' must be dictionary-like and a valid plotly Figure "
            "object. Run 'help(plotly.graph_objs.Figure)' for more info."
        )
    return plot(fig, **plot_options)


def _swap_keys(obj, key1, key2):
    """Swap obj[key1] with obj[key2]"""
    val1, val2 = None, None
    try:
        val2 = obj.pop(key1)
    except KeyError:
        pass
    try:
        val1 = obj.pop(key2)
    except KeyError:
        pass
    if val2 is not None:
        obj[key2] = val2
    if val1 is not None:
        obj[key1] = val1


def _swap_xy_data(data_obj):
    """Swap x and y data and references"""
    swaps = [
        ("x", "y"),
        ("x0", "y0"),
        ("dx", "dy"),
        ("xbins", "ybins"),
        ("nbinsx", "nbinsy"),
        ("autobinx", "autobiny"),
        ("error_x", "error_y"),
    ]
    for swap in swaps:
        _swap_keys(data_obj, swap[0], swap[1])
    try:
        rows = len(data_obj["z"])
        cols = len(data_obj["z"][0])
        for row in data_obj["z"]:
            if len(row) != cols:
                raise TypeError

        # if we can't do transpose, we hit an exception before here
        z = data_obj.pop("z")
        data_obj["z"] = [[0 for rrr in range(rows)] for ccc in range(cols)]
        for iii in range(rows):
            for jjj in range(cols):
                data_obj["z"][jjj][iii] = z[iii][jjj]
    except (KeyError, TypeError, IndexError) as err:
        warn = False
        try:
            if data_obj["z"] is not None:
                warn = True
            if len(data_obj["z"]) == 0:
                warn = False
        except (KeyError, TypeError):
            pass
        if warn:
            warnings.warn(
                "Data in this file required an 'xy' swap but the 'z' matrix "
                "in one of the data objects could not be transposed. Here's "
                "why:\n\n{}".format(repr(err))
            )


def byteify(input):
    """Convert unicode strings in JSON object to byte strings"""
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode("utf-8")
    else:
        return input


def get_figure(file_owner_or_url, file_id=None, raw=False):
    """Returns a JSON figure representation for the specified file

    Plotly uniquely identifies figures with a 'file_owner'/'file_id' pair.
    Since each file is given a corresponding unique url, you may also simply
    pass a valid plotly url as the first argument.

    Examples:
        fig = get_figure('https://plotly.com/~chris/1638')
        fig = get_figure('chris', 1638)

    Note, if you're using a file_owner string as the first argument, you MUST
    specify a `file_id` keyword argument. Else, if you're using a url string
    as the first argument, you MUST NOT specify a `file_id` keyword argument,
     or file_id must be set to Python's None value.

    Positional arguments:
    file_owner_or_url (string) -- a valid plotly username OR a valid plotly url

    Keyword arguments:
    file_id (default=None) -- an int or string that can be converted to int
                              if you're using a url, don't fill this in!
    raw (default=False) -- if true, return unicode JSON string verbatim**

    **by default, plotly will return a Figure object. This representation used
    to decode the keys and values from unicode (if possible) and remove
    information irrelevant to the figure representation. Now if in Python 2,
    unicode is converted to regular strings. Also irrelevant information is
    now NOT stripped: an error will be raised if a figure contains invalid
    properties.

    Finally this function converts the JSON dictionary objects to plotly
    `graph objects`.

    Run `help(plotly.graph_objs.Figure)` for a list of valid properties.

    """
    import plotly.tools

    plotly_rest_url = get_config()["plotly_domain"]
    if file_id is None:  # assume we're using a url
        url = file_owner_or_url
        if url[: len(plotly_rest_url)] != plotly_rest_url:
            raise _plotly_utils.exceptions.PlotlyError(
                "Because you didn't supply a 'file_id' in the call, "
                "we're assuming you're trying to snag a figure from a url. "
                "You supplied the url, '{0}', we expected it to start with "
                "'{1}'."
                "\nRun help on this function for more information."
                "".format(url, plotly_rest_url)
            )
        head = plotly_rest_url + "/~"
        file_owner = url.replace(head, "").split("/")[0]
        file_id = url.replace(head, "").split("/")[1]
    else:
        file_owner = file_owner_or_url
    try:
        int(file_id)
    except ValueError:
        raise _plotly_utils.exceptions.PlotlyError(
            "The 'file_id' argument was not able to be converted into an "
            "integer number. Make sure that the positional 'file_id' argument "
            "is a number that can be converted into an integer or a string "
            "that can be converted into an integer."
        )
    if int(file_id) < 0:
        raise _plotly_utils.exceptions.PlotlyError(
            "The 'file_id' argument must be a non-negative number."
        )

    fid = "{}:{}".format(file_owner, file_id)
    response = v2.plots.content(fid, inline_data=True)
    figure = response.json()
    if six.PY2:
        figure = byteify(figure)
    # Fix 'histogramx', 'histogramy', and 'bardir' stuff
    for index, entry in enumerate(figure["data"]):
        try:
            # Use xbins to bin data in x, and ybins to bin data in y
            if all(
                (entry["type"] == "histogramy", "xbins" in entry, "ybins" not in entry)
            ):
                entry["ybins"] = entry.pop("xbins")

            # Convert bardir to orientation, and put the data into the axes
            # it's eventually going to be used with
            if entry["type"] in ["histogramx", "histogramy"]:
                entry["type"] = "histogram"
            if "bardir" in entry:
                entry["orientation"] = entry.pop("bardir")
                if entry["type"] == "bar":
                    if entry["orientation"] == "h":
                        _swap_xy_data(entry)
                if entry["type"] == "histogram":
                    if ("x" in entry) and ("y" not in entry):
                        if entry["orientation"] == "h":
                            _swap_xy_data(entry)
                        del entry["orientation"]
                    if ("y" in entry) and ("x" not in entry):
                        if entry["orientation"] == "v":
                            _swap_xy_data(entry)
                        del entry["orientation"]
            figure["data"][index] = entry
        except KeyError:
            pass

    # Remove stream dictionary if found in a data trace
    # (it has private tokens in there we need to hide!)
    for index, entry in enumerate(figure["data"]):
        if "stream" in entry:
            del figure["data"][index]["stream"]

    if raw:
        return figure
    return plotly.tools.get_graph_obj(figure, obj_type="Figure")


@_plotly_utils.utils.template_doc(**tools.get_config_file())
class Stream:
    """
    Interface to Plotly's real-time graphing API.

    NOTE: Streaming is no longer supported in Plotly Cloud.
    Streaming is still available as part of Plotly On-Premises.

    Initialize a Stream object with a stream_id
    found in {plotly_domain}/settings.
    Real-time graphs are initialized with a call to `plot` that embeds
    your unique `stream_id`s in each of the graph's traces. The `Stream`
    interface plots data to these traces, as identified with the unique
    stream_id, in real-time.
    Every viewer of the graph sees the same data at the same time.

    View examples and tutorials here:
    https://plotly.com/python/streaming/

    Stream example:
    # Initialize a streaming graph
    # by embedding stream_id's in the graph's traces
    import plotly.plotly as py
    from plotly.graph_objs import Data, Scatter, Stream
    stream_id = "your_stream_id" # See {plotly_domain}/settings
    py.plot(Data([Scatter(x=[], y=[],
                          stream=Stream(token=stream_id, maxpoints=100))]))
    # Stream data to the import trace
    stream = Stream(stream_id) # Initialize a stream object
    stream.open() # Open the stream
    stream.write(dict(x=1, y=1)) # Plot (1, 1) in your graph

    """

    HTTP_PORT = 80
    HTTPS_PORT = 443

    @_plotly_utils.utils.template_doc(**tools.get_config_file())
    def __init__(self, stream_id):
        """
        Initialize a Stream object with your unique stream_id.
        Find your stream_id at {plotly_domain}/settings.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        https://plotly.com/python/streaming/

        """
        self.stream_id = stream_id
        self._stream = None

    def get_streaming_specs(self):
        """
        Returns the streaming server, port, ssl_enabled flag, and headers.

        """
        streaming_url = get_config()["plotly_streaming_domain"]
        ssl_verification_enabled = get_config()["plotly_ssl_verification"]
        ssl_enabled = "https" in streaming_url
        port = self.HTTPS_PORT if ssl_enabled else self.HTTP_PORT

        # If no scheme (https/https) is included in the streaming_url, the
        # host will be None. Use streaming_url in this case.
        host = six.moves.urllib.parse.urlparse(streaming_url).hostname or streaming_url

        headers = {"Host": host, "plotly-streamtoken": self.stream_id}
        streaming_specs = {
            "server": host,
            "port": port,
            "ssl_enabled": ssl_enabled,
            "ssl_verification_enabled": ssl_verification_enabled,
            "headers": headers,
        }

        return streaming_specs

    def heartbeat(self, reconnect_on=(200, "", 408, 502)):
        """
        Keep stream alive. Streams will close after ~1 min of inactivity.

        If the interval between stream writes is > 30 seconds, you should
        consider adding a heartbeat between your stream.write() calls like so:
        >>> stream.heartbeat()

        """
        try:
            self._stream.write("\n", reconnect_on=reconnect_on)
        except AttributeError:
            raise _plotly_utils.exceptions.PlotlyError(
                "Stream has not been opened yet, "
                "cannot write to a closed connection. "
                "Call `open()` on the stream to open the stream."
            )

    @property
    def connected(self):
        if self._stream is None:
            return False

        return self._stream._isconnected()

    def open(self):
        """
        Open streaming connection to plotly.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        https://plotly.com/python/streaming/

        """
        streaming_specs = self.get_streaming_specs()
        self._stream = chunked_requests.Stream(**streaming_specs)

    def write(self, trace, layout=None, reconnect_on=(200, "", 408, 502)):
        """
        Write to an open stream.

        Once you've instantiated a 'Stream' object with a 'stream_id',
        you can 'write' to it in real time.

        positional arguments:
        trace - A dict of properties to stream
                Some valid keys for trace dictionaries:
                    'x', 'y', 'text', 'z', 'marker', 'line'

        keyword arguments:
        layout (default=None) - A valid Layout object or dict with
                                compatible properties
                                Run help(plotly.graph_objs.Layout)

        Examples:

        Append a point to a scatter trace
        >>> write(dict(x=1, y=2))

        Overwrite the x and y properties of a scatter trace
        >>> write(dict(x=[1, 2, 3], y=[10, 20, 30]))

        Append a point to a scatter trace and set the points text value
        >>> write(dict(x=1, y=2, text='scatter text'))

        Append a point to a scatter trace and set the points color
        >>> write(dict(x=1, y=3, marker=go.Marker(color='blue')))

        Set a new z value array for a Heatmap trace
        >>> write(dict(z=[[1, 2, 3], [4, 5, 6]]))

        The connection to plotly's servers is checked before writing
        and reconnected if disconnected and if the response status code
        is in `reconnect_on`.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:

        """

        # Convert trace objects to dictionaries
        from plotly.basedatatypes import BaseTraceType

        if isinstance(trace, BaseTraceType):
            stream_object = trace.to_plotly_json()
        else:
            stream_object = copy.deepcopy(trace)

        # Remove 'type' if present since this trace type cannot be changed
        stream_object.pop("type", None)

        if layout is not None:
            stream_object.update(dict(layout=layout))

        # TODO: allow string version of this?
        jdata = _json.dumps(stream_object, cls=PlotlyJSONEncoder)
        jdata += "\n"

        try:
            self._stream.write(jdata, reconnect_on=reconnect_on)
        except AttributeError:
            raise _plotly_utils.exceptions.PlotlyError(
                "Stream has not been opened yet, "
                "cannot write to a closed connection. "
                "Call `open()` on the stream to open the stream."
            )

    def close(self):
        """
        Close the stream connection to plotly's streaming servers.

        For more help, see: `help(plotly.plotly.Stream)`
        or see examples and tutorials here:
        https://plotly.com/python/streaming/

        """
        try:
            self._stream.close()
        except AttributeError:
            raise _plotly_utils.exceptions.PlotlyError(
                "Stream has not been opened yet."
            )


class image:
    """
    Helper functions wrapped around plotly's static image generation api.

    """

    @staticmethod
    def get(figure_or_data, format="png", width=None, height=None, scale=None):
        """Return a static image of the plot described by `figure_or_data`.

        positional arguments:
        - figure_or_data: The figure dict-like or data list-like object that
                          describes a plotly figure.
                          Same argument used in `py.plot`, `py.iplot`,
                          see https://plotly.com/python for examples
        - format: 'png', 'svg', 'jpeg', 'pdf', 'emf'
        - width: output width
        - height: output height
        - scale: Increase the resolution of the image by `scale`
                 amount (e.g. `3`)
                 Only valid for PNG and JPEG images.

        example:
        ```
        import plotly.plotly as py
        fig = {'data': [{'x': [1, 2, 3], 'y': [3, 1, 5], 'type': 'bar'}]}
        py.image.get(fig, 'png', scale=3)
        ```

        """
        # TODO: format is a built-in name... we shouldn't really use it
        import plotly.tools

        figure = plotly.tools.return_figure_from_figure_or_data(figure_or_data, True)

        if format not in ["png", "svg", "jpeg", "pdf", "emf"]:
            raise _plotly_utils.exceptions.PlotlyError(
                "Invalid format. This version of your Plotly-Python "
                "package currently only supports png, svg, jpeg, and pdf. "
                "Learn more about image exporting, and the currently "
                "supported file types here: "
                "https://plotly.com/python/static-image-export/"
            )
        if scale is not None:
            try:
                scale = float(scale)
            except:
                raise _plotly_utils.exceptions.PlotlyError(
                    "Invalid scale parameter. Scale must be a number."
                )

        payload = {"figure": figure, "format": format}
        if width is not None:
            payload["width"] = width
        if height is not None:
            payload["height"] = height
        if scale is not None:
            payload["scale"] = scale

        response = v2.images.create(payload)

        headers = response.headers
        if "content-type" in headers and headers["content-type"] in [
            "image/png",
            "image/jpeg",
            "application/pdf",
            "image/svg+xml",
            "image/emf",
        ]:
            return response.content
        elif "content-type" in headers and "json" in headers["content-type"]:
            return response.json()["image"]

    @classmethod
    def ishow(cls, figure_or_data, format="png", width=None, height=None, scale=None):
        """Display a static image of the plot described by `figure_or_data`
        in an IPython Notebook.

        positional arguments:
        - figure_or_data: The figure dict-like or data list-like object that
                          describes a plotly figure.
                          Same argument used in `py.plot`, `py.iplot`,
                          see https://plotly.com/python for examples
        - format: 'png', 'svg', 'jpeg', 'pdf'
        - width: output width
        - height: output height
        - scale: Increase the resolution of the image by `scale` amount
               Only valid for PNG and JPEG images.

        example:
        ```
        import plotly.plotly as py
        fig = {'data': [{'x': [1, 2, 3], 'y': [3, 1, 5], 'type': 'bar'}]}
        py.image.ishow(fig, 'png', scale=3)
        """
        if format == "pdf":
            raise _plotly_utils.exceptions.PlotlyError(
                "Aw, snap! "
                "It's not currently possible to embed a pdf into "
                "an IPython notebook. You can save the pdf "
                "with the `image.save_as` or you can "
                "embed an png, jpeg, or svg."
            )
        img = cls.get(figure_or_data, format, width, height, scale)
        from IPython.display import display, Image, SVG

        if format == "svg":
            display(SVG(img))
        else:
            display(Image(img))

    @classmethod
    def save_as(
        cls, figure_or_data, filename, format=None, width=None, height=None, scale=None
    ):
        """Save a image of the plot described by `figure_or_data` locally as
        `filename`.

        Valid image formats are 'png', 'svg', 'jpeg', 'pdf' and 'emf'.
        The format is taken as the extension of the filename or as the
        supplied format.

        positional arguments:
        - figure_or_data: The figure dict-like or data list-like object that
                          describes a plotly figure.
                          Same argument used in `py.plot`, `py.iplot`,
                          see https://plotly.com/python for examples
        - filename: The filepath to save the image to
        - format: 'png', 'svg', 'jpeg', 'pdf', 'emf'
        - width: output width
        - height: output height
        - scale: Increase the resolution of the image by `scale` amount
               Only valid for PNG and JPEG images.

        example:
        ```
        import plotly.plotly as py
        fig = {'data': [{'x': [1, 2, 3], 'y': [3, 1, 5], 'type': 'bar'}]}
        py.image.save_as(fig, 'my_image.png', scale=3)
        ```
        """
        # todo: format shadows built-in name
        (base, ext) = os.path.splitext(filename)
        if not ext and not format:
            filename += ".png"
        elif ext and not format:
            format = ext[1:]
        elif not ext and format:
            filename += "." + format

        img = cls.get(figure_or_data, format, width, height, scale)

        f = open(filename, "wb")
        f.write(img)
        f.close()


class file_ops:
    """
    Interface to Plotly's File System API

    """

    @classmethod
    def mkdirs(cls, folder_path):
        """
        Create folder(s) specified by folder_path in your Plotly account.

        If the intermediate directories do not exist,
        they will be created. If they already exist,
        no error will be thrown.

        Mimics the shell's mkdir -p.

        Returns:
        - 200 if folders already existed, nothing was created
        - 201 if path was created
        Raises:
        -  exceptions.PlotlyRequestError with status code
           400 if the path already exists.

        Usage:
        >> mkdirs('new folder')
        >> mkdirs('existing folder/new folder')
        >> mkdirs('new/folder/path')

        """
        response = v2.folders.create({"path": folder_path})
        return response.status_code

    @classmethod
    def ensure_dirs(cls, folder_path):
        """
        Create folder(s) if they don't exist, but unlike mkdirs, doesn't
        raise an error if folder path already exist
        """
        try:
            cls.mkdirs(folder_path)
        except exceptions.PlotlyRequestError as e:
            if "already exists" in e.message:
                pass
            else:
                raise e


class grid_ops:
    """
    Interface to Plotly's Grid API.
    Plotly Grids are Plotly's tabular data object, rendered
    in an online spreadsheet. Plotly graphs can be made from
    references of columns of Plotly grid objects. Free-form
    JSON Metadata can be saved with Plotly grids.

    To create a Plotly grid in your Plotly account from Python,
    see `grid_ops.upload`.

    To add rows or columns to an existing Plotly grid, see
    `grid_ops.append_rows` and `grid_ops.append_columns`
    respectively.

    To delete one of your grid objects, see `grid_ops.delete`.

    """

    @classmethod
    def _fill_in_response_column_ids(cls, request_columns, response_columns, grid_id):
        for req_col in request_columns:
            for resp_col in response_columns:
                if resp_col["name"] == req_col.name:
                    req_col.id = "{0}:{1}".format(grid_id, resp_col["uid"])
                    response_columns.remove(resp_col)

    @staticmethod
    def ensure_uploaded(fid):
        if fid:
            return
        raise _plotly_utils.exceptions.PlotlyError(
            "This operation requires that the grid has already been uploaded "
            "to Plotly. Try `uploading` first."
        )

    @classmethod
    def upload(
        cls, grid, filename=None, world_readable=True, auto_open=True, meta=None
    ):
        """
        Upload a grid to your Plotly account with the specified filename.

        Positional arguments:
            - grid: A plotly.grid_objs.Grid object,
                    call `help(plotly.grid_ops.Grid)` for more info.
            - filename: Name of the grid to be saved in your Plotly account.
                        To save a grid in a folder in your Plotly account,
                        separate specify a filename with folders and filename
                        separated by backslashes (`/`).
                        If a grid, plot, or folder already exists with the same
                        filename, a `plotly.exceptions.RequestError` will be
                        thrown with status_code 409.  If filename is None,
                        and randomly generated filename will be used.

        Optional keyword arguments:
            - world_readable (default=True): make this grid publically (True)
                                             or privately (False) viewable.
            - auto_open (default=True): Automatically open this grid in
                                        the browser (True)
            - meta (default=None): Optional Metadata to associate with
                                   this grid.
                                   Metadata is any arbitrary
                                   JSON-encodable object, for example:
                                   `{"experiment name": "GaAs"}`

        Filenames must be unique. To overwrite a grid with the same filename,
        you'll first have to delete the grid with the blocking name. See
        `plotly.plotly.grid_ops.delete`.

        Usage example 1: Upload a plotly grid
        ```
        from plotly.grid_objs import Grid, Column
        import plotly.plotly as py
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([4, 2, 5], 'voltage')
        grid = Grid([column_1, column_2])
        py.grid_ops.upload(grid, 'time vs voltage')
        ```

        Usage example 2: Make a graph based with data that is sourced
                         from a newly uploaded Plotly grid
        ```
        import plotly.plotly as py
        from plotly.grid_objs import Grid, Column
        from plotly.graph_objs import Scatter
        # Upload a grid
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([4, 2, 5], 'voltage')
        grid = Grid([column_1, column_2])
        py.grid_ops.upload(grid, 'time vs voltage')

        # Build a Plotly graph object sourced from the
        # grid's columns
        trace = Scatter(xsrc=grid[0], ysrc=grid[1])
        py.plot([trace], filename='graph from grid')
        ```

        """
        # transmorgify grid object into plotly's format
        grid_json = grid._to_plotly_grid_json()
        if meta is not None:
            grid_json["metadata"] = meta

        payload = {"data": grid_json, "world_readable": world_readable}

        # Make a folder path
        if filename:
            if filename[-1] == "/":
                filename = filename[0:-1]

            paths = filename.split("/")
            parent_path = "/".join(paths[0:-1])
            filename = paths[-1]

            if parent_path != "":
                file_ops.ensure_dirs(parent_path)

            payload["filename"] = filename
            if parent_path:
                payload["parent_path"] = parent_path

        file_info = _create_or_overwrite_grid(payload)

        cols = file_info["cols"]
        fid = file_info["fid"]
        web_url = file_info["web_url"]

        # mutate the grid columns with the id's returned from the server
        cls._fill_in_response_column_ids(grid, cols, fid)

        grid.id = fid

        if meta is not None:
            meta_ops.upload(meta, grid=grid)

        if auto_open:
            _open_url(web_url)

        return web_url

    @classmethod
    def append_columns(cls, columns, grid=None, grid_url=None):
        """
        Append columns to a Plotly grid.

        `columns` is an iterable of plotly.grid_objs.Column objects
        and only one of `grid` and `grid_url` needs to specified.

        `grid` is a ploty.grid_objs.Grid object that has already been
        uploaded to plotly with the grid_ops.upload method.

        `grid_url` is a unique URL of a `grid` in your plotly account.

        Usage example 1: Upload a grid to Plotly, and then append a column
        ```
        from plotly.grid_objs import Grid, Column
        import plotly.plotly as py
        column_1 = Column([1, 2, 3], 'time')
        grid = Grid([column_1])
        py.grid_ops.upload(grid, 'time vs voltage')

        # append a column to the grid
        column_2 = Column([4, 2, 5], 'voltage')
        py.grid_ops.append_columns([column_2], grid=grid)
        ```

        Usage example 2: Append a column to a grid that already exists on
                         Plotly
        ```
        from plotly.grid_objs import Grid, Column
        import plotly.plotly as py

        grid_url = 'https://plotly.com/~chris/3143'
        column_1 = Column([1, 2, 3], 'time')
        py.grid_ops.append_columns([column_1], grid_url=grid_url)
        ```

        """
        grid_id = parse_grid_id_args(grid, grid_url)

        grid_ops.ensure_uploaded(grid_id)

        # Verify unique column names
        column_names = [c.name for c in columns]
        if grid:
            existing_column_names = [c.name for c in grid]
            column_names.extend(existing_column_names)
        duplicate_name = utils.get_first_duplicate(column_names)
        if duplicate_name:
            err = exceptions.NON_UNIQUE_COLUMN_MESSAGE.format(duplicate_name)
            raise exceptions.InputError(err)

        # This is sorta gross, we need to double-encode this.
        body = {"cols": _json.dumps(columns, cls=PlotlyJSONEncoder)}
        fid = grid_id
        response = v2.grids.col_create(fid, body)
        parsed_content = response.json()

        cls._fill_in_response_column_ids(columns, parsed_content["cols"], fid)

        if grid:
            grid.extend(columns)

    @classmethod
    def append_rows(cls, rows, grid=None, grid_url=None):
        """
        Append rows to a Plotly grid.

        `rows` is an iterable of rows, where each row is a
        list of numbers, strings, or dates. The number of items
        in each row must be equal to the number of columns
        in the grid. If appending rows to a grid with columns of
        unequal length, Plotly will fill the columns with shorter
        length with empty strings.

        Only one of `grid` and `grid_url` needs to specified.

        `grid` is a ploty.grid_objs.Grid object that has already been
        uploaded to plotly with the grid_ops.upload method.

        `grid_url` is a unique URL of a `grid` in your plotly account.

        Usage example 1: Upload a grid to Plotly, and then append rows
        ```
        from plotly.grid_objs import Grid, Column
        import plotly.plotly as py
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([5, 2, 7], 'voltage')
        grid = Grid([column_1, column_2])
        py.grid_ops.upload(grid, 'time vs voltage')

        # append a row to the grid
        row = [1, 5]
        py.grid_ops.append_rows([row], grid=grid)
        ```

        Usage example 2: Append a row to a grid that already exists on Plotly
        ```
        from plotly.grid_objs import Grid
        import plotly.plotly as py

        grid_url = 'https://plotly.com/~chris/3143'

        row = [1, 5]
        py.grid_ops.append_rows([row], grid=grid_url)
        ```

        """
        grid_id = parse_grid_id_args(grid, grid_url)

        grid_ops.ensure_uploaded(grid_id)

        if grid:
            n_columns = len([column for column in grid])
            for row_i, row in enumerate(rows):
                if len(row) != n_columns:
                    raise exceptions.InputError(
                        "The number of entries in "
                        "each row needs to equal the number of columns in "
                        "the grid. Row {0} has {1} {2} but your "
                        "grid has {3} {4}. ".format(
                            row_i,
                            len(row),
                            "entry" if len(row) == 1 else "entries",
                            n_columns,
                            "column" if n_columns == 1 else "columns",
                        )
                    )

        fid = grid_id
        v2.grids.row(fid, {"rows": rows})

        if grid:
            longest_column_length = max([len(col.data) for col in grid])

            for column in grid:
                n_empty_rows = longest_column_length - len(column.data)
                empty_string_rows = ["" for _ in range(n_empty_rows)]
                column.data.extend(empty_string_rows)

            column_extensions = zip(*rows)
            for local_column, column_extension in zip(grid, column_extensions):
                local_column.data.extend(column_extension)

    @classmethod
    def delete(cls, grid=None, grid_url=None):
        """
        Delete a grid from your Plotly account.

        Only one of `grid` or `grid_url` needs to be specified.

        `grid` is a plotly.grid_objs.Grid object that has already
               been uploaded to Plotly.

        `grid_url` is the URL of the Plotly grid to delete

        Usage example 1: Upload a grid to plotly, then delete it
        ```
        from plotly.grid_objs import Grid, Column
        import plotly.plotly as py
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([4, 2, 5], 'voltage')
        grid = Grid([column_1, column_2])
        py.grid_ops.upload(grid, 'time vs voltage')

        # now delete it, and free up that filename
        py.grid_ops.delete(grid)
        ```

        Usage example 2: Delete a plotly grid by url
        ```
        import plotly.plotly as py

        grid_url = 'https://plotly.com/~chris/3'
        py.grid_ops.delete(grid_url=grid_url)
        ```

        """
        fid = parse_grid_id_args(grid, grid_url)
        grid_ops.ensure_uploaded(fid)
        v2.grids.trash(fid)
        v2.grids.permanent_delete(fid)


class meta_ops:
    """
    Interface to Plotly's Metadata API.

    In Plotly, Metadata is arbitrary, free-form JSON data that is
    associated with Plotly grids. Metadata is viewable with any grid
    that is shared and grids are searchable by key value pairs in
    the Metadata. Metadata is any JSON-encodable object.

    To upload Metadata, either use the optional keyword argument `meta`
    in the `py.grid_ops.upload` method, or use `py.meta_ops.upload`.

    """

    @classmethod
    def upload(cls, meta, grid=None, grid_url=None):
        """
        Upload Metadata to a Plotly grid.

        Metadata is any JSON-encodable object. For example,
        a dictionary, string, or list.

        Only one of `grid` or `grid_url` needs to be specified.

        `grid` is a plotly.grid_objs.Grid object that has already
               been uploaded to Plotly.

        `grid_url` is the URL of the Plotly grid to attach Metadata to.

        Usage example 1: Upload a grid to Plotly, then attach Metadata to it
        ```
        from plotly.grid_objs import Grid, Column
        import plotly.plotly as py
        column_1 = Column([1, 2, 3], 'time')
        column_2 = Column([4, 2, 5], 'voltage')
        grid = Grid([column_1, column_2])
        py.grid_ops.upload(grid, 'time vs voltage')

        # now attach Metadata to the grid
        meta = {'experment': 'GaAs'}
        py.meta_ops.upload(meta, grid=grid)
        ```

        Usage example 2: Upload Metadata to an existing Plotly grid
        ```
        import plotly.plotly as py

        grid_url = 'https://plotly.com/~chris/3143'

        meta = {'experment': 'GaAs'}

        py.meta_ops.upload(meta, grid_url=grid_Url)
        ```

        """
        fid = parse_grid_id_args(grid, grid_url)
        return v2.grids.update(fid, {"metadata": meta}).json()


def parse_grid_id_args(grid, grid_url):
    """
    Return the grid_id from the non-None input argument.

    Raise an error if more than one argument was supplied.

    """
    if grid is not None:
        id_from_grid = grid.id
    else:
        id_from_grid = None
    args = [id_from_grid, grid_url]
    arg_names = ("grid", "grid_url")

    supplied_arg_names = [
        arg_name for arg_name, arg in zip(arg_names, args) if arg is not None
    ]

    if not supplied_arg_names:
        raise exceptions.InputError(
            "One of the two keyword arguments is required:\n"
            "    `grid` or `grid_url`\n\n"
            "grid: a plotly.graph_objs.Grid object that has already\n"
            "    been uploaded to Plotly.\n\n"
            "grid_url: the url where the grid can be accessed on\n"
            "    Plotly, e.g. 'https://plotly.com/~chris/3043'\n\n"
        )
    elif len(supplied_arg_names) > 1:
        raise exceptions.InputError(
            "Only one of `grid` or `grid_url` is required. \n" "You supplied both. \n"
        )
    else:
        supplied_arg_name = supplied_arg_names.pop()
        if supplied_arg_name == "grid_url":
            path = six.moves.urllib.parse.urlparse(grid_url).path
            file_owner, file_id = path.replace("/~", "").split("/")[0:2]
            return "{0}:{1}".format(file_owner, file_id)
        else:
            return grid.id


def add_share_key_to_url(plot_url, attempt=0):
    """
    Check that share key is enabled and update url to include the secret key

    """
    urlsplit = six.moves.urllib.parse.urlparse(plot_url)
    username = urlsplit.path.split("/")[1].split("~")[1]
    idlocal = urlsplit.path.split("/")[2]
    fid = "{}:{}".format(username, idlocal)
    body = {"share_key_enabled": True, "world_readable": False}
    response = v2.files.update(fid, body)

    # Sometimes a share key is added, but access is still denied.
    # Check that share_key_enabled is set to true and
    # retry if this is not the case
    # https://github.com/plotly/streambed/issues/4089
    time.sleep(4)
    share_key_enabled = v2.files.retrieve(fid).json()["share_key_enabled"]
    if not share_key_enabled:
        attempt += 1
        if attempt == 50:
            raise _plotly_utils.exceptions.PlotlyError(
                "The sharekey could not be enabled at this time so the graph "
                "is saved as private. Try again to save as 'secret' later."
            )
        add_share_key_to_url(plot_url, attempt)

    url_share_key = plot_url + "?share_key=" + response.json()["share_key"]
    return url_share_key


def get_grid(grid_url, raw=False):
    """
    Returns the specified grid as a Grid instance or in JSON/dict form.

    :param (str) grid_url: The web_url which locates a Plotly grid.
    :param (bool) raw: if False, will output a Grid instance of the JSON grid
    being retrieved. If True, raw JSON will be returned.
    """
    fid = parse_grid_id_args(None, grid_url)
    response = v2.grids.content(fid)
    parsed_content = response.json()

    if raw:
        return parsed_content
    return Grid(parsed_content, fid)


def _create_or_update(data, filetype):
    """
    Create or update (if file exists) and plot, spectacle, or dashboard
    object
    Parameters
    ----------
    data: dict
        update/create API payload
    filetype: str
        One of 'plot', 'grid', 'spectacle_presentation', or 'dashboard'
    Returns
    -------
    dict
        File info from API response
    """
    api_module = getattr(v2, filetype + "s")

    # lookup if pre-existing filename already exists
    if "parent_path" in data:
        filename = data["parent_path"] + "/" + data["filename"]
    else:
        filename = data.get("filename", None)

    if filename:
        try:
            lookup_res = v2.files.lookup(filename)
            if isinstance(lookup_res.content, bytes):
                content = lookup_res.content.decode("utf-8")
            else:
                content = lookup_res.content

            matching_file = json.loads(content)

            if matching_file["filetype"] == filetype:
                fid = matching_file["fid"]
                res = api_module.update(fid, data)
            else:
                raise _plotly_utils.exceptions.PlotlyError(
                    """
'{filename}' is already a {other_filetype} in your account. 
While you can overwrite {filetype}s with the same name, you can't overwrite
files with a different type. Try deleting '{filename}' in your account or
changing the filename.""".format(
                        filename=filename,
                        filetype=filetype,
                        other_filetype=matching_file["filetype"],
                    )
                )

        except exceptions.PlotlyRequestError:
            res = api_module.create(data)
    else:
        res = api_module.create(data)

    # Check response
    res.raise_for_status()

    # Get resulting file content
    file_info = res.json()
    file_info = file_info.get("file", file_info)

    return file_info


def _create_or_overwrite_grid(data, max_retries=3):
    """
    Create or overwrite (if file exists) a grid

    Parameters
    ----------
    data: dict
        update/create API payload
    filetype: str
        One of 'plot', 'grid', 'spectacle_presentation', or 'dashboard'

    Returns
    -------
    dict
        File info from API response
    """
    api_module = v2.grids

    # lookup if pre-existing filename already exists
    if "parent_path" in data:
        filename = data["parent_path"] + "/" + data["filename"]
    else:
        filename = data.get("filename", None)

    if filename:
        try:
            lookup_res = v2.files.lookup(filename)
            if isinstance(lookup_res.content, bytes):
                content = lookup_res.content.decode("utf-8")
            else:
                content = lookup_res.content

            matching_file = json.loads(content)

            fid = matching_file["fid"]

            # Delete fid
            # This requires sending file to trash and then deleting it
            res = api_module.destroy(fid)
            res.raise_for_status()

        except exceptions.PlotlyRequestError as e:
            # Raise on trash or permanent delete
            # Pass through to try creating the file anyway
            pass

    # Create file
    try:
        res = api_module.create(data)
    except exceptions.PlotlyRequestError as e:
        if max_retries > 0 and "already exists" in e.message:
            # Retry _create_or_overwrite
            time.sleep(1)
            return _create_or_overwrite_grid(data, max_retries=max_retries - 1)
        else:
            raise

    # Get resulting file content
    res.raise_for_status()
    file_info = res.json()
    file_info = file_info.get("file", file_info)

    return file_info


class dashboard_ops:
    """
    Interface to Plotly's Dashboards API.

    Plotly Dashboards are JSON blobs. They are made up by a bunch of
    containers which contain either empty boxes or boxes with file urls.
    For more info on Dashboard objects themselves, run
    `help(plotly.dashboard_objs)`.

    Example 1: Upload Simple Dashboard
    ```
    import plotly.plotly as py
    import plotly.dashboard_objs as dashboard
    box_1 = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': 'username:123',
        'title': 'box 1'
    }

    box_2 = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': 'username:456',
        'title': 'box 2'
    }

    my_dboard = dashboard.Dashboard()
    my_dboard.insert(box_1)
    # my_dboard.get_preview()
    my_dboard.insert(box_2, 'above', 1)
    # my_dboard.get_preview()

    py.dashboard_ops.upload(my_dboard)
    ```

    Example 2: Retreive Dashboard from Plotly
    ```
    # works if you have at least one dashboard in your files
    import plotly.plotly as py
    import plotly.dashboard_objs as dashboard

    dboard_names = get_dashboard_names()
    first_dboard = get_dashboard(dboard_names[0])

    first_dboard.get_preview()
    ```
    """

    @classmethod
    def upload(cls, dashboard, filename, sharing="public", auto_open=True):
        """
        BETA function for uploading/overwriting dashboards to Plotly.

        :param (dict) dashboard: the JSON dashboard to be uploaded. Use
            plotly.dashboard_objs.dashboard_objs to create a Dashboard
            object.
        :param (str) filename: the name of the dashboard to be saved in
            your Plotly account. Will overwrite a dashboard of the same
            name if it already exists in your files.
        :param (str) sharing: can be set to either 'public', 'private'
            or 'secret'. If 'public', your dashboard will be viewable by
            all other users. If 'private' only you can see your dashboard.
            If 'secret', the url will be returned with a sharekey appended
            to the url. Anyone with the url may view the dashboard.
        :param (bool) auto_open: automatically opens the dashboard in the
            browser.
        """
        if sharing == "public":
            world_readable = True
        elif sharing == "private":
            world_readable = False
        elif sharing == "secret":
            world_readable = False

        data = {
            "content": json.dumps(dashboard),
            "filename": filename,
            "world_readable": world_readable,
        }

        file_info = _create_or_update(data, "dashboard")

        url = file_info["web_url"]

        if sharing == "secret":
            url = add_share_key_to_url(url)

        if auto_open:
            webbrowser.open_new(file_info["web_url"])

        return url

    @classmethod
    def _get_all_dashboards(cls):
        dashboards = []
        res = v2.dashboards.list().json()

        for dashboard in res["results"]:
            if not dashboard["deleted"]:
                dashboards.append(dashboard)
        while res["next"]:
            res = v2.utils.request("get", res["next"]).json()

            for dashboard in res["results"]:
                if not dashboard["deleted"]:
                    dashboards.append(dashboard)
        return dashboards

    @classmethod
    def _get_dashboard_json(cls, dashboard_name, only_content=True):
        dashboards = cls._get_all_dashboards()
        for index, dboard in enumerate(dashboards):
            if dboard["filename"] == dashboard_name:
                break

        dashboard = v2.utils.request(
            "get", dashboards[index]["api_urls"]["dashboards"]
        ).json()
        if only_content:
            dashboard_json = json.loads(dashboard["content"])
            return dashboard_json
        else:
            return dashboard

    @classmethod
    def get_dashboard(cls, dashboard_name):
        """Returns a Dashboard object from a dashboard name."""
        dashboard_json = cls._get_dashboard_json(dashboard_name)
        return dashboard.Dashboard(dashboard_json)

    @classmethod
    def get_dashboard_names(cls):
        """Return list of all active dashboard names from users' account."""
        dashboards = cls._get_all_dashboards()
        return [str(dboard["filename"]) for dboard in dashboards]


class presentation_ops:
    """
    Interface to Plotly's Spectacle-Presentations API.
    """

    @classmethod
    def upload(cls, presentation, filename, sharing="public", auto_open=True):
        """
        Function for uploading presentations to Plotly.

        :param (dict) presentation: the JSON presentation to be uploaded. Use
            plotly.presentation_objs.Presentation to create presentations
            from a Markdown-like string.
        :param (str) filename: the name of the presentation to be saved in
            your Plotly account. Will overwrite a presentation of the same
            name if it already exists in your files.
        :param (str) sharing: can be set to either 'public', 'private'
            or 'secret'. If 'public', your presentation will be viewable by
            all other users. If 'private' only you can see your presentation.
            If it is set to 'secret', the url will be returned with a string
            of random characters appended to the url which is called a
            sharekey. The point of a sharekey is that it makes the url very
            hard to guess, but anyone with the url can view the presentation.
        :param (bool) auto_open: automatically opens the presentation in the
            browser.

        See the documentation online for examples.
        """
        if sharing == "public":
            world_readable = True
        elif sharing in ["private", "secret"]:
            world_readable = False
        else:
            raise _plotly_utils.exceptions.PlotlyError(SHARING_ERROR_MSG)
        data = {
            "content": json.dumps(presentation),
            "filename": filename,
            "world_readable": world_readable,
        }

        file_info = _create_or_update(data, "spectacle_presentation")

        url = file_info["web_url"]

        if sharing == "secret":
            url = add_share_key_to_url(url)

        if auto_open:
            webbrowser.open_new(file_info["web_url"])

        return url


def _extract_grid_graph_obj(obj_dict, reference_obj, grid, path):
    """
    Extract inline data arrays from a graph_obj instance and place them in
    a grid

    Parameters
    ----------
    obj_dict: dict
        dict representing a graph object that may contain inline arrays
    reference_obj: BasePlotlyType
        An empty instance of a `graph_obj` with type corresponding to obj_dict
    grid: Grid
        Grid to extract data arrays too
    path: str
        Path string of the location of `obj_dict` in the figure

    Returns
    -------
    None
        Function modifies obj_dict and grid in-place
    """

    from chart_studio.grid_objs import Column

    for prop in list(obj_dict.keys()):
        propsrc = "{}src".format(prop)
        if propsrc in reference_obj:
            val = obj_dict[prop]
            if is_array(val):
                column = Column(val, path + prop)
                grid.append(column)
                obj_dict[propsrc] = "TBD"
                del obj_dict[prop]

        elif prop in reference_obj:
            prop_validator = reference_obj._validators[prop]
            if isinstance(prop_validator, CompoundValidator):
                # Recurse on compound child
                _extract_grid_graph_obj(
                    obj_dict[prop],
                    reference_obj[prop],
                    grid,
                    "{path}{prop}.".format(path=path, prop=prop),
                )

            # Chart studio doesn't handle links to columns inside object
            # arrays, so we don't extract them for now.  Logic below works
            # and should be reinstated if chart studio gets this capability
            #
            # elif isinstance(prop_validator, CompoundArrayValidator):
            #     # Recurse on elements of object arary
            #     reference_element = prop_validator.validate_coerce([{}])[0]
            #     for i, element_dict in enumerate(obj_dict[prop]):
            #         _extract_grid_graph_obj(
            #             element_dict,
            #             reference_element,
            #             grid,
            #             '{path}{prop}.{i}.'.format(path=path, prop=prop, i=i)
            #         )


def _extract_grid_from_fig_like(fig, grid=None, path=""):
    """
    Extract inline data arrays from a figure and place them in a grid

    Parameters
    ----------
    fig: dict
         A dict representing a figure or a frame
    grid: Grid or None (default None)
        The grid to place the extracted columns in. If None, a new grid will
        be constructed
    path: str (default '')
        Parent path, set to `frames` for use with frame objects
    Returns
    -------
    (dict, Grid)
        * dict: Figure dict with data arrays removed
        * Grid: Grid object containing one column for each removed data array.
                Columns are named with the path the corresponding data array
                (e.g. 'data.0.marker.size')
    """
    from plotly.basedatatypes import BaseFigure
    from plotly.graph_objs import Figure

    if grid is None:
        # If not grid, this is top-level call so deep copy figure
        copy_fig = True
        grid = Grid([])
    else:
        # Grid passed in so this is recursive call, don't copy figure
        copy_fig = False

    if isinstance(fig, BaseFigure):
        fig_dict = fig.to_dict()
    elif isinstance(fig, dict):
        fig_dict = copy.deepcopy(fig) if copy_fig else fig
    else:
        raise ValueError("Invalid figure type {}".format(type(fig)))

    # Process traces
    reference_fig = Figure()
    reference_traces = {}
    for i, trace_dict in enumerate(fig_dict.get("data", [])):
        trace_type = trace_dict.get("type", "scatter")
        if trace_type not in reference_traces:
            reference_traces[trace_type] = reference_fig.add_trace(
                {"type": trace_type}
            ).data[-1]

        reference_trace = reference_traces[trace_type]
        _extract_grid_graph_obj(
            trace_dict, reference_trace, grid, path + "data.{}.".format(i)
        )

    # Process frames
    if "frames" in fig_dict:
        for i, frame_dict in enumerate(fig_dict["frames"]):
            _extract_grid_from_fig_like(frame_dict, grid, "frames.{}.".format(i))

    return fig_dict, grid


def _set_grid_column_references(figure, grid):
    """
    Populate *src columns in a figure from uploaded grid

    Parameters
    ----------
    figure: dict
        Figure dict that previously had inline data arrays extracted
    grid: Grid
        Grid that was created by extracting inline data arrays from figure
        using the _extract_grid_from_fig_like function

    Returns
    -------
    None
        Function modifies figure in-place
    """
    from plotly.basedatatypes import BaseFigure

    for col in grid:
        prop_path = BaseFigure._str_to_dict_path(col.name)
        prop_parent = figure
        for prop in prop_path[:-1]:
            prop_parent = prop_parent[prop]

        prop_parent[prop_path[-1] + "src"] = col.id


def create_animations(figure, filename=None, sharing="public", auto_open=True):
    """
    BETA function that creates plots with animations via `frames`.

    Creates an animated plot using 'frames' alongside 'data' and 'layout'.
    This BETA endpoint is subject to deprecation in the future. In relation
    to `plotly.plotly.plot`, folder-creation and overwriting are not supported
    but creating a plot with or without animations via frames is supported.

    :param (str) filename: if set to 'None', an automatically-generated plot
        name will be created. Does not support folder creation, meaning that
        a folder of the form 'folder/name' will NOT create a the folder and
        place the plot in it.
    :param (str) sharing: see `plotly.plotly.plot()` doc string.
    :param (bool) auto_open: if True, opens plot in the browser. If False,
        returns the url for the plot instead.

    Example 1: Simple Animation
    ```
    import plotly.plotly as py
    from plotly.grid_objs import Grid, Column

    column_1 = Column([0.5], 'x')
    column_2 = Column([0.5], 'y')
    column_3 = Column([1.5], 'x2')
    column_4 = Column([1.5], 'y2')

    grid = Grid([column_1, column_2, column_3, column_4])
    py.grid_ops.upload(grid, 'ping_pong_grid', auto_open=False)

    # create figure
    figure = {
        'data': [
            {
                'xsrc': grid.get_column_reference('x'),
                'ysrc': grid.get_column_reference('y'),
                'mode': 'markers',
            }
        ],
        'layout': {'title': 'Ping Pong Animation',
                   'xaxis': {'range': [0, 2], 'autorange': False},
                   'yaxis': {'range': [0, 2], 'autorange': False},
                   'updatemenus': [{
                       'buttons': [
                           {'args': [None],
                            'label': u'Play',
                            'method': u'animate'}
                   ],
                   'pad': {'r': 10, 't': 87},
                   'showactive': False,
                   'type': 'buttons'
                    }]},
        'frames': [
            {
                'data': [
                    {
                        'xsrc': grid.get_column_reference('x2'),
                        'ysrc': grid.get_column_reference('y2'),
                        'mode': 'markers',
                    }
                ]
            },
            {
                'data': [
                    {
                        'xsrc': grid.get_column_reference('x'),
                        'ysrc': grid.get_column_reference('y'),
                        'mode': 'markers',
                    }
                ]
            }
        ]
    }

    py.create_animations(figure, 'ping_pong')
    ```

    Example 2: Growing Circles Animation
    ```
    import plotly.plotly as py
    from plotly.grid_objs import Grid, Column

    column_1 = Column([0.9, 1.1], 'x')
    column_2 = Column([1.0, 1.0], 'y')
    column_3 = Column([0.8, 1.2], 'x2')
    column_4 = Column([1.2, 0.8], 'y2')
    column_5 = Column([0.7, 1.3], 'x3')
    column_6 = Column([0.7, 1.3], 'y3')
    column_7 = Column([0.6, 1.4], 'x4')
    column_8 = Column([1.5, 0.5], 'y4')
    column_9 = Column([0.4, 1.6], 'x5')
    column_10 = Column([1.2, 0.8], 'y5')

    grid = Grid([column_1, column_2, column_3, column_4, column_5,
                 column_6, column_7, column_8, column_9, column_10])
    py.grid_ops.upload(grid, 'growing_circles_grid', auto_open=False)

    # create figure
    figure = {
        'data': [
            {
                'xsrc': grid.get_column_reference('x'),
                'ysrc': grid.get_column_reference('y'),
                'mode': 'markers',
                'marker': {'color': '#48186a', 'size': 10}
            }
        ],
        'layout': {'title': 'Growing Circles',
                   'xaxis': {'range': [0, 2], 'autorange': False},
                   'yaxis': {'range': [0, 2], 'autorange': False},
                   'updatemenus': [{
                       'buttons': [
                           {'args': [None],
                            'label': u'Play',
                            'method': u'animate'}
                   ],
                   'pad': {'r': 10, 't': 87},
                   'showactive': False,
                   'type': 'buttons'
                    }]},
        'frames': [
            {
                'data': [
                    {
                        'xsrc': grid.get_column_reference('x2'),
                        'ysrc': grid.get_column_reference('y2'),
                        'mode': 'markers',
                        'marker': {'color': '#3b528b', 'size': 25}
                    }
                ]
            },
            {
                'data': [
                    {
                        'xsrc': grid.get_column_reference('x3'),
                        'ysrc': grid.get_column_reference('y3'),
                        'mode': 'markers',
                        'marker': {'color': '#26828e', 'size': 50}
                    }
                ]
            },
            {
                'data': [
                    {
                        'xsrc': grid.get_column_reference('x4'),
                        'ysrc': grid.get_column_reference('y4'),
                        'mode': 'markers',
                        'marker': {'color': '#5ec962', 'size': 80}
                    }
                ]
            },
            {
                'data': [
                    {
                        'xsrc': grid.get_column_reference('x5'),
                        'ysrc': grid.get_column_reference('y5'),
                        'mode': 'markers',
                        'marker': {'color': '#d8e219', 'size': 100}
                    }
                ]
            }
        ]
    }
    py.create_animations(figure, 'growing_circles')
    ```
    """
    # This function is no longer needed since plot now supports figures with
    # frames.  Delegate to this implementation for compatibility
    return plot(figure, filename=filename, sharing=sharing, auto_open=auto_open)


def icreate_animations(figure, filename=None, sharing="public", auto_open=False):
    """
    Create a unique url for this animated plot in Plotly and open in IPython.

    This function is based off `plotly.plotly.iplot`. See `plotly.plotly.
    create_animations` Doc String for param descriptions.
    """
    from plotly.basedatatypes import BaseFigure, BaseLayoutType

    url = create_animations(figure, filename, sharing, auto_open)

    if isinstance(figure, dict):
        layout = figure.get("layout", {})
        if isinstance(layout, BaseLayoutType):
            layout = layout.to_plotly_json()
    elif isinstance(figure, BaseFigure):
        layout = figure.layout.to_plotly_json()
    else:
        layout = {}

    embed_options = dict()
    embed_options["width"] = layout.get("width", "100%")
    embed_options["height"] = layout.get("height", 525)
    try:
        float(embed_options["width"])
    except (ValueError, TypeError):
        pass
    else:
        embed_options["width"] = str(embed_options["width"]) + "px"

    try:
        float(embed_options["height"])
    except (ValueError, TypeError):
        pass
    else:
        embed_options["height"] = str(embed_options["height"]) + "px"

    return tools.embed(url, **embed_options)


def _open_url(url):
    try:
        from webbrowser import open as wbopen

        wbopen(url)
    except:  # TODO: what should we except here? this is dangerous
        pass
