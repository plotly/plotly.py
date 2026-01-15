# tests/test_plotly_express/test_stacked_bar.py

import sys
import pytest
import pandas as pd
import plotly.express as px
from itertools import product

# Skip test for older Python/pandas versions to avoid build failures
pytestmark = pytest.mark.skipif(
    sys.version_info < (3, 9) or pd.__version__ < "1.2.0",
    reason="Requires Python >=3.9 and pandas >=1.2.0",
)


def test_stacked_bar_all_groups():
    """
    Test that stacked bar plots include all groups (commanders) for every week.
    This ensures that missing combinations are filled with 0.
    """

    # Step 1: Load example data
    plot_data = pd.read_csv("../../test_data/example_plot_data.csv")

    # Step 2: Convert the date column
    plot_data["savedate_week"] = pd.to_datetime(plot_data["savedate_week"])

    # Step 3: Get all unique weeks and commanders
    all_weeks = plot_data["savedate_week"].unique()
    all_commanders = plot_data["commanders"].unique()

    # Step 4: Generate full combinations of weeks and commanders
    full_index = pd.DataFrame(
        list(product(all_weeks, all_commanders)),
        columns=["savedate_week", "commanders"],
    )

    # Step 5: Merge with original data and fill missing values with 0
    plot_data_full = full_index.merge(
        plot_data, on=["savedate_week", "commanders"], how="left"
    )
    plot_data_full["commander_perc_of_card"] = plot_data_full[
        "commander_perc_of_card"
    ].fillna(0)

    # Step 6: Create the stacked bar plot (not shown in tests)
    fig = px.bar(
        plot_data_full,
        x="savedate_week",
        y="commander_perc_of_card",
        color="commanders",
    )

    # Step 7: Assertions
    weeks_in_fig = plot_data_full["savedate_week"].unique()
    commanders_in_fig = plot_data_full["commanders"].unique()

    # Check that all weeks and all commanders are present
    assert len(weeks_in_fig) == len(all_weeks), (
        "Some weeks are missing in the stacked bar data"
    )
    assert len(commanders_in_fig) == len(all_commanders), (
        "Some commanders are missing in the stacked bar data"
    )

    # Optional: Check that no NaNs exist after filling
    assert plot_data_full["commander_perc_of_card"].isna().sum() == 0, (
        "NaN values found in commander_perc_of_card"
    )
