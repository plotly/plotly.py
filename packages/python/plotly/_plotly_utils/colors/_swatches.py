def _swatches(module_names, module_contents):
    """
    Returns:
        A `Figure` object. This figure demonstrates the color scales and
        sequences in this module as stacked bar charts against the default
        template's background.
    """
    import plotly.graph_objs as go
    import plotly.express as px

    sequences = [
        (k, v)
        for k, v in module_contents.items()
        if not (k.startswith("_") or k == "swatches")
    ]

    return go.Figure(
        data=[
            go.Bar(
                orientation="h",
                y=[name] * len(colors),
                x=[1] * len(colors),
                customdata=list(range(len(colors))),
                marker=dict(color=colors),
                hovertemplate="%{y}[%{customdata}] = %{marker.color}<extra></extra>",
            )
            for name, colors in reversed(sequences)
        ],
        layout=dict(
            title=module_names.split(".")[-1].capitalize() + " colorscales",
            barmode="stack",
            barnorm="fraction",
            template=px.defaults.template,
            bargap=0.5,
            showlegend=False,
            xaxis=dict(range=[-0.02, 1.02], showticklabels=False, showgrid=False),
            height=max(px.defaults.height, 40 * len(sequences)),
            width=px.defaults.width,
        ),
    )
