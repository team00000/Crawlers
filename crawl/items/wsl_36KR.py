from scrapy import Field, Item

class wsl_36KR(Item):
    title = Field()
    author = Field()
    text = Field()
    time = Field()