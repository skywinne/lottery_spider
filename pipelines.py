# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class Lottery3DPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='spider', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        lottery_date = item['date']
        issue = item['issue']
        blue1 = item['blue1']
        blue2 = item['blue2']
        blue3 = item['blue3']
        sql = "insert into lottery_3d(date, issue, blue1, blue2, blue3) VALUES(%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (lottery_date, issue, blue1, blue2, blue3,))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
