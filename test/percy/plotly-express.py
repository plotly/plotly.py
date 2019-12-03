## This script uses px functions to generate html figures, which will be
## tested with percy.

# this directory
import os

dir_name = os.path.join("test", "percy")

import plotly.express as px

print(px.data.iris.__doc__)
px.data.iris().head()

# #### Scatter and Line plots

import plotly.express as px

iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length")
fig.write_html(os.path.join(dir_name, "scatter.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
fig.write_html(os.path.join(dir_name, "scatter_color.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_y="rug",
    marginal_x="histogram",
)
fig.write_html(os.path.join(dir_name, "scatter_marginal.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_y="violin",
    marginal_x="box",
    trendline="ols",
)
fig.write_html(os.path.join(dir_name, "scatter_trendline.html"))

import plotly.express as px

iris = px.data.iris()
iris["e"] = iris["sepal_width"] / 100
fig = px.scatter(
    iris, x="sepal_width", y="sepal_length", color="species", error_x="e", error_y="e"
)
fig.write_html(os.path.join(dir_name, "scatter_errorbar.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_row="time",
    facet_col="day",
    color="smoker",
    trendline="ols",
    category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]},
)
fig.write_html(os.path.join(dir_name, "scatter_categories.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.scatter_matrix(iris)
fig.write_html(os.path.join(dir_name, "scatter_matrix.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.scatter_matrix(
    iris,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color="species",
)
fig.write_html(os.path.join(dir_name, "scatter_matrix_dimensions.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.parallel_coordinates(
    iris,
    color="species_id",
    labels={
        "species_id": "Species",
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_width": "Petal Width",
        "petal_length": "Petal Length",
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2,
)
fig.write_html(os.path.join(dir_name, "parallel_coordinates.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.parallel_categories(
    tips, color="size", color_continuous_scale=px.colors.sequential.Inferno
)
fig.write_html(os.path.join(dir_name, "parallel_categories.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color="size",
    facet_col="sex",
    color_continuous_scale=px.colors.sequential.Viridis,
    render_mode="webgl",
)
fig.write_html(os.path.join(dir_name, "scatter_webgl.html"))

import plotly.express as px

gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
fig.write_html(os.path.join(dir_name, "scatter_hover.html"))

import plotly.express as px

gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    facet_col="continent",
    log_x=True,
    size_max=45,
    range_x=[100, 100000],
    range_y=[25, 90],
)
fig.write_html(os.path.join(dir_name, "scatter_log.html"), auto_play=False)

import plotly.express as px

gapminder = px.data.gapminder()
fig = px.line(
    gapminder,
    x="year",
    y="lifeExp",
    color="continent",
    line_group="country",
    hover_name="country",
    line_shape="spline",
    render_mode="svg",
)
fig.write_html(os.path.join(dir_name, "line.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.scatter(
    tips,
    x="day",
    y="tip",
    facet_col="day",
    facet_col_wrap=2,
    category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
)
fig.write_html(os.path.join(dir_name, "facet_wrap_neat.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.scatter(
    tips,
    x="day",
    y="tip",
    color="sex",
    facet_col="day",
    facet_col_wrap=3,
    category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
)
fig.write_html(os.path.join(dir_name, "facet_wrap_ragged.html"))

import plotly.express as px

gapminder = px.data.gapminder()
fig = px.area(gapminder, x="year", y="pop", color="continent", line_group="country")
fig.write_html(os.path.join(dir_name, "area.html"))

# #### Visualize Distributions

import plotly.express as px

iris = px.data.iris()
fig = px.density_contour(iris, x="sepal_width", y="sepal_length")
fig.write_html(os.path.join(dir_name, "density_contour.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.density_contour(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="rug",
    marginal_y="histogram",
)
fig.write_html(os.path.join(dir_name, "density_contour_marginal.html"))

import plotly.express as px

iris = px.data.iris()
fig = px.density_heatmap(
    iris, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram"
)
fig.write_html(os.path.join(dir_name, "density_heatmap.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group")
fig.write_html(os.path.join(dir_name, "bar.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.bar(
    tips,
    x="sex",
    y="total_bill",
    color="smoker",
    barmode="group",
    facet_row="time",
    facet_col="day",
    category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]},
)
fig.write_html(os.path.join(dir_name, "bar_facet.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.histogram(
    tips, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=tips.columns
)
fig.write_html(os.path.join(dir_name, "histogram.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.histogram(
    tips,
    x="sex",
    y="tip",
    histfunc="avg",
    color="smoker",
    barmode="group",
    facet_row="time",
    facet_col="day",
    category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]},
)
fig.write_html(os.path.join(dir_name, "histogram_histfunc.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.strip(tips, x="total_bill", y="time", orientation="h", color="smoker")
fig.write_html(os.path.join(dir_name, "strip.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.box(tips, x="day", y="total_bill", color="smoker", notched=True)
fig.write_html(os.path.join(dir_name, "box.html"))

import plotly.express as px

tips = px.data.tips()
fig = px.violin(
    tips,
    y="tip",
    x="smoker",
    color="sex",
    box=True,
    points="all",
    hover_data=tips.columns,
)
fig.write_html(os.path.join(dir_name, "violin.html"))

# #### Ternary Coordinates

import plotly.express as px

election = px.data.election()
fig = px.scatter_ternary(
    election,
    a="Joly",
    b="Coderre",
    c="Bergeron",
    color="winner",
    size="total",
    hover_name="district",
    size_max=15,
    color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"},
)
fig.write_html(os.path.join(dir_name, "scatter_ternary.html"))

import plotly.express as px

election = px.data.election()
fig = px.line_ternary(
    election, a="Joly", b="Coderre", c="Bergeron", color="winner", line_dash="winner"
)
fig.write_html(os.path.join(dir_name, "line_ternary.html"))

import plotly.express as px
import numpy as np

img_rgb = np.array(
    [[[255, 0, 0], [0, 255, 0], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [255, 0, 0]]],
    dtype=np.uint8,
)
fig = px.imshow(img_rgb)
fig.write_html(os.path.join(dir_name, "imshow.html"))

# #### 3D Coordinates

import plotly.express as px

election = px.data.election()
fig = px.scatter_3d(
    election,
    x="Joly",
    y="Coderre",
    z="Bergeron",
    color="winner",
    size="total",
    hover_name="district",
    symbol="result",
    color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"},
)
fig.write_html(os.path.join(dir_name, "scatter_3d.html"))

import plotly.express as px

election = px.data.election()
fig = px.line_3d(
    election, x="Joly", y="Coderre", z="Bergeron", color="winner", line_dash="winner"
)
fig.write_html(os.path.join(dir_name, "line_3d.html"))

# #### Polar Coordinates

import plotly.express as px

wind = px.data.wind()
fig = px.scatter_polar(
    wind,
    r="frequency",
    theta="direction",
    color="strength",
    symbol="strength",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1],
)
fig.write_html(os.path.join(dir_name, "scatter_polar.html"))

import plotly.express as px

wind = px.data.wind()
fig = px.line_polar(
    wind,
    r="frequency",
    theta="direction",
    color="strength",
    line_close=True,
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1],
)
fig.write_html(os.path.join(dir_name, "line_polar.html"))

import plotly.express as px

wind = px.data.wind()
fig = px.bar_polar(
    wind,
    r="frequency",
    theta="direction",
    color="strength",
    template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1],
)
fig.write_html(os.path.join(dir_name, "bar_polar.html"))

# #### Maps

import plotly.express as px

carshare = px.data.carshare()
fig = px.scatter_mapbox(
    carshare,
    lat="centroid_lat",
    lon="centroid_lon",
    color="peak_hour",
    size="car_hours",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=15,
    zoom=10,
)
fig.write_html(os.path.join(dir_name, "scatter_mapbox.html"))

import plotly.express as px

carshare = px.data.carshare()
fig = px.line_mapbox(
    carshare, lat="centroid_lat", lon="centroid_lon", color="peak_hour"
)
fig.write_html(os.path.join(dir_name, "line_mapbox.html"))

import plotly.express as px

sample_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "the_polygon",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]]
                ],
            },
        }
    ],
}
fig = px.choropleth_mapbox(
    geojson=sample_geojson, locations=["the_polygon"], color=[10], zoom=6,
)
fig.write_html(os.path.join(dir_name, "choropleth_mapbox.html"), auto_play=False)

import plotly.express as px

carshare = px.data.carshare()
fig = px.density_mapbox(
    carshare, lat="centroid_lat", lon="centroid_lon", z="peak_hour",
)
fig.write_html(os.path.join(dir_name, "density_mapbox.html"), auto_play=False)

import plotly.express as px


gapminder = px.data.gapminder()
fig = px.scatter_geo(
    gapminder,
    locations="iso_alpha",
    color="continent",
    hover_name="country",
    size="pop",
    animation_frame="year",
    projection="natural earth",
)
fig.write_html(os.path.join(dir_name, "scatter_geo.html"), auto_play=False)

import plotly.express as px

gapminder = px.data.gapminder()
fig = px.line_geo(
    gapminder.query("year==2007"),
    locations="iso_alpha",
    color="continent",
    projection="orthographic",
)
fig.write_html(os.path.join(dir_name, "line_geo.html"))

import plotly.express as px

gapminder = px.data.gapminder()
fig = px.choropleth(
    gapminder,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",
    range_color=[20, 80],
)
fig.write_html(os.path.join(dir_name, "choropleth.html"), auto_play=False)

import plotly.express as px

tips = px.data.tips()
fig = px.pie(tips, names="smoker", values="total_bill")
fig.write_html(os.path.join(dir_name, "pie.html"), auto_play=False)

import plotly.express as px

tips = px.data.tips()
fig = px.funnel_area(tips, names="smoker", values="total_bill")
fig.write_html(os.path.join(dir_name, "funnel_area.html"), auto_play=False)

import plotly.express as px

fig = px.treemap(
    names=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
)
fig.write_html(os.path.join(dir_name, "treemap.html"), auto_play=False)


import plotly.express as px

fig = px.sunburst(
    names=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
)
fig.write_html(os.path.join(dir_name, "sunburst.html"), auto_play=False)


import plotly.express as px

fig = px.funnel(
    y=["first", "second", "first", "second"], x=[3, 1, 4, 2], color=["A", "A", "B", "B"]
)
fig.write_html(os.path.join(dir_name, "funnel.html"), auto_play=False)
