import sys

if sys.version_info < (3, 7):
    from ._ypad import YpadValidator
    from ._yanchor import YanchorValidator
    from ._y import YValidator
    from ._xpad import XpadValidator
    from ._xanchor import XanchorValidator
    from ._x import XValidator
    from ._title import TitleValidator
    from ._tickwidth import TickwidthValidator
    from ._tickvalssrc import TickvalssrcValidator
    from ._tickvals import TickvalsValidator
    from ._ticktextsrc import TicktextsrcValidator
    from ._ticktext import TicktextValidator
    from ._ticksuffix import TicksuffixValidator
    from ._ticks import TicksValidator
    from ._tickprefix import TickprefixValidator
    from ._tickmode import TickmodeValidator
    from ._ticklen import TicklenValidator
    from ._ticklabelposition import TicklabelpositionValidator
    from ._tickformatstopdefaults import TickformatstopdefaultsValidator
    from ._tickformatstops import TickformatstopsValidator
    from ._tickformat import TickformatValidator
    from ._tickfont import TickfontValidator
    from ._tickcolor import TickcolorValidator
    from ._tickangle import TickangleValidator
    from ._tick0 import Tick0Validator
    from ._thicknessmode import ThicknessmodeValidator
    from ._thickness import ThicknessValidator
    from ._showticksuffix import ShowticksuffixValidator
    from ._showtickprefix import ShowtickprefixValidator
    from ._showticklabels import ShowticklabelsValidator
    from ._showexponent import ShowexponentValidator
    from ._separatethousands import SeparatethousandsValidator
    from ._outlinewidth import OutlinewidthValidator
    from ._outlinecolor import OutlinecolorValidator
    from ._nticks import NticksValidator
    from ._minexponent import MinexponentValidator
    from ._lenmode import LenmodeValidator
    from ._len import LenValidator
    from ._exponentformat import ExponentformatValidator
    from ._dtick import DtickValidator
    from ._borderwidth import BorderwidthValidator
    from ._bordercolor import BordercolorValidator
    from ._bgcolor import BgcolorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._ypad.YpadValidator",
            "._yanchor.YanchorValidator",
            "._y.YValidator",
            "._xpad.XpadValidator",
            "._xanchor.XanchorValidator",
            "._x.XValidator",
            "._title.TitleValidator",
            "._tickwidth.TickwidthValidator",
            "._tickvalssrc.TickvalssrcValidator",
            "._tickvals.TickvalsValidator",
            "._ticktextsrc.TicktextsrcValidator",
            "._ticktext.TicktextValidator",
            "._ticksuffix.TicksuffixValidator",
            "._ticks.TicksValidator",
            "._tickprefix.TickprefixValidator",
            "._tickmode.TickmodeValidator",
            "._ticklen.TicklenValidator",
            "._ticklabelposition.TicklabelpositionValidator",
            "._tickformatstopdefaults.TickformatstopdefaultsValidator",
            "._tickformatstops.TickformatstopsValidator",
            "._tickformat.TickformatValidator",
            "._tickfont.TickfontValidator",
            "._tickcolor.TickcolorValidator",
            "._tickangle.TickangleValidator",
            "._tick0.Tick0Validator",
            "._thicknessmode.ThicknessmodeValidator",
            "._thickness.ThicknessValidator",
            "._showticksuffix.ShowticksuffixValidator",
            "._showtickprefix.ShowtickprefixValidator",
            "._showticklabels.ShowticklabelsValidator",
            "._showexponent.ShowexponentValidator",
            "._separatethousands.SeparatethousandsValidator",
            "._outlinewidth.OutlinewidthValidator",
            "._outlinecolor.OutlinecolorValidator",
            "._nticks.NticksValidator",
            "._minexponent.MinexponentValidator",
            "._lenmode.LenmodeValidator",
            "._len.LenValidator",
            "._exponentformat.ExponentformatValidator",
            "._dtick.DtickValidator",
            "._borderwidth.BorderwidthValidator",
            "._bordercolor.BordercolorValidator",
            "._bgcolor.BgcolorValidator",
        ],
    )
