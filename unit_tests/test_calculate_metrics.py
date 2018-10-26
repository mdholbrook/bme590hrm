import pytest
import numpy as np
from functions.calculate_metrics import calc_num_beats, calc_beats
from functions.calculate_metrics import calc_voltage_extremes
from functions.calculate_metrics import check_input_duration
from functions.calculate_metrics import calc_mean_hr_bpm


def test_calc_num_beats():

    # Set up test data - num_beats will be inserted into an array
    num_beats = int(100)
    rpeak_locs = np.random.choice(1000, num_beats)

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


@pytest.mark.parametrize("duration, expected", [
    ((3, 6), False),
    ((0, 2), True),
    ((0, 5), False)
    ])
def test_check_input_duration(duration, expected):

    # Set up data
    metrics = {}
    metrics['duration'] = 140

    # Run the function
    try:
        output = check_input_duration(duration, metrics)
    except ValueError:
        output = False

    assert output == expected


def test_calc_mean_hr_bpm():

    # Set up test data
    duration = (1, 2)  # [min]
    beats_per_second = 1.2
    metrics = {}
    metrics['beats'] = np.arange(0, 180, beats_per_second)  # [sec]
    bpm = 60 / beats_per_second

    # Call the function
    metrics = calc_mean_hr_bpm(duration, metrics)

    assert metrics['mean_hr_bpm'] == bpm
