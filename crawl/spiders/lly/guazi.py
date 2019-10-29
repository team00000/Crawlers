# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem
from scrapy_redis.spiders import RedisSpider,RedisCrawlSpider,RedisMixin

# from tutorial.tutorial.items import TutorialItem


class BiaoSpider(RedisCrawlSpider):
    name = 'twocar'
    allowed_domains = []
    redis_key = 'twocar:start_urls'
    start_urls = ['https://www.ali213.net/news/pingce/']




    def parse(self, response):
        sel = Selector(response)
        title = sel.xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a/text()').extract()
        print(title)

