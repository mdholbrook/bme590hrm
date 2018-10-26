import numpy as np
from functions.process_ecg import calc_duration


def calculate_metrics(data, data_filt, rpeak_locs, duration):

    metrics = {}

    # Calculate voltage extremes
    metrics = calc_voltage_extremes(data, metrics)

    # Calculate duration
    metrics = calc_duration(data, metrics)

    # Calculate number of beads in a strip
    metrics = calc_num_beats(rpeak_locs, metrics)

    # Calculate time when beats occur
    metrics = calc_beats(data_filt, rpeak_locs, metrics)

    # Calculate mean heart rate
    metrics = calc_mean_hr_bpm(duration, metrics)

    return metrics


def calc_mean_hr_bpm(duration, metrics):
    """Calculate the heart rate within an interval

    The user inputs an interval in minutes via the command line. The average
    heart rate is calculated within this interval.

    Args:
        duration (tubple): contains the start and stop times that the user
            wants heart rate information for.
        metrics (dictionary): a dictionary of calculated metrics from the
            input ECG.

    Returns:
        dictionary: A dictionary field containing a float of the average
            beats per minute over the specified interval.
    """

    # Get duration indices specified by the user
    start_ind = metrics['beats'] >= duration[0]
    end_ind = metrics['beats'] >= duration[1]

    # Get list of times for each beat, in seconds, during the interval
    beats = metrics['beats'][start_ind:end_ind]
    bpm = np.mean(beats[1:] - beats[:-1]) * 60  # [beats per min]

    # Assign bpm to the dictionary
    metrics['mean_hr_bme'] = bpm

    return metrics


def calc_voltage_extremes(data, metrics):
    """Calculates the extremes of the input ECG.

    Args:
        data (2D numpy array): contains time and voltage information from the
            input ECG. This data is input pre-filtering so the input range is
            not altered.
        metrics (dictionary): contains calculated ECG metrics

    Returns:
        tuple, float: the minimum and maximum voltages recorded during
            the monitoring period under a dictionary label 'voltage_extremes'.
    """

    # Get ECG voltage
    volts = data[:, 1]

    # Calculate voltage extremes and place into a list
    volts_extremes = (volts.min(), volts.max())

    # Update the dictionary
    metrics['voltage_extremes'] = volts_extremes

    return metrics


def calc_num_beats(rpeak_locs, metrics):
    """Calculates the number of beats in an ECG

    This function takes an array of the ECG R-peaks. The number of R-peaks
    is equivalent to the number of beats in the ECG.

    Args:
        rpeak_locs (1D numpy array): index locations of R-peaks in an ECG.
        metrics (dictionary): dictionary containing the metrics which will be
            returned at the end of the program.

    Returns:
        int: dictionary with added field for the number of beats
    """

    # Add the number of beats
    num_beats = np.sum(rpeak_locs, dtype=int)
    metrics['num_beats'] = num_beats

    return metrics


def calc_beats(data, rpeak_locs, metrics):
    """Returns the times when R-peaks occur

    Args:
        data (2D numpy array): contains two columns with time and ECG data
        rpeak_locs (1D numpy array): contains locations of R-peaks
        metrics (dictionary): dictionary containing the metrics calculated
            by this program.

    Returns:
        numpy array: dictionary with added field for heart beat times
    """

    time = data[:, 0]
    beat_time = time[rpeak_locs]

    metrics['beats'] = beat_time

    return metrics
