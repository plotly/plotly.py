"""
graph_objs_meta
============

A module that contains language data for plotly. There is not meant to be
functionality here, only definitions for use with the graph_objs module.

The formatting of the INFO keys is VERY specific. Each key is exactly:

graph_obj.Obj.__class__.__name__.lower()

Where Obj is a class subclassing from list or dict in the graph_objs module.
This must by strictly followed.

"""
# TODO: fill in all 'valid' keys
# TODO: match all 'valid' keys to appropriate 'types' dict
# TODO: match all 'valid' keys to appropriate 'descriptors' dict
# TODO: SORT keys from most important to least important for each obj
# TODO: for help: with keys taking a DISCRETE number of opts, include all opts.

# key types are EITHER 'data', 'plot_info', 'structure', 'style'

INFO = dict(

    plotlylist=dict(),

    data=dict(),

    annotations=dict(),

    plotlydict=dict(),

    plotlytrace=dict(),

    bar=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='bar'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Bar(...)."),
    ),

    box=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='box'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Box(...)."),
    ),

    contour=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='contour'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Contour(...)."),
    ),

    heatmap=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='heatmap'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Heatmap(...)."),
    ),

    histogram2d=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='histogram2d'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Histogram2d(...)."),
    ),

    histogramx=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='histogramx'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Histogramx(...)."),
    ),

    histogramy=dict(
        type=dict(required=True, type='plot_info',
                  val_types="default: type='histogramy'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Histogramy(...)."),
    ),

    scatter=dict(
        x=dict(required=True, type='data',
               val_types="'data-array', numbers, datetimes, strings",
               description="the x coordinate from the (x,y) pair on the "
                           "scatter plot."),
        y=dict(required=True, type='data',
               val_types="'data-array', numbers, datetimes, strings",
               description="the y coordinate from the (x,y) pair on the "
                           "scatter plot."),
        type=dict(required=True, type='plot_info',
                  val_types="default: type='scatter'",
                  description="Plotly identifier for trace type, this is set "
                              "automatcally with a call to Scatter(...)."),
        mode=dict(required=False, type='plot_info',
                  val_types="string: 'lines' | 'markers' | 'text' | "
                            "'lines+markers' | 'lines+text' | etc.",
                  description="Plotting mode (style) for the scatter plot."),
        name=dict(required=False, type='plot_info',
                  val_types="string",
                  description="The label associated with this scatter trace. "
                              "For example, this is linked to the column "
                              "header of your data in plotly and it will "
                              "appear in the legend."),
        line=dict(required=False, type='structure',
                  val_types="Line object or dict",
                  description="A dictionary-like object containing "
                              "information about the line connecting points "
                              "on the scatter plot."),
        marker=dict(required=False, type='structure',
                    val_types="Marker object or dict",
                  description="A dictionary-like object containing "
                              "information about the marker style of the "
                              "scatter plot."),
        opacity=dict(required=False, type='style',
                     val_types="number in [0, 1]",
                     description="Also known as 'alpha', this number "
                                 "determines how easy it is to see objects "
                                 "'beneath' this one."),
        showlegend=dict(required=False, type='plot_info',
                        val_types="True | False",
                        description="This determines whether or not the "
                                    "resulting trace from the given (x, y)"
                                    " pairs will show up in the plot legend."),
        xaxis=dict(required=False, type='structure',
                   val_types="string: 'x', 'x2', 'x3', etc.",
                   description="This key determines which xaxis the x "
                               "coordinates in the given (x, y) pair will "
                               "reference in the figure."),
        yaxis=dict(required=False, type='structure',
                   val_types="string: 'y', 'y2', 'y3', etc.",
                   description="This key determines which xaxis the y "
                               "coordinates in the given (x, y) pair will "
                               "reference in the figure."),
        error_y=dict(required=False, type='structure',
                     val_types="coming soon!",
                     description="coming soon!"),
        textfont=dict(required=False, type='stucture',
                      val_types="Font or dict",
                      description="coming soon!")
    ),

    annotation=dict(
        text=dict(required=False, type='plot_info',
                  val_types="coming soon!",
                  descriptors="coming soon!"),
        bordercolor=dict(),
        borderwidth=dict(),
        borderpad=dict(),
        bgcolor=dict(),
        xref=dict(required=False, type='plot_info',
                  val_types="coming soon!",
                  description="coming soon!"),
        yref=dict(required=False, type='plot_info',
                  val_types="coming soon!",
                  description="coming soon!"),
        showarrow=dict(required=False, type='plot_info',
                       val_types="coming soon!",
                       description="coming soon!"),
        arrowwidth=dict(),
        arrowcolor=dict(),
        arrowhead=dict(),
        arrowsize=dict(),
        tag=dict(),
        font=dict(),
        opacity=dict(),
        align=dict(required=False, type='plot_info',
                   val_types="coming soon!",
                   description="coming soon!"),
        xanchor=dict(required=False, type='plot_info',
                     val_types="coming soon!",
                     description="coming soon!"),
        yanchor=dict(),
        ay=dict(),
        ax=dict(),
        y=dict(),
        x=dict()
    ),

    figure=dict(
        data=dict(),
        layout=dict(),
    ),

    font=dict(
        color=dict(),
        size=dict(),
        family=dict(),
    ),

    layout=dict(
        title=dict(),
        xaxis=dict(),
        yaxis=dict(),
        legend=dict(),
        width=dict(),
        height=dict(),
        autosize=dict(),
        margin=dict(),
        paper_bgcolor=dict(),
        plot_bgcolor=dict(),
        barmode=dict(),
        bargroupgap=dict(),
        boxmode=dict(),
        boxgap=dict(),
        boxgroupgap=dict(),
        font=dict(),
        titlefont=dict(),
        dragmode=dict(),
        hovermode=dict(),
        separators=dict(),
        hidesources=dict(),
        showlegend=dict(),
        annotations=dict()
    ),

    legend=dict(
        bgcolor=dict(),
        bordercolor=dict(),
        font=dict(),
        traceorder=dict()
    ),

    line=dict(
        dash=dict(),
        color=dict(),
        width=dict(),
        opacity=dict(),
    ),

    margin=dict(
        l=dict(),
        r=dict(),
        b=dict(),
        t=dict(),
        pad=dict()
    ),

    marker=dict(
        symbol=dict(),
        line=dict(),
        size=dict(),
        color=dict(),
        opacity=dict()
    ),

    xaxis=dict(
        range=dict(),
        type=dict(),
        showline=dict(),
        mirror=dict(),
        linecolor=dict(),
        linewidth=dict(),
        tick0=dict(),
        dtick=dict(),
        ticks=dict(),
        ticklen=dict(),
        tickcolor=dict(),
        nticks=dict(),
        showticklabels=dict(),
        tickangle=dict(),
        exponentformat=dict(),
        showgrid=dict(),
        gridcolor=dict(),
        gridwidth=dict(),
        autorange=dict(),
        rangemode=dict(),
        autotick=dict(),
        zeroline=dict(),
        zerolinecolor=dict(),
        zerolinewidth=dict(),
        titlefont=dict(),
        tickfont=dict(),
        overlaying=dict(),
        domain=dict(),
        position=dict(),
        anchor=dict(),
        title=dict()
    ),

    yaxis=dict(
        range=dict(),
        type=dict(),
        showline=dict(),
        mirror=dict(),
        linecolor=dict(),
        linewidth=dict(),
        tick0=dict(),
        dtick=dict(),
        ticks=dict(),
        ticklen=dict(),
        tickcolor=dict(),
        nticks=dict(),
        showticklabels=dict(),
        tickangle=dict(),
        exponentformat=dict(),
        showgrid=dict(),
        gridcolor=dict(),
        gridwidth=dict(),
        autorange=dict(),
        rangemode=dict(),
        autotick=dict(),
        zeroline=dict(),
        zerolinecolor=dict(),
        zerolinewidth=dict(),
        titlefont=dict(),
        tickfont=dict(),
        overlaying=dict(),
        domain=dict(),
        position=dict(),
        anchor=dict(),
        title=dict()
    ),

    errorx=dict(),

    errory=dict(),

    titlefont=dict()
)