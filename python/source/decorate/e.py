'''
12-8 装饰器

特性 注解  

#对修改是封闭的,对扩展是开放的

## 如果有100个函数,都要输出时间那怎样处理呢?

方案F 带多个参数的装饰器
'''

import time

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper


@decorator
def f1(name1,type1):
    print('this is a function '+name1)
    print('this is a function '+type1)

@decorator
def f2(namme2,type2,level3):
    print('this is a function '+namme2)
    print('this is a function '+type2)
    print('this is a function '+level3)


f1('test1','type1')    


"""
输出
1512958953.4491835
this is a function test1
this is a function type1
""" 

f2('test2','type2','level3')    

"""
输出
1512958953.4501817
this is a function test2
this is a function type2
this is a function level3
""" 