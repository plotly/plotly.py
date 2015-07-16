from __future__ import absolute_import

from plotly.graph_objs import (Data, Figure, Font, Layout, Line, Margin,
                               Marker, Scatter, XAxis, YAxis)

D = dict(
    x1=[1, 2, 2, 4, 5, 6, 1, 7, 8, 5 ,3],
    y1=[5, 3, 7, 2, 9, 7, 8, 4, 5, 9, 2],
    x2=[-1, 1, -0.3, -0.6, 0.4, 0.8, -0.1, 0.7],
    y2=[-0.5, 0.4, 0.7, -0.6, 0.3, -1, 0, 0.3]
)

SIMPLE_SCATTER = Figure(
    data=Data([
        Scatter(
            x=[1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 1.0, 7.0, 8.0, 5.0, 3.0],
            y=[5.0, 3.0, 7.0, 2.0, 9.0, 7.0, 8.0, 4.0, 5.0, 9.0, 2.0],
            mode='markers',
            marker=Marker(
                symbol='dot',
                line=Line(
                    color='rgba(0,0,0,1.0)',
                    width=1.0
                ),
                size=4.4721359549995796,
                color='rgba(0,0,255,1.0)',
                opacity=1.0
            ),
            xaxis='x1',
            yaxis='y1'
        )
    ]),
    layout=Layout(
        width=640,
        height=480,
        autosize=False,
        margin=Margin(
            l=80,
            r=63,
            b=47,
            t=47,
            pad=0
        ),
        hovermode='closest',
        showlegend=False,
        xaxis1=XAxis(
            domain=[0.0, 1.0],
            range=[0.0, 9.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=10,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y1',
            side='bottom',
            mirror='ticks'
        ),
        yaxis1=YAxis(
            domain=[0.0, 1.0],
            range=[1.0, 10.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=10,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x1',
            side='left',
            mirror='ticks'
        )
    )
)

DOUBLE_SCATTER = Figure(
    data=Data([
        Scatter(
            x=[1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 1.0, 7.0, 8.0, 5.0, 3.0],
            y=[5.0, 3.0, 7.0, 2.0, 9.0, 7.0, 8.0, 4.0, 5.0, 9.0, 2.0],
            mode='markers',
            marker=Marker(
                symbol='triangle-up',
                line=Line(
                    color='rgba(255,0,0,0.5)',
                    width=1.0
                ),
                size=11.0,
                color='rgba(255,0,0,0.5)',
                opacity=0.5
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        Scatter(
            x=[-1.0, 1.0, -0.29999999999999999, -0.59999999999999998,
               0.40000000000000002, 0.80000000000000004, -0.10000000000000001,
               0.69999999999999996],
            y=[-0.5, 0.40000000000000002, 0.69999999999999996,
               -0.59999999999999998, 0.29999999999999999, -1.0, 0.0,
               0.29999999999999999],
            mode='markers',
            marker=Marker(
                symbol='square',
                line=Line(
                    color='rgba(128,0,128,0.5)',
                    width=1.0
                ),
                size=8.0,
                color='rgba(128,0,128,0.5)',
                opacity=0.5
            ),
            xaxis='x1',
            yaxis='y1'
        )
    ]),
    layout=Layout(
        width=640,
        height=480,
        autosize=False,
        margin=Margin(
            l=80,
            r=63,
            b=47,
            t=47,
            pad=0
        ),
        hovermode='closest',
        showlegend=False,
        xaxis1=XAxis(
            domain=[0.0, 1.0],
            range=[-2.0, 10.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=7,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y1',
            side='bottom',
            mirror='ticks'
        ),
        yaxis1=YAxis(
            domain=[0.0, 1.0],
            range=[-2.0, 10.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=7,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x1',
            side='left',
            mirror='ticks'
        )
    )
)
