from icrawler.builtin import FlickrImageCrawler

attractionFolderList = ['box2', 'book2', 'fan2', 'monitor2', 'clothes2']
 
flickr_crawler = FlickrImageCrawler(
    apikey='9f1d3dc3057bf04e07fbb35e066743a8',
    feeder_threads=10,
    parser_threads=10,
    downloader_threads=10,
    storage={'root_dir': './data/'+attractionFolderList[4]})

flickr_crawler.crawl(max_num=50, tags='clothes', tag_mode='all')