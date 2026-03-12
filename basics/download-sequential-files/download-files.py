import os
import requests

# function to download and save a sequence of files
def download_files(firstItemUrl, outputDir):
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    retrieve = True
    base_filename = firstItemUrl.split('/')[-1].replace(' ', '_').split('.')[-2][:-3]
    index = firstItemUrl.split('/')[-1].replace(' ', '_').split('.')[-2][-3:]
    ext = firstItemUrl.split('/')[-1].replace(' ', '_').split('.')[-1]
    url_base = '/'.join(firstItemUrl.split('/')[:-1])
    while retrieve:
        filename = base_filename + index + '.' + ext
        url = url_base + '/' + filename
        filepath = os.path.join(outputDir, filename)
        r = requests.get(url, stream=True)
        print(f'Downloading {url}')
        if r.ok:
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
            index = '%03d' % (int(index) + 1)
            print(f'Saving {filename}')
        else:
            retrieve = False


if __name__ == '__main__':
    download_files('http://699340.youcanlearnit.net/image001.jpg', './output')