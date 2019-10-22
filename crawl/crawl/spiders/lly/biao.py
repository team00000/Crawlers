# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin





class BiaoSpider(scrapy.Spider):
    name = 'biao'
    allowed_domains = []
    start_urls = ['http://www.bidhome.com.cn/BiddingNoticeList.aspx']

    def parse(self, response):
        sel = Selector(response)
        link = sel.css('li.Title a::attr(href)').extract()
        for url in link:
            title_url = urljoin(response.url,url)
            # print(title_url)
            yield Request(url=title_url, callback=self.parse_eve)
        next_url = sel.xpath('//div[@class="Page"]/a[contains(text(),"下一页")]/@href').extract_first()
        last_url = sel.xpath('//div[@class="Page"]/a[contains(text(),"尾页")]/@href').extract_first()
        if next_url != last_url:
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url,callback=self.parse)



    def parse_eve(self,response):
        sel = Selector(response)
        title = ''.join(sel.css('span#TitleLbl::text').extract())
        tim = ''.join(sel.css('span#PublishDateLbl::text').extract())
        endtim = ''.join(sel.css('span#EndDateLbl::text').extract())
        addre = ''.join(sel.css('span#RegionLbl::text').extract())
        eve = ''.join(sel.css('div#DetBox ::text').re('\s+'))
        print(title)
        print(tim)
        print(endtim)
        print(addre)
        print(eve)