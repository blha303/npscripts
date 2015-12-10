#!/usr/bin/env python3
from requests import get
from json import dumps
from sys import exit
from random import random

from .util import get_itunes_info

__version__ = "1.0.0"
__author__ = "blha303 <stevensmith.ome@gmail.com>"
__location__ = "Bentley, Western Australia"

def get_data():
    data = get("http://curtinfm.fastcast4u.com/info.php?get=player&rand=" + str(random())).json()
    moreinfo = get_itunes_info(data["artist"], data["title"])
    if moreinfo:
        data["itunes_url"] = moreinfo["trackViewUrl"]
        data["album_title"] = data["albumname"] if data["albumname"] else moreinfo["collectionName"]
    return data


def main():
    print(dumps(get_data()))
    return 0

if __name__ == "__main__":
    exit(main())
