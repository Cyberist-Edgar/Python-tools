### pymysql 常用操作
```python
# -*- coding:utf-8 -*-

import pymysql


class Database:
    def __init__(self, db):
        self._db = db

    def create_table(self):
        connect = pymysql.connect("localhost", 'root', 'Edgar', self._db)
        cursor = connect.cursor()
        sql = "CREATE TABLE IF NOT EXISTS person(name varchar(20) not null , " \
              "age integer not null, city varchar(20)) "
        cursor.execute(sql)
        connect.commit()
        cursor.close()
        connect.close()

    def read(self):
        connect = pymysql.connect("localhost", 'root', 'Edgar', self._db)
        cursor = connect.cursor()
        sql = "SELECT * FROM person"
        cursor.execute(sql)
        connect.commit()
        result = cursor.fetchall()
        cursor.close()
        connect.close()
        return result

    def insert(self, name, age, city):
        connect = pymysql.connect("localhost", 'root', 'Edgar', self._db)
        cursor = connect.cursor()
        sql = "INSERT INTO person(name, age, city) VALUES('{}', '{}', '{}')".format(
            name, age, city)
        cursor.execute(sql)
        connect.commit()
        cursor.close()
        connect.close()

    def update_age(self, name, age):
        connect = pymysql.connect("localhost", 'root', 'Edgar', self._db)
        cursor = connect.cursor()
        sql = 'UPDATE person SET age=%d WHERE name="%s"' % (age, name)
        cursor.execute(sql)
        connect.commit()
        cursor.close()
        connect.close()

    def delete_name(self, name):
        connect = pymysql.connect("localhost", 'root', 'Edgar', self._db)
        cursor = connect.cursor()
        sql_1 = 'SELECT * FROM person WHERE name="%s"' % name
        cursor.execute(sql_1)
        if cursor.fetchall():
            sql = 'DELETE FROM person where name="%s"' % name
            cursor.execute(sql)
            connect.commit()
        else:
            print("No name %s" % name)
        cursor.close()
        connect.close()


if __name__ == '__main__':
    database = Database("edgar")
    # database.create_table()
    # database.insert("John jack", 18, 'hunan')
    # database.update_age("John jack", 20)
    database.delete_name('Edgar')
    database.delete_name('John jack')
    database.read()

```

> 使用的时候必须`先创建对应的数据库`