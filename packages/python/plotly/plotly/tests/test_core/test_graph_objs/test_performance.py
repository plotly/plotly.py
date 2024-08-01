import time
import numpy as np
import plotly.graph_objs as go
from plotly.tests.b64 import b64

np.random.seed(1)

def test_performance_scatter3d():
    N = 10000

    x = np.random.randn(N)
    y = np.random.randn(N).astype('float32')
    z = np.random.randint(size=N, low=0, high=256, dtype='uint8')
    c = np.random.randint(size=N, low=-10, high=10, dtype='int8')

    # Test the performance with lists
    list_start = time.time()
    fig = go.Figure(data=[go.Scatter3d(
        x=x.tolist(),
        y=y.tolist(),
        z=z.tolist(),
        marker=dict(color=c.tolist()),
        mode='markers',
        opacity=0.2
    )])
    list_time_elapsed = time.time() - list_start

    # Test the performance with base64 arrays
    b64_start = time.time()
    fig = go.Scatter3d(
        x=b64(x),
        y=b64(y),
        z=b64(z),
        marker=dict(color=b64(c)),
        mode='markers',
        opacity=0.2
    )
    b64_time_elapsed = time.time() - b64_start

    # b64 should be faster than raw
    assert (b64_time_elapsed / list_time_elapsed) < 0.75

def test_performance_b64_float64():
    np_arr_1 = np.random.random(10000)
    np_arr_2 = np.random.random(10000)

    # Test the performance of the base64 arrays
    b64_start = time.time()
    fig = go.Scatter(x=b64(np_arr_1), y=b64(np_arr_2))
    b64_time_elapsed = time.time() - b64_start

    # Test the performance of the raw arrays
    list_start = time.time()
    fig = go.Scatter(x=np_arr_1.tolist(), y=np_arr_2.tolist())
    list_time_elapsed = time.time() - list_start

    # b64 should be faster than raw
    assert (b64_time_elapsed / list_time_elapsed) < 0.75


def test_size_performance_b64_uint8():
    np_arr_1 = (np.random.random(100000) * 256).astype("uint8")
    np_arr_2 = (np.random.random(100000) * 256).astype("uint8")

    # Measure the size of figures with b64 arrays
    fig_b64 = go.Scatter(x=b64(np_arr_1), y=b64(np_arr_2))
    size_b64 = fig_b64.to_json().__sizeof__()

    # Measure the size of the figure with normal python lists
    fig_list = go.Scatter(x=np_arr_1.tolist(), y=np_arr_2.tolist())
    size_list = fig_list.to_json().__sizeof__()

    # b64 should be smaller than raw
    assert size_b64 / size_list < 0.75
