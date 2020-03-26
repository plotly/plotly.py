"""
exceptions
==========

A module that contains plotly's exception hierarchy.

"""
from __future__ import absolute_import

from chart_studio.api.utils import to_native_utf8_string


# Base Plotly Error
from _plotly_utils.exceptions import PlotlyError


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
    "Questions? chris@plotly.com"
)

NON_UNIQUE_COLUMN_MESSAGE = (
    "Yikes, plotly grids currently "
    "can't have duplicate column names. Rename "
    'the column "{0}" and try again.'
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
            "For more help, see https://plotly.com/python.\n"
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
