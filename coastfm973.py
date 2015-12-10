#!/usr/bin/env python3
from json import dumps
from sys import exit
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup

from .util import get_itunes_info

__version__ = "1.0.0"
__author__ = "blha303 <stevensmith.ome@gmail.com>"
__location__ = "Mandurah, Western Australia"

def get_data():
    info_html = urlopen("http://marci1368.getmarci.com").read()
    div = Soup(info_html, "html.parser").find('div', {'id': 'letterbox1'})
    moreinfo = get_itunes_info(div["data-artist"], div["data-title"])
    if not moreinfo:
        return {"artistName": div["data-artist"],
                "trackName": div["data-title"],
                "collectionName": div["data-album"]}
    return moreinfo

def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
