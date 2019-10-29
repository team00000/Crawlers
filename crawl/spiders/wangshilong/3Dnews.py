from scrapy import Selector, Spider, Request
from urllib.parse import urljoin
from crawl.items.wsl_3Dnews import NewsItem
import re


class newspider(Spider):
    name = "news"
    start_urls = [
        'http://www.3dhoo.com/news'
    ]

    def parse(self, response):
        sel = Selector(response)
        # 详情页链接
        # detauil_urls = sel.css('div.dybk_div a::attr(href)').extract()
        # for detauil_url in detauil_urls:
        #     yield Request(url=detauil_url, callback=self.new_content)

        # 爬取内容
        item = NewsItem()
        item['title'] = sel.css('div.dybk_div a::text').extract()
        item['image'] = sel.css('div.new_postion a img::attr(src)').extract()
        item['source'] = sel.css('div.date_div span.color_blue::text').extract()
        item['time'] = sel.xpath('//div[@class="date_div"]/span/text()').re(r'\d+-\d+-\d+ \d+:\d+:\d+')
        item['liang'] = sel.xpath('//span[@class="color_blue"]/text()').re(r'^\d+$')
        item['daodu'] = sel.css('p.yd_p ::text').extract()
        item['biaoqian'] = sel.css('div.label_div span a::text').extract()
        yield item

        # 翻页
        next_url = sel.xpath('//div[@class="page"]/a[contains(text(), "下一页")]/@href').extract_first()
        number = sel.xpath('//div[@class="page"]/a[contains(text(), "下一页")]/@href').re(r'\d+')[0]
        if int(number) <= 3:
            next_url = urljoin(response.url, next_url)
            yield Request(url=next_url, callback=self.parse)
        # three_url = sel.xpath('//div[@class="page"]/a[contains(text(), "3")]/@href').extract_first()
        # three_url = urljoin(response.url, three_url)




    # def new_content(self, response):
    #     sel = Selector(response)
    #     item = NewsItem()
    #     item['title'] = sel.css('div.news_title h2::text').extract_first()
    #     if sel.xpath('//div[@class="news_main"]//img/@src').extract():
    #         item['image'] = sel.xpath('//div[@class="news_main"]//img/@src').extract()
    #     item['source'] = sel.css('span.first_zr ::text').extract_first()
    #     item['time'] = sel.xpath('//div[@class="date_div"]/span/text()').re(r'\d+-\d+-\d+ \d+:\d+:\d+')
    #     item['liang'] = sel.xpath('//span[@class="color_blue"]/text()').re(r'^\d+$')
    #     item['daodu'] = sel.css('div.review_div p::text()').extract_first()


