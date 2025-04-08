import os
import requests
# TODO tqdm

def download_file(url, local_filename):

    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        #TODO muilti-threaded download
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=4096):
                f.write(chunk)
        print(f"Downloaded {local_filename}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

if __name__ == "__main__":
    url = "https://blitsdl.blitsgames.com/jockstudio/JockStudio-Demo-Win.zip"
    local_filename = "file.txt"
    download_file(url, local_filename)