# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:28:42 2020

@author: ErshovAA
"""
import re, string
import json, pickle
from os import getcwd as current_path
from codecs import decode
from bs4 import BeautifulSoup
from scrapy.http.response.html import HtmlResponse
from enum import Enum
import requests
from items import InstagramUser
from scrapy.loader import ItemLoader


lamfun1 = lambda x, y: x.search(y).group().split(' ')[2][5:-1]
lamfun2 = lambda x: x.split('=')[1].replace('"', '')
start_url = "https://www.instagram.com"


class UserRelationshipStatus(Enum):
    SELF = 0
    FOLLOWER = 1
    FOLLOWING = 2


def savePersonViaPickle(person) -> str:
    result = None
    fullFileName = f'{current_path()}\\person.dat'
    try:
        with open(fullFileName, 'wb') as f:
            pickle.dump(person, f)

        print('Объект записан')
    except:
        print('Объект записать не удалось')
    result = fullFileName
    return result


def readPersonViaPickle(fileName) -> object:
    result = None
    try:
        with open(fileName, 'rb') as f:
            result = pickle.load(f)

        print('Объект считан')
    except:
        print('Объект прочитать не удалось')

    return result


def savePersonViaJson(person) -> str:
    result = None
    fullFileName = f'{current_path()}\\profile.json'
    try:
        with open(fullFileName, 'w') as f:
            json.dump(person, f)

        print('Объект записан')
        result = fullFileName
    except:
        print('Объект записать не удалось')
    
    return result


def readPersonViaJson(fileName) -> dict:
    result = dict()
    try:
        with open(fileName, 'r') as f:
            result = json.load(f)
    
        print('Объект считан')
    except:
        print('Объект прочитать не удалось')
    
    return dict(result)


def fetch_csrf_token(text) -> str:
    result = re.search('\"csrf_token\"\:\"\w+\"', text).group()
    return result.split(':').pop().replace(r'"', '')


def decode_text(text):
    escaped_text = decode(text, 'unicode_escape')
    pattern = re.compile('[\W_]+')
    printable_text = pattern.sub(escaped_text, string.printable)[62:]
    return printable_text


def get_device_id(text:str) -> str:
    patern = re.compile('\"device_id\":\"[\S]{36}\"')
    result = patern.search(text).group().split(':')[1][1:-1]
    return result


def get_access_tokens(text:str) -> str:
    patern = re.compile('script type=\"text/javascript\" src=\"\S+ConsumerLibCommons.js\S+\"')
    result = lamfun1(patern, text)
    response = requests.get(f'{start_url}{result}')
    
    patern = re.compile("e.instagramWebDesktopFBAppId='\d+'")
    result1 = patern.search(response.text).group().split('=')[1][1:-1]
    
    patern = re.compile("e.instagramWebDesktopClientToken='[\S]{32}'")
    result2 = patern.search(response.text).group().split('=')[1][1:-1]
    return dict({'instagramWebDesktopFBAppId': result1,
                 'instagramWebDesktopClientToken': result2, })


def get_profile_hash(text:str) -> str:
    """
    https://www.diggernaut.ru/blog/kak-parsit-stranitsy-saytov-s-avtopodgruzkoy-na-primere-instagram/
    """
    patern = re.compile('script type=\"text/javascript\" src=\"\S+ProfilePageContainer.js\S+\"')
    result = lamfun1(patern, text)
    response = requests.get(f'{start_url}{result}')
    patern = re.compile('const l=\"\S+\"')
    result = patern.search(response.text).group().split('=')[1][1:-1]
    return result
    

def get_consumer_hash(text:str) -> dict:
    patern = re.compile('script type=\"text/javascript\" src=\"\S+Consumer.js\S+\"')
    result = lamfun1(patern, text)
    response = requests.get(f'{start_url}{result}')
    patern = re.compile('const t=\"\S+\",n=\"\S+\"')
    result = patern.search(response.text).group().split(',')
    return dict({"followers_query_hash": lamfun2(result[0]),
                 "following_query_hash": lamfun2(result[1]),})
    
    
def get_user_common_info(response:HtmlResponse, username) -> dict:
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('meta', attrs={'property':'og:description'})
    text = data[0].get('content').split()
    user_data = re.search('{\"id\"\:\"\\d+\",\"username\"\:\"%s\"}' % username, response.text).group()
    user_id = json.loads(user_data).get('id')
    followers = 0
    following = 0
    full_name = text[-2]
    try:
        followers = int(text[0][:2])
        following = int(text[2][:2])
    except Exception as e:
        print(e)
    return dict({'identity': user_id, 
                 'full_name': full_name, 
                 'username': username, 
                 'followers': followers, 
                 'following': following, })
    