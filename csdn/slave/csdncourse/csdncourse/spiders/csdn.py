# -*- coding: utf-8 -*-
import scrapy
from csdncourse.items import CsdncourseItem
from scrapy_redis.spiders import RedisSpider

class CsdnSpider(RedisSpider):
    name = 'csdn'
    redis_key = 'csdnspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CsdnSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        #print(response.status)
        item = CsdncourseItem()
        item['title'] = response.css("h1::text").extract_first()
        item['hour'] = response.css("span.pinfo::text").extract_first()
        item['teacher'] = response.css("div.professor_name a::text").extract_first()
       	#item['teacher'] = response.re("<span>(.*?)¿ªÅÌ</span>")[0]
        item['fitpeople'] = response.re('<span class="for">(.*?)</span>')[0]
        item['learnnum'] = response.re('<span class="num">(.*?)</span>')[0]
        item['price'] = response.css("span.money::text").extract_first()
        item['outline'] = response.css("dt.clearfix.J_accordion_btn span::text").extract()
        print(item)
        yield item