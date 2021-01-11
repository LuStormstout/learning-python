# coding: utf-8

import multiprocessing
import time
import os


# multiprocessing.process(target, args) 返回一个进程对象
# process.start() 执行进程
# process.join() 阻塞进程
# process.kill() 杀死进程
# process.is_alive() 进程是否存活
#
# 通过进程模块执行的函数无法获取返回值
# 多个进程同时修改文件可能会出现错误（并发问题）

def work_a():
    for i in range(10):
        print(i, 'a', os.getpid())
        time.sleep(1)


def work_b():
    for i in range(10):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    a_process = multiprocessing.Process(target=work_a)
    # a_process.start()
    # a_process.join()
    b_process = multiprocessing.Process(target=work_b)
    # b_process.start()

    for p in (a_process, b_process):
        p.start()

    for p in (a_process, b_process):
        p.join()

    for p in (a_process, b_process):
        print(p.is_alive())

    print(time.time() - start)
    print('parent pid is %s' % os.getpid())
