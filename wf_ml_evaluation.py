"""
Author: Trenton Mosher
Description: Splits the data into two sets, trains the model, and evaluates it
"""
from tabnanny import check


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
