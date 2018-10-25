import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def filter_ecg(data):
    """Filter the input ECG using a bandpass

    Sequential high and low-pass filters create a bandpass effect. The
    resulting signal will be centered on zero (resting potential).

    Args:
        data (2D numpy array): contains two columns with time and ECG data

    Returns:
        data (2D numpy array): modified array with now-filtered ECG data
    """

    volts = data[:, 1]

    # Remove low frequency drift
    volt_filt = high_pass_filter(volts)

    # Remove very high frequency information
    volt_filt = low_pass_filter(volt_filt)

    # Replace the old voltage information in the numpy array
    data[:, 1] = volt_filt

    return volt_filt


def low_pass_filter(volts, sigma=2, kernel_size=7):
    """Low pass filter function to filter ECG

    Args:
        volts (1D numpy array): voltage measurements of ECG
        sigma (int): parameter describing the frequency of the filter
        kernel_size (int): size of the Gaussian kernel

    Returns:
        volt_filt (1D numpy array): low pass filtered ECG signal
    """

    # Create Gaussian LP kernel
    sigma = 2
    kernel_size = 9
    kernel = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (np.arange(
        -kernel_size//2 + 1, kernel_size//2 + 1, 1)/sigma)**2)

    # Filter the signal
    volt_filt = signal.convolve(volts, kernel, mode='same')

    return volt_filt


def high_pass_filter(volts, kernel_size=401):
    """High pass filtered the ECG signal

    Median filtration will preserve the signal mean around the resting signal.

    Args:
        volts (1D numpy array): voltage measurements of ECG
        kernel_size (int): size of the median filter

    Returns:
        volt_filt (1D numpy array): low pass filtered ECG signal
    """

    # Get low frequency signal
    volt_lp = signal.medfilt(volts, kernel_size=kernel_size)

    # Subtract low frequency signal to get high frequencies
    volt_filt = volts - volt_lp

    return volt_filt


def normalize_ecg(data):
    """This function normalizes the ECG signal.

    This function scales the signal into a standard range, with R-peaks being
    brought near 1.

    Args:
        data (2D numpy array):

    Returns:

    """

    return data


def r_peak_detection(df):

    inds = np.zeros(1)
    df['r_peak_inds'] = inds

    return df


def calculate_metrics(df):

    metrics = {}

    # Calculate mean heart rate
    metrics = calc_mean_hr_bpm(df, metrics)

    # Calculate voltage extremes
    metrics = calc_voltage_extremes(df, metrics)

    # Calculate duration
    metrics = calc_duration(df, metrics)

    # Calculate number of beads in a strip
    metrics = calc_num_beats(df, metrics)

    # Calculate time when beats occur
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
