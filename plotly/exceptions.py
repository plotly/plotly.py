"""
exceptions
==========

A module that contains plotly's exception heirarchy.

"""


def PlotlyError(Exception):
    pass


def InvalidKeyError(PlotlyError):
    pass


def ConnectionError(PlotlyError):
    pass


def CredentialError(PlotlyError):
    pass


def  AccountError(PlotlyError):
    pass


def RateLimitError(PlotlyError):
    pass
