# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 00:00:01 2019

@author: andre
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

class x5rgDb:
    
    def __init__(self, base, connString):
        engine = create_engine(connString, echo=True)
        base.metadata.create_all(engine)
        session_db = sessionmaker(bind=engine)
        self.__session = session_db()
        
    @property
    def session (self):
        return self.__session
        