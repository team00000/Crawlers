from scrapy import Field, Item

class NewsItem(Item):
    title = Field()
    image = Field()
    source = Field()
    time = Field()
    liang = Field()
    daodu = Field()
    biaoqian = Field()