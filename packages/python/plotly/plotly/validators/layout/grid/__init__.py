import _plotly_utils.basevalidators


class YsideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yside", parent_name="layout.grid", **kwargs):
        super(YsideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["left", "left plot", "right plot", "right"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class YgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="ygap", parent_name="layout.grid", **kwargs):
        super(YgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YaxesValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="yaxes", parent_name="layout.grid", **kwargs):
        super(YaxesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                {
                    "valType": "enumerated",
                    "values": ["/^y([2-9]|[1-9][0-9]+)?$/", ""],
                    "editType": "plot",
                },
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XsideValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="xside", parent_name="layout.grid", **kwargs):
        super(XsideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["bottom", "bottom plot", "top plot", "top"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class XgapValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="xgap", parent_name="layout.grid", **kwargs):
        super(XgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XaxesValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="xaxes", parent_name="layout.grid", **kwargs):
        super(XaxesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                {
                    "valType": "enumerated",
                    "values": ["/^x([2-9]|[1-9][0-9]+)?$/", ""],
                    "editType": "plot",
                },
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SubplotsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="subplots", parent_name="layout.grid", **kwargs):
        super(SubplotsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dimensions=kwargs.pop("dimensions", 2),
            edit_type=kwargs.pop("edit_type", "plot"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                {
                    "valType": "enumerated",
                    "values": ["/^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$/", ""],
                    "editType": "plot",
                },
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RowsValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="rows", parent_name="layout.grid", **kwargs):
        super(RowsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RoworderValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="roworder", parent_name="layout.grid", **kwargs):
        super(RoworderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["top to bottom", "bottom to top"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class PatternValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="pattern", parent_name="layout.grid", **kwargs):
        super(PatternValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["independent", "coupled"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.grid", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            x
                Sets the horizontal domain of this grid subplot
                (in plot fraction). The first and last cells
                end exactly at the domain edges, with no grout
                around the edges.
            y
                Sets the vertical domain of this grid subplot
                (in plot fraction). The first and last cells
                end exactly at the domain edges, with no grout
                around the edges.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColumnsValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="columns", parent_name="layout.grid", **kwargs):
        super(ColumnsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
