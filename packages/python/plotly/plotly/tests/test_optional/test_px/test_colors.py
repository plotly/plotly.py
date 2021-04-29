import plotly.express as px


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
