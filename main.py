__author__ = 'haas'

import os
import sys
from shutil import copyfile
from eyed3.mp3 import Mp3AudioFile

import logging
log = logging.getLogger(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

if __name__ == "__main__":
    rename = False
    if len(sys.argv) > 1:
        i = 0
        for arg in sys.argv:
            if arg == '-i':
                INPUT_DIR = sys.argv[i + 1]
            if arg == '-o':
                OUTPUT_DIR = sys.argv[i + 1]
            if arg == '-r':
                rename = True
            i += 1

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    mp3_files = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR,f))]
    for mp3_name in mp3_files:
        if '.mp3' in mp3_name:
            mp3_name = mp3_name
            log.warning("Reading file: %s" % mp3_name)
            try:
                _path = os.path.join(INPUT_DIR, mp3_name)
                mp3_file = Mp3AudioFile(path=_path)

                _temp_dir = OUTPUT_DIR

                new_name = mp3_name

                if mp3_file.tag.artist and mp3_file.tag.artist != '':
                    _temp_dir = os.path.join(_temp_dir, mp3_file.tag.artist)

                if mp3_file.tag.album and mp3_file.tag.album != '':
                    _temp_dir = os.path.join(_temp_dir, mp3_file.tag.album)

                if not os.path.exists(_temp_dir):
                    os.makedirs(_temp_dir)

                if mp3_file.tag.title and mp3_file.tag.title != '':
                    if rename:
                        new_name = mp3_file.tag.title + '.mp3'

                log.warning("File name: %s" % new_name)

                if len(new_name) > 0:
                    copyfile(_path, os.path.join(_temp_dir, new_name))
            except Exception as ex:
                log.error("Error in file: %s" % mp3_name)
                log.error("Error is: %s" % str(ex))



