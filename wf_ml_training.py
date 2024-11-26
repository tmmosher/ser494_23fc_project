"""
Author: Trenton Mosher
Description: Trains the logistic regression model(s)
"""
import os
import time

from sklearn.linear_model import LogisticRegression


import numpy as np
from wf_ml_evaluation import save_model
os.environ["NUMPY_EXPERIMENTAL_ARRAY_FUNCTION"] = "0"
def standardize(inputs):
    return (inputs - np.mean(inputs, axis=0)) / np.std(inputs, axis=0)

def lg_naive_gradient_descent(inputs: np.array, outputs: np.array, alpha, filename):
    """
    Runs the gradient descent algorithm for logistic regression
    :param filename: Filename for output. Do not include the extension, please.
    :param inputs: input as numpy array
    :param outputs: outputs as numpy array
    :param alpha: learning rate. not stable at high values
    :return: tuple containing (weights, total_loss, intercept) for prediction. Saves the weights to file.
    """
    # standardize the inputs. Sources disagree on whether this is strictly necessary.
    # shouldn't be for my naive model, will be for my ridge & LASSO models. Might as well have it.
    inputs = standardize(inputs)
    outputs = outputs.flatten()
    # tries to be pretty generic with the number of features as I'll need to vary those later
    weights = np.zeros(inputs.shape[1])
    intercept = 0 # wikipedia says this is the 'c' value in the logistic function from the notes.
    # While the notes say that this value is unnecessary (and it may usually be?) wikipedia and
    # other internet sources use it, so I'm keeping it
    loss = 0
    stop = False
    while not stop:
        prediction = logistic_function(np.dot(inputs, weights) + intercept)
        # get error
        loss = get_loss(outputs, prediction)
        # update weights and intercept
        w0 = (1 / len(inputs)) * np.dot(inputs.T, (prediction - outputs))
        weights -= alpha * w0
        intercept -= alpha * (1 / len(inputs)) * np.sum(prediction - outputs)
        if np.allclose(w0, 0, atol=1e-6):
            stop = True
    save_model(weights, loss, intercept, filename)
    return weights, loss, intercept


def logistic_function(x, slowdown=False):
    """
    logistic function as described on p 41 of the regression notes
    :param x: input value
    :return: conditional probability value
    """
    return 1 / (1 + np.exp(-x))

def get_loss(output, pred_output):
    """
    Calculates the loss using the J(w) function shown on page 43 of the
    regression notes and Wikipedia for logistic regression @
    https://en.wikipedia.org/wiki/Logistic_regression
    :param output: Actual output list
    :param pred_output: Predicted output list
    :return: total calculated loss
    """
    size = len(output)
    return -(1 / size) * np.sum(output * np.log(pred_output) + (1 - output) * np.log(1 - pred_output))


def lg_sklearn_lasso_regression(inputs, outputs, filename):
    """
    Generates an SKLearn logistic regression model using an L1 penalty
    :param inputs: input as numpy array
    :param outputs: outputs as numpy array
    :param filename: Filename for output. Do not include the extension, please.
    :return: tuple containing (weights, intercept) for prediction. Saves the weights & intercept to file.
    """
    model = LogisticRegression(penalty="l1", solver="liblinear",tol=1e-6)
    inputs = standardize(inputs)
    outputs = outputs.flatten()
    model.fit(inputs, outputs)
    save_model(model.coef_[0], 0, model.intercept_[0], filename, is_sklearn=True, model=model)
    return model.coef_[0], model.intercept_[0]


def lg_sklearn_ridge_regression(inputs, outputs, filename):
    """
    Generates an SKLearn logistic regression model using an L2 penalty
    :param inputs: input as numpy array
    :param outputs: outputs as numpy array
    :param filename: Filename for output. Do not include the extension, please.
    :return: tuple containing (weights, intercept) for prediction. Saves the weights & intercept to file.
    """
    model = LogisticRegression(penalty="l2", tol=1e-6)
    inputs = standardize(inputs)
    outputs = outputs.flatten()
    model.fit(inputs, outputs)
    save_model(model.coef_[0], 0, model.intercept_[0], filename, is_sklearn=True, model=model)
    return model.coef_[0], model.intercept_[0]