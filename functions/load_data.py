import os
import numpy as np
from numpy import genfromtxt


def read_csv(filename):
    """Definition of read_csv

    This function takes a filename and reads in a file and outputs its
    contents. The file should be in csv format and have 2 columns representing
    time and voltage measurements.

    Args:
        filename (str): path to a csv file containing ECG data

    Returns:
        numpy array: numpy array containing two columns, time and ECG
        voltage
    """

    # Verify the existence of the file
    verify = os.path.exists(filename)
    if not verify:
        raise IOError('The input file given does not exist!')

    # Verify that the input file is a csv
    verify = verify_csv_extension(filename)
    if not verify:
        raise ValueError('Please input a valid .csv file!')

    # Read from csv file
    data = genfromtxt(filename, dtype='float', delimiter=',', autostrip=True)

    return data


def verify_csv_extension(file):
    """Verifies that the extension of the file passed to read_csv denotes a
    csv file

    Args:
        string (str): path to input file

    Returns:
        bool: returns if the input file is a .csv file

    """
    # Get extension
    _, file_extension = os.path.splitext(file)

    # Return false if not a csv extension
    if not file_extension == '.csv':
        return False

    return True


def interpolate_nan(data):
    """Interpolates NaN values in the the ECG

    Data passed in may contain NaN values where there were strings or blank
    spaces in the data, causing gaps in the data. This script interpolates
    over those gaps.

    Args:
        data (np array): a numpy array containing time, first col, and
            ECG, second col, signals

    Returns:
        1D numpy array, float: numpy array with interpolated NaN values
    """

    # Find and interpolate over NaN values, time then ECG
    for i in range(2):
        if np.isnan(data[:, i]).any():

            # Find NaN values
            nans = nan_inds(data[:, i])
            func = non_zero_func

            # Interpolate over NaN values
            data[nans, i] = np.interp(func(nans), func(~nans), data[~nans, i])

    return data


def nan_inds(x):
    """Function to handle indices and logical indices of NaNs.

    Args
        x (1D numpy array): a vector (time or ECG) containing NaN values

    Returns:
        1D numpy array, bool: array where True denotes a NaN value
        func (function): a function which return on all non-zero values, used
        to index the interpolation

    """

    nans = np.isnan(x)

    return nans


def non_zero_func(x):
    """Function which returns non-zero indices of an array

    Args:
        x (1d numpy array): input array

    Returns:
        inds (1d numpy array): output non-zero indicies
    """

    inds = x.nonzero()[0]

    return inds
