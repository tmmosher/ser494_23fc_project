"""
Author: Trenton Mosher
Description: Acquires data from internet and unpacks it in local storage.
"""

# site url for download is https://zenodo.org/records/4557828/files/covid-misinfo-videos.csv.gz?download=1

def get_data(url):
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        import os
        os.makedirs("/data_original")
        with response.content as f:
            import shutil
            print(f"{f}")
            try:
                shutil.move(f"/{f}", f"/data_original/{f}")
                shutil.unpack_archive(f"/data_original/{f}", f"/data_original/{f}")
            except:
                pass
    else:
        print("Unsuccessful response code received")

if __name__ == "__main__":
    url = "https://zenodo.org/records/4557828/files/covid-misinfo-videos.csv.gz?download=1"
    get_data(url)