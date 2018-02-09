from plotly import colors, exceptions, optional_imports

from plotly.figure_factory import utils

import array
import geopandas as gp
import numpy as np
import pandas as pd
import shapefile

from shapely.geometry import MultiPolygon, Polygon, shape
from numbers import Number


def _create_us_counties_df(code_to_country_name_dict, state_to_st_dict):
    # URLS
    pre_url = 'plotly/package_data/data/'

    shape_pre2010 = 'gz_2010_us_050_00_500k/gz_2010_us_050_00_500k.shp'
    shape_pre2010 = pre_url + shape_pre2010
    df_shape_pre2010 = gp.read_file(shape_pre2010)
    df_shape_pre2010['FIPS'] = df_shape_pre2010['STATE'] + df_shape_pre2010['COUNTY']
    df_shape_pre2010['FIPS'] = pd.to_numeric(df_shape_pre2010['FIPS'])

    states_path = 'cb_2016_us_state_500k/cb_2016_us_state_500k.shp'
    states_path = pre_url + states_path

    # state df
    df_state = gp.read_file(states_path)
    df_state = df_state[['STATEFP', 'NAME', 'geometry']]

    preurl = 'plotly/package_data/data/cb_2016_us_county_500k/'
    filenames = ['cb_2016_us_county_500k.dbf',
                 'cb_2016_us_county_500k.prj',
                 'cb_2016_us_county_500k.shp',
                 'cb_2016_us_county_500k.shx']

    for j in range(len(filenames)):
        filenames[j] = preurl + filenames[j]

    dbf = open(filenames[0], 'r')
    prj = open(filenames[1], 'r')
    shp = open(filenames[2], 'r')
    shx = open(filenames[3], 'r')

    r = shapefile.Reader(shp=shp, shx=shx, dbf=dbf)

    attributes, geometry = [], []
    field_names = [field[0] for field in r.fields[1:]]
    for row in r.shapeRecords():
        geometry.append(shape(row.shape.__geo_interface__))
        attributes.append(dict(zip(field_names, row.record)))

    gdf = gp.GeoDataFrame(data=attributes, geometry=geometry)

    gdf['FIPS'] = gdf['STATEFP'] + gdf['COUNTYFP']
    gdf['FIPS'] = pd.to_numeric(gdf['FIPS'])

    # add missing counties
    f = 46113
    singlerow = pd.DataFrame(
        [
            [code_to_country_name_dict['SD'], 'SD',
             df_shape_pre2010[df_shape_pre2010['FIPS'] == f]['geometry'].iloc[0],
             df_shape_pre2010[df_shape_pre2010['FIPS'] == f]['FIPS'].iloc[0],
             '46']
        ],
        columns=['State', 'ST', 'geometry', 'FIPS', 'STATEFP'],
        index=[max(gdf.index) + 1]
    )
    gdf = gdf.append(singlerow)

    f = 51515
    singlerow = pd.DataFrame(
        [
            [code_to_country_name_dict['VA'], 'VA',
             df_shape_pre2010[df_shape_pre2010['FIPS'] == f]['geometry'].iloc[0],
             df_shape_pre2010[df_shape_pre2010['FIPS'] == f]['FIPS'].iloc[0],
             '51']
        ],
        columns=['State', 'ST', 'geometry', 'FIPS', 'STATEFP'],
        index = [max(gdf.index) + 1]
    )
    gdf = gdf.append(singlerow)

    f = 2270
    singlerow = pd.DataFrame(
        [
            [code_to_country_name_dict['AK'], 'AK',
             df_shape_pre2010[df_shape_pre2010['FIPS'] == f]['geometry'].iloc[0],
             df_shape_pre2010[df_shape_pre2010['FIPS'] == f]['FIPS'].iloc[0],
             '02']
        ],
        columns=['State', 'ST', 'geometry', 'FIPS', 'STATEFP'],
        index = [max(gdf.index) + 1]
    )
    gdf = gdf.append(singlerow)

    row_2198 = gdf[gdf['FIPS'] == 2198]
    row_2198.index = [max(gdf.index) + 1]
    row_2198.loc[row_2198.index[0], 'FIPS'] = 2201
    row_2198.loc[row_2198.index[0], 'STATEFP'] = '02'
    gdf = gdf.append(row_2198)

    row_2105 = gdf[gdf['FIPS'] == 2105]
    row_2105.index = [max(gdf.index) + 1]
    row_2105.loc[row_2105.index[0], 'FIPS'] = 2232
    row_2105.loc[row_2105.index[0], 'STATEFP'] = '02'
    gdf = gdf.append(row_2105)

    gdf_reduced = gdf[['FIPS', 'STATEFP', 'geometry']]
    gdf_statefp = gdf_reduced.merge(df_state[['STATEFP', 'NAME']], on='STATEFP')

    ST = []
    for n in gdf_statefp['NAME']:
        ST.append(state_to_st_dict[n])

    gdf_statefp['ST'] = ST
    return gdf_statefp, df_state

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

