# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem
from crawl.items.play_items import PlayItem
from crawl.spiders.base_redis_spider import BaseRredis
from crawl.utils.dupefilter import RFPDupeFilter



class BiaoSpider(BaseRredis):
    name = 'play_redis'
    allowed_domains = []
    redis_key = 'play_redis:start_urls'
    start_urls = ['https://www.ali213.net/news/pingce/']

    def parse(self, response):
        sel = Selector(response)
        item = response(PlayItem)
        bod = sel.css('div.one_l_con')
        for i in bod:
            item['title'] = ''.join(i.css('div.one_l_con_tit a::text').extract())
            item['tim'] = ''.join(i.css('div.one_l_con_tag::text').extract())
            item['jianjie'] = ''.join(i.css('div.one_l_con_con::text').extract())
            item['kword'] = i.css('div.one_l_con_key span::text').extract()
            # for keyword in kword:
            #     print(keyword)
            item['url'] = ''.join(i.css('div.one_l_con_tit a::attr(href)').extract())
            yield Request(url=item['url'], callback=self.parse_every)
        latest_url = response.xpath('//div[@class="p_bar"]/a[contains(text(),"尾页")]/@href').extract_first()
        next_url = response.xpath('//div[@class="p_bar"]/a[contains(text(),"下页")]/@href').extract_first()
        if next_url != latest_url:
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse)

    def parse_every(self, response):
        sel = Selector(response)
        item = response(PlayItem)
        item['zuo'] = ''.join(sel.css('div#Content p::text').extract())
        next_url = response.xpath('//div[@class="page_fenye"]/span[@id="after_this_page"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_url:
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse_every)

