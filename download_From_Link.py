"""
#gets all the doc files from the current directory
import sys
import os
import re

doc_list = sys.argv[1].split(',')
print(doc_list)

path = os.getcwd()

def link_extractor(doc):
    with open('sample.txt') as file:
            for line in file:
                
                print(urls)

for doc in doc_list:
    isExist = os.path.exists(doc)
    if(not isExist):
        print("illegal file name "+doc)
    else:
        link_extractor(doc)


"""

#downloads the file from url into current directory

import requests
url = 'https://codeload.github.com/fogleman/Minecraft/zip/master'

#download the file contents in binary format
r = requests.get(url)

#open method to open file on your system and write the contents
with open("minemaster1.zip","wb") as code:
    code.write(r.content)

import urllib

urllib.request.urlretrieve(url, "minemaster.zip")

