# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
import re
# from crawl.spiders.base_redis_spider import BaseRredis
from crawl.items.shi_an_two_items import ShiantwoItem



class BiaoSpider(scrapy.Spider):
    name = 'shiantwo'
    allowed_domains = []
    # redis_key = 'play_redis:start_urls'
    start_urls = ['http://www.foodmate.net/foodsafe/knowledge/']

    def parse(self, response):
        sel = Selector(response)
        link = sel.css('ul li.catlist_li a::attr(href)').extract()
        for url in link:
            yield Request(url=url,callback=self.parse_every)

        #翻页
        next_url = response.xpath('//div[@class="pages"]/a[contains(text(),"»")]/@href').extract_first()
        if next_url:
            yield Request(url=next_url, callback=self.parse)

    def parse_every(self,response):
        sel = Selector(response)
        item = ShiantwoItem()
        item['title'] = ''.join(sel.css('h1.title::text').extract())
        item['tim'] = ''.join(sel.css('div.info::text').re('\d+-\d+-\d+'))
        item['laiyuan'] = ''.join(sel.css('div.info a::text').extract())
        item['zuozhe'] = ''.join(sel.css('div.info::text').re('作者：([\u4e00-\u9fa5]+)'))
        item['liuliang'] = ''.join(sel.css('div.info span#hits::text').extract())
        item['tishi'] = ''.join(sel.css('div.introduce ::text').extract())
        item['every'] = ''.join(sel.css('div.content div ::text').extract())
        item['keywords']= ''.join(sel.xpath('//meta[@name="keywords"]/@content').extract())
        print(item['title'])
        print(item['tim'])
        print(item['laiyuan'])
        print(item['zuozhe'])
        print(item['liuliang'])
        print(item['tishi'])
        print(item['every'])
        print(item['keywords'])
