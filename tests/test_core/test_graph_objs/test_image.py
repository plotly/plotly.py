import numpy as np
import pytest

import plotly.graph_objects as go

Z3 = np.random.randint(256, size=(10, 10, 3), dtype=np.uint8)
Z4 = np.random.randint(256, size=(10, 10, 4), dtype=np.uint8)


# Regression tests for https://github.com/plotly/plotly.py/issues/1973
# The number of components of zmin/zmax depends on the colormodel
# (3 for rgb/hsl, 4 for rgba/rgba256/hsla), so both lengths must validate.
@pytest.mark.parametrize(
    "colormodel,z,zmin,zmax",
    [
        ("rgb", Z3, [0, 0, 0], [255, 255, 255]),
        ("hsl", Z3, [0, 0, 0], [360, 100, 100]),
        ("rgba", Z4, [0, 0, 0, 0], [255, 255, 255, 1]),
        ("rgba256", Z4, [0, 0, 0, 0], [255, 255, 255, 255]),
        ("hsla", Z4, [0, 0, 0, 0], [360, 100, 100, 1]),
        # A 4-element value must keep working for 3-component models too,
        # as it did before this fix (it was the only length accepted).
        ("rgb", Z3, [0, 0, 0, 0], [255, 255, 255, 255]),
    ],
)
def test_image_zmin_zmax_matching_colormodel(colormodel, z, zmin, zmax):
    img = go.Image(z=z, colormodel=colormodel, zmin=zmin, zmax=zmax)
    assert img.zmin == tuple(zmin)
    assert img.zmax == tuple(zmax)


def test_image_zmin_zmax_issue_example():
    # The exact example from #1973
    im = np.random.randint(256, size=(50, 50, 3), dtype=np.uint8)
    fig = go.Figure(
        go.Image(z=im, colormodel="rgb", zmin=[10, 10, 10], zmax=[100, 100, 100])
    )
    assert fig.data[0].zmin == (10, 10, 10)
    assert fig.data[0].zmax == (100, 100, 100)


def test_image_zmin_zmax_default_colormodel():
    # colormodel defaults to "rgb", so 3 elements are valid without it.
    img = go.Image(z=Z3, zmin=[0, 0, 0], zmax=[255, 255, 255])
    assert img.zmax == (255, 255, 255)


def test_image_zmin_zmax_assignment_order():
    # Validation must not depend on the order properties are set in.
    img = go.Image(z=Z3, zmin=[0, 0, 0, 0], zmax=[255, 255, 255, 255])
    img.colormodel = "rgb"
    img.zmin = [0, 0, 0]
    img.zmax = [255, 255, 255]
    assert img.zmin == (0, 0, 0)


@pytest.mark.parametrize("colormodel", ["rgb", "rgba", "rgba256", "hsl", "hsla"])
def test_image_zmin_zmax_five_elements_rejected(colormodel):
    with pytest.raises(ValueError):
        go.Image(z=Z4, colormodel=colormodel, zmax=[1, 2, 3, 4, 5])


def test_image_zmin_zmax_non_numeric_rejected():
    with pytest.raises(ValueError):
        go.Image(z=Z3, colormodel="rgb", zmax=["a", "b", "c"])


def test_heatmap_zmin_zmax_scalar_unaffected():
    hm = go.Heatmap(z=[[1, 2], [3, 4]], zmin=0, zmax=5)
    assert hm.zmin == 0
    assert hm.zmax == 5
