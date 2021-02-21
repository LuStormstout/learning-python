# coding:utf-8

from db.mysql_db import pool


class RoleDao:
    # 获取 Role 列表
    @staticmethod
    def search_role_list():
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id, role FROM t_role"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
