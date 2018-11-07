# -*- coding: utf-8 -*-
import scrapy
from ..items import Lottery3DItem


class LotterySpider(scrapy.Spider):
    name = 'lottery'
    allowed_domains = ['zhcw.com']
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/3d/list_1.html']
    index = 1
    items = []

    def parse(self, response):
        node_list = response.xpath("//tr")
        node_list.pop(0)
        node_list.pop(0)
        node_list.pop()
        for node in node_list:
            item = Lottery3DItem()

            item["date"] = node.xpath("./td[1]/text()").extract_first()
            item["issue"] = node.xpath("./td[2]/text()").extract_first()
            item["blue1"] = node.xpath("./td[3]/em[1]/text()").extract_first()
            item["blue2"] = node.xpath("./td[3]/em[2]/text()").extract_first()
            item["blue3"] = node.xpath("./td[3]/em[3]/text()").extract_first()

            yield item

        self.index += 1
        next_url = "http://kaijiang.zhcw.com/zhcw/html/3d/list_{}.html".format(self.index)
        yield scrapy.Request(url=next_url, callback=self.parse)