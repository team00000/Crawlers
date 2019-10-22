import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem


class BiaoSpidera(scrapy.Spider):
    name = 'zjy_biao'
    allowed_domains = []
    start_urls = ['http://www.shenhuabidding.com.cn/bidweb/001/001002/1.html']

    def parse(self, response):
        sel=Selector(response)
        urls=sel.css('li.right-item.clearfix div a::attr(href)')
        urls=set(urls)
        for i in list(urls):
            print(i)

