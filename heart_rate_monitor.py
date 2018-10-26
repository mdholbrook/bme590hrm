from functions.load_data import read_csv, interpolate_nan
from functions.process_ecg import filter_ecg, r_peak_detection
from functions.process_ecg import normalize_ecg, calculate_metrics
from functions.write_results import write_results_to_file


def main(file):

    # Read in data
    data = read_csv(file)

    # Clean input data
    data = interpolate_nan(data)

    # Filter ECG signal
    data_filt = filter_ecg(data)

    # Normalize ECG
    data_filt = normalize_ecg(data_filt)

    # R-peak detection
    rpeak_locs = r_peak_detection(data_filt)

    # Calculate metrics
    metrics = calculate_metrics(data, data_filt, rpeak_locs)

    # Write results
    write_results_to_file(metrics, file)


if __name__ == "__main__":

    filename = 'test_data/test_data1.csv'
    main(filename)
