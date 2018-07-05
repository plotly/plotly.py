from __future__ import absolute_import

import plotly.graph_objs as go

D = dict(
    x1=[0, 1],
    y1=[1, 2]
)

BLANK_SUBPLOTS = go.Figure(
    data=[
        go.Scatter(
            x=[0.0, 1.0],
            y=[1.0, 2.0],
            name='_line0',
            mode='lines',
            line=go.scatter.Line(
                dash='solid',
                color='#0000FF',
                width=1.0
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
            l=168,
            r=63,
            b=52,
            t=57,
            pad=0
        ),
        hovermode='closest',
        showlegend=False,
        xaxis1=go.layout.XAxis(
            domain=[0.0, 0.13513513513513517],
            range=[-0.050000000000000003, 1.05],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=4,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y1',
            side='bottom',
            mirror='ticks'
        ),
        xaxis2=go.layout.XAxis(
            domain=[0.0, 0.13513513513513517],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=2,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y2',
            side='bottom',
            mirror='ticks'
        ),
        xaxis3=go.layout.XAxis(
            domain=[0.0, 0.13513513513513517],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=2,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y3',
            side='bottom',
            mirror='ticks'
        ),
        xaxis4=go.layout.XAxis(
            domain=[0.2162162162162162, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y4',
            side='bottom',
            mirror='ticks'
        ),
        xaxis5=go.layout.XAxis(
            domain=[0.2162162162162162, 0.56756756756756754],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=3,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y5',
            side='bottom',
            mirror='ticks'
        ),
        xaxis6=go.layout.XAxis(
            domain=[0.2162162162162162, 0.78378378378378377],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y6',
            side='bottom',
            mirror='ticks'
        ),
        xaxis7=go.layout.XAxis(
            domain=[0.64864864864864857, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=3,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y7',
            side='bottom',
            mirror='ticks'
        ),
        xaxis8=go.layout.XAxis(
            domain=[0.8648648648648648, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=2,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='y8',
            side='bottom',
            mirror='ticks'
        ),
        yaxis1=go.layout.YAxis(
            domain=[0.82758620689655171, 1.0],
            range=[0.94999999999999996, 2.0499999999999998],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=4,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x1',
            side='left',
            mirror='ticks'
        ),
        yaxis2=go.layout.YAxis(
            domain=[0.55172413793103448, 0.72413793103448265],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=3,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x2',
            side='left',
            mirror='ticks'
        ),
        yaxis3=go.layout.YAxis(
            domain=[0.0, 0.44827586206896547],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x3',
            side='left',
            mirror='ticks'
        ),
        yaxis4=go.layout.YAxis(
            domain=[0.82758620689655171, 1.0],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=3,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x4',
            side='left',
            mirror='ticks'
        ),
        yaxis5=go.layout.YAxis(
            domain=[0.27586206896551713, 0.72413793103448265],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x5',
            side='left',
            mirror='ticks'
        ),
        yaxis6=go.layout.YAxis(
            domain=[0.0, 0.17241379310344826],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=3,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x6',
            side='left',
            mirror='ticks'
        ),
        yaxis7=go.layout.YAxis(
            domain=[0.27586206896551713, 0.72413793103448265],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=6,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x7',
            side='left',
            mirror='ticks'
        ),
        yaxis8=go.layout.YAxis(
            domain=[0.0, 0.17241379310344826],
            range=[0.0, 1.0],
            type='linear',
            showline=True,
            ticks='inside',
            nticks=3,
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                size=10.0
            ),
            anchor='x8',
            side='left',
            mirror='ticks'
        )
    )
)
