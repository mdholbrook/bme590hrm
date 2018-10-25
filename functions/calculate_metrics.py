import numpy as np


def calculate_metrics(data, data_filt, rpeak_locs):

    metrics = {}

    # Calculate mean heart rate
    # metrics = calc_mean_hr_bpm(df, metrics)

    # Calculate voltage extremes
    # metrics = calc_voltage_extremes(df, metrics)

    # Calculate duration
    # metrics = calc_duration(df, metrics)

    # Calculate number of beads in a strip
    metrics = calc_num_beats(rpeak_locs, metrics)

    # Calculate time when beats occur
    # metrics = calc_beats(df, metrics)

    return metrics


def calc_mean_hr_bpm(df, metrics):

    metrics['mean_hr_bme'] = np.zeros(1)

    return metrics


def calc_voltage_extremes(df, metrics):

    metrics['voltage_extremes'] = np.zeros(1)

    return metrics


def calc_duration(data, metrics):

    # Get test duration
    time = data[:, 0]
    duration = time[-1] - time[0]

    metrics['duration'] = duration

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
        metrics: dictionary with added field for the number of beats
    """

    # Add the number of beats
    num_beats = np.sum(rpeak_locs)
    metrics['num_beats'] = num_beats

    return metrics


def calc_beats(data, metrics):


    metrics['beats'] = np.zeros(1)

    return metrics
