# tag2name

### Organize your music automatically with mp3 tags

With tag2name you can organize and rename your mp3 files using its id3 tag data.

Requirements
------------
python v 2.7 +

Usage
-----

python main.py [-r] [-i path_to_input_folder] [-o path_to_output_folder]

##### Optional parameters
-  -r: if we want to rename the file with the title id3tag
-  -i: an optional input folder should be specified (it will use tag2name/input if no folder is specified)
-  -o: an optional output folder should be specified (it will use tag2name/output if no folder is specified)

Log
---
When the proccess is finished you will find all the logs in this file: logfile.log