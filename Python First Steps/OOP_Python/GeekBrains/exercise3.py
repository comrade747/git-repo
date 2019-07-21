import requests, json

def my_f():
    try:
        print('Введите название города')
        search1=str(input())
        search2='Сургут'
        link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+search1+"%20в%20"+search2
        #print(link)
        resp = requests.get(link)
        text = resp.text
        data = json.loads(text)
        #print(text)
        if text == '{}':
            print('В этом городе нет аэропорта или он не найден')
        else:
            print('IATA-код города', search1, '"', data["origin"]["iata"], '"')
    except KeyError:
        print('Введены некорректные данные')

my_f()
