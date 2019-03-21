# -*- coding: utf-8 -*-

"""
tools
=====

Functions that USERS will possibly want access to.

"""
from __future__ import absolute_import

import warnings

import six
import copy

import plotly.exceptions
from plotly import optional_imports
from chart_studio import session, utils
from chart_studio.files import CONFIG_FILE, CREDENTIALS_FILE, FILE_CONTENT
from plotly.files import ensure_writable_plotly_dir

DEFAULT_PLOTLY_COLORS = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                         'rgb(44, 160, 44)', 'rgb(214, 39, 40)',
                         'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                         'rgb(227, 119, 194)', 'rgb(127, 127, 127)',
                         'rgb(188, 189, 34)', 'rgb(23, 190, 207)']


REQUIRED_GANTT_KEYS = ['Task', 'Start', 'Finish']
PLOTLY_SCALES = {'Greys': ['rgb(0,0,0)', 'rgb(255,255,255)'],
                 'YlGnBu': ['rgb(8,29,88)', 'rgb(255,255,217)'],
                 'Greens': ['rgb(0,68,27)', 'rgb(247,252,245)'],
                 'YlOrRd': ['rgb(128,0,38)', 'rgb(255,255,204)'],
                 'Bluered': ['rgb(0,0,255)', 'rgb(255,0,0)'],
                 'RdBu': ['rgb(5,10,172)', 'rgb(178,10,28)'],
                 'Reds': ['rgb(220,220,220)', 'rgb(178,10,28)'],
                 'Blues': ['rgb(5,10,172)', 'rgb(220,220,220)'],
                 'Picnic': ['rgb(0,0,255)', 'rgb(255,0,0)'],
                 'Rainbow': ['rgb(150,0,90)', 'rgb(255,0,0)'],
                 'Portland': ['rgb(12,51,131)', 'rgb(217,30,30)'],
                 'Jet': ['rgb(0,0,131)', 'rgb(128,0,0)'],
                 'Hot': ['rgb(0,0,0)', 'rgb(255,255,255)'],
                 'Blackbody': ['rgb(0,0,0)', 'rgb(160,200,255)'],
                 'Earth': ['rgb(0,0,130)', 'rgb(255,255,255)'],
                 'Electric': ['rgb(0,0,0)', 'rgb(255,250,220)'],
                 'Viridis': ['rgb(68,1,84)', 'rgb(253,231,37)']}

# color constants for violin plot
DEFAULT_FILLCOLOR = '#1f77b4'
DEFAULT_HISTNORM = 'probability density'
ALTERNATIVE_HISTNORM = 'probability'


# Warning format
def warning_on_one_line(message, category, filename, lineno,
                        file=None, line=None):
    return '%s:%s: %s:\n\n%s\n\n' % (filename, lineno, category.__name__,
                                     message)
warnings.formatwarning = warning_on_one_line

ipython_core_display = optional_imports.get_module('IPython.core.display')
sage_salvus = optional_imports.get_module('sage_salvus')


def get_config_defaults():
    """
    Convenience function to check current settings against defaults.

    Example:

        if plotly_domain != get_config_defaults()['plotly_domain']:
            # do something

    """
    return dict(FILE_CONTENT[CONFIG_FILE])  # performs a shallow copy


