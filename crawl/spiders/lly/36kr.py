# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem
import json
import pymongo
db = pymongo.MongoClient()['36k']['biao']


class BiaoSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = []
    start_urls = ['https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&per_page=40']

    def parse(self, response):
        result = json.loads(response.text)
        data = result.get('data')
        item = data.get('items')
        for post in item:
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
            for i in db.find({'title':title,'time':tim,'every':eve,'name':name}):
                break
            else:
                db.insert({'title':title,'time':tim,'every':eve,'name':name})



