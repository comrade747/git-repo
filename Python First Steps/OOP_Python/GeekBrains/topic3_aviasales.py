import requests
import json

# origin = "MOW"
# link = "http://min-prices.aviasales.ru/calendar_preload?origin="+origin+"&destination=UFA&depart_date=2019-05-21&one_way=true"
#
# data = json.loads(requests.get(link).text)
# # print(data["best_prices"][3])
# print(data)

city_from = input("Город вылета:")
city_to = input("Город прилета:")
link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+city_from+"%20в%20"+city_to
data = json.loads(requests.get(link, verify=False).text)  #  Есть проблема с сертификатом, решил так обойти.
print(data)