from __future__ import absolute_import

from numbers import Number
import itertools
from plotly import exceptions, optional_imports
import plotly.colors as clrs
from plotly.graph_objs import graph_objs
from plotly.subplots import make_subplots

pd = optional_imports.get_module("pandas")
np = optional_imports.get_module("numpy")


def create_upset(df, include_empty_set = False, max_width = 50):
    # an array of dimensions d x d*2^d possible subsets where d is the number of columns
    subsets = []
    # the sizes of each subset (2^d array)
    subset_sizes = [ ]
    d = len(df.columns)
    for i in range(1, d + 1):
        subsets = subsets + [list(x) for x in list(itertools.combinations(df.columns, i))]
    if include_empty_set: subsets = subsets + [[]]

    for s in subsets:
        curr_bool = [1]*len(df)
        for col in df.columns:
            if col in s: curr_bool = [x and y for x, y in zip(curr_bool, list(df.loc[:, col].copy()))]
            else: curr_bool = [x and not y for x, y in zip(curr_bool, list(df.loc[:, col].copy()))]
        subset_sizes.append(sum(curr_bool))
    
    
    plot_df = pd.DataFrame({'Intersection': subsets, 'Size':subset_sizes})
    plot_df = plot_df.sort_values(by = 'Size', ascending = False)
    max_y = max(plot_df['Size'])+0.1*max(plot_df['Size'])
    
    if not max_width is None and len(plot_df) > max_width: plot_df = plot_df.iloc[0:max_width,:]
    
    subsets = list(plot_df['Intersection'])
    scatter_x = []
    scatter_y = []
    for i, s in enumerate(subsets):
        for j in range(d):
            scatter_x.append(i)
            scatter_y.append(-j*max_y/d-0.1*max_y)
            
    fig = graph_objs.Figure()
#     fig.add_trace(graph_objs.Scatter(x=[-1.2,len(subsets)],y= [max_y+0.1*max_y,max_y+0.1*max_y],fill='tozeroy'))
    template =  ['' for x in scatter_x]
    fig.add_trace(graph_objs.Scatter(x = scatter_x, y = scatter_y, mode = 'markers', showlegend=False, marker=dict(size=16,color='#C9C9C9'), hovertemplate = template))
    fig.update_layout(xaxis=dict(showgrid=False, zeroline=False),
                  yaxis=dict(showgrid=True, zeroline=False),
                   plot_bgcolor = "#FFFFFF", margin=dict(t=40, l=150)) 
    for i, s in enumerate(subsets):
        scatter_x_has = []
        scatter_y_has = []
        for j in range(d):
            if df.columns[j] in s:
                scatter_x_has.append(i)
                scatter_y_has.append(-j*max_y/d-0.1*max_y)
                fig.add_trace(graph_objs.Scatter(x = scatter_x_has, y = scatter_y_has, mode = 'markers+lines', showlegend=False, marker=dict(size=16,color='#000000',showscale=False), hovertemplate = template))
    fig.update_xaxes(showticklabels=False) # Hide x axis ticks 
    fig.update_yaxes(showticklabels=False) # Hide y axis ticks
    fig.update_traces(hoverinfo=None)
    
    plot_df['Intersection'] = ['+'.join(x) for x in plot_df['Intersection']]
    template =  [f'<extra><br><b>{lab}</b><br><b>N-Count</b>: {n}</extra>' for  lab, n in zip(plot_df['Intersection'], plot_df['Size'])]
    bar = graph_objs.Bar(x = list(range(len(subsets))), y = plot_df['Size'], marker = dict(color='#000000'),  text = plot_df['Size'], hovertemplate = template, textposition='outside', hoverinfo='none')
    fig.add_trace(bar)
    
    template =  ['' for x in range(d)]
    max_string_len = max([len(x) for x in df.columns])
    print(max_string_len**2)
    
    ### the adjusment of the x range to accomodate labels probably needs work
    fig_lab = graph_objs.Scatter(x = [-0.02*max_string_len]*d, y = scatter_y, text = df.columns, mode = 'text', textposition='middle left',showlegend=False, hovertemplate = template)
    fig_lab = graph_objs.Scatter(x = [-0.02*max_string_len]*d, y = scatter_y, text = df.columns, mode = 'text', textposition='middle left',showlegend=False, hovertemplate = template)
    fig.add_trace(fig_lab)
    fig.update_layout(title = '<b>Intersections<b>', yaxis_range=[-max_y-0.1*max_y-1, max_y+0.1*max_y], xaxis_range = [-0.015*max_string_len**1.3, len(subsets)], showlegend = False, title_x=0.5)
    
    return fig