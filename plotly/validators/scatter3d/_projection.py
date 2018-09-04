import _plotly_utils.basevalidators


class ProjectionValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='projection', parent_name='scatter3d', **kwargs
    ):
        super(ProjectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Projection',
            data_docs="""
            x
                plotly.graph_objs.scatter3d.projection.X
                instance or dict with compatible properties
            y
                plotly.graph_objs.scatter3d.projection.Y
                instance or dict with compatible properties
            z
                plotly.graph_objs.scatter3d.projection.Z
                instance or dict with compatible properties
""",
            **kwargs
        )