def ensure_local_plotly_files():
    """Ensure that filesystem is setup/filled out in a valid way.
    If the config or credential files aren't filled out, then write them
    to the disk.
    """
    if ensure_writable_plotly_dir():
        for fn in [CREDENTIALS_FILE, CONFIG_FILE]:
            utils.ensure_file_exists(fn)
            contents = utils.load_json_dict(fn)
            contents_orig = contents.copy()
            for key, val in list(FILE_CONTENT[fn].items()):
                # TODO: removed type checking below, may want to revisit
                if key not in contents:
                    contents[key] = val
            contents_keys = list(contents.keys())
            for key in contents_keys:
                if key not in FILE_CONTENT[fn]:
                    del contents[key]
            # save only if contents has changed.
            # This is to avoid .credentials or .config file to be overwritten randomly,
            # which we constantly keep experiencing
            # (sync issues? the file might be locked for writing by other process in file._permissions)
            if contents_orig.keys() != contents.keys():
                utils.save_json_dict(fn, contents)

    else:
        warnings.warn("Looks like you don't have 'read-write' permission to "
                      "your 'home' ('~') directory or to our '~/.plotly' "
                      "directory. That means plotly's python api can't setup "
                      "local configuration files. No problem though! You'll "
                      "just have to sign-in using 'plotly.plotly.sign_in()'. "
                      "For help with that: 'help(plotly.plotly.sign_in)'."
                      "\nQuestions? Visit https://support.plot.ly")


### credentials tools ###

def set_credentials_file(username=None,
                         api_key=None,
                         stream_ids=None,
                         proxy_username=None,
                         proxy_password=None):
    """Set the keyword-value pairs in `~/.plotly_credentials`.

    :param (str) username: The username you'd use to sign in to Plotly
    :param (str) api_key: The api key associated with above username
    :param (list) stream_ids: Stream tokens for above credentials
    :param (str) proxy_username: The un associated with with your Proxy
    :param (str) proxy_password: The pw associated with your Proxy un

    """
    if not ensure_writable_plotly_dir():
        raise plotly.exceptions.PlotlyError("You don't have proper file permissions "
                                     "to run this function.")
    ensure_local_plotly_files()  # make sure what's there is OK
    credentials = get_credentials_file()
    if isinstance(username, six.string_types):
        credentials['username'] = username
    if isinstance(api_key, six.string_types):
        credentials['api_key'] = api_key
    if isinstance(proxy_username, six.string_types):
        credentials['proxy_username'] = proxy_username
    if isinstance(proxy_password, six.string_types):
        credentials['proxy_password'] = proxy_password
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
    # Read credentials from file if possible
    credentials = utils.load_json_dict(CREDENTIALS_FILE, *args)
    if not credentials:
        # Credentials could not be read, use defaults
        credentials = copy.copy(FILE_CONTENT[CREDENTIALS_FILE])

    return credentials


def reset_credentials_file():
    ensure_local_plotly_files()  # make sure what's there is OK
    utils.save_json_dict(CREDENTIALS_FILE, {})
    ensure_local_plotly_files()  # put the defaults back


### config tools ###

