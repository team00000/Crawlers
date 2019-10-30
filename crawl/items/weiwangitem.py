from scrapy import Item,Field

class WeiwangItem(Item):
    name = Field()
    price = Field()
    displacement = Field()
    # transmission = Field()
    # level = Field()
    # type = Field()