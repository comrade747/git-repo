# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""
from pymongo import MongoClient
import datetime


class InstagramUsersPipeline(object):
    
    def __init__(self):
#        connection = MongoClient('raspberry', 27017)
        connection = MongoClient('gbubuntu.tk', 27017)
        connection.geekbrains.authenticate('sysdba', 'masterkey')
        self.collection = connection.geekbrains.InstagramUsers
        
        
    def process_item(self, item, spider):
        item.update( {'parse_date': datetime.datetime.now()} )

        doc = self.collection.find_one( {"idenity": item['idenity']} )
        if doc is None:
            self.collection.insert_one(item)
        else:
            pass
        
        return item

