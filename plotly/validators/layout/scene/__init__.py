import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._zaxis.ZaxisValidator",
        "._yaxis.YaxisValidator",
        "._xaxis.XaxisValidator",
        "._uirevision.UirevisionValidator",
        "._hovermode.HovermodeValidator",
        "._dragmode.DragmodeValidator",
        "._domain.DomainValidator",
        "._camera.CameraValidator",
        "._bgcolor.BgcolorValidator",
        "._aspectratio.AspectratioValidator",
        "._aspectmode.AspectmodeValidator",
        "._annotationdefaults.AnnotationdefaultsValidator",
        "._annotations.AnnotationsValidator",
    ],
)
