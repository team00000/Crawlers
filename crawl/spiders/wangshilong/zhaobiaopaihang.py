from scrapy import Spider, Request, Selector
from crawl.items.wsl_zhaobiaopaihang import ZhaoBiaopaihang
from urllib.parse import urljoin
import re


class zhaobiao_paihang(Spider):
    name = "zhaobiaopaihang"
    start_urls = [
        'http://www.paihang360.com/ph/ping_ph.jsp?info_type=GYPBD'
    ]

    def parse(self, response):
        # 所属行业
        # hangye = response.css('div.con1_txt p::text').re(r'所属行业：(.*)?来源：')
        # 详情页链接
        detail_urls = response.xpath('//h1/a/@href').extract()
        for detail_url in detail_urls:
            detail_url = urljoin(response.url, detail_url)
            yield Request(url=detail_url, callback=self.parse_content)


        # 翻页链接
        if response.xpath('//div[@align="center"]/a/font[contains(text(),"下一页")]/../@href').extract_first():
            next_url = response.xpath('//div[@align="center"]/a/font[contains(text(),"下一页")]/../@href').extract_first()
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse)


    def parse_content(self, response):
        item = ZhaoBiaopaihang()
        sel = Selector(response)
        item['title'] = sel.xpath('//p[@class="style5"]/text()').extract_first()
        item['source'] = sel.xpath('//p/span[@class="style7"]/text()').extract_first()
        item['author'] = sel.css('span.style6::text').re(r'作者：(.*)?')
        item['readci'] = sel.xpath('//p/span[@class="style8"][1]/text()').re(r'\d+')
        item['time'] = sel.xpath('//p/span[@class="style8"][2]/text()').re(r'\d+-\d+-\d+')
        text = response.xpath('//div[@class="c_con1"]//text()').extract()
        item['text'] = ''.join(text).strip()
        yield item
