import sys

if sys.version_info < (3, 7):
    from ._start import StartValidator
    from ._size import SizeValidator
    from ._end import EndValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        ["._start.StartValidator", "._size.SizeValidator", "._end.EndValidator"],
    )
