import webbrowser
import time


def get_fresh_meme():
    new = 2
    url = ("https://9gag.com/tag/fresh-meme?ref=search")
    webbrowser.open(url, new=new)


def main():
    get_fresh_meme()


if __name__ == '__main__':
    main()
