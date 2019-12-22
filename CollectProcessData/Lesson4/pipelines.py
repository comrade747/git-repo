# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""
from pymongo import MongoClient
import datetime


class AvitoRealEstatePipeline(object):
    
    def __init__(self):
        client = MongoClient('mongodb://sysdba:masterkey@gbubuntu.tk:27017/')
        self.db = client['geekbrains'] 
        
    def process_item(self, item, spider):
        collection = self.db["AvitoRealEstate"]
        item.update(
                {'parse_date': datetime.datetime.now()})
        #doc = collection.find_one({"url": item.fields['url']})
        #if doc is None:
        collection.insert_one(item)
        return item