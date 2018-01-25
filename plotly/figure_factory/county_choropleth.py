import plotly
import plotly.plotly as py
from plotly import colors
from plotly.figure_factory import utils

import array
import shapefile
import feather
import pandas as pd
import numpy as np
import geopandas as gp

shape_path = 'data/cb_2016_us_county_500k/cb_2016_us_county_500k.shp'
states_path = 'data/cb_2016_us_state_500k/cb_2016_us_state_500k.shp'
csv_path = 'data/NCHS_-_Drug_Poisoning_Mortality_by_County__United_States.csv'
full_data_path = 'data/df.feather'
sf = shapefile.Reader(states_path)

df_shape = gp.read_file(shape_path)
df_shape['FIPS'] = df_shape['STATEFP'] + df_shape['COUNTYFP']
df_shape['FIPS'] = pd.to_numeric(df_shape['FIPS'])

# read state and csv
df_state = gp.read_file(states_path)
df_csv = pd.read_csv(csv_path)

death_rate_col = 'Estimated Age-adjusted Death Rate, 16 Categories (in ranges)'
death_rate = df_csv[death_rate_col].values
death_rate_min = [float(ea.strip('>').split('-')[0]) for ea in death_rate]
df_csv['MIN_DEATH_RATE'] = death_rate_min
df_full_data = feather.read_dataframe(full_data_path)
df_merged = pd.merge(df_shape, df_csv, on='FIPS')
df_merged['Death Rate'] = df_merged[death_rate_col]

code_to_country_name_dict = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

YEARS = sorted(df_merged['Year'].unique())
DEFAULT_YEAR = min(YEARS)
DEFAULT_COLORSCALE = [
    '#171c42', '#24327a', '#214ea5', '#006fbe', '#3f8eba',
    '#76a9be', '#aac3cd', '#d2d7dd', '#e6d2d2', '#ddb2a4',
    '#d08b73', '#c26245', '#b1392a', '#911a28', '#670d22',
    '#3c0911'
]
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


def intervals_to_strings(array_of_intervals):
    string_intervals = []
    for interval in array_of_intervals:
        if interval[0] == float('-inf'):
            as_str = '<{}'.format(interval[1])
        elif interval[1] == float('inf'):
            as_str = '>{}'.format(interval[0])
        else:
            as_str = '{}-{}'.format(interval[0], interval[1])
        string_intervals.append(as_str)
    return string_intervals


