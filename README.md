# database_factory

数据库工厂，抽象数据库统一接口，用工厂模式对接mongodb、sqlite等后端。

## 安装

```shell
git clone https://github.com/BZ-coding/database_factory utils/database_factory
```

```python
from utils.database_factory import DatabaseFactory

database_factory = DatabaseFactory(host='192.168.10.5', port=27017, model='pymongo')
database = database_factory.get(database_name='rss', sheet_name='rss')
print(database)
```
