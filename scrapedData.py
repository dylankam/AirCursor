from icrawler.builtin import BingImageCrawler
positives=['hand pointing down'] 
negatives=['fist', 'left hand', 'right hand'] 

numPositives=300
numNegatives=500


for c in positives:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'p/{c.replace(" ",".")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=numPositives,offset=0)

for c in negatives:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'n/{c.replace(" ",".")}'})
    bing_crawler.crawl(keyword=c,filters=None,max_num=numNegatives,offset=0)