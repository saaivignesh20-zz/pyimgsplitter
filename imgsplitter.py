"""

    Basic Image Splitter
    Script Language Version: Python 3
    Written in IDLE Version: Python 3.7
    Version 1.0 | Open Source

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

"""

import tkinter as tk
import os
from PIL import Image
from tkinter import filedialog

# image crop function
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    # check if output directory exists on that path
    image_obj = Image.open(image_path)
    target_info = image_obj.info
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location, **target_info)
    #cropped_image.show()
    image_obj.close()

# show file dialog to open picture
root = tk.Tk()
root.withdraw()

# get file path into a variable
file_path = filedialog.askopenfilename(filetypes=[("JPEG File", "*.jpg;*.jpeg")], initialdir=os.getcwd())

# verify file path
if file_path == "":
    print("Exiting: No image path has been specified!")
    exit()

# get image dimensions
img = Image.open(file_path)
size_w = img.size[0]
size_h = img.size[1]
dpi = img.info['dpi']
img.close()
print("Loaded image of size %dx%d with dpi" %(size_w, size_h), str(dpi))

# get parameters
temp_split_X = 0
temp_split_Y = 0
split_W = 0
split_H = 0
splits = int(input("Enter no. of splits: "))
split_dir = int(input("Enter split direction (X->1, Y->2): "))
if split_dir == 1:
    temp_split_X = size_w // splits
    temp_split_Y = size_h
else:
    temp_split_X = size_w
    temp_split_Y = size_h // splits
split_X_input = input("Enter split width (leave empty for %d): "  %(temp_split_X))
if (split_X_input == ""):
    
    split_W = temp_split_X
else:
    split_W = int(split_X_input)
split_Y_input = input("Enter split width (leave empty for %d): " %(temp_split_Y))
if (split_Y_input == ""):
    split_H = temp_split_Y
else:
    split_H = int(split_Y_input)
split_prefix = input("Enter split prefix (no symbols): ")

temp_X = 0
temp_Y = 0
if not os.path.exists(os.path.dirname(file_path) + "/is_output"):
    os.mkdir(os.path.dirname(file_path) + "/is_output", 755)
for i in range(1, splits + 1):
    result_name = str(split_prefix) + str(i) + os.path.splitext(file_path)[1]
    crop(file_path, (temp_X, temp_Y, split_W + temp_X, split_H + temp_Y), os.path.dirname(file_path) + "/is_output/" + result_name)
    if split_dir == 1:
        temp_X += split_W
    elif split_dir == 2:
        temp_Y += split_H
    else:
        print("Invalid parameter value for split direction: ", split_dir)

print("Program terminated!")
