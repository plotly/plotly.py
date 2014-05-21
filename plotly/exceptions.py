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


## Base Plotly Error ##

class PlotlyError(Exception):
    pass


## Graph Objects Errors ##

class PlotlyGraphObjectError(PlotlyError):
    def __init__(self, message='', path=None, notes=None, plain_message=''):
        self.message = message
        self.plain_message=plain_message
        if isinstance(path, list):
            self.path = path
        elif path is None:
            self.path = []
        else:
            self.path = [path]
        if isinstance(notes, list):
            self.notes = notes
        elif notes is None:
            self.notes = []
        else:
            self.notes = [notes]
        super(PlotlyGraphObjectError, self).__init__(message)
        self.prepare()

    def add_note(self, note):
        if isinstance(note, list):
            self.notes += note
        else:
            self.notes += [note]

    def add_to_error_path(self, path):
        if isinstance(path, list):
            self.path = path + self.path
        else:
            self.path = [path] + self.path

    def prepare(self):
        message = self.message
        message += "\n\nPath To Error:\n["
        for iii, key in enumerate(self.path):
            message += repr(key)
            if iii < len(self.path) - 1:
                message += "]["
        message += "]"
        if len(self.notes):
            message += "\n\nAdditional Notes:\n{}".format("\n".join(self.notes))
        if len(self.args) > 1:
            self.args = (message, self.args[1:][0])
        else:
            self.args = message,


class PlotlyDictKeyError(PlotlyGraphObjectError):
    def __init__(self, obj='', key='', **kwargs):
        message = (
            "Invalid key, '{key}', for class, '{obj_name}'.\n\nRun "
            "'help(plotly.graph_objs.{obj_name})' for more information."
            "".format(key=key, obj_name=obj.__class__.__name__)
        )
        plain_message="invalid key, '{}', in dictionary".format(key)
        super(PlotlyDictKeyError, self).__init__(message=message,
                                                 path=[key],
                                                 plain_message=plain_message,
                                                 **kwargs)


class PlotlyDictValueError(PlotlyGraphObjectError):
    def __init__(self, obj='', key='', value='', val_types='', **kwargs):
        message = (
            "Invalid value type, '{value_name}', associated with key, "
            "'{key}', for class, '{obj_name}'.\nValid types for this key "
            "are:\n '{val_types}'.\n\nRun 'help(plotly.graph_objs.{obj_name})' "
            "for more information.".format(key=key,
                                           value_name=value.__class__.__name__,
                                           val_types=val_types,
                                           obj_name=obj.__class__.__name__)
        )
        plain_message = ("invalid value associated with key, '{}', in "
                         "dictionary".format(key))
        super(PlotlyDictValueError, self).__init__(message=message,
                                                   plain_message=plain_message,
                                                   path=[key],
                                                   **kwargs)


class PlotlyListEntryError(PlotlyGraphObjectError):
    def __init__(self, obj='', index='', entry='', **kwargs):
        message = (
            "The entry at index, '{}', is invalid in a '{}' object"
            "".format(index, obj.__class__.__name__)
        )
        plain_message = (
            "The entry at index, '{}', is invalid."
            "".format(index)
        )
        super(PlotlyListEntryError, self).__init__(message=message,
                                                   plain_message=plain_message,
                                                   path=[index],
                                                   **kwargs)


class PlotlyDataTypeError(PlotlyGraphObjectError):
    def __init__(self, obj='', index='', **kwargs):
        message = (
                "The entry at index, '{}', is invalid because it does not "
                "contain a valid 'type' key-value. This is required for valid "
                "'{}' lists.".format(index, obj.__class__.__name__)
        )
        plain_message = (
                "The entry at index, '{}', is invalid because it does not "
                "contain a valid 'type' key-value. This is required for "
                "valid data lists.".format(index))
        super(PlotlyDataTypeError, self).__init__(message=message,
                                                  plain_message=plain_message,
                                                  path=[index],
                                                  **kwargs)


## Local Config Errors ##

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


## Server Errors ##

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
