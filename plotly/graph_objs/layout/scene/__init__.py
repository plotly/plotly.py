import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [".annotation", ".camera", ".xaxis", ".yaxis", ".zaxis"],
    [
        "._annotation.Annotation",
        "._aspectratio.Aspectratio",
        "._camera.Camera",
        "._domain.Domain",
        "._xaxis.XAxis",
        "._yaxis.YAxis",
        "._zaxis.ZAxis",
    ],
)
