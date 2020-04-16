import sys

if sys.version_info < (3, 7):
    from ._zaxis import ZAxis
    from ._yaxis import YAxis
    from ._xaxis import XAxis
    from ._domain import Domain
    from ._camera import Camera
    from ._aspectratio import Aspectratio
    from ._annotation import Annotation
    from . import zaxis
    from . import yaxis
    from . import xaxis
    from . import camera
    from . import annotation
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".zaxis", ".yaxis", ".xaxis", ".camera", ".annotation"],
        [
            "._zaxis.ZAxis",
            "._yaxis.YAxis",
            "._xaxis.XAxis",
            "._domain.Domain",
            "._camera.Camera",
            "._aspectratio.Aspectratio",
            "._annotation.Annotation",
        ],
    )
