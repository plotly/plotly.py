from _plotly_utils.colors import (
    find_intermediate_color,
    hex_to_rgb,
    label_rgb,
    unlabel_rgb,
)


def test_hex_to_rgb_basic_values():
    assert hex_to_rgb("#ffffff") == (255, 255, 255)
    assert hex_to_rgb("#000000") == (0, 0, 0)
    assert hex_to_rgb("#aabbcc") == (170, 187, 204)


def test_hex_to_rgb_shorthand_3_digit():
    assert hex_to_rgb("#fff") == (255, 255, 255)
    assert hex_to_rgb("#000") == (0, 0, 0)
    assert hex_to_rgb("#abc") == (170, 187, 204)
    assert hex_to_rgb("#f00") == (255, 0, 0)
    assert hex_to_rgb("#0f0") == (0, 255, 0)
    assert hex_to_rgb("#00f") == (0, 0, 255)


def test_label_rgb_formats_tuple():
    assert label_rgb((255, 0, 0)) == "rgb(255, 0, 0)"
    assert label_rgb((1, 2, 3)) == "rgb(1, 2, 3)"


def test_unlabel_rgb_parses_string():
    assert unlabel_rgb("rgb(255, 0, 0)") == (255.0, 0.0, 0.0)
    assert unlabel_rgb("rgb(1, 2, 3)") == (1.0, 2.0, 3.0)


def test_label_and_unlabel_are_inverses():
    assert unlabel_rgb(label_rgb((10, 20, 30))) == (10.0, 20.0, 30.0)


def test_find_intermediate_color_tuple_midpoint():
    assert find_intermediate_color((0, 0, 0), (1, 1, 1), 0.5) == (0.5, 0.5, 0.5)


def test_find_intermediate_color_endpoints():
    low, high = (0.0, 0.0, 0.0), (1.0, 1.0, 1.0)
    assert find_intermediate_color(low, high, 0.0) == low
    assert find_intermediate_color(low, high, 1.0) == high


def test_find_intermediate_color_rgb_colortype():
    result = find_intermediate_color(
        "rgb(0, 0, 0)", "rgb(10, 20, 30)", 0.5, colortype="rgb"
    )
    assert result == "rgb(5.0, 10.0, 15.0)"
