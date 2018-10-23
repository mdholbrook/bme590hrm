from functions.load_data import read_csv, clean_data
from functions.process_ecg import filter_voltage, r_peak_detection, calcuate_metrics
from functions.write_results import write_json

def main(file):

    # Read in data
    df = read_csv(file)

    # Clean data
    df = clean_data(df)

    # Filter data
    df = filter_voltage(df)

    # R-peak detection
    df = r_peak_detection(df)

    # Calculate metrics
    metrics = calcuate_metrics(df)

    # Write results
    write_json(metrics)


if __name__=="__main__":

    main()