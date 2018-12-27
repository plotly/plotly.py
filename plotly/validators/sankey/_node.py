import _plotly_utils.basevalidators


class NodeValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='node', parent_name='sankey', **kwargs):
        super(NodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Node'),
            data_docs=kwargs.pop(
                'data_docs', """
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
            hoverinfo
                Determines which trace information appear when
                hovering nodes. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverlabel
                plotly.graph_objs.sankey.node.Hoverlabel
                instance or dict with compatible properties
            hovertemplate
                Template string used for rendering the
                information that appear on hover box. Note that
                this will override `hoverinfo`. Variables are
                inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}". See https://github.com/d3/d
                3-format/blob/master/README.md#locale_format
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
                "<extra>{fullData.name}</extra>".
            hovertemplatesrc
                Sets the source reference on plot.ly for
                hovertemplate .
            label
                The shown name of the node.
            labelsrc
                Sets the source reference on plot.ly for  label
                .
            line
                plotly.graph_objs.sankey.node.Line instance or
                dict with compatible properties
            pad
                Sets the padding (in px) between the `nodes`.
            thickness
                Sets the thickness (in px) of the `nodes`.
"""
            ),
            **kwargs
        )
