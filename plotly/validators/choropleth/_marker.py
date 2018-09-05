import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='marker', parent_name='choropleth', **kwargs
    ):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Marker',
            data_docs="""
            line
                plotly.graph_objs.choropleth.marker.Line
                instance or dict with compatible properties
            opacity
                Sets the opacity of the locations.
            opacitysrc
                Sets the source reference on plot.ly for
                opacity .
""",
            **kwargs
        )
