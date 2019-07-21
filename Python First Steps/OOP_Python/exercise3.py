import re
import requests
import json
import datetime

def getOpenWeatherMapWeather(cityName):
    result = None
    resp = requests.get("http://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(cityName))
    jData = json.loads(resp.text)
    temp = jData['main']['temp'] - 273.15

    return temp


def getCheapTickets(origin = 'MOW', 
                    destination = 'MOW', 
                    depart_date = datetime.datetime.today().strftime('%Y-%m-%d'), 
                    one_way = False):
    result = None
    link = "http://min-prices.aviasales.ru/calendar_preload?origin={}&destination={}&depart_date={}&one_way={}"
    link = link.format(origin, destination, depart_date, one_way)
    resp = requests.get(link)
    jData = json.loads(resp.text)
    result = jData['best_prices'][0]
    print (result)

tickets = getCheapTickets('MOW', 'DBV')
print(tickets)
tickets = getCheapTickets('MOW', 'DBV', '2019-07-29', False)
print(tickets)

cityName = 'Moscow,ru'
weather = getOpenWeatherMapWeather(cityName)
print(weather)


#1. Напишите функцию получения IATA-кода города из его названия, 
#   используя API Aviasales для усовершенствования приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
#Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API (ссылка на значке «API-документация»). 
#Вам необходимо изучить раздел «API для определения IATA-кода».

def getIATACode(term, locale = 'ru'):
    result = None
    link = "http://autocomplete.travelpayouts.com/places2?term={}&locale={}&types[]=city"
    link = link.format(term, locale)
    resp = requests.get(link)
    jData = json.loads(resp.text)
    result = jData[0]['code']
    return result


code = getIATACode('москв')
print(code)