# ruff: noqa: F401 F403 F405
"""
Regression test for plotly/plotly.py#5849.

The optional ``FigureWidget`` import block (the ``try: import ipywidgets`` /
``missing_*`` fallback) must live only in ``plotly/graph_objs/__init__.py``.
``plotly/graph_objects/__init__.py`` must re-export ``FigureWidget`` from
``graph_objs`` like every other class, instead of duplicating that block.

These tests fail on unmodified master, where the block is emitted into both
generated files.
"""

import os
import os.path as opath
import subprocess
import sys

import plotly
import plotly.graph_objects as go
import plotly.graph_objs as go2
from plotly.missing_anywidget import FigureWidget as FigureWidgetMissingAnywidget


def test_figurewidget_is_reexported_from_graph_objs():
    # (a) graph_objects.FigureWidget is the same object as
    # graph_objs.FigureWidget: it is re-exported, not imported separately.
    assert go.FigureWidget is go2.FigureWidget


def test_figurewidget_fallback_when_ipywidgets_missing():
    # (b) With the ipywidgets import forced to fail, graph_objects.FigureWidget
    # still resolves to the missing_* fallback owned by graph_objs. This runs
    # in a subprocess so it holds whether or not ipywidgets is installed.
    script = (
        "import sys\n"
        "sys.modules['ipywidgets'] = None\n"
        "import plotly.graph_objects as go\n"
        "from plotly.missing_anywidget import FigureWidget as Missing\n"
        "assert go.FigureWidget is Missing, "
        "f'expected missing_* fallback, got {go.FigureWidget!r}'\n"
        "print('ok')\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"forced-failure fallback check failed:\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )
    assert "ok" in result.stdout


def test_no_duplicate_ipywidgets_block_in_graph_objects():
    # (c) The optional ipywidgets import block must not be duplicated in
    # graph_objects/__init__.py; it belongs only in graph_objs/__init__.py.
    plotly_root = opath.dirname(plotly.__file__)
    go_init = opath.join(plotly_root, "graph_objects", "__init__.py")
    with open(go_init) as f:
        go_source = f.read()
    assert "import ipywidgets" not in go_source, (
        "graph_objects/__init__.py still contains a duplicated "
        "optional ipywidgets import block"
    )
    assert "missing_anywidget" not in go_source, (
        "graph_objects/__init__.py still references the missing_* fallback "
        "directly instead of re-exporting FigureWidget from graph_objs"
    )

    # The block must still be present in graph_objs/__init__.py.
    go2_init = opath.join(plotly_root, "graph_objs", "__init__.py")
    with open(go2_init) as f:
        go2_source = f.read()
    assert "import ipywidgets" in go2_source
    assert "missing_anywidget" in go2_source
