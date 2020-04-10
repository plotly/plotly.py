import sys

if sys.version_info < (3, 7):
    from ._symbol import Symbol
    from ._line import Line
    from ._fill import Fill
    from ._circle import Circle
    from . import symbol
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [".symbol"],
        ["._symbol.Symbol", "._line.Line", "._fill.Fill", "._circle.Circle"],
    )
