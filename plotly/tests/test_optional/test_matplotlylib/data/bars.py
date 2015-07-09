from __future__ import absolute_import

from plotly.graph_objs import (Bar, Data, Figure, Font, Margin, Marker, Layout,
                               Line, XAxis, YAxis)

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

VERTICAL_BAR = Figure(
    data=Data([
        Bar(
            x=[0.40000000000000002, 1.3999999999999999, 2.3999999999999999, 3.3999999999999999, 4.4000000000000004, 5.4000000000000004],
            y=[10.0, 20.0, 50.0, 80.0, 100.0, 200.0],
            orientation='v',
            marker=Marker(
                line=Line(
                    width=1.0
                ),
                color='#0000FF'
            ),
            opacity=1,
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
        bargap=0.2,
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

HORIZONTAL_BAR = Figure(
    data=Data([
        Bar(
            x=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
            y=[0.40000000000000002, 1.3999999999999999, 2.3999999999999999, 3.3999999999999999, 4.4000000000000004, 5.4000000000000004, 6.4000000000000004],
            orientation='h',
            marker=Marker(
                line=Line(
                    width=1.0
                ),
                color='#0000FF'
            ),
            opacity=1,
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
        bargap=0.2,
        xaxis1=XAxis(
            domain=[0.0, 1.0],
            range=[0.0, 140.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=8,
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
            range=[0.0, 7.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=8,
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

H_AND_V_BARS = Figure(
    data=Data([
        Bar(
            x=[5.0, 15.0, 25.0, 35.0, 45.0, 55.0],
            y=[1.0, 4.0, 8.0, 16.0, 32.0, 64.0],
            orientation='v',
            marker=Marker(
                line=Line(
                    width=1.0
                ),
                color='#008000'
            ),
            opacity=0.5,
            xaxis='x1',
            yaxis='y1'
        ),
        Bar(
            x=[30.0, 60.0, 20.0, 50.0, 60.0, 30.0],
            y=[20.0, 35.0, 50.0, 65.0, 80.0, 95.0],
            orientation='h',
            marker=Marker(
                line=Line(
                    width=1.0
                ),
                color='#FF0000'
            ),
            opacity=0.5,
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
        bargap=5,
        xaxis1=XAxis(
            domain=[0.0, 1.0],
            range=[0.0, 60.0],
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
            range=[0.0, 100.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
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


