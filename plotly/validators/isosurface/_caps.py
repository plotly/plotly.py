import _plotly_utils.basevalidators


class CapsValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='caps', parent_name='isosurface', **kwargs):
        super(CapsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Caps'),
            data_docs=kwargs.pop(
                'data_docs', """
            x
                plotly.graph_objs.isosurface.caps.X instance or
                dict with compatible properties
            y
                plotly.graph_objs.isosurface.caps.Y instance or
                dict with compatible properties
            z
                plotly.graph_objs.isosurface.caps.Z instance or
                dict with compatible properties
"""
            ),
            **kwargs
        )
