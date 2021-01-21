import pickle

from _plotly_utils.optional_imports import get_module
from plotly.io._json import clean_to_json_compatible
from plotly.io.json import to_json_plotly
import time
import copy

modules = {
    "sage_all": get_module("sage.all", should_load=False),
    "np": get_module("numpy", should_load=False),
    "pd": get_module("pandas", should_load=False),
    "image": get_module("PIL.Image", should_load=False),
}

# path = '/home/jmmease/PyDev/repos/plotly.py/doc/timing/json_object/ed9498c3-25ca-4634-82d2-ee8c1837f24a.pkl'
path = '/doc/timing/json_object0/df55a585-3c9b-4097-8232-6778ecd620a2.pkl'
with open(path, "rb") as f:
    json_object = pickle.load(f)


def json_clean_json(plotly_object):
    return clean_to_json_compatible(
        plotly_object,
        numpy_allowed=False,
        datetime_allowed=False,
        modules=modules,
    )


def json_clean_orjson(plotly_object):
    return clean_to_json_compatible(
        plotly_object,
        numpy_allowed=True,
        datetime_allowed=True,
        modules=modules,
    )

if __name__ == "__main__":
    trials = 10
    for engine in ["legacy", "json", "orjson"]:
        t0 = time.time_ns()
        for _ in range(trials):
            to_json_plotly(json_object, engine=engine)

        t = (time.time_ns() - t0) / trials / 1000000
        print(f"Time for {trials} trials with engine {engine}: {t}")

    clean_json = json_clean_orjson(plotly_object=json_object)

    t0 = time.time_ns()
    for _ in range(trials):
        to_json_plotly(clean_json, engine="orjson")

    t = (time.time_ns() - t0) / trials / 1000000
    print(f"Time for {trials} trials with orjson after cleaning: {t}")

    # # cloning times
    # t0 = time.time_ns()
    # for _ in range(trials):
    #     copy.deepcopy(json_object)
    #
    # t = (time.time_ns() - t0) / trials / 1000000
    # print(f"Time to deep copy for {trials} trials: {t}")
    #
    # # Cleaning times
    # for clean in [json_clean_json, json_clean_orjson]:
    #     t0 = time.time_ns()
    #     for _ in range(trials):
    #         clean(json_object)
    #
    #     t = (time.time_ns() - t0) / trials / 1000000
    #     print(f"Time to clean for {trials} trials with {json_clean_json.__name__}: {t}")
