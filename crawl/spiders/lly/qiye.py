# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
import re
from crawl.items.qiye_ite import QiyeItem


class BiaoSpider(scrapy.Spider):
    name = 'maidanglao'
    allowed_domains = []
    start_urls = ['http://kfc.xixik.com/shop/beijing/mdl/']

    def parse(self, response):
        sel = Selector(response)
        title = sel.css('div.couponLeft div.moreShop h2::text').extract()
        name = sel.css('div.couponTitle1 a::attr(href)').extract()
        for i in name:
            link = urljoin(response.url,i)
            yield Request(url=link,callback=self.parse_every)

    def parse_every(self,response):
        sel = Selector(response)
        item = QiyeItem()
        item['name'] = sel.xpath('//*[@class="shopinfor_row"]/text()').extract()[0]
        item['phone'] = sel.xpath('//*[@class="shopinfor_row"]/text()').extract()[1]
        item['kword'] = ''.join(sel.xpath('//*[@class="shopinfor_row"]/a//text()').extract())
        every = ''.join(sel.css('div.shopabout ::text').extract())
        item['eve'] = re.sub('\s','',every)
        yield item


