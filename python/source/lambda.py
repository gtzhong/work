'''
匿名函数 

lambda parameter_list:expression(表达式,不做复杂的业务逻辑)
与函数比较
'''

#与函数比较

def add(x,y):
    return x+y

##函数调用
print(add(3,5)) # 输出8

#匿名函数

f = lambda x,y:x+y
print(f(1,2)) # 输出3
 