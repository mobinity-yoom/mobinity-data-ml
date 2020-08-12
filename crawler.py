from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import os
from icrawler.builtin import BingImageCrawler
import urllib3
import ssl

context = ssl._create_unverified_context()  # for urlopen verify
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Naver crawling
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
category = input('category name: ')
search = input('Word to search: ')
searchNum = int(input('Number to search: '))

url = baseUrl + quote_plus(search)
html = urlopen(url, context=context)
soup = bs(html, "html.parser")
image = soup.find_all(class_='_img')

baseDir = './data/train/' + category + '/'
targetName = search.split()
targetName = '_'.join(targetName)
targetDir = baseDir + targetName

if not os.path.isdir(targetDir):
    os.mkdir(targetDir)

for idx, img in enumerate(image):
    print(idx)
    imgSrc = img['data-source']
    with urlopen(imgSrc, context=context) as f:
        with open(targetDir + '/' + targetName + '_' + str(idx) + '.jpg','wb') as h:
            image = f.read()
            h.write(image)
    if idx > 50: break
print('Naver Crawling done.')

# Bing Crawling
bing_crawler = BingImageCrawler(feeder_threads=10,
                                parser_threads=10,
                                downloader_threads=10,
                                storage={'root_dir': targetDir})
bing_crawler.session.verify = False
filters = dict(type='photo') # only photo
bing_crawler.crawl(keyword=targetName,
                    min_size=(200,200),
                    filters=filters,
                    max_num=searchNum,
                    file_idx_offset='auto')