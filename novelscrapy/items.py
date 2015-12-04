# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    art_url = scrapy.Field()
    art_type = scrapy.Field()
    art_title = scrapy.Field()
    content = scrapy.Field()
    


