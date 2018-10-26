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

    if argc == 2:

        warnings.warn('No durations given via the command line,'
                      ' using full duration of ECG')

    elif argc == 3:  # If only one duration value is given

        warnings.warn('Two durations not given via the command line,'
                      ' using the given duration from the start of the ECG')

        # Verify that a number was entered
        if verify_numeric_inputs(user_inputs[2]):
            duration[1] = float(user_inputs[2])

        else:
            raise ValueError('Please provide the second commandline argument '
                             'as an integer or decimal number!')

    elif argc == 4:  # If both durations are given

        if verify_numeric_inputs(user_inputs[2]):
            duration[0] = float(user_inputs[2])

        else:
            raise ValueError('Please provide the second commandline argument '
                             'as an integer or decimal number!')

        if verify_numeric_inputs(user_inputs[3]):
            duration[1] = float(user_inputs[3])

        else:
            raise ValueError('Please provide the third commandline argument '
                             'as an integer or decimal number!')

    return filename, duration


def verify_numeric_inputs(input_num):
    """Verifies that the user input can be converted to a float.

    Args:
        input_num (str): string which may contain a float

    Returns:
        bool: boolean value indicating if input_num can be converted to float
    """

    try:
        float(input_num)
        return True

    except ValueError:
        return False
