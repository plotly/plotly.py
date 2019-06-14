"""
Built-in datasets for demonstration, educational and test purposes.
"""


def gapminder():
    """
    Each row represents a country on a given year.

    https://www.gapminder.org/data/

    Returns:
        A `pandas.DataFrame` with 1704 rows and the following columns: `['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap',
       'iso_alpha', 'iso_num']`.
    """
    return _get_dataset("gapminder")


def tips():
    """
    Each row represents a restaurant bill.

    https://vincentarelbundock.github.io/Rdatasets/doc/reshape2/tips.html

    Returns:
        A `pandas.DataFrame` with 244 rows and the following columns: `['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']`.
    """
    return _get_dataset("tips")


def iris():
    """
    Each row represents a flower.

    https://en.wikipedia.org/wiki/Iris_flower_data_set

    Returns:
        A `pandas.DataFrame` with 150 rows and the following columns: `['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species',
       'species_id']`.
    """
    return _get_dataset("iris")


def wind():
    """
    Each row represents a level of wind intensity in a cardinal direction.

    Returns:
        A `pandas.DataFrame` with 128 rows and the following columns: `['direction', 'strength', 'value']`.
    """
    return _get_dataset("wind")


def election():
    """
    Each row represents voting results for an electoral district in the 2013 Montreal mayoral election.

    Returns:
        A `pandas.DataFrame` with 58 rows and the following columns: `['district', 'Coderre', 'Bergeron', 'Joly', 'total', 'winner', 'result']`.
    """
    return _get_dataset("election")


def carshare():
    """
    Each row represents the availability of car-sharing services near the centroid of a zone in Montreal.

    Returns:
        A `pandas.DataFrame` with 249 rows and the following columns: `['centroid_lat', 'centroid_lon', 'car_hours', 'peak_hour']`.
    """
    return _get_dataset("carshare")


def _get_dataset(d):
    import pandas
    import os

    return pandas.read_csv(os.path.join(os.path.dirname(__file__), d + ".csv.gz"))
