# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem


class MeijuttSpider(scrapy.Spider):
    name = 'meijutt'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        # print(response.status_code, response.content, response.text)
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            # movie.xpath('./h5/a/text()').extract_first()
            name = movie.xpath('./h5/a/text()').extract()[0]
            # print(movie, name)

            item = MovieItem()
            item['name'] = name
            yield item