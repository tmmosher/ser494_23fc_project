#### SERX94: Experimentation
#### The Death of Truth: Who is the Most Gullible?
#### By Trenton Mosher
#### 11/25/24


## Explainable Records
### Record 1
**Raw Data:** [1, 2, 80, 4, 6, 3, 3, 2 (media sharing), 0 (shared mis-info), 0]

Model predicted: Has not shared misinformation

Prediction Explanation:** Given the weights array leaning so heavily toward a propensity
to share news on social media, it's not particularly surprising to see that this respondent
was not predicted to have shared misinformation based on his low score in that column.

### Record 2
**Raw Data:** [1, 3, 64, 4, 6, 3, 4, 2 (media sharing), 1 (shared mis-info), 0]

Model predicted: Has not shared misinformation

Prediction Explanation:** Despite the fact that this subject has unknowingly shared misinformation,
their propensity to share news online is also very low, making this an uncommon occurrence. 
Because that category holds the highest weight by far, a false negative prediction was understandable here.


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
### Varying A: Media Behavior
**Prediction Trend Seen:** Across 10 runs, the average precision across all three models dropped
to ~20.43%. At lower testing sample sizes, the performance became very poor. It's impossible
to discern a trend when the models themselves fall apart. While only varying social media behavior seems like it 
would show an insightful trend, unfortunately this does not make sense in practice. As we have to hold all other 
variables roughly equal, the demographics between each participant in the sample set are virtually identical, and will
therefore be largely influenced by feature B and the remaining features instead. This should intuitively make sense, as
we are pretty much testing on the exact same participant each time - of course the predictions would be very similar!

### Varying B: Media Sharing
**Prediction Trend Seen:** Across 10 runs, the outcome was a similarly sore sight for only varying feature B with some improvements. 
The precision averaged out to ~43.23% across all three models, a notable improvement over varying feature A. While this
isn't definitive, it at least shows that media sharing habits are a better predictor (reducing false positives) over 
baseline. However, do note that varying feature B runs into similar problems as only varying feature A. With keeping all
other demographic data the same, folks tend to have similar attitudes toward social media as well, meaning the data becomes
nearly identical. Therefore, the fact that only varying feature B impacts precision by such an amount may be less 
meaningful than anticipated.

### Varying A and B together
**Prediction Trend Seen:** Varying A and B together saw an improved precision outcome more similar to just varying B, 
at an average of 43.7% across all three models. This seems to imply that the addition of B into the mixture had a far 
greater impact on the precision than the varying of feature A, which is perhaps unsurprising given the interpretation
above. 


### Varying A and B inversely
**Prediction Trend Seen:** TODO

