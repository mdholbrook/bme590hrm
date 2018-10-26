import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pickle as p


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

    return data


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
        data (2D numpy array): contains two columns with time and ECG data

    Returns:

    """

    # Get run duration
    df = {}
    df = calc_duration(data, df)
    duration = df['duration']

    # Get the number of beats to use for normalization measurement
    num_beats_per_second = 1.0
    beats = int(num_beats_per_second * duration)

    # Find max values for each beat
    volts = data[:, 1]
    max_inds = np.argpartition(volts, -beats)[-beats:]
    max_values = volts[max_inds]

    # Get median peak value and normalize
    norm_val = np.median(max_values)

    # Normalize ECG
    volts_norm = volts / norm_val

    # Recreate data
    data[:, 1] = volts_norm

    return data


def r_peak_detection(data):
    """Detection of R-peaks in an ECG signal

    This function loads a sample QRS complex and computes a corrlation on an
    input ECG signal. Areas of high correction are found via thresholding and
    nonmaximum suppression is used to detect maxima (R-peak locations).

    Args:
        2D numpy array: array with two columns columns containing time and ECG
            data

    Returns:

    """

    # Get ECG signal
    volts = data[:, 1]

    # Load sample QRS structure
    rpeak = load_rpeak()

    # Correlate the QRS cycle with the ECG
    cor = signal.correlate(volts, rpeak, mode='same')
    cor = np.roll(cor, 2)

    # Normalize cor by the max correlation
    cor /= np.abs(rpeak).sum()

    # Threshold the correlation
    threshold = 0.35
    tcor = np.zeros_like(cor)
    tcor[cor > threshold] = cor[cor > threshold]

    # Non-maximum suppression for peak detection
    max_locs = nonmax_supression(tcor)

    return max_locs


def nonmax_supression(x):
    """Nonmaximum suppression finds crests of a signal.
    All other non-maxima found from thresholding are suppressed.

    Args:
        x (1D numpy array): a thresholded signal

    Returns:
        floats, 1D numpy array: an array of maxima indexes
    """

    # Get a list of indices which can shift the vector
    inds = np.arange(1, len(x)-1, 1)

    # Compare to the right and left of each point
    compareL = (x[1:-1] - x[inds-1]) > 0
    compareR = (x[1:-1] - x[inds+1]) > 0
    compare = compareL * compareR

    # Compute max indexes
    max_inds = np.zeros(len(x), dtype=bool)
    max_inds[1:-1] = compare

    # Convert max_inds to a list of locations
    max_locs = np.where(max_inds)[0]

    return max_locs


def load_rpeak():
    """Loads a sample R-peak for beat detection

    Returns:
        floats, 1D numpy array: sample waveform, normalized to 1
    """

    # Load sample R-peak
    f = open('functions/rpeak.p', 'rb')
    rpeak = p.load(f)
    f.close()

    return rpeak


def calc_duration(data, metrics):
    """Calculate the duration of the ECG strip

    Args:
        data (2D numpy array): contains two columns with time and ECG data
        metrics (float): dictionary containing ECG metrics


    Returns:
        float, seconds: dictionary with 'duration' field containing an float in seconds
    """

    # Get test duration
    time = data[:, 0]
    duration = time[-1] - time[0]

    metrics['duration'] = duration

    return metrics
