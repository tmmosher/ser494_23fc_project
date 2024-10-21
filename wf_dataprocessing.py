"""
Author: Trenton Mosher
Description: Processes data generated in wf_datagen.py
"""

import os, csv

def process_cvd_misinfo_data():
    data_path = os.getcwd() + '\\data_original\\'
    output_path = os.getcwd() + '\\data_processing'
    print(data_path)
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
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    with open(output_path + "\\processed_cvs_misinfo.csv", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(csv_data)
    print("COVID misinfo munging done")

if __name__ == '__main__':
    process_cvd_misinfo_data()