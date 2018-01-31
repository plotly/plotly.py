from plotly import colors, exceptions, optional_imports
from plotly.figure_factory import utils

import array
import shapefile
import feather
import pandas as pd
import numpy as np
import geopandas as gp

from numbers import Number

shape_path = 'cb_2016_us_county_500k/cb_2016_us_county_500k.shp'
states_path = 'cb_2016_us_state_500k/cb_2016_us_state_500k.shp'
csv_path = 'NCHS_-_Drug_Poisoning_Mortality_by_County__United_States.csv'
full_data_path = 'df.feather'

pre_url = 'plotly/package_data/data/'
shape_path = pre_url + shape_path
states_path = pre_url + states_path
csv_path = pre_url + csv_path
full_data_path = pre_url + full_data_path

# shape df
sf = shapefile.Reader(states_path)
df_shape = gp.read_file(shape_path)
df_shape['FIPS'] = df_shape['STATEFP'] + df_shape['COUNTYFP']
df_shape['FIPS'] = pd.to_numeric(df_shape['FIPS'])

# state df
df_state = gp.read_file(states_path)

# csv df
df_csv = pd.read_csv(csv_path)
DEATH_RATE_COL = (
    'Estimated Age-adjusted Death Rate, 16 Categories (in ranges)'
)
death_rate = df_csv[DEATH_RATE_COL].values
death_rate_min = [float(ea.strip('>').split('-')[0]) for ea in death_rate]
df_csv['MIN_DEATH_RATE'] = death_rate_min

# merge dfs
df_full_data = feather.read_dataframe(full_data_path)
df_merged = pd.merge(df_shape, df_csv, on='FIPS')

# create county code to county dict
ST = df_merged['ST'].unique()
code_to_country_name_dict = {}
for i in range(len(df_merged)):
    row = df_merged.iloc[i]
    if len(code_to_country_name_dict) == len(ST):
        break
    if row['ST'] not in code_to_country_name_dict:
        code_to_country_name_dict[row['ST']] = row['State']

YEARS = sorted(df_merged['Year'].unique())
YEARS_ERROR_MESSAGE = (
    "'year' must be a number or a list of numbers with "
    "possible values {}".format(
        utils.list_of_options(YEARS, conj='or')
    )
)

USA_XRANGE = [-125.0, -65.0]
USA_YRANGE = [25.0, 49.0]
DEFAULT_LAYOUT = dict(
    hovermode='closest',
    xaxis=dict(
        autorange=False,
        range=USA_XRANGE,
        showgrid=False,
        zeroline=False,
        fixedrange=True,
        showticklabels=False
    ),
    yaxis=dict(
        autorange=False,
        range=USA_YRANGE,
        showgrid=False,
        zeroline=False,
        fixedrange=True,
        showticklabels=False
    ),
    margin=dict(t=20, b=20, r=20, l=20),
    width=900,
    height=450,
    dragmode='select',
    legend=dict(traceorder='reversed')
)


def _intervals_as_labels(array_of_intervals):
    """
    Transform an interval [-inf, 30] to label <30
    """
    string_intervals = []
    for interval in array_of_intervals:
        # round to 2nd decimal place
        rnd_interval = [round(interval[0], 2),
                        round(interval[1], 2)]
        if rnd_interval[0] == float('-inf'):
            as_str = '<{}'.format(rnd_interval[1])
        elif rnd_interval[1] == float('inf'):
            as_str = '>{}'.format(rnd_interval[0])
        else:
            as_str = '{}-{}'.format(rnd_interval[0], rnd_interval[1])
        string_intervals.append(as_str)
    return string_intervals


def _update_xaxis_range(x_traces, level, xaxis_range_low, xaxis_range_high):
    if x_traces[level] != []:
        x_len = len(x_traces[level])
        mask = np.ones(x_len, dtype=bool)

        indices = []
        for i in range(x_len):
            if not isinstance(x_traces[level][i], array.array):
                indices.append(i)
        mask[indices] = True

        calc_x_min = min([x_traces[level][i] for i in indices])
        calc_x_max = max([x_traces[level][i] for i in indices])

        if calc_x_min < xaxis_range_low:
            xaxis_range_low = calc_x_min
        if calc_x_max > xaxis_range_high:
            xaxis_range_high = calc_x_max

    return xaxis_range_low, xaxis_range_high


def _update_yaxis_range(y_traces, level, yaxis_range_low, yaxis_range_high):
    if y_traces[level] != []:
        y_len = len(y_traces[level])
        mask = np.ones(y_len, dtype=bool)

        indices = []
        for i in range(y_len):
            if not isinstance(y_traces[level][i], array.array):
                indices.append(i)
        mask[indices] = True

        calc_y_min = min([y_traces[level][i] for i in indices])
        calc_y_max = max([y_traces[level][i] for i in indices])

        if calc_y_min < yaxis_range_low:
            yaxis_range_low = calc_y_min
        if calc_y_max > yaxis_range_high:
            yaxis_range_high = calc_y_max

    return yaxis_range_low, yaxis_range_high


