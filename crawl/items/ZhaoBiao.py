from scrapy import Field,Item
class ZhaoBiaoItem(Item):
    title=Field()
    hangye = Field()
    address=Field()
    time=Field()
    nei = Field()
import scrapy
