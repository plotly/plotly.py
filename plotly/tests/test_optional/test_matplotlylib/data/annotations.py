from __future__ import absolute_import

import plotly.graph_objs as go

ANNOTATIONS = go.Figure(
    data=[
        go.Scatter(
            x=[0.0, 1.0, 2.0],
            y=[1.0, 2.0, 3.0],
            name='_line0',
            mode='lines',
            line=go.scatter.Line(
                dash='solid',
                color='rgba (0, 0, 255, 1)',
                width=1.5
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        go.Scatter(
            x=[0.0, 1.0, 2.0],
            y=[3.0, 2.0, 1.0],
            name='_line1',
            mode='lines',
            line=go.scatter.Line(
                dash='solid',
                color='rgba (0, 0, 255, 1)',
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
            b=47,
            t=47,
            pad=0
        ),
        hovermode='closest',
        showlegend=False,
        annotations=[
            go.layout.Annotation(
                x=0.000997987927565,
                y=0.9973865229110511,
                text='top-left',
                xref='paper',
                yref='paper',
                showarrow=False,
                align='left',
                font=dict(
                    size=10.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='left',
                yanchor='top'
            ),
            go.layout.Annotation(
                x=0.000997987927565,
                y=0.0031525606469002573,
                text='bottom-left',
                xref='paper',
                yref='paper',
                align='left',
                showarrow=False,
                font=dict(
                    size=10.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='left',
                yanchor='bottom'
            ),
            go.layout.Annotation(
                x=0.996989939638,
                y=0.9973865229110511,
                text='top-right',
                xref='paper',
                yref='paper',
                align='right',
                showarrow=False,
                font=dict(
                    size=10.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='right',
                yanchor='top'
            ),
            go.layout.Annotation(
                x=0.996989939638,
                y=0.0031525606469002573,
                text='bottom-right',
                xref='paper',
                yref='paper',
                align='right',
                showarrow=False,
                font=dict(
                    size=10.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='right',
                yanchor='bottom'
            )
        ],
        xaxis1=go.layout.XAxis(
            domain=[0.0, 1.0],
            range=(0.0, 2.0),
            showline=True,
            ticks='inside',
            showgrid=False,
            zeroline=False,
            anchor='y1',
            mirror=True
        ),
        yaxis1=go.layout.YAxis(
            domain=[0.0, 1.0],
            range=(1.0, 3.0),
            showline=True,
            ticks='inside',
            showgrid=False,
            zeroline=False,
            anchor='x1',
            mirror=True
        )
    )
)
