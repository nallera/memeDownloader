# Meme downloader project

#### This is a program that downloads meme images from canihascheezburger, and you can indicate how many images to download, and how many simultaneous threads to have.

## Execution parameters:
- -u/--baseurl: is the base url to download the memes from
- -f/--folder is the local folder where the files will be downloaded to
- -a/--amount is the amount of memes to download
- -w/--workers is the amount of simultaneous threads

## Testing strategy

- Unit tests aren't very useful in the current state of the project
- Integration tests can be designed using a mock server that returns a mock html, and another mock server returning image data