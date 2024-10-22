"""
Author: Trenton Mosher
Description: Compute summary statistics of data
"""

import os, csv, numpy as np
from statistics import median


def compute_summary_statistics():
    if not os.path.isdir(os.getcwd() + "\\data_processing") or not os.path.isfile(os.getcwd() + "\\data_processing\\processed_misinfo_sharing_combined.csv"):
        print("Failed to find processed data files")
        return None
    csv_data = []

    # extract csv data

    with open(os.getcwd() + "\\data_processing\\processed_misinfo_sharing_combined.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_data.append(row)

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
        if row[8] not in quality_dict:
            quality_dict[row[9]] = 1
        else:
            quality_dict[row[9]] += 1
    freq_val_shared = "Yes" if quality_dict["Yes"] > quality_dict["No"] else "No"
    freq_least_shared = "No" if quality_dict["Yes"] > quality_dict["No"] else "Yes"

    # check education stats
    quality_dict.clear()
    for row in csv_data:
        if row[2] not in quality_dict:
            quality_dict[row[2]] = 1
        else:
            quality_dict[row[2]] += 1
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
    age_stats["max"] = max(csv_data, key=lambda x: x[3])[3]
    age_stats["min"] = min(csv_data, key=lambda x: x[3])[3]
    age_stats["median"] = csv_data[int(len(csv_data) / 2)][3] # the misinfo study file is already sorted by age, so pulling median from the middle is valid

    csv_data.sort(key=lambda x: x[5], reverse=True) # sort by political ideology

    # politi_ideo
    politi_ideo_stats["max"] = max(csv_data, key=lambda x: x[5])[5]
    politi_ideo_stats["min"] = min(csv_data, key=lambda x: x[5])[5]
    politi_ideo_stats["median"] = csv_data[int(len(csv_data) / 2)][5]

    csv_data.sort(key=lambda x: x[6], reverse=True) # sort by trust level

    # media_trust
    media_trust_stats["max"] = max(csv_data, key=lambda x: x[6])[6]
    media_trust_stats["min"] = min(csv_data, key=lambda x: x[6])[6]
    media_trust_stats["median"] = csv_data[int(len(csv_data) / 2)][6]

    # write output values

    with open(os.getcwd() + "\\data_processing\\summary.txt", "w", encoding='utf-8') as file:
        file.write(f"Summary Statistics:\nCategorical\n'shared_found_later': 2 Categories. Most frequent was '{freq_val_shared}'. Least frequent was '{freq_least_shared}'.\n")
        file.write(f"education: {categories_count} Categories. Most frequent was '{freq_val_edu}'. Least frequent was '{freq_least_edu}'.\n")
        file.write(f"Quantitative\nage: Minimum: {age_stats['min']}, Maximum: {age_stats['max']}, Median: {age_stats["median"]}.\n")
        file.write(f"politi_ideo: Minimum: {politi_ideo_stats['min']}, Maximum: {politi_ideo_stats['max']}, Median: {politi_ideo_stats["median"]}.\n")
        file.write(f"media_trust: Minimum: {media_trust_stats['min']}, Maximum: {media_trust_stats['max']}, Median: {media_trust_stats['median']}.\n")