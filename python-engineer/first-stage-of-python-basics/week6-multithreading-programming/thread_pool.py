# coding:utf-8

import os
import time
import threading

from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()


def work(i):
    # lock.acquire()
    print(i, os.getpid())
    time.sleep(1)
    # lock.release()
    return 'result is %s' % i


if __name__ == '__main__':
    print(os.getpid())
    t = ThreadPoolExecutor(2)
    result = []
    for i in range(20):
        t_result = t.submit(work, (i,))
        result.append(t_result)

    for res in result:
        print(res.result())
