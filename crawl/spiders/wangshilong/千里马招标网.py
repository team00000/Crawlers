from scrapy import Selector, Spider
from scrapy.spiders.crawl import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor

class qianbiao(CrawlSpider):
    name = "qianbiao"
    start_urls = ['http://www.qianlima.com/']
    rules = {
        Rule(LinkExtractor(allow=r'http://www.qianlima.com/zb/detail/\d+_\d+.html'), follow=True, callback='content')
    }

    def content(self, response):
        pass
