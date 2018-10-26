import pytest
import numpy as np
from functions.calculate_metrics import calc_num_beats


def test_calc_num_beats():

    # Set up test data - num_beats will be inserted into an array
    num_beats = 100
    rpeak_locs = np.zeros(1000)
    inds_one = np.random.choice(1000, num_beats, False)
    rpeak_locs[inds_one] = 1

    # Dummy metric dictionary
    metrics = {}

    # Call the function
    metrics = calc_num_beats(rpeak_locs, metrics)

    assert metrics['num_beats'] == num_beats
