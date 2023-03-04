import glob
import os
import csv
import urllib.request
import multiprocessing
import argparse

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def download_images(file):
    """
    Download images from URLs in a text file.

    :param file: the path to the text file containing image URLs
    """
    count = 1
    # split the "filename" and ".txt" 
    split_text = os.path.splitext(file)
    name = split_text[0]
    # create folder of the class_name
    if not os.path.exists(name):
        os.mkdir(name)
    # open the .txt file text file contains all the images links
    print("{name} images are downloading".format(name=name))
    with open(file, "r") as f:
        line = csv.reader(f, delimiter='\t')
        for i in line:
            url = i[1]
            filename = name+"/"+str(count)+".jpg"
            try:
                if not os.path.exists(filename):
                    urllib.request.urlretrieve(url=url, filename=filename)
                count += 1
            except:
                pass
    print("{name} download completed".format(name=name))

if __name__ == '__main__':
     # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', type=str,help='Directory path containing text files with image URLs')
    parser.add_argument('--processes', type=int, default=multiprocessing.cpu_count(), help='Number of processes to use for downloading')
    args = parser.parse_args()

    # Find text files in directory
    files = glob.glob(args.dir_path + "*.txt")

    # Download images from each text file concurrently
    with multiprocessing.Pool(args.processes) as pool:
        pool.map(download_images, files)




