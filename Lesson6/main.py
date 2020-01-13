# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre

Перед использованием необходимо авторизоваться пользователем в instagram и 
заменить параметр InstagramSpider.SESSION_ID на актуальный из запроса 
https://www.instagram.com/graphql/query/?query_hash=.... 
Google Chrome с режимом разработчика в помощь
"""

import scrapy.crawler as crwlr
from scrapy.settings import Settings
import settings
import spiders
    
if __name__ == '__main__':

    cr_settings = Settings()
    cr_settings.setmodule(settings)
    process = crwlr.CrawlerProcess(settings=cr_settings)
    process.crawl(spiders.InstagramSpider)
    process.start()
