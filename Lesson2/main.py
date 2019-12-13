# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:21:15 2019

@author: andre
"""


from models import Base, Good, Category, Stock, CategoriesGoods, StocksGoods
from database import x5rgDb
    
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
    
    good = Good("пепси", "Пепси Кола", "ООО Пепси Ко")
    cat = Category("газировка", "Газированная вода")
    db.session.add(good)
    good.categories.append(cat)
    
    db.session.transaction.commit()
    
    ourGood = db.session.query(Good).filter_by(name="кефир").count()
    print(ourGood)
    ourCateg = db.session.query(Category).filter_by(name="кисломолочка").all()
    print(ourCateg)
    cat_good = db.session.query(CategoriesGoods).all()
    print(cat_good)