# -*- coding: utf-8 -*-

"""
tools
=====

Functions that USERS will possibly want access to.

"""
from __future__ import absolute_import

import os
import os.path
import warnings
import six
import requests

from plotly import utils
from plotly import exceptions

from plotly.graph_objs import graph_objs

# Warning format
def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
    return '%s:%s: %s:\n\n%s\n\n' % (filename, lineno, category.__name__, message)
warnings.formatwarning = warning_on_one_line

try:
    from . import matplotlylib
    _matplotlylib_imported = True
except ImportError:
    _matplotlylib_imported = False

try:
    import IPython
    import IPython.core.display
    _ipython_imported = True
except ImportError:
    _ipython_imported = False

PLOTLY_DIR = os.path.join(os.path.expanduser("~"), ".plotly")
CREDENTIALS_FILE = os.path.join(PLOTLY_DIR, ".credentials")
CONFIG_FILE = os.path.join(PLOTLY_DIR, ".config")
TEST_DIR = os.path.join(os.path.expanduser("~"), ".test")
TEST_FILE = os.path.join(PLOTLY_DIR, ".permission_test")

# this sets both the DEFAULTS and the TYPES for these items
_FILE_CONTENT = {CREDENTIALS_FILE: {'username': '',
                                    'api_key': '',
                                    'stream_ids': []},
                 CONFIG_FILE: {'plotly_domain': 'https://plot.ly',
                               'plotly_streaming_domain': 'stream.plot.ly',
                               'plotly_api_domain': 'https://api.plot.ly',
                               'plotly_ssl_verification': True}}

try:
    os.mkdir(TEST_DIR)
    os.rmdir(TEST_DIR)
    if not os.path.exists(PLOTLY_DIR):
        os.mkdir(PLOTLY_DIR)
    f = open(TEST_FILE, 'w')
    f.write('testing\n')
    f.close()
    os.remove(TEST_FILE)
    _file_permissions = True
except:
    _file_permissions = False


def check_file_permissions():
    return _file_permissions


def ensure_local_plotly_files():
    """Ensure that filesystem is setup/filled out in a valid way"""
    if _file_permissions:
        for fn in [CREDENTIALS_FILE, CONFIG_FILE]:
            utils.ensure_file_exists(fn)
            contents = utils.load_json_dict(fn)
            for key, val in list(_FILE_CONTENT[fn].items()):
                # TODO: removed type checking below, may want to revisit
                if key not in contents:
                    contents[key] = val
            contents_keys = list(contents.keys())
            for key in contents_keys:
                if key not in _FILE_CONTENT[fn]:
                    del contents[key]
            utils.save_json_dict(fn, contents)
    else:
        warnings.warn("Looks like you don't have 'read-write' permission to "
                      "your 'home' ('~') directory or to our '~/.plotly' "
                      "directory. That means plotly's python api can't setup "
                      "local configuration files. No problem though! You'll "
                      "just have to sign-in using 'plotly.plotly.sign_in()'. For help "
                      "with that: 'help(plotly.plotly.sign_in)'."
                      "\nQuestions? support@plot.ly")


### credentials tools ###

def set_credentials_file(username=None, api_key=None, stream_ids=None):
    """Set the keyword-value pairs in `~/.plotly_credentials`.

    """
    if not _file_permissions:
        raise exceptions.PlotlyError("You don't have proper file permissions "
                                     "to run this function.")
    ensure_local_plotly_files()  # make sure what's there is OK
    credentials = get_credentials_file()
    if isinstance(username, six.string_types):
        credentials['username'] = username
    if isinstance(api_key, six.string_types):
        credentials['api_key'] = api_key
    if isinstance(stream_ids, (list, tuple)):
        credentials['stream_ids'] = stream_ids
    utils.save_json_dict(CREDENTIALS_FILE, credentials)
    ensure_local_plotly_files()  # make sure what we just put there is OK


def get_credentials_file(*args):
    """Return specified args from `~/.plotly_credentials`. as dict.

    Returns all if no arguments are specified.

    Example:
        get_credentials_file('username')

    """
    if _file_permissions:
        ensure_local_plotly_files()  # make sure what's there is OK
        return utils.load_json_dict(CREDENTIALS_FILE, *args)
    else:
        return _FILE_CONTENT[CREDENTIALS_FILE]


def reset_credentials_file():
    ensure_local_plotly_files()  # make sure what's there is OK
    utils.save_json_dict(CREDENTIALS_FILE, {})
    ensure_local_plotly_files()  # put the defaults back


### config tools ###

