# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class CrawlPipeline(object):
#     def process_item(self, item, spider):
#         return item
import pymongo
from scrapy.utils.project import get_project_settings
settings = get_project_settings()


class CrawlPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 有密码账号
        # self.client.admin.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])

        self.db = self.client[settings['MONGO_DB']]  # 库名
        self.coll = self.db[settings['MONGO_COLL']]  # 表名

    def process_item(self, item, spider):
        post = dict(item)  # 把item转化成字典形式
        self.coll.insert(post)
        return item