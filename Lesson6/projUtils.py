# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:28:42 2020

@author: ErshovAA
"""
import re, string
import json
from os import getcwd as current_path
from codecs import decode
from bs4 import BeautifulSoup
from scrapy.http.response.html import HtmlResponse
from enum import Enum


class UserRelationshipStatus(Enum):
    SELF = 0
    FOLLOWER = 1
    FOLLOWING = 2


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


def readPersonViaJson(fileName):
    result = dict()
    try:
        with open(fileName, 'r') as f:
            result = json.load(f)
    
        print('Объект считан')
    except:
        print('Объект прочитать не удалось')
    
    return dict(result)


def fetch_query_hash(text):
    # todo https://www.diggernaut.ru/blog/kak-parsit-stranitsy-saytov-s-avtopodgruzkoy-na-primere-instagram/
    return 'c76146de99bb02f6415203be841dd25a'


def fetch_csrf_token(text):
    result = re.search('\"csrf_token\"\:\"\w+\"', text).group()
    return result.split(':').pop().replace(r'"', '')


def decode_text(text):
    escaped_text = decode(text, 'unicode_escape')
    pattern = re.compile('[\W_]+')
    printable_text = pattern.sub(escaped_text, string.printable)[62:]
    return printable_text


def get_user_common_info(response:HtmlResponse, username):
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('meta', attrs={'property':'og:description'})
    text = data[0].get('content').split()
    user_data = re.search('{\"id\"\:\"\\d+\",\"username\"\:\"%s\"}' % username, response.text).group()
    user_id = json.loads(user_data).get('id')
    followers = 0
    following = 0
    fullname = text[-2]
    try:
        followers = int(text[0][:2])
        following = int(text[2][:2])
    except Exception as e:
        print(e)
    return dict({'user_id': user_id, 
                 'fullname': fullname, 
                 'username': username, 
                 'followers': followers, 
                 'following': following, })