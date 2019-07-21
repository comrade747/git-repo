import urllib3
import bs4
import re

#Задание 1
try:
    url ='https://geekbrains.ru/company?tab=history#history'
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('GET', url).data
except Exception as e:
    print("что то пошло не так", e)
else:

    def findnumber(li):
        find = [re.search('\d+[\.,\d]*', val) for val in li]
        find = max([float(val.group().replace(',', '.')) for val in find])
        return find

    r = r.decode("utf-8")
    #print(r)
    li = re.findall('>([^>]*зарег[^<]*)<', r)
    print("найденный текст в тэгах\n", li)
    print("Задание 1: Всего определено:", findnumber(li), "млн")

    #Задание 2

    def checkval(val):
        return str(val.get("class")).find("gb-history-table__title") > 0 and val.get_text().find("зарег") > 0

    d = bs4.BeautifulSoup(r, "html.parser")
    li = [val.get_text() for val in d.find_all("div") if checkval(val)]
    print("найденный текст в тэгах\n", li)
    print("Задание 2: Всего определено:", findnumber(li), "млн")
