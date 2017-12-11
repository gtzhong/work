'''
12-8 装饰器

特性 注解  

#对修改是封闭的,对扩展是开放的

## 如果有100个函数,都要输出时间那怎样处理呢?

方案D 带一个参数的装饰器
'''

import time

def decorator(func):
    def wrapper(func_name):
        print(time.time())
        func(func_name)
    return wrapper


@decorator
def f1(name1):
    print('this is a function '+name1)

@decorator
def f2(namme2):
    print('this is a function '+namme2)


f1('test1')    


"""
输出
1512958781.7031183
this is a function test1
""" 