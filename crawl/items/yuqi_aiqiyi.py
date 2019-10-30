import scrapy
from scrapy import Item,Field


class AiqiyiItem(Item):
    film_description=Field()#电影描述
    full_time=Field()#影片时长
    formatperiod=Field()#上映时间
    film_name=Field()#电影名称
