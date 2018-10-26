import os
import json


def write_json(df, filename):

    # Generate save_path
    gen_outpath(save_path='output_data')

    # Generate a save filename based on the csv file
    filename = gen_save_filename(filename)

    # Write calculated metrics to a JSON file
    with open(filename, 'w') as fp:
        json.dump(df, fp)


def gen_save_filename(filename):
    """Generates the filename in which to save the results.

    The filename will be the same as the input filename. The data will be
    saved as a JSON file and placed in a directory within root called
    "output_data".

    Args:
        filename (str): path to the input csv file as given by the user.

    Returns:
        str: new filename of a JSON file to be used to save the calculated
            metrics.
    """

    # Split extension from filename
    [file_path, _] = os.path.splitext(filename)

    # Get last '/' or '\' in file
    name = file_path.split(sep='\\')

    if len(name) < 2:  # If the string was not split by '\\'

        name = file_path.split(sep='/')

    name = name[-1]

    new_filename = 'output_data/' + name + '.json'

    return new_filename


def gen_outpath(save_path):
    """Determines the existence of a folder and creates if if needed.

    Args:
        save_path (str): relative path to a folder in which to save the output.

    Returns:

    """

    save_path = os.path.abspath(save_path)

    if not os.path.exists(save_path):
        os.mkdir(save_path)
