"""
exceptions
==========

A module that contains plotly's exception hierarchy.

"""
from __future__ import absolute_import

from plotly.api.utils import to_native_utf8_string


# Base Plotly Error
class PlotlyError(Exception):
    pass


class InputError(PlotlyError):
    pass


class PlotlyRequestError(PlotlyError):
    """General API error. Raised for *all* failed requests."""

    def __init__(self, message, status_code, content):
        self.message = to_native_utf8_string(message)
        self.status_code = status_code
        self.content = content

    def __str__(self):
        return self.message


# Grid Errors
COLUMN_NOT_YET_UPLOADED_MESSAGE = (
    "Hm... it looks like your column '{column_name}' hasn't "
    "been uploaded to Plotly yet. You need to upload your "
    "column to Plotly before you can assign it to '{reference}'.\n"
    "To upload, try `plotly.plotly.grid_objs.upload` or "
    "`plotly.plotly.grid_objs.append_column`.\n"
    "Questions? chris@plot.ly"
)

NON_UNIQUE_COLUMN_MESSAGE = (
    "Yikes, plotly grids currently "
    "can't have duplicate column names. Rename "
    "the column \"{0}\" and try again."
)


class PlotlyEmptyDataError(PlotlyError):
    pass


# Graph Objects Errors
class PlotlyGraphObjectError(PlotlyError):
    def __init__(self, message='', path=(), notes=()):
        """
        General graph object error for validation failures.

        :param (str|unicode) message: The error message.
        :param (iterable) path: A path pointing to the error.
        :param notes: Add additional notes, but keep default exception message.

        """
        self.message = message
        self.plain_message = message  # for backwards compat
        self.path = list(path)
        self.notes = notes
        super(PlotlyGraphObjectError, self).__init__(message)

    def __str__(self):
        """This is called by Python to present the error message."""
        format_dict = {
            'message': self.message,
            'path': '[' + ']['.join(repr(k) for k in self.path) + ']',
            'notes': '\n'.join(self.notes)
        }
        return ('{message}\n\nPath To Error: {path}\n\n{notes}'
                .format(**format_dict))


class PlotlyDictKeyError(PlotlyGraphObjectError):
    def __init__(self, obj, path, notes=()):
        """See PlotlyGraphObjectError.__init__ for param docs."""
        format_dict = {'attribute': path[-1], 'object_name': obj._name}
        message = ("'{attribute}' is not allowed in '{object_name}'"
                   .format(**format_dict))
        notes = [obj.help(return_help=True)] + list(notes)
        super(PlotlyDictKeyError, self).__init__(
            message=message, path=path, notes=notes
        )


class PlotlyDictValueError(PlotlyGraphObjectError):
    def __init__(self, obj, path, notes=()):
        """See PlotlyGraphObjectError.__init__ for param docs."""
        format_dict = {'attribute': path[-1], 'object_name': obj._name}
        message = ("'{attribute}' has invalid value inside '{object_name}'"
                   .format(**format_dict))
        notes = [obj.help(path[-1], return_help=True)] + list(notes)
        super(PlotlyDictValueError, self).__init__(
            message=message, notes=notes, path=path
        )


class PlotlyListEntryError(PlotlyGraphObjectError):
    def __init__(self, obj, path, notes=()):
        """See PlotlyGraphObjectError.__init__ for param docs."""
        format_dict = {'index': path[-1], 'object_name': obj._name}
        message = ("Invalid entry found in '{object_name}' at index, '{index}'"
                   .format(**format_dict))
        notes = [obj.help(return_help=True)] + list(notes)
        super(PlotlyListEntryError, self).__init__(
            message=message, path=path, notes=notes
        )


class PlotlyDataTypeError(PlotlyGraphObjectError):
    def __init__(self, obj, path, notes=()):
        """See PlotlyGraphObjectError.__init__ for param docs."""
        format_dict = {'index': path[-1], 'object_name': obj._name}
        message = ("Invalid entry found in '{object_name}' at index, '{index}'"
                   .format(**format_dict))
        note = "It's invalid because it doesn't contain a valid 'type' value."
        notes = [note] + list(notes)
        super(PlotlyDataTypeError, self).__init__(
            message=message, path=path, notes=notes
        )


# Local Config Errors
class PlotlyLocalError(PlotlyError):
    pass


class PlotlyLocalCredentialsError(PlotlyLocalError):
    def __init__(self):
        message = (
            "\n"
            "Couldn't find a 'username', 'api-key' pair for you on your local "
            "machine. To sign in temporarily (until you stop running Python), "
            "run:\n"
            ">>> import plotly.plotly as py\n"
            ">>> py.sign_in('username', 'api_key')\n\n"
            "Even better, save your credentials permanently using the 'tools' "
            "module:\n"
            ">>> import plotly.tools as tls\n"
            ">>> tls.set_credentials_file(username='username', "
            "api_key='api-key')\n\n"
            "For more help, see https://plot.ly/python.\n"
        )
        super(PlotlyLocalCredentialsError, self).__init__(message)


# Server Errors
class PlotlyServerError(PlotlyError):
    pass


class PlotlyConnectionError(PlotlyServerError):
    pass


class PlotlyCredentialError(PlotlyServerError):
    pass


class PlotlyAccountError(PlotlyServerError):
    pass


class PlotlyRateLimitError(PlotlyServerError):
    pass
