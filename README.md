npscripts
=========

A collection of scripts for getting radio now-playing information. Information is returned from an iTunes search for the song, or in that format if a result is not found.

New submissions welcomed!

    import npscripts.australia.triplej as triplej
    print("Now playing on {}: {} (Listen: {} )".format(
            triplej.__name__,
            "{artistName} - {trackName} (from {collectionName})".format(**triplej.get_data()),
            triplej.__player__
            )
         )
