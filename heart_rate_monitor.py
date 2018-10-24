from functions.load_data import read_csv, interpolate_nan
from functions.process_ecg import filter_ecg, r_peak_detection, \
    calculate_metrics
from functions.write_results import write_json


def main(file):

    # Read in data
    data = read_csv(file)

    # Clean input data
    data = interpolate_nan(data)

    # Filter ECG signal
    # df = filter_ecg(df)

    # R-peak detection
    # df = r_peak_detection(df)

    # Calculate metrics
    # metrics = calculate_metrics(df)

    # Write results
    # write_json(metrics)


if __name__ == "__main__":

    filename = 'test_data/test_data1.csv'
    main(filename)
