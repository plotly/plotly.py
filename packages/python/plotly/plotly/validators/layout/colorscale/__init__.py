import sys

if sys.version_info < (3, 7):
    from ._sequentialminus import SequentialminusValidator
    from ._sequential import SequentialValidator
    from ._diverging import DivergingValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._sequentialminus.SequentialminusValidator",
            "._sequential.SequentialValidator",
            "._diverging.DivergingValidator",
        ],
    )
