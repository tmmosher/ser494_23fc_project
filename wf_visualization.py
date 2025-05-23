"""
Author: Trenton Mosher
Description: Compute summary statistics of data
"""

import os, csv
from matplotlib.ticker import MaxNLocator


def compute_summary_statistics():
    csv_data = check_files("processed_misinfo_sharing_combined.csv")
    if not csv_data:
        return None

    """
    Chosen summary statistics:
    Categorical:
    - shared_found_later
    - education
    Quantitative:
    - age
    - politi_ideo
    - media_trust
    """

    # Qualitative
    quality_dict = {}
    csv_data.pop(0)

    # Check misinformation sharing stats
    for row in csv_data:
        if f"{row[8]}" not in quality_dict:
            quality_dict[f"{row[8]}"] = 1
        else:
            quality_dict[f"{row[8]}"] += 1
    freq_val_shared = "Yes" if quality_dict["1"] > quality_dict["0"] else "No"
    freq_least_shared = "No" if quality_dict["1"] > quality_dict["0"] else "Yes"

    # check education stats
    quality_dict.clear()
    for row in csv_data:
        if row[1] not in quality_dict:
            quality_dict[row[1]] = 1
        else:
            quality_dict[row[1]] += 1
    freq_val_edu = ""
    freq_least_edu = ""
    categories_count = len(quality_dict.keys())
    max_val = max(quality_dict.values())
    min_val = min(quality_dict.values())
    for key in quality_dict.keys():
        if quality_dict[key] >= max_val:
            freq_val_edu = key
        elif quality_dict[key] <= min_val:
            freq_least_edu = key

    # Quantitative
    age_stats = {}
    politi_ideo_stats = {}
    media_trust_stats = {}

    # age
    age_stats["max"] = max(csv_data, key=lambda x: x[2])[2]
    age_stats["min"] = min(csv_data, key=lambda x: x[2])[2]
    age_stats["median"] = csv_data[int(len(csv_data) / 2)][2] # the misinfo study file is already sorted by age, so pulling median from the middle is valid

    csv_data.sort(key=lambda x: x[4], reverse=True) # sort by political ideology

    # politi_ideo
    politi_ideo_stats["max"] = max(csv_data, key=lambda x: x[4])[4]
    politi_ideo_stats["min"] = min(csv_data, key=lambda x: x[4])[4]
    politi_ideo_stats["median"] = csv_data[int(len(csv_data) / 2)][4]

    csv_data.sort(key=lambda x: x[6], reverse=True) # sort by trust level

    # media_trust
    media_trust_stats["max"] = max(csv_data, key=lambda x: x[5])[5]
    media_trust_stats["min"] = min(csv_data, key=lambda x: x[5])[5]
    media_trust_stats["median"] = csv_data[int(len(csv_data) / 2)][5]

    # write output values

    with open(os.getcwd() + "\\data_processed\\summary.txt", "w", encoding='utf-8') as file:
        file.write(f"Summary Statistics:\nCategorical\n'shared_found_later': 2 Categories. Most frequent was '{freq_val_shared}'. Least frequent was '{freq_least_shared}'.\n")
        file.write(f"education: {categories_count} Categories. Most frequent was '{freq_val_edu}'. Least frequent was '{freq_least_edu}'.\n")
        file.write(f"Quantitative\nage: Minimum: {age_stats['min']}, Maximum: {age_stats['max']}, Median: {age_stats["median"]}.\n")
        file.write(f"politi_ideo: Minimum: {politi_ideo_stats['min']}, Maximum: {politi_ideo_stats['max']}, Median: {politi_ideo_stats["median"]}.\n")
        file.write(f"media_trust: Minimum: {media_trust_stats['min']}, Maximum: {media_trust_stats['max']}, Median: {media_trust_stats['median']}.\n")

def correlation_generation():
    import pandas as pd
    csv_data = check_files("processed_misinfo_sharing_combined.csv")
    if not csv_data:
        return None
    csv_data.pop(0) # remove columns for processing
    age_series = [x[2] for x in csv_data]
    poli_series = [x[4] for x in csv_data]
    media_series = [x[5] for x in csv_data]
    corref_data = {
        'age' : age_series,
        'politi_ideo' : poli_series,
        'media_trust' : media_series
    }
    df = pd.DataFrame(corref_data, columns=['age', 'politi_ideo', 'media_trust'])
    output_matrix = df.corr()
    with open(os.getcwd() + "/data_processed/correlations.txt", mode='w', encoding='utf-8') as file:
        file.write(output_matrix.to_string())

