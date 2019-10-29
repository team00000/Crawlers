import scrapy
from scrapy import Item,Field

class JdItem(Item):
    d_img_url = Field()  # 商品图片url
    jd_page_url = Field()  # 详情页面url
    jd_product_price = Field()  # 商品价格
