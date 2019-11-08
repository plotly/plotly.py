import plotly.express as px
import numpy as np
import pytest

img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]]], dtype=np.uint8)
img_gray = np.arange(100).reshape((10, 10))


def test_rgb_uint8():
    fig = px.imshow(img_rgb)
    assert fig.data[0]["zmax"] == (255, 255, 255, 1)


def test_vmax():
    for zmax in [
        100,
        [100],
        (100,),
        [100, 100, 100],
        (100, 100, 100),
        (100, 100, 100, 1),
    ]:
        fig = px.imshow(img_rgb, zmax=zmax)
        assert fig.data[0]["zmax"] == (100, 100, 100, 1)


def test_automatic_zmax_from_dtype():
    dtypes_dict = {
        np.uint8: 2 ** 8 - 1,
        np.uint16: 2 ** 16 - 1,
        np.float: 1,
        np.bool: 255,
    }
    for key, val in dtypes_dict.items():
        img = np.array([0, 1], dtype=key)
        img = np.dstack((img,) * 3)
        fig = px.imshow(img)
        assert fig.data[0]["zmax"] == (val, val, val, 1)


def test_origin():
    for img in [img_rgb, img_gray]:
        fig = px.imshow(img, origin="lower")
        assert fig.layout.yaxis.autorange == True
    fig = px.imshow(img_rgb)
    assert fig.layout.yaxis.autorange is None
    fig = px.imshow(img_gray)
    assert fig.layout.yaxis.autorange == "reversed"


def test_colorscale():
    fig = px.imshow(img_gray)
    plasma_first_color = px.colors.sequential.Plasma[0]
    assert fig.layout.coloraxis1.colorscale[0] == (0.0, plasma_first_color)
    fig = px.imshow(img_gray, color_continuous_scale="Viridis")
    assert fig.layout.coloraxis1.colorscale[0] == (0.0, "#440154")


def test_wrong_dimensions():
    imgs = [1, np.ones((5,) * 3), np.ones((5,) * 4)]
    for img in imgs:
        with pytest.raises(ValueError) as err_msg:
            fig = px.imshow(img)


def test_nan_inf_data():
    imgs = [np.ones((20, 20)), 255 * np.ones((20, 20), dtype=np.uint8)]
    zmaxs = [1, 255]
    for zmax, img in zip(zmaxs, imgs):
        img[0] = 0
        img[10:12] = np.nan
        # the case of 2d/heatmap is handled gracefully by the JS trace but I don't know how to check it
        fig = px.imshow(np.dstack((img,) * 3))
        assert fig.data[0]["zmax"] == (zmax, zmax, zmax, 1)


def test_zmax_floats():
    # RGB
    imgs = [
        np.ones((5, 5, 3)),
        1.02 * np.ones((5, 5, 3)),
        2 * np.ones((5, 5, 3)),
        1000 * np.ones((5, 5, 3)),
    ]
    zmaxs = [1, 1, 255, 65535]
    for zmax, img in zip(zmaxs, imgs):
        fig = px.imshow(img)
        assert fig.data[0]["zmax"] == (zmax, zmax, zmax, 1)
    # single-channel
    imgs = [
        np.ones((5, 5)),
        1.02 * np.ones((5, 5)),
        2 * np.ones((5, 5)),
        1000 * np.ones((5, 5)),
    ]
    for zmax, img in zip(zmaxs, imgs):
        fig = px.imshow(img)
        print(fig.data[0]["zmax"], zmax)
        assert fig.data[0]["zmax"] == None
