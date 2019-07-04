from base64 import b64encode

from requests.compat import builtin_str, is_py2


def _to_native_string(string, encoding):
    if isinstance(string, builtin_str):
        return string
    if is_py2:
        return string.encode(encoding)
    return string.decode(encoding)


def to_native_utf8_string(string):
    return _to_native_string(string, "utf-8")


def to_native_ascii_string(string):
    return _to_native_string(string, "ascii")


def basic_auth(username, password):
    """
    Creates the basic auth value to be used in an authorization header.

    This is mostly copied from the requests library.

    :param (str) username: A Plotly username.
    :param (str) password: The password for the given Plotly username.
    :returns: (str) An 'authorization' header for use in a request header.

    """
    if isinstance(username, str):
        username = username.encode("latin1")

    if isinstance(password, str):
        password = password.encode("latin1")

    return "Basic " + to_native_ascii_string(
        b64encode(b":".join((username, password))).strip()
    )
