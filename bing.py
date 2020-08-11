from icrawler.builtin import BingImageCrawler
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
attractionList = ['택배상자']
attractionFolderList = ['nbox2']
 
for idx, val in enumerate(attractionList):
    bing_crawler = BingImageCrawler(
        feeder_threads=10,
        parser_threads=10,
        downloader_threads=10,
        storage={'root_dir': './data/'+attractionFolderList[idx]})
    bing_crawler.session.verify = False
    filters = dict(type='photo') #사진만
    # 키워드로 돌면서 1000장 크롤링
    bing_crawler.crawl(keyword=val,
                        min_size=(200,200),
                        filters=filters,
                        max_num=500,
                        file_idx_offset=0)