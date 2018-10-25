import pytest
from functions.process_ecg import filter_ecg, high_pass_filter, low_pass_filter
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
    sig_filt = low_pass_filter(signal)

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
    sig_filt = low_pass_filter(signal)

    # Get new measure of drift error from zero
    drift_error_filt = np.sum(sig_filt**2)

    # Verify that variance decreases after filtration
    assert drift_error_filt < drift_error
