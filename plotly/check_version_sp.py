import subprocess


def get_latest():
    latest_version = subprocess.check_output(
        ['pip', 'show', 'plotly']).split('\n')[2][9:]
    return latest_version


def run_duration(f, **kwargs):
    import timeit
    start_time = timeit.default_timer()
    f(**kwargs)
    return (timeit.default_timer() - start_time)
