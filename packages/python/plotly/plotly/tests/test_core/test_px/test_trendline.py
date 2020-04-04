import plotly.express as px
import numpy as np


def test_trendline_nan_values():
    df = px.data.gapminder().query("continent == 'Oceania'")
    start_date = 1970
    df['pop'][df['year'] < start_date] = np.nan
    fig = px.scatter(df, x='year', y='pop', color='country', trendline='ols')
    country_numbers = len(fig['data']) // 2
    for trendline in fig['data'][1::2]:
        assert trendline.x[0] >= start_date
