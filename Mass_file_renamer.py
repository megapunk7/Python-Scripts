# This program will rename files in a folder sequentially in numeric order. 

import os

path = input("Enter the folder directory: ")
ext = input("Enter the extension of file you want to rename: ")
os.chdir(path)

for i, file in enumerate(sorted(os.listdir(path))):
    if ext in file:
        newname = file[:20] + str(i+1) + ext
        os.rename(file, newname)