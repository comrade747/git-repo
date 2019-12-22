# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import settings
from RealEstateSpider import AvitoRealEstateSpider

    
if __name__ == '__main__':

    cr_settings = Settings()
    cr_settings.setmodule(settings)
    process = CrawlerProcess(settings=cr_settings)
    process.crawl(AvitoRealEstateSpider)
    process.start()
