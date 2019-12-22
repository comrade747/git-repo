# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:24:01 2019

@author: andre
"""

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
import logging
    

def cleaner_proto(values):
    if values[:2] == '//':
        return f'https:{values}'
    return values
    
    
def cleaner_params(item):
    result = item.split('">')[-1].split(':')
    key = result[0]
    value = result[-1].split('/span')[-1].split('</')[0][:-1]
    try:
        value = int(value)
    except Exception as ex:
        logging.exception(ex)
    return {key, value}


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