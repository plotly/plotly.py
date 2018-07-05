from __future__ import absolute_import

import plotly.graph_objs as go

D = dict(
    x1=[0, 1, 2, 3, 4, 5],
    y1=[10, 20, 50, 80, 100, 200],
    x2=[0, 1, 2, 3, 4, 5, 6],
    y2=[1, 4, 8, 16, 32, 64, 128]
)

SIMPLE_LINE = go.Figure(
    data=[
        go.Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            name='simple',
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
            range=[-0.25, 5.25],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=8,
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
            range=[0.5, 209.5],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=10,
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

COMPLICATED_LINE = go.Figure(
    data=[
        go.Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            name='one',
            mode='markers',
            marker=go.scatter.Marker(
                symbol='circle',
                line=dict(
                    color='#FF0000',
                    width=1.0
                ),
                size=10,
                color='#FF0000',
                opacity=0.5
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        go.Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            name='two',
            mode='lines',
            line=dict(
                dash='solid',
                color='rgba (0, 0, 255, 0.7)',
                width=2
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        go.Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            y=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
            name='three',
            mode='markers',
            marker=go.scatter.Marker(
                symbol='cross',
                line=dict(
                    color='#0000FF',
                    width=2
                ),
                size=10,
                color='#0000FF',
                opacity=0.6
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        go.Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            y=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
            name='four',
            mode='lines',
            line=go.scatter.Line(
                dash='dash',
                color='rgba (255, 0, 0, 0.8)',
                width=2
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
            range=[-0.30000000000000004, 6.2999999999999998],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=9,
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
            range=[-8.9500000000000011, 209.94999999999999],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=11,
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