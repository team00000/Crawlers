from scrapy.spiders.crawl import Rule,CrawlSpider,Request
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from crawl.items.News import NewsItem

# from scrapy.loader import ItemLoader




class Wrj_rules(CrawlSpider):
    name='wrj'
    allowed_domains=[]
    start_urls=['https://www.81uav.cn/uav-news/']
    rules = [
        Rule(LinkExtractor(allow=r'https://www.81uav.cn/uav-news/index-htm-page-\d+.html'),callback='parse_items',follow=True),
        # Rule(LinkExtractor(allow=r'https://www.81uav.cn/uav-news/\d+/\d+/\d+.html'),callback='parse_xqy')
    ]
    def parse_items(self,response):
        # items=ItemLoader(item=NewsItem(),response=response)
        items = NewsItem()
        sel=Selector(response)
        list=sel.css('div.news-list-box dl ul li')
        print(list)
        for lis in list:
            items['title']=''.join(lis.css('h5 a::text').extract())
            items['time']=''.join(lis.css('em::text').extract())
            items['txt']=''.join(lis.css('p::text').extract())
            items['biaoqian']=''.join(lis.css('i a::text').extract())
            if items['biaoqian']==None:
                continue
            print('标题：',items['title'])
            print('时间：',items['time'])
            print('简介：',items['txt'])
            print('标签：',items['biaoqian'])





    def parse_xqy(self,response):
        items=NewsItem()
        sel=Selector(response)
        items['title']=''.join(sel.css('h1::text').extract())
        items['time']=''.join(sel.css('div.view div::text').re('\d+-\d+-\d+'))
        items['txt']=sel.css('div.content ::text')
        print(items['title'])
        print(items['time'])
        print(items['txt'])
        yield items