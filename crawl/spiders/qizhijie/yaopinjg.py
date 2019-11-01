from scrapy import Selector
from scrapy import Request
import scrapy

class YaoPinjg(scrapy.Spider):
    name='YPjg'
    start_urls=['https://ypk.familydoctor.com.cn/efficacy_42_0_0_0_0_1.html']
    def parse(self, response):
        sel=Selector(response)
        li=sel.css('div.text')
        for i in li:
            urls=''.join(i.css('h3 a::attr(href)').extract())
            yield Request(url=urls,callback=self.parse_ypjg)
        # next_url = sel.xpath('//div[@class="endPage"]/a[contains(text(),"下一页")]/@href').extract_first()
        # latest_url = sel.xpath('//div[@class="endPage"]/a[contains(text(),"尾页")]/@href').extract_first()
        # print(next_url)
        # if next_url!=latest_url:
        #     yield Request(url=next_url,callback=self.parse)

    def parse_ypjg(self,response):
        sel=Selector(response)
        name=''.join(sel.xpath('//div[@class="main"]/div[@class="info"]/table[@class="table-1"]/tr[1]/td/text()').extract())
        wenhao=''.join(sel.xpath('//div[@class="main"]/div[@class="info"]/table[@class="table-1"]/tr[2]/td/text()').extract())
        qiye=''.join(sel.xpath('//div[@class="main"]/div[@class="info"]/table[@class="table-1"]/tr[3]/td/a/text()').extract())
        shiying=''.join(sel.xpath('//div[@class="main"]/div[@class="info"]/table[@class="table-1"]/tr[4]/td/text()').extract())
        yongfa=''.join(sel.xpath('//div[@class="main"]/div[@class="detail"]/div[@class="info"]/table[@class="table-1"]/tr[4]/td/text()').extract())
        chengfen=''.join(sel.xpath('//div[@class="main"]/div[@class="detail"]/div[@class="info"]/table[@class="table-1"]/tr[5]/td/text()').extract())
        xingzhuang=''.join(sel.xpath('//div[@class="main"]/div[@class="detail"]/div[@class="info"]/table[@class="table-1"]/tr[6]/td/text()').extract())
        # print(name)
        # print(wenhao)
        # print(qiye)
        # print(shiying)
        # print(yongfa)
        # print(chengfen)
        # print(xingzhuang)