def _add_break_to_color_column(color_col):
    if isinstance(color_col, str) and len(color_col) >= 23:
        words = color_col.split(' ')
        color_col_with_br = (
            ' '.join(words[:len(words)/2]) +
            ' <br> ' + ' '.join(words[len(words)/2:])
        )
    else:
        color_col_with_br = str(color_col)
    return color_col_with_br


def _calculations(df_years, index, row, color_col, simplify_county, level,
                  x_centroids, y_centroids, centroid_text, x_traces, y_traces):
    if df_years['geometry'][index].type == 'Polygon':
        x = row.geometry.simplify(simplify_county).exterior.xy[0].tolist()
        y = row.geometry.simplify(simplify_county).exterior.xy[1].tolist()
        x_c, y_c = row.geometry.centroid.xy

        # split color_col if too long
        color_col_with_br = _add_break_to_color_column(color_col)

        t_c = (row.NAME + '<br>' + color_col_with_br + ': ' +
               str(level) + '<br>State: ' + str(row.State) + '<br>' +
               'FIPS: ' + str(row.FIPS))
        x_centroids.append(x_c[0])
        y_centroids.append(y_c[0])
        centroid_text.append(t_c)

        x_traces[level] = x_traces[level] + x + [np.nan]
        y_traces[level] = y_traces[level] + y + [np.nan]
    elif df_years['geometry'][index].type == 'MultiPolygon':
        x = ([poly.simplify(simplify_county).exterior.xy[0].tolist() for
              poly in df_years['geometry'][index]])
        y = ([poly.simplify(simplify_county).exterior.xy[1].tolist() for
              poly in df_years['geometry'][index]])
        x_c = [poly.centroid.xy[0].tolist() for poly in df_years['geometry'][index]]
        y_c = [poly.centroid.xy[1].tolist() for poly in df_years['geometry'][index]]

        # split color_col if too long
        color_col_with_br = _add_break_to_color_column(color_col)
        text = (row.NAME + '<br>' + color_col_with_br + ': ' +
                str(level) + '<br>' + 'FIPS: ' + str(row.FIPS))
        t_c = [text for poly in df_years['geometry'][index]]
        x_centroids = x_c + x_centroids
        y_centroids = y_c + y_centroids
        centroid_text = t_c + centroid_text
        for x_y_idx in range(len(x)):
            x_traces[level] = x_traces[level] + x[x_y_idx] + [np.nan]
            y_traces[level] = y_traces[level] + y[x_y_idx] + [np.nan]

    return x_traces, y_traces, x_centroids, y_centroids, centroid_text


