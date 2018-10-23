import numpy as np
import pytest
from functions.load_data import read_csv, clean_data


def test_read_csv():
    # Set up correct array
    correct_array = np.array([[0, 2.1], [0.1, 0.1], [0.2, -0.9], [0.3, 0]])

    # Run read_csv function
    data = read_csv('data/csv_test.csv')
    print(data)

    assert (data == correct_array).all()


def clean_data(data):

    cleaned_df = np.zeros(1)

    return cleaned_df
