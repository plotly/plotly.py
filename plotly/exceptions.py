"""
exceptions
==========

A module that contains plotly's exception heirarchy.

"""


class PlotlyError(Exception):
    pass

class PlotlyInstantiationError(PlotlyError):
    pass

class PlotlyInvalidKeyError(PlotlyError):
    pass


class PlotlyInvalidListItemError(PlotlyError):
    pass


class PlotlyConnectionError(PlotlyError):
    pass


class PlotlyCredentialError(PlotlyError):
    pass


class PlotlyAccountError(PlotlyError):
    pass


class PlotlyRateLimitError(PlotlyError):
    pass
