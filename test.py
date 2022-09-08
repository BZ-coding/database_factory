import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径
print(BASE_DIR)
sys.path.append(BASE_DIR)  # 添加路径

from database_factory import DatabaseFactory

database_factory = DatabaseFactory(host='192.168.10.5', port=27017, model='pymongo')
database = database_factory.get(database_name='rss', sheet_name='rss')
print(database)
