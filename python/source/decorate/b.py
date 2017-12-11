'''
12-8 装饰器

特性 注解  

#对修改是封闭的,对扩展是开放的

## 如果有100个函数,都要输出时间那怎样处理呢?

方案B 对功能封装,调用输出
'''

import time
def f1():
    print('this is a function')

def f2():
    print('this is a function')


def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

f = decorator(f1)
f()

"""
输出
1512958509.4328873
this is a function


总体流程跟A方案是一样,没什么区别
""" 