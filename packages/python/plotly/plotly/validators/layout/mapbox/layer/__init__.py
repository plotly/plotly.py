import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="type", parent_name="layout.mapbox.layer", **kwargs):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["circle", "line", "fill", "symbol", "raster"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self,
        plotly_name="templateitemname",
        parent_name="layout.mapbox.layer",
        **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SymbolValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="symbol", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(SymbolValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Symbol"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            icon
                Sets the symbol icon image
                (mapbox.layer.layout.icon-image). Full list:
                https://www.mapbox.com/maki-icons/
            iconsize
                Sets the symbol icon size
                (mapbox.layer.layout.icon-size). Has an effect
                only when `type` is set to "symbol".
            placement
                Sets the symbol and/or text placement
                (mapbox.layer.layout.symbol-placement). If
                `placement` is "point", the label is placed
                where the geometry is located If `placement` is
                "line", the label is placed along the line of
                the geometry If `placement` is "line-center",
                the label is placed on the center of the
                geometry
            text
                Sets the symbol text (mapbox.layer.layout.text-
                field).
            textfont
                Sets the icon text font
                (color=mapbox.layer.paint.text-color,
                size=mapbox.layer.layout.text-size). Has an
                effect only when `type` is set to "symbol".
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SourcetypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="sourcetype", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(SourcetypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["geojson", "vector", "raster", "image"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class SourcelayerValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="sourcelayer", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(SourcelayerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SourceattributionValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self,
        plotly_name="sourceattribution",
        parent_name="layout.mapbox.layer",
        **kwargs
    ):
        super(SourceattributionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SourceValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="source", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(SourceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="opacity", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="layout.mapbox.layer", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MinzoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="minzoom", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(MinzoomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 24),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MaxzoomValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="maxzoom", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(MaxzoomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 24),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="layout.mapbox.layer", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            dash
                Sets the length of dashes and gaps
                (mapbox.layer.paint.line-dasharray). Has an
                effect only when `type` is set to "line".
            dashsrc
                Sets the source reference on Chart Studio Cloud
                for  dash .
            width
                Sets the line width (mapbox.layer.paint.line-
                width). Has an effect only when `type` is set
                to "line".
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="fill", parent_name="layout.mapbox.layer", **kwargs):
        super(FillValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Fill"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            outlinecolor
                Sets the fill outline color
                (mapbox.layer.paint.fill-outline-color). Has an
                effect only when `type` is set to "fill".
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CoordinatesValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(
        self, plotly_name="coordinates", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(CoordinatesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="color", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CircleValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="circle", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(CircleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Circle"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            radius
                Sets the circle radius
                (mapbox.layer.paint.circle-radius). Has an
                effect only when `type` is set to "circle".
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class BelowValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="below", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(BelowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
