import sys
from . import version_skip


@version_skip
def test_dependencies_not_imported():

    # Check that creating a figure without using numpy and pandas does not result in
    # the import of numpy and pandas, even if they are installed.
    assert "plotly" not in sys.modules
    assert "numpy" not in sys.modules
    assert "pandas" not in sys.modules

    import plotly.graph_objects as go

    fig = go.Figure().add_scatter(x=[0], y=[1])
    fig.to_json()

    assert "plotly" in sys.modules
    assert "numpy" not in sys.modules
    assert "pandas" not in sys.modules

    # check that numpy is installed
    import numpy as np

    fig = go.Figure().add_scatter(x=np.array([0]), y=np.array([1]))
    fig.to_json()
    assert "numpy" in sys.modules
    assert "pandas" not in sys.modules

    # check that pandas is installed
    import pandas as pd

    fig = go.Figure().add_scatter(x=pd.Series([0]), y=pd.Series([1]))
    fig.to_json()
    assert "pandas" in sys.modules
