import sys

if sys.version_info < (3, 7):
    from ._value import ValueValidator
    from ._templateitemname import TemplateitemnameValidator
    from ._name import NameValidator
    from ._enabled import EnabledValidator
    from ._dtickrange import DtickrangeValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._value.ValueValidator",
            "._templateitemname.TemplateitemnameValidator",
            "._name.NameValidator",
            "._enabled.EnabledValidator",
            "._dtickrange.DtickrangeValidator",
        ],
    )