def create_choropleth(year, color_col, scope='usa', show_hover=True,
                      colorscale=None, order=None,
                      show_statedata=True, zoom=False, endpts=None,
                      simplify_county=0.02, simplify_state=0.02,
                      county_outline_color='#000', asp=None,
                      data_path=None):
    """
    Returns figure for county choropleth. Uses data from package_data.

    :param (int|list) year: filters data by year or years. Use a single
        year (eg. year=2004) or a list of years (eg. [2004, 2005, 2007])
    :param (str) color_col: the variable that the color indexing is based on.
        Can be categorical or numerical values.
    :param (str|list) scope: accepts a list of states and/or state
        abbreviations to be plotted. Selecting 'usa' shows the entire
        USA map excluding Hawaii and Alaska.
        Default = 'usa'
    :param (bool) show_hover: show county hover info
    :param (list) colorscale: a list of colors with length equal to the
        number of unique values in the color index `color_col`
    :param (list) order: a list of unique values contained in the color
        column 'color_col' provided, ordered however you want the order of
        the colorscale to be
    :param (bool) show_statedata: reveals hoverinfo for the state on hover
    :param (bool) zoom: enables zoom
    :param (list) endpts: creates bins from a color column of numbers to
    :param (float) simplify_county: determines the simplification factor
        for the counties. The larger the number, the fewer vertices and edges
        each polygon has. See
        http://toblerity.org/shapely/manual.html#object.simplify for more
        information.
        Default = 0.02
    :param (float) simplify_state: simplifies the state outline polygon.
        See http://toblerity.org/shapely/manual.html#object.simplify for more
        information.
        Default = 0.02
    :param (float) county_outline_color
    :param (float) asp: the width-to-height aspect ratio for the camera.
        Default = 2.5

    Example 1: Texas
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    color_col = 'Population'
    scope = 'Texas'
    fig = ff.create_choropleth(
        2008, color_col=color_col,
        scope=scope, asp=2.0,
        endpts=[100, 1000, 10000, 100000, 1000000]
    )
    py.iplot(fig, filename='my_choropleth_texas')
    ```

    Example 2: New England
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import numpy as np

    endpts = list(np.mgrid[100:100000:8j])
    scope = ['ME', 'Vermont', 'MA', 'NH',
             'Rhode Island', 'CT']
    color_col = 'Population'
    fig = ff.create_choropleth(
        2003, color_col=color_col,
        scope=scope,
    )
    py.iplot(fig, filename='my_choropleth_new_england')
    ```

    Example 3: The entire USA
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import numpy as np

    color_col = 'Estimated Age-adjusted Death Rate, 16 Categories (in ranges)'
    colorscale = ['#171c42', '#24327a', '#214ea5', '#006fbe', '#3f8eba',
                  '#76a9be', '#aac3cd', '#d2d7dd', '#e6d2d2', '#ddb2a4',
                  '#d08b73', '#c26245', '#b1392a', '#911a28', '#670d22',
                  '#3c0911']
    order = ['0-2', '2.1-4', '4.1-6', '6.1-8',
             '8.1-10', '10.1-12', '12.1-14', '14.1-16',
             '16.1-18', '18.1-20', '20.1-22', '22.1-24',
             '24.1-26', '26.1-28', '28.1-30', '>30']
    fig = ff.create_choropleth(
        2015, color_col=color_col,
        scope='usa', colorscale=colorscale,
        order=order, show_hover=False
    )
    py.iplot(fig, filename='my_choropleth_usa')
    ```
    """
    xaxis_range_low = 0
    xaxis_range_high = -1000
    yaxis_range_low = 1000
    yaxis_range_high = 0

    if isinstance(year, Number):
        if year not in YEARS:
            raise exceptions.PlotlyError(YEARS_ERROR_MESSAGE)
        # TODO: change df_years to df_years
        df_years = df_merged[df_merged.Year == year]
    else:
        for y in year:
            if y not in YEARS:
                raise exceptions.PlotlyError(YEARS_ERROR_MESSAGE)
        df_years = df_merged[df_merged['Year'].isin(year)]

    if color_col not in df_years:
        raise exceptions.PlotlyError(
            'your color_col must be one of the following '
            'column keys: {}'.format(
                utils.list_of_options(df_years.keys(), conj='or')
            )
        )

    if endpts:
        intervals = utils.endpts_to_intervals(endpts)
        LEVELS = _intervals_as_labels(intervals)
    else:
        if not order:
            LEVELS = sorted(df_merged[color_col].unique())
        else:
            # check if order is permutation
            # of unique color col values
            same_sets = set(df_merged[color_col].unique()) == set(order)
            no_duplicates = not any(order.count(x) > 1 for x in order)
            if same_sets and no_duplicates:
                LEVELS = order
            else:
                raise exceptions.PlotlyError(
                    'if you are using a custom order of unique values from '
                    'your color column, you must: have all the unique values '
                    'in your order and have no duplicate items'
                )

    if not colorscale:
        colorscale = colors.n_colors(
            'rgb(0, 109, 44)', 'rgb(199, 233, 192)', len(LEVELS), 'rgb'
        )

    if len(colorscale) < len(LEVELS):
        raise exceptions.PlotlyError(
            "your number of colors in 'colorscale' must be "
            "at least the number of LEVELS: {}".format(
                min(LEVELS, LEVELS[:20])
            )
        )

    color_lookup = dict(zip(LEVELS, colorscale))
    x_traces = dict(zip(LEVELS, [[] for i in range(len(LEVELS))]))
    y_traces = dict(zip(LEVELS, [[] for i in range(len(LEVELS))]))

    # scope
    if isinstance(scope, str):
        scope = [scope]

    if scope != ['usa']:
        scope_names = []
        for state in scope:
            if state in code_to_country_name_dict.keys():
                state = code_to_country_name_dict[state]
            scope_names.append(state)
        df_years = df_years[df_years['State'].isin(scope_names)]
    else:
        scope_names = df_years['State'].unique()

    plot_data = []
    x_centroids = []
    y_centroids = []
    centroid_text = []
    if not endpts:
        for index, row in df_years.iterrows():
            level = row[color_col]

            (x_traces, y_traces, x_centroids,
             y_centroids, centroid_text) = _calculations(
                df_years, index, row, color_col, simplify_county, level,
                x_centroids, y_centroids, centroid_text, x_traces, y_traces
            )

            if scope == ['usa']:
                xaxis_range_low = -125
                xaxis_range_high = -65
                yaxis_range_low = 25
                yaxis_range_high = 49
            else:
                xaxis_range_low, xaxis_range_high = _update_xaxis_range(
                    x_traces, level, xaxis_range_low, xaxis_range_high
                )

                yaxis_range_low, yaxis_range_high = _update_yaxis_range(
                    y_traces, level, yaxis_range_low, yaxis_range_high
                )

    else:
        for index, row in df_years.iterrows():
            for j, inter in enumerate(intervals):
                if row[color_col] > inter[0] and row[color_col] < inter[1]:
                    break
            level = LEVELS[j]

            (x_traces, y_traces, x_centroids,
             y_centroids, centroid_text) = _calculations(
                df_years, index, row, color_col, simplify_county, level,
                x_centroids, y_centroids, centroid_text, x_traces, y_traces
            )

            if scope == ['usa']:
                xaxis_range_low = -125
                xaxis_range_high = -65
                yaxis_range_low = 25
                yaxis_range_high = 49
            else:
                xaxis_range_low, xaxis_range_high = _update_xaxis_range(
                    x_traces, level, xaxis_range_low, xaxis_range_high
                )

                yaxis_range_low, yaxis_range_high = _update_yaxis_range(
                    y_traces, level, yaxis_range_low, yaxis_range_high
                )

    x_states = []
    y_states = []
    for index, row in df_state.iterrows():
        if df_state['geometry'][index].type == 'Polygon':
            x = row.geometry.simplify(simplify_state).exterior.xy[0].tolist()
            y = row.geometry.simplify(simplify_state).exterior.xy[1].tolist()
            x_states = x_states + x
            y_states = y_states + y
        elif df_state['geometry'][index].type == 'MultiPolygon':
            x = ([poly.simplify(simplify_state).exterior.xy[0].tolist() for
                  poly in df_state['geometry'][index]])
            y = ([poly.simplify(simplify_state).exterior.xy[1].tolist() for
                  poly in df_state['geometry'][index]])
            for segment in range(len(x)):
                x_states = x_states + x[segment]
                y_states = y_states + y[segment]
                x_states.append(np.nan)
                y_states.append(np.nan)
        x_states.append(np.nan)
        y_states.append(np.nan)

    for lev in LEVELS:
        county_outline = dict(
            type='scatter',
            mode='lines',
            x=x_traces[lev],
            y=y_traces[lev],
            line=dict(color=county_outline_color,
                      width=0.5),
            fill='toself',
            fillcolor=color_lookup[lev],
            name=lev,
            hoverinfo='none',
        )
        plot_data.append(county_outline)

    if show_hover:
        hover_points = dict(
            type='scatter',
            showlegend=False,
            legendgroup='centroids',
            x=x_centroids,
            y=y_centroids,
            text=centroid_text,
            name='US Counties',
            #selected=dict(
            #    marker=dict(size=2, color='white', opacity=1)
            #),
            #unselected=dict(
            #    marker=dict(opacity=0)
            #),
            mode='markers',
            marker=dict(size=2, color='white', opacity=0),
        )
        plot_data.append(hover_points)

    if show_statedata:
        state_data = dict(
            type='scatter',
            legendgroup='States',
            line=dict(color='white', width=1),
            x=x_states,
            y=y_states,
            hoverinfo='none',
            showlegend=False,
            mode='lines'
        )
        plot_data.append(state_data)

    fig = dict(data=plot_data, layout=DEFAULT_LAYOUT)

    # layout update
    fig['layout'].update(
        {'title': 'my choropleth',
         'margin': dict(t=40)}
    )

    # camera zoom
    fig['layout']['xaxis']['range'] = [xaxis_range_low, xaxis_range_high]
    fig['layout']['yaxis']['range'] = [yaxis_range_low, yaxis_range_high]

    # aspect ratio
    if asp is None:
        asp = (USA_XRANGE[1] - USA_XRANGE[0]) / (USA_YRANGE[1] - USA_YRANGE[0])

    # based on your figure
    width = float(fig['layout']['xaxis']['range'][1] -
                  fig['layout']['xaxis']['range'][0])
    height = float(fig['layout']['yaxis']['range'][1] -
                   fig['layout']['yaxis']['range'][0])

    center = (sum(fig['layout']['xaxis']['range']) / 2.,
              sum(fig['layout']['yaxis']['range']) / 2.)

    if height / width > (1 / asp):
        new_width = asp * height
        fig['layout']['xaxis']['range'][0] = center[0] - new_width * 0.5
        fig['layout']['xaxis']['range'][1] = center[0] + new_width * 0.5
    else:
        new_height = (1 / asp) * width
        fig['layout']['yaxis']['range'][0] = center[1] - new_height * 0.5
        fig['layout']['yaxis']['range'][1] = center[1] + new_height * 0.5

    return fig
