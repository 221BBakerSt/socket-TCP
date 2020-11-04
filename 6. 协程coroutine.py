from greenlet import greenlet
from time import sleep

# 计算密集型 -- 占用大量CPU资源 -- 用多进程可以使CPU多核同时工作
# IO密集型 -- 需要网络功能，大量时间都在等待网络数据 -- 用多线程或协程就够了，减少CPU的切换

def func1():
    for _ in range(5):
        print(111111)
        # 手动切换
        g2.switch()
        sleep(0.5)

def func2():
    for _ in range(5):
        print(222222)
        # 手动切换
        g1.switch()
        sleep(0.5)

g1 = greenlet(func1)
g2 = greenlet(func2)

g1.switch()

###########################################################################
import gevent

def func(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 自动识别耗时操作并切换协程
        gevent.sleep(1)

g1 = gevent.spawn(func, 5)
g2 = gevent.spawn(func, 5)
g3 = gevent.spawn(func, 5)
g1.join()
g2.join()
g3.join()
