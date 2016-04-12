from six.moves.urllib.request import urlopen as uo
import re


def get_latest():
    data = uo('https://raw.githubusercontent.com/plotly/plotly.py/' +
              'master/plotly/version.py')
    version = [i for i in data][0]
    latest_version = re.findall(r'([0-9\.]+)', str(version))[0]
    return latest_version


def run_duration(f, **kwargs):
    import timeit
    start_time = timeit.default_timer()
    f(**kwargs)
    return (timeit.default_timer() - start_time)
