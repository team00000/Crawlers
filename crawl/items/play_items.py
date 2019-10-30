import scrapy


class PlayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #标题
    tim = scrapy.Field() #时间
    jianjie = scrapy.Field() #简介
    kword = scrapy.Field() #关键字
    url = scrapy.Field() #详情页链接

    zuo = scrapy.Field() #正文
