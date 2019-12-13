# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:21:15 2019

@author: andre
"""


from models import Base, Good, Category, Stock, CategoriesGoods, StocksGoods
from database import x5rgDb
from datetime import datetime, timezone
    
if __name__ == '__main__':
    connString = 'sqlite:///x5rg.sqlite'
    db = x5rgDb(Base, connString)
    
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
    
    stk_good = db.session.query(StocksGoods).all()
    print(stk_good)