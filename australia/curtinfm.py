#!/usr/bin/env python3
from requests import get
from json import dumps
from sys import exit
from random import random

from ..util import get_itunes_info

__version__ = "1.0.0"
__author__ = "blha303 <stevensmith.ome@gmail.com>"
__name__ = "Curtin FM 100.1"
__location__ = "Bentley, Western Australia"
__player__ = "http://192.99.17.12:6192/stream"

def get_data():
    data = get("http://curtinfm.fastcast4u.com/info.php?get=player&rand=" + str(random())).json()
    moreinfo = get_itunes_info(data["artist"], data["title"])
    if not moreinfo:
        return {"artistName": data["artist"],
                "trackName": data["title"],
                "collectionName": data["albumname"]}
    return moreinfo


def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
