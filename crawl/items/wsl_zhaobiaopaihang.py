from scrapy import Field, Item


class ZhaoBiaopaihang(Item):
    # 标题
    title = Field()
    # 来源
    source = Field()
    # 作者
    author = Field()
    # 阅读次数
    readci = Field()
    # 发布时间
    time = Field()
    # 正文
    text = Field()
    # 所属行业
    hangye = Field()
