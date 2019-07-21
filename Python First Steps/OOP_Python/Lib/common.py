import re
import requests

def getYandexWeather():
    resp = requests.get("https://yandex.ru")

    strPattern = '<a class="home-link home-link_black_yes(?:[ weather__grade]{0,})" aria-label="([^\"]+)" href='
    pattern = re.compile(strPattern)
    result = pattern.findall(resp.text)
    return result

