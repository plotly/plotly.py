from __future__ import absolute_import

import plotly.graph_objs as go

D = dict(
    left=[0, 1, 2, 3, 4, 5],
    height=[10, 20, 50, 80, 100, 200],
    bottom=[0, 1, 2, 3, 4, 5, 6],
    width=[1, 4, 8, 16, 32, 64, 128],
    multi_left=[0, 10, 20, 30, 40, 50],
    multi_height=[1, 4, 8, 16, 32, 64],
    multi_bottom=[15, 30, 45, 60, 75, 90],
    multi_width=[30, 60, 20, 50, 60, 30]
)

VERTICAL_BAR = go.Figure(
    data=[
        go.Bar(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            orientation='v',
            marker=go.bar.Marker(
                line=dict(
                    width=1.0
                ),
                color='#1F77B4'
            ),
            opacity=1,
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
        bargap=0.2,
        xaxis1=go.layout.XAxis(
            domain=[0.0, 1.0],
            range=[-0.68999999999999995, 5.6899999999999995],
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
            range=[0.0, 210.0],
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

HORIZONTAL_BAR = go.Figure(
    data=[
        go.Bar(
            x=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
            y=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            orientation='h',
            marker=go.bar.Marker(
                line=dict(
                    width=1.0
                ),
                color='#1F77B4'
            ),
            opacity=1,
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
        bargap=0.19999999999999996,
        xaxis1=go.layout.XAxis(
            domain=[0.0, 1.0],
            range=[0.0, 134.40000000000001],
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
            range=[-0.73999999999999999, 6.7399999999999993],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=9,
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

H_AND_V_BARS = go.Figure(
    data=[
        go.Bar(
            x=[0.0, 10.0, 20.0, 30.0, 40.0, 50.0],
            y=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0],
            orientation='v',
            marker=go.bar.Marker(
                line=dict(
                    width=1.0
                ),
                color='#008000'
            ),
            opacity=0.5,
            xaxis='x1',
            yaxis='y1'
        ),
        go.Bar(
            x=[30.0, 60.0, 20.0, 50.0, 60.0, 30.0],
            y=[15.0, 30.0, 45.0, 60.0, 75.0, 90.0],
            orientation='h',
            marker=go.bar.Marker(
                line=dict(
                    width=1.0
                ),
                color='#FF0000'
            ),
            opacity=0.5,
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
        bargap=1,
        xaxis1=go.layout.XAxis(
            domain=[0.0, 1.0],
            range=[-8.25, 63.25],
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
            range=[0.0, 101.84999999999999],
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


