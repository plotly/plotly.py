import sys
from . import version_skip


@version_skip
def test_lazy_imports():

    # plotly not imported yet
    assert "plotly" not in sys.modules

    # Import top-level plotly module
    import plotly

    assert "plotly" in sys.modules

    # Check that submodules are not auto-imported, but can be be accessed using
    # attribute syntax
    submodules = ["graph_objs", "io"]
    for m in submodules:
        module_str = "plotly." + m
        assert module_str not in sys.modules

        getattr(plotly, m)
        assert module_str in sys.modules

    # Check that constructing and serializing empty figure doesn't auto-import
    # nested graph objects
    plotly.graph_objects.Figure().to_json()
    submodules = [("layout", "title"), ("scatter", "marker"), ("scattergl", "marker")]
    for module_parts in submodules:
        module_str = "plotly.graph_objs." + ".".join(module_parts)
        assert module_str not in sys.modules

        # Use getattr to
        module = plotly.graph_objects
        for m in module_parts:
            module = getattr(module, m)

        assert module_str in sys.modules
