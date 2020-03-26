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

from _plotly_utils import optional_imports
import _plotly_utils.exceptions
from _plotly_utils.files import ensure_writable_plotly_dir

from chart_studio import session, utils
from chart_studio.files import CONFIG_FILE, CREDENTIALS_FILE, FILE_CONTENT

ipython_core_display = optional_imports.get_module("IPython.core.display")
ipython_display = optional_imports.get_module("IPython.display")

sage_salvus = optional_imports.get_module("sage_salvus")


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
        warnings.warn(
            "Looks like you don't have 'read-write' permission to "
            "your 'home' ('~') directory or to our '~/.plotly' "
            "directory. That means plotly's python api can't setup "
            "local configuration files. No problem though! You'll "
            "just have to sign-in using 'plotly.plotly.sign_in()'. "
            "For help with that: 'help(plotly.plotly.sign_in)'."
            "\nQuestions? Visit https://support.plotly.com"
        )


### credentials tools ###


def set_credentials_file(
    username=None,
    api_key=None,
    stream_ids=None,
    proxy_username=None,
    proxy_password=None,
):
    """Set the keyword-value pairs in `~/.plotly_credentials`.

    :param (str) username: The username you'd use to sign in to Plotly
    :param (str) api_key: The api key associated with above username
    :param (list) stream_ids: Stream tokens for above credentials
    :param (str) proxy_username: The un associated with with your Proxy
    :param (str) proxy_password: The pw associated with your Proxy un

    """
    if not ensure_writable_plotly_dir():
        raise _plotly_utils.exceptions.PlotlyError(
            "You don't have proper file permissions " "to run this function."
        )
    ensure_local_plotly_files()  # make sure what's there is OK
    credentials = get_credentials_file()
    if isinstance(username, six.string_types):
        credentials["username"] = username
    if isinstance(api_key, six.string_types):
        credentials["api_key"] = api_key
    if isinstance(proxy_username, six.string_types):
        credentials["proxy_username"] = proxy_username
    if isinstance(proxy_password, six.string_types):
        credentials["proxy_password"] = proxy_password
    if isinstance(stream_ids, (list, tuple)):
        credentials["stream_ids"] = stream_ids
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


def set_config_file(
    plotly_domain=None,
    plotly_streaming_domain=None,
    plotly_api_domain=None,
    plotly_ssl_verification=None,
    plotly_proxy_authorization=None,
    world_readable=None,
    sharing=None,
    auto_open=None,
):
    """Set the keyword-value pairs in `~/.plotly/.config`.

    :param (str) plotly_domain: ex - https://plotly.com
    :param (str) plotly_streaming_domain: ex - stream.plotly.com
    :param (str) plotly_api_domain: ex - https://api.plotly.com
    :param (bool) plotly_ssl_verification: True = verify, False = don't verify
    :param (bool) plotly_proxy_authorization: True = use plotly proxy auth creds
    :param (bool) world_readable: True = public, False = private

    """
    if not ensure_writable_plotly_dir():
        raise _plotly_utils.exceptions.PlotlyError(
            "You don't have proper file permissions " "to run this function."
        )
    ensure_local_plotly_files()  # make sure what's there is OK
    utils.validate_world_readable_and_sharing_settings(
        {"sharing": sharing, "world_readable": world_readable}
    )

    settings = get_config_file()
    if isinstance(plotly_domain, six.string_types):
        settings["plotly_domain"] = plotly_domain
    elif plotly_domain is not None:
        raise TypeError("plotly_domain should be a string")
    if isinstance(plotly_streaming_domain, six.string_types):
        settings["plotly_streaming_domain"] = plotly_streaming_domain
    elif plotly_streaming_domain is not None:
        raise TypeError("plotly_streaming_domain should be a string")
    if isinstance(plotly_api_domain, six.string_types):
        settings["plotly_api_domain"] = plotly_api_domain
    elif plotly_api_domain is not None:
        raise TypeError("plotly_api_domain should be a string")
    if isinstance(plotly_ssl_verification, (six.string_types, bool)):
        settings["plotly_ssl_verification"] = plotly_ssl_verification
    elif plotly_ssl_verification is not None:
        raise TypeError("plotly_ssl_verification should be a boolean")
    if isinstance(plotly_proxy_authorization, (six.string_types, bool)):
        settings["plotly_proxy_authorization"] = plotly_proxy_authorization
    elif plotly_proxy_authorization is not None:
        raise TypeError("plotly_proxy_authorization should be a boolean")
    if isinstance(auto_open, bool):
        settings["auto_open"] = auto_open
    elif auto_open is not None:
        raise TypeError("auto_open should be a boolean")

    # validate plotly_domain and plotly_api_domain
    utils.validate_plotly_domains(
        {"plotly_domain": plotly_domain, "plotly_api_domain": plotly_api_domain}
    )

    if isinstance(world_readable, bool):
        settings["world_readable"] = world_readable
        settings.pop("sharing")
    elif world_readable is not None:
        raise TypeError("Input should be a boolean")
    if isinstance(sharing, six.string_types):
        settings["sharing"] = sharing
    elif sharing is not None:
        raise TypeError("sharing should be a string")
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
    f = open(CONFIG_FILE, "w")
    f.close()
    ensure_local_plotly_files()  # put the defaults back


