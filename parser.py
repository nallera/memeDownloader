import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="-u is the base url to download the memes from, -f is the local "
                                                 "folder where the files will be downloaded to, -a is the amount "
                                                 "of memes to download, -w is the amount of simultaneous threads")
    parser.add_argument("-u", "--baseurl", help="Meme page base url")
    parser.add_argument("-f", "--folder", help="Local folder path")
    parser.add_argument("-a", "--amount", help="Amount of memes to download")
    parser.add_argument("-w", "--workers", help="Amount of simultaneous threads")
    args = parser.parse_args()

    try:
        args.amount = int(args.amount)
    except ValueError:
        raise TypeError("--amount needs to be an integer")

    try:
        args.workers = int(args.workers)
    except ValueError:
        raise TypeError("--workers needs to be an integer")

    if args.workers < 1 or args.workers > 5:
        raise ValueError("--workers needs to be greater than 0 and less than 6")

    return args
