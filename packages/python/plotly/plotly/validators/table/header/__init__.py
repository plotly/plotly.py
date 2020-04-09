import _plotly_utils.basevalidators


class ValuessrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="valuessrc", parent_name="table.header", **kwargs):
        super(ValuessrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValuesValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="values", parent_name="table.header", **kwargs):
        super(ValuesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SuffixsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="suffixsrc", parent_name="table.header", **kwargs):
        super(SuffixsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SuffixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="suffix", parent_name="table.header", **kwargs):
        super(SuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PrefixsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="prefixsrc", parent_name="table.header", **kwargs):
        super(PrefixsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PrefixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="prefix", parent_name="table.header", **kwargs):
        super(PrefixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="table.header", **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            colorsrc
                Sets the source reference on Chart Studio Cloud
                for  color .
            width

            widthsrc
                Sets the source reference on Chart Studio Cloud
                for  width .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HeightValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="height", parent_name="table.header", **kwargs):
        super(HeightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FormatsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="formatsrc", parent_name="table.header", **kwargs):
        super(FormatsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FormatValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="format", parent_name="table.header", **kwargs):
        super(FormatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class FontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="font", parent_name="table.header", **kwargs):
        super(FontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Font"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            colorsrc
                Sets the source reference on Chart Studio Cloud
                for  color .
            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The Chart Studio Cloud (at
                https://chart-studio.plotly.com or on-premise)
                generates images on a server, where only a
                select number of fonts are installed and
                supported. These include "Arial", "Balto",
                "Courier New", "Droid Sans",, "Droid Serif",
                "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            familysrc
                Sets the source reference on Chart Studio Cloud
                for  family .
            size

            sizesrc
                Sets the source reference on Chart Studio Cloud
                for  size .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class FillValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="fill", parent_name="table.header", **kwargs):
        super(FillValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Fill"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the cell fill color. It accepts either a
                specific color or an array of colors or a 2D
                array of colors.
            colorsrc
                Sets the source reference on Chart Studio Cloud
                for  color .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class AlignsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="alignsrc", parent_name="table.header", **kwargs):
        super(AlignsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class AlignValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="align", parent_name="table.header", **kwargs):
        super(AlignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["left", "center", "right"]),
            **kwargs
        )
