import sys

if sys.version_info < (3, 7):
    from ._z import Z
    from ._y import Y
    from ._x import X
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._z.Z", "._y.Y", "._x.X"]
    )
