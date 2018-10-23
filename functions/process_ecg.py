import numpy as np

def filter_ecg(df):

    volt_filt = np.zeros()
    df['voltage'] = volt_filt
    return df


def r_peak_detection(df):

    inds = np.zeros()
    df['r_peak_inds'] = inds

    return df


def calculate_metrics(df):

    metrics = {}

    # Calculate mean heart rate
    metrics = calc_mean_hr_bpm(df, metrics)

    # Calculate voltage extremems
    metrics = calc_voltage_extremes(df, metrics)

    # Calculate duration
    metrics = calc_duration(df, metrics)

    # Calculate number of beads in a strip
    metrics = calc_num_beats(df, metrics)

    # Calculate time when beats occured
    metrics = calc_beats(df, metrics)

    return metrics


def calc_mean_hr_bpm(df, metrics):

    metrics['mean_hr_bme'] = np.zeros(1)

    return metrics


def calc_voltage_extremes(df, metrics):

    metrics['voltage_extremes'] = np.zeros(1)

    return metrics


def calc_duration(df, metrics):

    metrics['duration'] = np.zeros(1)

    return metrics


def calc_num_beats(df, metrics):

    metrics['num_beats'] = np.zeros(1)

    return metrics


def calc_beats(df, metrics):

    metrics['beats'] = np.zeros(1)

    return metrics


