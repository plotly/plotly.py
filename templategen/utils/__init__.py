colorscale_parent_paths = [
    ('histogram2dcontour',),
    ('choropleth',),
    ('histogram2d',),
    ('heatmap',),
    ('heatmapgl',),
    ('contourcarpet',),
    ('contour',),
    ('surface',),
    ('mesh3d',),
    ('scatter', 'marker'),
    ('parcoords', 'line'),
    ('scatterpolargl', 'marker'),
    ('bar', 'marker'),
    ('scattergeo', 'marker'),
    ('scatterpolar', 'marker'),
    ('histogram', 'marker'),
    ('scattergl', 'marker'),
    ('scatter3d', 'line'),
    ('scatter3d', 'marker'),
    ('scattermapbox', 'marker'),
    ('scatterternary', 'marker'),
    ('scattercarpet', 'marker'),
    ('scatter', 'marker', 'line'),
    ('scatterpolargl', 'marker', 'line'),
    ('bar', 'marker', 'line')
]


def set_all_colorscales(template, colorscale):
    for parent_path in colorscale_parent_paths:
        if not template.data[parent_path[0]]:
            template.data[parent_path[0]] = [{}]

        for trace in template.data[parent_path[0]]:
            parent = trace[parent_path[1:]]
            if 'colorscale' in parent:
                parent.colorscale = colorscale


def set_all_colorbars(template, colorbar):
    for parent_path in colorscale_parent_paths:
        if not template.data[parent_path[0]]:
            template.data[parent_path[0]] = [{}]

        for trace in template.data[parent_path[0]]:
            parent = trace[parent_path[1:]]

            if 'colorbar' in parent:
                parent.colorbar = colorbar