def set_config_file(plotly_domain=None,
                    plotly_streaming_domain=None,
                    plotly_api_domain=None,
                    plotly_ssl_verification=None,
                    plotly_proxy_authorization=None,
                    world_readable=None,
                    sharing=None,
                    auto_open=None):
    """Set the keyword-value pairs in `~/.plotly/.config`.

    :param (str) plotly_domain: ex - https://plot.ly
    :param (str) plotly_streaming_domain: ex - stream.plot.ly
    :param (str) plotly_api_domain: ex - https://api.plot.ly
    :param (bool) plotly_ssl_verification: True = verify, False = don't verify
    :param (bool) plotly_proxy_authorization: True = use plotly proxy auth creds
    :param (bool) world_readable: True = public, False = private

    """
    if not ensure_writable_plotly_dir():
        raise plotly.exceptions.PlotlyError("You don't have proper file permissions "
                                     "to run this function.")
    ensure_local_plotly_files()  # make sure what's there is OK
    utils.validate_world_readable_and_sharing_settings({
        'sharing': sharing, 'world_readable': world_readable})

    settings = get_config_file()
    if isinstance(plotly_domain, six.string_types):
        settings['plotly_domain'] = plotly_domain
    elif plotly_domain is not None:
        raise TypeError('plotly_domain should be a string')
    if isinstance(plotly_streaming_domain, six.string_types):
        settings['plotly_streaming_domain'] = plotly_streaming_domain
    elif plotly_streaming_domain is not None:
        raise TypeError('plotly_streaming_domain should be a string')
    if isinstance(plotly_api_domain, six.string_types):
        settings['plotly_api_domain'] = plotly_api_domain
    elif plotly_api_domain is not None:
        raise TypeError('plotly_api_domain should be a string')
    if isinstance(plotly_ssl_verification, (six.string_types, bool)):
        settings['plotly_ssl_verification'] = plotly_ssl_verification
    elif plotly_ssl_verification is not None:
        raise TypeError('plotly_ssl_verification should be a boolean')
    if isinstance(plotly_proxy_authorization, (six.string_types, bool)):
        settings['plotly_proxy_authorization'] = plotly_proxy_authorization
    elif plotly_proxy_authorization is not None:
        raise TypeError('plotly_proxy_authorization should be a boolean')
    if isinstance(auto_open, bool):
        settings['auto_open'] = auto_open
    elif auto_open is not None:
        raise TypeError('auto_open should be a boolean')

    # validate plotly_domain and plotly_api_domain
    utils.validate_plotly_domains(
        {'plotly_domain': plotly_domain, 'plotly_api_domain': plotly_api_domain}
    )

    if isinstance(world_readable, bool):
        settings['world_readable'] = world_readable
        settings.pop('sharing')
    elif world_readable is not None:
        raise TypeError('Input should be a boolean')
    if isinstance(sharing, six.string_types):
        settings['sharing'] = sharing
    elif sharing is not None:
        raise TypeError('sharing should be a string')
    utils.set_sharing_and_world_readable(settings)

    utils.save_json_dict(CONFIG_FILE, settings)
    ensure_local_plotly_files()  # make sure what we just put there is OK


