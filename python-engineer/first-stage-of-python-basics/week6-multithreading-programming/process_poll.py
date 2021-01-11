# coding: utf-8

import os
import time
import multiprocessing


# multiprocessing.Pool(Processcount)  创建进程池对象
# pool_obj.apply_async(func, args)  将任务加入到进程池（异步）
# pool_obj.close()  关闭进程池
# pool_obj.join()  等待进程池进程结束

def work(count, lock):
    lock.acquire()
    print(count, os.getpid())
    time.sleep(5)
    lock.release()
    return 'result is %s, pid is %s' % (count, os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    manger = multiprocessing.Manager()
    lock = manger.Lock()
    pool_results = []
    for i in range(20):
        pool_result = pool.apply_async(func=work, args=(i, lock))
        # pool_results.append(pool_result)

    # for res in pool_results:
    #     print(res.get())

    pool.close()
    pool.join()
