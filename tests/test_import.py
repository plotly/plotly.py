from plotly.graph_objects import Scatter


def test_trivial():
    assert Scatter().to_plotly_json() == {"type": "scatter"}
