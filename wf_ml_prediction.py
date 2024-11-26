"""
Author: Trenton Mosher
Description: Prediction suite for MS5. Takes three generated models
and uses them for prediction.
"""

import os, pickle

import numpy as np

from wf_ml_training import logistic_function

filepath = os.getcwd() + "/models/"

def predict(testing):
    inputs = np.asarray([row[:8] for row in testing])
    outputs = np.asarray([[row[8]] for row in testing])
    print(predict_naive(inputs, outputs))
    print(predict_lasso(inputs, outputs))
    print(predict_ridge(inputs, outputs))
    pass


def predict_naive(inputs, outputs):
    import wf_ml_training as tr
    if not os.path.isdir(filepath):
        return
    with open(filepath + "naive_model.pkl", 'rb') as f:
        model = pickle.load(f)
    weights = model["weights"]
    intercept = model["intercept"]
    accuracy = []
    val = np.dot(inputs, weights) + intercept
    y = tr.logistic_function(val)
    prediction = (y > 0.5).astype(int)
    for i in range(len(prediction)):
        accuracy.append(prediction[i] == outputs[i])
    accuracy_scores = float(sum(accuracy) / len(accuracy))
    return accuracy_scores


def predict_lasso(inputs, outputs):
    if not os.path.isdir(filepath):
        return
    with open(filepath + "lasso_model.pkl", 'rb') as f:
        model = pickle.load(f)
    return model.score(inputs, outputs)


def predict_ridge(inputs, outputs):
    if not os.path.isdir(filepath):
        return
    with open(filepath + "ridge_model.pkl", 'rb') as f:
        model = pickle.load(f)
    return model.score(inputs, outputs)
    pass