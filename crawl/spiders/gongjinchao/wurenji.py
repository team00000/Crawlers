import scrapy_redis
from scrapy.loader import ItemLoader
from urllib.parse import urljoin
from crawl.items.wurenji import WuRenJiItem
class WuRenJiSpider(scrapy_redis):
    name = 'wurenji'
    start_urls = [
        'https://www.81uav.cn/uav-news/'
    ]
    def parse(self, response):
        pass
