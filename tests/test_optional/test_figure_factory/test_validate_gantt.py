import pytest

from plotly import exceptions, optional_imports
from plotly.figure_factory._gantt import validate_gantt

pd = optional_imports.get_module("pandas")


@pytest.mark.parametrize("input_type", ["list", "dataframe"])
def test_valid_with_extra_keys(input_type):
    """Test that extra keys beyond required ones are preserved."""
    data = [
        {"Task": "A", "Start": "2020-01-01", "Finish": "2020-01-02", "Resource": "X"},
        {"Task": "B", "Start": "2020-01-03", "Finish": "2020-01-04", "Resource": "Y"},
    ]
    if input_type == "dataframe":
        input_data = pd.DataFrame(data)
        result = validate_gantt(input_data)
        assert isinstance(result, list)
        assert set(result[0].keys()) == set(input_data.columns)
    else:
        input_data = data
        result = validate_gantt(input_data)
        assert result is input_data

    assert len(result) == 2
    assert all("Resource" in row for row in result)
    assert set(result[0].keys()) == set(["Task", "Start", "Finish", "Resource"])
    assert result[0]["Task"] == "A"
    assert result[1]["Finish"] == "2020-01-04"


def test_missing_required_key_in_dataframe():
    df = pd.DataFrame(
        [
            {"Task": "A", "Start": "2020-01-01"},  # Missing "Finish"
        ]
    )
    with pytest.raises(exceptions.PlotlyError):
        validate_gantt(df)


def test_empty_list():
    with pytest.raises(exceptions.PlotlyError):
        validate_gantt([])


def test_input_is_not_list_or_dataframe():
    with pytest.raises(exceptions.PlotlyError):
        validate_gantt("Not a list or DataFrame")


def test_dataframe_with_no_rows():
    df = pd.DataFrame(columns=["Task", "Start", "Finish"])
    result = validate_gantt(df)
    assert isinstance(result, list)
    assert result == []


def test_list_with_dict_missing_all_keys():
    input_data = [{"Resource": "X"}]
    # Should NOT raise: list input is not validated for keys
    result = validate_gantt(input_data)
    assert result is input_data


def test_large_list_with_non_dict_first_element():
    input_data = [
        "Not a dict",
        *[
            {
                "Task": f"Task{i}",
                "Start": f"2020-01-{i % 30 + 1:02d}",
                "Finish": f"2020-02-{i % 28 + 1:02d}",
            }
            for i in range(999)
        ],
    ]
    with pytest.raises(exceptions.PlotlyError):
        validate_gantt(input_data)


def test_dataframe_column_order_and_index():
    df = pd.DataFrame(
        [
            {"Finish": "2023-01-02", "Start": "2023-01-01", "Task": "A"},
            {"Finish": "2023-01-03", "Start": "2023-01-02", "Task": "B"},
        ],
        index=["x", "y"],
    )
    result = validate_gantt(df)
    assert len(result) == 2
    # Ensure values preserved regardless of order/index
    assert result[0]["Task"] == "A"
    assert set(result[0].keys()) == set(["Task", "Start", "Finish"])
