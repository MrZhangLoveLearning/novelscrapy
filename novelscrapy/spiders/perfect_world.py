# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from novelscrapy.items import NovelscrapyItem


class PerfectWorldSpider(CrawlSpider):
    name = 'perfect_world'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E5%AE%8C%E7%BE%8E%E4%B8%96%E7%95%8C%E5%B0%8F%E8%AF%B4&ie=utf-8&tab=good']

    rules = (
        # Rule(LinkExtractor(allow=('http://tieba.baidu.com/f\?kw=%E5%89%91%E7%8E%8B%E6%9C%9D&ie=utf-8&tab=good&cid=&pn=[0-9]*',),)),
        Rule(LinkExtractor(allow=r'/p/[0-9]*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        yield Request(response.url+'?see_lz=1', callback=self.parse_lz_item)


    def parse_lz_item(self, response):
        i = NovelscrapyItem()
        i['art_url'] = response.url
        i['art_type'] = u"完美世界"
        i['art_title'] = response.xpath('//title/text()').extract()[0]
        i['content'] = u''.join(response.xpath("//div[@class='p_content ']/cc/div").extract())
        if i['art_title'].find(u"完美世界") >= 0:
            return i
        else:
            print 'this is not a good url：'+i['art_url']