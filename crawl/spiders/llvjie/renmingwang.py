import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.lj_renmingwang import RenMingWang
import re

class PersonxiangSpiderSpider(scrapy.Spider):
    name = 'renming'
    allowed_domains = []
    start_urls = ['http://politics.people.com.cn/']

    def parse(self, response):
        sel = Selector(response)
        title = sel.css('h5 a::attr(href)').extract()
        for tit in title:
            title_url = urljoin(response.url, tit)
            print(title_url)
            yield Request(url=title_url,callback=self.every_xiang)

        next_url = sel.xpath('//div[@class="page_n clearfix"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_url:
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse)

    def every_xiang(self,response):
        item = RenMingWang()
        sel = Selector(response)
        title = sel.css('h1::text').extract_first()
        print(title)
        kw = sel.css('div.box01 ::text').extract()
        for key in kw:
            kword = re.sub('\s','',key)
        every = sel.css('div#rwb_zw p::text').extract()
        print(every)
        for eve in every:
            yield item
