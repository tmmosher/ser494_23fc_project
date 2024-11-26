"""
Author: Trenton Mosher
Description: Prediction suite for MS5. Takes three generated models
and uses them for prediction.
"""
import gc
import os
import pickle
import time

import numpy as np

os.environ["NUMPY_EXPERIMENTAL_ARRAY_FUNCTION"] = "0"
filepath = os.getcwd() + "/models/"
outpath = os.getcwd() + "/evaluations/"

def predict(testing):
    """
    Tests all three models on the given set.
    :param testing: Testing data set
    :return: a tuple containing scores for each model
    """
    inputs = np.asarray([row[:8] for row in testing])
    outputs = np.asarray([[row[8]] for row in testing])
    naive = predict_naive(np.copy(inputs), np.copy(outputs))
    lasso = predict_lasso(np.copy(inputs), np.copy(outputs))
    ridge = predict_ridge(np.copy(inputs), np.copy(outputs))
    random = predict_random(np.copy(inputs), np.copy(outputs))
    return naive, lasso, ridge, random


def predict_naive(inputs, outputs):
    import wf_ml_training as tr
    # unpack model
    if not os.path.isdir(filepath):
        return
    with open(filepath + "naive_model.pkl", 'rb') as f:
        model = pickle.load(f)
    weights = model["weights"]
    intercept = model["intercept"]
    # run model
    accuracy = []
    true_pos = []
    false_pos = []
    val = np.dot(inputs, weights) + intercept
    y = tr.logistic_function(val)
    prediction = (y > 0.5).astype(int)
    # create prediction accuracy
    for i in range(len(prediction)):
        accuracy.append(prediction[i] == outputs[i])
        true_pos.append(prediction[i] == 1 and outputs[i] == 1)
        false_pos.append(prediction[i] == 1 and outputs[i] == 0)
    precision1 = float(sum(true_pos) / (sum(true_pos) + sum(false_pos)))
    accuracy_scores = float(sum(accuracy) / len(accuracy))
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    with open(outpath + "summary.txt",'w') as f:
        f.write(f"Naive predictions\nAccuracy: {accuracy_scores} | Precision: {precision1}\n")
    return accuracy_scores, precision1


def predict_lasso(inputs, outputs):
    if not os.path.isdir(filepath):
        return
    with open(filepath + "lasso_model.pkl", 'rb') as f:
        model = pickle.load(f)
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    # run model (yes, there is a 'score' method, but I need FP / TPs
    accuracy = []
    true_pos = []
    false_pos = []
    predictions = model.predict(inputs)
    for i in range(len(predictions)):
        accuracy.append(predictions[i] == outputs[i])
        true_pos.append(predictions[i] == 1 and outputs[i] == 1)
        false_pos.append(predictions[i] == 1 and outputs[i] == 0)
    precision2 = float(sum(true_pos) / (sum(true_pos) + sum(false_pos)))
    score = model.score(inputs, outputs)
    with open(outpath + "summary.txt",'a') as f:
        f.write(f"Lasso predictions\nScore: {score} | Precision: {precision2}\n")
    return score, precision2


def predict_ridge(inputs, outputs):
    if not os.path.isdir(filepath):
        return
    with open(filepath + "ridge_model.pkl", 'rb') as f:
        model = pickle.load(f)
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    accuracy = []
    true_pos = []
    false_pos = []
    predictions = model.predict(inputs)
    for i in range(len(predictions)):
        accuracy.append(predictions[i] == outputs[i])
        true_pos.append(predictions[i] == 1 and outputs[i] == 1)
        false_pos.append(predictions[i] == 1 and outputs[i] == 0)
    precision3 = float(sum(true_pos) / (sum(true_pos) + sum(false_pos)))
    score = model.score(inputs, outputs)
    with open(outpath + "summary.txt",'a') as f:
        f.write(f"Ridge predictions\nAccuracy: {score} | Precision: {precision3}\n")
    return score, precision3


def predict_random(inputs, outputs):
    from random import random
    if not os.path.isdir(filepath):
        return
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    accuracy = []
    true_pos = []
    false_pos = []
    predictions = [1 if (random() > 0.5) else 0 for _ in range(len(inputs))]
    for i in range(len(predictions)):
        accuracy.append(predictions[i] == outputs[i])
        true_pos.append(predictions[i] == 1 and outputs[i] == 1)
        false_pos.append(predictions[i] == 1 and outputs[i] == 0)
    precision4 = float(sum(true_pos) / (sum(true_pos) + sum(false_pos)))
    accuracy = float(sum(accuracy) / len(accuracy))
    with open(outpath + "summary.txt",'a') as f:
        f.write(f"Random predictions\nAccuracy: {accuracy} | Precision: {precision4}\n")
    return accuracy, precision4