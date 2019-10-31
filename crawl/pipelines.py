# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# class CrawlPipeline(object):
#     def process_item(self, item, spider):
#         return item

# mogon存入
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





















# mysql存入
# class FilePipeline(object):
#     def open_spider(self, spider):
#         self.db =pymysql.connect(host="localhost", user='root', password='1234', db='1704B', port=3306)
#         self.cursor= self.db.cursor()
#         sql = "CREATE TABLE bank(title text,send_time text,source text,keyword text)ENGINE=InnoDB DEFAULT CHARSET=utf8"
#         # 执行sql语句
#         self.cursor.execute(sql)
#     def process_item(self, item, spider):
#         self.cursor.execute('insert into bank(title,send_time,source,keyword)VALUES ("{}","{}","{}","{}")'.format(item['title'],item['send_time'],item['source'],item['keyword']))
#         self.db.commit()
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.db.close()