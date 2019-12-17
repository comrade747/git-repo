import datetime
from bs4 import BeautifulSoup
import requests
import dateparser

class Publication(object):
    """Заголовок статьи, ссылка на статью, дата публикации (только дата без времени), Имя автора
    """
    _id = ''
    title = ''
    url = 'http://www.geekbrains.ru/posts'
    publication_date = datetime.datetime.now()
    writer = ''

    def __init__(self, htmlElement):
        start_url = 'http://www.geekbrains.ru/posts'
        self.url = start_url + htmlElement.attrs['href'][6:]

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        self.title = soup.find(['h1'], attrs={'class' : 'blogpost-title'}).text

        date_string = soup.find(['time'], attrs={'class' : 'text-md'}).text
        self.publication_date = dateparser.parse(date_string)
        
        self.writer = soup.find(['div'], attrs={'class' : 'text-lg text-dark'}).text

    def __repr__(self):
        return "<Publication(title='%s', publication_date='%s', writer='%s')>" % \
        (self.title, self.publication_date, self.writer)
