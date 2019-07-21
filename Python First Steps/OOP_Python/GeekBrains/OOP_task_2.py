import re
from bs4 import BeautifulSoup as bs

with (open("index.html", 'r', encoding='utf-8'))as f:
    s=f.read()


fid = re.compile("Нас уже\s+\d+\s+\d+\s+\d+\s+\w+[^<]")
print("Re.result= ",fid.findall(s))

soup = bs(s,"html.parser")
list=soup.find_all("span", class_="total-users")
for item in list:
    print("bs4.result=", item.string)


