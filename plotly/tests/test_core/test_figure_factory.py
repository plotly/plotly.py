def test_figure_factory_import_does_not_break():
    # Even if we don't have the optional dependencies installed, importing
    # figure_factory should not cause an exception
    import plotly.figure_factory
