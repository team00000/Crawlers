from scrapy_redis.spiders import RedisCrawlSpider
from scrapy import signals
from scrapy.exceptions import DontCloseSpider


class BaseRredis(RedisCrawlSpider):
    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        self.idle_number = 0
        self.idle_list = []
        self.idle_count = 0
        spider = super(BaseRredis, self).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        # crawler.signals.connect(spider.spider_idle,signal=signals.spider_idle)
        spider.setup_redis(crawler)
        return spider

    def spider_opened(self, spider):

        print("################open spider ##############")
        for url in self.start_urls:
            self.server.lpush(self.redis_key, url)

    def spider_idle(self, spider):
        self.idle_count += 1  # 空闲计数
        print("test0000000000000000000000:{}".format(self.idle_count))
        if self.idle_count < 10:
            raise DontCloseSpider

    def close(spider, reason):
        print("##################close #################")