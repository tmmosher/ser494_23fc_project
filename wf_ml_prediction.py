"""
Author: Trenton Mosher
Description: Prediction suite for MS5. Takes three generated models
and uses them for prediction.
"""

import os
import pickle

import numpy as np

from sklearn.metrics import log_loss

filepath = os.getcwd() + "/models/"
outpath = os.getcwd() + "/evaluations/"

def predict(testing):
    """
    Tests all three models on the given set.
    :param testing: Testing data set
    :return: a tuple containing (naive_score, lasso_score, ridge_score)
    """
    inputs = np.asarray([row[:8] for row in testing])
    outputs = np.asarray([[row[8]] for row in testing])
    return (predict_naive(inputs, outputs)), (predict_lasso(inputs, outputs)), (predict_ridge(inputs, outputs))


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
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    with open(outpath + "summary.txt",'w') as f:
        f.write(f"Lasso predictions | Score: {accuracy_scores} | Intercept: {float(intercept)}")
    return accuracy_scores, float(intercept)


def predict_lasso(inputs, outputs):
    if not os.path.isdir(filepath):
        return
    with open(filepath + "lasso_model.pkl", 'rb') as f:
        model = pickle.load(f)
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    score = model.score(inputs, outputs)
    intercept = float(model.intercept_[0])
    with open(outpath + "summary.txt",'w') as f:
        f.write(f"Lasso predictions | Score: {score} | Intercept: {intercept}")
    return score, intercept


def predict_ridge(inputs, outputs):
    if not os.path.isdir(filepath):
        return
    with open(filepath + "ridge_model.pkl", 'rb') as f:
        model = pickle.load(f)
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    score = model.score(inputs, outputs)
    intercept = float(model.intercept_[0])
    with open(outpath + "summary.txt",'w') as f:
        f.write(f"Ridge predictions | Score: {score} | Intercept: {intercept}")
    return score, intercept
