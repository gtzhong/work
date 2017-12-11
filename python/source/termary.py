'''
12-2 三元表达式

x>y ? x:y

#条件为真时返回的结果 if条件判断 else 条件为假时的返回结果

'''

x=2
y=1
r = x if x>y else y  # x>y 直接返回给x
print(r) #输出2


x=1
y=3

r = x if x>y else y  # x>y 直接返回给x
print(r) #输出3