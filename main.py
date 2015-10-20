__author__ = 'haas'

import os
import sys
from shutil import copyfile
from eyed3.mp3 import Mp3AudioFile

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        INPUT_DIR = sys.argv[1]
    if len(sys.argv) > 2:
        OUTPUT_DIR = sys.argv[2]

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    mp3_files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR,f))]
    for mp3_path in mp3_files:
        try:
            _path = os.path.join(INPUT_DIR, mp3_path)
            mp3_file = Mp3AudioFile(path=_path)

            _temp_dir = OUTPUT_DIR

            new_name = ''

            if mp3_file.tag.album and mp3_file.tag.album != '':
                # new_name += mp3_file.tag.album + '-'
                _temp_dir = os.path.join(_temp_dir, mp3_file.tag.album)

            if mp3_file.tag.artist and mp3_file.tag.artist != '':
                # new_name += mp3_file.tag.artist + '-'
                _temp_dir = os.path.join(_temp_dir, mp3_file.tag.artist)

            if not os.path.exists(_temp_dir):
                os.makedirs(_temp_dir)

            if mp3_file.tag.title and mp3_file.tag.title != '':
                # new_name += mp3_file.tag.title + '-'
                new_name += mp3_file.tag.title + '.mp3'

            if len(new_name) > 0:
                # new_name = new_name[:-1] + '.mp3'
                copyfile(_path, os.path.join(_temp_dir, new_name))
                print new_name
                print "\n"
        except Exception as ex:
            print ex



