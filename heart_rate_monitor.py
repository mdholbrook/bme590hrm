import sys
from functions.load_data import read_csv, interpolate_nan
from functions.process_ecg import filter_ecg, r_peak_detection
from functions.process_ecg import normalize_ecg
from functions.calculate_metrics import calculate_metrics
from functions.write_results import write_results_to_file
from functions.user_inputs import parse_user_inputs


def main(user_input):
    """Main function which calls all helper functions
    This is the main function for the heart rate monitoring code

    Args:
        user_input (list): a list of commandline arguments as passed in
            using sys.argv()

    Returns:

    """

    # Parse user inputs
    filename, duration = parse_user_inputs(user_input)

    # Read in data
    data = read_csv(filename)

    # Clean input data
    data = interpolate_nan(data)

    # Filter ECG signal
    data_filt = filter_ecg(data)

    # Normalize ECG
    data_filt = normalize_ecg(data_filt)

    # R-peak detection
    rpeak_locs = r_peak_detection(data_filt)

    # Calculate metrics
    metrics = calculate_metrics(data, data_filt, rpeak_locs, duration)

    # Write results
    write_results_to_file(metrics, filename)


if __name__ == "__main__":

    cmdline_args = sys.argv

    main(cmdline_args)
