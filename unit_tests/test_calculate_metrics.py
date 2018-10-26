import pytest
import numpy as np
from functions.calculate_metrics import calc_num_beats, calc_beats
from functions.calculate_metrics import calc_voltage_extremes


def test_calc_num_beats():

    # Set up test data - num_beats will be inserted into an array
    num_beats = int(100)
    rpeak_locs = np.zeros(1000)
    inds_one = np.random.choice(1000, num_beats, False)
    rpeak_locs[inds_one] = 1

    # Dummy metric dictionary
    metrics = {}

    # Call the function
    metrics = calc_num_beats(rpeak_locs, metrics)

    assert metrics['num_beats'] == num_beats


def test_calc_beats():

    # Set up test data
    time = np.arange(0, 10, 0.1)
    locs = np.random.choice(100, 10, replace=False)
    times = time[locs]

    # Set up data array and metrics dictionary
    data = np.zeros((100, 2))
    data[:, 0] = time
    metrics = {}

    # Run the function
    metrics = calc_beats(data, rpeak_locs=locs, metrics=metrics)

    assert (metrics['beats'] == times).all()


def test_calc_voltage_extremes():

    # Set up test data
    data = np.array([[0, 1, 2, 3, 4, 5], [-1, -1.1, 0.9, 2.2, 0.2, -0.1]]).T

    # Run the function
    metrics = {}
    metrics = calc_voltage_extremes(data, metrics)

    assert (metrics['voltage_extremes'] == (-1.1, 2.2))
