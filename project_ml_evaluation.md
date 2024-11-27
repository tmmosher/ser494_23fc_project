#### SERX94: Machine Learning Evaluation
#### The Death of Truth: Who is the Most Gullible?
#### By Trenton Mosher
#### 11/25/24

## Evaluation Metrics
### Metric 1
**Name:** Accuracy

**Choice Justification:** 
I chose accuracy as a fairly obvious metric for a classification model. We want
an objective success rate for how good the model is at predicting our outcome.

### Metric 2
**Name:** Precision

**Choice Justification:** 
Higher precision minimizes false positives, which is an important metric for ensuring that
we don't flag innocent subjects for misinformation.

## Alternative Models
### Alternative 1: LASSO Logistic Regression
**Construction:** Use SKLearn's Logistic Regression class with an added L1 penalty.

**Evaluation:** Overall, this was the better model of the SKLearn's when tested with every metric. Accuracy averaging at ~77%, though
precision varies wildly. Precision averages about 53%.

### Alternative 2: Ridge Logistic Regression
**Construction:** Use SKLearn's Logistic Regression class with default penalty.

**Evaluation:** Second to worst model when it comes to average accuracy, but precision is still better (43% on average) than random.

### Alternative 3: Baseline random prediction
**Construction:** Simply fill a list with random values of 0 or 1.

**Evaluation:** Accuracy as expected (~50%) over the course of several runs. Precision is the worst at 24% on average.

## Best Model

**Model:** Personal model. The accuracy is virtually identical to the SKLearn models, but the precision is
on average slightly better.

While this model doesn't match the research objectives, I have found
that the objectives themselves are flawed. After building the models, it's clear that age and trust
in social media are extremely poor predictors of how often someone will share misinformation. Only using
those two features in a regression model leads to a model that is virtually useless. Therefore, the addition of
the other features is justifiable.