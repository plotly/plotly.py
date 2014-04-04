"""
exceptions
==========

A module that contains plotly's exception heirarchy.

"""


class PlotlyError(Exception):
    pass


class InvalidKeyError(PlotlyError):
    pass


class InvalidListItemError(PlotlyError):
    pass


class ConnectionError(PlotlyError):
    pass


class CredentialError(PlotlyError):
    pass


class AccountError(PlotlyError):
    pass


class RateLimitError(PlotlyError):
    pass
