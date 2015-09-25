#!/usr/bin/python2
import urllib, json, sys


def main():
    artist, song = urllib.urlopen("http://www.coastlive.com.au/data.html").read().split("</strong> ")[1].strip().split(" - ")
    moreinfo = json.loads(urllib.urlopen("https://itunes.apple.com/search?" + urllib.urlencode({'term': "{} - {}".format(artist, song), 'entity': 'song'})).read())["results"][0]
    print json.dumps({"artist_title": artist, "song_title": song, "album_title": moreinfo["collectionName"], "itunes_url": moreinfo["trackViewUrl"]})
    return 0

if __name__ == "__main__":
    sys.exit(main())
