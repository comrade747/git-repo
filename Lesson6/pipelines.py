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
        self.followers = connection.geekbrains.GefestartFollowers
        self.following = connection.geekbrains.GefestartFollowing
        
    def process_item(self, item, spider):
        item.update( {'parse_date': datetime.datetime.now()} )
        
        if (type(item).__name__ == 'GefestartFollower'):
            doc = self.followers.find_one( {"idenity": item['idenity']} )
            if doc is None:
                self.followers.insert_one(item)
        
        if (type(item).__name__ == 'GefestartFollowing'):
            doc = self.following.find_one( {"idenity": item['idenity']} )
            if doc is None:
                self.following.insert_one(item)
        
        return item

