# coding:utf-8

import mysql.connector.pooling

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "cptbtptp",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(**__config, pool_size=10)
except Exception as e:
    print(e)
