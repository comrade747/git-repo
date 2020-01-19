# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:22:07 2019

@author: andre
"""
import datetime


class CasheMachineFileData:
    file_name = None
    cash_board_no = None
    parce_date = None

    def __init__(self, fName:str, cbn:str):
        self.file_name = fName
        self.cash_board_no = cbn
        self.parce_date = datetime.datetime.now()


    def SaveData(self, collection):
        filt = {"file_name": self.file_name}
        doc = collection.find_one(filt)
        if doc is None:
            record = self.__dict__.copy()
            record['cash_board_no'] = [self.cash_board_no]
            collection.insert_one(record)
        else:
            doc.update( {'parce_date': datetime.datetime.now()} )
            items = [ num for num in [self.cash_board_no] if num not in doc['cash_board_no'] ]
            if len(items) > 0:
                doc['cash_board_no'].extend(items)
                collection.replace_one(filter=filt, replacement=doc)
        
