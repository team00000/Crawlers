from scrapy import Spider,Selector,Request
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.loader import ItemLoader
import re,json,pymongo




# db = pymongo.MongoClient()['xinhuawang']["xinhua"]
class Cqcb(CrawlSpider):
    name = 'cqcb'
    start_urls = ['https://www.cqcb.com/xindiaocha/redian/index_4.json']
    # rules
    # allowed_domains = ['http://toutiao.com/']
    def parse(self, response):

        result = json.loads(response.text)
        # newslist = result.get('newslist').re('"titleurl":"(.*?)"')
        newslist = result.get('newslist')
        for i in newslist:
            titleurl ='https://www.cqcb.com' + i['titleurl']
            print("这里是parse函数================",titleurl)
            # for i in db.find({"url": url}):
            #     break
            # else:

            yield Request(url=titleurl, callback=self.parse_every)

    def parse_every(self, response):
            sel = Selector(response)
            print('这里是parse_every')
            url = response.url
            print(url,22222222222222)
            title = ''.join(sel.xpath('//div[@class="top_biaoti"]/h1/text()').extract())
            if not title:
                return
            source = ''.join(sel.xpath('//div[@class="top_fubiao"]/span[2]/text()').extract_first())
            author = ''.join(sel.xpath('//div[@class="top_fubiao"]/span[3]/text()').extract_first())
            time = ''.join(sel.xpath('//div[@class="top_fubiao"]/span[4]/text()').extract_first())
            content = ''.join(sel.xpath('//div[@class="article_text"]/p/text()').extract())
            # print(author)
            print(time)
            print(content)

            # i = ItemLoader(item=XinhuaItem(), response=response)
            #
            # i.add_value(field_name='url', value=url)
            # i.add_value(field_name='title', value=title)
            # i.add_value(field_name='time', value=time)
            # i.add_value(field_name='source', value=source)
            # i.add_value(field_name='content', value=content)
            # yield i.load_item()




