from scrapy import Selector, Spider, Request
import json, time
from urllib.parse import urljoin
from crawl.items.wsl_wangzhe_hero import hero_item

class hero(Spider):
    name = "hero"
    start_urls = [
        'http://news.4399.com/gonglue/wzlm/yingxiong/'
    ]

    def parse(self, response):
        # result = json.loads(response.text, encoding='gdk')
        sel = Selector(response)
        detauil_urls = sel.xpath('//ul[@id="hreo_list"]/li[@rel2="1"]/a/@href').extract()
        for detauil_url in detauil_urls:
            # print(detauil_url)
            yield Request(url=detauil_url, callback=self.content)

    def content(self, response):
        sel = Selector(response)
        item = hero_item()
        # 英雄名
        item['hero_name'] = sel.xpath('//div[@class="yxinfo fl"]/h1/text()').extract_first()
        # 推荐技能
        item['tuijian_jineng'] = sel.css('div.yxsxinfo span.sp2::text').extract_first()
        # 钱
        item['money'] = sel.css('p.sty3 span::text').extract()
        image_skin = sel.css('div#yxpicul')
        for i in image_skin:
            # 皮肤图片
            skin_image = i.css('div#yxpicul a img::attr(src)').extract()
            # 皮肤名字
            skin_name = i.css('div#yxpicul a img::attr(alt)').extract()
            item['skin'] = list(zip(skin_image, skin_name))
        # 自身技能
        zishen_jineng = sel.css('ul.tp')
        for i in zishen_jineng:
            # 技能图片
            ji_img = i.css('li img::attr(src)').extract()
            # 技能名字
            ji_name = i.css('li img::attr(alt)').extract()
            item['jineng'] = list(zip(ji_img, ji_name))
        # 技能介绍
        item['ji_js'] = sel.css('ul.cent li::text').extract()
        time.sleep(0.5)
        yield item

