import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="scatter3d.error_x", **kwargs):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="scatter3d.error_x", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValueminusValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="valueminus", parent_name="scatter3d.error_x", **kwargs
    ):
        super(ValueminusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValueValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="value", parent_name="scatter3d.error_x", **kwargs):
        super(ValueValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="type", parent_name="scatter3d.error_x", **kwargs):
        super(TypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["percent", "constant", "sqrt", "data"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TracerefminusValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self, plotly_name="tracerefminus", parent_name="scatter3d.error_x", **kwargs
    ):
        super(TracerefminusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TracerefValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(
        self, plotly_name="traceref", parent_name="scatter3d.error_x", **kwargs
    ):
        super(TracerefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ThicknessValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="thickness", parent_name="scatter3d.error_x", **kwargs
    ):
        super(ThicknessValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SymmetricValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="symmetric", parent_name="scatter3d.error_x", **kwargs
    ):
        super(SymmetricValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CopyZstyleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="copy_zstyle", parent_name="scatter3d.error_x", **kwargs
    ):
        super(CopyZstyleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name="color", parent_name="scatter3d.error_x", **kwargs):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArraysrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="arraysrc", parent_name="scatter3d.error_x", **kwargs
    ):
        super(ArraysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrayminussrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self, plotly_name="arrayminussrc", parent_name="scatter3d.error_x", **kwargs
    ):
        super(ArrayminussrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrayminusValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(
        self, plotly_name="arrayminus", parent_name="scatter3d.error_x", **kwargs
    ):
        super(ArrayminusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrayValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="array", parent_name="scatter3d.error_x", **kwargs):
        super(ArrayValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )
