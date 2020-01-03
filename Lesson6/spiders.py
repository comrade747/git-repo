# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:58:26 2019

@author: andre
"""

import scrapy
import re, string
import json
from os import getcwd as current_path
from codecs import decode
from urllib.parse import urlencode
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from items import InstagramUser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http.response.html import HtmlResponse
from bs4 import BeautifulSoup

#class HHVacancyLoader(ItemLoader):
#    default_output_processor = Identity()


class InstagramSpider(CrawlSpider):
    name = "instagram"
    allowed_domains = ["instagram.com"]
    start_urls = ["http://instagram.com"]
    insta_login = 'd9976421'
    insta_passw = 'ddpA343Q'
    insta_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    insta_parse_user = 'gefestart'
    insta_graphql_url = 'https://www.instagram.com/graphql/query/?'
    query_hash = ''


    def fetch_user_id(self, text, username):
        result = re.search('{\"id\"\:\"\\d+\",\"username\"\:\"%s\"}' % username, 
                           text).group()
        return json.loads(result).get('id')
        
    def fetch_query_hash(self, text, username):
        # todo https://www.diggernaut.ru/blog/kak-parsit-stranitsy-saytov-s-avtopodgruzkoy-na-primere-instagram/
        return 'bd90987150a65578bc0dd5d4e60f113d'
    
    def fetch_csrf_token(self, text):
        result = re.search('\"csrf_token\"\:\"\w+\"', text).group()
        return result.split(':').pop().replace(r'"', '')
        

    def savePersonViaJson(self, person):
        result = None
        fullFileName = f'{current_path()}\\{self.insta_parse_user}.json'
        try:
            with open(fullFileName, 'w') as f:
                json.dump(person, f)
    
            print('Объект записан')
            result = fullFileName
        except:
            print('Объект записать не удалось')
        
        return result
    
    
    def decode_text(self, text):
        escaped_text = decode(text, 'unicode_escape')
        pattern = re.compile('[\W_]+')
        printable_text = pattern.sub(escaped_text, string.printable)[62:]
        return printable_text

    
    def data_parse(self, response:HtmlResponse, username):
        json_body = json.loads(response.text)
        self.savePersonViaJson(json_body)
        
    
    def user_follower_parse(self, response:HtmlResponse, username):
        pass
    
    
    def user_following_parse(self, response:HtmlResponse, username):
        pass
    
    
    def define_suggested_count(self, response:HtmlResponse):
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('meta', attrs={'property':'og:description'})
        text = data[0].get('content').split()
        followers = 0
        following = 0
        try:
            followers = int(text[0][:2])
            following = int(text[2][:2])
        except Exception as e:
            print(e)
        return dict({'followers': followers, 'following': following})
        
        
    def userdata_parse(self, response:HtmlResponse, username):
        s_Cnts = self.define_suggested_count(response)
        if s_Cnts['followers'] == 0 and s_Cnts['following'] == 0:
            return
        
        self.query_hash = self.fetch_query_hash(response.text, username)
        common_vars = {"fetch_media_count":0,
                      "fetch_suggested_count":30,
                      "ignore_cache":True,
                      "seen_ids":[],
                      "include_reel":True, }
        
        query_vars = common_vars.copy()
        query_vars.update ({
                "filter_followed_friends":True,
                "fetch_suggested_count":s_Cnts['followers'], })
        url = f'{self.insta_graphql_url}query_hash={self.query_hash}&{urlencode({"variables": query_vars})}'
        yield response.follow(
                url.lower().replace("%27", "%22").replace("+", ""),
                self.user_follower_parse,
                cb_kwargs={'username': self.insta_parse_user}
                )
        
        query_vars = common_vars.copy()
        query_vars.update ({
                "filter_following_friends":True,
                "fetch_suggested_count":s_Cnts['following'], })
        url = f'{self.insta_graphql_url}query_hash={self.query_hash}&{urlencode({"variables": query_vars})}'
        yield response.follow(
                url.lower().replace("%27", "%22").replace("+", ""),
                self.user_following_parse,
                cb_kwargs={'username': self.insta_parse_user}
                )
        
        
    def user_parse(self, response:HtmlResponse):
        j_body = json.loads(response.text)
        if j_body.get('authenticated'):
            yield response.follow(
                    f'/{self.insta_parse_user}',
                    callback=self.userdata_parse,
                    cb_kwargs={'username': self.insta_parse_user}
                    )
        
        
    def parse(self, response:HtmlResponse):
        csrf_token = self.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            url=self.insta_login_link, 
            method='POST',
            callback=self.user_parse,
            formdata={'username': self.insta_login, 'password': self.insta_passw},
            headers={'X-CSRFToken': csrf_token}
                )
        
