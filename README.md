# database_factory

数据库工厂，抽象数据库统一接口，用工厂模式对接mongodb、sqlite等后端。

## 安装

```shell
git clone https://github.com/BZ-coding/database_factory utils/database_factory
```

## 使用

```python
from database_factory import DataBaseFactory

database = DataBaseFactory.get(database_type='pymongo', database_name='rss', sheet_name='rss', host='192.168.10.5',
                               port=27017)
print(database)
```
