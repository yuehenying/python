# -*- coding: utf-8 -*-
import scrapy

# 创建scrapy.Item类型的DoubanItem类
class DoubanItem(scrapy.Item):
    # 定义scrapy.Field类型的item
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    evaluate = scrapy.Field()
    describe = scrapy.Field()
