#!/usr/bin/env python3
from requests import get
from json import dumps
from sys import exit

from ..util import get_itunes_info

__version__ = "1.0.0"
__author__ = "blha303 <stevensmith.ome@gmail.com>"
__name__ = "Triple J"
__location__ = "Australia"
__player__ = "http://live-radio01.mediahubaustralia.com/2TJW/mp3/"


def get_data(raw=False):
    data = get("http://music.abcradio.net.au/api/v1/plays/triplej/now.json").json()["now"]["recording"]
    if raw:
        return data
    for a in data["artists"]:
        if a["type"] == "primary":
            artist = a["name"]
    moreinfo = get_itunes_info(artist, data["title"])
    if not moreinfo:
        return {"artistName": artist,
                "trackName": data["title"],
                "collectionName": data["releases"][0]["title"]}
    return moreinfo

def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
