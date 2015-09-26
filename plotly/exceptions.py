"""
exceptions
==========

A module that contains plotly's exception hierarchy.

message (required!) (should be root message + caller message)
info: (required!)
    path_to_error (required!)
    minimal_message (required!)

- minimal_message is set inside this module, should not be set elsewhere

- message is set inside this module, should not be set elsewhere


"""
import json


# Base Plotly Error
class PlotlyError(Exception):
    pass


class InputError(PlotlyError):
    pass


class PlotlyRequestError(PlotlyError):
    def __init__(self, requests_exception):
        self.status_code = requests_exception.response.status_code
        self.HTTPError = requests_exception
        content_type = requests_exception.response.headers['content-type']
        if 'json' in content_type:
            content = requests_exception.response.content
            if content != '':
                res_payload = json.loads(
                    requests_exception.response.content.decode('utf8')
                )
                if 'detail' in res_payload:
                    self.message = res_payload['detail']
                else:
                    self.message = ''
            else:
                self.message = ''
        elif content_type == 'text/plain':
            self.message = requests_exception.response.content
        else:
            try:
                self.message = requests_exception.message
            except AttributeError:
                self.message = 'unknown error'

    def __str__(self):
        return self.message


# Grid Errors #
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

# Would Cause Server Errors


class PlotlyEmptyDataError(PlotlyError):
    pass


# Graph Objects Errors
class PlotlyGraphObjectError(PlotlyError):
    def __init__(self, message='', path=(), note='', plain_message=''):
        self.message = message
        self.plain_message = plain_message
        self.path = list(path)
        self.note = note
        super(PlotlyGraphObjectError, self).__init__(message)

    def __str__(self):
        format_dict = {
            'message': self.message,
            'path': '[' + ']['.join(repr(k) for k in self.path) + ']',
            'note': self.note
        }
        message = '{message}\n\nPath To Error: {path}'.format(**format_dict)
        if format_dict['note']:
            message += '\n\nAdditional Notes:\n {note}'.format(**format_dict)
        return message


class PlotlyDictKeyError(PlotlyGraphObjectError):
    def __init__(self, obj, path=(), **kwargs):
        key = path[-1]
        message = (
            "Invalid key, '{key}', for class, '{obj_name}'.\n\nRun "
            "'help(plotly.graph_objs.{obj_name})' for more information."
            "".format(key=key, obj_name=obj.__class__.__name__)
        )
        plain_message = ("Invalid key, '{key}', found in '{obj}' object"
                         "".format(key=key, obj=obj.__class__.__name__))
        super(PlotlyDictKeyError, self).__init__(message=message,
                                                 path=path,
                                                 plain_message=plain_message,
                                                 **kwargs)


class PlotlyDictValueError(PlotlyGraphObjectError):
    def __init__(self, obj, value, val_types, path=(), **kwargs):
        key = path[-1]
        message = (
            "Invalid value type, '{value_name}', associated with key, "
            "'{key}', for class, '{obj_name}'.\nValid types for this key "
            "are:\n '{val_types}'.\n\n"
            "Run 'help(plotly.graph_objs.{obj_name})' for more information."
            .format(key=key, value_name=value.__class__.__name__,
                    val_types=val_types, obj_name=obj.__class__.__name__)
        )
        plain_message = ("Invalid value found in '{obj}' associated with key, "
                         "'{key}'".format(key=key, obj=obj.__class__.__name__))
        super(PlotlyDictValueError, self).__init__(message=message,
                                                   plain_message=plain_message,
                                                   path=path,
                                                   **kwargs)


class PlotlyListEntryError(PlotlyGraphObjectError):
    def __init__(self, obj, path=(), **kwargs):
        index = path[-1]
        message = (
            "The entry at index, '{0}', is invalid in a '{1}' object"
            "".format(index, obj.__class__.__name__)
        )
        plain_message = (
            "Invalid entry found in '{obj}' object at index, '{index}'."
            "".format(obj=obj.__class__.__name__, index=index)
        )
        super(PlotlyListEntryError, self).__init__(message=message,
                                                   plain_message=plain_message,
                                                   path=path,
                                                   **kwargs)


class PlotlyDataTypeError(PlotlyGraphObjectError):
    def __init__(self, obj, path=(), **kwargs):
        index = path[-1]
        message = (
                "The entry at index, '{0}', is invalid because it does not "
                "contain a valid 'type' key-value. This is required for valid "
                "'{1}' lists.".format(index, obj.__class__.__name__)
        )
        plain_message = (
                "Invalid entry found in 'data' object at index, '{0}'. It "
                "does not contain a valid 'type' key, required for 'data' "
                "lists.".format(index))
        super(PlotlyDataTypeError, self).__init__(message=message,
                                                  plain_message=plain_message,
                                                  path=path,
                                                  **kwargs)


# Local Config Errors
class PlotlyLocalError(PlotlyError):
    pass


class PlotlyLocalCredentialsError(PlotlyLocalError):
    def __init__(self):
        message = ("\n"
            "Couldn't find a 'username', 'api-key' pair for you on your local "
            "machine. To sign in temporarily (until you stop running Python), "
            "run:\n"
            ">>> import plotly.plotly as py\n"
            ">>> py.sign_in('username', 'api_key')\n\n"
            "Even better, save your credentials permanently using the 'tools' "
            "module:\n"
            ">>> import plotly.tools as tls\n"
            ">>> tls.set_credentials_file(username='username', api_key='api-key')\n\n"
            "For more help, see https://plot.ly/python.\n")
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
