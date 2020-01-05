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
    start_urls = ["http://instagram.com"]
    insta_login = 'd9976421'
    insta_passw = 'ddpA343Q'
    insta_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    insta_parse_user = 'gefestart'
    insta_graphql_url = 'https://www.instagram.com/graphql/query/?'
    query_hash = ''


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
            item.add_value('followers', jdata['edge_followed_by']['edges'])
        if userStatus == pu.UserRelationshipStatus.FOLLOWING and \
            len(jdata['edge_follow']['edges']) == 0:
            jdata = pu.readPersonViaJson('following.json')['data']['user']
            item.add_value('following', jdata['edge_follow']['edges'])

        yield item.load_item()

        
    def userdata_parse(self, response:HtmlResponse, user_info:dict):
        uci = pu.get_user_common_info(response, user_info.get('username'))
        if uci['followers'] == 0 and uci['following'] == 0:
            return
        
        self.query_hash = pu.fetch_query_hash(response.text)
        query_vars = {"id":uci.get('user_id'),
                      "include_reel":True,
                      "fetch_mutual":True,
                      "first":24, }
        user_info.update({'identity': uci.get('user_id'),
                          'full_name': uci.get('full_name')})
        
        if uci['followers'] != 0:
            self.query_hash = 'c76146de99bb02f6415203be841dd25a'
            url = f'{self.insta_graphql_url}query_hash={self.query_hash}&{urlencode({"variables": query_vars})}'
            yield response.follow(
                    url.lower().replace("%27", "%22").replace("+", ""),
                    self.data_parse,
                    cb_kwargs={ 'userStatus': pu.UserRelationshipStatus.FOLLOWER, 'user_info': user_info }
                    )
        
        if uci['following'] != 0:
            self.query_hash = 'd04b0a864b4b54837c0d870b0e77e076'
            query_vars.update ({ "fetch_mutual":False, })
            url = f'{self.insta_graphql_url}query_hash={self.query_hash}&{urlencode({"variables": query_vars})}'
            yield response.follow(
                    url.lower().replace("%27", "%22").replace("+", ""),
                    self.data_parse,
                    cb_kwargs={ 'userStatus': pu.UserRelationshipStatus.FOLLOWING, 'user_info': user_info }
                    )
        
        
    def user_parse(self, response:HtmlResponse):
        j_body = json.loads(response.text)
        if j_body.get('authenticated'):
            user_info = dict({'username': self.insta_parse_user, })
            yield response.follow(
                    f'/{self.insta_parse_user}',
                    callback=self.userdata_parse,
                    cb_kwargs={'user_info': user_info}
                    )
        
        
    def parse(self, response:HtmlResponse):
        csrf_token = pu.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            url=self.insta_login_link, 
            method='POST',
            callback=self.user_parse,
            formdata={'username': self.insta_login, 'password': self.insta_passw},
            headers={'X-CSRFToken': csrf_token}
                )
        
