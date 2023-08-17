import logging

from ._DataBase import DataBase


class DataBaseFactory:
    _map = {}

    @staticmethod
    def register(database_type: str, database_class):
        DataBaseFactory._map[database_type] = database_class
        logging.info(f"DatabaseFactory : register : database_type:{database_type} database_class:{database_class}")

    @staticmethod
    def get(database_type: str, **kwargs) -> DataBase:
        database_class = DataBaseFactory._map.get(database_type, None)
        if database_class is None:
            logging.error(f"DatabaseFactory : get : database_type:{database_type} is invalid.")
            return None

        return database_class(**kwargs)
