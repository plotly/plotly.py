import _plotly_utils.basevalidators


class LinkValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='link', parent_name='sankey', **kwargs):
        super(LinkValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Link'),
            data_docs=kwargs.pop(
                'data_docs', """
            color
                Sets the `link` color. It can be a single
                value, or an array for specifying color for
                each `link`. If `link.color` is omitted, then
                by default, a translucent grey link will be
                used.
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
                plotly.graph_objs.sankey.link.Hoverlabel
                instance or dict with compatible properties
            label
                The shown name of the link.
            labelsrc
                Sets the source reference on plot.ly for  label
                .
            line
                plotly.graph_objs.sankey.link.Line instance or
                dict with compatible properties
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
"""
            ),
            **kwargs
        )
