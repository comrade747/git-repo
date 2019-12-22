from bs4 import BeautifulSoup, Tag
import requests
import re
import Publication as pb
from pymongo import MongoClient


def persist_publications(db, publs:list):
    collection = db[pb.Publication.__name__]
#    json_data = [item.__dict__ for item in publs]
#    collection.insert_many(json_data)
    for item in publs:
        doc = collection.find_one({"url": item.url})
        if doc is None:
            collection.insert_one(item.__dict__)


def get_publications(soup:BeautifulSoup):
    result = []
    publs = soup.find_all(['a', 'li'], attrs={'class': 'post-item__title'})
    for html_publ in publs:
        publ = pb.Publication(html_publ)
        print(publ)
        result.append(publ)
    return result

def getUrl(tag:Tag):
    result = 'http://www.geekbrains.ru'
    pattern = re.compile("(\/posts\?page=\d+)")
    pageUrl = tag.findAll(attrs={'href': pattern})[0].attrs['href']
    pageUrl = tag.select_one('li.active').next.next.next.findAll(attrs={'href': re.compile("(\/posts\?page=\d+)")})
    pageUrl = tag.select_one('li.active').next.next.next.attrs['href']
    return result + pageUrl

if __name__ == '__main__':
    start_url = 'http://www.geekbrains.ru'
    next_url = start_url + '/posts?page=1'
    connString = 'mongodb://sysdba:masterkey@gbubuntu.tk:27017/'
    client = MongoClient(connString)
    db = client['geekbrains'] 

    have_next_page = True
    i = 1
    while have_next_page:
        next_url = start_url + f'/posts?page={i}'
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'lxml')
        publs = get_publications(soup)
        persist_publications(db, publs)
        
        tag = soup.select_one('ul.gb__pagination')
        i = i + 1
        #next_url = getUrl(tag)
        #have_next_page = tag is not None
        have_next_page = i < 55


    