import sys

if sys.version_info < (3, 7):
    from ._y import YValidator
    from ._x import XValidator
    from ._row import RowValidator
    from ._column import ColumnValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._y.YValidator",
            "._x.XValidator",
            "._row.RowValidator",
            "._column.ColumnValidator",
        ],
    )
