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
import scrapy_settings as sts
import project_settings as pss

#class HHVacancyLoader(ItemLoader):
#    default_output_processor = Identity()
            

class InstagramSpider(CrawlSpider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/']
    

    def data_parse(self, response:HtmlResponse, 
                   userStatus:pu.UserRelationshipStatus,
                   user_info:dict ):
        jdata = json.loads(response.text)['data']['user']
        cursor_id = ''
        hash_value = ''
        csrf_token = ''
        device_id = ''
        fb_app_id = ''

        item = ItemLoader(InstagramUser(), user_info)
        item.add_value('identity', int(user_info.get('identity')))
        item.add_value('username', user_info.get('username'))
        item.add_value('full_name', user_info.get('full_name'))

        if userStatus == pu.UserRelationshipStatus.FOLLOWER:
            if len(jdata['edge_followed_by']['edges']) == 0:
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                jdata = pu.readPersonViaJson('followers.json')['data']['user']
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            hash_value = user_info.get('followers_query_hash')
            param_name = 'edge_followed_by'
            profile_param = 'followers'
            related_param = 'following'
            
        if userStatus == pu.UserRelationshipStatus.FOLLOWING:
            if len(jdata['edge_follow']['edges']) == 0:
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                jdata = pu.readPersonViaJson('following.json')['data']['user']
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            hash_value = user_info.get('following_query_hash')
            param_name = 'edge_follow'
            profile_param = 'following'
            related_param = 'followers'
            
        users = jdata[param_name]['edges']
        cursor_data = jdata[param_name]['page_info']
            
        for usr in users:
            iusr = ItemLoader(InstagramUser(), usr)
            iusr.add_value('identity', int(usr['node']['id']))
            iusr.add_value('username', usr['node']['username'])
            iusr.add_value('full_name', usr['node']['full_name'])
            iusr.add_value(related_param, {'node': {'id': user_info.get('identity'),
                                                  'username': user_info.get('username'),
                                                  'full_name': user_info.get('full_name')}})
            yield iusr.load_item()

        item.add_value(profile_param, users)
        yield item.load_item()

        if cursor_data['has_next_page']:
            csrf_token = user_info.get('csrf_token')
            device_id = user_info.get('device_id')
            fb_app_id = user_info.get('instagramWebDesktopFBAppId')

            query_vars = {"id":user_info.get('identity'),
                        "include_reel":True,
                        "fetch_mutual":False,
                        "first":13, 
                        "after":cursor_data['end_cursor'], }

            header_vars = { 'referer': f'https://www.instagram.com/{pss.PROFILE}/{profile_param}/'
                     , 'sec-fetch-mode': 'cors'
                     , 'sec-fetch-site': 'same-origin'
                     , 'x-csrftoken': csrf_token
                     , 'x-ig-app-id': fb_app_id
                     #, 'x-ig-www-claim': 'hmac.AR3TihBiDn-8VpgpLKuRJkIFYKTuTovBB7CxmtPKXiPxO5h3'
                     , 'x-requested-with': 'XMLHttpRequest' 
                     , 'Connection': 'keep-alive'
                     , 'Host': 'www.instagram.com' }
            header_vars.update(sts.DEFAULT_REQUEST_HEADERS)

            url = f'{pss.GRAPHQL_URL}query_hash={hash_value}&variables={json.dumps(query_vars)}'
            yield scrapy.FormRequest(
                    url=url,
                    method='GET',
                    callback=self.data_parse,
                    headers=header_vars,
                    cb_kwargs={'userStatus': userStatus, 
                               'user_info': user_info, }
                    )

        
    def userdata_parse(self, response:HtmlResponse, user_info:dict):
        if user_info['followers'] == 0 and user_info['following'] == 0:
            return
        
        fwersqhash = user_info.get('followers_query_hash')
        fwingqhash = user_info.get('following_query_hash')
        csrf_token = user_info.get('csrf_token')
        device_id = user_info.get('device_id')
        fb_app_id = user_info.get('instagramWebDesktopFBAppId')
        
        query_vars = {"id":user_info.get('identity'),
                      "include_reel":True,
                      "fetch_mutual":True,
                      "first":24, }
        
        header_vars = { 'referer': f'https://www.instagram.com/{pss.PROFILE}/'
                     , 'sec-fetch-mode': 'cors'
                     , 'sec-fetch-site': 'same-origin'
                     , 'x-csrftoken': csrf_token
                     , 'x-ig-app-id': fb_app_id
                     #, 'x-ig-www-claim': 'hmac.AR3TihBiDn-8VpgpLKuRJkIFYKTuTovBB7CxmtPKXiPxO5h3'
                     , 'x-requested-with': 'XMLHttpRequest' 
                     , 'Connection': 'keep-alive'
                     , 'Host': 'www.instagram.com' }
        header_vars.update(sts.DEFAULT_REQUEST_HEADERS)
        
        if user_info['followers'] > 0:
            url = f'{pss.GRAPHQL_URL}query_hash={fwersqhash}&variables={json.dumps(query_vars)}'
            yield scrapy.FormRequest(
                    url=url,
                    method='GET',
                    callback=self.data_parse,
                    headers=header_vars,
                    cb_kwargs={'userStatus': pu.UserRelationshipStatus.FOLLOWER, 
                               'user_info': user_info, }
                    )
        
        if user_info['following'] > 0:
            query_vars.update ({ "fetch_mutual":False, })
            url = f'{pss.GRAPHQL_URL}query_hash={fwingqhash}&variables={json.dumps(query_vars)}'
            yield scrapy.FormRequest(
                    url=url,
                    method='GET',
                    callback=self.data_parse,
                    headers=header_vars,
                    cb_kwargs={ 'userStatus': pu.UserRelationshipStatus.FOLLOWING, 
                               'user_info': user_info, }
                    )

        
    def userprofile_parce(self, response:HtmlResponse, user_info:dict):
        uci = pu.get_user_common_info(response, user_info.get('username'))
        prflhash = pu.get_profile_hash(response.text)
        uci.update({"profile_query_hash": prflhash})
        consumer_hash = pu.get_consumer_hash(response.text)
        uci.update(consumer_hash)
        uci.update({'csrf_token': user_info.get('csrf_token'),})
        device_id = pu.get_device_id(response.text)
        uci.update({'device_id': device_id,})
        access_tokens = pu.get_access_tokens(response.text)
        uci.update(access_tokens)
        
        query_vars = {"user_id":uci.get('identity'),
                     "include_chaining":True,
                     "include_reel":True,
                     "include_suggested_users":False,
                     "include_logged_out_extras":False,
                     "include_highlight_reels":True,
                     "include_related_profiles":False, }

        url = f'{pss.GRAPHQL_URL}query_hash={prflhash}&variables={json.dumps(query_vars)}' 
        yield response.follow(
                    url,
                    self.userdata_parse,
                    cb_kwargs={'user_info': uci}
                    )
        
        
    def user_parse(self, response:HtmlResponse, csrf_token:dict):
        j_body = json.loads(response.text)
        if j_body.get('authenticated'):
            pss.USER_ID = int(j_body.get('userId'))
            user_info = dict({'username': pss.PROFILE, 
                              'csrf_token': csrf_token, })
            yield response.follow(
                    f'/{pss.PROFILE}',
#                    callback=self.userdata_parse,
                    callback=self.userprofile_parce,
                    cb_kwargs={'user_info': user_info}
                    )
        
        
    def parse(self, response:HtmlResponse):
        csrf_token = pu.fetch_csrf_token(response.text)
        yield scrapy.FormRequest(
            url=pss.LOGIN_URL, 
            method='POST',
            callback=self.user_parse,
            formdata={'username': pss.USER,
                      'password': pss.PWRD,},
            headers={'X-CSRFToken': csrf_token
                     , 'X-Instagram-AJAX':'1'
                     , 'Connection': 'keep-alive'
                     , 'X-Requested-With':'XMLHttpRequest',},
            cb_kwargs=dict({'csrf_token': csrf_token, })
                )
        