def set_config_file(plotly_domain=None,
                    plotly_streaming_domain=None,
                    plotly_api_domain=None,
                    plotly_ssl_verification=None):
    """Set the keyword-value pairs in `~/.plotly/.config`.

    """
    if not _file_permissions:
        raise exceptions.PlotlyError("You don't have proper file permissions "
                                     "to run this function.")
    ensure_local_plotly_files()  # make sure what's there is OK
    settings = get_config_file()
    if isinstance(plotly_domain, six.string_types):
        settings['plotly_domain'] = plotly_domain
    if isinstance(plotly_streaming_domain, six.string_types):
        settings['plotly_streaming_domain'] = plotly_streaming_domain
    if isinstance(plotly_api_domain, six.string_types):
        settings['plotly_api_domain'] = plotly_api_domain
    if isinstance(plotly_ssl_verification, (six.string_types, bool)):
        settings['plotly_ssl_verification'] = plotly_ssl_verification
    utils.save_json_dict(CONFIG_FILE, settings)
    ensure_local_plotly_files()  # make sure what we just put there is OK


def get_config_file(*args):
    """Return specified args from `~/.plotly_credentials`. as dict.

    Returns all if no arguments are specified.

    Example:
        get_credentials_file('username')

    """
    if _file_permissions:
        ensure_local_plotly_files()  # make sure what's there is OK
        return utils.load_json_dict(CONFIG_FILE, *args)
    else:
        return _FILE_CONTENT[CONFIG_FILE]


def reset_config_file():
    ensure_local_plotly_files()  # make sure what's there is OK
    f = open(CONFIG_FILE, 'w')
    f.close()
    ensure_local_plotly_files()  # put the defaults back


### embed tools ###

def get_embed(file_owner_or_url, file_id=None, width="100%", height=525):
    """Returns HTML code to embed figure on a webpage as an <iframe>

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
    width (default="100%") -- an int or string corresp. to width of the figure
    height (default="525") -- same as width but corresp. to the height of the figure

    """
    padding = 25
    plotly_rest_url = get_config_file()['plotly_domain']
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
    resource = "/apigetfile/{file_owner}/{file_id}".format(file_owner=file_owner,
                                                           file_id=file_id)
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
    if isinstance(width, int):
        s = ("<iframe id=\"igraph\" scrolling=\"no\" style=\"border:none;\""
             "seamless=\"seamless\" "
             "src=\"{plotly_rest_url}/"
             "~{file_owner}/{file_id}.embed"
             "?width={plot_width}&height={plot_height}\" "
             "height=\"{iframe_height}\" width=\"{iframe_width}\">"
             "</iframe>").format(
            plotly_rest_url=plotly_rest_url,
            file_owner=file_owner, file_id=file_id,
            plot_width=width-padding, plot_height=height-padding,
            iframe_height=height, iframe_width=width)
    else:
        s = ("<iframe id=\"igraph\" scrolling=\"no\" style=\"border:none;\""
             "seamless=\"seamless\" "
             "src=\"{plotly_rest_url}/"
             "~{file_owner}/{file_id}.embed\" "
             "height=\"{iframe_height}\" width=\"{iframe_width}\">"
             "</iframe>").format(
            plotly_rest_url=plotly_rest_url,
            file_owner=file_owner, file_id=file_id,
            iframe_height=height, iframe_width=width)

    return s


def embed(file_owner_or_url, file_id=None, width="100%", height=525):
    """Embeds existing Plotly figure in IPython Notebook

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
    width (default="100%") -- an int or string corresp. to width of the figure
    height (default="525") -- same as width but corresp. to the height of the figure

    """
    try:
        s = get_embed(file_owner_or_url, file_id, width, height)
        # see if we are in the SageMath Cloud
        from sage_salvus import html
        return html(s, hide=False)
    except:
        pass
    if _ipython_imported:
        if file_id:
            url = "{plotly_domain}/~{un}/{fid}".format(
                plotly_domain=get_config_file()['plotly_domain'],
                un=file_owner_or_url,
                fid=file_id)
        else:
            url = file_owner_or_url
        return PlotlyDisplay(url, width, height)
    else:
        warnings.warn(
            "Looks like you're not using IPython or Sage to embed this plot. "
            "If you just want the *embed code*, try using `get_embed()` "
            "instead."
            "\nQuestions? support@plot.ly")


