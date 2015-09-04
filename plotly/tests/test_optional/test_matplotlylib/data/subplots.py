from __future__ import absolute_import

from plotly.graph_objs import (Data, Figure, Font, Layout, Line, Margin,
                               Scatter, XAxis, YAxis)

D = dict(
    x1=[0, 1],
    y1=[1, 2]
)

BLANK_SUBPLOTS = Figure(
    data=Data([
        Scatter(
            x=[0.0, 1.0],
            y=[1.0, 2.0],
            name='_line0',
            mode='lines',
            line=Line(
                dash='solid',
                color='#0000FF',
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
            l=168,
            r=63,
            b=47,
            t=47,
            pad=0
        ),
        hovermode='closest',
        showlegend=False,
        xaxis1=XAxis(
            domain=[0.0, 0.13513513513513517],
            range=[0.0, 1.0],
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
        xaxis2=XAxis(
            domain=[0.0, 0.13513513513513517],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y2',
            side='bottom',
            mirror='ticks'
        ),
        xaxis3=XAxis(
            domain=[0.0, 0.13513513513513517],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y3',
            side='bottom',
            mirror='ticks'
        ),
        xaxis4=XAxis(
            domain=[0.2162162162162162, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y4',
            side='bottom',
            mirror='ticks'
        ),
        xaxis5=XAxis(
            domain=[0.2162162162162162, 0.56756756756756754],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y5',
            side='bottom',
            mirror='ticks'
        ),
        xaxis6=XAxis(
            domain=[0.2162162162162162, 0.78378378378378377],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y6',
            side='bottom',
            mirror='ticks'
        ),
        xaxis7=XAxis(
            domain=[0.64864864864864857, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y7',
            side='bottom',
            mirror='ticks'
        ),
        xaxis8=XAxis(
            domain=[0.8648648648648648, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='y8',
            side='bottom',
            mirror='ticks'
        ),
        yaxis1=YAxis(
            domain=[0.82758620689655182, 1.0],
            range=[1.0, 2.2000000000000002],
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
        ),
        yaxis2=YAxis(
            domain=[0.55172413793103459, 0.72413793103448276],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x2',
            side='left',
            mirror='ticks'
        ),
        yaxis3=YAxis(
            domain=[0.0, 0.44827586206896558],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x3',
            side='left',
            mirror='ticks'
        ),
        yaxis4=YAxis(
            domain=[0.82758620689655182, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x4',
            side='left',
            mirror='ticks'
        ),
        yaxis5=YAxis(
            domain=[0.27586206896551724, 0.72413793103448276],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x5',
            side='left',
            mirror='ticks'
        ),
        yaxis6=YAxis(
            domain=[0.0, 0.17241379310344834],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x6',
            side='left',
            mirror='ticks'
        ),
        yaxis7=YAxis(
            domain=[0.27586206896551724, 0.72413793103448276],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x7',
            side='left',
            mirror='ticks'
        ),
        yaxis8=YAxis(
            domain=[0.0, 0.17241379310344834],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=Font(
                size=12.0
            ),
            anchor='x8',
            side='left',
            mirror='ticks'
        )
    )
)
