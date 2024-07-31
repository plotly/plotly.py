import sys
import time
from unittest import TestCase
import pytest
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from plotly.tests.b64 import b64, _b64


def test_performance_b64():
    rand_arr_1 = np.random.random(100000)
    rand_arr_2 = np.random.random(100000)
    raw_arr_1 = rand_arr_1.tolist()
    raw_arr_2 = rand_arr_2.tolist()
    b64_arr_1 = b64(rand_arr_1)
    b64_arr_2 = b64(rand_arr_2)

    # Test the performance of the base64 arrays
    b64_start = time.time()
    fig = go.Scatter(x=b64_arr_1, y=b64_arr_2)
    b64_time_elapsed = time.time() - b64_start

    # Test the performance of the raw arrays
    raw_start = time.time()
    fig = go.Scatter(x=raw_arr_1, y=raw_arr_2)
    raw_time_elapsed = time.time() - raw_start

    # b64 should be faster than raw
    assert (b64_time_elapsed / raw_time_elapsed) < 0.85


def test_size_performance_b64_uint8():
    rand_arr_1 = np.random.random(100000).astype("uint8")
    rand_arr_2 = np.random.random(100000).astype("uint8")
    raw_arr_1 = rand_arr_1.tolist()
    raw_arr_2 = rand_arr_2.tolist()
    b64_arr_1 = b64(rand_arr_1)
    b64_arr_2 = b64(rand_arr_2)

    # Compare the size of figures with b64 arrays and raw arrays
    fig_b64 = go.Scatter(x=b64_arr_1, y=b64_arr_2)
    size_b64 = fig_b64.to_json().__sizeof__()
    fig_raw = go.Scatter(x=raw_arr_1, y=raw_arr_2)
    size_raw = fig_raw.to_json().__sizeof__()

    assert size_b64 / size_raw < .85
