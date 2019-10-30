# list = [1,2,3,4,5]
# list1=[]
# list2=[]
# for i in list:
#     a = i*i
#     i += 1
#     list1.append(a)
# print(list1)
# for j in list1:
#     if j>=10:
#         list2.append(j)
# print(list2)
import scrapy
from scrapy.loader import ItemLoader
from urllib.parse import urljoin
from crawl.items.month import MonthItem
class News(scrapy.Spider):
    name = 'news'
    start_urls = [
        'http://www.3dhoo.com/news'
    ]
    def parse(self, response):
        sel = scrapy.Selector(response)
        print(response.url)
        xiang_urls = sel.xpath('//*[@id="nn_0"]//a/@href').extract()
        print(xiang_urls)
        for xiang_url in xiang_urls:
            yield scrapy.Request(url=xiang_url,callback=self.parse_item)
        last_url = sel.xpath('//div[@class="page"]/a[contains(text(),"尾页")]/@href').extract_first()
        next_url = sel.xpath('/div[@class="page"]/a[contains(text(),"下一页")]/@href').extract_first()
        if next_url != last_url:
            next_url = urljoin(response.url, next_url)
            print('翻页链接:', next_url)
    def parse_item(self,response):
        sel = scrapy.Selector(response)
        print(response.url)
        title = sel.xpath('//div[@class="news_title"]//h2/text()').extract_first()
        tupian = sel.xpath('//div[@id="main"]//img/@src').extract_first()
        laiyuan = sel.xpath('//div[@class="editor_div"]//span/text()').extract_first()
        time = sel.xpath('//div[@class="date_div"]//span[2]/text()').extract_first()
        yueduliang = sel.xpath('//div[@class="date_div"]//span[3]/text()').extract_first()
        daodu = sel.xpath('//div[@class="review_div"]//p/text()').extract_first()
        biaoqian = sel.xpath('//div[@class="news_title"]//span/text()').extract_first()
        i = ItemLoader(item=MonthItem(), response=response)
        i.add_value(field_name='title', value=title)
        i.add_value(field_name='tupian', value=tupian)
        i.add_value(field_name='laiyuan', value=laiyuan)
        i.add_value(field_name='time', value=time)
        i.add_value(field_name='yueduliang', value=yueduliang)
        i.add_value(field_name='daodu', value=daodu)
        i.add_value(field_name='biaoqian', value=biaoqian)
        yield i.load_item()
