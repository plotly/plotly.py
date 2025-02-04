

import _plotly_utils.basevalidators as _bv


class SourcetypeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='sourcetype',
                       parent_name='layout.mapbox.layer',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['geojson', 'vector', 'raster', 'image']),
        **kwargs)