"""
Author: Trenton Mosher
Description: Processes data generated in wf_datagen.py
"""

import os, csv

def process_cvd_misinfo_data():
    data_path = os.getcwd() + '\\data_original\\'
    output_path = os.getcwd() + '\\data_processing'
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    if not os.path.isfile(output_path + '\\processed_cvs_misinfo.csv'):
        csv_data = []
        with open(data_path + "cvd_misinfo_data.csv", 'r', encoding='utf-8') as csvfile:
            for row in csv.reader(csvfile):
                csv_data.append(row)
        columns = csv_data[0] # keep the columns for writing back out later
        columns.append("num_twitter_shares")
        columns.append("num_facebook_shares")
        csv_data.remove(csv_data[0]) # delete the column row for processing
        for row in csv_data:
            if row[3] == "":
                row[3] = 0
            else:
                row[3] = int(row[3])
            if row[5] == "":
                row[5] = 0
            else:
                row[5] = int(row[5])
            row.append(f"{len(row[12].split(','))}")
            row.append(f"{len(row[13].split(','))}")
        with open(output_path + "\\processed_cvs_misinfo.csv", 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            writer.writerows(csv_data)
        print("COVID misinfo munging done")
    else:
        print("Munged .csv already present for COVID misinfo study. Please delete file before re-munging.")

def process_misinfo_sharing():
    data_path = os.getcwd() + '\\data_original\\'
    output_path = os.getcwd() + '\\data_processing'
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    # each misinfo study has unique column structure. To combine the data I want, I have to go over them all individually :/

    """
    Wanted structure for CSV file:
    Gender, country, education, age, occupation, poli_ideo, media_trust, 
    media_behavior, med_share, shared_found_later, shared_knowing
    """
    if not os.path.isfile(output_path + "\\processed_misinfo_sharing_combined.csv"):
        csv_data = []

        # collect data from individual studies for conglomeration

        with open(data_path + "misinfo_study1.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                row = [row[0], row[2], row[4], row[5], row[6], row[7], row[8],
                       row[9], row[10], row[11], row[12]]
                csv_data.append(row)
            csv_data.pop(0)
        with open(data_path + "misinfo_study2.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            delete_index = len(csv_data)
            for row in csv_reader:
                row = [row[0], row[3], row[5], row[6], row[7], row[8],
                       row[24], row[25], row[26], row[45], row[64]]
                csv_data.append(row)
            csv_data.pop(delete_index)
        with open(data_path + "misinfo_study3.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            delete_index = len(csv_data)
            for row in csv_reader:
                row = [row[0], row[2], row[5], row[6], row[7], row[9],
                       row[32], row[33], row[34], row[35], row[36]]
                csv_data.append(row)
            csv_data.pop(delete_index)
        with open(data_path + "misinfo_study4.csv", 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            delete_index = len(csv_data)
            for row in csv_reader:
                row = [row[2], row[4], row[6], row[7], row[8], row[10],
                       row[12], row[13], row[14], row[15], row[16]]
                csv_data.append(row)
            csv_data.pop(delete_index)

        # remove text from numerical data

        import re
        for row in csv_data:
            row[3] = int(float(row[3]))
            if re.match("^[1-7]$", row[5]):
                row[5] = int(row[5])
            else:
                row[5] = (int(re.search("[1-7]", row[5]).group()))
            if re.match("^[1-7]$", row[6]):
                row[6] = int(row[6])
            else:
                row[6] = (int(re.search("[1-7]", row[6]).group()))
            if re.match("^[1-7]$", row[7]):
                row[7] = int(row[7])
            else:
                row[7] = (int(re.search("[1-7]", row[7]).group()))
            if re.match("^[1-7]$", row[8]):
                row[8] = int(row[8])
            else:
                row[8] = (int(re.search("[1-7]", row[8]).group()))

        # sort by age for easier reading

        csv_data.sort(key=lambda x: x[3], reverse=True)

        # add the columns back in for the final product

        columns = ["gender", "country", "education", "age", "occupation", "polit_ideo", "media_trust",
            "media_behavior", "med_share", "shared_found_later", "shared_knowing"]
        csv_data.insert(0, columns)

        # write the file back out

        with open(output_path + "\\processed_misinfo_sharing_combined.csv", 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
        print("Misinfo sharing munging done")
    else:
        print("Munged .csv already present for misinfo sharing study. Please delete file before re-munging.")

def munge():
    process_cvd_misinfo_data()
    process_misinfo_sharing()

