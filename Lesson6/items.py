# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:24:01 2019

@author: andre
"""

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst

    
def users_handler(item):
    identity = int(item['node']['id'])
    username = item['node']['username']
    full_name = item['node']['full_name']
    return {'identity': identity, 'username': username, 'full_name': full_name, }


class InstagramUser(Item):
    _id = Field()
    identity = Field(output_processor=TakeFirst())
    username = Field(output_processor=TakeFirst())
    full_name = Field(output_processor=TakeFirst())
    parse_date = Field()
    followers = Field(input_processor=MapCompose(users_handler))
    following = Field(input_processor=MapCompose(users_handler))
    
