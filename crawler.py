from bs4 import BeautifulSoup
import requests
import urllib
import urllib3
import os
from os.path import os
import html5lib
import codecs

count = 28
index = 1
max_count = 1000
dataDir = "./data"
querySet = ['clothes', 'monitor', 'book', 'box', 'fan']

def get_soup (url, header):
    return BeautifulSoup(urllib3.urlopen(urllib3.Request(url, headers = header)))

if not os.path.isdir(dataDir):
    os.mkdir(dataDir)

for query in querySet:
    image_naming = query
    query = query.split()
    tempDirName = '_'.join(query)
    query ='+'.join(query)
    isQueryKorean = False

    targetDir = dataDir + tempDirName

    try:
        if not os.path.isdir(targetDir):
            os.mkdir(targetDir)
    except:
        isQueryKorean = True
        image_naming = "temp"
        targetDir = dataDir + "temp"
        dirNum = 0
        while(True):
            tempTargetDir = targetDir + str(dirNum)
            dirNum += 1
            if not os.path.isdir(tempTargetDir):
                targetDir = tempTargetDir
                os.mkdir(targetDir)
                break
    
    index = 1

    for i in range(max_count/count):
        url = "http://www.bing.com/images/search?q=" + query + "&first=" + str(index) + "&count" + str(count) + "&FORM=HDRSC2"
        index = index + count
        print(url) 

        page = urllib.urlopen(url).read()
        soup = BeautifulSoup(page, 'html5lib')
        
        for img_temp in soup.find_all("a", "thumb"):
            img = img_temp.get('href')
            try:
                print(img)
                raw_img = urllib3.urlopen(img).read()
                cntr = len([i for i in os.listdir(targetDir) if image_naming in i]) + 1
                print(cntr)

                f = open(targetDir + "/" + image_naming + "_" + str(cntr) + ".jpg", "wb")
                f.write(raw_img)
                f.close()
            except:
                print("fail to download")
                
