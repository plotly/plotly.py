import _plotly_utils.basevalidators


class ProjectionValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='projection', parent_name='layout.geo', **kwargs
    ):
        super(ProjectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Projection',
            data_docs="""
            parallels
                For conic projection types only. Sets the
                parallels (tangent, secant) where the cone
                intersects the sphere.
            rotation
                plotly.graph_objs.layout.geo.projection.Rotatio
                n instance or dict with compatible properties
            scale
                Zooms in or out on the map view. A scale of 1
                corresponds to the largest zoom level that fits
                the map's lon and lat ranges.
            type
                Sets the projection type.
""",
            **kwargs
        )
