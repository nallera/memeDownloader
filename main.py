import logging

from downloader import download_memes
from parser import parse_args

if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(threadName)s: %(message)s",
                        level=logging.INFO, datefmt="%H:%M:%S")
    args = parse_args()

    download_memes(args.baseurl, args.folder, int(args.amount), int(args.workers))
