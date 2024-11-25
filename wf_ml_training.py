"""
Author: Trenton Mosher
Description: Trains the logistic regression model
"""

import numpy as np

def standardize(inputs):
    return (inputs - np.mean(inputs, axis=0)) / np.std(inputs, axis=0)

def lg_gradient_descent(inputs, outputs, alpha, iterations=500):
    """
    Runs the gradient descent algorithm for logistic regression
    :param inputs: input as numpy array
    :param outputs: outputs as numpy array
    :param alpha: learning rate. not stable at high values
    :param iterations: number of desired iterations. Minimum 100
    :return: tuple containing (weights, total_loss)
    """
    # baseline number of iterations
    iterations = 100 if iterations < 100 else iterations
    # standardize the inputs. Sources disagree on whether this is strictly necessary.
    # shouldn't be for my naive model, will be for my ridge & LASSO models. Might as well have it.
    inputs = standardize(inputs)
    # tries to be pretty generic with the number of features as I'll need to vary those later
    weights = np.zeros(inputs.shape[1])
    intercept = 0 # wikipedia says this is the 'c' value in the logistic function from the notes.
    # While the notes say that this value is unnecessary (and it may usually be?) wikipedia and
    # other internet sources use it, so I'm keeping it
    loss = 0
    for i in range(iterations):
        prediction = logistic_function(np.dot(inputs, weights) + intercept)
        # get error
        loss = get_loss(outputs, prediction)
        # update weights and intercept
        weights -= alpha * (1 / len(inputs)) * np.dot(inputs.T, prediction - outputs)
        intercept -= alpha * (1 / len(inputs)) * np.sum(prediction - outputs)
    return weights, loss


def logistic_function(x):
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