### mpl-related tools ###
@utils.template_doc(**get_config_file())
def mpl_to_plotly(fig, resize=False, strip_style=False, verbose=False):
    """Convert a matplotlib figure to plotly dictionary and send.

    All available information about matplotlib visualizations are stored
    within a matplotlib.figure.Figure object. You can create a plot in python
    using matplotlib, store the figure object, and then pass this object to
    the fig_to_plotly function. In the background, mplexporter is used to
    crawl through the mpl figure object for appropriate information. This
    information is then systematically sent to the PlotlyRenderer which
    creates the JSON structure used to make plotly visualizations. Finally,
    these dictionaries are sent to plotly and your browser should open up a
    new tab for viewing! Optionally, if you're working in IPython, you can
    set notebook=True and the PlotlyRenderer will call plotly.iplot instead
    of plotly.plot to have the graph appear directly in the IPython notebook.

    Note, this function gives the user access to a simple, one-line way to
    render an mpl figure in plotly. If you need to trouble shoot, you can do
    this step manually by NOT running this fuction and entereing the following:

    ===========================================================================
    from mplexporter import Exporter
    from mplexporter.renderers import PlotlyRenderer

    # create an mpl figure and store it under a varialble 'fig'

    renderer = PlotlyRenderer()
    exporter = Exporter(renderer)
    exporter.run(fig)
    ===========================================================================

    You can then inspect the JSON structures by accessing these:

    renderer.layout -- a plotly layout dictionary
    renderer.data -- a list of plotly data dictionaries

    Positional arguments:
    fig -- a matplotlib figure object
    username -- a valid plotly username **
    api_key -- a valid api_key for the above username **
    notebook -- an option for use with an IPython notebook

    ** Don't have a username/api_key? Try looking here:
    {plotly_domain}/plot

    ** Forgot your api_key? Try signing in and looking here:
    {plotly_domain}/python/getting-started

    """
    if _matplotlylib_imported:
        renderer = matplotlylib.PlotlyRenderer()
        matplotlylib.Exporter(renderer).run(fig)
        if resize:
            renderer.resize()
        if strip_style:
            renderer.strip_style()
        if verbose:
            print(renderer.msg)
        return renderer.plotly_fig
    else:
        warnings.warn(
            "To use Plotly's matplotlylib functionality, you'll need to have "
            "matplotlib successfully installed with all of its dependencies. "
            "You're getting this error because matplotlib or one of its "
            "dependencies doesn't seem to be installed correctly.")


### graph_objs related tools ###

def get_subplots(rows=1, columns=1, print_grid=False, **kwargs):
    """Return a dictionary instance with the subplots set in 'layout'.

    Example 1:
    # stack two subplots vertically
    fig = tools.get_subplots(rows=2)
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x1', yaxis='y1')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Example 2:
    # print out string showing the subplot grid you've put in the layout
    fig = tools.get_subplots(rows=3, columns=2, print_grid=True)

    Keywords arguments with constant defaults:

    rows (int, default=1):
        Number of rows, evenly spaced vertically on the figure.

    columns (int, default=1):
        Number of columns, evenly spaced horizontally on the figure.

    horizontal_spacing (float in [0,1], default=0.1):
        Space between subplot columns. Applied to all columns.

    vertical_spacing (float in [0,1], default=0.05):
        Space between subplot rows. Applied to all rows.

    print_grid (True | False, default=False):
        If True, prints a tab-delimited string representation
        of your plot grid.

    Keyword arguments with variable defaults:

    horizontal_spacing (kwarg, float in [0,1], default=0.2 / columns):
        Space between subplot columns.

    vertical_spacing (kwarg, float in [0,1], default=0.3 / rows):
        Space between subplot rows.

    """

    warnings.warn(
        "tools.get_subplots is depreciated. "
        "Please use tools.make_subplots instead."
    )

    # Throw exception for non-integer rows and columns
    if not isinstance(rows, int):
        raise Exception("Keyword argument 'rows' must be an int")
    if not isinstance(columns, int):
        raise Exception("Keyword argument 'columns' must be an int")

    # Throw exception if non-valid kwarg is sent
    VALID_KWARGS = ['horizontal_spacing', 'vertical_spacing']
    for key in kwargs.keys():
        if key not in VALID_KWARGS:
            raise Exception("Invalid keyword argument: '{0}'".format(key))

    # Set 'horizontal_spacing' / 'vertical_spacing' w.r.t. rows / columns
    try:
        horizontal_spacing = float(kwargs['horizontal_spacing'])
    except KeyError:
        horizontal_spacing = 0.2 / columns
    try:
        vertical_spacing = float(kwargs['vertical_spacing'])
    except KeyError:
        vertical_spacing = 0.3 / rows

    fig = dict(layout=graph_objs.Layout())  # will return this at the end
    plot_width = (1 - horizontal_spacing * (columns - 1)) / columns
    plot_height = (1 - vertical_spacing * (rows - 1)) / rows
    plot_num = 0
    for rrr in range(rows):
        for ccc in range(columns):
            xaxis_name = 'xaxis{0}'.format(plot_num + 1)
            x_anchor = 'y{0}'.format(plot_num + 1)
            x_start = (plot_width + horizontal_spacing) * ccc
            x_end = x_start + plot_width

            yaxis_name = 'yaxis{0}'.format(plot_num + 1)
            y_anchor = 'x{0}'.format(plot_num + 1)
            y_start = (plot_height + vertical_spacing) * rrr
            y_end = y_start + plot_height

            xaxis = graph_objs.XAxis(domain=[x_start, x_end], anchor=x_anchor)
            fig['layout'][xaxis_name] = xaxis
            yaxis = graph_objs.YAxis(domain=[y_start, y_end], anchor=y_anchor)
            fig['layout'][yaxis_name] = yaxis
            plot_num += 1

    if print_grid:
        print("This is the format of your plot grid!")
        grid_string = ""
        plot = 1
        for rrr in range(rows):
            grid_line = ""
            for ccc in range(columns):
                grid_line += "[{0}]\t".format(plot)
                plot += 1
            grid_string = grid_line + '\n' + grid_string
        print(grid_string)

    return graph_objs.Figure(fig)  # forces us to validate what we just did...


