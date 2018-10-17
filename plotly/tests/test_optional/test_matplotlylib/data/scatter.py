from __future__ import absolute_import

import plotly.graph_objs as go

D = dict(
    x1=[1, 2, 2, 4, 5, 6, 1, 7, 8, 5, 3],
    y1=[5, 3, 7, 2, 9, 7, 8, 4, 5, 9, 2],
    x2=[-1, 1, -0.3, -0.6, 0.4, 0.8, -0.1, 0.7],
    y2=[-0.5, 0.4, 0.7, -0.6, 0.3, -1, 0, 0.3]
)


SIMPLE_SCATTER = go.Figure(
    data=[
        go.Scatter(
            x=[1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 1.0, 7.0, 8.0, 5.0, 3.0],
            y=[5.0, 3.0, 7.0, 2.0, 9.0, 7.0, 8.0, 4.0, 5.0, 9.0, 2.0],
            mode='markers',
            marker=go.scatter.Marker(
                symbol='circle',
                line=dict(
                    color='rgba(31,119,180,1.0)',
                    width=1.0
                ),
                size=6.0,
                color='rgba(31,119,180,1.0)',
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
            range=[0.64334677419354847, 8.3566532258064505],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=10,
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
            range=[1.6410714285714287, 9.3589285714285726],
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

DOUBLE_SCATTER = go.Figure(
    data=[
        go.Scatter(
            x=[1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 1.0, 7.0, 8.0, 5.0, 3.0],
            y=[5.0, 3.0, 7.0, 2.0, 9.0, 7.0, 8.0, 4.0, 5.0, 9.0, 2.0],
            mode='markers',
            marker=go.scatter.Marker(
                symbol='triangle-up',
                line=dict(
                    color='rgba(255,0,0,0.5)',
                    width=1.0
                ),
                size=11.0,
                color='rgba(255,0,0,0.5)',
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        go.Scatter(
            x=[-1.0, 1.0, -0.3, -0.6, 0.4, 0.8, -0.1, 0.7],
            y=[-0.5, 0.4, 0.7, -0.6, 0.3, -1.0, 0.0, 0.3],
            mode='markers',
            marker=go.scatter.Marker(
                symbol='square',
                line=dict(
                    color='rgba(128,0,128,0.5)',
                    width=1.0
                ),
                size=8.0,
                color='rgba(128,0,128,0.5)',
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
            range=[-1.5159626203173777, 8.4647578206295506],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=7,
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
            range=[-1.588616071428572, 9.5198093820861693],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=7,
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
