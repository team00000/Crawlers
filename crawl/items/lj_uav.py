import scrapy



class NewsItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    send_time = scrapy.Field()
    content = scrapy.Field()