### embed tools ###
def _get_embed_url(file_owner_or_url, file_id=None):
    plotly_rest_url = (
        session.get_session_config().get("plotly_domain")
        or get_config_file()["plotly_domain"]
    )
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
        urlsplit = six.moves.urllib.parse.urlparse(url)
        file_owner = urlsplit.path.split("/")[1].split("~")[1]
        file_id = urlsplit.path.split("/")[2]

        # to check for share_key we check urlsplit.query
        query_dict = six.moves.urllib.parse.parse_qs(urlsplit.query)
        if query_dict:
            share_key = query_dict["share_key"][-1]
        else:
            share_key = ""
    else:
        file_owner = file_owner_or_url
        share_key = ""
    try:
        test_if_int = int(file_id)
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

    if share_key is "":
        return "{plotly_rest_url}/~{file_owner}/{file_id}.embed".format(
            plotly_rest_url=plotly_rest_url, file_owner=file_owner, file_id=file_id
        )
    else:
        return (
            "{plotly_rest_url}/~{file_owner}/" "{file_id}.embed?share_key={share_key}"
        ).format(
            plotly_rest_url=plotly_rest_url,
            file_owner=file_owner,
            file_id=file_id,
            share_key=share_key,
        )


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
    embed_url = _get_embed_url(file_owner_or_url, file_id)

    return (
        '<iframe id="igraph" scrolling="no" style="border:none;" '
        'seamless="seamless" '
        'src="{embed_url}" '
        'height="{iframe_height}" width="{iframe_width}">'
        "</iframe>"
    ).format(embed_url=embed_url, iframe_height=height, iframe_width=width)


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
        s = get_embed(file_owner_or_url, file_id=file_id, width=width, height=height)

        # see if we are in the SageMath Cloud
        if sage_salvus:
            return sage_salvus.html(s, hide=False)
    except:
        pass
    if ipython_core_display:
        if file_id:
            plotly_domain = (
                session.get_session_config().get("plotly_domain")
                or get_config_file()["plotly_domain"]
            )
            url = "{plotly_domain}/~{un}/{fid}".format(
                plotly_domain=plotly_domain, un=file_owner_or_url, fid=file_id
            )
        else:
            url = file_owner_or_url

        embed_url = _get_embed_url(url, file_id)
        return ipython_display.IFrame(embed_url, width, height)
    else:
        if (
            get_config_defaults()["plotly_domain"]
            != session.get_session_config()["plotly_domain"]
        ):
            feedback_contact = "Visit support.plotly.com"
        else:

            # different domain likely means enterprise
            feedback_contact = "Contact your On-Premise account executive"

        warnings.warn(
            "Looks like you're not using IPython or Sage to embed this "
            "plot. If you just want the *embed code*,\ntry using "
            "`get_embed()` instead."
            "\nQuestions? {}".format(feedback_contact)
        )
