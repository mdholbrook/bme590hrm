import pytest
from functions.process_ecg import filter_ecg, high_pass_filter, low_pass_filter
from functions.process_ecg import normalize_ecg, nonmax_supression, load_rpeak
from functions.process_ecg import r_peak_detection
import numpy as np


def test_filter_ecg():

    # Set up test signal with noise and drift
    np.random.seed(42)
    drift = np.linspace(0, 2, 1000)
    signal = np.random.randn(1000) + drift

    # Monitor error due to signal drift
    drift_error = np.sum(signal**2)

    # Monitor variance of the signal
    signal_var = signal.var()

    # Filter signal
    data = np.zeros((1000, 2))
    data[:, 1] = signal
    sig_filt = filter_ecg(data)
    sig_filt = sig_filt[:, 1]

    # Get new measure of drift error from zero
    drift_error_filt = np.sum(sig_filt**2)

    # Get measure of variation
    sig_filt_var = sig_filt.var()

    # Verify that variance decreases after filtration
    assert sig_filt_var < signal_var

    # Verify that variance decreases after filtration
    assert drift_error_filt < drift_error


def test_low_pass_filter():

    # Set up test signal with noise and drift
    np.random.seed(42)
    signal = np.random.randn(1000) + np.linspace(0, 2, 1000)

    # Monitor variance of the signal
    signal_var = signal.var()

    # Filter signal
    sig_filt = low_pass_filter(signal)

    # Get measure of variation
    sig_filt_var = sig_filt.var()

    # Verify that variance decreases after filtration
    assert sig_filt_var < signal_var


def test_high_pass_filter():

    # Set up test signal with noise and drift
    np.random.seed(42)
    drift = np.linspace(0, 2, 1000)
    signal = np.random.randn(1000) + drift

    # Monitor error due to signal drift
    drift_error = np.sum(signal**2)

    # Filter signal
    sig_filt = high_pass_filter(signal)

    # Get new measure of drift error from zero
    drift_error_filt = np.sum(sig_filt**2)

    # Verify that variance decreases after filtration
    assert drift_error_filt < drift_error


def test_normalize_ecg():

    # Set up test data - max of 5
    data = np.zeros((1000, 2))
    data[:, 0] = np.linspace(0, 30, 1000)
    data[:500, 1] = 5*np.ones(500)

    # Expected data - max of 1
    expected = np.zeros((1000, 2))
    expected[:, 0] = np.linspace(0, 30, 1000)
    expected[:500, 1] = np.ones(500)

    # Run normalization
    result = normalize_ecg(data)

    assert (result == expected).all()


def test_nonmax_supression():

    # Set up test data
    x = np.array([0, 1.2, 3.3, 2.1, 5.6, 6.0, 4.2, 1.1])
    expected = np.array([False, False, True, False, False, True, False])
    expected = np.where(expected)[0]

    # Test function
    result = nonmax_supression(x)

    assert (result == expected).all()


def test_load_rpeak():
    import pickle as p

    # Load test data
    f = open('functions/rpeak.p', 'rb')
    expected = p.load(f)
    f.close()

    # Test function
    result = load_rpeak()

    assert (result == expected).all()


def test_rpeak_detection():
    import pickle as p

    # Load test data
    f = open('functions/rpeak.p', 'rb')
    expected = p.load(f)
    f.close()

    # Get test peak
    expected_loc = np.where(expected == expected.max())[0]

    # Set up data for function
    data = np.zeros((len(expected), 2))
    data[:, 0] = np.linspace(1, 2, len(expected))
    data[:, 1] = expected

    # Run peak detection
    result_loc = r_peak_detection(data)

    assert result_loc == expected_loc
