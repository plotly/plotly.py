import plotly.express as px
import plotly.graph_objects as go
from numpy.testing import assert_equal
import numpy as np
import pandas as pd
import pytest


def _compare_legend_to_column_name(name_column, name_from_fig):
    """Compare legend title name to the name given to it
    in "names" value to see if is equal to it and not None.
    """
    assert_equal(name_from_fig, name_column)
    assert name_from_fig


def test_pie_like_px():
    # Pie
    data_name = "col1"
    names_name = "col2"
    df = pd.DataFrame(data={data_name: [3, 2, 1], names_name: [1, 2, 4]})
    fig = px.pie(
        df, values=data_name, names=names_name, title="Population of European continent"
    )
    _compare_legend_to_column_name(names_name, fig.layout.legend.title.text)
