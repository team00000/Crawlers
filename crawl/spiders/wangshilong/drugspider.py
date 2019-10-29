from scrapy import Spider, Selector

class drugspider(Spider):
    name = "drug"
    start_urls = [
        'http://www.360kad.com/Spzt/www_yjjc.shtml?pageType=1'
    ]

    def parse(self, response):
        print(response.url)