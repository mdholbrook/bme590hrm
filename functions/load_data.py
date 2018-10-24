import os
import numpy as np
from numpy import genfromtxt


def read_csv(file):
    """Definition of read_csv

    This function takes a filename and reads in a file and outputs its
    contents. The file should be in csv format and have 2 columns representing
    time and voltage measurements.

    Args:
        file: path to a csv file containing ECG data

    Returns:
        data: numpy array containing two columns, time and ECG voltage
    """

    # Verify that the input file is a csv
    verify = verify_csv_extension(file)
    if not verify:
        raise ValueError('Please input a valid .csv file')

    # Read from csv file
    data = genfromtxt(file, dtype='float', delimiter=',', autostrip=True)

    return data


def verify_csv_extension(file):
    """Verifies that the extension of the file passed to read_csv denotes a
    csv file

    Args:
        file: path to input file

    Returns:

    """
    # Get extension
    _, file_extension = os.path.splitext(file)

    # Return false if not a csv extension
    if not file_extension == '.csv':
        return False

    return True


def interpolate_nan(df):

    cleaned_df = np.zeros(1)

    return cleaned_df