state_to_st_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Commonwealth of the Northern Mariana Islands': 'MP',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': '',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'United States Virgin Islands': 'VI',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

df, df_state = _create_us_counties_df(code_to_country_name_dict, state_to_st_dict)


fips_polygon_map = dict(
    zip(
        df['FIPS'].tolist(),
        df['geometry'].tolist()
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


def _calculations2(df, fips, values, index, f, simplify_county, level,
                   x_centroids, y_centroids, centroid_text, x_traces, y_traces):
    if fips_polygon_map[f].type == 'Polygon':
        x = fips_polygon_map[f].simplify(simplify_county).exterior.xy[0].tolist()
        y = fips_polygon_map[f].simplify(simplify_county).exterior.xy[1].tolist()

        x_c, y_c = fips_polygon_map[f].centroid.xy
        t_c = (
            'County: ' + df[df['FIPS'] == f]['NAME'].iloc[0] + '<br>' +
            'FIPS: ' + str(f) + '<br>' + 'Value: ' + str(values[index])
        )

        x_centroids.append(x_c[0])
        y_centroids.append(y_c[0])
        centroid_text.append(t_c)

        x_traces[level] = x_traces[level] + x + [np.nan]
        y_traces[level] = y_traces[level] + y + [np.nan]
    elif fips_polygon_map[f].type == 'MultiPolygon':
        x = ([poly.simplify(simplify_county).exterior.xy[0].tolist() for
              poly in fips_polygon_map[f]])
        y = ([poly.simplify(simplify_county).exterior.xy[1].tolist() for
              poly in fips_polygon_map[f]])

        x_c = [poly.centroid.xy[0].tolist() for poly in fips_polygon_map[f]]
        y_c = [poly.centroid.xy[1].tolist() for poly in fips_polygon_map[f]]

        text = (
            'County: ' + df[df['FIPS'] == f]['NAME'].iloc[0] + '<br>' +
            'FIPS: ' + str(f) + '<br>' + 'Value: ' + str(values[index])
        )
        t_c = [text for poly in fips_polygon_map[f]]
        x_centroids = x_c + x_centroids
        y_centroids = y_c + y_centroids
        centroid_text = t_c + centroid_text
        for x_y_idx in range(len(x)):
            x_traces[level] = x_traces[level] + x[x_y_idx] + [np.nan]
            y_traces[level] = y_traces[level] + y[x_y_idx] + [np.nan]

    return x_traces, y_traces, x_centroids, y_centroids, centroid_text


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


def create_choropleth(fips, values, scope='usa', colorscale=None, order=None,
                      zoom=False, endpts=None, simplify_county=0.02,
                      simplify_state=0.02, asp=None, offline_mode=False,
                      show_hover=True, show_statedata=True,
                      state_outline_line=None, county_outline_line=None,
                      centroid_marker=None, df=df, df_state=df_state,
                      **layout_options):
    """
    Returns figure for county choropleth. Uses data from package_data.

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
    if not state_outline_line:
        state_outline_line = {'color': 'rgb(240, 240, 240)',
                              'width': 1}
    if not county_outline_line:
        county_outline_line = {'color': 'rgb(0, 0, 0)',
                               'width': 0}
    if not centroid_marker:
        centroid_marker = {'size': 2,
                           'color': 'rgb(255, 255, 255)',
                           'opacity': 1}

    xaxis_range_low = 0
    xaxis_range_high = -1000
    yaxis_range_low = 1000
    yaxis_range_high = 0

    if len(fips) != len(values):
        raise exceptions.PlotlyError(
            'fips and values must be the same length'
        )

    # make fips numeric
    fips = map(lambda x: int(x), fips)

    if endpts:
        intervals = utils.endpts_to_intervals(endpts)
        LEVELS = _intervals_as_labels(intervals)
    else:
        if not order:
            LEVELS = sorted(list(set(values)))
        else:
            # check if order is permutation
            # of unique color col values
            same_sets = sorted(list(set(values))) == set(order)
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
        colorscale = []
        viridis_colors = colors.colorscale_to_colors(
            colors.PLOTLY_SCALES['Viridis']
        )
        viridis_colors = colors.color_parser(
            viridis_colors, colors.hex_to_rgb
        )
        viridis_colors = colors.color_parser(
            viridis_colors, colors.label_rgb
        )
        viri_len = len(viridis_colors)
        viri_intervals = utils.endpts_to_intervals(
            list(np.linspace(0, 1, viri_len))
        )[1:-1]

        for l in np.linspace(0, 1, len(LEVELS)):
            for idx, inter in enumerate(viri_intervals):
                if l == 0:
                    break
                elif inter[0] < l <= inter[1]:
                    break
            
            intermed = ((l - viri_intervals[idx][0]) /
                        (viri_intervals[idx][1] - viri_intervals[idx][0]))
            colorscale.append(
                colors.find_intermediate_color(
                    viridis_colors[idx],
                    viridis_colors[idx],
                    intermed,
                    colortype='rgb'
                )
            )

        print colorscale

    if len(colorscale) < len(LEVELS):
        raise exceptions.PlotlyError(
            "You have {} LEVELS. Your number of colors in 'colorscale' must "
            "be at least the number of LEVELS: {}. If you are "
            "using 'endpts' then 'colorscale' must have at "
            "least len(endpts) + 2 colors".format(
                len(LEVELS), min(LEVELS, LEVELS[:20])
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
        df = df[df['NAME'].isin(scope_names)]
    else:
        scope_names = df['NAME'].unique()

    plot_data = []
    x_centroids = []
    y_centroids = []
    centroid_text = []
    if not endpts:
        for index, f in enumerate(fips):
            level = values[index]

            (x_traces, y_traces, x_centroids,
             y_centroids, centroid_text) = _calculations2(
                df, fips, values, index, f, simplify_county, level,
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
        for index, f in enumerate(fips):
            for j, inter in enumerate(intervals):
                if inter[0] < values[index] <= inter[1]:
                    break
            level = LEVELS[j]

            (x_traces, y_traces, x_centroids,
             y_centroids, centroid_text) = _calculations2(
                df, fips, values, index, f, simplify_county, level,
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
            line=county_outline_line,
            fill='toself',
            fillcolor=color_lookup[lev],
            name=lev,
            hoverinfo=None,
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
            mode='markers',
            marker=centroid_marker,
        )
        if offline_mode:
            centroids_on_select = dict(
                selected=dict(
                    marker=dict(size=2, color='white', opacity=1)
                ),
                unselected=dict(
                    marker=Districtct(opacity=0)
                )
            )
            hover_points.update(centroids_on_select)
        plot_data.append(hover_points)

    if show_statedata:
        state_data = dict(
            type='scatter',
            legendgroup='States',
            line=state_outline_line,
            x=x_states,
            y=y_states,
            hoverinfo='none',
            showlegend=False,
            mode='lines'
        )
        plot_data.append(state_data)

    fig = dict(data=plot_data, layout=DEFAULT_LAYOUT)


    # layout options
    fig['layout'].update(
        title='',
        margin=dict(t=40)
    )
    fig['layout'].update(layout_options)

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
