# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem
import json


class BiaoSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = []
    start_urls = ['https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&b_id=70324&per_page=40']

    def parse(self, response):
        result = json.loads(response.text)
        data = result.get('data')
        item = data.get('items')
        for post in item:
            b_id = post.get('id')
            url = 'https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&b_id={}&per_page=40'.format(str(b_id))
            pos = post.get('post')
            title = pos['title']
            print(title)
            tim = pos['published_at']
            print(tim)
            eve = pos['summary']
            print(eve)
            user = pos['user']
            name = user['name']
            print(name)
            yield Request(url, callback=self.parse)



