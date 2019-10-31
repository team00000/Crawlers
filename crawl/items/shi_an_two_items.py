import scrapy


class ShiantwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#标题
    tim = scrapy.Field()#时间
    laiyuan= scrapy.Field()#来源
    zuozhe= scrapy.Field()#作者
    liuliang= scrapy.Field()#浏览量
    tishi= scrapy.Field()#核心提示
    every= scrapy.Field()#正文
    keywords= scrapy.Field()#关键字