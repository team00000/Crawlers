import scrapy
from scrapy.loader import ItemLoader
from urllib.parse import urljoin
from crawl.items.month import MonthItem1
class News(scrapy.Spider):
    name = 'news1'
    start_urls = [
        'https://36kr.com/information/web_news'
    ]
    def parse(self, response):
        sel = scrapy.Selector(response)
        print(response.url)
        xiang_urls = sel.xpath('//div[@class="information-flow-list"]//div/a/@href').extract()
        print(xiang_urls)
        for xiang_url in xiang_urls:
            yield scrapy.Request(url=xiang_url,callback=self.parse_item)
    def parse_item(self,response):
        sel = scrapy.Selector(response)
        print(response.url)
        title = sel.xpath('//div[@class="common-width"]//h1/text()').extract_first()
        zuozhe = sel.xpath('//div[@class="article-footer-txt"]//p/text()').extract_first()
        zhengwen = sel.xpath('//div[@class="common-width margin-bottom-20"]//p/text()').extract_first()
        time = sel.xpath('//div[@class="article-title-icon common-width margin-bottom-40"]//span[2]/text()').extract_first()
        i = ItemLoader(item=MonthItem1(), response=response)
        i.add_value(field_name='title', value=title)
        i.add_value(field_name='zuozhe', value=zuozhe)
        i.add_value(field_name='zhengwen', value=zhengwen)
        i.add_value(field_name='time', value=time)
        yield i.load_item()