def make_subplots(rows=1, cols=1,
                 shared_xaxes=False, shared_yaxes=False,
                 start_cell='bottom-left', print_grid=False,
                 **kwargs):
    """Return an instance of plotly.graph_objs.Figure
    with the subplots domain set in 'layout'.

    Example 1:
    # stack two subplots vertically
    fig = tools.make_subplots(rows=2, print_grid=True)

    This is the format of your plot grid!
    [ (1,1) x1,y1 ]
    [ (2,1) x2,y2 ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x1', yaxis='y1')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Example 2:
    # subplots with shared x axes
    fig = tools.make_subplots(rows=2, shared_xaxes=True, print_grid=True)

    TODO What's the default behavior here??

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], yaxis='y1')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], yaxis='y2')]

    Example 3:
    # irregular subplot layout (more examples below under 'specs')
    fig = tools.make_subplots(rows=2, cols=2,
                              specs=[[{}, {}],
                                     [{'colspan': 2}, None]],
                              print_grid=True)

    This is the format of your plot grid!
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3           -      ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x1', yaxis='y1')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x3', yaxis='y3')]

    Example 4:
    # insets
    fig = tools.make_subplots(insets=[{'cell': (1,1), 'l': 0.7, 'b': 0.3}],
                              print_grid=True)

    This is the format of your plot grid!
    [ (1,1) x1,y1 ]

    With insets:
    [ x2,y2 ] over [ (1,1) x1,y1 ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Keywords arguments with constant defaults:

    rows (kwarg, int, default=1):
        Number of rows in the subplot grid.

    cols (kwarg, int, default=1):
        Number of columns in the subplot grid.

    shared_xaxes (kwarg, boolean or list, default=False)
        Assign shared x axes.
        If True, all x axes are shared.

        To assign shared x axes per subplot grid cell (see 'specs'),
        send list (or list of lists, one list per shared axis)
        of cell index tuples.

    shared_yaxes (kwarg, boolean or list, default=False)
        Assign shared y axes.
        If True, all y axes are shared.

        To assign shared y axes per subplot grid cell (see 'specs'),
        send list (or list of lists, one list per shared axis)
        of cell index tuples.

    start_cell (kwarg, 'bottom-left' or 'top-left', default='top-left')
        Choose the starting cell in the subplot grid used to set the
        domains of the subplots.

    print_grid (kwarg, boolean, default=False):
        If True, prints a tab-delimited string representation of
        your plot grid.

    Keyword arguments with variable defaults:

    horizontal_spacing (kwarg, float in [0,1], default=0.2 / cols):
        Space between subplot columns.
        Applies to all columns (use 'specs' subplot-dependents spacing)

    vertical_spacing (kwarg, float in [0,1], default=0.3 / rows):
        Space between subplot rows.
        Applies to all rows (use 'specs' subplot-dependents spacing)

    specs (kwarg, list of lists of dictionaries):
        Subplot specifications.

        ex1: specs=[[{}, {}], [{'colspan': 2}, None]]

        ex2: specs=[[{'rowspan': 2}, {}], [None, {}]]

        - Indices of the outer list correspond to subplot grid rows
          starting from the bottom. The number of rows in 'specs'
          must be equal to 'rows'.

        - Indices of the inner lists correspond to subplot grid columns
          starting from the left. The number of columns in 'specs'
          must be equal to 'cols'.

        - Each item in the 'specs' list corresponds to one subplot
          in a subplot grid. (N.B. The subplot grid has exactly 'rows'
          times 'cols' cells.)

        - Use None for blank a subplot cell (or to move pass a col/row span).

        - Note that specs[0][0] has the specs of the 'start_cell' subplot.

        - Each item in 'specs' is a dictionary.
            The available keys are:

            * is_3d (boolean, default=False): flag for 3d scenes
            * colspan (int, default=1): number of subplot columns
                for this subplot to span.
            * rowspan (int, default=1): number of subplot rows
                for this subplot to span.
            * l (float, default=0.0): padding left of cell
            * r (float, default=0.0): padding right of cell
            * t (float, default=0.0): padding right of cell
            * b (float, default=0.0): padding bottom of cell

        - Use 'horizontal_spacing' and 'vertical_spacing' to adjust
          the spacing in between the subplots.

    insets (kwarg, list of dictionaries):
        Inset specifications.

        - Each item in 'insets' is a dictionary.
            The available keys are:

            * cell (tuple, default=(1,1)): (row, col) index of the
                subplot cell to overlay inset axes onto.
            * is_3d (boolean, default=False): flag for 3d scenes
            * l (float, default=0.0): padding left of inset
                  in fraction of cell width
            * w (float or 'to_end', default='to_end') inset width
                  in fraction of cell width ('to_end': to cell right edge)
            * b (float, default=0.0): padding bottom of inset
                  in fraction of cell height
            * h (float or 'to_end', default='to_end') inset height
                  in fraction of cell height ('to_end': to cell top edge)
    """

    # Throw exception for non-integer rows and cols
    if not isinstance(rows, int):
        raise Exception("Keyword argument 'rows' must be an int")
    if not isinstance(cols, int):
        raise Exception("Keyword argument 'cols' must be an int")

    # Dictionary of things start_cell
    START_CELL_all = {
        'bottom-left': {
            # 'natural' setup where x & y domains increase monotonically
            'col_dir': 1,
            'row_dir': 1
        },
        'top-left': {
            # 'default' setup visually matching the 'specs' list of lists
            'col_dir': 1,
            'row_dir': -1
        }
        # TODO maybe add 'bottom-right' and 'top-right'
    }

    # Throw exception for invalid 'start_cell' values
    try:
        START_CELL = START_CELL_all[start_cell]
    except KeyError:
        raise Exception("Invalid 'start_cell' value")

    # Throw exception if non-valid kwarg is sent
    VALID_KWARGS = ['horizontal_spacing', 'vertical_spacing',
                    'specs', 'insets']
    for key in kwargs.keys():
        if key not in VALID_KWARGS:
            raise Exception("Invalid keyword argument: '{0}'".format(key))

    # Set 'horizontal_spacing' / 'vertical_spacing' w.r.t. rows / cols
    try:
        horizontal_spacing = float(kwargs['horizontal_spacing'])
    except KeyError:
        horizontal_spacing = 0.2 / cols
    try:
        vertical_spacing = float(kwargs['vertical_spacing'])
    except KeyError:
        vertical_spacing = 0.3 / rows

    # Sanitize 'specs' (must be a list of lists)
    exception_msg = "Keyword argument 'specs' must be a list of lists"
    try:
        specs = kwargs['specs']
        if not isinstance(specs, list):
            raise Exception(exception_msg)
        else:
            for spec_row in specs:
                if not isinstance(spec_row, list):
                    raise Exception(exception_msg)
    except KeyError:
        specs = [[{}
                 for c in range(cols)]
                 for r in range(rows)]     # default 'specs'

    # Throw exception if specs is over or under specified
    if len(specs) != rows:
        raise Exception("The number of rows in 'specs' "
                        "must be equal to 'rows'")
    for r, spec_row in enumerate(specs):
        if len(spec_row) != cols:
            raise Exception("The number of columns in 'specs' "
                            "must be equal to 'cols'")

    # Sanitize 'insets'
    try:
        insets = kwargs['insets']
        if not isinstance(insets, list):
            raise Exception("Keyword argument 'insets' must be a list")
    except KeyError:
        insets = False

    # Throw exception if non-valid key / fill in defaults
    def _check_keys_and_fill(name, arg, defaults):
        def _checks(item, defaults):
            if item is None:
                return
            if not isinstance(item, dict):
                raise Exception("Items in keyword argument '{name}' must be "
                                "dictionaries or None".format(name=name))
            for k in item.keys():
                if k not in defaults.keys():
                    raise Exception("Invalid key '{k}' in keyword "
                                    "argument '{name}'".format(k=k, name=name))
            for k in defaults.keys():
                if k not in item.keys():
                    item[k] = defaults[k]
        for arg_i in arg:
            if isinstance(arg_i, list):
                for arg_ii in arg_i:
                    _checks(arg_ii, defaults)
            elif isinstance(arg_i, dict):
                _checks(arg_i, defaults)

    # Default spec key-values
    SPEC_defaults = dict(
        is_3d=False,
        colspan=1,
        rowspan=1,
        l=0.0,
        r=0.0,
        b=0.0,
        t=0.0
    )
    _check_keys_and_fill('specs', specs, SPEC_defaults)

    # Default inset key-values
    if insets:
        INSET_defaults = dict(
            cell=(0, 0),
            is_3d=False,
            l=0.0,
            w='to_end',
            b=0.0,
            h='to_end'
        )
        _check_keys_and_fill('insets', insets, INSET_defaults)

    # Set width & height of each subplot cell (excluding padding)
    width = (1. - horizontal_spacing * (cols - 1)) / cols
    height = (1. - vertical_spacing * (rows - 1)) / rows

    # Built row/col sequence using 'row_dir' and 'col_dir'
    col_dir = START_CELL['col_dir']
    col_seq = range(cols)[::col_dir]
    row_dir = START_CELL['row_dir']
    row_seq = range(rows)[::row_dir]

    # [grid] Build subplot grid (coord tuple of cell)
    grid = [[((width + horizontal_spacing) * c,
              (height + vertical_spacing) * r)
            for c in col_seq]
            for r in row_seq]

    # [grid_ref] Initialize the grid and insets' axis-reference lists
    grid_ref = [[None for c in range(cols)] for r in range(rows)]
    insets_ref = [None for inset in range(len(insets))] if insets else None

    layout = graph_objs.Layout()  # init layout object

    # Function handling logic around 2d axis labels
    # Returns 'x{}' | 'y{}'
    def _get_label(x_or_y, row, col, cnt, shared_axes):
        # Default label (given strictly by cnt)
        label = "{x_or_y}{cnt}".format(x_or_y=x_or_y, cnt=cnt)

        if isinstance(shared_axes, bool):
            if shared_axes:
                if x_or_y == 'x':
                    label = "{x_or_y}{c}".format(x_or_y=x_or_y, c=col+1)
                if x_or_y == 'y':
                    label = "{x_or_y}{r}".format(x_or_y=x_or_y, r=row+1)

        if isinstance(shared_axes, list):
            if isinstance(shared_axes[0], tuple):
                shared_axes = [shared_axes]  # TODO put this elsewhere
            for shared_axis in shared_axes:
                if (row, col) in shared_axis:
                    label = {
                        'x': "x{0}".format(shared_axis[0][1]+1),
                        'y': "y{0}".format(shared_axis[0][0]+1)
                    }[x_or_y]

        return label

    # Function handling logic around 2d axis anchors
    # Return 'x{}' | 'y{}' | 'free' | False
    def _get_anchors(row, col, x_cnt, y_cnt, shared_xaxes, shared_yaxes):
        # Default anchors (give strictly by cnt)
        x_anchor = "y{y_cnt}".format(y_cnt=y_cnt)
        y_anchor = "x{x_cnt}".format(x_cnt=x_cnt)

        if isinstance(shared_xaxes, bool):
            if shared_xaxes:
                if row == 0:
                    x_anchor = "y{col_cnt}".format(col_cnt=col+1)
                else:
                    x_anchor = False
                    y_anchor = 'free'
                    if shared_yaxes and col > 0:  # TODO covers all cases?
                        y_anchor = False
                    return x_anchor, y_anchor

        elif isinstance(shared_xaxes, list):
            if isinstance(shared_xaxes[0], tuple):
                shared_xaxes = [shared_xaxes]  # TODO put this elsewhere
            for shared_xaxis in shared_xaxes:
                if (row, col) in shared_xaxis[1:]:
                    x_anchor = False
                    y_anchor = 'free'  # TODO covers all cases?

        if isinstance(shared_yaxes, bool):
            if shared_yaxes:
                if col == 0:
                    y_anchor = "x{row_cnt}".format(row_cnt=row+1)
                else:
                    y_anchor = False
                    x_anchor = 'free'
                    if shared_xaxes and row > 0:  # TODO covers all cases?
                        x_anchor = False
                    return x_anchor, y_anchor

        elif isinstance(shared_yaxes, list):
            if isinstance(shared_yaxes[0], tuple):
                shared_yaxes = [shared_yaxes]  # TODO put this elsewhere
            for shared_yaxis in shared_yaxes:
                if (row, col) in shared_yaxis[1:]:
                    y_anchor = False
                    x_anchor = 'free'  # TODO covers all cases?

        return x_anchor, y_anchor

    # Function pasting x/y domains in fig object (2d case)
    def _add_domain(fig, x_or_y, label, domain, anchor, position):
        name = label[0] + 'axis' + label[1:]
        graph_obj = '{X_or_Y}Axis'.format(X_or_Y=x_or_y.upper())
        axis = getattr(graph_objs, graph_obj)(domain=domain)
        if anchor:
            axis['anchor'] = anchor
        if position:  # N.B. No need to add position == 0 to axis
            axis['position'] = position
        fig['layout'][name] = axis

    # Function pasting x/y domains in fig object (3d case)
    def _add_domain_is_3d(fig, s_cnt, x_domain, y_domain):
        scene_name = "scene{s_cnt}".format(s_cnt=s_cnt)
        scene = graph_objs.Scene(domain={'x': x_domain, 'y': y_domain})
        fig['layout'][scene_name] = scene

    x_cnt = y_cnt = s_cnt = 1  # subplot axis/scene counters

    # Loop through specs -- (r, c) <-> (row, col)
    for r, spec_row in enumerate(specs):
        for c, spec in enumerate(spec_row):

            if spec is None:  # skip over None cells
                continue

            c_spanned = c + spec['colspan'] - 1  # get spanned c
            r_spanned = r + spec['rowspan'] - 1  # get spanned r

            # Throw exception if 'colspan' | 'rowspan' is too large for grid
            if c_spanned >= cols:
                raise Exception("Some 'colspan' value is too large for "
                                "this subplot grid.")
            if r_spanned >= rows:
                raise Exception("Some 'rowspan' value is too large for "
                                "this subplot grid.")

            # Get x domain using grid and colspan
            x_s = grid[r][c][0] + spec['l']
            x_e = grid[r][c_spanned][0] + width - spec['r']
            x_domain = [x_s, x_e]

            # Get y domain (dep. on row_dir) using grid & r_spanned
            if row_dir > 0:
                y_s = grid[r][c][1] + spec['b']
                y_e = grid[r_spanned][c][1] + height - spec['t']
            else:
                y_s = grid[r_spanned][c][1] + spec['b']
                y_e = grid[r][c][1] + height - spec['t']
            y_domain = [y_s, y_e]

            if spec['is_3d']:

                # Add scene to layout
                s_label = 'scene{0}'.format(s_cnt)
                _add_domain_is_3d(layout, s_label, x_domain, y_domain)
                grid_ref[r][c] = (s_label, )
                s_cnt += 1

            else:

                # Get axis label and anchor
                x_label = _get_label('x', r, c, x_cnt, shared_xaxes)
                y_label = _get_label('y', r, c, y_cnt, shared_yaxes)
                x_anchor, y_anchor = _get_anchors(r, c,
                                                  x_cnt, y_cnt,
                                                  shared_xaxes,
                                                  shared_yaxes)

                # Add a xaxis to layout (N.B anchor == False -> no axis)
                if x_anchor:
                    x_position = y_domain[0] if x_anchor == 'free' else 0
                    _add_domain(layout, 'x', x_label, x_domain,
                                x_anchor, x_position)
                    x_cnt += 1

                # Add a yaxis to layout (N.B anchor == False -> no axis)
                if y_anchor:
                    y_position = x_domain[0] if y_anchor == 'free' else 0
                    _add_domain(layout, 'y', y_label, y_domain,
                                y_anchor, y_position)
                    y_cnt += 1

                grid_ref[r][c] = (x_label, y_label)  # fill in ref
                if print_grid:
                    grid_str[i][j] = '[{},{}'.format(x_label, y_label)

            # String representation for spanned cells
            # TODO more general spacing over spanned cells
            if print_grid:
                if spec['colspan'] > 1:
                    for c in range(1, spec['colspan']-1):
                        grid_str[i][j+c] = '       '
                    grid_str[i][j+spec['colspan']-1] = '       ]'
                else:
                    grid_str[i][j] += ']'
                if spec['rowspan'] > 1:
                    for r in range(1, spec['rowspan']-1):
                        grid_str[i+r][j] = '       '
                    for c in range(0, spec['colspan']):
                        grid_str[i+spec['rowspan']-1][j+c] = '   ^   '

    # Loop through insets
    if insets:
        for i_inset, inset in enumerate(insets):

            i = inset['cell'][0]
            j = inset['cell'][1]

            # Get inset x domain using grid
            x_s = grid[i][j][0] + inset['l'] * width
            if inset['w'] == 'to_end':
                x_e = grid[i][j][0] + width
            else:
                x_e = x_s + inset['w'] * width
            x_domain = [x_s, x_e]

            # Get inset y domain using grid
            y_s = grid[i][j][1] + inset['b'] * height
            if inset['h'] == 'to_end':
                y_e = grid[i][j][1] + height
            else:
                y_e = y_s + inset['h'] * height
            y_domain = [y_s, y_e]

            if inset['is_3d']:
                # Add scene to layout
                _add_domain_is_3d(fig, s_cnt, x_domain, y_domain)
                if print_grid:
                    insets_str[i_inset] = '[scene{}]'.format(s_cnt)
                s_cnt += 1
            else:

                # Get axis label and anchor
                x_label = _get_label('x', False, False, x_cnt, False)
                y_label = _get_label('y', False, False, y_cnt, False)
                x_anchor, y_anchor = _get_anchors(row, col,
                                                  x_cnt, y_cnt,
                                                  False, False)

                # Add a xaxis to layout (N.B insets always have anchors)
                _add_domain(fig, 'x', x_label, x_domain, x_anchor, False)
                x_cnt += 1

                # Add a yayis to layout (N.B insets always have anchors)
                _add_domain(fig, 'y', y_label, y_domain, y_anchor, False)
                y_cnt += 1

                if print_grid:
                    insets_str[i_inset] = '[{},{}]'.format(x_label, y_label)

    if print_grid:
        print("This is the format of your plot grid!")
        grid_string = ""
        for grid_str_row in grid_str:
            grid_string = "  ".join(grid_str_row) + '\n' + grid_string
        print(grid_string)
        if insets:
            print("With insets:")
            for i_inset, inset in enumerate(insets):
                print(
                    insets_str[i_inset] + ' over ' +
                    grid_str[inset['cell'][0]][inset['cell'][1]])
            print('')

    fig = graph_objs.Figure(layout=layout)
    return fig


