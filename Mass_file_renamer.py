# This program will rename files in a folder sequentially in numeric order. 

import os

path = input("Enter the folder directory: ")
os.chdir(path)

for i, file in enumerate(sorted(os.listdir(path))):
    if '.mp4' in file:
        ext = file[len(file)-4:]
        newname = file[:20] + str(i+1) + ext
        os.rename(file, newname)