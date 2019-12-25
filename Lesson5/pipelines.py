# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""
from pymongo import MongoClient
import datetime


class HHVacanciesPipeline(object):
    db = None
    
    def __init__(self):
        client = MongoClient('mongodb://sysdba:masterkey@gbubuntu.tk:27017/')
        self.db = client['geekbrains'] 
        
        
    def process_item(self, item, spider):
        collection = self.db['HeadHunterVacancies']
        item.update(
                {'parse_date': datetime.datetime.now()})
        collection.insert_one(item)
        return item
