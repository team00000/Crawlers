# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
import re
# from crawl.spiders.base_redis_spider import BaseRredis
from crawl.items.shi_an_two_items import ShiantwoItem



class BiaoSpider(scrapy.Spider):
    name = 'lunwen'
    allowed_domains = []
    # redis_key = 'play_redis:start_urls'
    start_urls = ['https://www.lunwendata.com/']

    def parse(self, response):
        sel = Selector(response)
        bod = sel.css('div.index-main dl')
        for i in bod:
            title = ''.join(i.css('dt a strong::text').extract())
            # print(title)
            link = i.css('dd a::attr(href)').extract()
            for url in link:
                yield Request(url=url,callback=self.parse_every)

    def parse_every(self,response):
        sel = Selector(response)
        title = ''.join(sel.css('div#article h1::text').extract())
        tim = ''.join(sel.css('div#time::text').re('\d+-\d+-\d+'))
        chuchu = ''.join(sel.css('div#source a::text').extract())
        kkword_url = sel.css('div#content p img::attr(src)').extract()
        for one in kkword_url:
            first_link = urljoin('https://www.lunwendata.com',one)
            print(first_link)
        every = ''.join(sel.css('div#content p ::text').extract())
        print(title)
        print(tim)
        print(chuchu)
        print(every)