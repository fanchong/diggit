#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename: database/dbhelper.py


import pymongo
from pymongo.son_manipulator import AutoReference, NamespaceInjector

HOST = "127.0.0.1"
PORT = 27017
MAX_POOL_SIZE = 2


class Database(object):
    def __init__(self):
        self.connection = pymongo.Connection(HOST, PORT, MAX_POOL_SIZE)
        self.db = self.connection["blade"]
        #self.db.add_son_manipulator(NamespaceInjector())
        self.db.add_son_manipulator(AutoReference(self.db))

    def insert(self, table, documents): 
        return self.db[table].insert(documents)


    def query(self, table, parameters, sort, offset, limit, fields=None):
        cursor = self.db[table].find(parameters, fields)\
            .skip(offset).limit(limit)
        cursor.sort(sort, pymongo.DESCENDING)
        return cursor


    def get_count(self, table, parameters):
        return self.db[table].find(parameters).count()


    def get_id(self, table):
        value = self.db["ids"].find_and_modify(
            {"name": table}, {"$inc": {"value": 1}}, new=True, upsert=True)
        return value["value"]


    def find_one(self, table, parameters):
        return self.db[table].find_one(parameters)


    def update(self, table, parameters, update, safe=True):
        return self.db[table].update(parameters, update, safe)

    
    def dereference(self, dbref):
        return self.db.dereference(dbref)


    def remove(self, table, parameters):
        self.db[table].remove(parameters)
