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
    artist = div["data-artist"]
    song = div["data-title"]
    album = div["data-album"]
    moreinfo = get_itunes_info(artist, song)
    return {"artist_title": artist, "song_title": song, "album_title": album if album else moreinfo["collectionName"], "itunes_url": moreinfo["trackViewUrl"]}
    

def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
