# coding:utf-8

import mysql.connector

"""
    创建数据库连接
    方法一
"""
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "cptbtptp",
    "database": "vega"
}
con = mysql.connector.connect(**config)

"""
    # 方法二
    con = mysql.connector.connect(
        host="localhost", port="3306",
        user="root", password="cptbtptp",
        database="vega"
    )
"""

"""
    游标（Cursor）
    MySQL Connector 里面的游标用来执行 SQL 语句，而且查询的结果集也会保存在游标之中
    cursor = con.cursor()
    cursor.execute(SQL语句)
"""
cursor = con.cursor()
sql = "SELECT username, email, role_id FROM t_user"
cursor.execute(sql)
for one in cursor:
    print(one[0], one[1], one[2])

"""
    SQL注入攻击案例
    SQL 注入攻击的危害
    由于 SQL 语句是解释型语言，所以在拼接 SQL 语句的时候，容易被注入恶意的 SQL 语句
"""
username = "1 OR 1=1"
password = "1 OR 1=1"
sql = "SELECT COUNT(*) FROM t_user WHERE username = " + username + \
      " AND AES_DECRYPT(UNHEX(password),'HelloWorld') = " + password
cursor.execute(sql)
print(cursor.fetchone()[0])

username = "1 OR 1=1"
password = "1 OR 1=1"
sql = "SELECT COUNT(*) FROM t_user WHERE username = %s" \
      " AND AES_DECRYPT(UNHEX(password),'HelloWorld') = %s"
cursor.execute(sql % (username, password))  # 直接拼接字符串到 SQL 语句中
print(cursor.fetchone()[0])

"""
    SQL 预编译机制
        预编译 SQL 就是数据库提前把 SQL 语句编译成二进制，这样反复执行同一条 SQL 语句的时候效率就会提升
        SQL > 编译为二进制 > 执行
        sql = "INSERT INTO t_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        
    SQL 预编译机制抵御注入攻击
        SQL语句编译的过程中，关键字已经被解析过了，所以向编译后的 SQL 语句传入参数，都被当作字符串处理，数据库不会解析其中注入的 SQL语句。
"""
username = "1 OR 1=1"
password = "1 OR 1=1"
sql = ("SELECT COUNT(*) FROM t_user WHERE username = %s "
       "AND AES_DECRYPT(UNHEX(password),'HelloWorld') = %s")
cursor.execute(sql, (username, password))  # 先把 SQL 预编译，再传入字符串。
print(cursor.fetchone()[0])

"""
    事务控制
        Connector 为我们提供了非常简单的事务控制函数
        con.start_transaction([事务的隔离级别])
        con.commit()
        con.rollback()
        
    异常处理
        try:
            con = mysql.connector.connect(...)
            [ con.start_transaction() ]
            ...
        except Exception as e:
            [ con.rollback() ]
            print(e)
        finally:
            if "con" in dir():
                con.close()
"""
try:
    con = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="cptbtptp",
        database="demo"
    )
    con.start_transaction()
    cursor = con.cursor()
    sql = "INSERT INTO t_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (9600, "赵娜", "SALESMAN", None, "1985-12-01", 2500, None, 10))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()

# 关闭数据库连接
con.close()
