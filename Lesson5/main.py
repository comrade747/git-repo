# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""

import scrapy.crawler as crwlr
from scrapy.settings import Settings
import settings
from VacanciesSpider import HHVacanciesSpider

    
if __name__ == '__main__':

    cr_settings = Settings()
    cr_settings.setmodule(settings)
    process = crwlr.CrawlerProcess(settings=cr_settings)
    process.crawl(HHVacanciesSpider)
    process.start()