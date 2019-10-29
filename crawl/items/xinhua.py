from scrapy import Item,Field

class XinHuaItem(Item):
    title = Field()
    tim = Field()
    laiyuan = Field()
    every = Field()
    zebian = Field()