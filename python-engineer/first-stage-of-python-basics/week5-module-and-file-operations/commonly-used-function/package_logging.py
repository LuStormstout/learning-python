# coding: utf-8

import logging
import os


# logging.baseConfig()
#   参数：
#       level 日志输出等级 level=logging.DEBUG
#           日志等级：debug info warnning error critical
#       format 日志输出格式
#           常用的日志输出格式：format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
#           format 具体格式：
#               %(levelname)s 日志级别名称
#               %(pathname)s 执行程序的路径
#               %(filename)s 执行程序名（程序文件名称）
#               %(lineno)d 日志程序的当前行号
#               %(asctime)s 打印日志的时间
#               %(message)s 具体日志信息
#       filename 存储位置 filename='./test.log'
#       filemode 输出模式 filemode='a'


def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
        filename=path,
        filemode=mode
    )
    return logging


current_path = os.getcwd()
log_path = os.path.join(current_path, 'test.log')
log = init_log(log_path)

log.info('这是第一个记录的日志信息')
log.warning('这是一个警告日志')
log.error('这是一个错误的日志')
log.debug('这是一个 DEBUG 日志')  # 日志等级低于已经定义的 INFO 所以不会被记录