def get_valid_graph_obj(obj, obj_type=None):
    """Returns a new graph object that is guaranteed to pass validate().

    CAREFUL: this will *silently* strip out invalid pieces of the object.

    """
    try:
        new_obj = graph_objs.get_class_instance_by_name(
            obj.__class__.__name__)
    except KeyError:
        try:
            new_obj = graph_objs.get_class_instance_by_name(obj_type)
        except KeyError:
            raise exceptions.PlotlyError(
                "'{0}' nor '{1}' are recognizable graph_objs.".
                format(obj.__class__.__name__, obj_type))
    if isinstance(new_obj, list):
        new_obj += obj
    else:
        for key, val in list(obj.items()):
            new_obj[key] = val
    new_obj.force_clean()
    return new_obj


def validate(obj, obj_type):
    """Validate a dictionary, list, or graph object as 'obj_type'.

    This will not alter the 'obj' referenced in the call signature. It will
    raise an error if the 'obj' reference could not be instantiated as a
    valid 'obj_type' graph object.

    """
    try:
        obj_type = graph_objs.KEY_TO_NAME[obj_type]
    except KeyError:
        pass
    try:
        test_obj = graph_objs.get_class_instance_by_name(obj_type, obj)
    except KeyError:
        raise exceptions.PlotlyError(
            "'{0}' is not a recognizable graph_obj.".
            format(obj_type))


