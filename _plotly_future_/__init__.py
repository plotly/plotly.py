_future_flags = set()


def _assert_plotly_not_imported():
    import sys
    if 'plotly' in sys.modules:
        raise ImportError("""\
The _plotly_future_ module must be import before the plotly module""")
