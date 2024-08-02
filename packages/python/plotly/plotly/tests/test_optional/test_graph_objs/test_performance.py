import time
import numpy as np
import plotly.graph_objs as go
import pytest

np.random.seed(1)


def test_performance_b64_scatter3d():
    N = 10000

    x = np.random.randn(N)
    y = np.random.randn(N).astype("float32")
    z = np.random.randint(size=N, low=0, high=256, dtype="uint8")
    c = np.random.randint(size=N, low=-10, high=10, dtype="int8")

    # Test the performance with lists
    x_list = x.tolist()
    y_list = y.tolist()
    z_list = z.tolist()
    c_list = c.tolist()
    list_start = time.time()
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x_list,
                y=y_list,
                z=z_list,
                marker=dict(color=c_list),
                mode="markers",
                opacity=0.2,
            )
        ]
    )
    fig.show()
    list_time_elapsed = time.time() - list_start

    # Test the performance with base64 arrays
    np_start = time.time()
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                marker=dict(color=c),
                mode="markers",
                opacity=0.2,
            )
        ]
    )
    fig.show()
    np_time_elapsed = time.time() - np_start

    # np should be faster than lists
    assert (np_time_elapsed / list_time_elapsed) < 0.55


FLOAT_TEST_CASES = [
    ("float32", 100000, 0.45),  # dtype  # difference threshold
    ("float64", 10000, 0.55),
]


@pytest.mark.parametrize("dtype, count, expected_size_difference", FLOAT_TEST_CASES)
def test_performance_b64_float(dtype, count, expected_size_difference):
    np_arr_1 = np.random.random(count).astype(dtype)
    np_arr_2 = np.random.random(count).astype(dtype)
    list_1 = np_arr_1.tolist()
    list_2 = np_arr_2.tolist()

    # Test the performance of the base64 arrays
    np_start = time.time()
    fig = go.Figure(data=[go.Scatter(x=np_arr_1, y=np_arr_2)])
    fig.show()
    np_time_elapsed = time.time() - np_start

    # Test the performance of the normal lists
    list_start = time.time()
    fig = go.Figure(data=[go.Scatter(x=list_1, y=list_2)])
    fig.show()
    list_time_elapsed = time.time() - list_start

    # np should be faster than lists
    assert (np_time_elapsed / list_time_elapsed) < expected_size_difference


INT_SIZE_PERFORMANCE_TEST_CASES = [
    ("uint8", 256, 100000, 30000),
    ("uint32", 2**32, 100000, 100000),
]


@pytest.mark.parametrize(
    "dtype, max_value, count, expected_size_difference", INT_SIZE_PERFORMANCE_TEST_CASES
)
def test_size_performance_b64_int(dtype, max_value, count, expected_size_difference):
    np_arr_1 = (np.random.random(count) * max_value).astype(dtype)
    np_arr_2 = (np.random.random(count) * max_value).astype(dtype)

    # Measure the size of figures with numpy arrays
    fig_np = go.Scatter(x=np_arr_1, y=np_arr_2)
    size_np = fig_np.to_json().__sizeof__()

    # Measure the size of the figure with normal python lists
    fig_list = go.Scatter(x=np_arr_1.tolist(), y=np_arr_2.tolist())
    size_list = fig_list.to_json().__sizeof__()

    # np should be smaller than lists
    assert size_list - size_np > expected_size_difference
