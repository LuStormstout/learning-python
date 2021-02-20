# coding:utf-8

from db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

    def search_unapproved_list(self, page):
        result = self.__news_dao.search_unapproved_list(page=page)
        return result

    def search_unapproved_count_page(self):
        count_page = self.__news_dao.search_unapproved_count_page()
        return count_page
