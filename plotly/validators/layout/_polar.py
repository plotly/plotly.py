import _plotly_utils.basevalidators


class PolarValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='polar', parent_name='layout', **kwargs):
        super(PolarValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Polar',
            data_docs="""
            angularaxis
                plotly.graph_objs.layout.polar.AngularAxis
                instance or dict with compatible properties
            bgcolor
                Set the background color of the subplot
            domain
                plotly.graph_objs.layout.polar.Domain instance
                or dict with compatible properties
            gridshape
                Determines if the radial axis grid lines and
                angular axis line are drawn as "circular"
                sectors or as "linear" (polygon) sectors. Has
                an effect only when the angular axis has `type`
                "category". Note that `radialaxis.angle` is
                snapped to the angle of the closest vertex when
                `gridshape` is "circular" (so that radial axis
                scale is the same as the data scale).
            radialaxis
                plotly.graph_objs.layout.polar.RadialAxis
                instance or dict with compatible properties
            sector
                Sets angular span of this polar subplot with
                two angles (in degrees). Sector are assumed to
                be spanned in the counterclockwise direction
                with 0 corresponding to rightmost limit of the
                polar subplot.
""",
            **kwargs
        )
