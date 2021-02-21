# coding:utf-8

from db.mysql_db import pool


class NewsDao:
    # 查询待审批新闻列表
    @staticmethod
    def search_unapproved_list(page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id = t.id JOIN t_user u ON n.editor_id = u.id " \
                  "WHERE n.state = %s ORDER BY n.create_time DESC LIMIT %s, %s"
            cursor.execute(sql, ("待审批", ((page - 1) * 10), 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询待审批新闻的总页数
    @staticmethod
    def search_unapproved_count_page():
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state = %s"
            cursor.execute(sql, ["待审批"])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 审批新闻
    @staticmethod
    def update_unapproved_news(news_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state = %s WHERE id = %s"
            cursor.execute(sql, ("已审批", news_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 获取所有新闻列表
    @staticmethod
    def search_list(page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username " \
                  "FROM t_news n JOIN t_type t ON n.type_id = t.id JOIN t_user u ON n.editor_id = u.id " \
                  "ORDER BY n.create_time DESC LIMIT %s, %s"
            cursor.execute(sql, (((page - 1) * 10), 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询新闻总页数
    @staticmethod
    def search_count_page():
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*)/10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 根据 ID 删除新闻
    @staticmethod
    def delete_news(news_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id = %s"
            cursor.execute(sql, [news_id])
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()
