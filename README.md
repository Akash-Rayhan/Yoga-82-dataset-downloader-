# Yoga-82-dataset-downloader-
This is a Python script for downloading images from a list of URLs contained in text files. The script uses the `multiprocessing` module to download the images concurrently, which can significantly speed up the download process.

## Requirements

The script requires Python 3.x and the following packages:

- `os`
- `csv`
- `urllib.request`
- `glob`
- `multiprocessing`
- `argparse`

## Usage

To use the script, you need to provide the path to the directory containing the text files with the image URLs. The text files should have the extension `.txt` and should contain one URL per line, separated by tabs. Here's an example:
`image1_url image1_label`
`image2_url image2_label`
`image3_url image3_label`

The script will create a subdirectory with the same name as the text file for each text file found in the directory, and download the images to the corresponding subdirectory. For example, if you have a text file named `yoga.txt` containing URLs for yoga images, the script will create a directory named `yoga` and download the images to that directory.
To download the images, simply run the `main.py` script with the following command:
`python main.py /path/to/directory/ --processes 4`

You can adjust the number of worker processes used for downloading the images by changing the `processes` argument in the `Pool` constructor.
