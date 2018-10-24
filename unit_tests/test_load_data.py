import numpy as np
import pytest
from functions.load_data import read_csv, verify_csv_extension, interpolate_nan
from functions.load_data import nan_inds, non_zero_func


@pytest.mark.parametrize("candidate, expected", [
    ("unit_tests/data/csv_test.csv",
     np.array([[0, 2.1], [0.1, 0.1], [0.2, -0.9], [0.3, 0]])),
    ("unit_tests/data/string.csv", np.array([[(2.2, np.nan), (np.nan, 3.1)]])),
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
    ("unit_tests/data/csv_test.csv", True),
    ("unit_tests/data/string.xlsx", False),
    ])
def test_verify_csv_extension(candidate, expected):

    # Run verity_csv_extension
    result = verify_csv_extension(candidate)

    assert result == expected


def test_interpolate_nan():

    candidate = np.array([[1, 1, 1, np.nan, np.nan, 2, 2, np.nan, 0],
                          [0, 1, np.nan, 3, 4, 5, np.nan, 7, 8]]).T
    expected = np.array([[1, 1, 1, 1.33333333, 1.66666667, 2, 2, 1, 0],
                         [0, 1, 2, 3, 4, 5, 6, 7, 8]]).T

    # Run interpolate_nan
    result = interpolate_nan(candidate)

    # Approximate comparison
    compare = result == pytest.approx(expected)

    assert not np.isnan(result).any()
    assert compare


def test_nan_inds():

    x = np.array([0, 1, 2, 3, np.nan, np.nan, 6, np.nan, 8, 9])
    y = np.array([False, False, False, False, True, True, False, True, False,
                  False])

    inds = nan_inds(x)

    assert (inds == y).all()


def test_non_zero_func():

    x = np.array([0, 1, 2, 0, 6.1, 0])
    y = np.array([1, 2, 4])

    nzero = non_zero_func(x)

    assert (y == nzero).all()
