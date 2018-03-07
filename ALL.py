import os
import shutil

from heapq import nlargest
from operator import itemgetter


# The folder containing files.
directory = "e:\\videos\\"

# Get all files.
list = os.listdir(directory)

# Loop and add files to list.
pairs = []
for file in list:

    # Use join to get full file path.
    location = os.path.join(directory, file)

    # Get size and add to list of tuples.
    size = os.path.getsize(location)
    pairs.append((size, file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0],reverse=True)

# Display pairs.
i=1

for pair in pairs[:20]:
    print(pair)


# nlargest(5, pairs, key=itemgetter(1))





exten1 = ['.txt','.rar']
exten2 = ['.mp4']
source = "c:\\users\\vaibhav\\desktop"
destination = "e:\\text\\"
destination1 = "e:\\invid\\"
for files in os.listdir(source): #list all files and directories
    if os.path.isfile(os.path.join(source, files)): #is this a file
        if files.endswith(tuple(exten1)):
            shutil.move(os.path.join(source, files),destination) #move the file

for files in os.listdir(source): #list all files and directories
    if os.path.isfile(os.path.join(source, files)): #is this a file
        if files.endswith(tuple(exten2)):
            shutil.move(os.path.join(source, files),destination1) #move the file