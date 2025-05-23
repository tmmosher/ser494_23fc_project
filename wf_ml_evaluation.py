"""
Author: Trenton Mosher
Description: Splits the data into two sets, trains the model(s), and evaluates it
"""
import os
import random

import numpy as np
import wf_ml_prediction

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
    random.shuffle(csv_data)
    split_ind = int(len(csv_data) * percent)
    # save data sets to file
    save_dataset(csv_data[:split_ind], training_name)
    save_dataset(csv_data[split_ind:], testing_name)
    return csv_data[:split_ind], csv_data[split_ind:]


def save_dataset(dataset, filename):
    output_folder = os.getcwd() + "/data_processed/"
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    np.save(output_folder + filename, np.asarray(dataset))


def save_model(data, loss, intercept, filename, is_sklearn=False, model=None):
    import pickle
    output_folder = os.getcwd() + "/models/"
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    if not is_sklearn:
        obj = {
            "weights": data,
            "loss": loss,
            "intercept": intercept
        }
        with open(output_folder + filename+".pkl", 'wb') as f:
            pickle.dump(obj, f)
    else:
        with open(output_folder + filename+".pkl", 'wb') as f:
            pickle.dump(model, f)


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


def generate_lasso_model(in_array, out_array):
    import wf_ml_training as tr
    weights, intercept = tr.lg_sklearn_lasso_regression(in_array, out_array, "lasso_model")
    print("LASSO regression model generated.")


def engineer_feature(csv_data):
    """
    Engineers a dataset with similarly populated samples. Need to change the 'conditions' object
    manually to isolated different variables. 
    :param csv_data: list
    :return: a sample data set
    """
    sample = []
    # pick random sample as point of comparison
    comp = csv_data[0]
    sample.append(comp)
    for i in range(1, len(csv_data)):
        if multi_comparison(comp, csv_data[i], conditions):
            sample.append(csv_data[i])
    return sample

conditions = [
    lambda a, b: a == b, # must match gender
    lambda a, b: abs(a-b) < 2, # must be within one education level
    lambda a, b: abs(a-b) < 3, # must be within 2 years of age
    lambda a, b: a == b, # must have same employment status
    lambda a, b: abs(a-b) < 2, # similar political leanings
    lambda a, b: abs(a-b) < 2, # similar trust in media
    ### swap these two to 'True' to isolate for them. Otherwise, swap in their commented code
    lambda a, b: True, # abs(a-b) < 2,
    lambda a, b: True #abs(a-b) < 2 #True # abs(a-b) < 2
]
def multi_comparison(a, b, conditions_set):
    return all(cond(a, b) for a, b, cond in zip(a, b, conditions_set))


def generate_ridge_model(in_array, out_array):
    import wf_ml_training as tr
    weights, intercept = tr.lg_sklearn_ridge_regression(in_array, out_array, "ridge_model")
    print("Ridge regression model generated.")

if __name__ == "__main__":
    training, testing = split_training("processed_misinfo_sharing_combined.csv")
    inputs = np.asarray([row[:8] for row in training])
    outputs = np.asarray([[row[8]] for row in training])
    generate_naive_model(inputs, outputs)
    generate_lasso_model(inputs, outputs)
    generate_ridge_model(inputs, outputs)
    # sample = None
    sample = engineer_feature([row for row in testing])
    wf_ml_prediction.predict(testing)
