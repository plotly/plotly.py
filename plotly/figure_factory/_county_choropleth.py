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
#pre_url = 'data/'
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

ST = df_merged['ST'].unique()
code_to_country_name_dict = {}
for i in range(len(df_merged)):
    row = df_merged.iloc[i]
    if len(code_to_country_name_dict) == len(ST):
        break
    if row['ST'] not in code_to_country_name_dict:
        code_to_country_name_dict[row['ST']] = row['State']

YEARS = sorted(df_merged['Year'].unique())
DEFAULT_LAYOUT = dict(
    hovermode='closest',
    xaxis=dict(
        autorange=False,
        range=[-125, -65],
        showgrid=False,
        zeroline=False,
        fixedrange=True,
        showticklabels=False
    ),
    yaxis=dict(
        autorange=False,
        range=[25, 49],
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


def create_choropleth(year, color_col, scope='usa', show_hover=True,
                      colorscale=None, order=None,
                      show_statedata=True, zoom=False, endpts=None,
                      SIMPLIFY_FACTOR=None):
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
    :param (float) SIMPLIFY_FACTOR: determines how many edges and vertices
        each county polygon has. The lower the number, the less simplified
        Default = 0.05

    Example 1:
    ```

    ```
    Example 2: New England
    import plotly.plotly as py
    import plotly.figure_factory as ff

    import numpy as np

    endpts = list(np.mgrid[1000:1000000:3j])
    scope = ['Maine', 'Vermont', 'MA', 'New Hampshire',
             'Rhode Island', 'Connecticut']

    fig = ff.create_choropleth(
        2011, scope=scope, color_col='Population', endpts=endpts,
    )
    ```
    Example 3: The entire USA
    ```
    import plotly.plotly as py
    import plotly.figure_factory as ff

    colorscale = ['#171c42', '#24327a', '#214ea5', '#006fbe', '#3f8eba',
                  '#76a9be', '#aac3cd', '#d2d7dd', '#e6d2d2', '#ddb2a4',
                  '#d08b73', '#c26245', '#b1392a', '#911a28', '#670d22',
                  '#3c0911']

    fig = ff.create_choropleth(
        2000, scope='usa', color_col='Death Rate',
        colorscale=colorscale, show_statedata=False
    )
    ```
    """
    xaxis_range_low = 0
    xaxis_range_high = -1000
    yaxis_range_low = 1000
    yaxis_range_high = 0

    if isinstance(year, Number):
        if year not in YEARS:
            raise exceptions.PlotlyError(
                "'year' must be a year (int) or a list of years all "
                "in the {}-{} range".format(min(YEARS), max(YEARS))
            )
        # TODO: change df_single_year to df_years
        df_single_year = df_merged[df_merged.Year == year]
    else:
        for y in year:
            if y not in YEARS:
                raise exceptions.PlotlyError(
                    "'year' must be a year (int) or a list of years all "
                    "in the {}-{} range".format(min(YEARS), max(YEARS))
                )
        df_single_year = df_merged[df_merged['Year'].isin(year)]

    if color_col not in df_single_year:
        raise exceptions.PlotlyError(
            'your color_col must be one of the following '
            'column keys: {}'.format(
                utils.list_of_options(df_single_year.keys(), conj='or')
            )
        )

    # utils.validate_index(df_single_year[color_col])

    # bin color data categorically
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
    # TODO: change list to utils.sequence
    if isinstance(scope, str):
        scope = [scope]

    if scope != ['usa']:
        scope_names = []
        for state in scope:
            if state in code_to_country_name_dict.keys():
                state = code_to_country_name_dict[state]
            scope_names.append(state)
        df_single_year = df_single_year[df_single_year['State'].isin(scope_names)]
    else:
        scope_names = df_single_year['State'].unique()

    if not SIMPLIFY_FACTOR:
        SIMPLIFY_FACTOR = 0.05

    plot_data = []
    x_centroids = []
    y_centroids = []
    centroid_text = []
    if not endpts:
        for index, row in df_single_year.iterrows():
            level = row[color_col]
            if df_single_year['geometry'][index].type == 'Polygon':
                x = row.geometry.simplify(SIMPLIFY_FACTOR).exterior.xy[0].tolist()
                y = row.geometry.simplify(SIMPLIFY_FACTOR).exterior.xy[1].tolist()
                x_c, y_c = row.geometry.centroid.xy
                t_c = (row.NAME + '<br>' + color_col + ': ' + level + '<br>State: ' +
                       row.State + '<br>' + 'FIPS: ' + str(row.FIPS))
                x_centroids.append(x_c[0])
                y_centroids.append(y_c[0])
                centroid_text.append(t_c)
            elif df_single_year['geometry'][index].type == 'MultiPolygon':
                x = ([poly.simplify(SIMPLIFY_FACTOR).exterior.xy[0] for
                      poly in df_single_year['geometry'][index]])
                y = ([poly.simplify(SIMPLIFY_FACTOR).exterior.xy[1] for
                      poly in df_single_year['geometry'][index]])
                x_c = [poly.centroid.xy[0] for poly in df_single_year['geometry'][index]]
                y_c = [poly.centroid.xy[1] for poly in df_single_year['geometry'][index]]
                text = (row.NAME + '<br>' + color_col + ': ' + level +
                        '<br>' + 'FIPS: ' + str(row.FIPS))
                t_c = [text for poly in df_single_year['geometry'][index]]
                x_centroids = x_c + x_centroids
                y_centroids = y_c + y_centroids
                centroid_text = t_c + centroid_text
            x_traces[level] = x_traces[level] + x + [np.nan]
            y_traces[level] = y_traces[level] + y + [np.nan]

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
        for index, row in df_single_year.iterrows():
            for j, inter in enumerate(intervals):
                if row[color_col] > inter[0] and row[color_col] < inter[1]:
                    break
            level = LEVELS[j]
            if df_single_year['geometry'][index].type == 'Polygon':
                x = row.geometry.simplify(SIMPLIFY_FACTOR).exterior.xy[0].tolist()
                y = row.geometry.simplify(SIMPLIFY_FACTOR).exterior.xy[1].tolist()
                x_c, y_c = row.geometry.centroid.xy
                t_c = (
                    row.NAME + '<br>' + color_col + ': ' + str(row[color_col]) +
                    '<br>State: ' + row.State + '<br>' + 'FIPS: ' + str(row.FIPS)
                )
                x_centroids.append(x_c[0])
                y_centroids.append(y_c[0])
                centroid_text.append(t_c)
            elif df_single_year['geometry'][index].type == 'MultiPolygon':
                x = ([poly.simplify(SIMPLIFY_FACTOR).exterior.xy[0] for
                      poly in df_single_year['geometry'][index]])
                y = ([poly.simplify(SIMPLIFY_FACTOR).exterior.xy[1] for
                      poly in df_single_year['geometry'][index]])
                x_c = [poly.centroid.xy[0] for poly in df_single_year['geometry'][index]]
                y_c = [poly.centroid.xy[1] for poly in df_single_year['geometry'][index]]
                text = (
                    row.NAME + '<br>' + color_col + ': ' + str(row[color_col]) +
                    '<br>' + 'FIPS: ' + str(row.FIPS)
                )
                t_c = [text for poly in df_single_year['geometry'][index]]
                x_centroids = x_c + x_centroids
                y_centroids = y_c + y_centroids
                centroid_text = t_c + centroid_text
            x_traces[level] = x_traces[level] + x + [np.nan]
            y_traces[level] = y_traces[level] + y + [np.nan]

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
    #sim_fct_2 = 0.1
    sim_fct_2 = 0.05
    for index, row in df_state.iterrows():
        if df_state['geometry'][index].type == 'Polygon':
            x = row.geometry.simplify(sim_fct_2).exterior.xy[0].tolist()
            y = row.geometry.simplify(sim_fct_2).exterior.xy[1].tolist()
            x_states = x_states + x
            y_states = y_states + y
        elif df_state['geometry'][index].type == 'MultiPolygon':
            x = ([poly.simplify(sim_fct_2).exterior.xy[0].tolist() for
                  poly in df_state['geometry'][index]])
            y = ([poly.simplify(sim_fct_2).exterior.xy[1].tolist() for
                  poly in df_state['geometry'][index]])
            for segment in range(len(x)):
                x_states = x_states + x[segment]
                y_states = y_states + y[segment]
                x_states.append(np.nan)
                y_states.append(np.nan)
        x_states.append(np.nan)
        y_states.append(np.nan)

    # TODO: sort LEVELS if '<30' type
    for lev in LEVELS:
        county_outline = dict(
            type='scatter',
            mode='lines',
            x=x_traces[lev],
            y=y_traces[lev],
            line=dict(color='black', width=0.5),
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
            marker=dict(size=2, color='white', opacity=0),
            mode='markers'
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

    # camera zoom
    fig['layout']['xaxis']['range'] = [xaxis_range_low, xaxis_range_high]
    fig['layout']['yaxis']['range'] = [yaxis_range_low, yaxis_range_high]

    # fix aspect ratio
    init_width = float(-65 + 125)
    init_height = float(49 - 25)

    width = float(fig['layout']['xaxis']['range'][1] -
                  fig['layout']['xaxis']['range'][0])
    height = float(fig['layout']['yaxis']['range'][1] -
                   fig['layout']['yaxis']['range'][0])

    center = (sum(fig['layout']['xaxis']['range']) / 2,
              sum(fig['layout']['yaxis']['range']) / 2)

    if height / width > init_height / init_width:
        new_width = (init_width / init_height) * height
        fig['layout']['xaxis']['range'][0] = center[0] - new_width * 0.5
        fig['layout']['xaxis']['range'][1] = center[0] + new_width * 0.5
    else:
        new_height = (init_height / init_width) * width
        fig['layout']['yaxis']['range'][0] = center[1] - new_height * 0.5
        fig['layout']['yaxis']['range'][1] = center[1] + new_height * 0.5

    return fig
