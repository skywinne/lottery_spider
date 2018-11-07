# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Lottery3DItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 开奖日期
    date = scrapy.Field()
    # 期号
    issue = scrapy.Field()
    # 第一个蓝球号码
    blue1 = scrapy.Field()
    # 第二个蓝球号码
    blue2 = scrapy.Field()
    # 第三个蓝球号码
    blue3 = scrapy.Field()
