# coding:utf-8

import time
import random
import threading  # 多线程

lists = ['django', 'python', 'flask', 'bs5', 'requests', 'tornado']

new_lists = []


def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_lists.append(new_data)
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print('old list length %s' % len(lists))
    t_list = []
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()

    print('old list:', lists)
    print('new list:', new_lists)
    print('new list length %s' % len(new_lists))
    print('time is %s' % (time.time() - start))
