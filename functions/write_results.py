import os
import json


def write_results_to_file(metrics, filename):
    """Writes the calculated metrics in a JSON file.

    This function takes the metrics and filename of the input csv file. It
    generates an output folder and makes a new file in that folder named after
    the input csv file. The metrics calculated in the previous parts of the
    code are written to this file.

    Args:
        metrics (dict: a dictionary containing all of the metrics calculated by
            this program on the ECG.
        filename (str): name of the input csv file.

    Returns:

    """

    # Generate save_path
    save_path = 'output_data'
    gen_outpath(save_path)

    # Generate a save filename based on the csv file
    filename = gen_save_filename(filename, save_path)

    # Write calculated metrics to a JSON file
    write_json(metrics, filename)


def gen_save_filename(filename, save_path):
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

    new_filename = save_path + '/' + name + '.json'

    return new_filename


def gen_outpath(save_path):
    """Determines the existence of a folder and creates if if needed.

    Args:
        save_path (str): relative path to a folder in which to save the output.

    Returns:
        bool: value indicating if the output folder was successfully created.
    """

    # Strip leading slashes
    save_path = save_path.strip('/')
    save_path = save_path.strip('\\')

    # Generate absolute path
    save_path = os.path.abspath(save_path)

    if not os.path.exists(save_path):
        try:
            os.mkdir(save_path)
        except Exception:
            raise FileNotFoundError('Cannot make the '
                                    'directory:\n\t%s' % save_path)
            print('Please ensure base directory exists')


def write_json(metrics, filename):
    """Function writes metrics to a JSON file.

    Args:
        metrics (dict): dictionary containing calculated metrics for the ECG.
        filename (str): filename, including path, of the JSON file to be
            written.

    Returns:

    """

    # Write calculated metrics to a JSON file
    try:
        with open(filename, 'w') as fp:
            json.dump(metrics, fp)

        print('Output file written to:\n\t%s' % filename)

    except FileNotFoundError:
        raise FileNotFoundError('Cannot access output JSON file for writing!')
