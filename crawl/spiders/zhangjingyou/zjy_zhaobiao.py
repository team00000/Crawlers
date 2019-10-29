import scrapy
from scrapy import Selector,Request
from urllib.parse import urljoin
from crawl.items.zjy_biao_item import ZhaoBiao
import re,time




class BiaoSpidera(scrapy.Spider):
    name = 'zjy_biao'
    allowed_domains = []
    start_urls = ['https://www.bibenet.com/search?pageNum=1']
    page=1
    custom_settings = {
        "DOWNLOAD_DELAY":'1'
    }

    def parse(self, response):
        sel=Selector(response)
        urls=sel.css('table.secondary_detail tr')
        for i in urls:
            a=i.css('td a::attr(href)').extract_first()
            if a:
                # url=urljoin(response.url,i)
                # time.sleep(1)
                # yield  Request(url=a,callback=self.xiangqing,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'})
                yield Request(url=a, callback=self.xiangqing,)
        next_url= response.url
        self.page+=1
        next_url=re.sub('\d+',str(self.page),next_url)
        if next_url and self.page<5:
            next_url=urljoin(response.url,next_url)
           # yield Request(url=next_url,callback=self.parse,headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'})
            yield Request(url=next_url, callback=self.parse)
    def xiangqing(self,response):
        sel=Selector(response)
        item=ZhaoBiao()
        item['title'] =  sel.css('h1.detailtitle::attr(title)').extract_first()
        # item['start_time'] = ''.join(sel.css('p.info-sources').re('\d+-\d+-\d+\s+\d+:\d+:\d+'))
        # item['content'] =sel.xpath('//div[@class="con"]//text()').extract()

        yield item






