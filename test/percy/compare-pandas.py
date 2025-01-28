import difflib
import json
import os

os.chdir(os.path.dirname(__file__))


def get_fig(html):
    # strip off all the rest of the html and js
    fig_str = html[html.index("[{", html.rindex("Plotly.newPlot(")) :]
    fig_str = fig_str[: fig_str.index("}    ") + 1]
    data, layout, config = json.loads(f"[{fig_str}]")
    fig_dict = dict(data=data, layout=layout, config=config)
    return json.dumps(fig_dict, indent=2).splitlines(keepends=True)


for filename in os.listdir("pandas2"):
    if filename not in [
        "density_mapbox.html",
        "density_map.html",
        "scatter_hover.html",
        "scatter_mapbox.html",
        "scatter_map.html",
        "line.html",
        "choropleth.html",
        "line_mapbox.html",
        "line_map.html",
        "scatter_log.html",
    ]:
        with open(filename, encoding="utf-8") as f1:
            with open(os.path.join("pandas2", filename)) as f2:
                fig1 = get_fig(f1.read())
                fig2 = get_fig(f2.read())
                if any(l1 != l2 for l1, l2 in zip(fig1, fig2)):
                    print("".join(difflib.unified_diff(fig1, fig2)))
                    raise ValueError(f"Pandas 1/2 difference in {filename}")
