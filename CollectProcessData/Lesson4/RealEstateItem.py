# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:24:01 2019

@author: andre
"""

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from bs4 import BeautifulSoup

def cleaner_proto(value):
    result = value
    if value[:2] == '//':
        result = f'https:{value}'
    return result
    
    
def cleaner_params(item):
    soup = BeautifulSoup(item, 'lxml')
    result = soup.select_one('li.item-params-list-item').text
    params = result.split(':')
    return dict({params[0]: params[1]})


def dict_params(items):
    result = {}
    for itm in items:
        result.update(itm)
    return result


class AvitoREItem(Item):
    _id = Field()
    title = Field(output_processor=TakeFirst())
    url = Field(output_processor=TakeFirst())
    parse_date = Field()
    params = Field(input_processor=MapCompose(cleaner_params), output_processor=dict_params)
    photos = Field(input_processor=MapCompose(cleaner_proto))