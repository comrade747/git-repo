# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:24:01 2019

@author: andre
"""

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
    

def name_handler(item):
    pass
    
    
def url_handler(item):
    pass


def price_handler(item):
    pass


class HHVacancyItem(Item):
    """
    Заголовок вакансии
    URL объявления
    Описание вакансии
    Оклад
    Название организации разместившей объявление
    Url на страницу организации на HH
    """
    _id = Field()
    url = Field(output_processor=TakeFirst())
    title = Field(output_processor=TakeFirst())
    parse_date = Field()
    max_price = Field(input_processor=MapCompose(price_handler))
    org_name = Field(input_processor=MapCompose(name_handler))
    org_url = Field(input_processor=MapCompose(url_handler))
