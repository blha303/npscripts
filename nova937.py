#!/usr/bin/env python3
from requests import get
from json import dumps
from sys import exit

from .util import get_itunes_info

__version__ = "1.0.0"
__author__ = "blha303 <stevensmith.ome@gmail.com>"
__location__ = "Perth, Western Australia"

def get_data():
    data = get("http://prod-filesbucket-7hmmorphht20.s3-ap-southeast-2.amazonaws.com/nova-player-history/nova937-current.json").json()
    moreinfo = get_itunes_info(data["artist_title"], data["song_title"])
    if not data["itunes_url"]:
        data["itunes_url"] = moreinfo["trackViewUrl"]
    if not data["album_title"]:
        data["album_title"] = moreinfo["collectionName"]
    return data


def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
