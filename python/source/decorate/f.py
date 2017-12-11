'''

特性 注解  

#对修改是封闭的,对扩展是开放的

## 如果有100个函数,都要输出时间那怎样处理呢?

12-12 装饰器 五

#带多个参数的装饰器优化
## 通杀变态的参数长度 func(*args,**kw)
'''

import time

def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
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


@decorator
def f3(namme2,type2,**kw):  #加入第三个参数 **kw
    print('this is a function '+namme2)
    print('this is a function '+type2)
    print(kw)

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


f3('test2','type2',a=1,b=2,c='123')   
"""
输出
1512959167.143935
this is a function test2
this is a function type2
{'a': 1, 'b': 2, 'c': '123'}
""" 