def get_figure(year, colorscale=DEFAULT_COLORSCALE, scope='usa', color_col=None,
               show_hover=True, show_statedata=True, zoom=False, endpts=None):
    xaxis_range_low = 0
    xaxis_range_high = -1000
    yaxis_range_low = 1000
    yaxis_range_high = 0

    if year not in YEARS:
        print "'year' must be an int in the range 1999-2015 inclusive"
    df_single_year = df_merged[df_merged.Year == year]

    if not color_col:
        color_col = 'Death Rate'

    # utils.validate_index(df_single_year[color_col])

    # bin color data categorically
    if endpts:
        intervals = utils.endpts_to_intervals(endpts)
        LEVELS = intervals_to_strings(intervals)
    else:
        LEVELS = sorted(df_merged[color_col].unique())

    if len(colorscale) < len(LEVELS):
        print (
            "your number of colors in 'colorscale' must be "
            "at least the number of LEVELS: {}".format(min(LEVELS, LEVELS[:20]))
        )
    color_lookup = dict(zip(LEVELS, colorscale))

    x_traces = dict(zip(LEVELS, [[] for i in range(len(LEVELS))]))
    y_traces = dict(zip(LEVELS, [[] for i in range(len(LEVELS))]))

    SIMPLIFY_FACTOR = 0.05

    # scope
    # TODO: change list to utils.sequence
    if scope != 'usa' and isinstance(scope, list):
        scope_names = []
        for state in scope:
            if state in code_to_country_name_dict.keys():
                state = code_to_country_name_dict[state]
            scope_names.append(state)
        df_single_year = df_single_year[df_single_year['State'].isin(scope_names)]

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
                x = [poly.simplify(SIMPLIFY_FACTOR).exterior.xy[0] for poly in df_single_year['geometry'][index]]
                y = [poly.simplify(SIMPLIFY_FACTOR).exterior.xy[1] for poly in df_single_year['geometry'][index]]
                x_c = [poly.centroid.xy[0] for poly in df_single_year['geometry'][index]]
                y_c = [poly.centroid.xy[1] for poly in df_single_year['geometry'][index]]
                text = row.NAME + '<br>' + color_col + ': ' + level + '<br>' + 'FIPS: ' + str(row.FIPS)
                t_c = [text for poly in df_single_year['geometry'][index]]
                x_centroids = x_c + x_centroids
                y_centroids = y_c + y_centroids
                centroid_text = t_c + centroid_text
            else:
                print('stop')
            x_traces[level] = x_traces[level] + x + [np.nan]
            y_traces[level] = y_traces[level] + y + [np.nan]

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
                t_c = (row.NAME + '<br>' + color_col + ': ' + str(row[color_col]) +
                       '<br>State: ' + row.State + '<br>' + 'FIPS: ' + str(row.FIPS))
                x_centroids.append(x_c[0])
                y_centroids.append(y_c[0])
                centroid_text.append(t_c)
            elif df_single_year['geometry'][index].type == 'MultiPolygon':
                x = [poly.simplify(SIMPLIFY_FACTOR).exterior.xy[0] for poly in df_single_year['geometry'][index]]
                y = [poly.simplify(SIMPLIFY_FACTOR).exterior.xy[1] for poly in df_single_year['geometry'][index]]
                x_c = [poly.centroid.xy[0] for poly in df_single_year['geometry'][index]]
                y_c = [poly.centroid.xy[1] for poly in df_single_year['geometry'][index]]
                text = row.NAME + '<br>' + color_col + ': ' + str(row[color_col]) + '<br>' + 'FIPS: ' + str(row.FIPS)
                t_c = [text for poly in df_single_year['geometry'][index]]
                x_centroids = x_c + x_centroids
                y_centroids = y_c + y_centroids
                centroid_text = t_c + centroid_text
            else:
                print('stop')
            x_traces[level] = x_traces[level] + x + [np.nan]
            y_traces[level] = y_traces[level] + y + [np.nan]

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

    x_states = []
    y_states = []
    SIMPLIFY_FACTOR = 0.1
    for index, row in df_state.iterrows():
        if df_state['geometry'][index].type == 'Polygon':
            x = row.geometry.simplify(SIMPLIFY_FACTOR).exterior.xy[0].tolist()
            y = row.geometry.simplify(SIMPLIFY_FACTOR).exterior.xy[1].tolist()
            x_states = x_states + x
            y_states = y_states + y
        elif df_state['geometry'][index].type == 'MultiPolygon':
            x = [poly.simplify(SIMPLIFY_FACTOR).exterior.xy[0].tolist() for poly in df_state['geometry'][index]]
            y = [poly.simplify(SIMPLIFY_FACTOR).exterior.xy[1].tolist() for poly in df_state['geometry'][index]]
            for segment in range(len(x)):
                x_states = x_states + x[segment]
                y_states = y_states + y[segment]
                x_states.append(np.nan)
                y_states.append(np.nan)
        else:
            print('stop')
        x_states.append(np.nan)
        y_states.append(np.nan)

    for lev in LEVELS:
        county_outline = dict(
            type='scattergl',
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
            legendgroup="centroids",
            x=x_centroids,
            y=y_centroids,
            text=centroid_text,
            hoverinfo='text',
            marker=dict(size=2, color='white'),
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
    orig_diff_x = float(-65 + 125)
    orig_diff_y = float(49 - 25)

    diff_x = fig['layout']['xaxis']['range'][1] - fig['layout']['xaxis']['range'][0]
    diff_y = fig['layout']['yaxis']['range'][1] - fig['layout']['yaxis']['range'][0]
    if diff_x > diff_y:
        pass
    else:
        pass
    return fig


def create_county_choropleth(year, scope='usa', show_hover=True,
                             colorscale=DEFAULT_COLORSCALE, ):

    fig = get_figure(year)
    return fig
fig = get_figure(
    2001, scope=['Texas'], show_hover=True,
    colorscale=None, color_col='Death Rate',
    show_statedata=True, endpts=None,
)
