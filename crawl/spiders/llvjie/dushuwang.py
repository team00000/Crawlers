# # -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from crawl.items.lj_dushuwang import NewsItem



class NewsSpider(Spider):
    name = 'news'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/news/86.html']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url)

    def parse(self, response):
        # 获取下一页的链接
        next_page_selector = response.xpath('//a[contains(text(),"下一页")]/@href')
        if next_page_selector:
            next_page_url = response.urljoin(next_page_selector.extract_first())
            print(next_page_url)
            # 生成请求 没有callback 默认为parse

            yield scrapy.Request(url=next_page_url,callback=self.content_parse)

    def content_parse(self,response):
        title = response.xpath('//h1/text()').extract_first()
        author = response.xpath('//div[@class="news-item hasImg"]/h3/a/text()').extract()[0]
        send_time = response.xpath('//div[@class="news-item-info"]/p/span/text()').extract()[1]
        content = '\n'.join(response.xpath('//div[@class="news-item hasImg"]/p/text()').extract())
        news_item = NewsItem()
        news_item['title'] = title
        news_item['author'] = author
        news_item['send_time'] = send_time
        news_item['content'] = content
        print(news_item['title'])
        yield news_item