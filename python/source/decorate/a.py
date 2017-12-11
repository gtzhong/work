'''

12-8 装饰器

特性 注解  

#对修改是封闭的,对扩展是开放的

## 如果有100个函数,都要输出时间那怎样处理呢?

方案A 最笨的方式
'''
import time
def f1():
    print('this is a function')

def f2():
    print('this is a function')

def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)    

"""
输出:
1512958352.50973
this is a function
1512958352.50973
this is a function
"""