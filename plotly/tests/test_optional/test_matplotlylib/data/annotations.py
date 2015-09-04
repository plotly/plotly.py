from __future__ import absolute_import

from plotly.graph_objs import (Annotation, Annotations, Data, Figure, Font,
                               Layout, Line, Margin, Scatter, XAxis, YAxis)

ANNOTATIONS = Figure(
    data=Data([
        Scatter(
            x=[0.0, 1.0, 2.0],
            y=[1.0, 2.0, 3.0],
            name='_line0',
            mode='lines',
            line=Line(
                dash='solid',
                color='rgba (0, 0, 255, 1)',
                width=1.0
            ),
            xaxis='x1',
            yaxis='y1'
        ),
        Scatter(
            x=[0.0, 1.0, 2.0],
            y=[3.0, 2.0, 1.0],
            name='_line1',
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
        annotations=Annotations([
            Annotation(
                x=0.000997987927565,
                y=0.996414507772,
                text='top-left',
                xref='paper',
                yref='paper',
                showarrow=False,
                align='left',
                font=Font(
                    size=12.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='left',
                yanchor='top'
            ),
            Annotation(
                x=0.000997987927565,
                y=0.00358549222798,
                text='bottom-left',
                xref='paper',
                yref='paper',
                align='left',
                showarrow=False,
                font=Font(
                    size=12.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='left',
                yanchor='bottom'
            ),
            Annotation(
                x=0.996989939638,
                y=0.996414507772,
                text='top-right',
                xref='paper',
                yref='paper',
                align='right',
                showarrow=False,
                font=Font(
                    size=12.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='right',
                yanchor='top'
            ),
            Annotation(
                x=0.996989939638,
                y=0.00358549222798,
                text='bottom-right',
                xref='paper',
                yref='paper',
                align='right',
                showarrow=False,
                font=Font(
                    size=12.0,
                    color='#000000'
                ),
                opacity=1,
                xanchor='right',
                yanchor='bottom'
            )
        ]),
        xaxis1=XAxis(
            domain=[0.0, 1.0],
            range=(0.0, 2.0),
            showline=True,
            ticks='inside',
            showgrid=False,
            zeroline=False,
            anchor='y1',
            mirror=True
        ),
        yaxis1=YAxis(
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
