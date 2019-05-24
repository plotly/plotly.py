import plotly
plotly_plot = plotly.offline.plot
import os
import shutil

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
    trace_0 = go.Scatter(
        x=random_x,
        y=random_y_0,
        mode='markers',
        name='Above',
    )

    data = [trace_0]
    res = plotly.offline.plot(data)


def test_monkey_patching():
    from plotly.io._sg_scraper import plotly_sg_scraper
    # test that monkey-patching worked ok
    assert plotly_plot != plotly.offline.plot
    # Use dummy values for arguments of plotly_sg_scraper
    block = '' # we don't need actually code
    import tempfile
    tempdir = tempfile.mkdtemp()
    gallery_conf = {'src_dir':tempdir,
                    'examples_dirs':'plotly/tests/test_io'}
    names = iter(['0', '1', '2'])
    block_vars = {'image_path_iterator':names}
    execute_plotly_example()
    res = plotly_sg_scraper(block, block_vars, gallery_conf)
    shutil.rmtree(tempdir)
    assert ".. raw:: html" in res
    plotly.offline.plot = plotly_plot
    assert plotly_plot == plotly.offline.plot
