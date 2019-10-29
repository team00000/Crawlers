# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class CrawlPipeline(object):
    def process_item(self, item, spider):
        return item


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