# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:58:26 2019

@author: andre
"""

import scrapy
import json
from urllib.parse import urlencode
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from items import InstagramUser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http.response.html import HtmlResponse
import projUtils as pu


#class HHVacancyLoader(ItemLoader):
#    default_output_processor = Identity()
            

class InstagramSpider(CrawlSpider):
    name = "instagram"
    allowed_domains = ["instagram.com"]
    start_urls = ["https://www.instagram.com"]
    insta_login = 'd9976421'
    insta_passw = 'ddpA343Q'
    insta_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    insta_parse_user = 'gefestart'
    insta_graphql_url = 'https://www.instagram.com/graphql/query/?'
    
    url_converter = lambda self, x: x.lower().replace("%27", "%22").replace("+", "")

    def add_users(self, users):
        for user_info in users:
            iusr = ItemLoader(InstagramUser(), user_info)
            iusr.add_value('identity', int(user_info['node']['id']))
            iusr.add_value('username', user_info['node']['username'])
            iusr.add_value('full_name', user_info['node']['full_name'])
            yield iusr.load_item()
            
            
    def data_parse(self, response:HtmlResponse, 
                   userStatus:pu.UserRelationshipStatus,
                   user_info:dict):
        jdata = json.loads(response.text)['data']['user']
        
        item = ItemLoader(InstagramUser(), jdata)
        item.add_value('identity', int(user_info.get('identity')))
        item.add_value('username', user_info.get('username'))
        item.add_value('full_name', user_info.get('full_name'))
        
        if userStatus == pu.UserRelationshipStatus.FOLLOWER and \
            len(jdata['edge_followed_by']['edges']) == 0:
            jdata = pu.readPersonViaJson('followers.json')['data']['user']
            users = jdata['edge_followed_by']['edges']
#            self.add_users(users)
            for user_info in users:
                iusr = ItemLoader(InstagramUser(), user_info)
                iusr.add_value('identity', int(user_info['node']['id']))
                iusr.add_value('username', user_info['node']['username'])
                iusr.add_value('full_name', user_info['node']['full_name'])
                yield iusr.load_item()
            
            item.add_value('followers', users)
            
        if userStatus == pu.UserRelationshipStatus.FOLLOWING and \
            len(jdata['edge_follow']['edges']) == 0:
            jdata = pu.readPersonViaJson('following.json')['data']['user']
            users = jdata['edge_follow']['edges']
#            self.add_users(users)
            for user_info in users:
                iusr = ItemLoader(InstagramUser(), user_info)
                iusr.add_value('identity', int(user_info['node']['id']))
                iusr.add_value('username', user_info['node']['username'])
                iusr.add_value('full_name', user_info['node']['full_name'])
                yield iusr.load_item()
                
            item.add_value('following', users)

        yield item.load_item()

        
    def userdata_parse(self, response:HtmlResponse, user_info:dict):
        if user_info['followers'] == 0 and user_info['following'] == 0:
            return

        fwersqhash = user_info.get('followers_query_hash')
        fwingqhash = user_info.get('following_query_hash')
        
        query_vars = {"id":user_info.get('identity'),
                      "include_reel":True,
                      "fetch_mutual":True,
                      "first":24, }
        
        if user_info['followers'] > 0:
            url = f'{self.insta_graphql_url}query_hash={fwersqhash}&{urlencode({"variables": query_vars})}'
            yield response.follow(
                    self.url_converter(url),
                    self.data_parse,
                    cb_kwargs={ 'userStatus': pu.UserRelationshipStatus.FOLLOWER, 'user_info': user_info }
                    )
        
        if user_info['following'] > 0:
            query_vars.update ({ "fetch_mutual":False, })
            url = f'{self.insta_graphql_url}query_hash={fwingqhash}&{urlencode({"variables": query_vars})}'
            yield response.follow(
                    self.url_converter(url),
                    self.data_parse,
                    cb_kwargs={ 'userStatus': pu.UserRelationshipStatus.FOLLOWING, 'user_info': user_info }
                    )
    
        
    def userprofile_parce(self, response:HtmlResponse, user_info:dict):
        uci = pu.get_user_common_info(response, user_info.get('username'))
        prflhash = pu.get_profile_hash(response.text)
        uci.update({"profile_query_hash": prflhash})
        consumer_hash = pu.get_consumer_hash(response.text)
        uci.update(consumer_hash)
        
        query_vars = {"user_id":uci.get('identity'),
                     "include_chaining":True,
                     "include_reel":True,
                     "include_suggested_users":False,
                     "include_logged_out_extras":False,
                     "include_highlight_reels":True,
                     "include_related_profiles":False, }
        url = f'{self.insta_graphql_url}query_hash={prflhash}&{urlencode({"variables": query_vars})}' 
        yield response.follow(
                    self.url_converter(url),
                    self.userdata_parse,
                    cb_kwargs={'user_info': uci}
                    )
        
        
    def user_parse(self, response:HtmlResponse):
        j_body = json.loads(response.text)
        if j_body.get('authenticated'):
            user_info = dict({'username': self.insta_parse_user, })
            yield response.follow(
                    f'/{self.insta_parse_user}',
#                    callback=self.userdata_parse,
                    callback=self.userprofile_parce,
                    cb_kwargs={'user_info': user_info}
                    )
        
        
    def parse(self, response:HtmlResponse):
        csrf_token = pu.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            url=self.insta_login_link, 
            method='POST',
            callback=self.user_parse,
            formdata={'username': self.insta_login,
                      'password': self.insta_passw,},
            headers={'X-CSRFToken': csrf_token,
                     'X-Instagram-AJAX':'1',
                     'X-Requested-With':'XMLHttpRequest',}
                )
        
