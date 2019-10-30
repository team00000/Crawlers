from scrapy import Spider,Selector,Request
from crawl.items.ZhaoBiao import ZhaoBiaoItem
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
class ZhaoBiaoSpider(Spider):
    name = "zhaobiao"
    start_urls = [
        'https://www.chinabidding.cn/zbxx/zbgg/'
    ]
    def parse(self, response):
        sel = Selector(response)
        print(response.url)
        xiang_urls = sel.xpath('//*[@id="list"]//tr/td/a/@href').extract()
        for xiang_url in xiang_urls:
            yield Request(url="https://www.chinabidding.cn/"+xiang_url,callback=self.parse_item)
        last_url = sel.xpath('//div[@id="pageZone"]/span[contains(text(),"尾页")]/@href').extract_first()
        next_url = sel.xpath('/div[@id="pageZone"]/span[contains(text(),"下一页")]/@href').extract_first()
        if next_url != last_url:
            next_url = urljoin(response.url, next_url)
            print('翻页链接:', next_url)
    def parse_item(self, response):
        sel = Selector(response)
        print(response.url)
        title = sel.xpath('//*[@id="main_dom"]/div/h1/text()').extract_first()
        hangye = sel.xpath('//*[@id="main_dom"]/div[1]/div[1]/div[1]/text()').extract_first()
        address = sel.xpath('//div[@class="fl xiab_1"]//a[2]/text()').extract_first()
        time = sel.xpath('//div[@class="fl xiab_1"]//span/text()').extract_first()
        nei = sel.xpath('//div[@class="xq_nr"]//p/text()').extract_first()
        i = ItemLoader(item=ZhaoBiaoItem(), response=response)
        i.add_value(field_name='title', value=title)
        i.add_value(field_name='hangye', value=hangye)
        i.add_value(field_name='address', value=address)
        i.add_value(field_name='time', value=time)
        i.add_value(field_name='nei',value=nei)
        yield i.load_item()
