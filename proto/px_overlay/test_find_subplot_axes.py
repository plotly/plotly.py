from plotly.subplots import make_subplots
import px_overlay
import pytest

fig = px_overlay.make_subplots_all_secondary_y(3, 4)
fig_no_sy = px_overlay.make_subplots(3, 4)
fig_custom = make_subplots(
    rows=2,
    cols=2,
    specs=[[{}, {}], [{"colspan": 2}, None]],
    subplot_titles=("First Subplot", "Second Subplot", "Third Subplot"),
)


def test_bad_row_col():
    with pytest.raises(
        IndexError,
        match=r"^Figure does not have a subplot at the requested row or column\.$",
    ):
        px_overlay.find_subplot_axes(fig, 4, 2, secondary_y=False)
    with pytest.raises(
        IndexError,
        match=r"^Figure does not have a subplot at the requested row or column\.$",
    ):
        px_overlay.find_subplot_axes(fig, 4, 2, secondary_y=True)


def test_no_secondary_y():
    with pytest.raises(
        IndexError,
        match=r"^Could not find a secondary y-axis at the subplot in the requested row or column\.$",
    ):
        px_overlay.find_subplot_axes(fig_no_sy, 2, 2, secondary_y=True)
    with pytest.raises(
        IndexError,
        match=r"^Could not find a y-axis at the subplot in the requested row or column\.$",
    ):
        px_overlay.find_subplot_axes(fig_custom, 2, 2, secondary_y=False)
    axes = px_overlay.find_subplot_axes(fig_custom, 1, 2, secondary_y=False)
    assert axes == ("xaxis2", "yaxis2")
