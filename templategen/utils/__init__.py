from plotly import graph_objs as go

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
                parent.autocolorscale = False


def set_all_colorbars(template, colorbar):
    for parent_path in colorscale_parent_paths:
        if not template.data[parent_path[0]]:
            template.data[parent_path[0]] = [{}]

        for trace in template.data[parent_path[0]]:
            parent = trace[parent_path[1:]]

            if 'colorbar' in parent:
                parent.colorbar = colorbar


def initialize_template(annotation_defaults,
                        axis_common,
                        axis_ticks_clr,
                        colorbar_common,
                        colorscale,
                        colorway,
                        font_clr,
                        panel_background_clr,
                        panel_grid_clr,
                        paper_clr,
                        shape_defaults,
                        table_cell_clr,
                        table_header_clr,
                        table_line_clr,
                        zerolinecolor_clr):

    # Initialize template
    # -------------------
    template = go.layout.Template()

    # trace cycle color
    template.layout.colorway = colorway

    # Set global font color
    template.layout.font.color = font_clr

    # Set background colors
    template.layout.paper_bgcolor = paper_clr
    template.layout.plot_bgcolor = panel_background_clr
    template.layout.polar.bgcolor = panel_background_clr
    template.layout.ternary.bgcolor = panel_background_clr
    set_all_colorscales(template, colorscale)
    set_all_colorbars(template, colorbar_common)
    cartesian_axis = dict(axis_common, zerolinecolor=zerolinecolor_clr)

    # Cartesian
    template.layout.xaxis = cartesian_axis
    template.layout.yaxis = cartesian_axis

    # 3D
    axis_3d = dict(cartesian_axis)
    if panel_background_clr:
        axis_3d['backgroundcolor'] = panel_background_clr
        axis_3d['showbackground'] = True
    template.layout.scene.xaxis = axis_3d
    template.layout.scene.yaxis = axis_3d
    template.layout.scene.zaxis = axis_3d

    # Ternary
    template.layout.ternary.aaxis = axis_common
    template.layout.ternary.baxis = axis_common
    template.layout.ternary.caxis = axis_common

    # Polar
    template.layout.polar.angularaxis = axis_common
    template.layout.polar.radialaxis = axis_common

    # Carpet
    carpet_axis = dict(
        gridcolor=panel_grid_clr,
        linecolor=panel_grid_clr,
        startlinecolor=axis_ticks_clr,
        endlinecolor=axis_ticks_clr,
        minorgridcolor=panel_grid_clr)
    template.data.carpet = [{
        'aaxis': carpet_axis,
        'baxis': carpet_axis}]

    # Shape defaults
    template.layout.shapedefaults = shape_defaults

    # Annotation defaults
    template.layout.annotationdefaults = annotation_defaults

    # Geo
    template.layout.geo.bgcolor = paper_clr
    template.layout.geo.landcolor = panel_background_clr
    template.layout.geo.subunitcolor = panel_grid_clr
    template.layout.geo.showland = True
    template.layout.geo.showlakes = True
    template.layout.geo.lakecolor = paper_clr

    # Table
    template.data.table = [{'header': {'fill': {'color': table_header_clr},
                                       'line': {'color': table_line_clr},},
                            'cells': {'fill': {'color': table_cell_clr},
                                      'line': {'color': table_line_clr}}}]
    return template