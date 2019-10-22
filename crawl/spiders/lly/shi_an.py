# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
import re



class BiaoSpider(scrapy.Spider):
    name = 'shian'
    allowed_domains = []
    start_urls = ['http://www.cfsn.cn/front/web/']

    def parse(self, response):
        sel = Selector(response)
        url = sel.xpath('//*[@class="nav"]/div/ul/li/a/@href').extract()[1:]
        for link in url:
            yield Request(url=link,callback=self.parse_list)

    def parse_list(self,response):
        sel = Selector(response)
        url = sel.xpath('//*[@class="fl w655"]/div/ul/li/div/a/@href').extract()
        for link in url:
            yield Request(url=link,callback=self.parse_every)
        # weiye = sel.xpath('//div[@class="pageNum"]/a[contains(text(),"尾页")]/@href').re(r'page=(\d+)')[0]
        # wei = int(weiye)
        # for i in range(wei):



        # 翻页


        last_url = sel.css('div.pageNum a::attr(href)').extract()
        # page_num = re.findall('page=(\d+)', last_url)[0]  # 取到上面网址的pgnum的值（str）
        # next_page = int(page_num) + 1  # 转为int   递加
        # next_p = re.sub('page=(\d+)', 'page=' + str(next_page), last_url)  # 新数字替换掉之前的数字
        # # if next_p == last_url:
        # print(next_p)
        # # yield Request(url=next_p, callback=self.parse_list)



    def parse_every(self,response):
        sel = Selector(response)
        title = ''.join(sel.css('h2.title::text').extract())
        tim = ''.join(sel.css('div.msg div::text').re('\d+-\d+-\d+\s\d+:\d+'))
        address = ''.join(sel.css('div.msg div span::text').extract())
        bianji = ''.join(sel.css('div.msg div::text').re('编辑：([\u4e00-\u9fa5]+)'))
        every = ''.join(sel.css('div.content p ::text').extract())
        print(title)
        print(tim)
        print(address)
        print(bianji)
        print(every)

    #
    #
    # # next_url = sel.xpath('//div[@class="pageNum"]/a[contains(text(),r'')]/@href').extract_first()
    # # next_url = sel.xpath('//*[@class="pageNum"]/a/@href').re('http://www.cfsn.cn/front/web/site.hangye?hyid=1&page=(\d+)')
    # next_url = sel.css('div.pageNum a::attr(href)').extract()
    # print(next_url)
    # last_url = sel.xpath('//div[@class="pageNum"]/a[contains(text(),"尾页")]/@href').extract_first()
    # # if next_url != last_url:
    # #     next_url = urljoin(response.url, next_url)
    # #     yield Request(url=next_url, callback=self.parse_list)