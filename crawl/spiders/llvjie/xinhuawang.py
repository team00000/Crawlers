import scrapy
from scrapy import Selector,Request
from crawl.items.xinhua import XinHuaItem
import re,json

class XinHuaWangItem(scrapy.Spider):
    name = 'xhw'
    allowed_domains = []
    start_urls = ['http://qc.wa.news.cn/nodeart/list?nid=113352&pgnum=1&cnt=10&tp=1&orderby=1']

    def parse(self, response):
        rules = json.loads(response.text[1:-1])
        data = rules.get('data')
        data_list = data.get('list')
        for raw in data_list:
            url = raw.get('LinkUrl')
            # print(url)
            PubTime = raw.get('PubTime')
            title = raw.get('Title')
            # print(title)
            yield Request(url=url,callback=self.parse_content,meta={'PubTime':PubTime,'title':title})
            page_num = re.findall('pgnum=(\d+)', response.url)[0]
            next_page = int(page_num) + 1
            next_p = re.sub('pgnum=(\d+)', 'pgnum=' + str(next_page), response.url)
            yield Request(url=next_p, callback=self.parse)

    def parse_content(self,response):
        sel = Selector(response)
        # title = ''.join(bod.css('div.h-title::text').extract_first())
        # print(title)
        print(response.meta.get('title'))
        print(response.meta.get('PubTime'))
        tim = ''.join(sel.css('div.h-info span::text').re('\d+-\d+-\d+\s\d+:\d+:\d+'))
        laiyuan = ''.join(sel.xpath('//div[@class="h-info"]/span[2]//text()').extract())
        every = ''.join(sel.css('p::text').extract())
        zebian = ''.join(sel.css('span.p-jc::text').extract())
        print(laiyuan)
        print(every)
        print(zebian)