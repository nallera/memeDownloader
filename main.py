from downloader import download_memes
from parser import parse_args

if __name__ == '__main__':
    args = parse_args()

    download_memes(args.url, args.folder, int(args.amount))
