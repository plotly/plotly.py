import _plotly_utils.basevalidators


class NodeValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='node', parent_name='sankey', **kwargs):
        super(NodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Node',
            data_docs="""
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
""",
            **kwargs
        )
