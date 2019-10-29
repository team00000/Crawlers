from scrapy import Spider, Request
import json, re

from scrapy.spiders import CrawlSpider


class ImageSpider(CrawlSpider):
    name = "image"
    a = 30
    b = 0
    start_urls = ['https://image.so.com/zjl?ch=photography&sn='+str(a)+'&listtype=new&temp=1']
    def parse(self, response):
        result = json.loads(response.text)
        result = result.get('list')
        for li in result:
            image = li.get('qhimg_url')
            print(image)
            # yield Request(url=image, callback=self.parse_content)
        self.a += 30
        next_url = re.sub(r'sn=\d+', 'sn='+str(self.a), response.url)
        # yield Request(url=next_url, callback=self.parse)
        if response.status != 200:
            self.b += 1
            if self.b == 3:
                pass
        elif response.status == 200:
            yield Request(url=next_url, callback=self.parse)



    # def parse_content(self, response):




