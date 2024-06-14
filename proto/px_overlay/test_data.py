import numpy as np
import plotly.express as px
import pandas as pd
from random import sample
from itertools import product
from functools import reduce

# some made up data for demos


def words(remove_non_letters=True):
    with open("/usr/share/dict/british-english", "r") as fd:
        ws = fd.readlines()
    return [w.strip().replace("'s", "") for w in ws]


def aug_tips():
    """ The tips data buf with "calories consumed". """
    tips = px.data.tips()
    calories = np.clip(
        tips["total_bill"] * 30 + np.random.standard_normal(tips.shape[0]) * 100,
        100,
        None,
    )
    tips["calories_consumed"] = calories
    return tips


def take(it, N):
    return [next(it) for n in range(N)]


def multilayered_data(
    N=20, d_divs=[2, 3, 4], rseed=np.random.RandomState(seed=2), rwalk=0.1
):
    """
    Generate data that can be faceted in len(d_divs) ways (e.g., row, col and
    trace color/linestyle. etc.)
    """
    ws = words()
    tot_divs = np.cumprod(d_divs)[-1]
    sample_i = np.arange(len(ws), dtype="int")
    rseed.shuffle(sample_i)
    names = iter(ws[i] for i in sample_i[: tot_divs + len(d_divs)])
    x = np.arange(N)
    cat_div_names = []
    for div in d_divs:
        # generate category names
        div_names = [next(names) for _ in range(div)]
        cat_div_names.append(div_names)
    cat_names = [next(names) for _ in d_divs]
    dfs = []
    for cat_combo in product(*cat_div_names):
        d = dict()
        for cat_name, c in zip(cat_names, cat_combo):
            d[cat_name] = c
        d["x"] = x
        if rwalk is not None:
            y = np.cumsum(rseed.standard_normal(N)) * rwalk
        else:
            y = rseed.standard_normal(N)
        d["y"] = y
        dfs.append(pd.DataFrame(d))
    # combine all the dicts
    df = reduce(lambda a, b: pd.concat([a, b]), dfs, pd.DataFrame())
    return df
