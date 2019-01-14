# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        # 爬虫部分在for循环中yield item，所以process_item方法会重复执行。
        # open(mode='a')追加模式，如果w模式的话会覆盖掉上次写的信息。
        with open('my_meiju.txt', 'a', encoding='utf-8') as f:
            f.write(str(item['name']) + '\n')
        return item
