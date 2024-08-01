import time
import numpy as np
import plotly.graph_objs as go

np.random.seed(1)


def test_performance_b64_scatter3d():
    N = 10000

    x = np.random.randn(N)
    y = np.random.randn(N).astype("float32")
    z = np.random.randint(size=N, low=0, high=256, dtype="uint8")
    c = np.random.randint(size=N, low=-10, high=10, dtype="int8")

    # Test the performance with lists
    list_start = time.time()
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x.tolist(),
                y=y.tolist(),
                z=z.tolist(),
                marker=dict(color=c.tolist()),
                mode="markers",
                opacity=0.2,
            )
        ]
    )
    list_time_elapsed = time.time() - list_start

    # Test the performance with base64 arrays
    np_start = time.time()
    fig = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        marker=dict(color=c),
        mode="markers",
        opacity=0.2,
    )
    np_time_elapsed = time.time() - np_start

    # np should be faster than raw
    assert (np_time_elapsed / list_time_elapsed) < 0.75


def test_performance_b64_float64():
    np_arr_1 = np.random.random(10000)
    np_arr_2 = np.random.random(10000)

    # Test the performance of the base64 arrays
    np_start = time.time()
    fig = go.Scatter(x=np_arr_1, y=np_arr_2)
    np_time_elapsed = time.time() - np_start

    # Test the performance of the raw arrays
    list_start = time.time()
    fig = go.Scatter(x=np_arr_1.tolist(), y=np_arr_2.tolist())
    list_time_elapsed = time.time() - list_start

    # np should be faster than raw
    assert (np_time_elapsed / list_time_elapsed) < 0.75


def test_size_performance_b64_uint8():
    np_arr_1 = (np.random.random(100000) * 256).astype("uint8")
    np_arr_2 = (np.random.random(100000) * 256).astype("uint8")

    # Measure the size of figures with numpy arrays
    fig_np = go.Scatter(x=np_arr_1, y=np_arr_2)
    size_np = fig_np.to_json().__sizeof__()

    # Measure the size of the figure with normal python lists
    fig_list = go.Scatter(x=np_arr_1.tolist(), y=np_arr_2.tolist())
    size_list = fig_list.to_json().__sizeof__()

    # np should be smaller than raw
    assert size_list - size_np > 1000
