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
        filt = {"identity": item['identity']}
        doc = self.collection.find_one(filt)
        if doc is None:
            self.collection.insert_one(item)
        else:
            if 'followers' in item:
                doc.update({ 'followers': item['followers'] })
            if 'following' in item:
                doc.update({ 'following': item['following'] })
                
            self.collection.replace_one(filter=filt, replacement=doc)
        return item

