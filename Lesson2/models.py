# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:21:15 2019

@author: andre
"""
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func


Base = declarative_base()


CategoriesGoods = Table('categories_goods', Base.metadata,
    Column('good_id', Integer, ForeignKey('goods.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
    )


StocksGoods = Table('stocks_goods', Base.metadata,
    Column('good_id', Integer, ForeignKey('goods.id')),
    Column('stock_id', Integer, ForeignKey('stocks.id')),
    Column('start_date', DateTime(timezone=True), server_default=func.now()),
    Column('end_date', DateTime(timezone=True), server_default=func.now()),
    Column('price', Float, server_default=func.now())
    )

    
class Good (Base):
    __tablename__ = 'goods'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)
    manufacturer = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    
    categories = relationship('Category', secondary=CategoriesGoods, backref='Good')
    stocks = relationship('Stock', secondary=StocksGoods, backref='Good')

    def __init__(self, name, fullname, manufacturer):
        self.name = name
        self.full_name = fullname
        self.manufacturer = manufacturer
        
    def __repr__(self):
            return "<Good(id='%s', name='%s', full_name='%s', manufacturer='%s')>" % \
        (self.id, self.name, self.full_name, self.manufacturer)


class Category (Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    
    goods = relationship('Good', secondary=CategoriesGoods, backref='Category')
    
    def __init__(self, name, fullname):
        self.name = name
        self.full_name = fullname

    def __repr__(self):
            return "<Category(id='%s', name='%s', full_name='%s')>" % \
        (self.id, self.name, self.full_name)
    
class Stock (Base):
    __tablename__ = 'stocks'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)
    condition = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    
    goods = relationship('Good', secondary=StocksGoods, backref='Stock')
    
    def __init__(self, name, fullname):
        self.name = name
        self.full_name = fullname

    def __repr__(self):
            return "<Stock(id='%s', name='%s', full_name='%s')>" % \
        (self.id, self.name, self.full_name)
        
