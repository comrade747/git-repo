import requests
import json

lst = ["Москва", "Париж", "Брюссель", "Ереван", "Пекин"]
maximum = 0

for city in lst:
    if len(city) > maximum:
        maximum = len(city)

for city in lst:
    link = "http://autocomplete.travelpayouts.com/places2?term="+city
    data = json.loads(requests.get(link).text)
    print(f"{city:<{maximum}} - {data[0]['code']}")
