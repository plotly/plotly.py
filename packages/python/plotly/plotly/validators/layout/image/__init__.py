import _plotly_utils.basevalidators


class YrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yref", parent_name="layout.image", **kwargs):
        super(YrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["paper", "/^y([2-9]|[1-9][0-9]+)?$/"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yanchor", parent_name="layout.image", **kwargs):
        super(YanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["top", "middle", "bottom"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="y", parent_name="layout.image", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xref", parent_name="layout.image", **kwargs):
        super(XrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["paper", "/^x([2-9]|[1-9][0-9]+)?$/"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XanchorValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xanchor", parent_name="layout.image", **kwargs):
        super(XanchorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["left", "center", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="x", parent_name="layout.image", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="visible", parent_name="layout.image", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="templateitemname", parent_name="layout.image", **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SourceValidator(_plotly_utils.basevalidators.ImageUriValidator):
    def __init__(self, plotly_name="source", parent_name="layout.image", **kwargs):
        super(SourceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="sizing", parent_name="layout.image", **kwargs):
        super(SizingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["fill", "contain", "stretch"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizeyValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="sizey", parent_name="layout.image", **kwargs):
        super(SizeyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizexValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="sizex", parent_name="layout.image", **kwargs):
        super(SizexValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="opacity", parent_name="layout.image", **kwargs):
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
    def __init__(self, plotly_name="name", parent_name="layout.image", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LayerValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="layer", parent_name="layout.image", **kwargs):
        super(LayerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["below", "above"]),
            **kwargs
        )
