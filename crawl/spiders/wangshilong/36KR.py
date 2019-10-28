from scrapy import Selector, Spider, Request
from urllib.parse import urljoin
from crawl.items.wsl_36KR import wsl_36KR
import json

class KRspider(Spider):
    name = '36KR'
    start_urls = [
        'https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&per_page=30'
    ]
    def parse(self, response):
        result = json.loads(response.text)
        for i in result['data']['items']:
            entity_id = i.get('entity_id')
            detauil_url = urljoin('https://36kr.com/p/', str(entity_id))
            yield Request(url=detauil_url, callback=self.content)


    def content(self, response):
        sel = Selector(response)
        item = wsl_36KR()
        item['title'] = sel.css('h1::text').extract_first()
        item['author'] = sel.xpath('//div[@class="article-title-icon common-width margin-bottom-40"]/a/text()').extract_first()
        item['text'] = ''.join(sel.xpath('//p//text()').extract()).strip()
        item['time'] = ''.join(sel.xpath('//span[@class="title-icon-item item-time"]/text()').re(r'\d+\w+'))
        yield item