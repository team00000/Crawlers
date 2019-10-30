# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlPipeline(object):
    def process_item(self, item, spider):
        return item

from openpyxl import Workbook


class ExcelPipeline(object):
    def __init__(self):
        self.wb=Workbook()#实例化
        self.ws=self.wb.active#激活
        self.ws.append(['故事梗概','电影时长','上映时间','电影名字'])


    def process_item(self,item,spider):#这里的参数spider 实际上是Spider的实例，item就是主程序中的aiqiyifilm_info，模块自动识别为item
        line=[item['film_description'],item['full_time'],item['formatperiod'],item['film_name']]
        self.ws.append(line)
        self.wb.save('aiqiyi_film.xlsx')
        return item #pipline 必须返回迭代对象，或者异常值