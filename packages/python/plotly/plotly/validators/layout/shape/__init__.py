import _plotly_utils.basevalidators


class YsizemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="ysizemode", parent_name="layout.shape", **kwargs):
        super(YsizemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["scaled", "pixel"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yref", parent_name="layout.shape", **kwargs):
        super(YrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["paper", "/^y([2-9]|[1-9][0-9]+)?$/"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="yanchor", parent_name="layout.shape", **kwargs):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class Y1Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="y1", parent_name="layout.shape", **kwargs):
        super(Y1Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class Y0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="y0", parent_name="layout.shape", **kwargs):
        super(Y0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XsizemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xsizemode", parent_name="layout.shape", **kwargs):
        super(XsizemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["scaled", "pixel"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xref", parent_name="layout.shape", **kwargs):
        super(XrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["paper", "/^x([2-9]|[1-9][0-9]+)?$/"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.shape", **kwargs):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class X1Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="x1", parent_name="layout.shape", **kwargs):
        super(X1Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class X0Validator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="x0", parent_name="layout.shape", **kwargs):
        super(X0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="visible", parent_name="layout.shape", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="type", parent_name="layout.shape", **kwargs):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["circle", "rect", "path", "line"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="templateitemname", parent_name="layout.shape", **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PathValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="path", parent_name="layout.shape", **kwargs):
        super(PathValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="opacity", parent_name="layout.shape", **kwargs):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="layout.shape", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="layout.shape", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the line color.
            dash
                Sets the dash style of lines. Set to a dash
                type string ("solid", "dot", "dash",
                "longdash", "dashdot", or "longdashdot") or a
                dash length list in px (eg "5px,10px,2px,2px").
            width
                Sets the line width (in px).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LayerValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="layer", parent_name="layout.shape", **kwargs):
        super(LayerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["below", "above"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="fillcolor", parent_name="layout.shape", **kwargs):
        super(FillcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
