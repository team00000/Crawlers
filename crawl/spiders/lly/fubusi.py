# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
import re
# from crawl.spiders.base_redis_spider import BaseRredis
from crawl.items.shi_an_two_items import ShiantwoItem



class BiaoSpider(scrapy.Spider):
    name = 'fubusi'
    allowed_domains = []
    # redis_key = 'play_redis:start_urls'
    start_urls = ['http://finance.sina.com.cn/zt_d/2018fbszg500fhbbd/']

    def parse(self, response):
        sel = Selector(response)
        title = sel.css('tr td::text').extract()
        for i in title:
            print(i)

