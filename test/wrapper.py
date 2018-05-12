# coding:utf8

#既不需要侵入，也不需要函数重复执行
import time

def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")

def add(x,y,z):
    return z(x)+z(y)

def format_name(s):
    return s.upper()

def calc_prod(slt):
    def g():
        total = 1
        for each in slt:
            total = each * total
        return total
    return g

if __name__ == '__main__':
    print calc_prod([1,2,3,3])()