# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lly_biao import ZhaobiaoItem


class BiaoSpider(scrapy.Spider):
    name = 'play'
    allowed_domains = []
    start_urls = ['https://www.ali213.net/news/pingce/']

    def parse(self, response):
        sel = Selector(response)
        bod = sel.css('div.one_l_con')
        for i in bod:
            title = ''.join(i.css('div.one_l_con_tit a::text').extract())
            # print(title)
            tim = ''.join(i.css('div.one_l_con_tag::text').extract())
            # print(tim)
            jianjie = ''.join(i.css('div.one_l_con_con::text').extract())
            # print(jianjie)
            kword = i.css('div.one_l_con_key span::text').extract()
            # for keyword in kword:
            #     print(keyword)
            url = ''.join(i.css('div.one_l_con_tit a::attr(href)').extract())
            # print(url)
            yield Request(url=url,callback=self.parse_every)
        # latest_url = response.xpath('//div[@class="p_bar"]/a[contains(text(),"尾页")]/@href').extract_first()
        # next_url = response.xpath('//div[@class="p_bar"]/a[contains(text(),"下页")]/@href').extract_first()
        # if next_url != latest_url:
        #     next_url = urljoin(response.url, next_url)
        #     yield Request(url=next_url, callback=self.parse)

    def parse_every(self,response):
        sel = Selector(response)
        zuo = ''.join(sel.css('div#Content p::text').extract())
        print(zuo)
        # latest_url = response.xpath('//div[@class="p_bar"]/a[contains(text(),"尾页")]/@href').extract_first()
        next_url = response.xpath('//div[@class="page_fenye"]/span[@id="after_this_page"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_url:
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse_every)

