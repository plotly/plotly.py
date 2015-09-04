from __future__ import absolute_import

from plotly.graph_objs import (Data, Figure, Font, Layout, Line, Margin,
                               Scatter, XAxis, YAxis)

D = dict(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[10, 3, 100, 6, 45, 4, 80, 45, 3, 59])

EVEN_LINEAR_SCALE = Figure(
    data=Data([
        Scatter(
            x=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
            y=[10.0, 3.0, 100.0, 6.0, 45.0, 4.0, 80.0, 45.0, 3.0, 59.0],
            name='_line0',
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
            range=[0.0, 18.0],
            type='linear',
            showline=True,
            tick0=0,
            dtick=3,
            ticks='inside',
            showgrid=False,
            tickmode=False,
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
            range=[0.0, 195.0],
            type='linear',
            showline=True,
            tick0=0,
            dtick=13,
            ticks='inside',
            showgrid=False,
            tickmode=False,
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
