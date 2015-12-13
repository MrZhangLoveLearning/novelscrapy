# -*- coding: utf-8 -*-
import model
import db_helper
import items
from scrapy.exceptions import DropItem
import logging
import connection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DropPipeLine(object):
	def process_item(self, item, spider):
		if item['art_url']:
			if db_helper.is_exist_url(item['art_url']) or item['art_title'].find(u"山寨") > 0:
				raise DropItem('the article had colocted %s' % item['art_url'])
			else:
				return item
		else:
			raise KeyError('the art_url in item should\'n bell null')

class NovelPipeline(object):
    def process_item(self, item, spider):
    	db_helper.save_art(item['art_url'], item['art_type'], item['art_title'], item['content'])
    	logging.warning('item saved %s'%item['art_url'])
    	raise DropItem('the article had saved %s'%item['art_url'])

