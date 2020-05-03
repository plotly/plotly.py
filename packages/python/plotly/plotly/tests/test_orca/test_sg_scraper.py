import plotly
import os
import shutil
import pytest


# Fixtures
# --------
@pytest.fixture()
def setup():
    # Reset orca state
    plotly.io.orca.config.restore_defaults(reset_server=False)


here = os.path.dirname(os.path.abspath(__file__))


# Run setup before every test function in this file
pytestmark = pytest.mark.usefixtures("setup")


def execute_plotly_example():
    """
    Some typical code which would go inside a gallery example.
    """
    import plotly.graph_objs as go

    # Create random data with numpy
    import numpy as np

    N = 200
    random_x = np.random.randn(N)
    random_y_0 = np.random.randn(N)
    random_y_1 = np.random.randn(N) - 1

    # Create traces
    trace_0 = go.Scatter(x=random_x, y=random_y_0, mode="markers", name="Above")

    fig = go.Figure(data=[trace_0])
    plotly.io.show(fig)


def test_scraper():
    from plotly.io._sg_scraper import plotly_sg_scraper

    # test that monkey-patching worked ok
    assert plotly.io.renderers.default == "sphinx_gallery_png"
    # Use dummy values for arguments of plotly_sg_scraper
    block = ""  # we don't need actually code
    import tempfile

    tempdir = tempfile.mkdtemp()
    gallery_conf = {"src_dir": tempdir, "examples_dirs": here}
    names = iter(["0", "1", "2"])
    block_vars = {
        "image_path_iterator": names,
        "src_file": os.path.join(here, "plot_example.py"),
    }
    execute_plotly_example()
    res = plotly_sg_scraper(block, block_vars, gallery_conf)
    shutil.rmtree(tempdir)
    assert ".. raw:: html" in res
