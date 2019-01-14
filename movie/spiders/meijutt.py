# -*- coding: utf-8 -*-
import scrapy


class MeijuttSpider(scrapy.Spider):
    name = 'meijutt'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def parse(self, response):
        pass
