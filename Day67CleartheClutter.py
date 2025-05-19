# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all the way till n.png 
# where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png


import os

folder_path = '/path/to/your/folder'
new_name_prefix = 'file_'  # or whatever pattern you want

files = os.listdir(folder_path)

for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    extension = os.path.splitext(filename)[1]  # Keep the file extension
    new_filename = f"{new_name_prefix}{index + 1}{extension}"
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)