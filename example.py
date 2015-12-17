#!/usr/bin/env python3
# Imports for script output
from json import dumps
from sys import exit

# Imports for HTML parsing
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup

# Imports for JSON parsing
# from requests import get

# All scripts should be in country subdirectories so this resolves
from ..util import get_itunes_info

# 1.0.0 for first version, increment this number for future versions
__version__ = "1.0.0"
# Original script author. Can probably just be left to the git contributors
__author__ = "blha303 <stevensmith.ome@gmail.com>"
# The official station name
__name__ = "97.3 Coast FM"
# The approximate geographic location of the station's broadcast area, or broadcast origin if known
__location__ = "Mandurah, Western Australia"
# A direct playback URL. Can be obtained from the playlist file most radio stations provide
__player__ = "http://203.121.207.78:8000/"

def get_data():
    """ The main function for returning data. Returns a dict, either iTunes search result for the current song, or similarly-formatted artist/title/album (where available) """
    info_html = urlopen("http://marci1368.getmarci.com").read()
    div = Soup(info_html, "html.parser").find('div', {'id': 'letterbox1'})
    moreinfo = get_itunes_info(div["data-artist"], div["data-title"])
    if not moreinfo:
        return {"artistName": div["data-artist"],
                "trackName": div["data-title"],
                "collectionName": div["data-album"]}
    return moreinfo

def main():
    """ For if someone wants to just run a file directly. Not actually supported due to the ..util import. Can probably be removed """
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
