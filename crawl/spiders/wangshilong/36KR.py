from scrapy import Selector, Spider, Request
from urllib.parse import urljoin
from crawl.items.wsl_36KR import wsl_36KR
import json

class KRspider(Spider):
    name = '36KR'
    start_urls = [
        'https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&b_id=70274&per_page=30'
    ]

    def parse(self, response):
        result = json.loads(response)
        # for res in result['data']:
        #     res
        pass









    # def parse(self, response):
    #     sel = Selector(response)
    #     detauil_urls = sel.xpath('//a[@class="article-item-title weight-bold"]/@href').extract()
    #     if len(detauil_urls) <= 40:
    #         for detauil_url in detauil_urls:
    #             detauil_url = urljoin(response.url, detauil_url)
    #             yield Request(url=detauil_url, callback=self.parse_content)
    #
    # def parse_content(self, response):
    #     item = wsl_36KR()
    #     sel = Selector(response)
    #     item['title'] = sel.css('h1::text').extract_first()
    #     item['author'] = sel.xpath('//a[@class="title-icon-item item-a"]/text()').extract_first()
    #     text = sel.xpath('//div[@class="common-width content articleDetailContent kr-rich-text-wrapper"]//p/text()').extract()
    #     item['text'] = ''.join(text).strip()
    #     item['time'] = sel.xpath('//span[@class="title-icon-item item-time"]/text()').re(r'\d+\w+')
    #     print(item['title'])