import sys

if sys.version_info < (3, 7):
    from ._yanchor import YanchorValidator
    from ._y import YValidator
    from ._xanchor import XanchorValidator
    from ._x import XValidator
    from ._valign import ValignValidator
    from ._uirevision import UirevisionValidator
    from ._traceorder import TraceorderValidator
    from ._tracegroupgap import TracegroupgapValidator
    from ._title import TitleValidator
    from ._orientation import OrientationValidator
    from ._itemwidth import ItemwidthValidator
    from ._itemsizing import ItemsizingValidator
    from ._itemdoubleclick import ItemdoubleclickValidator
    from ._itemclick import ItemclickValidator
    from ._font import FontValidator
    from ._borderwidth import BorderwidthValidator
    from ._bordercolor import BordercolorValidator
    from ._bgcolor import BgcolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._yanchor.YanchorValidator",
            "._y.YValidator",
            "._xanchor.XanchorValidator",
            "._x.XValidator",
            "._valign.ValignValidator",
            "._uirevision.UirevisionValidator",
            "._traceorder.TraceorderValidator",
            "._tracegroupgap.TracegroupgapValidator",
            "._title.TitleValidator",
            "._orientation.OrientationValidator",
            "._itemwidth.ItemwidthValidator",
            "._itemsizing.ItemsizingValidator",
            "._itemdoubleclick.ItemdoubleclickValidator",
            "._itemclick.ItemclickValidator",
            "._font.FontValidator",
            "._borderwidth.BorderwidthValidator",
            "._bordercolor.BordercolorValidator",
            "._bgcolor.BgcolorValidator",
        ],
    )