def validate_stream(obj, obj_type):
    """Validate a data dictionary (only) for use with streaming.

    An error is raised if a key within (or nested within) is not streamable.

    """
    try:
        obj_type = graph_objs.KEY_TO_NAME[obj_type]
    except KeyError:
        pass
    info = graph_objs.INFO[graph_objs.NAME_TO_KEY[obj_type]]
    for key, val in list(obj.items()):
        if key == 'type':
            continue
        if 'streamable' in info['keymeta'][key].keys():
            if not info['keymeta'][key]['streamable']:
                raise exceptions.PlotlyError(
                    "The '{0}' key is not streamable in the '{1}' "
                    "object".format(
                        key, obj_type
                    )
                )
        else:
            raise exceptions.PlotlyError(
                "The '{0}' key is not streamable in the '{1}' object".format(
                    key, obj_type
                )
            )
        try:
            sub_obj_type = graph_objs.KEY_TO_NAME[key]
            validate_stream(val, sub_obj_type)
        except KeyError:
            pass


def _replace_newline(obj):
    """Replaces '\n' with '<br>' for all strings in a collection."""
    if isinstance(obj, dict):
        d = dict()
        for key, val in list(obj.items()):
            d[key] = _replace_newline(val)
        return d
    elif isinstance(obj, list):
        l = list()
        for index, entry in enumerate(obj):
            l += [_replace_newline(entry)]
        return l
    elif isinstance(obj, six.string_types):
        s = obj.replace('\n', '<br>')
        if s != obj:
            warnings.warn("Looks like you used a newline character: '\\n'.\n\n"
                          "Plotly uses a subset of HTML escape characters\n"
                          "to do things like newline (<br>), bold (<b></b>),\n"
                          "italics (<i></i>), etc. Your newline characters \n"
                          "have been converted to '<br>' so they will show \n"
                          "up right on your Plotly figure!")
        return s
    else:
        return obj  # we return the actual reference... but DON'T mutate.


