import scrapy
import  re
import logging
from scrapy.http import Request
from scrapy_redis.spiders import RedisCrawlSpider#用于进行分布式部署
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor#crawlspider中专门用于提取相关连接的工具
logger=logging.getLogger('jd')#日志输出,warning,不打印没有返回值

class JingdongSpider(RedisCrawlSpider):
    name = 'jingdong'
    allowed_domains = ['jd.com']


    rules=[Rule(LinkExtractor(allow=r"page=\d+?"),callback='parse_item',follow=True)]#将返回的htmlresponse 给到解析函数

    def parse_item(self, response):
        pattern = re.compile('page=(\d+?)', re.S)  # 这样就识别了目前爬取的列表的页数
        num = re.search(pattern, response.url).group(1)
        print('目前正在爬取的页数为%s' % (num))
        phone_items = response.xpath('//li[@class="gl-item"]')  # 列表页面中每一个产品的所在位置
        base_price_url = 'https://p.3.cn/prices/mgets?callback=jQuery%s&skuIds=J_%s'  # 以手机为例，一款手机有不同的sku,价格也不一样，sku价格是用jquery 的异步存储的方式
        for phone_item in phone_items:
            item = JdItem()  # 首先实例化
            item['jd_shop_name'] = phone_item.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract_first()  # 店铺名
            item['product_id'] = phone_item.xpath('.//div/@data-sku').extract_first()  # 提取的是商品的id
            item['jd_page_url'] = 'http://' + gl_item.xpath('.//div[@class="p-img"]/a/@href').extract_first()  # 商品详情页链接
            price_url = base_price_url % (item['product_id'], item['product_id'])  # 这样就获得了每一款sku的价格的链接
            jd_img_url = gl_item.xpath('.//img[@height="220"]/@src').extract_first()
            item['jd_img_url'] = 'https:' + jd_img_url  # 图片url
            yield Request(url=price_url, callback=self.parse_price, meta={'item': item})