def get_config_file(*args):
    """Return specified args from `~/.plotly/.config`. as tuple.

    Returns all if no arguments are specified.

    Example:
        get_config_file('plotly_domain')

    """
    # Read config from file if possible
    config = utils.load_json_dict(CONFIG_FILE, *args)
    if not config:
        # Config could not be read, use defaults
        config = copy.copy(FILE_CONTENT[CONFIG_FILE])

    return config


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
    as the first argument, you MUST NOT specify a `file_id` keyword argument,
    or file_id must be set to Python's None value.

    Positional arguments:
    file_owner_or_url (string) -- a valid plotly username OR a valid plotly url

    Keyword arguments:
    file_id (default=None) -- an int or string that can be converted to int
                              if you're using a url, don't fill this in!
    width (default="100%") -- an int or string corresp. to width of the figure
    height (default="525") -- same as width but corresp. to the height of the
                              figure

    """
    plotly_rest_url = (session.get_session_config().get('plotly_domain') or
                       get_config_file()['plotly_domain'])
    if file_id is None:  # assume we're using a url
        url = file_owner_or_url
        if url[:len(plotly_rest_url)] != plotly_rest_url:
            raise plotly.exceptions.PlotlyError(
                "Because you didn't supply a 'file_id' in the call, "
                "we're assuming you're trying to snag a figure from a url. "
                "You supplied the url, '{0}', we expected it to start with "
                "'{1}'."
                "\nRun help on this function for more information."
                "".format(url, plotly_rest_url))
        urlsplit = six.moves.urllib.parse.urlparse(url)
        file_owner = urlsplit.path.split('/')[1].split('~')[1]
        file_id = urlsplit.path.split('/')[2]

        # to check for share_key we check urlsplit.query
        query_dict = six.moves.urllib.parse.parse_qs(urlsplit.query)
        if query_dict:
            share_key = query_dict['share_key'][-1]
        else:
            share_key = ''
    else:
        file_owner = file_owner_or_url
        share_key = ''
    try:
        test_if_int = int(file_id)
    except ValueError:
        raise plotly.exceptions.PlotlyError(
            "The 'file_id' argument was not able to be converted into an "
            "integer number. Make sure that the positional 'file_id' argument "
            "is a number that can be converted into an integer or a string "
            "that can be converted into an integer."
        )
    if int(file_id) < 0:
        raise plotly.exceptions.PlotlyError(
            "The 'file_id' argument must be a non-negative number."
        )
    if share_key is '':
        s = ("<iframe id=\"igraph\" scrolling=\"no\" style=\"border:none;\" "
             "seamless=\"seamless\" "
             "src=\"{plotly_rest_url}/"
             "~{file_owner}/{file_id}.embed\" "
             "height=\"{iframe_height}\" width=\"{iframe_width}\">"
             "</iframe>").format(
            plotly_rest_url=plotly_rest_url,
            file_owner=file_owner, file_id=file_id,
            iframe_height=height, iframe_width=width)
    else:
        s = ("<iframe id=\"igraph\" scrolling=\"no\" style=\"border:none;\" "
             "seamless=\"seamless\" "
             "src=\"{plotly_rest_url}/"
             "~{file_owner}/{file_id}.embed?share_key={share_key}\" "
             "height=\"{iframe_height}\" width=\"{iframe_width}\">"
             "</iframe>").format(
            plotly_rest_url=plotly_rest_url,
            file_owner=file_owner, file_id=file_id, share_key=share_key,
            iframe_height=height, iframe_width=width)

    return s


def embed(file_owner_or_url, file_id=None, width="100%", height=525):
    """Embeds existing Plotly figure in IPython Notebook

    Plotly uniquely identifies figures with a 'file_owner'/'file_id' pair.
    Since each file is given a corresponding unique url, you may also simply
    pass a valid plotly url as the first argument.

    Note, if you're using a file_owner string as the first argument, you MUST
    specify a `file_id` keyword argument. Else, if you're using a url string
    as the first argument, you MUST NOT specify a `file_id` keyword argument,
    or file_id must be set to Python's None value.

    Positional arguments:
    file_owner_or_url (string) -- a valid plotly username OR a valid plotly url

    Keyword arguments:
    file_id (default=None) -- an int or string that can be converted to int
                              if you're using a url, don't fill this in!
    width (default="100%") -- an int or string corresp. to width of the figure
    height (default="525") -- same as width but corresp. to the height of the
                              figure

    """
    try:
        s = get_embed(file_owner_or_url, file_id=file_id, width=width,
                      height=height)

        # see if we are in the SageMath Cloud
        if sage_salvus:
            return sage_salvus.html(s, hide=False)
    except:
        pass
    if ipython_core_display:
        if file_id:
            plotly_domain = (
                    session.get_session_config().get('plotly_domain') or
                    get_config_file()['plotly_domain']
            )
            url = "{plotly_domain}/~{un}/{fid}".format(
                plotly_domain=plotly_domain,
                un=file_owner_or_url,
                fid=file_id)
        else:
            url = file_owner_or_url
        return PlotlyDisplay(url, width, height)
    else:
        if (get_config_defaults()['plotly_domain']
                != session.get_session_config()['plotly_domain']):
            feedback_contact = 'Visit support.plot.ly'
        else:

            # different domain likely means enterprise
            feedback_contact = 'Contact your On-Premise account executive'

        warnings.warn(
            "Looks like you're not using IPython or Sage to embed this "
            "plot. If you just want the *embed code*,\ntry using "
            "`get_embed()` instead."
            '\nQuestions? {}'.format(feedback_contact))


### graph_objs related tools ###


def get_graph_obj(obj, obj_type=None):
    """Returns a new graph object.

    OLD FUNCTION: this will *silently* strip out invalid pieces of the object.
    NEW FUNCTION: no striping of invalid pieces anymore - only raises error
        on unrecognized graph_objs
    """
    # TODO: Deprecate or move. #283
    from plotly.graph_objs import graph_objs
    try:
        cls = getattr(graph_objs, obj_type)
    except (AttributeError, KeyError):
        raise plotly.exceptions.PlotlyError(
            "'{}' is not a recognized graph_obj.".format(obj_type)
        )
    return cls(obj)


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


if ipython_core_display:
    class PlotlyDisplay(ipython_core_display.HTML):
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

# Default colours for finance charts
_DEFAULT_INCREASING_COLOR = '#3D9970'  # http://clrs.cc
_DEFAULT_DECREASING_COLOR = '#FF4136'

DIAG_CHOICES = ['scatter', 'histogram', 'box']
VALID_COLORMAP_TYPES = ['cat', 'seq']


class FigureFactory(object):

    @staticmethod
    def _deprecated(old_method, new_method=None):
        if new_method is None:
            # The method name stayed the same.
            new_method = old_method
        warnings.warn(
            'plotly.tools.FigureFactory.{} is deprecated. '
            'Use plotly.figure_factory.{}'.format(old_method, new_method)
        )

    @staticmethod
    def create_2D_density(*args, **kwargs):
        FigureFactory._deprecated('create_2D_density', 'create_2d_density')
        from plotly.figure_factory import create_2d_density
        return create_2d_density(*args, **kwargs)

    @staticmethod
    def create_annotated_heatmap(*args, **kwargs):
        FigureFactory._deprecated('create_annotated_heatmap')
        from plotly.figure_factory import create_annotated_heatmap
        return create_annotated_heatmap(*args, **kwargs)

    @staticmethod
    def create_candlestick(*args, **kwargs):
        FigureFactory._deprecated('create_candlestick')
        from plotly.figure_factory import create_candlestick
        return create_candlestick(*args, **kwargs)

    @staticmethod
    def create_dendrogram(*args, **kwargs):
        FigureFactory._deprecated('create_dendrogram')
        from plotly.figure_factory import create_dendrogram
        return create_dendrogram(*args, **kwargs)

    @staticmethod
    def create_distplot(*args, **kwargs):
        FigureFactory._deprecated('create_distplot')
        from plotly.figure_factory import create_distplot
        return create_distplot(*args, **kwargs)

    @staticmethod
    def create_facet_grid(*args, **kwargs):
        FigureFactory._deprecated('create_facet_grid')
        from plotly.figure_factory import create_facet_grid
        return create_facet_grid(*args, **kwargs)

    @staticmethod
    def create_gantt(*args, **kwargs):
        FigureFactory._deprecated('create_gantt')
        from plotly.figure_factory import create_gantt
        return create_gantt(*args, **kwargs)

    @staticmethod
    def create_ohlc(*args, **kwargs):
        FigureFactory._deprecated('create_ohlc')
        from plotly.figure_factory import create_ohlc
        return create_ohlc(*args, **kwargs)

    @staticmethod
    def create_quiver(*args, **kwargs):
        FigureFactory._deprecated('create_quiver')
        from plotly.figure_factory import create_quiver
        return create_quiver(*args, **kwargs)

    @staticmethod
    def create_scatterplotmatrix(*args, **kwargs):
        FigureFactory._deprecated('create_scatterplotmatrix')
        from plotly.figure_factory import create_scatterplotmatrix
        return create_scatterplotmatrix(*args, **kwargs)

    @staticmethod
    def create_streamline(*args, **kwargs):
        FigureFactory._deprecated('create_streamline')
        from plotly.figure_factory import create_streamline
        return create_streamline(*args, **kwargs)

    @staticmethod
    def create_table(*args, **kwargs):
        FigureFactory._deprecated('create_table')
        from plotly.figure_factory import create_table
        return create_table(*args, **kwargs)

    @staticmethod
    def create_trisurf(*args, **kwargs):
        FigureFactory._deprecated('create_trisurf')
        from plotly.figure_factory import create_trisurf
        return create_trisurf(*args, **kwargs)

    @staticmethod
    def create_violin(*args, **kwargs):
        FigureFactory._deprecated('create_violin')
        from plotly.figure_factory import create_violin
        return create_violin(*args, **kwargs)
