import _plotly_utils.basevalidators


class DataValidator(_plotly_utils.basevalidators.BaseDataValidator):

    def __init__(self, plotly_name='data', parent_name='', **kwargs):

        super(DataValidator, self).__init__(
            class_strs_map={
                'area': 'Area',
                'bar': 'Bar',
                'barpolar': 'Barpolar',
                'box': 'Box',
                'candlestick': 'Candlestick',
                'carpet': 'Carpet',
                'choropleth': 'Choropleth',
                'cone': 'Cone',
                'contour': 'Contour',
                'contourcarpet': 'Contourcarpet',
                'heatmap': 'Heatmap',
                'heatmapgl': 'Heatmapgl',
                'histogram': 'Histogram',
                'histogram2d': 'Histogram2d',
                'histogram2dcontour': 'Histogram2dContour',
                'mesh3d': 'Mesh3d',
                'ohlc': 'Ohlc',
                'parcats': 'Parcats',
                'parcoords': 'Parcoords',
                'pie': 'Pie',
                'pointcloud': 'Pointcloud',
                'sankey': 'Sankey',
                'scatter': 'Scatter',
                'scatter3d': 'Scatter3d',
                'scattercarpet': 'Scattercarpet',
                'scattergeo': 'Scattergeo',
                'scattergl': 'Scattergl',
                'scattermapbox': 'Scattermapbox',
                'scatterpolar': 'Scatterpolar',
                'scatterpolargl': 'Scatterpolargl',
                'scatterternary': 'Scatterternary',
                'splom': 'Splom',
                'streamtube': 'Streamtube',
                'surface': 'Surface',
                'table': 'Table',
                'violin': 'Violin',
            },
            plotly_name=plotly_name,
            parent_name=parent_name,
            **kwargs
        )
