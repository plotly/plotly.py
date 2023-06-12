import plotly.express as px
import inspect


def test_reversed_colorscale():
    fig1 = px.scatter(
        x=[1, 2], y=[2, 3], color=[3, 4], color_continuous_scale="plasma_r"
    )
    fig2 = px.scatter(x=[1, 2], y=[2, 3], color=[3, 4], color_continuous_scale="plasma")
    colors1 = [val[1] for val in fig1.layout.coloraxis.colorscale]
    colors2 = [val[1] for val in fig2.layout.coloraxis.colorscale]
    assert colors1 == colors2[::-1]
    fig1 = px.scatter(
        x=[1, 2],
        y=[2, 3],
        color=[3, 4],
        color_continuous_scale=px.colors.sequential.Plasma,
    )
    fig2 = px.scatter(
        x=[1, 2],
        y=[2, 3],
        color=[3, 4],
        color_continuous_scale=px.colors.sequential.Plasma_r,
    )
    colors1 = [val[1] for val in fig1.layout.coloraxis.colorscale]
    colors2 = [val[1] for val in fig2.layout.coloraxis.colorscale]
    assert colors1 == colors2[::-1]


def test_r_colorscales():

    for colorscale_members in [
        inspect.getmembers(px.colors.sequential),
        inspect.getmembers(px.colors.diverging),
        inspect.getmembers(px.colors.cyclical),
        inspect.getmembers(px.colors.qualitative),
        inspect.getmembers(px.colors.carto),
        inspect.getmembers(px.colors.cmocean),
        inspect.getmembers(px.colors.colorbrewer),
        inspect.getmembers(px.colors.plotlyjs),
    ]:
        scale_names = [
            c[0]
            for c in colorscale_members
            if isinstance(c, tuple)
            and len(c) == 2
            and isinstance(c[0], str)
            and isinstance(c[1], list)
            and not c[0].startswith("_")
        ]
        for scale in scale_names:
            if scale.endswith("_r"):
                assert scale.replace("_r", "") in scale_names
            else:
                assert scale + "_r" in scale_names
