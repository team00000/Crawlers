from scrapy import Field, Item

class hero_item(Item):
    hero_name = Field()
    tuijian_jineng = Field()
    money = Field()
    skin = Field()
    jineng = Field()
    ji_js = Field()