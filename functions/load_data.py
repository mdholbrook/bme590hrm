import numpy as np
from numpy import genfromtxt


def read_csv(file):

    df = genfromtxt(file, dtype='float', delimiter=',')

    return df


def clean_data(df):

    cleaned_df = np.zeros(1)

    return cleaned_df
