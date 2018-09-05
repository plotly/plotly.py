import _plotly_utils.basevalidators


class MapboxValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='mapbox', parent_name='layout', **kwargs):
        super(MapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Mapbox',
            data_docs="""
            accesstoken
                Sets the mapbox access token to be used for
                this mapbox map. Alternatively, the mapbox
                access token can be set in the configuration
                options under `mapboxAccessToken`.
            bearing
                Sets the bearing angle of the map (in degrees
                counter-clockwise from North).
            center
                plotly.graph_objs.layout.mapbox.Center instance
                or dict with compatible properties
            domain
                plotly.graph_objs.layout.mapbox.Domain instance
                or dict with compatible properties
            layers
                plotly.graph_objs.layout.mapbox.Layer instance
                or dict with compatible properties
            pitch
                Sets the pitch angle of the map (in degrees,
                where 0 means perpendicular to the surface of
                the map).
            style
                Sets the Mapbox map style. Either input one of
                the default Mapbox style names or the URL to a
                custom style or a valid Mapbox style JSON.
            zoom
                Sets the zoom level of the map.
""",
            **kwargs
        )
