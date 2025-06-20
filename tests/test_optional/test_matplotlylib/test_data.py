import pytest

from plotly import optional_imports
from ...test_optional.optional_utils import run_fig
from ...test_optional.test_matplotlylib.data.data import D

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib.pyplot as plt


@pytest.mark.skip
def test_line_data():
    fig, ax = plt.subplots()
    ax.plot(D["x1"], D["y1"])
    renderer = run_fig(fig)
    for xi, xf, yi, yf in zip(
        renderer.plotly_fig["data"][0]["x"],
        D["x1"],
        renderer.plotly_fig["data"][0]["y"],
        D["y1"],
    ):
        assert xi == xf, (
            str(renderer.plotly_fig["data"][0]["x"]) + " is not " + str(D["x1"])
        )
        assert yi == yf, (
            str(renderer.plotly_fig["data"][0]["y"]) + " is not " + str(D["y1"])
        )


@pytest.mark.skip
def test_lines_data():
    fig, ax = plt.subplots()
    ax.plot(D["x1"], D["y1"])
    ax.plot(D["x2"], D["y2"])
    renderer = run_fig(fig)
    for xi, xf, yi, yf in zip(
        renderer.plotly_fig["data"][0]["x"],
        D["x1"],
        renderer.plotly_fig["data"][0]["y"],
        D["y1"],
    ):
        assert xi == xf, (
            str(renderer.plotly_fig["data"][0]["x"]) + " is not " + str(D["x1"])
        )
        assert yi == yf, (
            str(renderer.plotly_fig["data"][0]["y"]) + " is not " + str(D["y1"])
        )
    for xi, xf, yi, yf in zip(
        renderer.plotly_fig["data"][1]["x"],
        D["x2"],
        renderer.plotly_fig["data"][1]["y"],
        D["y2"],
    ):
        assert xi == xf, (
            str(renderer.plotly_fig["data"][1]["x"]) + " is not " + str(D["x2"])
        )
        assert yi == yf, (
            str(renderer.plotly_fig["data"][0]["y"]) + " is not " + str(D["y2"])
        )


@pytest.mark.skip
def test_bar_data():
    fig, ax = plt.subplots()
    ax.bar(D["x1"], D["y1"])
    renderer = run_fig(fig)
    for yi, yf in zip(renderer.plotly_fig["data"][0]["y"], D["y1"]):
        assert yi == yf, (
            str(renderer.plotly_fig["data"][0]["y"]) + " is not " + str(D["y1"])
        )


@pytest.mark.skip
def test_bars_data():
    fig, ax = plt.subplots()
    ax.bar(D["x1"], D["y1"], color="r")
    ax.barh(D["x2"], D["y2"], color="b")
    renderer = run_fig(fig)
    for yi, yf in zip(renderer.plotly_fig["data"][0]["y"], D["y1"]):
        assert yi == yf, (
            str(renderer.plotly_fig["data"][0]["y"]) + " is not " + str(D["y1"])
        )
    for xi, yf in zip(renderer.plotly_fig["data"][1]["x"], D["y2"]):
        assert xi == yf, (
            str(renderer.plotly_fig["data"][1]["x"]) + " is not " + str(D["y2"])
        )
