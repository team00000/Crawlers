from scrapy import Field,Item

class ZhaoBiao(Item):
    #标题
    title=Field()
    #开始时间
    start_time=Field()
    #结束时间
    end_time=Field()
    #地址
    dizhi=Field()
    content=Field()



