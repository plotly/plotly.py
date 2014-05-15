"""
exceptions
==========

A module that contains plotly's exception heirarchy.

"""


## Base Plotly Error ##

class PlotlyError(Exception):
    def __init__(self, message, info=None):
        super(PlotlyError, self).__init__(message)
        if info is None:
            info = dict()
        self.info = info


## Graph Objects Errors ##

class PlotlyGraphObjectError(PlotlyError):
    pass


class PlotlyDictKeyError(PlotlyGraphObjectError):
    pass


class PlotlyDictValueError(PlotlyGraphObjectError):
    pass


class PlotlyListItemError(PlotlyGraphObjectError):
    pass


# todo, do we need this?
# class PlotlyGraphObjectInstantiationError(PlotlyGraphObjectError):
#     pass


# class PlotlyInvalidKeyError(PlotlyError):
#     pass
#
#
# class PlotlyInvalidListItemError(PlotlyError):
#     pass


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
