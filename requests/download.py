import requests
# TODO tqdm


def download_file(url, filepath):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        #TODO multi-threaded download
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=4096):
                f.write(chunk)
        return 0
    else:
        return 1
