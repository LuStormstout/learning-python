# coding:utf-8

from db.mysql_db import pool


class UserDao:

    # 验证用户登录
    @staticmethod
    def login(username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username = %s AND AES_DECRYPT(UNHEX(password),'HelloWorld') = %s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户角色
    @staticmethod
    def search_user_role(username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id = r.id WHERE u.username = %s"
            cursor.execute(sql, [username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 添加用户
    @staticmethod
    def insert(username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_user(username, password, email, role_id) " \
                  "VALUES(%s, HEX(AES_ENCRYPT(%s, 'HelloWorld')), %s, %s)"
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户总页数
    @staticmethod
    def search_count_page():
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*) / 10) FROM t_user"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户分页列表
    @staticmethod
    def search_user_list(page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT u.id, u.username, r.role FROM t_user u JOIN t_role r on u.role_id = r.id " \
                  "ORDER BY u.id " \
                  "LIMIT %s, %s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 修改用户信息
    @staticmethod
    def update_user(user_id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_user " \
                  "SET username = %s, password = HEX(AES_ENCRYPT(%s, 'HelloWorld')), email = %s, role_id = %s " \
                  "WHERE id = %s"
            cursor.execute(sql, (username, password, email, role_id, user_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 删除用户
    @staticmethod
    def delete_user(user_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id = %s"
            cursor.execute(sql, [user_id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
