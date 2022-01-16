import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="-u is the url to download the memes from, -f is the local folder "
                                                 "where the files will be downloaded to, -a is the amount of "
                                                 "memes to download")
    parser.add_argument("-u", "--url", help="Meme page url")
    parser.add_argument("-f", "--folder", help="Local folder path")
    parser.add_argument("-a", "--amount", help="Amount of memes to download")
    args = parser.parse_args()

    try:
        args.amount = int(args.amount)
    except ValueError:
        raise TypeError("--amount needs to be an integer")

    return args