# usually filename will be "processed_misinfo_sharing_combined.csv" for this
def check_files(filename):
    if not os.path.isdir(os.getcwd() + "\\data_processed") or not os.path.isfile(
            os.getcwd() + f"\\data_processed\\{filename}"):
        print("Failed to find processed data files")
        return None
    csv_data = []
    # extract csv data
    with open(os.getcwd() + f"\\data_processed\\{filename}", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_data.append(row)
    return csv_data

def create_charts():
    import matplotlib.pyplot as plt, pandas as pd
    csv_data = check_files("processed_misinfo_sharing_combined.csv")
    if not csv_data:
        return None
    csv_data.pop(0) # remove columns for processing
    age_series = [int(x[2]) for x in csv_data]
    poli_series = [int(x[4]) for x in csv_data]
    media_series = [int(x[5]) for x in csv_data]
    shared_found_later = [x[8] for x in csv_data]
    education_stats = [x[1] for x in csv_data]
    age_pooli_corref = {
        'age' : age_series,
        'politi_ideo' : poli_series
    }
    age_media_corref = {
        'age' : age_series,
        'media_trust' : media_series
    }
    poli_media_corref = {
        'politi_ideo' : poli_series,
        'media_trust' : media_series,
    }
    age_poli = pd.DataFrame(age_pooli_corref, columns=['age', 'politi_ideo'])
    age_media = pd.DataFrame(age_media_corref, columns=['age', 'media_trust'])
    poli_media = pd.DataFrame(poli_media_corref, columns=['politi_ideo', 'media_trust'])
    if not os.path.isdir(os.getcwd() + "/visuals"):
        os.mkdir(os.getcwd() + "/visuals")
    # age and political ideology
    ap_fig, ap_ax = plt.subplots()
    ap_ax.set(title="Age v. Political Ideology",
              xlabel='Political Ideology',
              ylabel='Age',)
    ap_ax.scatter(age_poli['politi_ideo'], age_poli['age'])
    ap_fig.savefig(os.getcwd() + "/visuals/age_politi.png")
    # age and media trust
    am_fig, am_ax = plt.subplots()
    am_ax.set(title="Age v. Media Trust",
              xlabel='Media Trust',
              ylabel='Age')
    am_ax.xaxis.set_major_locator(MaxNLocator(integer=True)) # forces integer plots
    am_ax.scatter(age_media['media_trust'], age_media['age'])
    am_fig.savefig(os.getcwd() + "/visuals/age_media.png")
    # political ideology and media trust
    pm_fig, pm_ax = plt.subplots()
    pm_ax.set(title="Political Ideology v. Media Trust",
              xlabel='Political Ideology',
              ylabel='Media Trust')
    pm_ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    pm_ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    pm_ax.scatter(poli_media['politi_ideo'], poli_media['media_trust'], s=len(poli_media['politi_ideo']) * 0.1, alpha=0.10)
    pm_fig.savefig(os.getcwd() + "/visuals/politi_media.png")

    # qualitative
    # shared_found_later
    sh_fig, sh_ax = plt.subplots()
    sh_ax.set(title="Histogram of Whether Participants Unknowingly Shared Misinformation",
              xlabel='Shared Misinformation',
              ylabel='# of Participants')
    sh_ax.hist(shared_found_later)
    sh_fig.savefig(os.getcwd() + "/visuals/shared_found_later.png")
    # education
    edu_fig, edu_ax = plt.subplots()
    edu_ax.set(title="Highest Achieved Education Level",
               xlabel='Education Level',
               ylabel='# of Participants')
    edu_ax.tick_params(axis='x', labelrotation=15)
    plt.rcParams["font.size"] = 20
    plt.tight_layout()
    edu_ax.hist(education_stats)
    edu_fig.savefig(os.getcwd() + "/visuals/education_stats.png")


def visualize():
    compute_summary_statistics()
    correlation_generation()
    create_charts()