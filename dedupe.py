import os
import json
from tqdm import tqdm

from imagededup.methods import PHash
from imagededup.utils import plot_duplicates

BASE_DIR = "/home/its-an-avacado/plex/data/pictures"


def main():
    # Get all dirs in BASE_DIR
    BASE_DIR_SUBDIRS = [item[0] for item in os.walk(BASE_DIR)]
    phasher = PHash()

    duplicate_image_mappings = []
    all_encodings = {}
    for pic_dir in tqdm([BASE_DIR] + BASE_DIR_SUBDIRS):

        # Generate encodings for all images in an image directory
        encodings = phasher.encode_images(image_dir=pic_dir)

        # Add subdir to all keys (encode_images defaults to key = <filename>; I want the full path as the key)
        full_path_encodings = {
            f'{pic_dir}/{k}': v for k, v in encodings.items()}

        all_encodings.update(full_path_encodings)

    # Save encodings to disk
    with open(f"{BASE_DIR}/pictures_encodings.json", 'w') as f:
        json.dump(all_encodings, f)

    # Find duplicates using the generated encodings
    duplicates = phasher.find_duplicates(encoding_map=all_encodings,
                                         outfile=f"{BASE_DIR}/pictures_duplicates.json")


if __name__ == "__main__":
    main()
