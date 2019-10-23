import scrapy


class QiyeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    kword = scrapy.Field()
    eve = scrapy.Field()