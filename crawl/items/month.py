from scrapy import Field,Item
class MonthItem(Item):
    title=Field()
    tupian = Field()
    laiyuan=Field()
    time=Field()
    yueduliang = Field()
    daodu = Field()
    biaoqian = Field()

class MonthItem1(Item):
    title = Field()
    zuozhe = Field()
    zhengwen = Field()
    time = Field()

