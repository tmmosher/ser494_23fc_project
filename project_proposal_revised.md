# SER494: Project Proposal
## The Death of Truth: Who is the Most Gullible?
## By Trenton Mosher
### 10/28/24

#### Keywords: 
Misinformation, fake news, dead internet
#### Description:
In this project, I plan to discover which population is at the highest risk of sharing factual misinformation. 
Questions I would like to ask include, "What demographic combinations have the highest risk of accidentally
sharing online misinformation?"
and, "Are there any demographics that indicate a higher chance of purposefully spreading misinformation?". 
#### Intellectual Merit: 
I chiefly want to find out who is the most at risk of falling victim to online misinformation. 
While it may be nice to assume it's simply old people who are out of touch with modern technology, 
many peers my age (including myself) have fallen victim to misinformation, even if innocuous. Further, 
I think it would be interesting to see if there's even a difference at all between age groups / sex, or if the 
naturally trusting nature of most human interaction leads to a pretty stable output across the board. Further, trust in
media sources and social media posts varies with age, experience, and education. While a previous study has been conducted
on the topic, it was primarily focused on discerning whether psychopathic or schizotypal 
tendencies were a causal factor in misinformation dissemination. 
#### Data Sourcing:
I source my data from the June 2024 study ['Individual differences in sharing false political information on social media: deliberate and accidental sharing, motivations and positive schizotypy.'](https://pmc.ncbi.nlm.nih.gov/articles/PMC11206957/)
by Buchanan et al. which provides detailed demographic information on participants and their propensity to share
false information. The wf_datagen.py script scrapes the OSF site for the SAV files and saves them to local storage.
The wf_dataprocessing.py script converts the file to a CSV and then strips the unnecessary fields. The authors have not
indicated that such a methodology is a misuse of the study. 
#### Research Objectives:
    1. 
#### Background Knowledge: 
  - [Some background reading that clarifies potentially confounding factors, such as culture](https://misinforeview.hks.harvard.edu/article/who-is-afraid-of-fake-news-modeling-risk-perceptions-of-misinformation-in-142-countries/)
  - [A brief article going over some background information on AI misinfo](https://apnews.com/article/artificial-intelligence-davos-misinformation-disinformation-climate-change-106a1347ca9f987bf71da1f86a141968)
  - [MIT Tech article that covers AI vulnerability in detail](https://www.technologyreview.com/2023/06/28/1075683/humans-may-be-more-likely-to-believe-disinformation-generated-by-ai/)
#### Related Work: 
  - [Misinformation in SEO](https://doi.org/10.1016/j.dss.2023.113976)
  - [Researching misinformation using the internet can make misinfo easier to believe](https://doi.org/10.1038/s41586-023-06883-y)
  - [Navigating persuasive strategies in online health misinformation: An interview study with older adults on misinformation management](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271879/)
  - [Does a perceptual gap lead to actions against digital misinformation? A third-person effect study among medical students](https://pmc.ncbi.nlm.nih.gov/articles/PMC11088137/)
  - [Flattening the Infodemic Curve](https://osf.io/g7vyz)
  - [Corrections of Political Misinformation: No Evidence for an Effect of Partisan Worldview](https://osf.io/cbzvk)