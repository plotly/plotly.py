from __future__ import absolute_import

import plotly.graph_objs as go

D = dict(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[10, 3, 100, 6, 45, 4, 80, 45, 3, 59])


EVEN_LINEAR_SCALE = go.Figure(
    data=[
        go.Scatter(
            x=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
            y=[10.0, 3.0, 100.0, 6.0, 45.0, 4.0, 80.0, 45.0, 3.0, 59.0],
            name='_line0',
            mode='lines',
            line=go.scatter.Line(
                dash='solid',
                color='rgba (31, 119, 180, 1)',
                width=1.5
            ),
            xaxis='x1',
            yaxis='y1'
        )
    ],
    layout=go.Layout(
        width=640,
        height=480,
        autosize=False,
        margin=go.layout.Margin(
            l=80,
            r=63,
            b=52,
            t=57,
            pad=0
        ),
        hovermode='closest',
        showlegend=False,
        xaxis1=go.layout.XAxis(
            domain=[0.0, 1.0],
            range=[0.0, 18.0],
            type='linear',
            showline=True,
            nticks=10,
            ticks='inside',
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y1',
            side='bottom',
            mirror='ticks'
        ),
        yaxis1=go.layout.YAxis(
            domain=[0.0, 1.0],
            range=[-1.8500000000000005, 195.0],
            type='linear',
            showline=True,
            nticks=10,
            ticks='inside',
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x1',
            side='left',
            mirror='ticks'
        )
    )
)
