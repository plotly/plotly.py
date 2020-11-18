import plotly.express as px
import numpy as np
import pytest
import xarray as xr
from PIL import Image
from io import BytesIO
import base64
import datetime
from plotly.express.imshow_utils import rescale_intensity

img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]]], dtype=np.uint8)
img_gray = np.arange(100, dtype=np.float).reshape((10, 10))


def decode_image_string(image_string):
    """
    Converts image string to numpy array.
    """
    if "png" in image_string[:22]:
        return np.asarray(Image.open(BytesIO(base64.b64decode(image_string[22:]))))
    elif "jpeg" in image_string[:23]:
        return np.asarray(Image.open(BytesIO(base64.b64decode(image_string[23:]))))
    else:
        raise ValueError("image string format not recognized")


@pytest.mark.parametrize("binary_string", [False, True])
def test_rgb_uint8(binary_string):
    fig = px.imshow(img_rgb, binary_string=binary_string)
    assert fig.data[0]["zmax"] is None


def test_zmax():
    for zmax in [
        100,
        [100],
        (100,),
        [100, 100, 100],
        (100, 100, 100),
        (100, 100, 100, 255),
    ]:
        fig = px.imshow(img_rgb, zmax=zmax, binary_string=False)
        assert fig.data[0]["zmax"] == (100, 100, 100, 255)


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
        fig = px.imshow(img, binary_string=False)
        # For uint8 in "infer" mode we don't pass zmin/zmax unless specified
        if key in [np.uint8, np.bool]:
            assert fig.data[0]["zmax"] is None
        else:
            assert fig.data[0]["zmax"] == (val, val, val, 255)


@pytest.mark.parametrize("binary_string", [False, True])
@pytest.mark.parametrize("binary_format", ["png", "jpg"])
def test_origin(binary_string, binary_format):
    for i, img in enumerate([img_rgb, img_gray]):
        fig = px.imshow(
            img,
            origin="lower",
            binary_string=binary_string,
            binary_format=binary_format,
        )
        assert fig.layout.yaxis.autorange is True
        if binary_string and i == 0 and binary_format == "png":
            # The equality below does not hold for jpeg compression since it's lossy
            assert np.all(img[::-1] == decode_image_string(fig.data[0].source))
        if binary_string:
            if binary_format == "jpg":
                assert fig.data[0].source[:15] == "data:image/jpeg"
            else:
                assert fig.data[0].source[:14] == "data:image/png"
    fig = px.imshow(img_rgb, binary_string=binary_string)
    assert fig.layout.yaxis.autorange is None
    fig = px.imshow(img_gray, binary_string=binary_string)
    if binary_string:
        assert fig.layout.yaxis.autorange is None
    else:
        assert fig.layout.yaxis.autorange == "reversed"


def test_colorscale():
    fig = px.imshow(img_gray)
    plasma_first_color = px.colors.sequential.Plasma[0]
    assert fig.layout.coloraxis1.colorscale[0] == (0.0, plasma_first_color)
    fig = px.imshow(img_gray, color_continuous_scale="Viridis")
    assert fig.layout.coloraxis1.colorscale[0] == (0.0, "#440154")


def test_wrong_dimensions():
    imgs = [1, np.ones((5,) * 3), np.ones((5,) * 4)]
    msg = "px.imshow only accepts 2D single-channel, RGB or RGBA images."
    for img in imgs:
        with pytest.raises(ValueError, match=msg):
            _ = px.imshow(img)


@pytest.mark.parametrize("binary_string", [False, True])
def test_nan_inf_data(binary_string):
    imgs = [np.ones((20, 20)), 255 * np.ones((20, 20))]
    zmaxs = [1, 255]
    for zmax, img in zip(zmaxs, imgs):
        img[0] = 0
        img[10:12] = np.nan
        # the case of 2d/heatmap is handled gracefully by the JS trace but I don't know how to check it
        fig = px.imshow(
            np.dstack((img,) * 3),
            binary_string=binary_string,
            contrast_rescaling="minxmax",
        )
        if not binary_string:
            assert fig.data[0]["zmax"] == (zmax, zmax, zmax, 255)
        else:
            assert fig.data[0]["zmax"] is None


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
        fig = px.imshow(img, binary_string=False)
        assert fig.data[0]["zmax"] == (zmax, zmax, zmax, 255)
    # single-channel
    imgs = [
        np.ones((5, 5)),
        1.02 * np.ones((5, 5)),
        2 * np.ones((5, 5)),
        1000 * np.ones((5, 5)),
    ]
    for zmax, img in zip(zmaxs, imgs):
        fig = px.imshow(img)
        assert fig.data[0]["zmax"] is None


def test_zmin_zmax_range_color():
    img = img_gray / 100.0
    fig = px.imshow(img)
    # assert not (fig.layout.coloraxis.cmin or fig.layout.coloraxis.cmax)
    fig1 = px.imshow(img, zmin=0.2, zmax=0.8)
    fig2 = px.imshow(img, range_color=[0.2, 0.8])
    assert fig1 == fig2
    # color_range overrides zmin and zmax
    fig = px.imshow(img, zmin=0.3, zmax=0.9, range_color=[0.2, 0.8])
    assert fig.layout.coloraxis.cmin == 0.2
    assert fig.layout.coloraxis.cmax == 0.8
    # It's possible to pass only zmin OR zmax
    fig = px.imshow(img, zmax=0.8)
    assert fig.layout.coloraxis.cmin == 0.0
    assert fig.layout.coloraxis.cmax == 0.8


