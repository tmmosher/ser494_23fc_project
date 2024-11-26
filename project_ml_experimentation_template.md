#### SERX94: Experimentation
#### The Death of Truth: Who is the Most Gullible?
#### By Trenton Mosher
#### 11/25/24


## Explainable Records
### Record 1
**Raw Data:** [1, 2, 80, 4, 6, 3, 3, 2 (media sharing), 0 (shared mis-info), 0]

Prediction Explanation:** Given the weights array leaning so heavily toward a propensity
to share news on social media, it's not particularly surprising to see that this respondent
was not predicted to have shared misinformation based on his low score in that column 
(column 7, zero-indexed, here it is '2').

### Record 2
**Raw Data:** [1, 3, 64, 4, 6, 3, 4, 2 (media sharing), 1 (shared mis-info), 0]

Prediction Explanation:** Despite the fact that this subject has unknowingly shared misinformation,
their propensity to share news online is also very low. Because that category holds the highest weight by far, a false 
negative prediction was understandable here.


## Interesting Features
### Feature A
**Feature:** Media Behavior

**Justification:** Holding the second-highest feature weight on average,
it would make sense that such a feature would trump demographic variations in
the data. Increasing this feature will surely lead to more positive predictions.

### Feature B
**Feature:** Media Sharing

**Justification:** Holding the highest feature weight on average, varying this
feature is likely to lead to significant changes in the predictions.

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

