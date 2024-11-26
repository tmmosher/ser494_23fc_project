"""
Author: Trenton Mosher
Description: Splits the data into two sets, trains the model(s), and evaluates it
"""
import os

import numpy as np


def split_training(filepath, training_name="training", testing_name="testing", percent=0.8):
    """
    :param testing_name:
    :param training_name:
    :param filepath: file path to the CSV file to process
    :param percent: relative percentage of training data to test split
    :return: Tuple containing (training, test) data sets
    """
    # ensures that bad input doesn't mess up index calculation
    percent = 0.8 if percent > 1 or percent < 0 else percent
    # load csv file into memory, split, and return both data structures as a tuple
    csv_data = get_processed_data(filepath)
    split_ind = int(len(csv_data) * percent)
    # save data sets to file
    save_dataset(csv_data[:split_ind], training_name)
    save_dataset(csv_data[split_ind:], testing_name)
    return csv_data[:split_ind], csv_data[split_ind:]


def save_dataset(dataset, filename):
    output_folder = os.getcwd() + "/models/"
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    np.save(output_folder + filename, np.asarray(dataset))


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
        csv_data.pop(0)
    return [list(map(lambda a: int(a), row)) for row in csv_data]


def generate_naive_model(in_array, out_array):
    import wf_ml_training as tr
    weights, loss, intercept = tr.lg_naive_gradient_descent(in_array, out_array, 0.01, "naive_model")
    print("Naive logistic regression model generated.")

if __name__ == "__main__":
    training, testing = split_training("processed_misinfo_sharing_combined.csv")
    inputs = np.asarray([row[:8] for row in training])
    outputs = np.asarray([[row[8]] for row in training])
    generate_naive_model(inputs, outputs)
