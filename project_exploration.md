# Exploratory Analysis of Misinformation Data
## By Trenton Mosher, 10/22/24
# Basic Questions and Interpretable Records
## Dataset One
### Title: [A dataset of Covid-related misinformation videos and their spread on social media](https://zenodo.org/records/4557828)
### Author(s): Aleksi Knuutila
### Date: 2/23/2021
### Records: 8,122
### MD5 Hash: 
#### 3825781f8b59248eaa8095582ec02fbb
### Column Definitions
#### youtube_link
A link to the video in question. YouTube has deleted most of the videos for being misinforming, so most will be dead.
#### video_title
Title of the video
#### video_description
Description of the video
#### view_count
Number of views
#### channel_id
ID of the channel in question
#### subscriber_count
Number of subscribers to channel
#### removal_timestamp
Time that video was deleted
#### published_timestamp
TIme that video was uploaded
#### archive_url
Link to an archive containing the video, where available
#### facebook_graph_reactions
Number of reactions on Facebook
#### facebook_graph_comments
Number of comments on Facebook
#### facebook_graph_shares
Number of shares on Facebook
#### twitter_post_ids
Twitter post ID's including links to the video
#### facebook_post_ids
Facebook post ID's including links to the video
## Row Exploration
### Row 31
Row 31 exhibits qualities of good data. Every column is valid and contains easily readable data from a well-known creator.
### Row 54
Row 54 exhibits qualities of very poor data. Relatively few columns are valid, and critical descriptors to be used as a key (i.e., channel_id) are missing. 

