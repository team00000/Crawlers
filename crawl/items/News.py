#news item
from scrapy import Item,Field



class NewsItem(Item):
    title = Field()
    time = Field()
    txt = Field()
    biaoqian = Field()
