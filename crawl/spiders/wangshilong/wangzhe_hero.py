from scrapy import Selector, Spider, Request
import json
from urllib.parse import urljoin

class hero(Spider):
    name = "hero"
    start_urls = [
        'https://pvp.qq.com/web201605/js/herolist.json'
    ]

    def parse(self, response):
        result = json.loads(response.text, encoding='gdk')
        for i in result:
            ename = i.get('ename')
            # cname = i.get('cname')
            detauil_url = urljoin('https://pvp.qq.com/web201605/herodetail/', str(ename)+'.shtml')
            yield Request(url=detauil_url, callback=self.content)

    def content(self, response):
        pass