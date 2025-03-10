import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._uirevision.UirevisionValidator",
        "._sector.SectorValidator",
        "._radialaxis.RadialaxisValidator",
        "._hole.HoleValidator",
        "._gridshape.GridshapeValidator",
        "._domain.DomainValidator",
        "._bgcolor.BgcolorValidator",
        "._barmode.BarmodeValidator",
        "._bargap.BargapValidator",
        "._angularaxis.AngularaxisValidator",
    ],
)
