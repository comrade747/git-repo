# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""
from pymongo import MongoClient
import datetime


class InstagramUsersPipeline(object):
    
    def __init__(self):
        connection = MongoClient('raspberry', 27017)
#        connection = MongoClient('gbubuntu.tk', 27017)
        connection.geekbrains.authenticate('sysdba', 'masterkey')
        self.collection = connection.geekbrains.InstagramUsers
        
        
    def process_item(self, item, spider):
        item.update( {'parse_date': datetime.datetime.now()} )
        filt = {"identity": item['identity']}
        doc = self.collection.find_one(filt)
        if doc is None:
            self.collection.insert_one(item)
        else:
            userStatus = 'followers'
            if userStatus in item:
                self.update_collection(userStatus, item, doc)
#                doc.update({ 'followers': item['followers'] })
            userStatus = 'following'
            if userStatus in item:
                self.update_collection(userStatus, item, doc)
#                doc.update({ 'following': item['following'] })

            self.collection.replace_one(filter=filt, replacement=doc)
        return item


    def update_collection(self, userStatus, item, doc):
        if userStatus in doc:
            items = [ user for user in item[userStatus] if user not in doc[userStatus] ]
            doc[userStatus].extend(items)
        else:
            items = item[userStatus]
            doc.update({ userStatus: items })