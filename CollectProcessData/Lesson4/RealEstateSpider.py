# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:58:26 2019

@author: andre
"""
import scrapy
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from RealEstateItem import AvitoREItem

#class AvitoRealEstateLoader(ItemLoader):
#    default_output_processor = Identity()


class AvitoRealEstateSpider(CrawlSpider):
    name = "avitorealestate"
    allowed_domains = ["avito.ru"]
    start_urls = [f"https://www.avito.ru/kazan/kvartiry/prodam?p={i}" for i in range(1, 101)]

    rules = (
        Rule(LinkExtractor(allow=('prodam')), callback='parse'),
    )

    def parse(self, response):
        hxs = Selector(response)
        links = hxs.xpath('//div[@class="snippet-title-row"]/h3[@class="snippet-title"]/a[@itemprop="url"]/@href')
        for url in links:
            yield response.follow(url, callback=self.parse_item)
    
    def parse_item(self, response):
        item = ItemLoader(AvitoREItem(), response)
        item.add_value('url', response.url)
        item.add_xpath('title', 'h1/span/text()')
        item.add_xpath('photos', '//div[contains(@class, "js-gallery-img-frame")]/@data-url')
        item.add_xpath('params', '//div[@class="item-params"]/ul[@class="item-params-list"]/li')
        yield item.load_item()
            
            