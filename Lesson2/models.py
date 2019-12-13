# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:21:15 2019

@author: andre
"""
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


CategoriesGoods = Table('categories_goods', Base.metadata,
    Column('goodId', Integer, ForeignKey('goods.id')),
    Column('categoryId', Integer, ForeignKey('categories.id')))


StocksGoods = Table('stocks_goods', Base.metadata,
    Column('goodId', Integer, ForeignKey('goods.id')),
    Column('stockId', Integer, ForeignKey('stocks.id')))


class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    manufacturer = Column(String)
    categories = relationship('Category', secondary=CategoriesGoods, backref='Good')
    stocks = relationship('Stock', secondary=StocksGoods, backref='Good')
    
    def __init__(self, name, fullname, manufacturer):
        self.name = name
        self.fullname = fullname
        self.manufacturer = manufacturer


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    goods = relationship('Good', secondary=CategoriesGoods, backref='Category')
    
    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname

    
class Stock (Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    goods = relationship('Good', secondary=StocksGoods, backref='Stock')
    
    def __init__(self, name, fullname, startdate, enddate):
        self.name = name
        self.fullname = fullname
        self.startdate = startdate
        self.enddate = enddate

        