def test_zmin_zmax_range_color_source():
    img = img_gray / 100.0
    fig1 = px.imshow(img, zmin=0.2, zmax=0.8, binary_string=True)
    fig2 = px.imshow(img, range_color=[0.2, 0.8], binary_string=True)
    assert fig1 == fig2


@pytest.mark.parametrize("binary_string", [False, True])
def test_imshow_xarray(binary_string):
    img = np.random.random((20, 30))
    da = xr.DataArray(img, dims=["dim_rows", "dim_cols"])
    fig = px.imshow(da, binary_string=binary_string)
    # Dimensions are used for axis labels and coordinates
    assert fig.layout.xaxis.title.text == "dim_cols"
    assert fig.layout.yaxis.title.text == "dim_rows"
    if not binary_string:
        assert np.all(np.array(fig.data[0].x) == np.array(da.coords["dim_cols"]))


def test_imshow_xarray_slicethrough():
    img = np.random.random((8, 9, 10))
    da = xr.DataArray(img, dims=["dim_0", "dim_1", "dim_2"])
    fig = px.imshow(da, animation_frame="dim_0")
    # Dimensions are used for axis labels and coordinates
    assert fig.layout.xaxis.title.text == "dim_2"
    assert fig.layout.yaxis.title.text == "dim_1"
    assert np.all(np.array(fig.data[0].x) == np.array(da.coords["dim_2"]))


def test_imshow_labels_and_ranges():
    fig = px.imshow([[1, 2], [3, 4], [5, 6]],)
    assert fig.layout.xaxis.title.text is None
    assert fig.layout.yaxis.title.text is None
    assert fig.layout.coloraxis.colorbar.title.text is None
    assert fig.data[0].x is None
    assert fig.data[0].y is None
    fig = px.imshow(
        [[1, 2], [3, 4], [5, 6]],
        x=["a", "b"],
        y=["c", "d", "e"],
        labels=dict(x="the x", y="the y", color="the color"),
    )
    # Dimensions are used for axis labels and coordinates
    assert fig.layout.xaxis.title.text == "the x"
    assert fig.layout.yaxis.title.text == "the y"
    assert fig.layout.coloraxis.colorbar.title.text == "the color"
    assert fig.data[0].x[0] == "a"
    assert fig.data[0].y[0] == "c"

    with pytest.raises(ValueError):
        fig = px.imshow([[1, 2], [3, 4], [5, 6]], x=["a"])

    img = np.ones((2, 2), dtype=np.uint8)
    fig = px.imshow(img, x=["a", "b"])
    assert fig.data[0].x == ("a", "b")

    with pytest.raises(ValueError):
        img = np.ones((2, 2, 3), dtype=np.uint8)
        fig = px.imshow(img, x=["a", "b"])

    img = np.ones((2, 2), dtype=np.uint8)
    base = datetime.datetime(2000, 1, 1)
    fig = px.imshow(img, x=[base, base + datetime.timedelta(hours=1)])
    assert fig.data[0].x == (
        datetime.datetime(2000, 1, 1, 0, 0),
        datetime.datetime(2000, 1, 1, 1, 0),
    )

    with pytest.raises(ValueError):
        img = np.ones((2, 2, 3), dtype=np.uint8)
        base = datetime.datetime(2000, 1, 1)
        fig = px.imshow(img, x=[base, base + datetime.timedelta(hours=1)])


def test_imshow_ranges_image_trace():
    fig = px.imshow(img_rgb, x=[1, 11, 21])
    assert fig.data[0].dx == 10
    assert fig.data[0].x0 == 1
    fig = px.imshow(img_rgb, x=[21, 11, 1])
    assert fig.data[0].dx == -10
    assert fig.data[0].x0 == 21
    assert fig.layout.xaxis.autorange == "reversed"


def test_imshow_dataframe():
    df = px.data.medals_wide(indexed=False)
    fig = px.imshow(df)
    assert fig.data[0].x[0] == df.columns[0]
    assert fig.data[0].x[0] == "nation"
    assert fig.layout.xaxis.title.text is None
    assert fig.data[0].y[0] == df.index[0]
    assert fig.data[0].y[0] == 0
    assert fig.layout.yaxis.title.text is None

    df = px.data.medals_wide(indexed=True)
    fig = px.imshow(df)
    assert fig.data[0].x[0] == df.columns[0]
    assert fig.data[0].x[0] == "gold"
    assert fig.layout.xaxis.title.text == df.columns.name
    assert fig.layout.xaxis.title.text == "medal"
    assert fig.data[0].y[0] == df.index[0]
    assert fig.data[0].y[0] == "South Korea"
    assert fig.layout.yaxis.title.text == df.index.name
    assert fig.layout.yaxis.title.text == "nation"


