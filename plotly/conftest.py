import os
from pathlib import Path


def pytest_ignore_collect(collection_path: Path):
    # Ignored files, most of them are raising a chart studio error
    ignored_paths = [
        "exploding_module.py",
        "chunked_requests.py",
        "v2.py",
        "v1.py",
        "presentation_objs.py",
        "widgets.py",
        "dashboard_objs.py",
        "grid_objs.py",
        "config.py",
        "presentation_objs.py",
        "session.py",
    ]
    path_str = str(collection_path)
    if (
        collection_path.name in ignored_paths
        or "plotly/plotly/plotly/__init__.py" in path_str
        or "plotly/api/utils.py" in path_str
    ):
        return True
