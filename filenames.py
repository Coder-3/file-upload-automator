import os
import hidden
import keyword

os.chdir(hidden.filesPath)
filenames = os.popen('ls')
filenamesString = filenames.read()
filenamesArray = filenamesString.split('\n')
# print(filenamesArray[0].replace('_', ' ')[-30:-4])