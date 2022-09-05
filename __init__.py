# -*- coding: utf-8 -*-


class DatabaseFactory:
    def __init__(self, host, port, model="pymongo"):
        self.host = host
        self.port = port
        self.model = model

    def get(self, database_name, sheet_name):
        if self.model == "pymongo":
            from .database_pymongo import DataBasePyMongo
            return DataBasePyMongo(database_name=database_name, sheet_name=sheet_name, host=self.host, port=self.port)
        else:
            raise ValueError('model name: {} can not find.'.format(self.model))
            pass
