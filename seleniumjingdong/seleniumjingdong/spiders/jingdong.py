# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from seleniumjingdong.items import ProductItem

class JingdongSpider(Spider):
    name = 'jingdong'
    allowed_domains = ['www.jingdong.com']
    base_url = 'https://list.jd.com/list.html?cat='

    def start_requests(self):
        for keynum in self.settings.get('KEYNUM'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keynum)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('//div[@id="plist"]//li[@class="gl-item"]')
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(product.xpath('.//div[@class="p-price"]//strong[@class="J_price"]//i//text()').extract()).strip()
            item['name'] = ''.join(product.xpath('.//div[@class="p-name"]//em/text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[@class="p-shop"]//a/text()').extract()).strip()
            #item['image'] = "https:" + ''.join(product.xpath('.//div[@class="p-img"]//img/@src').extract()).strip()
            item['commitnum'] = product.xpath('.//div[contains(@class, "p-commit")]//strong//a/text()').extract_first()
            yield item