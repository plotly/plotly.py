from __future__ import absolute_import

from plotly.graph_objs import (Data, Figure, Font, Layout, Line, Margin,
                               Marker, Scatter, XAxis, YAxis)

D = dict(
    x1=[0, 1, 2, 3, 4, 5],
    y1=[10, 20, 50, 80, 100, 200],
    x2=[0, 1, 2, 3, 4, 5, 6],
    y2=[1, 4, 8, 16, 32, 64, 128]
)

SIMPLE_LINE = Figure(
    data=Data([
        Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            name='simple',
            mode='lines',
            line=Line(
                dash='solid',
                color='rgba (0, 0, 255, 1)',
                width=1.0
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
            range=[0.0, 5.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
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
            range=[0.0, 200.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=5,
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

COMPLICATED_LINE = Figure(
    data=Data([
        Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            name='one',
            mode='markers',
            marker=Marker(
                symbol='dot',
                line=Line(
                    color='#000000',
                    width=0.5
                ),
                size=10,
                color='#FF0000',
                opacity=0.5
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            name='two',
            mode='lines',
            line=Line(
                dash='solid',
                color='rgba (0, 0, 255, 0.7)',
                width=2
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            y=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
            name='three',
            mode='markers',
            marker=Marker(
                symbol='cross',
                line=Line(
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
        Scatter(
            x=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            y=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
            name='four',
            mode='lines',
            line=Line(
                dash='dash',
                color='rgba (255, 0, 0, 0.8)',
                width=2
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
            range=[0.0, 6.0],
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
            range=[0.0, 200.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=5,
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
