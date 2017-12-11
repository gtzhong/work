'''
12-8 装饰器

特性 注解  

#对修改是封闭的,对扩展是开放的

## 如果有100个函数,都要输出时间那怎样处理呢?

方案C @的精髓使用,使用原来的函数名调用即可
'''

import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print('this is a function')

@decorator
def f2():
    print('this is a function')


f1()
f2()


"""
输出
1512958638.1101754
this is a function
1512958638.1111763
this is a function
""" 