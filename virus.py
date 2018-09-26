import webbrowser
import time


def meme_virus(how_many):
    new = 2
    for i in range(1):
        url = ("https://www.memecenter.com/")
        webbrowser.open(url, new=new)
        time.sleep(3)
    for i in range(how_many):
        url = ("https://www.memecenter.com/")
        webbrowser.open(url, new=new)
        time.sleep(1)


def main():
    meme_virus(20)


if __name__ == '__main__':
    main()
