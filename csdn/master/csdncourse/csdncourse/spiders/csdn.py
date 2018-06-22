# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider,Rule  
from scrapy.linkextractors import LinkExtractor  
from csdncourse.items import MasterItem  

class CsdnSpider(CrawlSpider):  
    name = 'master'  
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/k'] 
    item = MasterItem()  

    #Rule是在定义抽取链接的规则
    rules = (  
        Rule(LinkExtractor(allow=('https://fang.5i5j.com/bj/loupan/n[0-9]+/',)), callback='parse_item',  
             follow=True),  
    )  

    def parse_item(self,response):  
        item = self.item  
        item['url'] = response.url  
        return item