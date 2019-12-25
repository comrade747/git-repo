# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:58:26 2019

@author: andre
"""

import scrapy
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from VacancyItem import HHVacancyItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#class HHVacancyLoader(ItemLoader):
#    default_output_processor = Identity()


class HHVacanciesSpider(CrawlSpider):
    handle_httpstatus_list = [301, 302,]
    name = "hhvacancies"
    allowed_domains = ["hh.ru"]
    #'https://www.hh.ru/search/vacancy?area=1&st=searchVacancy&page={i}'
    start_urls = [f"https://hh.ru/search/vacancy?area=1&page={i}" for i in range(1, 101)]


    def parse(self, response):
        hxs = Selector(response)
        items = hxs.xpath('//div[contains(@class, "vacancy-serp-item")]').extract()
#        pg_spec = hxs.xpath("//div[@class='vacancy-serp__vacancy']/b/div/text()").extract()[0].strip()
        for fld in items:
            item = ItemLoader(HHVacancyItem(), response)
            item.add_value('url', response.url)
            item.add_xpath('title', 'h1/span/text()')
            item.add_xpath('max_price', '//div[contains(@class, "vacancy-serp__vacancy")]/@data-url')
            item.add_xpath('org_name', '//div[@class="item-params"]/ul[@class="item-params-list"]/li')
            item.add_xpath('org_url', '//div[@class="item-params"]/ul[@class="item-params-list"]/li')
            yield item.load_item()

            
            