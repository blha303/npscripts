#!/usr/bin/env python3
from requests import get
from json import dumps
from sys import exit

from .util import get_itunes_info

__version__ = "1.0.0"
__author__ = "blha303 <stevensmith.ome@gmail.com>"
__name__ = "Nova 937"
__location__ = "Perth, Western Australia"
__player__ = "http://streaming.novaentertainment.com.au/nova937"

def get_data():
    data = get("http://prod-filesbucket-7hmmorphht20.s3-ap-southeast-2.amazonaws.com/nova-player-history/nova937-current.json").json()
    moreinfo = get_itunes_info(data["artist_title"], data["song_title"])
    if not moreinfo:
        return {"artistName": data["artist_title"],
                "trackName": data["song_title"],
                "collectionName": data["album_title"],
                "trackViewUrl": data["itunes_url"]}
    return moreinfo


def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