## Dataset Two
### Title: [Individual differences in sharing false political information on social media: deliberate and accidental sharing, motivations and positive schizotypy.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11206957/)
### Author(s): Tom Buchanan, Rotem Perach, Deborah Husbands, Amber F Tout, Ekaterina Kostyuk, James Kempley, Laura Joyner
### Date: 1/12/2024
### Records: 1,916 (all studies)
### MD5 Hashes
#### Study 1: b06377c714fcbfd1a1730a1f9b0b6d47
#### Study 2: b06377c714fcbfd1a1730a1f9b0b6d47
#### Study 3: 34b7e7325d3e84ba116594e479c5a606
#### Study 4: 8b4138fc7ccefbbc44b435b46e1b110a
### Column Definitions:
#### Self-Descriptors
Many fields contain data such as race, age, gender, education, etc. None of these require any special interpretation beyond the ability to read.
#### polit_ideo
Measured on a scale where 1 is most left and 7 is most right
#### soc_med_use_recoded
Measured on a frequency basis from 1 (not at all) to 7 (several times a day)
#### soc_med_trust
Level in trust in political information on social media, measured on a scale of 1 (not at all) to 5 (a great deal)
#### soc_med_behav
How much social media influences a participants' behavior, measured on a scale of 1 (not at all) to 5 (a great deal)
#### soc_med_share
How much a participant shares political information on social media, measured on a scale of 1 (not at all) to 5 (a great deal)
#### shared_found_later
Yes/No question indicating whether a participant had shared information online and later found out it was false.
#### shared_knowing
Yes/No question indicating whether a participant had knowingly shared false information online
#### Remainder
Many of the other columns are specific to the authors' study of psychopathy and shizotypal behavior. Out of scope for this analysis. 
## Row Exploration (taken from misinfo_study1)
### Row 576
This row is interesting as it contains the oldest participant. Of course, all columns are filled (the study required every question be answered). He is quite conservative and has unknowingly shared false information. Reasonable and representative data.
### Row 518
This row similarly contains an elderly retired participant of similar age and political belief. He has similarly unknowingly shared misinformation online (wonder if that will be a pattern...). Reasonable and representative data
### [Hashing Tool](https://emn178.github.io/online-tools/md5_checksum.html)
## Background Domain Knowledge
In the era of AI, bots, and mass internet misinformation, discerning the truth when scrolling online is becoming extraordinarily difficult. 
Even those who attempt to proactively guard themselves from lies find themselves prone to being enwebbed, according to 
Aslett et al. Search engine optimization leads to untrustworthy sources of niche misinformation cases slipping up to the top
of results, with common resources like Wikipedia failing to debunk bunk sources. Studies have previously shown that participants with lower levels of reading 
and critical thinking skills are at greater risk of accidentally spreading misinformation. A recent study by Buchanan et al. discovered that a primary motivation
for accidentally sharing misinformation was to raise awareness of a certain topic, perhaps implying that the natural impulse to share alarming information
often trumps our critical thinking. The key factors I want to consider are how age, education, political ideology, and trust in social media influence the propensity to
share online misinformation, with a focus on age. Older people are often at risk of scams and are less familiar with the internet and surrounding culture (i.e., trolling),
and we would therefore expect age to correlate quite highly with the propensity to share fake news, AI generated videos, etc. 
### Citations:
- Alan R. Dennis, Patricia L. Moravec, Antino Kim, Search & Verify: Misinformation and source evaluations in Internet search results, Decision Support Systems, Volume 171, 2023,113976, ISSN 0167-9236,[https://doi.org/10.1016/j.dss.2023.113976.](https://www.sciencedirect.com/science/article/pii/S0167923623000519)
- Aslett, K., Sanderson, Z., Godel, W. et al. Online searches to evaluate misinformation can increase its perceived veracity. Nature 625, 548–556 (2024). https://doi.org/10.1038/s41586-023-06883-y
- Buchanan, T., & Perach, R. (2024, June 27). Individual differences in sharing false political information on social media: deliberate and accidental sharing, motivations and positive schizotypy. Retrieved from osf.io/d84mu 

## Dataset Generality
I consider the dataset to represent the common American quite well. The data exhibits low levels of psychopathic and schizotypal behavior (<2%, by the author's summary).
The median age among the data is 34 years, with the median American age being 38.5 years according to the US Census Bureau, making the median
about 88% that of the overall population. Furthermore, ages range from 18 to 80, which represents the entire spectrum of American adults - from young adult, to just above
the life expectancy. The sample size is also quite sufficient for an online survey with over 1,900 responses, exceeding the 1,000 responses recommended 
by sources such as [surveyplanet](https://surveyplanet.com/sample-size-calculator#:~:text=A%20good%20sample%20size%20for,reading%20our%20blog%20about%20it.). Furthermore,
school the least common education category was a high school dropout, matching real American census data. 

## Data Transformations
Empty view counts for the COVID misinformation dataset were adjusted to zeroes. Often, these videos had very little (less than 100) views, so I placed
them in the lowest bracket possible. Of course, it is obvious that the videos themselves have SOME views - as they were flagged for misinformation - but in comparison to the largest
videos in the dataset that sparked hundreds of Twitter posts and hundreds of thousands to millions of views, I don't think this is an unreasonable transformation. Also, I added a couple columns in this
dataset to count how many Twitter and Facebook posts were linked to said video as a convenience for later interpretation. On the misinformation sharing dataset,
I removed several unrelated columns, as the authors were originally collecting the data for interpretation on schizotypal behavior's effect on misinformation sharing. As there were 
relatively few responses indicating schizotypal behavior, I find including them makes little difference, and probably is even more indicative of the expected American population. 
I also removed all text from numeric data columns for easier graphing and reading. 

## Visualizations

### age_media.png ![age_media.png](visuals%2Fage_media.png)
While a scatter plot doesn't do incredible justice to the data here, it does show that young responders are more likely to 
trust media sources. Hilariously, nobody over the age of 65 has complete trust in the media. 
### age_politi.png ![age_politi.png](visuals%2Fage_politi.png)
The variety of political ideologies shows a relatively broad field at younger ages. 
However, There is a noticeable bump in far-right ideology toward the higher age ranges.
Aside from a select few outliers, there are not many far-left participants over the age of 70.
### education_stats.png ![education_stats.png](visuals%2Feducation_stats.png)
As expected, most participants have at least attended some university or college. This indicates that most participants are 
at least functionally literate and are likely to have higher critical thinking skills.
### politi_media.png ![politi_media.png](visuals%2Fpoliti_media.png)
Quite unsurprisingly, the fringes of both political ideologies are rather distrustful of the media.
Very few participants have complete trust in the media, with no slight right leaners and slight left leaners trusting the media.
Interestingly, more far-right participants had more trust in the media that far-left participants.
### shared_found_later.png ![shared_found_later.png](visuals%2Fshared_found_later.png)
This graph, showing whether participants shared information they later discovered was incorrect, indicates that relatively few of the sample
had unwittingly shared false information (to their knowledge). This study was self-reported, meaning that it is likely there was a significant
population of responders who have shared misinformation and are yet to discover it was false.