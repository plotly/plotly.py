import os
import shutil
import tempfile

import numpy as np
import pandas as pd
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import plotly.express as px
from plotly.io import write_images

IMAGE_TEST_ROOT_DIR = os.path.join("tests", "image")
BASELINE_IMAGE_DIR = os.path.join(IMAGE_TEST_ROOT_DIR, "baselines")


class TestFigures:
    def fig_scatter(self):
        iris = px.data.iris()
        return px.scatter(iris, x="sepal_width", y="sepal_length")

    def fig_scatter_color(self):
        iris = px.data.iris()
        return px.scatter(iris, x="sepal_width", y="sepal_length", color="species")

    def fig_scatter_marginal(self):
        iris = px.data.iris()
        return px.scatter(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            marginal_y="rug",
            marginal_x="histogram",
        )

    def fig_scatter_trendline(self):
        iris = px.data.iris()
        return px.scatter(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            marginal_y="violin",
            marginal_x="box",
            trendline="ols",
        )

    def fig_scatter_errorbar(self):
        iris = px.data.iris()
        iris["e"] = iris["sepal_width"] / 100
        return px.scatter(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            error_x="e",
            error_y="e",
        )

    def fig_scatter_categories(self):
        tips = px.data.tips()
        return px.scatter(
            tips,
            x="total_bill",
            y="tip",
            facet_row="time",
            facet_col="day",
            color="smoker",
            trendline="ols",
            category_orders={
                "day": ["Thur", "Fri", "Sat", "Sun"],
                "time": ["Lunch", "Dinner"],
            },
        )

    def fig_scatter_matrix(self):
        iris = px.data.iris()
        return px.scatter_matrix(iris)

    def fig_scatter_matrix_dimensions(self):
        iris = px.data.iris()
        return px.scatter_matrix(
            iris,
            dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
            color="species",
        )

    def fig_parallel_coordinates(self):
        iris = px.data.iris()
        return px.parallel_coordinates(
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

    def fig_parallel_categories(self):
        tips = px.data.tips()
        return px.parallel_categories(
            tips,
            color="size",
            color_continuous_scale=px.colors.sequential.Inferno,
        )

    def fig_scatter_webgl(self):
        tips = px.data.tips()
        return px.scatter(
            tips,
            x="total_bill",
            y="tip",
            color="size",
            facet_col="sex",
            color_continuous_scale=px.colors.sequential.Viridis,
            render_mode="webgl",
        )

    def fig_scatter_hover(self):
        gapminder = px.data.gapminder()
        return px.scatter(
            gapminder.query("year==2007"),
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            size_max=60,
        )

    def fig_scatter_log(self):
        gapminder = px.data.gapminder()
        return px.scatter(
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

    def fig_line(self):
        gapminder = px.data.gapminder()
        return px.line(
            gapminder,
            x="year",
            y="lifeExp",
            color="continent",
            line_group="country",
            hover_name="country",
            line_shape="spline",
            render_mode="svg",
        )

    def fig_facet_wrap_neat(self):
        tips = px.data.tips()
        return px.scatter(
            tips,
            x="day",
            y="tip",
            facet_col="day",
            facet_col_wrap=2,
            category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        )

    def fig_facet_wrap_ragged(self):
        tips = px.data.tips()
        return px.scatter(
            tips,
            x="day",
            y="tip",
            color="sex",
            facet_col="day",
            facet_col_wrap=3,
            category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        )

    def fig_area(self):
        gapminder = px.data.gapminder()
        return px.area(
            gapminder, x="year", y="pop", color="continent", line_group="country"
        )

    def fig_density_contour(self):
        iris = px.data.iris()
        return px.density_contour(iris, x="sepal_width", y="sepal_length")

    def fig_density_contour_marginal(self):
        iris = px.data.iris()
        return px.density_contour(
            iris,
            x="sepal_width",
            y="sepal_length",
            color="species",
            marginal_x="rug",
            marginal_y="histogram",
        )

    def fig_density_heatmap(self):
        iris = px.data.iris()
        return px.density_heatmap(
            iris,
            x="sepal_width",
            y="sepal_length",
            marginal_x="rug",
            marginal_y="histogram",
        )

    def fig_bar(self):
        tips = px.data.tips()
        return px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group")

    def fig_bar_facet(self):
        tips = px.data.tips()
        return px.bar(
            tips,
            x="sex",
            y="total_bill",
            color="smoker",
            barmode="group",
            facet_row="time",
            facet_col="day",
            category_orders={
                "day": ["Thur", "Fri", "Sat", "Sun"],
                "time": ["Lunch", "Dinner"],
            },
        )

    def fig_histogram(self):
        tips = px.data.tips()
        return px.histogram(
            tips,
            x="total_bill",
            y="tip",
            color="sex",
            marginal="rug",
            hover_data=tips.columns,
        )

    def fig_histogram_histfunc(self):
        tips = px.data.tips()
        return px.histogram(
            tips,
            x="sex",
            y="tip",
            histfunc="avg",
            color="smoker",
            barmode="group",
            facet_row="time",
            facet_col="day",
            category_orders={
                "day": ["Thur", "Fri", "Sat", "Sun"],
                "time": ["Lunch", "Dinner"],
            },
        )

    def fig_strip(self):
        tips = px.data.tips()
        return px.strip(tips, x="total_bill", y="time", orientation="h", color="smoker")

    def fig_box(self):
        tips = px.data.tips()
        return px.box(tips, x="day", y="total_bill", color="smoker", notched=True)

    def fig_violin(self):
        tips = px.data.tips()
        return px.violin(
            tips,
            y="tip",
            x="smoker",
            color="sex",
            box=True,
            points="all",
            hover_data=tips.columns,
        )

    def fig_scatter_ternary(self):
        election = px.data.election()
        return px.scatter_ternary(
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

    def fig_line_ternary(self):
        election = px.data.election()
        return px.line_ternary(
            election,
            a="Joly",
            b="Coderre",
            c="Bergeron",
            color="winner",
            line_dash="winner",
        )

    def fig_imshow(self):
        img_rgb = np.array(
            [
                [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                [[0, 255, 0], [0, 0, 255], [255, 0, 0]],
            ],
            dtype=np.uint8,
        )
        return px.imshow(img_rgb)

    def fig_scatter_3d(self):
        election = px.data.election()
        return px.scatter_3d(
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

    def fig_line_3d(self):
        election = px.data.election()
        return px.line_3d(
            election,
            x="Joly",
            y="Coderre",
            z="Bergeron",
            color="winner",
            line_dash="winner",
        )

    def fig_scatter_polar(self):
        wind = px.data.wind()
        return px.scatter_polar(
            wind,
            r="frequency",
            theta="direction",
            color="strength",
            symbol="strength",
            color_discrete_sequence=px.colors.sequential.Plasma[-2::-1],
        )

    def fig_line_polar(self):
        wind = px.data.wind()
        return px.line_polar(
            wind,
            r="frequency",
            theta="direction",
            color="strength",
            line_close=True,
            color_discrete_sequence=px.colors.sequential.Plasma[-2::-1],
        )

    def fig_bar_polar(self):
        wind = px.data.wind()
        return px.bar_polar(
            wind,
            r="frequency",
            theta="direction",
            color="strength",
            template="plotly_dark",
            color_discrete_sequence=px.colors.sequential.Plasma[-2::-1],
        )

    def fig_scatter_map(self):
        carshare = px.data.carshare()
        return px.scatter_map(
            carshare,
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            size="car_hours",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=10,
        )

    def fig_line_map(self):
        carshare = px.data.carshare()
        return px.line_map(
            carshare, lat="centroid_lat", lon="centroid_lon", color="peak_hour"
        )

    def fig_choropleth_map(self):
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
        return px.choropleth_map(
            geojson=sample_geojson,
            locations=["the_polygon"],
            color=[10],
            zoom=6,
        )

    def fig_density_map(self):
        carshare = px.data.carshare()
        return px.density_map(
            carshare,
            lat="centroid_lat",
            lon="centroid_lon",
            z="peak_hour",
        )

    def fig_scatter_geo(self):
        gapminder = px.data.gapminder()
        return px.scatter_geo(
            gapminder,
            locations="iso_alpha",
            color="continent",
            hover_name="country",
            size="pop",
            animation_frame="year",
            projection="natural earth",
        )

    def fig_line_geo(self):
        gapminder = px.data.gapminder()
        return px.line_geo(
            gapminder.query("year==2007"),
            locations="iso_alpha",
            color="continent",
            projection="orthographic",
        )

    def fig_choropleth(self):
        gapminder = px.data.gapminder()
        return px.choropleth(
            gapminder,
            locations="iso_alpha",
            color="lifeExp",
            hover_name="country",
            animation_frame="year",
            range_color=[20, 80],
        )

    def fig_pie(self):
        tips = px.data.tips()
        return px.pie(tips, names="smoker", values="total_bill")

    def fig_funnel_area(self):
        tips = px.data.tips()
        return px.funnel_area(tips, names="smoker", values="total_bill")

    def fig_treemap(self):
        return px.treemap(
            names=[
                "Eve",
                "Cain",
                "Seth",
                "Enos",
                "Noam",
                "Abel",
                "Awan",
                "Enoch",
                "Azura",
            ],
            parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
        )

    def fig_sunburst(self):
        return px.sunburst(
            names=[
                "Eve",
                "Cain",
                "Seth",
                "Enos",
                "Noam",
                "Abel",
                "Awan",
                "Enoch",
                "Azura",
            ],
            parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
        )

    def fig_funnel(self):
        return px.funnel(
            y=["first", "second", "first", "second"],
            x=[3, 1, 4, 2],
            color=["A", "A", "B", "B"],
        )

    def fig_scatter_bool_color(self):
        return px.scatter(
            x=[1, 2, 1, 2], y=[4, 3, 2, 4], color=[True, True, False, False]
        )

    def fig_pie_bool_color(self):
        return px.pie(values=[1, 2, 3, 4], color=[True, False, True, False])

    def fig_choropleth_bool_color(self):
        df = px.data.gapminder().query("year == 2007")
        np.random.seed(0)
        df["color"] = np.random.choice([True, False], len(df))
        return px.choropleth(df, locations="iso_alpha", color="color")

    def fig_density_contour_bool_color(self):
        df = px.data.iris()
        df["is_setosa"] = df["species"] == "setosa"
        return px.density_contour(
            df, x="sepal_width", y="sepal_length", color="is_setosa"
        )

    def fig_sunburst_bool_color(self):
        return px.sunburst(
            path=[["yes", "no", "no"], ["yes", "no", "a"]], color=[True, False, True]
        )

    def fig_timeline(self):
        df = pd.DataFrame(
            [
                dict(Task="Job A", Start="2009-01-01", Finish="2009-02-28"),
                dict(Task="Job B", Start="2009-03-05", Finish="2009-04-15"),
                dict(Task="Job C", Start="2009-02-20", Finish="2009-05-30"),
            ]
        )
        return px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")


def make_images(out_dir: str):
    fig_funcs = [
        getattr(TestFigures, name)
        for name in dir(TestFigures)
        if name.startswith("fig_")
    ]
    figs = [f(TestFigures()) for f in fig_funcs]
    fig_filenames = [os.path.join(out_dir, f"{f.__name__[4:]}.png") for f in fig_funcs]
    write_images(fig=figs, file=fig_filenames, validate=False)


def remake_baselines():
    print("Generating baseline images...")
    make_images(BASELINE_IMAGE_DIR)


def compare_image_dirs(baseline_dir: str, compare_to_dir: str, diff_dir: str = ""):
    print(f"Comparing images in {baseline_dir} and {compare_to_dir}...")
    success = True

    baseline_filenames = sorted(os.listdir(baseline_dir))
    compare_to_filenames = sorted(os.listdir(compare_to_dir))

    # Check for missing or extra images
    if baseline_filenames != compare_to_filenames:
        missing_list = list(set(baseline_filenames) - set(compare_to_filenames))
        extra_list = list(set(compare_to_filenames) - set(baseline_filenames))

        if missing_list:
            success = False
            print(f"Missing images: {missing_list}")
        if extra_list:
            success = False
            print(f"Extra images: {extra_list}")
            if diff_dir:
                for filename in extra_list:
                    shutil.copy(
                        os.path.join(compare_to_dir, filename),
                        os.path.join(diff_dir, filename),
                    )

    # Compare individual image files
    for filename in baseline_filenames:
        baseline_image_path = os.path.join(baseline_dir, filename)
        compare_to_image_path = os.path.join(compare_to_dir, filename)
        diff_path = os.path.join(diff_dir, filename)

        if not images_equal(baseline_image_path, compare_to_image_path, diff_path):
            print(f"Image {filename} does not match baseline")
            success = False

    return success


def images_equal(
    img_baseline_path: str, img_compare_path: str, img_diff_path: str = ""
):
    img_baseline = Image.open(img_baseline_path)
    img_compare = Image.open(img_compare_path)
    img_diff = Image.new("RGBA", img_baseline.size)
    mismatch = pixelmatch(img_baseline, img_compare, img_diff, includeAA=True)
    if img_diff_path and mismatch > 0:
        img_diff.save(img_diff_path)
    return mismatch == 0


def verify():
    temp_image_dir = tempfile.TemporaryDirectory(dir=IMAGE_TEST_ROOT_DIR)
    temp_diff_dir = tempfile.TemporaryDirectory(dir=IMAGE_TEST_ROOT_DIR)
    try:
        # Make new images
        make_images(temp_image_dir.name)

        # Compare new images to baselines
        success = compare_image_dirs(
            BASELINE_IMAGE_DIR, temp_image_dir.name, temp_diff_dir.name
        )
        if success:
            print("Images match baselines.")
        else:
            print("Images do not match baselines.")
        return success
    finally:
        temp_image_dir.cleanup()
        temp_diff_dir.cleanup()


if __name__ == "__main__":
    remake_baselines()
