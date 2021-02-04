# coding:utf-8

import mysql.connector.pooling

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "cptbtptp",
    "database": "demo"
}
# try:
#     pool = mysql.connector.pooling.MySQLConnectionPool(**config, pool_size=10)
#     con = pool.get_connection()
#     con.start_transaction()
#     cursor = con.cursor()
#     sql = "UPDATE t_emp SET sal = sal + %s WHERE deptno = %s"
#     cursor.execute(sql, (200, 20))
#     con.commit()
# except Exception as e:
#     if "con" in dir():
#         con.rollback()
#     print(e)

# try:
#     pool = mysql.connector.pooling.MySQLConnectionPool(**config, pool_size=10)
#     con = pool.get_connection()
#     con.start_transaction()
#     cursor = con.cursor()
#     sql = "DELETE e, d FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno WHERE d.deptno = 20"
#     # sql = "TRUNCATE TABLE t_emp"
#     cursor.execute(sql)
#     con.commit()
# except Exception as e:
#     if "con" in dir():
#         con.rollback()
#     print(e)


"""
循环执行 SQL 语句
游标对象中的 executemany() 函数可以反复执行一条 SQL 语句
    sql = "INSERT INTO t_dept(deptno, dname, loc) VALUES(%s, %s, %s)"
    data = [[100, "A部门", "北京"], [110, "B部门", "上海"]]
    cursor.executemany(sql, data)
"""
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(**config, pool_size=10)
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "INSERT INTO t_dept(deptno, dname, loc) VALUES(%s, %s, %s)"
    data = [[100, "A部门", "北京"], [110, "B部门", "上海"]]
    cursor.executemany(sql, data)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
