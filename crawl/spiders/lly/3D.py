# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem
import json
import pymongo
db = pymongo.MongoClient()['3dhu']['biao']



class BiaoSpider(scrapy.Spider):
    name = '3Dhu'
    allowed_domains = []
    start_urls = ['http://www.3dhoo.com/news']

    def parse(self, response):
        sel = Selector(response)
        li = sel.css('div#nn_0 ul li')
        for i in li:
            link = ''.join(i.css('div.new_postion a img::attr(src)').extract())
            title = ''.join(i.css('div.dybk_div a::text').extract())
            laiyuan = ''.join(i.css('div.date_div span.color_blue::text').extract()[0])
            tim = ''.join(i.css('div.date_div span::text').re('\d+-\d+-\d+\s\d+:\d+:\d+'))
            yueduliang = ''.join(i.css('div.date_div span.color_blue::text').extract()[1])
            every = ''.join(i.css('p.yd_p::text').extract())
            kword = ''.join(i.css('div.label_div span a::text').extract())
            print(link)
            print(title)
            print(laiyuan)
            print(tim)
            print(yueduliang)
            print(every)
            print(kword)
            db.insert({'url':link,'title':title,'laiyuan':laiyuan,'time':tim,'yueduliang':yueduliang,'every':every,'kword':kword})

            next_url = response.xpath('//div[@class="page"]/a[contains(text(),"下一页")]/@href').extract_first()
            rl = 'http://www.3dhoo.com/news/p-4.html'
            if next_url:
                next_url = urljoin(response.url, next_url)
                if next_url == rl:
                    continue
                yield Request(url=next_url, callback=self.parse)