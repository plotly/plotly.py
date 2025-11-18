import pytest

from plotly import exceptions, optional_imports
from plotly.figure_factory._gantt import validate_gantt

pd = optional_imports.get_module("pandas")
REQUIRED_GANTT_KEYS = ["Task", "Start", "Finish"]


# --- BASIC TEST CASES ---


def test_valid_list_of_dicts():
    input_data = [
        {"Task": "A", "Start": "2020-01-01", "Finish": "2020-01-02"},
        {"Task": "B", "Start": "2020-01-03", "Finish": "2020-01-04"},
    ]

    result = validate_gantt(input_data)
    assert result is input_data
    assert len(result) == 2
    assert all(isinstance(x, dict) for x in result)


def test_valid_dataframe():
    df = pd.DataFrame(
        [
            {"Task": "A", "Start": "2020-01-01", "Finish": "2020-01-02"},
            {"Task": "B", "Start": "2020-01-03", "Finish": "2020-01-04"},
        ]
    )
    result = validate_gantt(df)
    assert isinstance(result, list)
    assert len(result) == 2
    assert set(result[0].keys()) == set(df.columns)
    assert result[0]["Task"] == "A"
    assert result[1]["Finish"] == "2020-01-04"


def test_valid_list_with_extra_keys():
    input_data = [
        {"Task": "A", "Start": "2020-01-01", "Finish": "2020-01-02", "Resource": "X"},
        {"Task": "B", "Start": "2020-01-03", "Finish": "2020-01-04", "Resource": "Y"},
    ]
    result = validate_gantt(input_data)
    assert result is input_data
    assert all("Resource" in row for row in result)


def test_valid_dataframe_with_extra_keys():
    df = pd.DataFrame(
        [
            {
                "Task": "A",
                "Start": "2020-01-01",
                "Finish": "2020-01-02",
                "Resource": "X",
            },
            {
                "Task": "B",
                "Start": "2020-01-03",
                "Finish": "2020-01-04",
                "Resource": "Y",
            },
        ]
    )
    result = validate_gantt(df)
    assert len(result) == 2
    assert set(result[0].keys()) == set(["Task", "Start", "Finish", "Resource"])


# --- EDGE TEST CASES ---


def test_missing_required_key_in_list():
    input_data = [
        {"Task": "A", "Start": "2020-01-01"},  # Missing "Finish"
    ]
    # Should NOT raise: list input is not validated for keys
    result = validate_gantt(input_data)
    assert result is input_data


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


def test_dataframe_with_extra_rows_and_missing_keys():
    df = pd.DataFrame(
        [
            {"Task": "A", "Start": "2020-01-01", "Resource": "X"},
            {"Task": "B", "Start": "2020-01-03", "Resource": "Y"},
        ]
    )
    with pytest.raises(exceptions.PlotlyError):
        validate_gantt(df)


def test_list_with_dict_missing_all_keys():
    input_data = [{"Resource": "X"}]
    # Should NOT raise: list input is not validated for keys
    result = validate_gantt(input_data)
    assert result is input_data


def test_dataframe_with_only_required_keys():
    df = pd.DataFrame(
        [
            {"Task": "A", "Start": "2020-01-01", "Finish": "2020-01-02"},
        ]
    )
    result = validate_gantt(df)
    assert len(result) == 1
    assert set(result[0].keys()) == set(REQUIRED_GANTT_KEYS)


# --- LARGE SCALE TEST CASES ---


def test_large_list_of_dicts():
    input_data = [
        {
            "Task": f"Task{i}",
            "Start": f"2020-01-{i % 30 + 1:02d}",
            "Finish": f"2020-02-{i % 28 + 1:02d}",
        }
        for i in range(1000)
    ]
    result = validate_gantt(input_data)
    assert result is input_data
    assert len(result) == 1000


def test_large_dataframe():
    df = pd.DataFrame(
        [
            {
                "Task": f"Task{i}",
                "Start": f"2020-01-{i % 30 + 1:02d}",
                "Finish": f"2020-02-{i % 28 + 1:02d}",
            }
            for i in range(1000)
        ]
    )
    result = validate_gantt(df)
    assert isinstance(result, list)
    assert len(result) == 1000
    assert set(result[0].keys()) == set(df.columns)


def test_large_dataframe_missing_key():
    df = pd.DataFrame(
        [
            {
                "Task": f"Task{i}",
                "Start": f"2020-01-{i % 30 + 1:02d}",
            }  # Missing "Finish"
            for i in range(1000)
        ]
    )
    with pytest.raises(exceptions.PlotlyError):
        validate_gantt(df)


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


def test_large_list_with_non_dict_later_element():
    input_data = [
        *[
            {
                "Task": f"Task{i}",
                "Start": f"2020-01-{i % 30 + 1:02d}",
                "Finish": f"2020-02-{i % 28 + 1:02d}",
            }
            for i in range(999)
        ],
        "Not a dict",
    ]
    # Should NOT raise: only first element is checked
    result = validate_gantt(input_data)
    assert result is input_data
    assert len(result) == 1000


# --- Additional determinism/robustness checks ---


def test_determinism_multiple_calls_list():
    input_data = [
        {"Task": "A", "Start": "2023-01-01", "Finish": "2023-01-02"},
        {"Task": "B", "Start": "2023-01-02", "Finish": "2023-01-03"},
    ]
    out1 = validate_gantt(input_data)
    out2 = validate_gantt(input_data)
    assert out1 is input_data
    assert out2 is input_data


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
