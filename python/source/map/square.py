'''
12-3 map

# 对数据的每个值进行平方
  方法一
  方法二
# ap与lambda
  上述传入两个参数
'''

# 对数据的每个值进行平方

list_x = [1,2,3,4,5,6,7,8]

def square(x):
    return x*x

##方法一

for x in list_x:
    print(square(x))

"""
输出
1
4
9
16
25
36
49
64
"""    

## 方法二
r = map(square,list_x)
print(r) # 输出: # <map object at 0x02AE2710>
print(list(r)) # 输出 :[1, 4, 9, 16, 25, 36, 49, 64]


# map与lambda

r = map(lambda x:x*x,list_x)
print(list(r)) # 输出 :[1, 4, 9, 16, 25, 36, 49, 64]


## 上述传入两个参数

list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6,7,8]
r = map(lambda x,y:x*x,list_x,list_y)
print(list(r))  # 输出 :[1, 4, 9, 16, 25, 36, 49, 64]

r = map(lambda x,y:x*x+y,list_x,list_y)
print(list(r))  # 输出 : [2, 6, 12, 20, 30, 42, 56, 72]


#list_y少了几个值
list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6]

r = map(lambda x,y:x*x+y,list_x,list_y)
print(list(r)) #输出 [2,6,12,20,30,42]  ,并不会报错,就是少输出对应的值


#list_x少了几个值
list_x = [1,2,3,4,5,6]
list_y = [1,2,3,4,5,6,7,8]

r = map(lambda x,y:x*x+y,list_x,list_y)
print(list(r)) #输出 [2,6,12,20,30,42]  ,并不会报错,就是少输出对应的值