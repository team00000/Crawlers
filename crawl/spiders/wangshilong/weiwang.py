from scrapy import Spider, Selector, Request
from urllib.parse import urljoin
from crawl.items.weiwangitem import WeiwangItem

class weiwangspider(Spider):
    name = "weiwang"
    start_urls = [
        'https://price.pcauto.com.cn/price/nb643/'
    ]

    def parse(self, response):
        sel = Selector(response)
        bigdiv = sel.css('div.thBig')
        for div in bigdiv:
            carname = div.css('p.tit a::text').extract_first()
            url = div.css('p.tit a::attr(href)').extract_first()
            url = urljoin(response.url, url)
            canurl = response.xpath('//p[@class="lin linA"]/a[contains(text(), "参配")]/@href').extract_first()
            canurl = urljoin(response.url, canurl)
            yield Request(url=url, callback=self.car_content, meta={'carname': carname})
            yield Request(url=canurl, callback=self.can_content)
        # carname = response.css('p.tit a::text').extract()
        # urls = response.css('p.tit a::attr(href)').extract()


    def car_content(self, response):
        item = WeiwangItem()
        sel = Selector(response)
        item['name'] = response.meta.get('carname')
        item['price'] = sel.css('em.gf ::text').extract_first()
        item['displacement'] = sel.css('ul.des p em a::text').re(r'\d+.\d+L')
        # item['level'] = sel.css('p a::text').extract()[2]
        # item['transmission'] = sel.css('p a::text').extract[3]
        # item['type'] = sel.css('p a::text').extract[4]
        # print(item['name'], item['price'], item['displacement'])
        yield item

    def can_content(self, response):
        sel = Selector(response)

        pass