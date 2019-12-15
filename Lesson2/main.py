# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:21:15 2019

@author: andre
"""


from models import Base, Good, Category, Stock, CategoriesGoods, StocksGoods
from database import x5rgDb
from datetime import datetime, timezone
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome import service
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.opera import options
    

def createBrowser ():
    _operaDriverLoc = os.path.abspath(r'c:\browser_drivers\operadriver_win32\operadriver.exe')  # Replace this path with the actual path on your machine.
    _operaExeLoc = os.path.abspath(r'C:\Program Files\Opera\65.0.3467.72\opera.exe')   # Replace this path with the actual path on your machine.

    webdriver_service = service.Service(_operaDriverLoc)
    webdriver_service.start()
    _remoteExecutor = webdriver_service.service_url
    _operaCaps = desired_capabilities.DesiredCapabilities.OPERA.copy()

    _operaOpts = options.ChromeOptions()
    _operaOpts._binary_location = _operaExeLoc

    # Use the below argument if you want the Opera browser to be in the maximized state when launching. 
    # The full list of supported arguments can be found on http://peter.sh/experiments/chromium-command-line-switches/
    _operaOpts.add_argument('--start-maximized')  

#    driver = webdriver.Remote(_remoteExecutor, 
#                              options = _operaOpts, 
#                              desired_capabilities = _operaCaps)
    driver = webdriver.Chrome(executable_path = _operaDriverLoc, 
                              chrome_options = _operaOpts, 
                              desired_capabilities = _operaCaps)

    driver.get('https://5ka.ru/special_offers/')
    return driver
    
    
def fillGoods (driver, db):

    catName = "Акционные товары"
    cat = Category(catName, "ВСЕ Акционные товары")
    rows = db.session.query(Category).filter_by(name=catName).all()
    if len(rows) == 0:
        db.session.add(cat)
    else:
        cat = rows[0]
    
#    elements = driver.find_elements_by_css_selector('div.sale-card__footer')
    elements = WebDriverWait(driver, timeout=5). \
        until(lambda x: x.find_elements_by_css_selector('div.sale-card__description-wrapper'))
#    elements = driver.find_elements_by_css_selector('div.sale-card__description-wrapper')
    for element in elements:
        name = element.find_element_by_css_selector('p.sale-card__title')
        date = element.find_element_by_css_selector('span.sale-card__date')
        good = Good(name.text, name.text, name.text)
        
        rows = db.session.query(Good).filter_by(name=name.text).all()
        if len(rows) == 0:
            cat.goods.append(good)

    db.session.transaction.commit()
#        print(f'{name.text} : {date.text}')

if __name__ == '__main__':
    connString = 'sqlite:///x5rg.sqlite'
    db = x5rgDb(Base, connString)

    cat = Category("Акционные товары", "ВСЕ Акционные товары")
    db.session.add(cat)
    
    driver = createBrowser()
    
    fillGoods (driver, db)

    time.sleep(5) #see the result
    if driver is not None:
        driver.quit()
#    good = Good("кефир", "Кефир Простоквашино 3.2%", "ООО Простоквашино")
#    cat = Category("кисломолочка", "Кисломолочные продукты")
#    db.session.add(cat)
#    cat.goods.append(good)
#    
#    good = Good("молоко", "Молоко Домик в деревне 3.2%", "ООО Домик в деревне")
#    cat.goods.append(good)
#    
#    good = Good("ряженка", "Молоко Вкуснотеево 5%", "ООО Вкуснотеево")
#    cat.goods.append(good)
#    
#    db.session.transaction.commit()
    
#    good = Good("пепси", "Пепси Кола", "ООО Пепси Ко")
#    cat = Category("газировка", "Газированная вода")
#    db.session.add(good)
#    good.categories.append(cat)
    
#    dt1 = datetime(2019, 9, 30, 18, 59, 39, tzinfo=timezone.utc)
#    fmt = '%a, %d %b %Y %H:%M:%S %z'
#    dt2 = datetime.strptime('Wed, 29 Jan 2020 18:59:39 +0300', fmt)
#    stock = Stock("новогодняя", "Новогодняя распродажа", dt1, dt2)
#    db.session.add(stock)
#    good = db.session.query(Good).filter_by(name="кефир").first()
#    stock.goods.append(good)
#    
#    db.session.transaction.commit()
#    
#    ourGood = db.session.query(Good).filter_by(name="кефир").all()
#    print(ourGood)
#    ourCateg = db.session.query(Category).filter_by(name="кисломолочка").all()
#    print(ourCateg)
#    cat_good = db.session.query(CategoriesGoods).all()
#    print(cat_good)
    
    stk_good = db.session.query(CategoriesGoods).all()
    print(stk_good)
    