if _ipython_imported:
    class PlotlyDisplay(IPython.core.display.HTML):
        """An IPython display object for use with plotly urls

        PlotlyDisplay objects should be instantiated with a url for a plot.
        IPython will *choose* the proper display representation from any
        Python object, and using provided methods if they exist. By defining
        the following, if an HTML display is unusable, the PlotlyDisplay
        object can provide alternate representations.

        """
        def __init__(self, url, width, height):
            self.resource = url
            self.embed_code = get_embed(url, width=width, height=height)
            super(PlotlyDisplay, self).__init__(data=self.embed_code)

        def _repr_html_(self):
            return self.embed_code

        def _repr_svg_(self):
            url = self.resource + ".svg"
            res = requests.get(url)
            if six.PY3:
                cont = res.content.decode('utf-8', 'replace')
            else:
                cont = res.content
            return cont

        def _repr_png_(self):
            url = self.resource + ".png"
            res = requests.get(url)
            cont = res.content
            return cont

        def _repr_pdf_(self):
            url = self.resource + ".pdf"
            res = requests.get(url)
            cont = res.content
            if six.PY3:
                cont = res.content.decode('utf-8', 'replace')
            else:
                cont = res.content
            return cont

        def _repr_jpeg_(self):
            url = self.resource + ".jpeg"
            res = requests.get(url)
            cont = res.content
            return cont
