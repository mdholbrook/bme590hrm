import warnings


def parse_user_inputs(user_inputs):
    """Function that parses user inputs via the command line

    Args:
        user_inputs (list): a list of inputs from the command line. The first
            index is the name of the file being run, followed by user inputs.

    Returns:
        str: parsed filename
        list: list of start and end duration of the ECG to analyse in minutes
    """

    # Get the size of the user inputs
    argc = len(user_inputs)

    # Initialize duration list
    duration = [0, 0]

    # If no file is given raise an error
    if argc == 1:

        raise Exception('Please enter the path to an input file '
                        'using the command line!')
    else:

        filename = user_inputs[1]
        warnings.warn('No durations given via the command line,'
                      ' using full duration of ECG')

    if argc == 3:  # If only one duration value is given

        warnings.warn('Two durations not given via the command line,'
                      ' using the given duration from the start of the ECG')

        duration[0] = 0
        duration[1] = float(user_inputs[2])

    if argc == 4:  # If both durations are given

        duration[0] = float(user_inputs[2])
        duration[1] = float(user_inputs[3])

    return filename, duration
