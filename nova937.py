#!/usr/bin/python2
import urllib, json, sys


def main():
    print urllib.urlopen("http://prod-filesbucket-7hmmorphht20.s3-ap-southeast-2.amazonaws.com/nova-player-history/nova937-current.json").read()
    return 0

if __name__ == "__main__":
    sys.exit(main())
