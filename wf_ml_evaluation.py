"""
Author: Trenton Mosher
Description: Splits the data into two sets, trains the model, and evaluates it
"""
import os


def split_training(filepath, percent=0.8):
    """
    :param filepath: file path to the CSV file to process
    :param percent: relative percentage of training data to test split
    :return: Tuple containing (training, test) data sets
    """
    # ensures that bad input doesn't mess up index calculation
    percent = 0.8 if percent > 1 or percent < 0 else percent
    # load csv file into memory, split, and return both data structures as a tuple
    from wf_visualization import check_files
    csv_data = check_files("processed_misinfo_sharing_combined.csv")
    split_ind = int(len(csv_data) * percent)
    return csv_data[split_ind:], csv_data[:split_ind]

def get_processed_data(filename):
    import csv
    if not os.path.isdir(os.getcwd() + "\\data_processed") or not os.path.isfile(
            os.getcwd() + f"\\data_processed\\{filename}"):
        print("Failed to find processed data files")
        return None
    csv_data = []
    # extract csv data
    with open(os.getcwd() + f"\\data_processed\\{filename}", "r") as file:
        csv_reader = csv.reader(file)
        [csv_data.append(row) for row in csv_reader]
    return [int(col) for val in csv_data for col in val]