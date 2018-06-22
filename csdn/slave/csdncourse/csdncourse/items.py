# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdncourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    hour = scrapy.Field()
    teacher = scrapy.Field()
    fitpeople = scrapy.Field()
    learnnum = scrapy.Field()
    price = scrapy.Field()
    outline = scrapy.Field()
