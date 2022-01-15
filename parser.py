import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="-u is the url to download the memes from, -f is the local folder"
                                                 " where the files will be downloaded to")
    parser.add_argument("-u", "--url", help="Meme page url")
    parser.add_argument("-f", "--folder", help="Local folder path")
    return parser.parse_args()
