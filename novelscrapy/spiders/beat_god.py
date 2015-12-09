# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from novelscrapy.items import NovelscrapyItem


class BeatGodSpider(CrawlSpider):
    name = 'beat_god'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E6%8B%A9%E5%A4%A9%E8%AE%B0&ie=utf-8&tab=good']

    rules = (
        # Rule(LinkExtractor(allow=('http://tieba.baidu.com/f\?kw=%E6%8B%A9%E5%A4%A9%E8%AE%B0&ie=utf-8&tab=good&cid=&pn=[0-9]*',),)),
        Rule(LinkExtractor(allow=r'/p/[0-9]*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        yield Request(response.url+'?see_lz=1', callback=self.parse_lz_item)


    def parse_lz_item(self, response):
        i = NovelscrapyItem()
        i['art_url'] = response.url
        i['art_type'] = u"择天记"
        i['art_title'] = response.xpath('//title/text()').extract()[0]
        i['content'] = u''.join(response.xpath("//div[@class='p_content ']/cc/div").extract())
        if i['art_title'].find(u'【择天记】') >= 0  :
            return i
        else:
            print 'this is not a good novel web'+i['art_url']
        # return i

    
