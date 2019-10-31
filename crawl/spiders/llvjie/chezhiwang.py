from scrapy import Spider
from scrapy import Selector,Request
from crawl.items.lj_chezhiwang import TousuItem
from urllib.parse import urljoin
from scrapy.loader import ItemLoader

class CheZhiWang(Spider):
    name = 'chezhiwang'
    allowed_domains = []
    start_urls = ['http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml']
    #第一种方法
    def parse(self, response):
        sel = Selector(response)
        detail_urls = sel.css('tr td.tsjs a::attr(href)').extract()
        print(detail_urls)
        for detail_url in detail_urls:
            yield Request(url=detail_url,callback=self.parse_item)

    def parse_item(self,response):
        sel = Selector(response)
        title = sel.css('h1#newstitle::text').extract_first()
        print(title)
        if sel.xpath('//ul/li[@class="fir"]/span[contains(text(),"投诉编号")]/../text()').re('\d+'):
            id = sel.xpath('//ul/li[@class="fir"]/span[contains(text(),"投诉编号")]/../text()').re('\d+')[0]
            print(id)
        else:
            raise Exception("id is null")
        i = ItemLoader(item=TousuItem(), response=response)
        i.add_value(field_name='id', value=id)
        i.add_value(field_name='pinpai', value=title)
        yield i.load_item()

    #第二种方法
    # def parse(self, response):
    #     item = TousuItem()
    #     sel = Selector(response)
    #     for i in range(1,32):
    #         item['id'] = response.xpath('//div[@class="tslb_b"]/table/tr['+str(i)+']//text()').extract()
    #         latest_url = response.xpath('//div[@class="p_page"]/a[contains(text(),"尾页")]/@href').extract_first()
    #         next_url = response.xpath('//div[@class="p_page"]/a[contains(text(),"下一页")]/@href').extract_first()
    #         if latest_url != next_url:
    #             next_url = urljoin(response.url, next_url)
    #             print(item['id'])
    #             yield Request(url=next_url, callback=self.parse)
    #     detail_urls = sel.css('tr td.tsjs a::attr(href)').extract()
    #     for detail_url in detail_urls:
    #         yield Request(url=detail_url, callback=self.parse_item)
    # def parse_item(self,response):
    #     sel = Selector(response)
    #     title = sel.xpath('//*[@id="content"]/div[4]/div[2]/table//tr[1]/th[1]').extract()
    #     print(title)