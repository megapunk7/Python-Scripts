#change direcoty to ATBSWP
#walk through the tree, and loop files over it
#take files with .txt extension and readline
#finally compile it all into one file

import os

path = 'E:\Programming\Automate the Boring Stuff with Python Programming'
text_file = open('C:\\Users\\Dell\\Documents\\Recap.txt', 'w')
for folder, subfolders, filename in sorted(os.walk(path)):
    os.chdir(folder)
    for file in filename:
        if file.endswith('.txt'):
            recap_file = open(file)
            contents = recap_file.readlines()
            text_file.write(file+'\n')
            text_file.write(''.join(contents)+'\n\n')
    
text_file.close()