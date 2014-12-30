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

def get_subplots(rows=1, columns=1,
                 shared_xaxes=False, shared_yaxes=False,
                 print_grid=False, **kwargs):
    """Return an instance of plotly.graph_objs.Figure
    with the subplots domain set in 'layout'.

    Example 1:
        # stack two subplots vertically
        fig = tools.get_subplots(rows=2)
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x1', yaxis='y1')]
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Example 2:
        # subplots with shared x axes
        fig = tools.get_subplots(rows=2, shared_xaxes=True)
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], yaxis='y1')]
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], yaxis='y2')]

    Example 3:
        # irregular subplot layout
        fig = tools.get_subplots(rows=2, columns=2,
                                 specs=[[{}, {}], [{'colspan': 2}]])
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x1', yaxis='y1')]
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]
        fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x3', yaxis='y3')]

    Example 4:
        # print out string showing the subplot grid you've put in the layout
        fig = tools.get_subplots(rows=3, columns=2, print_grid=True)

    Keywords arguments with constant defaults:

    rows (kwarg, int, default=1):
        Number of rows on the figure.

    columns (kwarg, int, default=1):
        Number of columns on the figure.

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

    print_grid (kwarg, boolean, default=False):
        If True, prints a tab-delimited string representation of
        your plot grid.

    Keyword arguments with variable defaults:

    horizontal_spacing (kwarg, float in [0,1], default=0.2 / columns):
        Space between subplot columns.

        Applies to all columns (use 'specs' subplot-dependents spacing)

    vertical_spacing (kwarg, float in [0,1], default=0.3 / rows):
        Space between subplot rows.
        Applies to all rows (use 'specs' subplot-dependents spacing)

    specs (kwarg, list (of lists) of dictionaries):
        Subplot specifications.

        - Indices of the outer list correspond to subplot grid rows
          starting from the bottom.

        - Indices of the inner lists correspond to subplot grid columns
          starting from the left

        - Note that specs[0][0] has the specs for the bottom-left subplot

        - Each item in the 'specs' list corresponds to one subplot
          in a subplot grid. The subplot grid has 'rows' times 'columns'
          cells.

        - Each item in the 'specs' is a dictionary.
            The available keys are:

            * isEmpty (boolean, default=False): flag for empty grid cells
            * is3D (boolean, default=False): flag for 3d scenes
            * colspan (int, default=1): span across grid columns
                                        from left to right
            * rowspan (int, default=1): span across grid rows
                                        from bottom to top
            * l (float, default=0.0): padding left of cell
            * r (float, default=0.0): padding right of cell
            * t (float, default=0.0): padding right of cell
            * b (float, default=0.0): padding bottom of cell
    """

    # Throw exception for non-integer rows and columns
    if not isinstance(rows, int):
        raise Exception("Keyword argument 'rows' must be an int")
    if not isinstance(columns, int):
        raise Exception("Keyword argument 'columns' must be an int")

    # Set 'horizontal_spacing' / 'vertical_spacing' w.r.t. rows / columns
    try:
        horizontal_spacing = float(kwargs['horizontal_spacing'])
    except KeyError:
        horizontal_spacing = 0.2 / columns
    try:
        vertical_spacing = float(kwargs['vertical_spacing'])
    except KeyError:
        vertical_spacing = 0.3 / rows

    # Sanitize 'specs' -- TODO more sanitizing?
    try:
        specs = kwargs['specs']
        if not isinstance(specs, list):
            raise Exception("Keyword argument 'specs' must be a list")
        elif isinstance(specs[0], dict):
            # To support one-row specs=[{},{}]
            specs = [specs]
    except KeyError:
        specs = [[{}
                 for col in range(columns)]
                 for row in range(rows)]     # default 'specs'

    # Default spec key-values
    SPEC_defaults = dict(
        isEmpty=False,
        is3D=False,
        colspan=1,
        rowspan=1,
        l=0.0,
        r=0.0,
        t=0.0,
        b=0.0
    )

    # Fill in 'specs' with defaults
    for spec_row in specs:
        for spec in spec_row:
            for k in SPEC_defaults.keys():
                if k not in spec.keys():
                    spec[k] = SPEC_defaults[k]

    # Width / Height of each subplot cell (exclud. spacing and padding)
    width = 1. / columns
    height = 1. / rows

    # Spacing corrections between each subplot
    x_space = horizontal_spacing * (columns - 1) / columns
    y_space = vertical_spacing * (rows - 1) / rows

    # Handler for shared axes logic (return shared axis label or False)
    def _get_shared(cell, x_or_y, shared_axes):
        if isinstance(shared_axes, bool):
            if not shared_axes:
                return False
            if x_or_y == 'x':
                if cell[0] == 0:
                    return False
                else:
                    return "x{0}".format(cell[1]+1)
            elif x_or_y == 'y':
                if cell[1] == 0:
                    return False
                else:
                    return "y{0}".format(cell[0]+1)
        elif isinstance(shared_axes, list):
            if isinstance(shared_axes[0], tuple):
                if cell in shared_axes and cell != shared_axes[0]:
                    return {
                        'x': "x{0}".format(shared_axes[0][1]+1),
                        'y': "y{0}".format(shared_axes[0][0]+1)
                    }[x_or_y]
                else:
                    return False
            elif isinstance(shared_axes[0], list):
                for shared_axis in shared_axes:
                    if cell in shared_axis and cell != shared_axis[0]:
                        return {
                            'x': "x{0}".format(shared_axis[0][1]+1),
                            'y': "y{0}".format(shared_axis[0][0]+1)
                        }[x_or_y]
                else:
                    return False
            else:
                return False
        else:
            return False

    # Function pasting x/y domains in fig object (2d anchored case)
    def _add_domain(fig, x_or_y, cnt, shared, domain):
        num = cnt + 1
        y_or_x = {'x': 'y', 'y': 'x'}[x_or_y]
        axis_name = '{x_or_y}axis{num}'.format(x_or_y=x_or_y, num=num)
        graph_obj = '{X_or_Y}Axis'.format(X_or_Y=x_or_y.upper())
        axis = getattr(graph_objs, graph_obj)(domain=domain)
        if not shared:  # non-shared axes get an anchor
            anchor = '{y_or_x}{num}'.format(y_or_x=y_or_x, num=num)
            axis['anchor'] = anchor
        fig['layout'][axis_name] = axis

    # Function pasting x/y domains in fig object (3d case)
    def _add_domain_is3D(fig, s_cnt, x_domain, y_domain):
        num = s_cnt + 1
        scene_name = "scene{num}".format(num=num)
        scene = graph_objs.Scene(domain={'x': x_domain, 'y': y_domain})
        fig['layout'][scene_name] = scene

    # Loop through 'specs'
    for row, spec_row in enumerate(specs):

        x = 0  # init x tracer before row

        for col, spec in enumerate(spec_row):

            # Get x domain (and correct x_e for colspan > 1)
            x_s = x + spec['l']
            x_e = x_s + spec['colspan'] * width
            x_e -= (spec['l'] + spec['r'] + x_space)
            if spec['colspan'] > 1:
                x_e += (spec['colspan'] - 1) * (horizontal_spacing - x_space)

            # Get y domain (and correct y_e for rowspan > 1)
            y_s = y + spec['b']
            y_e = y_s + spec['rowspan'] * height
            y_e -= (spec['b'] + spec['t'] + y_space)
            if spec['rowspan'] > 1:
                y_e += (spec['rowspan'] - 1) * (vertical_spacing - y_space)

            # Add domains to fig!
            if not spec['isEmpty']:
                if spec['is3D']:
                    _add_domain_is3D(fig, s_cnt, [x_s, x_e], [y_s, y_e])
                    _fill_grid(grid, (row, col), spec, s_cnt, False)
                    s_cnt += 1

                else:
                    x_shared = get_shared((row, col), 'x', shared_xaxes)
                    y_shared = get_shared((row, col), 'y', shared_yaxes)
                    _fill_grid(grid, (row, col), spec,
                               (x_cnt, y_cnt), (x_shared, y_shared))
                    if not x_shared:
                        _add_domain(fig, 'x', x_cnt, y_shared, [x_s, x_e])
                        x_cnt += 1
                    if not y_shared:
                        _add_domain(fig, 'y', y_cnt, x_shared, [y_s, y_e])
                        y_cnt += 1
            else:
                _fill_grid(grid, (row, col), spec, False, (False, False))

            x = x_e + horizontal_spacing  # move tracer to next col

        y = y_e + vertical_spacing  # move tracer to next row

    if print_grid:
        print("This is the format of your plot grid!")
        grid_string = ""
        print(grid_string)
    return graph_objs.Figure(fig)  # forces us to validate what we just did...


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
