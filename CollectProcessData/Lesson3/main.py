from bs4 import BeautifulSoup
import requests
import re
import Publication as pb
from pymongo import MongoClient


def persist_publications(client, publs):
    db = client['geekbrains']  
    collection = db[pb.Publication.__name__]
#    json_data = [item.__dict__ for item in publs]
#    collection.insert_many(json_data)
    for item in publs:
        doc = collection.find_one({"url": item.url})
        if doc is None:
            collection.insert_one(item.__dict__)


def get_publications(soup):
    result = []
    publs = soup.find_all(['a', 'li'], attrs={'class': 'post-item__title'})
    for html_publ in publs:
        publ = pb.Publication(html_publ)
        print(publ)
        result.append(publ)
    
    return result

if __name__ == '__main__':
    start_url = 'http://www.geekbrains.ru'
    next_url = start_url + '/posts?page=1'
    connString = 'mongodb://sysdba:xxx@gbubuntu.tk:27017/'
    client = MongoClient(connString)

    have_next_page = True
    while have_next_page:
        response = requests.get(next_url)
        soup = BeautifulSoup(response.text, 'lxml')
        publs = get_publications(soup)
        persist_publications(client, publs)
        
        next_url = start_url + soup.select_one('ul.gb__pagination'). \
            contents[0].nextSibling.contents[0].attrs['href']
        have_next_page = soup.select_one('ul.gb__pagination') is not None

    #print(soup.select_one('ul.gb__pagination'))

    