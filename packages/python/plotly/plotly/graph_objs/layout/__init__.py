import sys

if sys.version_info < (3, 7):
    from ._yaxis import YAxis
    from ._xaxis import XAxis
    from ._updatemenu import Updatemenu
    from ._uniformtext import Uniformtext
    from ._transition import Transition
    from ._title import Title
    from ._ternary import Ternary
    from ._template import Template
    from ._slider import Slider
    from ._shape import Shape
    from ._scene import Scene
    from ._radialaxis import RadialAxis
    from ._polar import Polar
    from ._modebar import Modebar
    from ._margin import Margin
    from ._mapbox import Mapbox
    from ._legend import Legend
    from ._image import Image
    from ._hoverlabel import Hoverlabel
    from ._grid import Grid
    from ._geo import Geo
    from ._font import Font
    from ._colorscale import Colorscale
    from ._coloraxis import Coloraxis
    from ._annotation import Annotation
    from ._angularaxis import AngularAxis
    from . import yaxis
    from . import xaxis
    from . import updatemenu
    from . import title
    from . import ternary
    from . import template
    from . import slider
    from . import shape
    from . import scene
    from . import polar
    from . import mapbox
    from . import legend
    from . import hoverlabel
    from . import grid
    from . import geo
    from . import coloraxis
    from . import annotation
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [
            ".yaxis",
            ".xaxis",
            ".updatemenu",
            ".title",
            ".ternary",
            ".template",
            ".slider",
            ".shape",
            ".scene",
            ".polar",
            ".mapbox",
            ".legend",
            ".hoverlabel",
            ".grid",
            ".geo",
            ".coloraxis",
            ".annotation",
        ],
        [
            "._yaxis.YAxis",
            "._xaxis.XAxis",
            "._updatemenu.Updatemenu",
            "._uniformtext.Uniformtext",
            "._transition.Transition",
            "._title.Title",
            "._ternary.Ternary",
            "._template.Template",
            "._slider.Slider",
            "._shape.Shape",
            "._scene.Scene",
            "._radialaxis.RadialAxis",
            "._polar.Polar",
            "._modebar.Modebar",
            "._margin.Margin",
            "._mapbox.Mapbox",
            "._legend.Legend",
            "._image.Image",
            "._hoverlabel.Hoverlabel",
            "._grid.Grid",
            "._geo.Geo",
            "._font.Font",
            "._colorscale.Colorscale",
            "._coloraxis.Coloraxis",
            "._annotation.Annotation",
            "._angularaxis.AngularAxis",
        ],
    )
