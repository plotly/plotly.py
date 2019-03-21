import warnings

_future_flags = set()


def _assert_plotly_not_imported():
    import sys
    if 'plotly' in sys.modules:
        raise ImportError("""\
The _plotly_future_ module must be import before the plotly module""")


warnings.filterwarnings(
    'default',
    '.*?please use chart_studio.*',
    DeprecationWarning
)


def _chart_studio_warning(submodule):
    warnings.warn(
        'The plotly.{submodule} module is deprecated, '
        'please use chart_studio.{submodule} instead'
            .format(submodule=submodule),
        DeprecationWarning,
        stacklevel=2)


__all__ = ['_future_flags', '_chart_studio_warning']
