# coding:utf-8

from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()

while True:
    os.system("clear")
    print(Fore.LIGHTBLUE_EX, "\n\t+----------------------+")
    print(Fore.LIGHTBLUE_EX, "\n\t| 欢迎使用新闻管理系统 |")
    print(Fore.LIGHTBLUE_EX, "\n\t+----------------------+")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t请输入操作编号：")
    if opt == "1":
        username = input("\n\t请输入用户名：")
        password = getpass("\n\t请输入密码：")
        result = __user_service.login(username=username, password=password)

        # 登录成功
        if result:
            # 获取当前登录用户的角色
            role = __user_service.search_user_role(username=username)
            os.system("clear")
            while True:
                if role == "新闻编辑":
                    print("新闻编辑菜单")
                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t请输入操作编号：")
                    if opt == "1":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作编号：")
                            if opt == "1":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_unapproved_count_page()
                                    result = __news_service.search_unapproved_list(page=page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              '\n\t%d\t%s\t%s\t%s' % (index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTRED_EX, "\n\t---------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t 当前第 %d 页/共 %d 页" % (page, count_page))
                                    print(Fore.LIGHTRED_EX, "\n\t---------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号：")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 10:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.update_unapproved_news(news_id=news_id)
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_count_page()
                                    result = __news_service.search_list(page=page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              '\n\t%d\t%s\t%s\t%s' % (index + 1, one[1], one[2], one[3]))
                                    print(Fore.LIGHTRED_EX, "\n\t---------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t 当前第 %d 页/共 %d 页" % (page, count_page))
                                    print(Fore.LIGHTRED_EX, "\n\t---------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t请输入操作编号：")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif 1 <= int(opt) <= 10:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.delete_news(news_id=news_id)
                    elif opt == "2":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t请输入操作编号：")
                            if opt == "back":
                                break
                            if opt == "1":
                                os.system("clear")
                                username = input("\n\t请输入用户名：")
                                password = getpass("\n\t请输入密码：")
                                confirm_password = getpass("\n\t确认您的密码：")
                                if password != confirm_password:
                                    print(Fore.RED, "\n\t两次密码不一致！( 3 秒后自动返回)")
                                    time.sleep(3)
                                    continue
                                email = input("\n\t请输入邮箱：")
                                result = __role_service.search_role_list()
                                for index in range(len(result)):
                                    one = result[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t请输入角色编号：")
                                role_id = result[int(opt) - 1][0]
                                __user_service.insert(username=username, password=password, email=email,
                                                      role_id=role_id)
                                print(Fore.GREEN, "\n\t用户创建成功。( 3 秒后自动返回)")
                                time.sleep(3)
                    elif opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
        else:
            print(Fore.RED, "\n\t登录失败！(3 秒后自动返回)")
            time.sleep(3)

    elif opt == "2":
        sys.exit(0)
