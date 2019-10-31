from scrapy import Item
from scrapy import Field

class TousuItem(Item):
    # 投诉编号
    id = Field()
    # 投诉品牌
    pinpai = Field()
    # 投诉车系
    chexi = Field()
    # 投诉车型
    # 问题简述
    # 典型问题
    # 投诉状态
    # 投诉时间