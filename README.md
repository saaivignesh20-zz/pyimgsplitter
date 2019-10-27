# pyimgsplitter

This is a script written in Python 3 to split image files based on number of 
splits and the image's resolution. The image is equally splitted, so it is
best suited for use with equally spaced graphics (like image sprites in
games).

I wrote this script to easily split my scanned images for splitting multiple
identical proof of identities (like Income Tax Cards in Order). I made many
initial revisions and made this script stable enough for uploading in GitHub.

Please feel free to use without any hesitations and report bugs (if any) to
saaivignesh20@gmail.com (or) commit the changes yourself in this repo itself
so that it will be useful to others. Don't hesitate to add some features too!

Hope you find this script useful.

## Installation
```
pip3 install -r requirements.txt
```

## Usage
Split ~/Pictures/my_image.png into 2 rows and 3 columns
```
python3 imagesplitter.py ~/Pictures/my_image.png --style=23
```
A folder with generated images will be created on CWD  
Split my_image.png into 2 rows and 3 columns and save it to ~/Pictures/buf
```
python3 imagesplitter.py my_image.png --style=23 -o ~/Pictures/buf
```

## Status
No GUI and barebones functionality.  
