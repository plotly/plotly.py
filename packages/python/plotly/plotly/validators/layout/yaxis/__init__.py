import sys

if sys.version_info < (3, 7):
    from ._zerolinewidth import ZerolinewidthValidator
    from ._zerolinecolor import ZerolinecolorValidator
    from ._zeroline import ZerolineValidator
    from ._visible import VisibleValidator
    from ._uirevision import UirevisionValidator
    from ._type import TypeValidator
    from ._title import TitleValidator
    from ._tickwidth import TickwidthValidator
    from ._tickvalssrc import TickvalssrcValidator
    from ._tickvals import TickvalsValidator
    from ._ticktextsrc import TicktextsrcValidator
    from ._ticktext import TicktextValidator
    from ._ticksuffix import TicksuffixValidator
    from ._tickson import TicksonValidator
    from ._ticks import TicksValidator
    from ._tickprefix import TickprefixValidator
    from ._tickmode import TickmodeValidator
    from ._ticklen import TicklenValidator
    from ._ticklabelmode import TicklabelmodeValidator
    from ._tickformatstopdefaults import TickformatstopdefaultsValidator
    from ._tickformatstops import TickformatstopsValidator
    from ._tickformat import TickformatValidator
    from ._tickfont import TickfontValidator
    from ._tickcolor import TickcolorValidator
    from ._tickangle import TickangleValidator
    from ._tick0 import Tick0Validator
    from ._spikethickness import SpikethicknessValidator
    from ._spikesnap import SpikesnapValidator
    from ._spikemode import SpikemodeValidator
    from ._spikedash import SpikedashValidator
    from ._spikecolor import SpikecolorValidator
    from ._side import SideValidator
    from ._showticksuffix import ShowticksuffixValidator
    from ._showtickprefix import ShowtickprefixValidator
    from ._showticklabels import ShowticklabelsValidator
    from ._showspikes import ShowspikesValidator
    from ._showline import ShowlineValidator
    from ._showgrid import ShowgridValidator
    from ._showexponent import ShowexponentValidator
    from ._showdividers import ShowdividersValidator
    from ._separatethousands import SeparatethousandsValidator
    from ._scaleratio import ScaleratioValidator
    from ._scaleanchor import ScaleanchorValidator
    from ._rangemode import RangemodeValidator
    from ._rangebreakdefaults import RangebreakdefaultsValidator
    from ._rangebreaks import RangebreaksValidator
    from ._range import RangeValidator
    from ._position import PositionValidator
    from ._overlaying import OverlayingValidator
    from ._nticks import NticksValidator
    from ._mirror import MirrorValidator
    from ._matches import MatchesValidator
    from ._linewidth import LinewidthValidator
    from ._linecolor import LinecolorValidator
    from ._layer import LayerValidator
    from ._hoverformat import HoverformatValidator
    from ._gridwidth import GridwidthValidator
    from ._gridcolor import GridcolorValidator
    from ._fixedrange import FixedrangeValidator
    from ._exponentformat import ExponentformatValidator
    from ._dtick import DtickValidator
    from ._domain import DomainValidator
    from ._dividerwidth import DividerwidthValidator
    from ._dividercolor import DividercolorValidator
    from ._constraintoward import ConstraintowardValidator
    from ._constrain import ConstrainValidator
    from ._color import ColorValidator
    from ._categoryorder import CategoryorderValidator
    from ._categoryarraysrc import CategoryarraysrcValidator
    from ._categoryarray import CategoryarrayValidator
    from ._calendar import CalendarValidator
    from ._autorange import AutorangeValidator
    from ._automargin import AutomarginValidator
    from ._anchor import AnchorValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._zerolinewidth.ZerolinewidthValidator",
            "._zerolinecolor.ZerolinecolorValidator",
            "._zeroline.ZerolineValidator",
            "._visible.VisibleValidator",
            "._uirevision.UirevisionValidator",
            "._type.TypeValidator",
            "._title.TitleValidator",
            "._tickwidth.TickwidthValidator",
            "._tickvalssrc.TickvalssrcValidator",
            "._tickvals.TickvalsValidator",
            "._ticktextsrc.TicktextsrcValidator",
            "._ticktext.TicktextValidator",
            "._ticksuffix.TicksuffixValidator",
            "._tickson.TicksonValidator",
            "._ticks.TicksValidator",
            "._tickprefix.TickprefixValidator",
            "._tickmode.TickmodeValidator",
            "._ticklen.TicklenValidator",
            "._ticklabelmode.TicklabelmodeValidator",
            "._tickformatstopdefaults.TickformatstopdefaultsValidator",
            "._tickformatstops.TickformatstopsValidator",
            "._tickformat.TickformatValidator",
            "._tickfont.TickfontValidator",
            "._tickcolor.TickcolorValidator",
            "._tickangle.TickangleValidator",
            "._tick0.Tick0Validator",
            "._spikethickness.SpikethicknessValidator",
            "._spikesnap.SpikesnapValidator",
            "._spikemode.SpikemodeValidator",
            "._spikedash.SpikedashValidator",
            "._spikecolor.SpikecolorValidator",
            "._side.SideValidator",
            "._showticksuffix.ShowticksuffixValidator",
            "._showtickprefix.ShowtickprefixValidator",
            "._showticklabels.ShowticklabelsValidator",
            "._showspikes.ShowspikesValidator",
            "._showline.ShowlineValidator",
            "._showgrid.ShowgridValidator",
            "._showexponent.ShowexponentValidator",
            "._showdividers.ShowdividersValidator",
            "._separatethousands.SeparatethousandsValidator",
            "._scaleratio.ScaleratioValidator",
            "._scaleanchor.ScaleanchorValidator",
            "._rangemode.RangemodeValidator",
            "._rangebreakdefaults.RangebreakdefaultsValidator",
            "._rangebreaks.RangebreaksValidator",
            "._range.RangeValidator",
            "._position.PositionValidator",
            "._overlaying.OverlayingValidator",
            "._nticks.NticksValidator",
            "._mirror.MirrorValidator",
            "._matches.MatchesValidator",
            "._linewidth.LinewidthValidator",
            "._linecolor.LinecolorValidator",
            "._layer.LayerValidator",
            "._hoverformat.HoverformatValidator",
            "._gridwidth.GridwidthValidator",
            "._gridcolor.GridcolorValidator",
            "._fixedrange.FixedrangeValidator",
            "._exponentformat.ExponentformatValidator",
            "._dtick.DtickValidator",
            "._domain.DomainValidator",
            "._dividerwidth.DividerwidthValidator",
            "._dividercolor.DividercolorValidator",
            "._constraintoward.ConstraintowardValidator",
            "._constrain.ConstrainValidator",
            "._color.ColorValidator",
            "._categoryorder.CategoryorderValidator",
            "._categoryarraysrc.CategoryarraysrcValidator",
            "._categoryarray.CategoryarrayValidator",
            "._calendar.CalendarValidator",
            "._autorange.AutorangeValidator",
            "._automargin.AutomarginValidator",
            "._anchor.AnchorValidator",
        ],
    )
