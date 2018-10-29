import _plotly_utils.basevalidators


class DataValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='data', parent_name='layout.template', **kwargs
    ):
        super(DataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Data'),
            data_docs=kwargs.pop(
                'data_docs', """
            area
                plotly.graph_objs.layout.template.data.Area
                instance or dict with compatible properties
            barpolar
                plotly.graph_objs.layout.template.data.Barpolar
                instance or dict with compatible properties
            bar
                plotly.graph_objs.layout.template.data.Bar
                instance or dict with compatible properties
            box
                plotly.graph_objs.layout.template.data.Box
                instance or dict with compatible properties
            candlestick
                plotly.graph_objs.layout.template.data.Candlest
                ick instance or dict with compatible properties
            carpet
                plotly.graph_objs.layout.template.data.Carpet
                instance or dict with compatible properties
            choropleth
                plotly.graph_objs.layout.template.data.Chorople
                th instance or dict with compatible properties
            cone
                plotly.graph_objs.layout.template.data.Cone
                instance or dict with compatible properties
            contourcarpet
                plotly.graph_objs.layout.template.data.Contourc
                arpet instance or dict with compatible
                properties
            contour
                plotly.graph_objs.layout.template.data.Contour
                instance or dict with compatible properties
            heatmapgl
                plotly.graph_objs.layout.template.data.Heatmapg
                l instance or dict with compatible properties
            heatmap
                plotly.graph_objs.layout.template.data.Heatmap
                instance or dict with compatible properties
            histogram2dcontour
                plotly.graph_objs.layout.template.data.Histogra
                m2dContour instance or dict with compatible
                properties
            histogram2d
                plotly.graph_objs.layout.template.data.Histogra
                m2d instance or dict with compatible properties
            histogram
                plotly.graph_objs.layout.template.data.Histogra
                m instance or dict with compatible properties
            mesh3d
                plotly.graph_objs.layout.template.data.Mesh3d
                instance or dict with compatible properties
            ohlc
                plotly.graph_objs.layout.template.data.Ohlc
                instance or dict with compatible properties
            parcats
                plotly.graph_objs.layout.template.data.Parcats
                instance or dict with compatible properties
            parcoords
                plotly.graph_objs.layout.template.data.Parcoord
                s instance or dict with compatible properties
            pie
                plotly.graph_objs.layout.template.data.Pie
                instance or dict with compatible properties
            pointcloud
                plotly.graph_objs.layout.template.data.Pointclo
                ud instance or dict with compatible properties
            sankey
                plotly.graph_objs.layout.template.data.Sankey
                instance or dict with compatible properties
            scatter3d
                plotly.graph_objs.layout.template.data.Scatter3
                d instance or dict with compatible properties
            scattercarpet
                plotly.graph_objs.layout.template.data.Scatterc
                arpet instance or dict with compatible
                properties
            scattergeo
                plotly.graph_objs.layout.template.data.Scatterg
                eo instance or dict with compatible properties
            scattergl
                plotly.graph_objs.layout.template.data.Scatterg
                l instance or dict with compatible properties
            scattermapbox
                plotly.graph_objs.layout.template.data.Scatterm
                apbox instance or dict with compatible
                properties
            scatterpolargl
                plotly.graph_objs.layout.template.data.Scatterp
                olargl instance or dict with compatible
                properties
            scatterpolar
                plotly.graph_objs.layout.template.data.Scatterp
                olar instance or dict with compatible
                properties
            scatter
                plotly.graph_objs.layout.template.data.Scatter
                instance or dict with compatible properties
            scatterternary
                plotly.graph_objs.layout.template.data.Scattert
                ernary instance or dict with compatible
                properties
            splom
                plotly.graph_objs.layout.template.data.Splom
                instance or dict with compatible properties
            streamtube
                plotly.graph_objs.layout.template.data.Streamtu
                be instance or dict with compatible properties
            surface
                plotly.graph_objs.layout.template.data.Surface
                instance or dict with compatible properties
            table
                plotly.graph_objs.layout.template.data.Table
                instance or dict with compatible properties
            violin
                plotly.graph_objs.layout.template.data.Violin
                instance or dict with compatible properties
"""
            ),
            **kwargs
        )
