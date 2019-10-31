import scrapy


class RenMingWang(scrapy.Item):
    title = scrapy.Field()
    send_time = scrapy.Field()
    source = scrapy.Field()