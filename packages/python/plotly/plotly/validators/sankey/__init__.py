import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="visible", parent_name="sankey", **kwargs):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", [True, False, "legendonly"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValuesuffixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="valuesuffix", parent_name="sankey", **kwargs):
        super(ValuesuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValueformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="valueformat", parent_name="sankey", **kwargs):
        super(ValueformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UirevisionValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="sankey", **kwargs):
        super(UirevisionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class UidValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="uid", parent_name="sankey", **kwargs):
        super(UidValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TextfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="textfont", parent_name="sankey", **kwargs):
        super(TextfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Textfont"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color

            family
                HTML font family - the typeface that will be
                applied by the web browser. The web browser
                will only be able to apply a font if it is
                available on the system which it operates.
                Provide multiple font families, separated by
                commas, to indicate the preference in which to
                apply fonts if they aren't available on the
                system. The plotly service (at https://plot.ly
                or on-premise) generates images on a server,
                where only a select number of fonts are
                installed and supported. These include "Arial",
                "Balto", "Courier New", "Droid Sans",, "Droid
                Serif", "Droid Sans Mono", "Gravitas One", "Old
                Standard TT", "Open Sans", "Overpass", "PT Sans
                Narrow", "Raleway", "Times New Roman".
            size

""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class StreamValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="stream", parent_name="sankey", **kwargs):
        super(StreamValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Stream"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            maxpoints
                Sets the maximum number of points to keep on
                the plots from an incoming stream. If
                `maxpoints` is set to 50, only the newest 50
                points will be displayed on the plot.
            token
                The stream id number links a data trace on a
                plot with a stream. See
                https://plot.ly/settings for more details.
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class SelectedpointsValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="selectedpoints", parent_name="sankey", **kwargs):
        super(SelectedpointsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="orientation", parent_name="sankey", **kwargs):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["v", "h"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class NodeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="node", parent_name="sankey", **kwargs):
        super(NodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Node"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the `node` color. It can be a single
                value, or an array for specifying color for
                each `node`. If `node.color` is omitted, then
                the default `Plotly` color palette will be
                cycled through to have a variety of colors.
                These defaults are not fully opaque, to allow
                some visibility of what is beneath the node.
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            groups
                Groups of nodes. Each group is defined by an
                array with the indices of the nodes it
                contains. Multiple groups can be specified.
            hoverinfo
                Determines which trace information appear when
                hovering nodes. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverlabel
                plotly.graph_objects.sankey.node.Hoverlabel
                instance or dict with compatible properties
            hovertemplate
                Template string used for rendering the
                information that appear on hover box. Note that
                this will override `hoverinfo`. Variables are
                inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `value` and `label`. Anything
                contained in tag `<extra>` is displayed in the
                secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            label
                The shown name of the node.
            labelsrc
                Sets the source reference on plot.ly for  label
                .
            line
                plotly.graph_objects.sankey.node.Line instance
                or dict with compatible properties
            pad
                Sets the padding (in px) between the `nodes`.
            thickness
                Sets the thickness (in px) of the `nodes`.
            x
                The normalized horizontal position of the node.
            xsrc
                Sets the source reference on plot.ly for  x .
            y
                The normalized vertical position of the node.
            ysrc
                Sets the source reference on plot.ly for  y .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="sankey", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="metasrc", parent_name="sankey", **kwargs):
        super(MetasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MetaValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="meta", parent_name="sankey", **kwargs):
        super(MetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class LinkValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="link", parent_name="sankey", **kwargs):
        super(LinkValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Link"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            color
                Sets the `link` color. It can be a single
                value, or an array for specifying color for
                each `link`. If `link.color` is omitted, then
                by default, a translucent grey link will be
                used.
            colorscales
                A tuple of
                plotly.graph_objects.sankey.link.Colorscale
                instances or dicts with compatible properties
            colorscaledefaults
                When used in a template (as layout.template.dat
                a.sankey.link.colorscaledefaults), sets the
                default property values to use for elements of
                sankey.link.colorscales
            colorsrc
                Sets the source reference on plot.ly for  color
                .
            hoverinfo
                Determines which trace information appear when
                hovering links. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverlabel
                plotly.graph_objects.sankey.link.Hoverlabel
                instance or dict with compatible properties
            hovertemplate
                Template string used for rendering the
                information that appear on hover box. Note that
                this will override `hoverinfo`. Variables are
                inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}".
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                for details on the formatting syntax. The
                variables available in `hovertemplate` are the
                ones emitted as event data described at this
                link https://plot.ly/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                variables `value` and `label`. Anything
                contained in tag `<extra>` is displayed in the
                secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            label
                The shown name of the link.
            labelsrc
                Sets the source reference on plot.ly for  label
                .
            line
                plotly.graph_objects.sankey.link.Line instance
                or dict with compatible properties
            source
                An integer number `[0..nodes.length - 1]` that
                represents the source node.
            sourcesrc
                Sets the source reference on plot.ly for
                source .
            target
                An integer number `[0..nodes.length - 1]` that
                represents the target node.
            targetsrc
                Sets the source reference on plot.ly for
                target .
            value
                A numeric value representing the flow volume
                value.
            valuesrc
                Sets the source reference on plot.ly for  value
                .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdssrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="idssrc", parent_name="sankey", **kwargs):
        super(IdssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class IdsValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="ids", parent_name="sankey", **kwargs):
        super(IdsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverlabelValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="hoverlabel", parent_name="sankey", **kwargs):
        super(HoverlabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Hoverlabel"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            align
                Sets the horizontal alignment of the text
                content within hover label box. Has an effect
                only if the hover label text spans more two or
                more lines
            alignsrc
                Sets the source reference on plot.ly for  align
                .
            bgcolor
                Sets the background color of the hover labels
                for this trace
            bgcolorsrc
                Sets the source reference on plot.ly for
                bgcolor .
            bordercolor
                Sets the border color of the hover labels for
                this trace.
            bordercolorsrc
                Sets the source reference on plot.ly for
                bordercolor .
            font
                Sets the font used in hover labels.
            namelength
                Sets the default length (in number of
                characters) of the trace name in the hover
                labels for all traces. -1 shows the whole name
                regardless of length. 0-3 shows the first 0-3
                characters, and an integer >3 will show the
                whole name if it is less than that many
                characters, but if it is longer, will truncate
                to `namelength - 3` characters and add an
                ellipsis.
            namelengthsrc
                Sets the source reference on plot.ly for
                namelength .
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class HoverinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name="hoverinfo", parent_name="sankey", **kwargs):
        super(HoverinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "calc"),
            extras=kwargs.pop("extras", ["all", "none", "skip"]),
            flags=kwargs.pop("flags", []),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="sankey", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            column
                If there is a layout grid, use the domain for
                this column in the grid for this sankey trace .
            row
                If there is a layout grid, use the domain for
                this row in the grid for this sankey trace .
            x
                Sets the horizontal domain of this sankey trace
                (in plot fraction).
            y
                Sets the vertical domain of this sankey trace
                (in plot fraction).
""",
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdatasrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="customdatasrc", parent_name="sankey", **kwargs):
        super(CustomdatasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class CustomdataValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="customdata", parent_name="sankey", **kwargs):
        super(CustomdataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArrangementValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="arrangement", parent_name="sankey", **kwargs):
        super(ArrangementValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["snap", "perpendicular", "freeform", "fixed"]),
            **kwargs
        )
