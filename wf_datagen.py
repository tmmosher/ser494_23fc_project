"""
Author: Trenton Mosher
Description: Acquires data from internet and unpacks it in local storage.
"""
# site url for download is https://zenodo.org/records/4557828/files/covid-misinfo-videos.csv.gz?download=1

"""Site URLs for misinfo summary data 
1. https://osf.io/download/6pdxw/
2. https://osf.io/download/6cj7t/
3. https://osf.io/download/7zshu/
4. https://osf.io/download/2aqhj/
"""

import os

current_dir = os.getcwd()

def get_data_cvd_misinfo(url):
    import requests
    if not os.path.isdir(current_dir + "/data_original"):
        os.makedirs(current_dir + "/data_original")
    if not os.path.isfile(current_dir + "/data_original/cvd_misinfo_data.csv.gz"):
        response = requests.get(url)
        if response.status_code == 200:
            import gzip
            # save response content to file
            if not os.path.isfile(current_dir + "/data_original/cvd_misinfo_data.csv.gz"):
                with open(current_dir + "/data_original/cvd_misinfo_data.csv.gz", 'wb') as f:
                    f.write(response.content)
                with open(current_dir + "/data_original/cvd_misinfo_data.csv.gz", 'rb') as f:
                    file_content = gzip.decompress(f.read())
                with open (current_dir + "/data_original/cvd_misinfo_data.csv", 'wb') as f:
                    f.write(file_content)
                print("Finished COVID misinfo download")
        else:
            print("URL download request unsuccessful.")
    else:
        print("COVID misinformation files already present, skipping download.")

def get_data_sharing_misinfo(url, val):
    # most of this code will be very similar until reading of the data
    import requests
    if not os.path.isdir(current_dir + "/data_original"):
        os.makedirs(current_dir + "/data_original")
    if not os.path.isfile(current_dir + f"/data_original/misinfo_study{val}.sav"):
        response = requests.get(url)
        if response.status_code == 200:
            import pandas as pd
            #download the original file as a .sav (we can keep it, but don't really need it)
            with open(current_dir + f"/data_original/misinfo_study{val}.sav", 'wb') as f:
                f.write(response.content)
            #convert to a .csv
            file_content = pd.read_spss(current_dir + f"/data_original/misinfo_study{val}.sav")
            with open(current_dir + f"/data_original/misinfo_study{val}.csv", 'wb') as f:
                file_content.to_csv(f, index=False)
            print(f"Finished misinformation sharing study file {val}")
        else:
            print("URL download request unsuccessful.")
    else:
        print(f"Misinfo sharing study {val} already present, skipping download.")

def generate():
    # download and process all files
    #cvd_misinfo_url = "https://zenodo.org/records/4557828/files/covid-misinfo-videos.csv.gz?download=1"
    #get_data_cvd_misinfo(cvd_misinfo_url)
    osf_summ_data_1 = "https://osf.io/download/6pdxw/"
    get_data_sharing_misinfo(osf_summ_data_1, 1)
    osf_summ_data_2 = "https://osf.io/download/6cj7t/"
    get_data_sharing_misinfo(osf_summ_data_2, 2)
    osf_summ_data_3 = "https://osf.io/download/7zshu/"
    get_data_sharing_misinfo(osf_summ_data_3, 3)
    osf_summ_data_4 = "https://osf.io/download/2aqhj/"
    get_data_sharing_misinfo(osf_summ_data_4, 4)