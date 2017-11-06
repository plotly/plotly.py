from __future__ import absolute_import

from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs

import math
import copy
from numbers import Number

pd = optional_imports.get_module('pandas')


def create_bullet(df):
    """
    Returns figure for bullet chart.

    :param (pd.DataFrame) df:

    """
    if not pd:
        raise exceptions.ImportError(
            "'pandas' must be imported for this figure_factory."
        )

    if not isinstance(df, pd.DataFrame):
        raise exceptions.PlotlyError(
            "You must input a pandas DataFrame."
        )
