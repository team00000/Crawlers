import scrapy,re
from scrapy import Spider
from scrapy import Selector,Request
from urllib.parse import urljoin
class Qikan(scrapy.Spider):
    name='qklw'
    start_urls = ['http://qikan.xmqikan.com/qikan/zhengzhifalv/']
    def parse(self, response):
        sel=Selector(response)
        li=response.xpath('//div[@class="lisrig"]/ul/li')
        # print(response.url)
        #翻页
        next_urls = response.xpath('//div[@class="plist"]/ul/li[4]/a[contains(text(),"下一页")]/@href').extract_first()
        # print(next_urls)
        # print(latest_url)
        for i in li:
            urls=i.css('a::attr(href)').extract_first()
            next_url = urljoin(response.url,urls)
            # print(next_url)
            yield Request(url=next_url,callback=self.parse_text)
        if next_urls:
            next_url = urljoin(response.url, next_urls)
            yield Request(url=next_url,callback=self.parse)
    def parse_text(self,response):
        sel = Selector(response)
        title=''.join(sel.css('dl dd strong::text').extract())
        laiyuan=''.join(response.xpath('//div[@class="qkinf mt15"]/div[2]/dl/text()').extract())
        txt=''.join(response.xpath('//div[@class="qkinf mt15"]/div[2]/text()').extract())
        print(title)
        print(laiyuan)
        print(txt)


