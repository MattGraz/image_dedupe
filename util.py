import json


def _get_dupe_photos_dict():
    with open("pictures_duplicates.json", 'r') as f:
        dupes = json.load(f)

    # Remove photos with no dupes
    dupes = {k: v for k, v in dupes.items() if v != []}

    return dupes
