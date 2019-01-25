import _plotly_utils.basevalidators


class SlicesValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='slices', parent_name='isosurface', **kwargs
    ):
        super(SlicesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Slices'),
            data_docs=kwargs.pop(
                'data_docs', """
            x
                plotly.graph_objs.isosurface.slices.X instance
                or dict with compatible properties
            y
                plotly.graph_objs.isosurface.slices.Y instance
                or dict with compatible properties
            z
                plotly.graph_objs.isosurface.slices.Z instance
                or dict with compatible properties
"""
            ),
            **kwargs
        )
