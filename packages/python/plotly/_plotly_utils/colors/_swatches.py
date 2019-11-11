def _swatches(module_names, module_contents, template=None):
    """
    Parameters
    ----------
    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name or definition.

    Returns
    -------
    fig : graph_objects.Figure containing the displayed image
        A `Figure` object. This figure demonstrates the color scales and
        sequences in this module, as stacked bar charts.
    """
    import plotly.graph_objs as go
    from plotly.express._core import apply_default_cascade

    args = dict(template=template)
    apply_default_cascade(args)

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
            title="plotly.colors." + module_names.split(".")[-1],
            barmode="stack",
            barnorm="fraction",
            bargap=0.5,
            showlegend=False,
            xaxis=dict(range=[-0.02, 1.02], showticklabels=False, showgrid=False),
            height=max(600, 40 * len(sequences)),
            template=args["template"],
        ),
    )
