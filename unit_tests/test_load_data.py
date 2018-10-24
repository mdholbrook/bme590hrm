import numpy as np
import pytest
from functions.load_data import read_csv, verify_csv_extension, clean_data


@pytest.mark.parametrize("candidate, expected", [
    ("data/csv_test.csv", np.array([[0, 2.1], [0.1, 0.1], [0.2, -0.9], [0.3, 0]])),
    ("data/string.csv", np.array([[(2.2, np.nan), (np.nan, 3.1)]])),
    ])
def test_read_csv(candidate, expected):

    # Run read_csv function
    data = read_csv(candidate)

    # Compare functions
    if np.isnan(expected).any():  # if there are strings or missing data
        data = data.reshape(-1)
        expected = expected.reshape(-1)
        temp = (data == expected) | (np.isnan(data) == np.isnan(expected))
        comparison = temp.all()

    else:   # if there is not missing data
        comparison = (data == expected).all()

    assert comparison


@pytest.mark.parametrize("candidate, expected", [
    ("data/csv_test.csv", True),
    ("data/string.xlsx", False),
    ])
def test_verify_csv_extension(candidate, expected):

    # Run verity_csv_extension
    result = verify_csv_extension(candidate)

    assert result == expected


# def test_clean_data(data):
#
#     cleaned_df = np.zeros(1)
#
#     return cleaned_df
