#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
from sys import exit

def get_itunes_info(artist, song):
    """Returns the first result of searching iTunes for 'artist - song'.
       Returns an empty dict if no results returned"""
    data = get("https://itunes.apple.com/search",
               params={'term': "{} - {}".format(artist, song),
                       'entity': 'song'}).json()
    if data["results"]:
        return data["results"][0]
    return {}

if __name__ == "__main__":
    parser = ArgumentParser(prog="npscripts-util")
    parser.add_argument("artist", help="Artist name")
    parser.add_argument("song", help="Song name")
    args = parser.parse_args()
    print(dumps(get_itunes_info(args.artist, args.song)))
    exit(0)
