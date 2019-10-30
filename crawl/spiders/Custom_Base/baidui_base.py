from crawl.spiders.base_redis_spider import BaseRredis
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
import logging
import time
from scrapy import signals,Request
from scrapy.exceptions import DontCloseSpider
from scrapy.exceptions import NotConfigured
logger = logging.getLogger(__name__)
from urllib.parse import urljoin


class baseBaidu(BaseRredis):
    name = 'baidu_base'
    # allowed_domains=[]
    redis_key = 'baidu:start_url'
    start_urls=[
        'https://www.81uav.cn/uav-news/'
    ]
    default_page = 0
    custom_settings = {
        "SCHEDULER_DUPEFILTER_KEY":'{}'.format(name)
    }




        #raise DontCloseSpider

    def parse(self, response):
        sel = Selector(response)
        print('current url is ',response.url)
        details = sel.css('div.news-list-box ul h5 a::attr(href)').extract()
        for detail in details:
            yield Request(url=detail,callback=self.parse_item)
        #next page
        next_urls = sel.css('div.pages a::attr(href)').extract()
        next_url = urljoin(response.url,next_urls[-1])
        self.default_page +=1
        if self.default_page<5:
            yield Request(url=next_url,callback=self.parse)

    def parse_item(self,response):
        print(response.url,"########################################################33")