@pytest.mark.parametrize(
    "dtype",
    [
        np.uint8,
        np.uint16,
        np.int8,
        np.int16,
        np.int32,
        np.int64,
        np.float32,
        np.float64,
    ],
)
@pytest.mark.parametrize("contrast_rescaling", ["minmax", "infer"])
def test_imshow_source_dtype_zmax(dtype, contrast_rescaling):
    img = np.arange(100, dtype=dtype).reshape((10, 10))
    fig = px.imshow(img, binary_string=True, contrast_rescaling=contrast_rescaling)
    if contrast_rescaling == "minmax":
        assert (
            np.max(
                np.abs(
                    rescale_intensity(img, in_range="image", out_range=np.uint8)
                    - decode_image_string(fig.data[0].source)
                )
            )
            < 1
        )
    else:
        if dtype in [np.uint8, np.float32, np.float64]:
            assert np.all(img == decode_image_string(fig.data[0].source))
        else:
            assert (
                np.abs(
                    np.max(decode_image_string(fig.data[0].source))
                    - 255 * img.max() / np.iinfo(dtype).max
                )
                < 1
            )


@pytest.mark.parametrize("backend", ["auto", "pypng", "pil"])
def test_imshow_backend(backend):
    fig = px.imshow(img_rgb, binary_backend=backend)
    decoded_img = decode_image_string(fig.data[0].source)
    assert np.all(decoded_img == img_rgb)


@pytest.mark.parametrize("level", [0, 3, 6, 9])
def test_imshow_compression(level):
    _, grid_img = np.mgrid[0:10, 0:100]
    grid_img = grid_img.astype(np.uint8)
    fig = px.imshow(
        grid_img,
        binary_string=True,
        binary_compression_level=level,
        contrast_rescaling="infer",
    )
    decoded_img = decode_image_string(fig.data[0].source)
    assert np.all(decoded_img == grid_img)
    if level > 0:
        assert len(fig.data[0].source) < grid_img.size
    else:
        assert len(fig.data[0].source) > grid_img.size


@pytest.mark.parametrize("level", [-1, 10])
def test_imshow_invalid_compression(level):
    with pytest.raises(ValueError) as msg:
        _ = px.imshow(img_rgb, binary_compression_level=level)
    assert "between 0 and 9" in str(msg.value)


@pytest.mark.parametrize("binary_string", [False, True])
def test_imshow_hovertemplate(binary_string):
    fig = px.imshow(img_rgb, binary_string=binary_string)
    assert (
        fig.data[0].hovertemplate
        == "x: %{x}<br>y: %{y}<br>color: [%{z[0]}, %{z[1]}, %{z[2]}]<extra></extra>"
    )
    fig = px.imshow(img_gray, binary_string=binary_string)
    if binary_string:
        assert fig.data[0].hovertemplate == "x: %{x}<br>y: %{y}<extra></extra>"
    else:
        assert (
            fig.data[0].hovertemplate
            == "x: %{x}<br>y: %{y}<br>color: %{z}<extra></extra>"
        )


@pytest.mark.parametrize("facet_col", [0, 1, 2, -1])
@pytest.mark.parametrize("binary_string", [False, True])
def test_facet_col(facet_col, binary_string):
    img = np.random.randint(255, size=(10, 9, 8))
    facet_col_wrap = 3
    fig = px.imshow(
        img,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
        binary_string=binary_string,
    )
    nslices = img.shape[facet_col]
    ncols = int(facet_col_wrap)
    nrows = nslices // ncols + 1 if nslices % ncols else nslices // ncols
    nmax = ncols * nrows
    assert "yaxis%d" % nmax in fig.layout
    assert "yaxis%d" % (nmax + 1) not in fig.layout
    assert len(fig.data) == nslices


@pytest.mark.parametrize("animation_frame", [0, 1, 2, -1])
@pytest.mark.parametrize("binary_string", [False, True])
def test_animation_frame_grayscale(animation_frame, binary_string):
    img = np.random.randint(255, size=(10, 9, 8)).astype(np.uint8)
    fig = px.imshow(img, animation_frame=animation_frame, binary_string=binary_string,)
    nslices = img.shape[animation_frame]
    assert len(fig.frames) == nslices


@pytest.mark.parametrize("animation_frame", [0, 1, 2])
@pytest.mark.parametrize("binary_string", [False, True])
def test_animation_frame_rgb(animation_frame, binary_string):
    img = np.random.randint(255, size=(10, 9, 8, 3)).astype(np.uint8)
    fig = px.imshow(img, animation_frame=animation_frame, binary_string=binary_string,)
    nslices = img.shape[animation_frame]
    assert len(fig.frames) == nslices


@pytest.mark.parametrize("binary_string", [False, True])
def test_animation_and_facet(binary_string):
    img = np.random.randint(255, size=(10, 9, 8, 7)).astype(np.uint8)
    fig = px.imshow(img, animation_frame=0, facet_col=1, binary_string=binary_string)
    nslices = img.shape[0]
    assert len(fig.frames) == nslices
    assert len(fig.data) == img.shape[1]
